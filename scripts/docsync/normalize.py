"""
Fase 2 del pipeline: work/ → src/

Convierte lo descargado en markdown canónico: un front-matter YAML por
fichero, más _meta.json y _toc.json por tecnología.

El front-matter es lo que permite que el mismo fichero sirva a la web,
a `grep` y a un modelo de IA local: cada documento lleva consigo de qué
versión habla, de dónde salió y bajo qué licencia está.

No inventa valores. Si un dato no se puede obtener de la fuente, omite
la clave en lugar de rellenarla con algo falso.

    python3 -m scripts.docsync.normalize --in work --out src
    python3 -m scripts.docsync.normalize --source filament
"""

from __future__ import annotations

import argparse
import posixpath
import re
import shutil
import sys
from datetime import date
from pathlib import Path
from typing import Any

from .common import Config, Log, Source, read_json, write_json

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("Falta PyYAML.\n  pip3 install pyyaml --break-system-packages")


# ── Expresiones reutilizadas ────────────────────────────────────────

RE_FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
RE_H1 = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
RE_NUMERIC_PREFIX = re.compile(r"^\d{1,3}[-_.]")
RE_MDX_IMPORT = re.compile(r"^\s*(?:import|export)\s+.*?$\n?", re.MULTILINE)
RE_MDX_TAG = re.compile(r"</?[A-Z][A-Za-z0-9._]*(?:\s[^<>]*?)?/?>")
# Enlaces markdown a ficheros locales. Excluye URLs absolutas de forma
# explícita: hay documentación que enlaza a ficheros .md de GitHub y no
# hay que tocarlos.
RE_MD_LINK = re.compile(
    r"(\]\()(?!https?://|mailto:|//)([^)\s#]+\.mdx?)((?:#[^)]*)?\))"
)

# Enlaces de referencia:  [1]: ../04-schema.md#type
# Composer los usa mucho y no los cubre la expresión anterior, que solo
# entiende la forma en línea [texto](destino).
RE_MD_REF_LINK = re.compile(
    r"^([ \t]*\[[^\]]+\]:[ \t]*)(?!https?://|mailto:|//)([^\s#]+\.mdx?)((?:#\S*)?)[ \t]*$",
    re.MULTILINE,
)


# ── Utilidades de texto ─────────────────────────────────────────────

def split_front_matter(text: str) -> tuple[dict[str, Any], str]:
    """Separa el front-matter existente del cuerpo.

    Varias fuentes ya traen front-matter propio (npm y pnpm lo usan para
    Docusaurus). Se aprovecha su título en lugar de adivinarlo.
    """
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


