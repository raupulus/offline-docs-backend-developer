"""
Fase 3 del pipeline: src/ → public/

Genera el sitio HTML estático a partir del markdown canónico. El
resultado se abre con doble clic desde file://, sin servidor y sin
conexión.

Restricciones que impone ese objetivo:

  * Todas las rutas son relativas. Nada que empiece por /.
  * Ningún recurso externo: ni CDN, ni tipografías remotas.
  * El resaltado de sintaxis se genera aquí con Pygments, no en el
    navegador. Cero JavaScript para colorear código.
  * Los enlaces .md del markdown se reescriben a .html.

    python3 -m scripts.docsync.build --in src --out public
    python3 -m scripts.docsync.build --source laravel
"""

from __future__ import annotations

import argparse
import html
import posixpath
import re
import shutil
import sys
from datetime import date
from pathlib import Path
from typing import Any

from .common import Config, Log, read_json
from .search import write_indexes

try:
    import markdown
    from markdown.extensions.codehilite import CodeHiliteExtension
    from markdown.extensions.toc import TocExtension
except ImportError:  # pragma: no cover
    sys.exit(
        "Falta python-markdown.\n"
        "  pip3 install markdown pygments --break-system-packages"
    )

try:
    from jinja2 import Environment, FileSystemLoader, select_autoescape
    from markupsafe import Markup
except ImportError:  # pragma: no cover
    sys.exit("Falta Jinja2.\n  pip3 install jinja2 --break-system-packages")

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("Falta PyYAML.\n  pip3 install pyyaml --break-system-packages")


RE_FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
RE_HREF_MD = re.compile(r'(href=")(?!https?://|mailto:|#)([^"]+?)\.mdx?(#[^"]*)?(")')
# Enlaces que la documentación original escribe como rutas del sitio
# oficial: /docs/{{version}}/container en Laravel, /commands/npm-config
# en npm. Sin traducir quedarían muertos al abrir el sitio en local.
RE_HREF_ABS = re.compile(r'(href=")(/[^"#]*)(#[^"]*)?(")')
RE_HEADING = re.compile(
    r'<h([23])[^>]*\bid="([^"]+)"[^>]*>(.*?)</h\1>', re.DOTALL
)
RE_TAG = re.compile(r"<[^>]+>")

ASSETS_DIR = "_assets"


# ── Utilidades ──────────────────────────────────────────────────────

def to_html_path(md_path: str) -> str:
    """tables/columns/getting-started.md → tables/columns/getting-started.html"""
    return re.sub(r"\.mdx?$", ".html", md_path)


def relative_prefix(depth: int) -> str:
    """Prefijo relativo para subir `depth` niveles. Nunca una ruta absoluta."""
    return "/".join([".."] * depth) if depth else "."


def rewrite_html_links(
    content: str,
    depth: int,
    pages: set[str],
    by_basename: dict[str, list[str]],
) -> str:
    """Ajusta los enlaces del cuerpo para que funcionen en local.

    Dos transformaciones:

    1. `.md` → `.html`, porque el markdown enlaza a ficheros markdown.

    2. Rutas absolutas del sitio oficial → páginas locales. Laravel
       escribe /docs/{{version}}/container y npm /commands/npm-config;
       tal cual quedarían muertas al abrir el sitio desde file://. Se
       intenta la ruta completa y, si no encaja, el nombre de fichero,
       pero solo cuando es inequívoco en la tecnología. Si no se puede
       resolver con certeza se deja como estaba: un enlace que no lleva
       a ninguna parte es menos dañino que uno que lleva al sitio
       equivocado sin avisar.
    """

    def md_to_html(match: re.Match) -> str:
        anchor = match.group(3) or ""
        return f"{match.group(1)}{match.group(2)}.html{anchor}{match.group(4)}"

    content = RE_HREF_MD.sub(md_to_html, content)

    up = relative_prefix(depth)

    def absolute(match: re.Match) -> str:
        target = match.group(2).strip("/")
        anchor = match.group(3) or ""
        if not target:
            return match.group(0)

        # Solo páginas de documentación, no imágenes ni descargas
        if "." in posixpath.basename(target) and not target.endswith(".html"):
            return match.group(0)

        candidate = target if target.endswith(".html") else f"{target}.html"

        if candidate not in pages:
            options = by_basename.get(posixpath.basename(candidate), [])
            if len(options) != 1:
                return match.group(0)
            candidate = options[0]

        return f"{match.group(1)}{up}/{candidate}{anchor}{match.group(4)}"

    return RE_HREF_ABS.sub(absolute, content)


