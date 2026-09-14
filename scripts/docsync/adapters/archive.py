"""
Descarga y extracción de archivos comprimidos.

Lo usan las fuentes que no se distribuyen por git: el bundle de texto
plano de Python y el tarball de Bash con su fuente en Texinfo.

Aquí solo se descarga y se descomprime. La conversión a markdown va en
normalize_text.py.
"""

from __future__ import annotations

import shutil
import tarfile
import urllib.error
import urllib.request
import zipfile
from datetime import date
from pathlib import Path

from ..common import Log, dir_size, human_size

USER_AGENT = "docsync/0.1 (+https://github.com/raupulus)"
CHUNK = 1 << 16


def download(url: str, dest: Path, timeout: int = 180) -> Path:
    """Descarga a un fichero temporal y renombra al terminar.

    El renombrado final evita quedarse con una descarga a medias que
    parezca válida si se corta la conexión, que es precisamente el
    escenario para el que existe este proyecto.
    """
    dest.parent.mkdir(parents=True, exist_ok=True)
    partial = dest.with_suffix(dest.suffix + ".part")

    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            total = int(response.headers.get("Content-Length") or 0)
            done = 0
            with partial.open("wb") as fh:
                while True:
                    chunk = response.read(CHUNK)
                    if not chunk:
                        break
                    fh.write(chunk)
                    done += len(chunk)
                    if total:
                        print(
                            f"\r    descargando… {done * 100 // total}%",
                            end="",
                            flush=True,
                        )
            if total:
                print("\r" + " " * 30 + "\r", end="")
    except urllib.error.URLError as exc:
        partial.unlink(missing_ok=True)
        raise RuntimeError(f"no se pudo descargar {url}: {exc}") from exc

    partial.replace(dest)
    return dest


def _is_safe(member_name: str, root: Path) -> bool:
    """Rechaza rutas absolutas y las que escapan del directorio destino.

    Sin esto, un archivo malicioso podría escribir fuera de work/. El
    script antiguo hacía extractall() sin comprobar nada.
    """
    target = (root / member_name).resolve()
    try:
        target.relative_to(root.resolve())
    except ValueError:
        return False
    return True


def extract(archive: Path, dest: Path) -> Path:
    """Descomprime un .tar.gz, .tar.bz2, .tar.xz o .zip en dest."""
    dest.mkdir(parents=True, exist_ok=True)
    name = archive.name.lower()

    if name.endswith((".tar.gz", ".tgz", ".tar.bz2", ".tbz2", ".tar.xz", ".tar")):
        with tarfile.open(archive) as tar:
            members = [m for m in tar.getmembers() if _is_safe(m.name, dest)]
            skipped = len(tar.getmembers()) - len(members)
            if skipped:
                Log.warn(f"{skipped} entradas descartadas por ruta insegura")
            tar.extractall(path=dest, members=members)

    elif name.endswith(".zip"):
        with zipfile.ZipFile(archive) as zf:
            members = [n for n in zf.namelist() if _is_safe(n, dest)]
            zf.extractall(path=dest, members=members)

    else:
        raise RuntimeError(f"formato de archivo no reconocido: {archive.name}")

    return dest


def collapse_single_root(path: Path) -> None:
    """Si el archivo trae una única carpeta raíz, sube su contenido.

    Los tarballs de python.org y de bash envuelven todo en una carpeta
    con el número de versión en el nombre, que cambia en cada descarga.
    Sin aplanarla, las rutas dependerían de la versión.
    """
    entries = [p for p in path.iterdir() if not p.name.startswith(".")]
    if len(entries) != 1 or not entries[0].is_dir():
        return

    inner = entries[0]
    for item in list(inner.iterdir()):
        shutil.move(str(item), str(path / item.name))
    inner.rmdir()


def fetch(source, out_dir: Path, force: bool) -> dict:
    """Descarga y descomprime en work/<id>/."""
    dest = out_dir / source.id
    url = source.get("url")
    if not url:
        raise RuntimeError(f"{source.name}: falta 'url' en sources.yaml")

    marker = dest / ".fetched"
    if marker.is_file() and not force:
        Log.ok(f"{source.name}: ya descargado (usa --force para rehacer)")
        return {
            "adapter": source.adapter,
            "url": url,
            "fetched_at": marker.read_text(encoding="utf-8").strip(),
        }

    shutil.rmtree(dest, ignore_errors=True)
    dest.mkdir(parents=True, exist_ok=True)

    suffix = "".join(Path(url).suffixes[-2:]) or ".tar.gz"
    archive = dest / f"_download{suffix}"
    download(url, archive)

    Log.info(f"descomprimiendo {human_size(archive.stat().st_size)}…")
    extract(archive, dest)
    archive.unlink(missing_ok=True)
    collapse_single_root(dest)

    Log.ok(f"{source.name}: descargado · {human_size(dir_size(dest))}")

    today = date.today().isoformat()
    marker.write_text(today + "\n", encoding="utf-8")

    return {"adapter": source.adapter, "url": url, "fetched_at": today}
