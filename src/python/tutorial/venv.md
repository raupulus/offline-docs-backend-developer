---
title: 12. Entornos virtuales y paquetes
source_url: https://docs.python.org/es/3
source_path: tutorial/venv.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: tutorial
order: 5010
---

# 12. Entornos virtuales y paquetes

## 12.1. Introducción

Las aplicaciones en Python usualmente hacen uso de paquetes y módulos
que no forman parte de la librería estándar. Las aplicaciones a veces
necesitan una versión específica de una librería, debido a que dicha
aplicación requiere que un bug particular haya sido solucionado o bien
la aplicación ha sido escrita usando una versión obsoleta de la
interfaz de la librería.

Esto significa que tal vez no sea posible para una instalación de
Python cumplir los requerimientos de todas las aplicaciones. Si la
aplicación A necesita la versión 1.0 de un módulo particular y la
aplicación B necesita la versión 2.0, entonces los requerimientos
entran en conflicto e instalar la versión 1.0 o 2.0 dejará una de las
aplicaciones sin funcionar.

La solución a este problema es crear un *entorno virtual*,  un
directorio que contiene una instalación de Python de una versión en
particular,  además de unos cuantos paquetes adicionales.

Diferentes aplicaciones pueden entonces usar entornos virtuales
diferentes.  Para resolver el ejemplo de requerimientos en conflicto
citado anteriormente, la aplicación A puede tener su propio entorno
virtual con la versión 1.0 instalada mientras que la aplicación B
tiene otro entorno virtual con la versión 2.0.  Si la aplicación B
requiere que actualizar la librería a la versión 3.0, ésto no afectará
el entorno virtual de la aplicación A.

## 12.2. Creando entornos virtuales

The module used to create and manage virtual environments is called
"venv".  "venv" will install the Python version from which the command
was run (as reported by the "--version" option). For instance,
executing the command with "python3.12" will install version 3.12.

Para crear un entorno virtual, decide en que carpeta quieres crearlo y
ejecuta el módulo "venv" como script con la ruta a la carpeta:

   python -m venv tutorial-env

Esto creará el directorio "tutorial-env" si no existe, y también
creará directorios dentro de él que contienen una copia del intérprete
de Python y varios archivos de soporte.

Una ruta común para el directorio de un entorno virtual es ".venv".
Ese nombre mantiene el directorio típicamente escondido en la consola
y fuera de vista mientras le da un nombre que explica cuál es el
motivo de su existencia. También permite que no haya conflicto con los
ficheros de definición de variables de entorno ".env" que algunas
herramientas soportan.

Una vez creado el entorno virtual, podrás activarlo.

En Windows, ejecuta:

   tutorial-env\Scripts\activate

En Unix o MacOS, ejecuta:

   source tutorial-env/bin/activate

(Este script está escrito para la consola bash. Si usas las consolas
**csh** or **fish**, hay scripts alternativos "activate.csh" y
"activate.fish" que deberá usar en su lugar.)

Activar el entorno virtual cambiará el prompt de tu consola para
mostrar que entorno virtual está usando, y modificará el entorno para
que al ejecutar "python" sea con esa versión e instalación en
particular.  Por ejemplo:

   $ source ~/envs/tutorial-env/bin/activate
   (tutorial-env) $ python
   Python 3.5.1 (default, May  6 2016, 10:59:36)
     ...
   >>> import sys
   >>> sys.path
   ['', '/usr/local/lib/python35.zip', ...,
   '~/envs/tutorial-env/lib/python3.5/site-packages']
   >>>

Note that the activated virtual environment does not alter the
"PYTHONPATH" variable in any way. This may lead to unexpected results
if the path includes references to code which is incompatible with the
Python version the virtual environment is using. The best practice is
to "unset PYTHONPATH" in bash or the equivalent for the shell you are
using.

Para desactivar el entorno virtual, digita:

   deactivate

en el terminal.

## 12.3. Manejando paquetes con pip

Puede instalar, actualizar y eliminar paquetes usando un programa
llamado **pip**. De forma predeterminada, "pip" instalará paquetes
desde el Indice de Paquetes de Python. Puede navegar por el índice de
paquetes de Python yendo a él en su navegador web.

"pip" tiene varios subcomandos: "install", "uninstall", "freeze", etc.
(Consulte la guía Installing Python modules para obtener la
documentación completa de "pip").

Se puede instalar la última versión de un paquete especificando el
nombre del paquete:

   (tutorial-env) $ python -m pip install novas
   Collecting novas
     Downloading novas-3.1.1.3.tar.gz (136kB)
   Installing collected packages: novas
     Running setup.py install for novas
   Successfully installed novas-3.1.1.3

También se puede instalar una versión específica de un paquete
ingresando el nombre del paquete seguido de "==" y el número de
versión:

   (tutorial-env) $ python -m pip install requests==2.6.0
   Collecting requests==2.6.0
     Using cached requests-2.6.0-py2.py3-none-any.whl
   Installing collected packages: requests
   Successfully installed requests-2.6.0

Si se ejecuta de nuevo el comando, "pip" detectará que la versión ya
está instalada y no hará nada. Se puede ingresar un número de versión
diferente para instalarlo, o se puede ejecutar "pip install --upgrade"
para actualizar el paquete a la última versión:

   (tutorial-env) $ python -m pip install --upgrade requests
   Collecting requests
   Installing collected packages: requests
     Found existing installation: requests 2.6.0
       Uninstalling requests-2.6.0:
         Successfully uninstalled requests-2.6.0
   Successfully installed requests-2.7.0

"pip -m pip uninstall" seguido de uno o varios nombres de paquetes
eliminará los paquetes del entorno virtual.

"python -m pip show" mostrará información de un paquete en particular:

   (tutorial-env) $ python -m pip show requests
   ---
   Metadata-Version: 2.0
   Name: requests
   Version: 2.7.0
   Summary: Python HTTP for Humans.
   Home-page: http://python-requests.org
   Author: Kenneth Reitz
   Author-email: me@kennethreitz.com
   License: Apache 2.0
   Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
   Requires:

"python -m pip list" mostrará todos los paquetes instalados en el
entorno virtual:

   (tutorial-env) $ python -m pip list
   novas (3.1.1.3)
   numpy (1.9.2)
   pip (7.0.3)
   requests (2.7.0)
   setuptools (16.0)

"python -m pip freeze" retorna una lista de paquetes instalados, pero
el formato de salida es el requerido por "python -m pip install".  Una
convención común es poner esta lista en un archivo "requirements.txt":

   (tutorial-env) $ python -m pip freeze > requirements.txt
   (tutorial-env) $ cat requirements.txt
   novas==3.1.1.3
   numpy==1.9.2
   requests==2.7.0

El archivo "requirements.txt" puede ser agregado al controlador de
versiones y distribuido como parte de la aplicación. Los usuarios
pueden entonces instalar todos los paquetes necesarios con "install
-r":

   (tutorial-env) $ python -m pip install -r requirements.txt
   Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
     ...
   Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
     ...
   Collecting requests==2.7.0 (from -r requirements.txt (line 3))
     ...
   Installing collected packages: novas, numpy, requests
     Running setup.py install for novas
   Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0

"pip" tiene muchas más opciones.  Consulte la guía Installing Python
modules para obtener documentación completa de "pip".  Cuando haya
escrito un paquete y desee que esté disponible en el índice de
paquetes de Python, consulte la Guía de usuario de empaquetado de
Python.
