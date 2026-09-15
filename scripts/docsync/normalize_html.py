"""
Normalizado de fuentes HTML estáticas: work/<id>/**/*.html → src/<id>/*.md

Convierte documentación HTML limpia (como el bundle oficial de SQLite)
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

RE_TITLE = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)
RE_NOSEARCH = re.compile(
    r"<div\s+class=[\"']?nosearch[\"']?>.*?</div>\s*</div>",
    re.DOTALL | re.IGNORECASE,
)
RE_NOSEARCH_SINGLE = re.compile(
    r"<div\s+class=[\"']?nosearch[\"']?>.*?</div>",
    re.DOTALL | re.IGNORECASE,
)
RE_SCRIPT = re.compile(r"<script\b.*?</script>", re.DOTALL | re.IGNORECASE)
RE_STYLE = re.compile(r"<style\b.*?</style>", re.DOTALL | re.IGNORECASE)
RE_FOOTER = re.compile(
    r"<p\s+align=[\"']?center[\"']?>\s*<small><i>This page was last updated.*?</p>",
    re.DOTALL | re.IGNORECASE,
)
RE_BARE_DIV = re.compile(r"^\s*</?div[^>]*>\s*$", re.MULTILINE)
RE_HTML_LINK = re.compile(
    r"(\]\()(?!https?://|mailto:|//)([^)\s#]+\.html)((?:#[^)]*)?\))"
)


def section_of(rel: Path) -> str:
    """Determina la sección lógica en la navegación."""
    stem = rel.stem.lower()
    if rel.parent.name == "c3ref":
        return "c-api"
    if stem.startswith("lang_"):
        return "sql-language"
    if stem.startswith("syntax"):
        return "syntax"
    if stem in (
        "cli",
        "pragma",
        "fts3",
        "fts5",
        "json1",
        "rtree",
        "session",
        "vtab",
        "backup",
        "carray",
        "dbhash",
        "sqlar",
        "c_interface",
        "capi3ref",
    ):
        return "tools-extensions"
    return "guides"


def _clean_html(raw: str) -> tuple[str, str]:
    """Extrae título y elimina navegación y scripts antes de pandoc."""
    title = ""
    m = RE_TITLE.search(raw)
    if m:
        title = html_lib.unescape(m.group(1)).strip()
        title = re.sub(r"\s*[-–:]\s*SQLite\s*$", "", title, flags=re.IGNORECASE)
        title = re.sub(r"^SQLite\s*[-–:]\s*", "", title, flags=re.IGNORECASE)

    cleaned = RE_NOSEARCH.sub("", raw)
    cleaned = RE_NOSEARCH_SINGLE.sub("", cleaned)
    cleaned = RE_SCRIPT.sub("", cleaned)
    cleaned = RE_STYLE.sub("", cleaned)
    cleaned = RE_FOOTER.sub("", cleaned)

    return title, cleaned


def _convert_one(args: tuple[str, str, str]) -> dict | None:
    path_str, rel_str, root_str = args
    file_path = Path(path_str)
    root = Path(root_str)

    try:
        raw_html = file_path.read_text(encoding="utf-8", errors="replace")
        title, cleaned = _clean_html(raw_html)

        proc = subprocess.run(
            ["pandoc", "-f", "html", "-t", "gfm", "--wrap=none"],
            input=cleaned,
            cwd=root,
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            return {"rel": rel_str, "error": proc.stderr.strip() or "pandoc falló"}
        body = proc.stdout
    except Exception as exc:  # pragma: no cover
        return {"rel": rel_str, "error": f"{exc.__class__.__name__}: {exc}"}

    if not body.strip():
        return None

    # Limpiar restos de etiquetas HTML residuales
    body = RE_BARE_DIV.sub("", body)

    # Reescribir enlaces .html -> .md internos
    body = RE_HTML_LINK.sub(
        lambda m: f"{m.group(1)}{m.group(2)[:-5]}.md{m.group(3)}", body
    )

    if not title or title.lower() == "sqlite":
        title = file_path.stem.replace("_", " ").replace("-", " ").title()

    return {
        "rel": rel_str,
        "body": body.strip() + "\n",
        "title": title,
    }


def _collect(root: Path, source: Source) -> list[Path]:
    exclude = set(source.get("exclude") or [])
    files = []
    for path in sorted(root.rglob("*.html")):
        rel = path.relative_to(root)
        if any(p in exclude for p in rel.parts):
            continue
        files.append(path)
    return files


def normalize_html_source(
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
        Log.warn(f"{source.name}: no se encontró HTML en {root}")
        return None

    Log.info(f"convirtiendo {len(files)} documentos con pandoc…")

    payload = [
        (str(p), p.relative_to(root).as_posix(), str(root))
        for p in files
    ]

    results: list[dict] = []
    errors = 0

    with ProcessPoolExecutor(max_workers=jobs or None) as pool:
        for i, item in enumerate(pool.map(_convert_one, payload, chunksize=32), 1):
            if item is None:
                continue
            if "error" in item:
                errors += 1
                if errors <= 3:
                    Log.warn(f"{item['rel']}: {item['error']}")
                continue
            results.append(item)
            if i % 100 == 0:
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
    version = source.expect.get("version") or "3.53.4"
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

        front: dict[str, Any] = {"title": title}
        if homepage:
            front["source_url"] = f"https://www.sqlite.org/{rel.as_posix()}"
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
    write_json(out_root / "_meta.json", meta)

    Log.ok(f"{source.name}: {len(results)} documentos en {len(sections)} sección(es)")
    return meta
