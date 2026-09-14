"""
Índices de búsqueda offline.

POR QUÉ SON .js Y NO .json
──────────────────────────
El sitio se abre desde file://, donde el navegador trata cada fichero
como origen opaco y bloquea fetch() y XMLHttpRequest. Lo que sí permite
es cargar <script src="...">.

Por eso el índice se emite como JavaScript que declara una variable
global en lugar de como JSON que habría que descargar:

    window.DOCS_INDEX = window.DOCS_INDEX || {};
    window.DOCS_INDEX.laravel = [ ... ];

Convertir esto a .json rompería el buscador al abrir el sitio sin
servidor, que es el caso de uso principal del proyecto.

QUÉ SE INDEXA
─────────────
Título, sección, encabezados y un extracto del cuerpo. No el documento
entero: el índice se carga en memoria y debe ser pequeño. Se genera uno
por tecnología, cargado bajo demanda, para no traer el índice completo
de PHP cuando se busca en Composer.

Claves abreviadas para que el fichero ocupe menos:
    u = url    t = título    s = sección
    n = nombre de la tecnología             b = cuerpo indexable
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from .common import Log, read_json

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None


RE_FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
RE_HEADING = re.compile(r"^#{2,4}\s+(.+?)\s*$", re.MULTILINE)
RE_CODE_BLOCK = re.compile(r"```.*?```", re.DOTALL)
RE_INLINE_CODE = re.compile(r"`[^`]*`")
RE_MD_LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
RE_MD_SYNTAX = re.compile(r"[#*_>|\-]{1,}")
RE_SPACES = re.compile(r"\s+")

# Suficiente para encontrar el documento; no es un buscador de texto
# completo, es un índice de navegación.
BODY_CHARS = 600


def _front_matter(text: str) -> tuple[dict, str]:
    match = RE_FRONT_MATTER.match(text)
    if not match:
        return {}, text
    if yaml is None:
        return {}, text[match.end():]
    try:
        data = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        data = {}
    return (data if isinstance(data, dict) else {}), text[match.end():]


def _searchable_body(body: str) -> str:
    """Texto plano del documento, sin código ni sintaxis markdown.

    Los bloques de código se descartan a propósito: llenan el índice de
    ruido y casi nunca es por donde se busca un documento.
    """
    text = RE_CODE_BLOCK.sub(" ", body)
    text = RE_INLINE_CODE.sub(" ", text)
    text = RE_MD_LINK.sub(r"\1", text)
    text = RE_MD_SYNTAX.sub(" ", text)
    text = RE_SPACES.sub(" ", text).strip()
    return text[:BODY_CHARS]


def build_index(tech_dir: Path) -> list[dict]:
    meta = read_json(tech_dir / "_meta.json") or {}
    tech_name = meta.get("name", tech_dir.name)

    entries: list[dict] = []

    for doc in sorted(tech_dir.rglob("*.md")):
        rel = doc.relative_to(tech_dir).as_posix()
        front, body = _front_matter(
            doc.read_text(encoding="utf-8", errors="replace")
        )

        url = re.sub(r"\.mdx?$", ".html", rel)
        title = front.get("title") or Path(rel).stem
        section = front.get("section", "")

        headings = " ".join(RE_HEADING.findall(body))
        haystack = f"{_searchable_body(body)} {headings}"[: BODY_CHARS * 2]

        entry = {"u": url, "t": title, "n": tech_name, "b": haystack}
        if section:
            entry["s"] = section
        entries.append(entry)

    return entries


def _render(tech: str, entries: list[dict]) -> str:
    payload = json.dumps(entries, ensure_ascii=False, separators=(",", ":"))
    return (
        "/* Índice de búsqueda generado. No editar a mano.\n"
        "   Es un .js y no un .json a propósito: sobre file:// el\n"
        "   navegador bloquea fetch() pero permite <script src>. */\n"
        "window.DOCS_INDEX = window.DOCS_INDEX || {};\n"
        f"window.DOCS_INDEX[{json.dumps(tech)}] = {payload};\n"
    )


def write_indexes(src_dir: Path, out_dir: Path, technologies: list[str]) -> None:
    """Un índice por tecnología, más uno global para la portada."""
    combined: dict[str, list[dict]] = {}

    for tech in technologies:
        tech_dir = src_dir / tech
        if not tech_dir.is_dir():
            continue

        entries = build_index(tech_dir)
        combined[tech] = entries

        target = out_dir / tech / "_search-index.js"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(_render(tech, entries), encoding="utf-8")

        size_kb = target.stat().st_size / 1024
        Log.info(f"{tech}: {len(entries)} entradas · {size_kb:.0f} KB")

    # Índice global de la portada. La URL de cada entrada se prefija con
    # la tecnología porque desde la raíz las rutas son ./<tec>/<pagina>.
    lines = [
        "/* Índice global generado. No editar a mano. */",
        "window.DOCS_INDEX = window.DOCS_INDEX || {};",
    ]
    everything: list[dict] = []
    for tech, entries in combined.items():
        for entry in entries:
            everything.append({**entry, "u": f"{tech}/{entry['u']}"})

    payload = json.dumps(everything, ensure_ascii=False, separators=(",", ":"))
    lines.append(f'window.DOCS_INDEX["*"] = {payload};')

    global_index = out_dir / "_search-all.js"
    global_index.write_text("\n".join(lines) + "\n", encoding="utf-8")

    size_kb = global_index.stat().st_size / 1024
    Log.ok(f"Índice global: {len(everything)} entradas · {size_kb:.0f} KB")
