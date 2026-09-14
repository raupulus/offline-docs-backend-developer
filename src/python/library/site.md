---
title: '"site" --- Site-specific configuration hook'
source_url: https://docs.python.org/es/3
source_path: library/site.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3800
---

# "site" --- Site-specific configuration hook

**Código Fuente:** Lib/site.py

======================================================================

**Este módulo se importa automáticamente durante la inicialización.**
La importación automática se puede suprimir utilizando la opción del
intérprete opción "-S" .

Importing this module normally appends site-specific paths to the
module search path and adds callables, including "help()" to the
built-in namespace. However, Python startup option "-S" blocks this
and this module can be safely imported with no automatic modifications
to the module search path or additions to the builtins.  To explicitly
trigger the usual site-specific additions, call the "main()" function.

Distinto en la versión 3.3: Importar el módulo utilizado para activar
la manipulación de rutas incluso cuando se utiliza "-S".

It starts by constructing up to four directories from a head and a
tail part. For the head part, it uses "sys.prefix" and
"sys.exec_prefix"; empty heads are skipped.  For the tail part, it
uses the empty string and then "lib/site-packages" (on Windows) or
"lib/python*X.Y[t]*/site-packages" (on Unix and macOS). (The optional
suffix "t" indicates the *free-threaded build*, and is appended if
""t"" is present in the "sys.abiflags" constant.) For each of the
distinct head-tail combinations, it sees if it refers to an existing
directory, and if so, adds it to "sys.path" and also inspects the
newly added path for configuration files.

Distinto en la versión 3.5: Se ha eliminado la compatibilidad con el
directorio "site-python".

Distinto en la versión 3.13: On Unix, *Free threading* Python
installations are identified by the "t" suffix in the version-specific
directory name, such as "lib/python3.13t/".

Distinto en la versión 3.14: "site" is no longer responsible for
updating "sys.prefix" and "sys.exec_prefix" on Virtual Environments.
This is now done during the path initialization. As a result, under
Virtual Environments, "sys.prefix" and "sys.exec_prefix" no longer
depend on the "site" initialization, and are therefore unaffected by
"-S".

When running under a virtual environment, the "pyvenv.cfg" file in
"sys.prefix" is checked for site-specific configurations. If the
"include-system-site-packages" key exists and is set to "true" (case-
insensitive), the system-level prefixes will be searched for site-
packages, otherwise they won't.

Un archivo de configuración de ruta es un archivo cuyo nombre tiene la
forma "*name*.pth" y existe en uno de los cuatro directorios
mencionados anteriormente; su contenido son elementos adicionales (uno
por línea) que se agregarán a "sys.path". Los elementos que no existen
nunca se agregan a "sys.path" y no se comprueba que el elemento se
refiera a un directorio en lugar de a un archivo. No se agrega ningún
elemento a "sys.path" más de una vez. Se omiten las líneas en blanco y
las que comienzan con "#". Se ejecutan las líneas que comienzan con
"import" (seguidas de un espacio o tabulación).

Nota:

  Una línea ejecutable en un archivo ".pth" se ejecuta en cada inicio
  de Python, independientemente de si se va a utilizar un módulo en
  particular. Por tanto, su impacto debería reducirse al mínimo. El
  propósito principal de las líneas ejecutables es hacer que los
  módulos correspondientes se puedan importar (cargar ganchos de
  importación de terceros, ajustar "PATH", etc.). Se supone que
  cualquier otra inicialización se debe realizar en la importación
  real de un módulo, siempre y cuando ocurra. Limitar un fragmento de
  código a una sola línea es una medida deliberada para desalentar la
  inclusión de algo más complejo aquí.

Distinto en la versión 3.13: The ".pth" files are now decoded by UTF-8
at first and then by the *locale encoding* if it fails.

Por ejemplo, supongamos que "sys.prefix" y "sys.exec_prefix" están
configurados en "/usr/local". La biblioteca Python X.Y se instala en
"/usr/local/lib/python*X.Y*". Supongamos que tiene un subdirectorio
"/usr/local/lib/python*X.Y*/site-packages" con tres subsubdirectorios,
"foo", "bar" y "spam", y dos archivos de configuración de ruta,
"foo.pth" y "bar.pth". Suponga "foo.pth" contiene lo siguiente:

   # foo package configuration

   foo
   bar
   bletch

y "bar.pth" contiene:

   # bar package configuration

   bar

Luego, los siguientes directorios específicos de la versión se agregan
a "sys.path", en este orden:

   /usr/local/lib/pythonX.Y/site-packages/bar
   /usr/local/lib/pythonX.Y/site-packages/foo

Tenga en cuenta que "bletch" se omite porque no existe; el directorio
"bar" precede al directorio "foo" porque "bar.pth" viene
alfabéticamente antes de "foo.pth"; y "spam" se omite porque no se
menciona en ninguno de los archivos de configuración de ruta.

## "sitecustomize"

After these path manipulations, an attempt is made to import a module
named "sitecustomize", which can perform arbitrary site-specific
customizations. It is typically created by a system administrator in
the site-packages directory.  If this import fails with an
"ImportError" or its subclass exception, and the exception's "name"
attribute equals "'sitecustomize'", it is silently ignored.  If Python
is started without output streams available, as with "pythonw.exe" on
Windows (which is used by default to start IDLE), attempted output
from "sitecustomize" is ignored.  Any other exception causes a silent
and perhaps mysterious failure of the process.

