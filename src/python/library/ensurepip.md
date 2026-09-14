---
title: '"ensurepip" --- Bootstrapping the "pip" installer'
source_url: https://docs.python.org/es/3
source_path: library/ensurepip.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2540
---

# "ensurepip" --- Bootstrapping the "pip" installer

Added in version 3.4.

**Source code:** Lib/ensurepip

======================================================================

The "ensurepip" package provides support for bootstrapping the "pip"
installer into an existing Python installation or virtual environment.
This bootstrapping approach reflects the fact that "pip" is an
independent project with its own release cycle, and the latest
available stable version is bundled with maintenance and feature
releases of the CPython reference interpreter.

En la mayoría de los casos, los usuarios finales de Python no deberían
tener que invocar este módulo directamente (como "pip" deben
arrancarse de forma predeterminada), pero puede ser necesario si se
omitió la instalación de "pip" al instalar Python (o al crear un
entorno virtual) o después de desinstalar explícitamente "pip".

Nota:

  Este módulo *no* accede a Internet. Todos los componentes necesarios
  para ejecutar "pip" se incluyen como partes internas del paquete.

This is an *optional module*. If it is missing from your copy of
CPython, look for documentation from your distributor (that is,
whoever provided Python to you). If you are the distributor, see
Requirements for optional modules.

Ver también:

  Installing Python modules
     La guía del usuario final para instalar paquetes python

  **PEP 453**: Arranque explícito de pip en instalaciones de Python
     La justificación original y la especificación de este módulo.

Availability: not Android, not iOS, not WASI.

This module is not supported on mobile platforms or WebAssembly
platforms.

## Command-line interface

La interfaz de línea de comandos se invoca mediante el modificador
"-m" del intérprete.

La invocación más simple posible es:

   python -m ensurepip

Esta invocación instalará "pip" si aún no está instalado, pero de lo
contrario no hace nada. Para asegurarse de que la versión instalada de
"pip" sea al menos tan reciente como la disponible en "ensurepip",
pase la opción "--upgrade":

   python -m ensurepip --upgrade

De forma predeterminada, "pip" se instala en el entorno virtual actual
(si uno está activo) o en los paquetes de sitio del sistema (si no hay
ningún entorno virtual activo). La ubicación de instalación se puede
controlar a través de dos opciones de línea de comandos adicionales:

--root <dir>

   Installs "pip" relative to the given root directory rather than the
   root of the currently active virtual environment (if any) or the
   default root for the current Python installation.

--user

   Installs "pip" into the user site packages directory rather than
   globally for the current Python installation (this option is not
   permitted inside an active virtual environment).

De forma predeterminada, se instalarán los scripts "pipX" y "pipX.Y"
(donde X.Y representa la versión de Python utilizada para invocar
"ensurepip"). Los scripts instalados se pueden controlar a través de
dos opciones de línea de comandos adicionales:

--altinstall

   If an alternate installation is requested, the "pipX" script will
   *not* be installed.

--default-pip

   If a "default pip" installation is requested, the "pip" script will
   be installed in addition to the two regular scripts.

Proporcionar ambas opciones de selección de script desencadenará una
excepción.

## API del módulo

"ensurepip" exposes two functions for programmatic use:

ensurepip.version()

   Retorna una cadena que especifica la versión disponible de pip que
   se instalará al arrancar un entorno.

ensurepip.bootstrap(root=None, upgrade=False, user=False, altinstall=False, default_pip=False, verbosity=0)

   Ejecuta "pip" en el entorno actual o designado.

   *root* especifica un directorio raíz alternativo para instalar en
   relación con. Si *root* es "None", la instalación utiliza la
   ubicación de instalación predeterminada para el entorno actual.

   *upgrade* indica si se debe actualizar o no una instalación
   existente de una versión anterior de "pip" a la versión disponible.

   *user* indica si se debe utilizar el esquema de usuario en lugar de
   instalar globalmente.

   De forma predeterminada, se instalarán los scripts "pipX" y
   "pipX.Y" (donde X.Y representa la versión actual de Python).

   Si se establece *altinstall*, *no* se instalará "pipX".

   Si se establece *default_pip*, se instalará "pip" además de los dos
   scripts normales.

   Establecer tanto *altinstall* como *default_pip* desencadenará
   "ValueError".

   *verbosity* controla el nivel de salida a "sys.stdout" de la
   operación de ejecución.

   Genera un evento auditing "ensurepip.bootstrap" con el argumento
   "root".

   Nota:

     El proceso de ejecución tiene efectos secundarios tanto en
     "sys.path" como "os.environ". Invocar la interfaz de línea de
     comandos en un subproceso en su lugar permite evitar estos
     efectos secundarios.

   Nota:

     El proceso de ejecución puede instalar módulos adicionales
     requeridos por "pip", pero otro software no debe asumir que esas
     dependencias siempre estarán presentes de forma predeterminada
     (ya que las dependencias se pueden eliminar en una versión futura
     de "pip").
