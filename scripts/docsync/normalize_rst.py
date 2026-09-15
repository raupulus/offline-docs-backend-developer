"""
Normalizado de fuentes reStructuredText: work/<id>/**/*.rst → src/<id>/*.md

Convierte documentación escrita en reStructuredText (Sphinx de MicroPython)
a markdown canónico con front-matter YAML, _meta.json y _toc.json.
"""

from __future__ import annotations

import html as html_lib
import re
import shutil
import subprocess
from concurrent.futures import ProcessPoolExecutor
from datetime import date
from pathlib import Path
from typing import Any

from .common import Log, Source, render_front_matter, slugify, write_json

RE_H1 = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
RE_SPHINX_DIV = re.compile(r'<div class="(?:currentmodule|toctree)"[^>]*>.*?</div>', re.DOTALL | re.IGNORECASE)
RE_TITLE_REF = re.compile(r'<span class="title-ref">(.*?)</span>', re.DOTALL | re.IGNORECASE)
RE_BARE_DIV = re.compile(r"^\s*</?div[^>]*>\s*$", re.MULTILINE)
RE_RST_LINK = re.compile(r"(\]\()(?!https?://|mailto:|//)([^)\s#]+\.rst)((?:#[^)]*)?\))")


def section_of(rel: Path) -> str:
    """Determina la sección lógica en la navegación."""
    parts = rel.parts
    stem = rel.stem.lower()

    if parts and parts[0] == "rp2":
        return "rp2-pico"
    if parts and parts[0] == "reference":
        return "reference"
    if parts and parts[0] == "library":
        if stem.startswith("machine.") or stem == "machine":
            return "library-machine"
        if stem.startswith("network.") or stem in ("network", "bluetooth"):
            return "library-network"
        if stem.startswith("rp2.") or stem == "rp2":
            return "library-rp2"
        return "library-core"
    return "general"


def _clean_body(text: str) -> tuple[str, str, str]:
    """Limpia el markdown producido por pandoc a partir de RST y extrae título."""
    text = RE_SPHINX_DIV.sub("", text)
    text = RE_TITLE_REF.sub(r"`\1`", text)
    text = RE_BARE_DIV.sub("", text)
    text = RE_RST_LINK.sub(lambda m: f"{m.group(1)}{m.group(2)[:-4]}.md{m.group(3)}", text)

    title = ""
    description = ""

    h1_match = RE_H1.search(text)
    if h1_match:
        raw_title = h1_match.group(1).strip()
        # Parse patterns like "class Pin -- control I/O pins" or "machine --- hardware control"
        if " -- " in raw_title:
            parts = raw_title.split(" -- ", 1)
            title = parts[0].replace("class ", "").replace("module ", "").strip()
            description = parts[1].strip()
        elif " --- " in raw_title:
            parts = raw_title.split(" --- ", 1)
            title = parts[0].replace("class ", "").replace("module ", "").strip()
            description = parts[1].strip()
        else:
            title = raw_title

    return title, description, text.strip() + "\n"


