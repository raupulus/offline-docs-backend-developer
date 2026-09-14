---
title: Installing Python modules
source_url: https://docs.python.org/es/3
source_path: installing/index.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: installing
order: 1450
---

# Installing Python modules

As a popular open source development project, Python has an active
supporting community of contributors and users that also make their
software available for other Python developers to use under open-
source license terms.

Esto permite a los usuarios de Python compartir y colaborar de manera
efectiva, beneficiándose de las soluciones que otros ya han creado
para problemas comunes (¡y a veces incluso raros!), además de
contribuir potencialmente con sus propias soluciones al grupo común.

This guide covers the installation part of the process. For a guide to
creating and sharing your own Python projects, refer to the Python
packaging user guide.

Nota:

  Para los usuarios corporativos y otros usuarios institucionales, se
  debe tener en cuenta que muchas organizaciones tienen sus propias
  políticas sobre el uso y la contribución al software de código
  abierto. Se deben tener en cuenta dichas políticas al utilizar las
  herramientas de distribución e instalación proporcionadas con
  Python.

## Palabras clave

* **pip** is the preferred installer program. It is included by
  default with the Python binary installers.

* Un *entorno virtual* es un entorno de Python parcialmente aislado
  que permite instalar paquetes para que los use una aplicación en
  particular, en lugar de instalarlos en todo el sistema.

* "venv" is the standard tool for creating virtual environments. It
  defaults to installing **pip** into all created virtual
  environments.

* "virtualenv" is a third-party alternative (and predecessor) to
  "venv".

* The Python Package Index (PyPI) is a public repository of open
  source licensed packages made available for use by other Python
  users.

* The Python Packaging Authority is the group of developers and
  documentation authors responsible for the maintenance and evolution
  of the standard packaging tools and the associated metadata and file
  format standards. They maintain a variety of tools, documentation,
  and issue trackers on GitHub.

Distinto en la versión 3.5: Ahora se recomienda el uso de "venv" para
crear entornos virtuales.

Ver también:

  Guía de usuario de empaquetado de Python: Crear y usar entornos
  virtuales

## Uso básico

Las herramientas estándar de empaquetado están diseñadas para que se
usen desde la línea de comandos.

The following command will install the latest version of a module and
its dependencies from PyPI:

   python -m pip install SomePackage

Nota:

  Para usuarios POSIX (incluyendo los usuarios de macOS y Linux), los
  ejemplos en esta guía asumen que se está usando un *virtual
  environment*.Para los usuarios de Windows, los ejemplos en esta guía
  asumen que se seleccionó la opción de ajustar la variable de entorno
  PATH del sistema al instalar Python.

Es posible especificar una versión exacta o mínima directamente en la
linea de comandos. Cuando se use un operando comparador como ">", "<"
o cualquier otro carácter especial que puede ser interpretado por el
intérprete de comandos, el nombre del paquete y la versión deben ir
entre comillas dobles:

   python -m pip install SomePackage==1.0.4    # specific version
   python -m pip install "SomePackage>=1.0.4"  # minimum version

Normalmente, si ya hay instalado un módulo adecuado, intentar
instalarlo otra vez no tendrá efecto alguno. Actualizar módulos
existentes requiere que se solicite explícitamente:

   python -m pip install --upgrade SomePackage

More information and resources regarding **pip** and its capabilities
can be found in the Python Packaging User Guide.

La creación de entornos virtuales se realiza a través de el módulo
"venv". Instalar paquetes en un entorno virtual activo usa los
comandos mostrados arriba.

Ver también:

  Guía de usuario de empaquetado de Python: Instalando paquetes de
  distribución de Python

## ¿Cómo...

Respuestas rápidas o enlaces para algunas tareas comunes.

### ... instalo paquetes solamente para el usuario actual?

Pasando la opción "--user" a "python -m pip install" instalará el
paquete únicamente para el usuario actual, en lugar de hacerlo para
todos los usuarios del sistema.

### ... instalo paquetes científicos de Python?

A number of scientific Python packages have complex binary
dependencies, and aren't currently easy to install using **pip**
directly. It will often be easier for users to install these packages
by other means rather than attempting to install them with **pip**.

Ver también:

  Guía de usuario de empaquetado de Python: Instalando paquetes
  científicos

### ... trabajo con múltiples versiones de Python instaladas en paralelo?

On Linux, macOS, and other POSIX systems, use the versioned Python
commands in combination with the "-m" switch to run the appropriate
copy of **pip**:

   python3    -m pip install SomePackage  # default Python 3
   python3.14 -m pip install SomePackage  # specifically Python 3.14

Appropriately versioned **pip** commands may also be available.

On Windows, use the **py** Python launcher in combination with the
"-m" switch:

   py -3    -m pip install SomePackage  # default Python 3
   py -3.14 -m pip install SomePackage  # specifically Python 3.14

## Problemas de instalación comunes

### Instalando en el Python del sistema bajo Linux

On Linux systems, a Python installation will typically be included as
part of the distribution. Installing into this Python installation
requires root access to the system, and may interfere with the
operation of the system package manager and other components of the
system if a component is unexpectedly upgraded using **pip**.

On such systems, it is often better to use a virtual environment or a
per-user installation when installing packages with **pip**.

### Pip no está instalado

It is possible that **pip** does not get installed by default. One
potential fix is:

   python -m ensurepip --default-pip

There are also additional resources for installing pip.

### Instalando extensiones binarias

Python once relied heavily on source-based distribution, with end
users being expected to compile extension modules from source as part
of the installation process.

With the introduction of the binary wheel format, and the ability to
publish wheels through PyPI, this problem is diminishing, as users are
more regularly able to install pre-built extensions rather than
needing to build them themselves.

Some of the solutions for installing scientific software that are not
yet available as pre-built wheel files may also help with obtaining
other binary extensions without needing to build them locally.

Ver también:

  Guía de usuario de empaquetado de Python: Extensiones binarias
