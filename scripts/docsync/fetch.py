"""
Fase 1 del pipeline: red → work/

Descarga cada fuente declarada en sources.yaml. Para repositorios git
usa siempre clon superficial (--depth 1) y sparse checkout limitado a
la carpeta de documentación.

Esto no es un detalle de optimización: un clon completo de Filament
arrastra vendor/ y node_modules, unos 60.000 ficheros y 40 MB, cuando
la documentación real son 82 ficheros y 1,5 MB.

Registra el commit exacto de cada fuente en versions.lock.json para que
una reconstrucción sea reproducible.

    python3 -m scripts.docsync.fetch --config sources.yaml --out work
    python3 -m scripts.docsync.fetch --source laravel

Nota: work/ debe estar en un sistema de ficheros normal. Sobre carpetas
sincronizadas (Google Drive, Dropbox) git puede fallar al no poder
cambiar permisos. En ese caso:  make update WORK_DIR=/tmp/docs-work
"""

from __future__ import annotations

import argparse
import shutil
import sys
from datetime import date
from pathlib import Path

from .common import Config, Log, Source, dir_size, human_size, require, run, write_json


# ── Adaptador git_markdown ──────────────────────────────────────────

def _clone(source: Source, dest: Path) -> None:
    """Clon superficial y parcial. Sin sparse todavía."""
    args = ["git", "clone"]

    depth = source.get("depth", 1)
    if depth:
        args += ["--depth", str(depth)]

    blob_filter = source.get("filter")
    if blob_filter:
        args += [f"--filter={blob_filter}"]

    if source.get("sparse"):
        args += ["--sparse"]

    ref = source.get("ref")
    if ref:
        args += ["--branch", str(ref)]

    args += [source.get("repo"), str(dest)]
    run(args)


def _apply_sparse(source: Source, dest: Path) -> None:
    """Restringe el working tree a las carpetas de documentación."""
    patterns = source.get("sparse")
    if not patterns:
        return

    # Los patrones con comodines (/packages/*/docs) necesitan --no-cone.
    # El modo cone solo admite prefijos de directorio literales.
    cone = source.get("sparse_cone", True)
    args = ["git", "sparse-checkout", "set"]
    if not cone:
        args.append("--no-cone")
    args += list(patterns)
    run(args, cwd=dest)


def _current_commit(dest: Path) -> str:
    return run(["git", "rev-parse", "HEAD"], cwd=dest).stdout.strip()


def _update_existing(source: Source, dest: Path) -> bool:
    """Actualiza un clon ya presente. Devuelve False si no es viable."""
    if not (dest / ".git").is_dir():
        return False

    ref = str(source.get("ref") or "HEAD")
    try:
        run(["git", "fetch", "--depth", "1", "origin", ref], cwd=dest)
        run(["git", "reset", "--hard", "FETCH_HEAD"], cwd=dest)
        _apply_sparse(source, dest)
        return True
    except RuntimeError:
        # Cambió la rama, se corrompió el clon o el remoto se movió.
        # work/ es desechable: se rehace desde cero sin drama.
        return False


def fetch_git_markdown(source: Source, out_dir: Path, force: bool) -> dict:
    dest = out_dir / source.id

    if dest.exists() and not force:
        if _update_existing(source, dest):
            Log.ok(f"{source.name}: actualizado")
        else:
            Log.warn(f"{source.name}: clon inservible, se rehace")
            shutil.rmtree(dest, ignore_errors=True)
            _clone(source, dest)
            _apply_sparse(source, dest)
            Log.ok(f"{source.name}: clonado de nuevo")
    else:
        shutil.rmtree(dest, ignore_errors=True)
        _clone(source, dest)
        _apply_sparse(source, dest)
        Log.ok(f"{source.name}: clonado")

    commit = _current_commit(dest)
    count = _count_documents(source, dest)
    size = dir_size(dest) - dir_size(dest / ".git")

    Log.info(f"{count} ficheros · {human_size(max(size, 0))} · {commit[:9]}")
    _warn_if_unexpected(source, count)

    return {
        "adapter": "git_markdown",
        "repo": source.get("repo"),
        "ref": source.get("ref"),
        "commit": commit,
        "files": count,
        "fetched_at": date.today().isoformat(),
    }


# Extensión de los documentos según el adaptador. Contar .md en una
# fuente DocBook daba un falso aviso de "faltan ficheros".
DOCUMENT_GLOBS = {
    "docbook_xml": ("*.xml",),
    "git_markdown": ("*.md", "*.mdx"),
}


