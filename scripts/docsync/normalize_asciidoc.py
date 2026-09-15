"""
Normalizado de fuentes AsciiDoc: work/<id>/**/*.adoc → src/<id>/*.md

Convierte documentación escrita en AsciiDoc (como la de Git) a markdown
canónico con front-matter YAML, _meta.json y _toc.json.
"""

from __future__ import annotations

import re
import shutil
import subprocess
from concurrent.futures import ProcessPoolExecutor
from datetime import date
from pathlib import Path
from typing import Any

from .common import Log, Source, render_front_matter, slugify, write_json

RE_NAME = re.compile(r"NAME\s*[-=]+\s*([^\n]+)", re.IGNORECASE)
RE_SETEXT_H1 = re.compile(r"^([^\n]+)\n[=]{3,}\s*$", re.MULTILINE)
RE_LINKGIT = re.compile(r"linkgit:([a-zA-Z0-9_-]+)(?:\\*\[\d+[\\\]]+)?")

MAN5_NAMES = {
    "gitattributes",
    "gitformat-bundle",
    "gitformat-chunk",
    "gitformat-commit-graph",
    "gitformat-index",
    "gitformat-loose",
    "gitformat-pack",
    "gitformat-signature",
    "githooks",
    "gitignore",
    "gitmailmap",
    "gitmodules",
    "gitprotocol-capabilities",
    "gitprotocol-common",
    "gitprotocol-http",
    "gitprotocol-pack",
    "gitprotocol-v2",
    "gitrepository-layout",
    "gitweb.conf",
}

MAN7_NAMES = {
    "gitcli",
    "gitcore-tutorial",
    "gitcredentials",
    "gitcvs-migration",
    "gitdatamodel",
    "gitdiffcore",
    "giteveryday",
    "gitfaq",
    "gitglossary",
    "gitnamespaces",
    "gitpacking",
    "gitremote-helpers",
    "gitrevisions",
    "gitsubmodules",
    "gittutorial",
    "gittutorial-2",
    "gitworkflows",
    "user-manual",
}


def section_of(rel: Path) -> str:
    """Determina la sección lógica en la navegación."""
    stem = rel.stem.lower()
    if rel.parent.name == "howto":
        return "howto"
    if stem in MAN5_NAMES:
        return "formats"
    if stem in MAN7_NAMES:
        return "guides"
    return "commands"


def _convert_one(args: tuple[str, str, str]) -> dict | None:
    path_str, rel_str, root_str = args
    file_path = Path(path_str)
    root = Path(root_str)

    try:
        proc = subprocess.run(
            [
                "pandoc",
                "-f",
                "asciidoc",
                "-t",
                "gfm",
                "--wrap=none",
                str(file_path.relative_to(root)),
            ],
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

    # Limpiar y resolver enlaces linkgit:...
    body = RE_LINKGIT.sub(r"[\1](\1.md)", body)

    title = file_path.stem
    description = ""

    name_match = RE_NAME.search(body)
    if name_match:
        full_name = name_match.group(1).strip()
        parts = full_name.split(" - ", 1)
        title = parts[0].strip()
        if len(parts) > 1:
            description = parts[1].strip()
    else:
        h1_match = RE_SETEXT_H1.search(body)
        if h1_match:
            title = h1_match.group(1).strip()
            title = re.sub(r"\([1-9]\)$", "", title).strip()

    if file_path.stem == "user-manual":
        title = "Git User's Manual"

    return {
        "rel": rel_str,
        "body": body,
        "title": title,
        "description": description,
    }


def _collect(root: Path, source: Source) -> list[Path]:
    exclude = set(source.get("exclude") or [])
    files = []
    for path in sorted(root.rglob("*.adoc")):
        rel = path.relative_to(root)
        if any(p in exclude for p in rel.parts):
            continue
        if (
            rel.name.startswith("git")
            or rel.name in ("scalar.adoc", "user-manual.adoc")
            or (rel.parent.name == "howto" and not rel.name.startswith("."))
        ):
            files.append(path)
    return files


def _sanitize_source(root: Path) -> None:
    alias_file = root / "config" / "alias.adoc"
    if alias_file.is_file():
        text = alias_file.read_text(encoding="utf-8", errors="replace")
        fixed = text.replace("\n#", "\n //").replace("--\n", "")
        alias_file.write_text(fixed, encoding="utf-8")

    git_file = root / "git.adoc"
    if git_file.is_file():
        text = git_file.read_text(encoding="utf-8", errors="replace")
        fixed = re.sub(r"include::\{build_dir\}/[^\n]+", "", text)
        git_file.write_text(fixed, encoding="utf-8")


def normalize_asciidoc_source(
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

    _sanitize_source(root)

    files = _collect(root, source)
    if not files:
        Log.warn(f"{source.name}: no se encontró AsciiDoc en {root}")
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
    version = source.expect.get("version") or (ref if ref else None)
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
            front["source_url"] = f"{homepage}/{stem}"
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
