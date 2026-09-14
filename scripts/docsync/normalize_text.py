"""
Normalizado de las fuentes que no son ni markdown ni DocBook.

Dos caminos, ninguno pasa por HTML:

  plaintext  Python. docs.python.org publica un bundle de texto plano
             junto al de HTML: es la salida del builder `text` de
             Sphinx. No hay nada que parsear — se trocea, se detecta el
             título y se le pone front-matter. Cero dependencias.

  texinfo    Bash. El fuente del manual es Texinfo. `texi2any --docbook`
             lo pasa a DocBook, y de ahí entra por docbook.py, que ya
             está probado con PHP. Tampoco toca HTML.

Se descartó convertir desde el HTML compilado de ambos proyectos: obliga
a recortar navegación de cada página y a deshacer maquetación, y el
resultado es peor que el de estas dos rutas.
"""

from __future__ import annotations

import re
import shutil
import subprocess
from datetime import date
from pathlib import Path
from typing import Any

from .common import Log, Source, render_front_matter, require, slugify, write_json

# Sphinx subraya los títulos con una línea de signos de puntuación
RE_UNDERLINE = re.compile(r"^[=\-~^\"'`*+#]{3,}\s*$")
RE_BLANK = re.compile(r"\n{3,}")
RE_TRAILING_WS = re.compile(r"[ \t]+$", re.MULTILINE)


# ── Texto plano (Python) ────────────────────────────────────────────

def title_from_text(content: str, fallback: str) -> str:
    """Primer título del documento.

    El builder `text` de Sphinx marca los títulos subrayándolos con una
    línea de signos, igual que en reStructuredText.
    """
    lines = content.splitlines()
    for i, line in enumerate(lines[:40]):
        text = line.strip()
        if not text:
            continue
        if i + 1 < len(lines) and RE_UNDERLINE.match(lines[i + 1]):
            return text
    return fallback.replace("-", " ").replace("_", " ").strip().capitalize()


# Nivel de encabezado según el signo con que Sphinx lo subraya
UNDERLINE_LEVELS = {"*": 1, "=": 2, "-": 3, "~": 4, "^": 5, '"': 6}


def text_to_markdown(content: str) -> str:
    """Convierte la salida del builder `text` de Sphinx en markdown.

    Sphinx marca los títulos subrayándolos con una línea de signos, y
    sangra el resto del contenido. Traducir solo eso ya da un documento
    navegable, con su índice lateral y sus anclas.

    El cuerpo se deja tal cual: las tablas y los ejemplos dependen de la
    alineación por espacios y cualquier reformateo los rompería. Las
    líneas sangradas cuatro espacios o más las interpreta markdown como
    bloque de código, que es justo lo que son.

    Antes se envolvía el documento entero en un bloque literal. Se leía,
    pero salía un muro de texto monoespaciado sin estructura.
    """
    lines = RE_TRAILING_WS.sub("", content).split("\n")
    out: list[str] = []
    i = 0

    while i < len(lines):
        line = lines[i]
        text = line.strip()
        nxt = lines[i + 1] if i + 1 < len(lines) else ""

        # Sobrelínea + título + sublínea: el título del documento
        if (
            text
            and RE_UNDERLINE.match(line)
            and i + 2 < len(lines)
            and RE_UNDERLINE.match(lines[i + 2])
            and lines[i + 1].strip()
        ):
            out.append(f"# {lines[i + 1].strip()}")
            out.append("")
            i += 3
            continue

        # Título subrayado
        if text and RE_UNDERLINE.match(nxt) and not line.startswith(" "):
            level = UNDERLINE_LEVELS.get(nxt.strip()[0], 2)
            out.append(f"{'#' * min(level, 6)} {text}")
            out.append("")
            i += 2
            continue

        out.append(line)
        i += 1

    body = "\n".join(out)
    return RE_BLANK.sub("\n\n", body).strip() + "\n"


def collect_text(root: Path, source: Source) -> list[Path]:
    exclude = set(source.get("exclude") or [])
    files = []
    for path in sorted(root.rglob("*.txt")):
        rel = path.relative_to(root)
        if rel.name in exclude or (rel.parts and rel.parts[0] in exclude):
            continue
        files.append(path)
    return files


def load_plaintext(source: Source, root: Path) -> list[dict]:
    documents = []
    for index, path in enumerate(collect_text(root, source)):
        rel = path.relative_to(root)
        content = path.read_text(encoding="utf-8", errors="replace")
        if not content.strip():
            continue
        documents.append(
            {
                "rel": rel,
                "title": title_from_text(content, rel.stem),
                "body": text_to_markdown(content),
                "section": rel.parts[0] if len(rel.parts) > 1 else "",
                "order": (index + 1) * 10,
            }
        )
    return documents


# ── Texinfo (Bash) ──────────────────────────────────────────────────