def strip_mdx(text: str) -> str:
    """Elimina imports y componentes JSX, conservando el texto interior."""
    text = RE_MDX_IMPORT.sub("", text)
    text = RE_MDX_TAG.sub("", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


# Solo etiquetas de formato HTML de verdad. Un <NuxtLink> o un
# <ClientOnly> NO son maquetación: son el nombre del componente que
# documenta la página, y quitarlos deja el título vacío.
HTML_FORMAT_TAGS = (
    "br|wbr|code|em|strong|b|i|u|s|sup|sub|span|small|kbd|abbr|a|mark|q"
)
RE_HTML_TAG = re.compile(rf"</?(?:{HTML_FORMAT_TAGS})(?:\s[^>]*)?/?>", re.IGNORECASE)
RE_ANCHOR_SUFFIX = re.compile(r"\s*\{#[^}]*\}\s*$")
RE_MD_INLINE = re.compile(r"[`*_]")


def clean_title(text: str) -> str:
    """Quita del título lo que es maquetación, no texto.

    Vue escribe encabezados como
        Composition API: <br>Dependency Injection {#composition-api}
    El <br> es un salto visual y el {#...} es el ancla de VitePress.
    Ninguno de los dos debe acabar en el menú ni en la pestaña del
    navegador.

    En cambio los títulos de Nuxt son literalmente <NuxtLink>, el
    nombre del componente. Por eso solo se quitan etiquetas de formato
    conocidas, y si aun así el resultado queda vacío se devuelve el
    original: más vale un título con ruido que ninguno.
    """
    cleaned = RE_ANCHOR_SUFFIX.sub("", text)
    cleaned = RE_HTML_TAG.sub(" ", cleaned)
    cleaned = RE_MD_INLINE.sub("", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()

    if cleaned:
        return cleaned

    fallback = RE_ANCHOR_SUFFIX.sub("", text).strip()
    return fallback or text.strip()


def extract_title(body: str, existing: dict, fallback: str) -> str:
    """Título real del documento, por orden de fiabilidad."""
    for key in ("title", "sidebar_label"):
        value = existing.get(key)
        if isinstance(value, str) and value.strip():
            return clean_title(value)

    match = RE_H1.search(body)
    if match:
        return clean_title(match.group(1))

    # Último recurso: el nombre del fichero legible.
    # El generador antiguo hacía solo esto, y por eso 'http-client.md'
    # acababa mostrándose como "Http client".
    return fallback.replace("-", " ").replace("_", " ").strip().capitalize()


def slugify(name: str) -> str:
    name = RE_NUMERIC_PREFIX.sub("", name)
    return name.lower().replace("_", "-").strip("-")


# ── Mapeo de rutas ──────────────────────────────────────────────────

def target_path(source: Source, rel: Path) -> tuple[str, Path]:
    """Traduce la ruta de origen a (sección, ruta destino relativa).

    Filament entrega packages/<paquete>/docs/<fichero>.md; se quiere
    <paquete>/<fichero>.md, así que los segmentos puramente
    estructurales se descartan.

    Los prefijos numéricos de ordenación se quitan tanto de los
    ficheros como de los directorios: Filament los usa en ambos
    (docs/02-columns/01-getting-started.md).
    """
    drop = set(source.get("drop_segments") or ["docs", "content"])
    strip_prefixes = source.get("strip_numeric_prefix", True)

    parts = []
    for part in rel.parts[:-1]:
        if part in drop:
            continue
        parts.append(slugify(part) if strip_prefixes else part)

    stem = rel.stem
    if strip_prefixes:
        stem = RE_NUMERIC_PREFIX.sub("", stem)
    stem = slugify(stem) or rel.stem

    if parts:
        section = parts[0]
        dest = Path(*parts) / f"{stem}.md"
    else:
        section = ""
        dest = Path(f"{stem}.md")

    return section, dest


def order_of(rel: Path, index: int) -> int:
    """Orden del documento dentro de su sección."""
    match = RE_NUMERIC_PREFIX.match(rel.name)
    if match:
        return int(re.sub(r"\D", "", match.group(0)))
    return (index + 1) * 10


# ── Recolección ─────────────────────────────────────────────────────

def collect(source: Source, work_dir: Path) -> tuple[Path, list[Path]]:
    root = work_dir / source.id
    prefix = source.get("strip_prefix")
    if prefix:
        candidate = root / prefix
        if candidate.is_dir():
            root = candidate
        else:
            Log.warn(f"strip_prefix '{prefix}' no existe; se usa la raíz")

    patterns = source.get("include") or ["*.md"]
    excludes = {e.lower() for e in (source.get("exclude") or [])}

    found: list[Path] = []
    for pattern in patterns:
        found.extend(root.rglob(pattern))

    files = []
    seen = set()
    for path in sorted(found):
        if not path.is_file() or path in seen:
            continue
        seen.add(path)
        rel = path.relative_to(root)
        if rel.name.lower() in excludes or str(rel).lower() in excludes:
            continue
        # Restos de los propios repositorios que no son documentación
        if any(part in {".git", "node_modules", "vendor"} for part in rel.parts):
            continue
        files.append(path)

    return root, files


# ── Normalización de una fuente ─────────────────────────────────────

def normalize_source(
    source: Source,
    work_dir: Path,
    src_dir: Path,
    lock: dict,
) -> dict | None:
    root = work_dir / source.id
    if not root.is_dir():
        Log.warn(f"{source.name}: sin descargar, ejecuta antes 'make fetch'")
        return None

    base, files = collect(source, work_dir)
    if not files:
        Log.warn(f"{source.name}: no se encontró ningún markdown en {base}")
        return None

    out_root = src_dir / source.id
    shutil.rmtree(out_root, ignore_errors=True)
    out_root.mkdir(parents=True, exist_ok=True)

    meta_lock = lock.get(source.id, {})
    commit = meta_lock.get("commit", "")
    ref = source.get("ref")
    version = source.expect.get("version") or (ref if ref else None)
    today = date.today().isoformat()
    url_template = source.get("url_template")
    strip_mdx_flag = source.get("strip_mdx_components", False)

    # Primera pasada: decidir rutas destino para poder reescribir enlaces
    plan: list[dict] = []
    path_map: dict[str, str] = {}

    for index, path in enumerate(files):
        rel = path.relative_to(base)
        section, dest_rel = target_path(source, rel)
        plan.append(
            {
                "src": path,
                "rel": rel,
                "section": section,
                "dest_rel": dest_rel,
                "order": order_of(rel, index),
            }
        )
        path_map[rel.as_posix()] = dest_rel.as_posix()

    # Índice por nombre de fichero para los enlaces resueltos por slug.
    # Solo se usa cuando el nombre es único; si se repite, no hay forma
    # fiable de saber a cuál apuntaba y se deja el enlace como estaba.
    basename_map: dict[str, list[str]] = {}
    for original, destination in path_map.items():
        basename_map.setdefault(posixpath.basename(original), []).append(destination)

    sections: dict[str, list[dict]] = {}

    for item in plan:
        raw = item["src"].read_text(encoding="utf-8", errors="replace")
        existing, body = split_front_matter(raw)

        if strip_mdx_flag or item["src"].suffix == ".mdx":
            body = strip_mdx(body)

        body = rewrite_links(body, item, path_map, basename_map)

        title = extract_title(body, existing, item["dest_rel"].stem)
        slug = item["dest_rel"].with_suffix("").as_posix()

        front: dict[str, Any] = {"title": title}

        description = existing.get("description")
        if isinstance(description, str) and description.strip():
            front["description"] = description.strip()

        if url_template:
            front["source_url"] = url_template.format(slug=slug)
        if source.get("repo"):
            front["source_repo"] = shorten_repo(source.get("repo"))
        if ref:
            front["source_ref"] = str(ref)
        if commit:
            front["source_commit"] = commit[:9]

        front["source_path"] = item["rel"].as_posix()
        front["technology"] = source.id
        if version:
            front["version"] = str(version)
        if source.license:
            front["license"] = source.license
        front["retrieved_at"] = today
        if item["section"]:
            front["section"] = item["section"]
        front["order"] = item["order"]

        dest = out_root / item["dest_rel"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(render(front, body), encoding="utf-8")

        sections.setdefault(item["section"], []).append(
            {
                "title": title,
                "path": item["dest_rel"].as_posix(),
                "order": item["order"],
            }
        )

    toc = build_toc(source, sections)
    write_json(out_root / "_toc.json", toc)

    meta = {
        "id": source.id,
        "name": source.name,
        "documents": len(plan),
        "sections": len(sections),
        "retrieved_at": today,
    }
    if version:
        meta["version"] = str(version)
    if source.license:
        meta["license"] = source.license
    for key in ("homepage", "repo", "ref"):
        if source.get(key):
            meta[key] = source.get(key)
    if commit:
        meta["commit"] = commit
    write_json(out_root / "_meta.json", meta)

    Log.ok(f"{source.name}: {len(plan)} documentos en {len(sections)} sección(es)")
    return meta


def rewrite_links(
    body: str,
    item: dict,
    path_map: dict[str, str],
    basename_map: dict[str, list[str]],
) -> str:
    """Ajusta los enlaces internos a los ficheros ya renombrados.

    Al quitar el prefijo numérico de 01-installation.md, cualquier
    enlace [x](01-installation.md) quedaría roto si no se reescribe.

    Se resuelve la ruta completa, no solo el nombre: dos secciones
    distintas pueden tener un overview.md y confundirlos rompería los
    enlaces de forma silenciosa.

    Hay generadores (Docusaurus, que usa pnpm) que resuelven los enlaces
    por slug de la ruta pública y no por ruta de fichero, de modo que
    cli/add.md enlaza a config-dependencies.md aunque ese fichero esté
    en la raíz. Para esos casos se recurre al nombre de fichero, pero
    solo cuando es inequívoco en toda la tecnología.
    """
    src_dir = item["rel"].parent.as_posix()
    dst_dir = item["dest_rel"].parent.as_posix()

    def resolve(target: str) -> str | None:
        if target.startswith("/"):
            # Enlace absoluto respecto a la raíz de la documentación
            resolved = posixpath.normpath(target.lstrip("/"))
        else:
            resolved = posixpath.normpath(posixpath.join(src_dir, target))

        new_path = path_map.get(resolved)
        if new_path is not None:
            return new_path

        candidates = basename_map.get(posixpath.basename(resolved), [])
        return candidates[0] if len(candidates) == 1 else None

    def repl(match: re.Match) -> str:
        new_path = resolve(match.group(2))
        if new_path is None:
            return match.group(0)
        new_target = posixpath.relpath(new_path, dst_dir or ".")
        return f"{match.group(1)}{new_target}{match.group(3)}"

    body = RE_MD_LINK.sub(repl, body)
    return RE_MD_REF_LINK.sub(repl, body)


def shorten_repo(url: str) -> str:
    """https://github.com/laravel/docs.git → laravel/docs"""
    cleaned = re.sub(r"\.git$", "", url.rstrip("/"))
    parts = cleaned.split("/")
    return "/".join(parts[-2:]) if len(parts) >= 2 else cleaned


def render(front: dict[str, Any], body: str) -> str:
    header = yaml.safe_dump(
        front,
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
    ).strip()
    return f"---\n{header}\n---\n\n{body.strip()}\n"


def build_toc(source: Source, sections: dict[str, list[dict]]) -> dict:
    entries = []
    for name in sorted(sections, key=lambda s: (s == "", s)):
        pages = sorted(sections[name], key=lambda p: (p["order"], p["title"]))
        entries.append(
            {
                "title": (name or source.name).replace("-", " ").title(),
                "slug": name,
                "pages": pages,
            }
        )
    return {
        "technology": source.id,
        "name": source.name,
        "sections": entries,
    }


# ── Orquestación ────────────────────────────────────────────────────

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="docsync.normalize",
        description="Convierte work/ en markdown canónico dentro de src/",
    )
    parser.add_argument("--config", default="sources.yaml")
    parser.add_argument("--in", dest="work", default="work")
    parser.add_argument("--out", dest="src", default="src")
    parser.add_argument("--source", help="Normalizar solo esta fuente")
    parser.add_argument(
        "--jobs",
        type=int,
        default=0,
        help="Procesos para convertir XML o HTML (0 = tantos como núcleos)",
    )
    args = parser.parse_args(argv)

    config = Config.load(args.config)
    work_dir = Path(args.work)
    src_dir = Path(args.src)
    src_dir.mkdir(parents=True, exist_ok=True)

    lock = (read_json(Path("versions.lock.json")) or {}).get("sources", {})
    selected = config.select(args.source)

    Log.step(f"Normalizando {len(selected)} fuente(s) a {src_dir}/")

    done, skipped = 0, 0
    for source in selected:
        # Cada adaptador convierte desde su formato, pero todos escriben
        # el mismo markdown canónico: a partir de src/ nada distingue de
        # dónde salió un documento.
        if source.adapter == "docbook_xml":
            from .normalize_docbook import normalize_docbook_source

            result = normalize_docbook_source(
                source, work_dir, src_dir, lock, jobs=args.jobs
            )
        elif source.adapter in ("plaintext", "texinfo"):
            from .normalize_text import normalize_text_source

            result = normalize_text_source(
                source, work_dir, src_dir, lock, jobs=args.jobs
            )
        else:
            result = normalize_source(source, work_dir, src_dir, lock)

        if result:
            done += 1
        else:
            skipped += 1

    # El marcador deja de tener sentido en cuanto hay contenido real
    placeholder = src_dir / ".gitkeep"
    if done and placeholder.exists():
        placeholder.unlink()

    Log.step("Resumen")
    Log.ok(f"{done} normalizadas")
    if skipped:
        Log.warn(f"{skipped} omitidas")

    return 0 if done else 1


if __name__ == "__main__":
    sys.exit(main())