def extract_headings(content: str) -> list[dict[str, Any]]:
    """Encabezados H2 y H3 para el índice lateral de la página."""
    headings = []
    for level, anchor, raw in RE_HEADING.findall(content):
        text = html.unescape(RE_TAG.sub("", raw)).strip()
        if text:
            headings.append({"level": int(level), "id": anchor, "text": text})
    return headings


def split_front_matter(text: str) -> tuple[dict[str, Any], str]:
    match = RE_FRONT_MATTER.match(text)
    if not match:
        return {}, text
    try:
        data = yaml.safe_load(match.group(1)) or {}
        if not isinstance(data, dict):
            data = {}
    except yaml.YAMLError:
        data = {}
    return data, text[match.end():]


def make_converter() -> markdown.Markdown:
    return markdown.Markdown(
        extensions=[
            "extra",           # tablas, bloques cercados, listas de definición
            "sane_lists",
            "admonition",
            CodeHiliteExtension(guess_lang=False, linenums=False),
            TocExtension(permalink="#", toc_depth="2-4"),
        ],
        output_format="html5",
    )


# ── Generación ──────────────────────────────────────────────────────

def flat_pages(toc: dict) -> list[dict]:
    """Todas las páginas en orden de lectura, para anterior y siguiente."""
    pages = []
    for section in toc.get("sections", []):
        for entry in section.get("pages", []):
            pages.append({**entry, "section": section.get("slug", "")})
    return pages


# Topes del menú lateral. El índice completo de cada tecnología está
# siempre en su portada y en el buscador, así que recortar aquí no
# esconde nada: solo evita repetirlo en cada página.
MAX_NAV_SECTIONS = 40
MAX_NAV_PAGES = 60


def _window(pages: list[dict], current_path: str, size: int) -> list[dict]:
    """Ventana de páginas alrededor de la actual."""
    if len(pages) <= size:
        return pages

    index = next(
        (i for i, p in enumerate(pages) if p.get("path") == current_path), 0
    )
    half = size // 2
    start = max(0, min(index - half, len(pages) - size))
    return pages[start:start + size]


def nav_for(toc: dict, current_section: str, current_path: str) -> dict:
    """Menú lateral de una página, recortado a un tamaño razonable.

    Emitir el índice completo en cada página crece al cuadrado. Con PHP
    (11.000 documentos, 193 secciones) eran ~900 KB de menú por página y
    9,6 GB de sitio; con JavaScript, 3 secciones de ~1.000 páginas, el
    problema es el mismo por el otro lado.

    Se aplican dos topes:

      * Si hay muchas secciones, solo se muestra la activa.
      * Si la sección activa tiene muchas páginas, se muestra una
        ventana alrededor de la actual.

    No se pierde información: la portada de cada tecnología lleva el
    índice íntegro y el buscador cubre todos los documentos.
    """
    all_sections = toc.get("sections", [])
    truncated_sections = len(all_sections) > MAX_NAV_SECTIONS

    sections = []
    for section in all_sections:
        pages = section.get("pages", [])
        slug = section.get("slug", "")
        active = slug == current_section

        if truncated_sections and not active:
            continue

        shown = _window(pages, current_path, MAX_NAV_PAGES) if active else []

        sections.append(
            {
                "title": section.get("title", slug),
                "slug": slug,
                "pages": shown,
                "first": pages[0] if pages else None,
                "count": len(pages),
                "partial": active and len(shown) < len(pages),
            }
        )

    return {
        "sections": sections,
        "truncated": truncated_sections
        or any(s["partial"] for s in sections),
        "total": sum(len(s.get("pages", [])) for s in all_sections),
    }