def _convert_one(args: tuple[str, str, str]) -> dict | None:
    path_str, rel_str, root_str = args
    file_path = Path(path_str)
    root = Path(root_str)

    try:
        proc = subprocess.run(
            ["pandoc", "-f", "rst", "-t", "gfm", "--wrap=none", str(file_path.relative_to(root))],
            cwd=root,
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            return {"rel": rel_str, "error": proc.stderr.strip() or "pandoc falló"}
        raw_output = proc.stdout
    except Exception as exc:  # pragma: no cover
        return {"rel": rel_str, "error": f"{exc.__class__.__name__}: {exc}"}

    if not raw_output.strip():
        return None

    title, description, body = _clean_body(raw_output)

    if not title:
        title = file_path.stem.replace("_", " ").replace("-", " ").title()

    return {
        "rel": rel_str,
        "body": body,
        "title": title,
        "description": description,
    }


def _collect(root: Path, source: Source) -> list[Path]:
    exclude = set(source.get("exclude") or [])
    files = []
    for path in sorted(root.rglob("*.rst")):
        rel = path.relative_to(root)
        if any(p in exclude for p in rel.parts) or rel.name in exclude:
            continue
        # Exclude root index and empty indexes
        if rel.name == "index.rst" and len(rel.parts) == 1:
            continue
        files.append(path)
    return files


def normalize_rst_source(
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

    prefix = source.get("strip_prefix")
    if prefix:
        candidate = root / prefix
        if candidate.is_dir():
            root = candidate
        else:
            Log.warn(f"strip_prefix '{prefix}' no existe; se usa la raíz")

    files = _collect(root, source)
    if not files:
        Log.warn(f"{source.name}: no se encontró RST en {root}")
        return None

    Log.info(f"convirtiendo {len(files)} documentos con pandoc…")

    payload = [
        (str(p), p.relative_to(root).as_posix(), str(root))
        for p in files
    ]

    results: list[dict] = []
    errors = 0

    with ProcessPoolExecutor(max_workers=jobs or None) as pool:
        for i, item in enumerate(pool.map(_convert_one, payload, chunksize=16), 1):
            if item is None:
                continue
            if "error" in item:
                errors += 1
                if errors <= 3:
                    Log.warn(f"{item['rel']}: {item['error']}")
                continue
            results.append(item)
            if i % 50 == 0:
                print(f"\r    {i}/{len(files)}…", end="", flush=True)

    print("\r" + " " * 30 + "\r", end="")
    if errors:
        Log.warn(f"{errors} documentos no se pudieron convertir")

    if not results:
        Log.warn(f"{source.name}: no se generó ningún documento")
        return None

    out_root = src_dir / source.id
    shutil.rmtree(out_root, ignore_errors=True)
    out_root.mkdir(parents=True, exist_ok=True)

    meta_lock = lock.get(source.id, {})
    retrieved = meta_lock.get("fetched_at", date.today().isoformat())
    commit = meta_lock.get("commit", "")
    ref = source.get("ref")
    version = source.expect.get("version") or (ref if ref else "latest")
    homepage = (source.get("homepage") or "").rstrip("/")

    sections: dict[str, list[dict]] = {}
    used: set[str] = set()

    for index, item in enumerate(results):
        rel = Path(item["rel"])
        section = section_of(rel)
        stem = slugify(rel.stem)

        candidate = f"{section}/{stem}.md" if section else f"{stem}.md"
        suffix = 2
        while candidate in used:
            candidate = (
                f"{section}/{stem}-{suffix}.md" if section else f"{stem}-{suffix}.md"
            )
            suffix += 1
        used.add(candidate)

        title = item.get("title") or stem
        description = item.get("description") or ""

        front: dict[str, Any] = {"title": title}
        if description:
            front["description"] = description
        if homepage:
            front["source_url"] = f"https://docs.micropython.org/en/latest/{rel.with_suffix('.html').as_posix()}"
        front["source_repo"] = source.get("repo", "")
        if source.get("ref"):
            front["source_ref"] = str(source.get("ref"))
        if commit:
            front["source_commit"] = commit[:9]
        front["source_path"] = rel.as_posix()
        front["technology"] = source.id
        if version:
            front["version"] = str(version)
        if source.license:
            front["license"] = source.license
        front["retrieved_at"] = retrieved
        if section:
            front["section"] = section

        front["order"] = (index + 1) * 10

        dest = out_root / candidate
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(render_front_matter(front, item["body"]), encoding="utf-8")

        sections.setdefault(section, []).append(
            {"title": title, "path": candidate, "order": front["order"]}
        )

    toc = {
        "technology": source.id,
        "name": source.name,
        "sections": [
            {
                "title": (name or source.name).replace("-", " ").title(),
                "slug": name,
                "pages": sorted(pages, key=lambda p: p["title"].lower()),
            }
            for name, pages in sorted(sections.items(), key=lambda kv: (kv[0] == "", kv[0]))
        ],
    }
    write_json(out_root / "_toc.json", toc)

    meta = {
        "id": source.id,
        "name": source.name,
        "documents": len(results),
        "sections": len(sections),
        "retrieved_at": retrieved,
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

    Log.ok(f"{source.name}: {len(results)} documentos en {len(sections)} sección(es)")
    return meta