## "usercustomize"

After this, an attempt is made to import a module named
"usercustomize", which can perform arbitrary user-specific
customizations, if "ENABLE_USER_SITE" is true.  This file is intended
to be created in the user site-packages directory (see below), which
is part of "sys.path" unless disabled by "-s".  If this import fails
with an "ImportError" or its subclass exception, and the exception's
"name" attribute equals "'usercustomize'", it is silently ignored.

Note that for some non-Unix systems, "sys.prefix" and
"sys.exec_prefix" are empty, and the path manipulations are skipped;
however the import of "sitecustomize" and "usercustomize" is still
attempted.

## Configuración de *Readline*

On systems that support "readline", this module will also import and
configure the "rlcompleter" module, if Python is started in
interactive mode and without the "-S" option. The default behavior is
to enable tab completion and to use "~/.python_history" as the history
save file.  To disable it, delete (or override) the
"sys.__interactivehook__" attribute in your "sitecustomize" or
"usercustomize" module or your "PYTHONSTARTUP" file.

Distinto en la versión 3.4: La activación de *rlcompleter* y el
historial se hizo automática.

## Contenido del módulo

site.PREFIXES

   Una lista de prefijos para directorios de site-packages.

site.ENABLE_USER_SITE

   Flag que muestra el estado del directorio site-packages del
   usuario. "True" significa que está habilitado y se agregó a
   "sys.path". "False" significa que fue deshabilitado por solicitud
   del usuario (con "-s" o "PYTHONNOUSERSITE"). "None" significa que
   fue deshabilitado por razones de seguridad (falta de coincidencia
   entre la identificación de usuario o grupo y la identificación
   efectiva) o por un administrador.

site.USER_SITE

   Path to the user site-packages for the running Python.  Can be
   "None" if "getusersitepackages()" hasn't been called yet.  Default
   value is "~/.local/lib/python*X.Y*[t]/site-packages" for UNIX and
   non-framework macOS builds, "~/Library/Python/*X.Y*/lib/python
   /site-packages" for macOS framework builds, and
   "*%APPDATA%*\Python\Python*XY*\site-packages" on Windows.  The
   optional "t" indicates the free-threaded build.  This directory is
   a site directory, which means that ".pth" files in it will be
   processed.

site.USER_BASE

   Path to the base directory for the user site-packages.  Can be
   "None" if "getuserbase()" hasn't been called yet.  Default value is
   "~/.local" for UNIX and macOS non-framework builds,
   "~/Library/Python/*X.Y*" for macOS framework builds, and
   "*%APPDATA%*\Python" for Windows.  This value is used to compute
   the installation directories for scripts, data files, Python
   modules, etc. for the user installation scheme. See also
   "PYTHONUSERBASE".

site.main()

   Agrega todos los directorios estándar específicos del sitio a la
   ruta de búsqueda del módulo. Esta función se llama automáticamente
   cuando se importa este módulo, a menos que el intérprete de Python
   se haya iniciado con la opción "-S".

   Distinto en la versión 3.3: Esta función solía llamarse
   incondicionalmente.

site.addsitedir(sitedir, known_paths=None)

   Agrega un directorio a sys.path y procesa sus archivos ".pth".
   Típicamente utilizado en "sitecustomize" o "usercustomize" (ver
   arriba).

site.getsitepackages()

   Retorna una lista que contiene todos los directorios *site-
   packages* globales.

   Added in version 3.2.

site.getuserbase()

   Retorna la ruta del directorio base del usuario "USER_BASE". Si
   este aún no fue inicializado, esta función también lo configurará,
   respetando "PYTHONUSERBASE".

   Added in version 3.2.

site.getusersitepackages()

   Retorna la ruta del directorio base del usuario "USER_SITE". Si
   este aún no fue inicializado, esta función también lo configurará,
   respetando "USER_BASE". Para determinar si los paquetes específicos
   del sitio de usuario fueron añadidos a "sys.path" debe usarse
   "ENABLE_USER_SITE".

   Added in version 3.2.

## Command-line interface

The "site" module also provides a way to get the user directories from
the command line:

   $ python -m site --user-site
   /home/user/.local/lib/python3.11/site-packages

Si se llama sin argumentos, imprimirá el contenido de "sys.path" en la
salida estándar, seguido del valor de "USER_BASE" y si el directorio
existe, entonces lo mismo para "USER_SITE", y finalmente el valor de
"ENABLE_USER_SITE".

--user-base

   Imprime la ruta al directorio base del usuario.

--user-site

   Imprime la ruta al directorio *site-packages* del usuario.

Si se dan ambas opciones, la ruta del directorio base y la del
directorio *site-packages* del usuario se imprimirán (siempre en este
orden), separados por "os.pathsep".

Si se da alguna opción, el script saldrá con uno de estos valores: "0"
si el directorio *site-packages* del usuario está habilitado, "1" si
fue deshabilitado por el usuario, "2" si está deshabilitado por
razones de seguridad o por un administrador, y un valor mayor que 2 si
hay un error.

Ver también:

  * **PEP 370** - Directorio *site-packages* de cada usuario

  * La inicialización de la ruta de búsqueda de módulo de sys.path --
    Inicialización de "sys.path".