def build_technology(
    tech_dir: Path,
    out_dir: Path,
    env: Environment,
    built_at: str,
) -> dict | None:
    tech = tech_dir.name

    meta = read_json(tech_dir / "_meta.json")
    toc = read_json(tech_dir / "_toc.json")
    if not meta or not toc:
        Log.warn(f"{tech}: falta _meta.json o _toc.json, se omite")
        return None

    tech_out = out_dir / tech
    shutil.rmtree(tech_out, ignore_errors=True)
    tech_out.mkdir(parents=True, exist_ok=True)

    ordered = flat_pages(toc)
    by_path = {p["path"]: i for i, p in enumerate(ordered)}

    # Páginas existentes, para poder traducir las rutas absolutas que la
    # documentación original hereda de su sitio web
    pages = {
        to_html_path(d.relative_to(tech_dir).as_posix())
        for d in tech_dir.rglob("*.md")
    }
    by_basename: dict[str, list[str]] = {}
    for page_path in pages:
        by_basename.setdefault(posixpath.basename(page_path), []).append(page_path)

    converter = make_converter()
    page_template = env.get_template("page.html")
    written = 0

    for doc in sorted(tech_dir.rglob("*.md")):
        rel = doc.relative_to(tech_dir).as_posix()
        front, body = split_front_matter(
            doc.read_text(encoding="utf-8", errors="replace")
        )

        depth = len(Path(rel).parts) - 1

        converter.reset()
        content = rewrite_html_links(
            converter.convert(body), depth, pages, by_basename
        )

        # El autoescape de Jinja está activo a propósito para todo lo
        # que venga del front-matter. El cuerpo es la excepción: ya es
        # HTML generado por python-markdown a partir de un fichero local
        # de src/, así que se marca explícitamente como seguro.
        content = Markup(content)

        dest = tech_out / to_html_path(rel)
        dest.parent.mkdir(parents=True, exist_ok=True)

        tech_root = relative_prefix(depth)
        root = relative_prefix(depth + 1)

        index = by_path.get(rel)
        prev_page = ordered[index - 1] if index not in (None, 0) else None
        next_page = (
            ordered[index + 1]
            if index is not None and index + 1 < len(ordered)
            else None
        )

        page = {
            "title": front.get("title") or Path(rel).stem,
            "path": rel,
            "section": front.get("section", ""),
            "source_url": front.get("source_url"),
            "retrieved_at": front.get("retrieved_at"),
            "headings": extract_headings(content),
            "prev": prev_page,
            "next": next_page,
        }

        dest.write_text(
            page_template.render(
                page=page,
                meta=meta,
                toc=toc,
                nav=nav_for(toc, page["section"], rel),
                content=content,
                root=root,
                tech_root=tech_root,
                page_title=page["title"],
                built_at=built_at,
            ),
            encoding="utf-8",
        )
        written += 1

    # Portada de la tecnología
    (tech_out / "index.html").write_text(
        env.get_template("tech-index.html").render(
            meta=meta,
            toc=toc,
            root="..",
            tech_root=".",
            page_title=meta.get("name", tech),
            built_at=built_at,
        ),
        encoding="utf-8",
    )

    Log.ok(f"{meta.get('name', tech)}: {written} páginas")
    return meta


def copy_assets(assets_src: Path, out_dir: Path) -> None:
    dest = out_dir / ASSETS_DIR
    shutil.rmtree(dest, ignore_errors=True)
    dest.mkdir(parents=True, exist_ok=True)

    for item in assets_src.iterdir():
        if item.name.startswith("."):
            continue
        if item.is_file():
            shutil.copy2(item, dest / item.name)
        else:
            shutil.copytree(item, dest / item.name, dirs_exist_ok=True)

    # Hoja de estilos de Pygments para ambos temas. Se genera aquí para
    # no arrastrar un CSS a mano que se desactualice.
    try:
        from pygments.formatters import HtmlFormatter

        light = HtmlFormatter(style="default").get_style_defs(".codehilite")
        dark = HtmlFormatter(style="monokai").get_style_defs(".codehilite")
        (dest / "code.css").write_text(
            "/* Generado por Pygments. No editar a mano. */\n"
            f"{light}\n"
            "@media (prefers-color-scheme: dark) {\n"
            f":root[data-theme=\"auto\"] {dark.replace(chr(10), chr(10) + '  ')}\n"
            "}\n"
            f":root[data-theme=\"dark\"] {dark.replace(chr(10), chr(10) + '  ')}\n",
            encoding="utf-8",
        )
    except ImportError:
        Log.warn("Pygments no está instalado: el código no se resaltará")
        (dest / "code.css").write_text("/* Pygments no disponible */\n", encoding="utf-8")


def build_home(
    metas: list[dict],
    pending: list[str],
    out_dir: Path,
    env: Environment,
    built_at: str,
) -> None:
    technologies = sorted(metas, key=lambda m: m.get("name", "").lower())
    total = sum(m.get("documents", 0) for m in technologies)

    (out_dir / "index.html").write_text(
        env.get_template("index.html").render(
            technologies=technologies,
            pending=pending,
            total_docs=total,
            root=".",
            page_title="Documentación offline",
            built_at=built_at,
        ),
        encoding="utf-8",
    )
    Log.ok(f"Portada con {len(technologies)} tecnologías y {total} documentos")


