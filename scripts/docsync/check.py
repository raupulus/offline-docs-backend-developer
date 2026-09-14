"""
Validación del contenido de src/

Comprueba que el markdown canónico está completo y es coherente. La
gracia de este proyecto es funcionar sin internet, así que el momento
de descubrir un fallo es ahora, no el día que se cae la red.

    python3 -m scripts.docsync.check --src src
"""

from __future__ import annotations

import argparse
import posixpath
import re
import sys
from pathlib import Path

from .common import Config, Log, read_json

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("Falta PyYAML.\n  pip3 install pyyaml --break-system-packages")


RE_FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
RE_MD_LINK = re.compile(r"\]\((?!https?://|mailto:|#)([^)\s]+?)(?:#[^)]*)?\)")

REQUIRED_KEYS = ("title", "technology", "source_path", "retrieved_at")


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def check_technology(tech_dir: Path, report: Report) -> int:
    tech = tech_dir.name

    meta = read_json(tech_dir / "_meta.json")
    if meta is None:
        report.error(f"{tech}: falta o está corrupto _meta.json")
    elif not meta.get("license"):
        report.warn(f"{tech}: sin licencia declarada en _meta.json")

    if read_json(tech_dir / "_toc.json") is None:
        report.error(f"{tech}: falta o está corrupto _toc.json")

    docs = [p for p in tech_dir.rglob("*.md")]
    if not docs:
        report.error(f"{tech}: no contiene ningún documento")
        return 0

    known = {p.relative_to(tech_dir).as_posix() for p in docs}

    for doc in docs:
        rel = doc.relative_to(tech_dir).as_posix()
        text = doc.read_text(encoding="utf-8", errors="replace")

        match = RE_FRONT_MATTER.match(text)
        if not match:
            report.error(f"{tech}/{rel}: sin front-matter")
            continue

        try:
            front = yaml.safe_load(match.group(1)) or {}
        except yaml.YAMLError as exc:
            report.error(f"{tech}/{rel}: front-matter inválido ({exc.__class__.__name__})")
            continue

        for key in REQUIRED_KEYS:
            if not front.get(key):
                report.error(f"{tech}/{rel}: falta '{key}' en el front-matter")

        if front.get("technology") != tech:
            report.warn(
                f"{tech}/{rel}: technology='{front.get('technology')}' "
                f"no coincide con la carpeta"
            )

        body = text[match.end():]
        if not body.strip():
            report.warn(f"{tech}/{rel}: documento vacío")

        for target in RE_MD_LINK.findall(body):
            if not target.endswith((".md", ".mdx")):
                continue

            # Un enlace que empieza por / es relativo a la raíz de la
            # tecnología, no al sistema de ficheros.
            if target.startswith("/"):
                candidate = posixpath.normpath(target.lstrip("/"))
            else:
                base = doc.parent.relative_to(tech_dir).as_posix()
                candidate = posixpath.normpath(posixpath.join(base, target))

            if candidate.startswith(".."):
                report.warn(f"{tech}/{rel}: enlace fuera de la tecnología → {target}")
            elif candidate not in known:
                report.warn(f"{tech}/{rel}: enlace roto → {target}")

    if meta and meta.get("documents") not in (None, len(docs)):
        report.warn(
            f"{tech}: _meta.json dice {meta.get('documents')} documentos "
            f"pero hay {len(docs)}"
        )

    return len(docs)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="docsync.check",
        description="Valida el markdown canónico de src/",
    )
    parser.add_argument("--config", default="sources.yaml")
    parser.add_argument("--src", default="src")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Tratar los avisos como errores",
    )
    args = parser.parse_args(argv)

    src_dir = Path(args.src)
    if not src_dir.is_dir():
        Log.error(f"No existe {src_dir}/. Ejecuta antes 'make normalize'.")
        return 1

    config = Config.load(args.config)
    report = Report()

    tech_dirs = sorted(d for d in src_dir.iterdir() if d.is_dir())
    if not tech_dirs:
        Log.error(f"{src_dir}/ está vacío. Ejecuta antes 'make normalize'.")
        return 1

    Log.step(f"Validando {len(tech_dirs)} tecnología(s)")

    total = 0
    for tech_dir in tech_dirs:
        if tech_dir.name not in config.sources:
            report.warn(f"{tech_dir.name}: no está declarada en sources.yaml")
        count = check_technology(tech_dir, report)
        total += count
        Log.info(f"{tech_dir.name}: {count} documentos")

    declared = {
        sid for sid, s in config.sources.items()
        if s.adapter == "git_markdown"
    }
    present = {d.name for d in tech_dirs}
    for missing in sorted(declared - present):
        report.warn(f"{missing}: declarada en sources.yaml pero ausente de src/")

    Log.step("Resultado")
    for msg in report.warnings:
        Log.warn(msg)
    for msg in report.errors:
        Log.error(msg)

    if report.errors:
        Log.error(f"{len(report.errors)} error(es) en {total} documentos")
        return 1

    if report.warnings and args.strict:
        Log.error(f"{len(report.warnings)} aviso(s) con --strict")
        return 1

    Log.ok(f"{total} documentos correctos" + (
        f", {len(report.warnings)} aviso(s)" if report.warnings else ""
    ))
    return 0


if __name__ == "__main__":
    sys.exit(main())
