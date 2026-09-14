"""
Fase 5 del pipeline: concatena cada tecnología de src/ en un único archivo markdown en bundles/.

Pensado para:
  * Modelos de IA (LLMs): alimentar contexto amplio con la doc entera de una tecnología.
  * Lectura continua o búsqueda global en un solo archivo plano.
  * Descarga directa desde la web estática.

Uso:
  python3 -m scripts.docsync.bundle --src src --out bundles --public public/bundles
"""

from __future__ import annotations

import argparse
import html
import re
import shutil
import sys
from datetime import date
from pathlib import Path
from typing import Any

from .common import Log, read_json

RE_FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def format_size(bytes_count: int) -> str:
    """Convierte bytes a formato legible (e.g. 520 KB, 3.1 MB)."""
    if bytes_count < 1024:
        return f"{bytes_count} B"
    elif bytes_count < 1024 * 1024:
        return f"{bytes_count / 1024:.0f} KB"
    else:
        return f"{bytes_count / (1024 * 1024):.1f} MB"


def split_front_matter(text: str) -> tuple[dict[str, Any], str]:
    match = RE_FRONT_MATTER.match(text)
    if not match:
        return {}, text
    try:
        import yaml
        data = yaml.safe_load(match.group(1)) or {}
        if not isinstance(data, dict):
            data = {}
    except Exception:
        data = {}
    return data, text[match.end():]


def flat_pages(toc: dict) -> list[dict]:
    pages = []
    for section in toc.get("sections", []):
        for entry in section.get("pages", []):
            pages.append({**entry, "section": section.get("title", section.get("slug", ""))})
    return pages


def bundle_technology(tech_dir: Path, out_dir: Path, public_dir: Path | None = None) -> tuple[str, int] | None:
    tech = tech_dir.name
    meta = read_json(tech_dir / "_meta.json")
    toc = read_json(tech_dir / "_toc.json")
    if not meta or not toc:
        return None

    name = meta.get("name", tech)
    version = meta.get("version", "")
    v_str = f" v{version}" if version else ""
    license_name = meta.get("license", "No especificada")
    homepage = meta.get("homepage", "")
    retrieved_at = meta.get("retrieved_at", date.today().isoformat())

    ordered = flat_pages(toc)
    if not ordered:
        ordered = [{"path": doc.relative_to(tech_dir).as_posix(), "title": doc.stem, "section": ""} for doc in sorted(tech_dir.rglob("*.md"))]

    lines = []
    lines.append(f"# {name}{v_str} — Documentación técnica oficial\n")
    lines.append("> **Espejo Offline de Documentación Técnica**")
    lines.append(f"> Licencia: {license_name} | Documentos incluidos: {len(ordered)} | Versión: {version or 'Oficial'}")
    lines.append(f"> Descargado/sincronizado: {retrieved_at}")
    if homepage:
        lines.append(f"> Documentación oficial en línea: {homepage}")
    lines.append("> Mantenedor del espejo: Raúl Caro Pastorino (@raupulus) · https://raupulus.dev\n")
    lines.append("---\n")

    lines.append("## Índice de contenidos\n")
    current_section = None
    for item in ordered:
        sec = item.get("section", "")
        if sec and sec != current_section:
            current_section = sec
            lines.append(f"\n### {sec}\n")
        title = item.get("title", item["path"])
        slug = re.sub(r"[^a-zA-Z0-9_\-]+", "-", title.lower()).strip("-")
        lines.append(f"- [{title}](#{slug})")
    lines.append("\n---\n")

    current_section = None
    for item in ordered:
        doc_path = tech_dir / item["path"]
        if not doc_path.is_file():
            continue

        raw = doc_path.read_text(encoding="utf-8", errors="replace")
        front, body = split_front_matter(raw)
        title = front.get("title") or item.get("title") or doc_path.stem
        sec = item.get("section") or front.get("section") or ""
        source_url = front.get("source_url") or ""

        lines.append("\n\n---\n")
        lines.append(f"# {title}\n")
        meta_sub = []
        if sec:
            meta_sub.append(f"Sección: {sec}")
        if source_url:
            meta_sub.append(f"Origen: {source_url}")
        if meta_sub:
            lines.append(f"*{' | '.join(meta_sub)}*\n")

        cleaned_body = body.strip()
        if cleaned_body.startswith("# ") and cleaned_body.split("\n", 1)[0][2:].strip() == title:
            cleaned_body = cleaned_body.split("\n", 1)[1].strip() if "\n" in cleaned_body else ""

        lines.append(cleaned_body)

    content = "\n".join(lines) + "\n"
    bundle_file = out_dir / f"{tech}.md"
    bundle_file.write_text(content, encoding="utf-8")
    size_bytes = bundle_file.stat().st_size

    if public_dir:
        public_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(bundle_file, public_dir / f"{tech}.md")

    Log.ok(f"{name}: {format_size(size_bytes)} ({len(ordered)} docs) → {bundle_file.name}")
    return tech, size_bytes


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="docsync.bundle", description="Genera archivos markdown concatenados por tecnología")
    parser.add_argument("--src", default="src")
    parser.add_argument("--out", default="bundles")
    parser.add_argument("--public", default="public/bundles")
    args = parser.parse_args(argv)

    src_dir = Path(args.src)
    out_dir = Path(args.out)
    public_dir = Path(args.public) if args.public else None

    if not src_dir.is_dir():
        Log.error(f"No existe {src_dir}/")
        return 1

    out_dir.mkdir(parents=True, exist_ok=True)
    if public_dir:
        public_dir.mkdir(parents=True, exist_ok=True)

    tech_dirs = sorted(d for d in src_dir.iterdir() if d.is_dir() and not d.name.startswith("."))

    Log.step(f"Generando bundles Markdown en {out_dir}/")
    total_size = 0
    count = 0
    for td in tech_dirs:
        res = bundle_technology(td, out_dir, public_dir)
        if res:
            count += 1
            total_size += res[1]

    Log.ok(f"Total: {count} bundles generados ({format_size(total_size)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
