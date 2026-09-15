"""
Normalizado de fuentes DocBook: work/<id>/**/*.xml → src/<id>/*.md

Es la contraparte de normalize.py para PHP. El resultado tiene el mismo
formato que el de cualquier otra fuente — mismo front-matter, mismo
_meta.json, mismo _toc.json — así que a partir de src/ nada distingue
de dónde salió cada documento.

Son unos 11.000 ficheros, así que la conversión va en paralelo. Cada
documento es independiente: no hay estado compartido más allá del
diccionario de entidades, que se pasa por valor a cada proceso.
"""

from __future__ import annotations

import shutil
from concurrent.futures import ProcessPoolExecutor
from datetime import date
from pathlib import Path
from typing import Any

from .common import Log, Source, render_front_matter, slugify, write_json
from .docbook import convert, load_entities

# Ficheros de armazón: solo ensamblan el manual con entidades de
SKELETON_NAMES = {
    "book.xml",
    "reference.xml",
    "versions.xml",
    "manual.xml",
    "filelist.sgml",
    "allfiles.sgml",
}


def section_of(rel: Path) -> str:
    """Sección del menú a partir de la ruta."""
    parts = rel.parts
    if not parts:
        return ""
    if parts[0] in ("reference", "ref") and len(parts) > 1:
        return parts[1] if len(parts) > 2 else parts[0]
    return parts[0] if len(parts) > 1 else ""


def _convert_one(args: tuple[str, str, dict, str]) -> dict | None:
    path_str, rel_str, entities, language = args
    try:
        xml = Path(path_str).read_text(encoding="utf-8", errors="replace")
        body, title, meta = convert(xml, entities, language=language)
    except Exception as exc:  # pragma: no cover
        return {"rel": rel_str, "error": f"{exc.__class__.__name__}: {exc}"}

    if not body.strip():
        return None

    return {"rel": rel_str, "body": body, "title": title, "extra": meta}


def _collect(root: Path, source: Source) -> list[Path]:
    exclude = set(source.get("exclude") or [])
    patterns = source.get("include") or ["*.xml"]
    files = []
    seen = set()
    for pattern in patterns:
        for path in sorted(root.rglob(pattern)):
            if path in seen:
                continue
            seen.add(path)
            rel = path.relative_to(root)
            if rel.name in SKELETON_NAMES or rel.name in exclude:
                continue
            if rel.parts and rel.parts[0] in exclude:
                continue
            files.append(path)
    return files


def normalize_docbook_source(
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

    entity_paths = list(root.glob("*.ent")) + list(root.glob("*.def"))
    for extra_ent in ("version.sgml", "postgres.sgml"):
        if (root / extra_ent).is_file():
            entity_paths.append(root / extra_ent)
    entity_root = work_dir / f"{source.id}.entities"
    if entity_root.is_dir():
        entity_paths += list(entity_root.rglob("*.ent"))

    entities = load_entities(entity_paths)
    if not entities:
        Log.info(f"{source.name}: sin entidades externas necesarias")
    else:
        Log.info(f"{len(entities)} entidades cargadas")

    files = _collect(root, source)
    if not files:
        Log.warn(f"{source.name}: no se encontró XML en {root}")
        return None

    language = source.get("code_language", "php")
    Log.info(f"convirtiendo {len(files)} documentos con pandoc…")

    payload = [
        (str(p), p.relative_to(root).as_posix(), entities, language)
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
            if i % 1000 == 0:
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
    version = source.expect.get("version") or source.get("ref")
    homepage = (source.get("homepage") or "").rstrip("/")

    sections: dict[str, list[dict]] = {}
    used: set[str] = set()

    for index, item in enumerate(results):
        rel = Path(item["rel"])
        section = section_of(rel)
        stem = slugify(rel.stem)

        # Dos ficheros distintos pueden compartir nombre en la misma
        # sección; sin esto uno pisaría al otro en silencio.
        candidate = f"{section}/{stem}.md" if section else f"{stem}.md"
        suffix = 2
        while candidate in used:
            candidate = (
                f"{section}/{stem}-{suffix}.md" if section else f"{stem}-{suffix}.md"
            )
            suffix += 1
        used.add(candidate)

        title = item.get("title") or stem
        extra = item.get("extra") or {}

        front: dict[str, Any] = {"title": title}
        if extra.get("description"):
            front["description"] = extra["description"]
        # Solo se enlaza a php.net cuando el XML trae su identificador
        # real. Una URL construida a ojo acabaría en 404.
        if homepage and extra.get("doc_id"):
            if "php.net" in homepage:
                front["source_url"] = f"{homepage}/{extra['doc_id']}.php"
            elif "postgresql.org" in homepage:
                front["source_url"] = f"{homepage}/{extra['doc_id']}.html"
            else:
                front["source_url"] = f"{homepage}/{extra['doc_id']}"
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

        # Estado de la traducción, tal y como lo anota php.net. Sirve
        # para avisar de qué páginas están sin revisar.
        for key in ("translation_status", "translation_reviewed", "translation_revision"):
            if key in extra:
                front[key] = extra[key]

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

    stale = sum(
        1 for r in results
        if (r.get("extra") or {}).get("translation_status") not in (None, "ready")
    )

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
    if stale:
        meta["translation_pending"] = stale
    write_json(out_root / "_meta.json", meta)

    Log.ok(f"{source.name}: {len(results)} documentos en {len(sections)} sección(es)")
    if stale:
        Log.info(f"{stale} con la traducción sin marcar como lista")

    return meta