def _count_documents(source: Source, dest: Path) -> int:
    patterns = source.get("include") or DOCUMENT_GLOBS.get(
        source.adapter, ("*.md", "*.mdx")
    )
    return sum(len(list(dest.rglob(pattern))) for pattern in patterns)


def _warn_if_unexpected(source: Source, n_files: int) -> None:
    """Avisa si el volumen se desvía mucho de lo esperado.

    Un salto grande casi siempre significa que el sparse checkout dejó
    de filtrar y estamos arrastrando código fuente, o que el proyecto
    reorganizó su carpeta de documentación.
    """
    expected = source.expect.get("files")
    if not expected or not n_files:
        return

    ratio = n_files / expected
    if ratio > 3:
        Log.warn(
            f"{n_files} ficheros frente a ~{expected} esperados. "
            "¿Ha fallado el sparse checkout?"
        )
    elif ratio < 0.4:
        Log.warn(
            f"Solo {n_files} ficheros frente a ~{expected} esperados. "
            "¿Han movido la carpeta de documentación?"
        )


# ── Orquestación ────────────────────────────────────────────────────

def fetch_docbook_xml(source: Source, out_dir: Path, force: bool) -> dict:
    """Igual que git_markdown, más el repo de entidades.

    La documentación de PHP se escribe en DocBook y usa unas 1.500
    entidades definidas en ficheros .ent. Las del idioma vienen en el
    propio repo de traducción; las comunes están en php/doc-base, que
    hay que clonar aparte.
    """
    info = fetch_git_markdown(source, out_dir, force)
    info["adapter"] = "docbook_xml"

    entity_repo = source.get("entity_repo")
    if not entity_repo:
        return info

    entity_source = Source(
        id=f"{source.id}.entities",
        raw={
            "name": f"{source.name} (entidades)",
            "repo": entity_repo,
            "ref": source.get("entity_ref"),
            "sparse": source.get("entity_sparse") or ["entities"],
            "depth": 1,
            "filter": "blob:none",
        },
    )
    entity_info = fetch_git_markdown(entity_source, out_dir, force)
    info["entity_repo"] = entity_repo
    info["entity_commit"] = entity_info.get("commit")

    return info


def fetch_archive(source: Source, out_dir: Path, force: bool) -> dict:
    """Descarga y descomprime. Lo usan Python (texto plano) y Bash (Texinfo)."""
    from .adapters.archive import fetch as _fetch

    return _fetch(source, out_dir, force)


ADAPTERS = {
    "git_markdown": fetch_git_markdown,
    "docbook_xml": fetch_docbook_xml,
    "plaintext": fetch_archive,
    "texinfo": fetch_archive,
}

PENDING_ADAPTERS: set[str] = set()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="docsync.fetch",
        description="Descarga las fuentes de documentación a work/",
    )
    parser.add_argument("--config", default="sources.yaml")
    parser.add_argument("--out", default="work")
    parser.add_argument("--source", help="Descargar solo esta fuente")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Rehacer el clon aunque ya exista",
    )
    args = parser.parse_args(argv)

    require("git")

    config = Config.load(args.config)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    selected = config.select(args.source)
    lock_path = Path("versions.lock.json")
    lock = {}
    existing = {}
    if lock_path.is_file():
        from .common import read_json

        existing = (read_json(lock_path) or {}).get("sources", {})

    Log.step(f"Descargando {len(selected)} fuente(s) a {out_dir}/")

    ok, skipped, failed = 0, 0, 0

    for source in selected:
        adapter = source.adapter

        if adapter in PENDING_ADAPTERS:
            Log.warn(f"{source.name}: adaptador '{adapter}' pendiente (fase 4)")
            skipped += 1
            if source.id in existing:
                lock[source.id] = existing[source.id]
            continue

        handler = ADAPTERS.get(adapter)
        if handler is None:
            Log.error(f"{source.name}: adaptador desconocido '{adapter}'")
            failed += 1
            continue

        try:
            lock[source.id] = handler(source, out_dir, args.force)
            ok += 1
        except RuntimeError:
            Log.error(f"{source.name}: no se pudo descargar")
            failed += 1
        except KeyboardInterrupt:
            print()
            return 130

    # Al descargar una sola fuente hay que conservar el resto del lock
    if args.source:
        merged = dict(existing)
        merged.update(lock)
        lock = merged

    write_json(
        lock_path,
        {
            "generated_at": date.today().isoformat(),
            "config": str(config.path),
            "sources": lock,
        },
    )

    Log.step("Resumen")
    Log.ok(f"{ok} descargadas")
    if skipped:
        Log.warn(f"{skipped} pendientes de la fase 4")
    if failed:
        Log.error(f"{failed} con errores")
    Log.info(f"Commits registrados en {lock_path}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
