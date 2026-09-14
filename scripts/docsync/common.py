"""
Utilidades compartidas por las fases del pipeline.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

def missing_package(name: str) -> str:
    """Mensaje de instalación correcto según dónde esté corriendo Python.

    Dentro de un entorno virtual, `--break-system-packages` no solo
    sobra: instala en el sitio equivocado y el error se repite.
    """
    in_venv = sys.prefix != sys.base_prefix

    if in_venv:
        arreglo = "  pip install -r requirements.txt"
    else:
        arreglo = (
            "  python3 -m venv .venv && source .venv/bin/activate\n"
            "  pip install -r requirements.txt\n\n"
            "  O bien, sin entorno virtual:\n"
            "  pip3 install -r requirements.txt --break-system-packages"
        )

    return (
        f"Falta el paquete '{name}'.\n\n"
        f"{arreglo}\n\n"
        f"  Python en uso: {sys.executable}\n"
        f"  Ver info/dependencias.md"
    )


try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit(missing_package("pyyaml"))


# ── Salida por consola ──────────────────────────────────────────────

class Log:
    """Salida legible. Se desactiva el color si no hay terminal."""

    _tty = sys.stdout.isatty()

    @classmethod
    def _c(cls, code: str, text: str) -> str:
        return f"\033[{code}m{text}\033[0m" if cls._tty else text

    @classmethod
    def step(cls, msg: str) -> None:
        print(cls._c("1;36", f"\n→ {msg}"))

    @classmethod
    def ok(cls, msg: str) -> None:
        print(f"  {cls._c('32', '✓')} {msg}")

    @classmethod
    def warn(cls, msg: str) -> None:
        print(f"  {cls._c('33', '!')} {msg}")

    @classmethod
    def error(cls, msg: str) -> None:
        print(f"  {cls._c('31', '✗')} {msg}", file=sys.stderr)

    @classmethod
    def info(cls, msg: str) -> None:
        print(f"    {msg}")


# ── Configuración ───────────────────────────────────────────────────

@dataclass
class Source:
    """Una entrada de sources.yaml, ya resuelta con los valores por defecto."""

    id: str
    raw: dict[str, Any] = field(repr=False)

    def get(self, key: str, default: Any = None) -> Any:
        return self.raw.get(key, default)

    @property
    def name(self) -> str:
        return self.raw.get("name", self.id)

    @property
    def adapter(self) -> str:
        return self.raw.get("adapter", "git_markdown")

    @property
    def license(self) -> str:
        return self.raw.get("license", "")

    @property
    def expect(self) -> dict[str, Any]:
        return self.raw.get("expect") or {}


@dataclass
class Config:
    path: Path
    defaults: dict[str, Any]
    sources: dict[str, Source]

    @classmethod
    def load(cls, path: str | Path) -> "Config":
        p = Path(path)
        if not p.is_file():
            sys.exit(f"No se encuentra el catálogo de fuentes: {p}")

        with p.open(encoding="utf-8") as fh:
            data = yaml.safe_load(fh) or {}

        defaults = data.get("defaults") or {}
        raw_sources = data.get("sources") or {}
        if not raw_sources:
            sys.exit(f"{p} no declara ninguna fuente en 'sources:'")

        sources = {}
        for sid, entry in raw_sources.items():
            merged = {**defaults, **(entry or {})}
            sources[sid] = Source(id=sid, raw=merged)

        return cls(path=p, defaults=defaults, sources=sources)

    def select(self, only: str | None) -> list[Source]:
        if not only:
            return list(self.sources.values())
        if only not in self.sources:
            disponibles = ", ".join(sorted(self.sources))
            sys.exit(f"Fuente desconocida: '{only}'.\nDisponibles: {disponibles}")
        return [self.sources[only]]


# ── Ejecución de comandos ───────────────────────────────────────────

def run(
    args: list[str],
    cwd: Path | None = None,
    check: bool = True,
    quiet: bool = True,
) -> subprocess.CompletedProcess:
    """Ejecuta un comando y devuelve el resultado.

    Con check=True aborta el programa mostrando stderr, en lugar de
    dejar escapar una excepción sin contexto.
    """
    proc = subprocess.run(
        args,
        cwd=str(cwd) if cwd else None,
        capture_output=True,
        text=True,
    )
    if check and proc.returncode != 0:
        Log.error(f"Falló: {' '.join(args)}")
        if proc.stderr.strip():
            Log.info(proc.stderr.strip().splitlines()[-1])
        raise RuntimeError(proc.stderr)
    if not quiet and proc.stdout.strip():
        Log.info(proc.stdout.strip())
    return proc


def require(*tools: str) -> None:
    """Aborta si falta alguna herramienta externa."""
    import shutil

    missing = [t for t in tools if shutil.which(t) is None]
    if missing:
        sys.exit(
            f"Faltan herramientas: {', '.join(missing)}\n"
            "  Debian/Ubuntu:  sudo apt install git pandoc\n"
            "  macOS:          brew install git pandoc"
        )


# ── JSON ────────────────────────────────────────────────────────────

def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def read_json(path: Path, default: Any = None) -> Any:
    if not path.is_file():
        return default
    try:
        with path.open(encoding="utf-8") as fh:
            return json.load(fh)
    except json.JSONDecodeError:
        return default


# ── Texto ───────────────────────────────────────────────────────────

RE_SPACES = re.compile(r"\s+")
RE_UNSAFE = re.compile(r"[^a-z0-9._-]+")
RE_NUMERIC_PREFIX = re.compile(r"^\d{1,3}[-_.]")


def slugify(text: str) -> str:
    """Nombre de fichero seguro: minúsculas, sin acentos y sin espacios."""
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii").lower()
    text = RE_NUMERIC_PREFIX.sub("", text)
    text = RE_SPACES.sub("-", text.strip())
    text = RE_UNSAFE.sub("-", text)
    return text.strip("-.") or "documento"


def render_front_matter(front: dict[str, Any], body: str) -> str:
    """Documento canónico: front-matter YAML más el cuerpo en markdown."""
    header = yaml.safe_dump(
        front, sort_keys=False, allow_unicode=True, default_flow_style=False
    ).strip()
    return f"---\n{header}\n---\n\n{body.strip()}\n"


def human_size(num_bytes: int) -> str:
    size = float(num_bytes)
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024 or unit == "GB":
            return f"{size:.1f} {unit}" if unit != "B" else f"{int(size)} B"
        size /= 1024
    return f"{size:.1f} GB"


def dir_size(path: Path, pattern: str = "**/*") -> int:
    return sum(f.stat().st_size for f in path.glob(pattern) if f.is_file())
