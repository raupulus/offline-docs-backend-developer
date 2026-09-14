# Dependencias

## Sistema

| Herramienta | Para qué | Obligatoria |
|---|---|---|
| `git` | Clonar Laravel, Filament, Composer, Node.js, npm, pnpm y PHP | Sí |
| `python3` (3.9+) | Todo el pipeline | Sí |
| `pandoc` | DocBook → markdown (PHP) y Texinfo → markdown (Bash) | Solo para PHP y Bash |
| `texi2any` | Texinfo → DocBook (Bash). Viene en el paquete `texinfo` | Solo para Bash |
| `make` | Interfaz de uso | Recomendable |

### Debian / Ubuntu

```bash
sudo apt update
sudo apt install git python3 python3-venv python3-pip pandoc texinfo make
```

### macOS

```bash
brew install git python3 pandoc texinfo make
```

En macOS `texi2any` se instala en `/opt/homebrew/opt/texinfo/bin` y **no entra en el PATH por defecto**, porque macOS ya trae una versión antigua. Si `make fetch` no lo encuentra:

```bash
echo 'export PATH="/opt/homebrew/opt/texinfo/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

---

## Python

Cuatro paquetes, en un entorno virtual:

```bash
make venv                    # crea .venv e instala todo
source .venv/bin/activate    # actívalo en cada sesión de terminal
```

Los dos pasos son necesarios y en ese orden: `make venv` crea el entorno, `source` lo activa. Sin activarlo, `make` seguirá usando el Python del sistema y volverás a ver el error.

A mano, si prefieres:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

| Paquete | Para qué |
|---|---|
| `pyyaml` | Leer `sources.yaml` y el front-matter de cada documento |
| `markdown` | Convertir markdown a HTML en el generador de sitio |
| `jinja2` | Plantillas del visor |
| `pygments` | Resaltar el código en tiempo de compilación |

`pyyaml` hace falta desde el primer comando; los otros tres solo en `make build`.

### Sin entorno virtual

En Debian 12+ y en macOS con Homebrew, Python viene marcado como *externally managed* y `pip install` falla. Con entorno virtual no pasa. Si aun así prefieres instalarlos en el sistema:

```bash
pip3 install -r requirements.txt --break-system-packages
```

---

## Comprobar que está todo

```bash
make deps
```

Avisa de lo que falte y de si estás dentro de un entorno virtual. `texi2any` solo se reclama si vas a generar Bash.

---

## Problemas conocidos

**`Falta PyYAML` con el entorno virtual activado.** El `make` está usando otro Python. Comprueba con `which python3`: debe apuntar a `.venv/bin/python3`. Si no, vuelve a activar el entorno.

**`Operation not permitted` al clonar.** Estás dejando `work/` dentro de Google Drive o Dropbox, que montan un sistema de ficheros donde git no puede cambiar permisos. Sácalo fuera:

```bash
make update WORK_DIR=/tmp/docs-work
```

**`pandoc: command not found` solo al normalizar PHP o Bash.** Las seis fuentes en markdown no necesitan pandoc; las otras tres sí.