def build_standalone_pages(
    out_dir: Path,
    env: Environment,
    built_at: str,
) -> None:
    """Compila páginas raíz informativas desde markdown a HTML."""
    pages = [
        ("LICENSES.md", "licenses.html", "Licencias y Atribución"),
        ("LEGAL.md", "legal.html", "Aviso Legal y Privacidad"),
    ]
    md = markdown.Markdown(
        extensions=[
            "extra",
            "tables",
            TocExtension(permalink=True),
            CodeHiliteExtension(guess_lang=False),
        ]
    )
    template = env.get_template("standalone.html")

    for src_name, dest_name, title in pages:
        src_path = Path(src_name)
        if not src_path.is_file():
            continue
        raw_md = src_path.read_text(encoding="utf-8")
        html_body = md.reset().convert(raw_md)
        (out_dir / dest_name).write_text(
            template.render(
                content=Markup(html_body),
                root=".",
                page_title=f"{title} · Documentación offline",
                built_at=built_at,
            ),
            encoding="utf-8",
        )
        Log.ok(f"Página informativa: {dest_name}")


# ── Orquestación ────────────────────────────────────────────────────

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="docsync.build",
        description="Genera el sitio HTML estático a partir de src/",
    )
    parser.add_argument("--config", default="sources.yaml")
    parser.add_argument("--in", dest="src", default="src")
    parser.add_argument("--out", dest="public", default="public")
    parser.add_argument("--templates", default="scripts/templates")
    parser.add_argument("--assets", default="scripts/assets")
    parser.add_argument("--source", help="Regenerar solo esta tecnología")
    args = parser.parse_args(argv)

    src_dir = Path(args.src)
    out_dir = Path(args.public)
    templates = Path(args.templates)
    assets = Path(args.assets)

    if not src_dir.is_dir():
        Log.error(f"No existe {src_dir}/. Ejecuta antes 'make normalize'.")
        return 1
    if not templates.is_dir():
        Log.error(f"No existen las plantillas en {templates}/")
        return 1

    config = Config.load(args.config)
    out_dir.mkdir(parents=True, exist_ok=True)
    built_at = date.today().isoformat()

    env = Environment(
        loader=FileSystemLoader(str(templates)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["to_html"] = to_html_path

    tech_dirs = sorted(
        d for d in src_dir.iterdir()
        if d.is_dir() and not d.name.startswith(".")
    )
    if args.source:
        tech_dirs = [d for d in tech_dirs if d.name == args.source]
        if not tech_dirs:
            Log.error(f"'{args.source}' no está en {src_dir}/")
            return 1

    Log.step(f"Generando el sitio en {out_dir}/")

    metas = []
    for tech_dir in tech_dirs:
        meta = build_technology(tech_dir, out_dir, env, built_at)
        if meta:
            metas.append(meta)

    if not metas:
        Log.error("No se generó ninguna tecnología")
        return 1

    Log.step("Índices de búsqueda")
    write_indexes(src_dir, out_dir, [m["id"] for m in metas])

    Log.step("Recursos estáticos")
    if assets.is_dir():
        copy_assets(assets, out_dir)
        Log.ok(f"Copiados a {out_dir}/{ASSETS_DIR}/")
    else:
        Log.warn(f"No existe {assets}/, el sitio saldrá sin estilos")

    # Al regenerar una sola tecnología hay que conservar el resto en la
    # portada, así que se releen los metadatos ya publicados.
    if args.source:
        for other in sorted(src_dir.iterdir()):
            if not other.is_dir() or other.name == args.source:
                continue
            extra = read_json(other / "_meta.json")
            if extra and (out_dir / other.name / "index.html").is_file():
                metas.append(extra)

    pending = sorted(
        source.name
        for sid, source in config.sources.items()
        if sid not in {m["id"] for m in metas}
    )

    Log.step("Portada")
    build_home(metas, pending, out_dir, env, built_at)

    Log.step("Páginas informativas")
    build_standalone_pages(out_dir, env, built_at)

    Log.step("Listo")
    Log.info(f"Abre {out_dir}/index.html en el navegador")
    return 0


if __name__ == "__main__":
    sys.exit(main())