def texinfo_to_docbook(path: Path, include_dirs: list[Path]) -> str:
    """Convierte un .texi a DocBook con texi2any.

    Los @include de Texinfo se resuelven por rutas de búsqueda. El
    manual de Bash incluye ficheros de readline que viven en otra
    carpeta del tarball (lib/readline/doc), así que hay que pasarlas
    con -I o falla con 'could not find rluser.texi'.

    texi2any viene en el paquete `texinfo`:
        Debian/Ubuntu:  sudo apt install texinfo
        macOS:          brew install texinfo
    """
    args = ["texi2any", "--docbook", "--no-split", "--output=-"]
    for directory in include_dirs:
        args += ["-I", str(directory)]
    args.append(str(path))

    proc = subprocess.run(args, capture_output=True, text=True)

    # texi2any avisa de referencias cruzadas rotas por stderr aunque la
    # conversión salga bien; solo es error si no produjo nada.
    if not proc.stdout.strip():
        raise RuntimeError(proc.stderr.strip() or "texi2any no devolvió nada")

    if proc.returncode != 0:
        Log.warn("texi2any terminó con avisos; se continúa con lo convertido")

    return proc.stdout


def load_texinfo(source: Source, root: Path) -> list[dict]:
    from .docbook import convert as docbook_convert
    from .mdsplit import split_sections

    require("texi2any")

    pattern = source.get("texi_file") or "**/*.texi"
    candidates = sorted(root.glob(pattern))
    if not candidates:
        Log.warn(f"{source.name}: no se encontró ningún .texi con '{pattern}'")
        return []

    main = candidates[0]

    # Rutas donde buscar los @include. Por defecto, la carpeta del
    # propio fichero más las que declare sources.yaml.
    include_dirs = [main.parent]
    for extra in source.get("texi_include") or []:
        for found in sorted(root.glob(extra)):
            if found.is_dir():
                include_dirs.append(found)

    Log.info(f"convirtiendo {main.name} con texi2any…")

    docbook = texinfo_to_docbook(main, include_dirs)
    body, _, _ = docbook_convert(docbook, {}, language=source.get("code_language", "bash"))

    levels = tuple(
        int(str(level).lstrip("h")) for level in (source.get("split_on") or ["h2"])
    )
    sections = split_sections(body, levels)

    return [
        {
            "rel": Path(f"{order:03d}-{slugify(title)}.md"),
            "title": title,
            "body": chunk,
            "section": "",
            "order": order * 10,
        }
        for order, (title, chunk) in enumerate(sections, start=1)
    ]


# ── Escritura ───────────────────────────────────────────────────────

LOADERS = {
    "plaintext": load_plaintext,
    "texinfo": load_texinfo,
}


def normalize_text_source(
    source: Source,
    work_dir: Path,
    src_dir: Path,
    lock: dict,
    jobs: int = 0,
) -> dict | None:
    root = work_dir / source.id
    if not root.is_dir():
        Log.warn(f"{source.name}: sin descargar, ejecuta antes 'make fetch'")
        return None

    loader = LOADERS.get(source.adapter)
    if loader is None:
        Log.error(f"{source.name}: adaptador desconocido '{source.adapter}'")
        return None

    documents = loader(source, root)
    if not documents:
        Log.warn(f"{source.name}: no se generó ningún documento")
        return None

    out_root = src_dir / source.id
    shutil.rmtree(out_root, ignore_errors=True)
    out_root.mkdir(parents=True, exist_ok=True)

    meta_lock = lock.get(source.id, {})
    retrieved = meta_lock.get("fetched_at", date.today().isoformat())
    version = source.expect.get("version") or source.get("ref")
    homepage = (source.get("homepage") or "").rstrip("/")

    sections: dict[str, list[dict]] = {}
    used: set[str] = set()

    for item in documents:
        rel: Path = item["rel"]
        section = item["section"]
        stem = slugify(rel.stem)

        candidate = f"{section}/{stem}.md" if section else f"{stem}.md"
        suffix = 2
        while candidate in used:
            candidate = (
                f"{section}/{stem}-{suffix}.md" if section else f"{stem}-{suffix}.md"
            )
            suffix += 1
        used.add(candidate)

        front: dict[str, Any] = {"title": item["title"]}
        if homepage:
            front["source_url"] = homepage
        front["source_path"] = rel.as_posix()
        front["technology"] = source.id
        if version:
            front["version"] = str(version)
        if source.license:
            front["license"] = source.license
        front["retrieved_at"] = retrieved
        if section:
            front["section"] = section
        front["order"] = item["order"]

        dest = out_root / candidate
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(
            render_front_matter(front, RE_BLANK.sub("\n\n", item["body"])),
            encoding="utf-8",
        )

        sections.setdefault(section, []).append(
            {"title": item["title"], "path": candidate, "order": item["order"]}
        )

    write_json(
        out_root / "_toc.json",
        {
            "technology": source.id,
            "name": source.name,
            "sections": [
                {
                    "title": (name or source.name).replace("-", " ").title(),
                    "slug": name,
                    "pages": sorted(pages, key=lambda p: (p["order"], p["title"])),
                }
                for name, pages in sorted(
                    sections.items(), key=lambda kv: (kv[0] == "", kv[0])
                )
            ],
        },
    )

    meta = {
        "id": source.id,
        "name": source.name,
        "documents": len(documents),
        "sections": len(sections),
        "retrieved_at": retrieved,
    }
    if version:
        meta["version"] = str(version)
    if source.license:
        meta["license"] = source.license
    for key in ("homepage", "url"):
        if source.get(key):
            meta[key] = source.get(key)
    write_json(out_root / "_meta.json", meta)

    Log.ok(f"{source.name}: {len(documents)} documentos en {len(sections)} sección(es)")
    return meta
