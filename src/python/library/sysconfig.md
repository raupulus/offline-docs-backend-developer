---
title: '"sysconfig" --- Provide access to Python''s configuration information'
source_url: https://docs.python.org/es/3
source_path: library/sysconfig.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4030
---

# "sysconfig" --- Provide access to Python's configuration information

Added in version 3.2.

**Source code:** Lib/sysconfig

======================================================================

The "sysconfig" module provides access to Python's configuration
information like the list of installation paths and the configuration
variables relevant for the current platform.

## Variables de configuración

A Python distribution contains a "Makefile" and a "pyconfig.h" header
file that are necessary to build both the Python binary itself and
third-party C extensions compiled using "setuptools".

"sysconfig" puts all variables found in these files in a dictionary
that can be accessed using "get_config_vars()" or "get_config_var()".

Tenga en cuenta que en Windows, es un conjunto mucho más pequeño.

sysconfig.get_config_vars(*args)

   Sin argumentos, retorna un diccionario de todas las variables de
   configuración relevantes para la plataforma actual.

   Con argumentos, retorna un lista de valores que resultan de buscar
   cada argumento en el diccionario de variables de configuración.

   Por cada argumento, si no se encuentra el valor, retorna "None".

sysconfig.get_config_var(name)

   Retorna el valor de un solo nombre de variable (*name*).
   Equivalente a "get_config_vars().get(name)".

   Si no se encuentra *name*, retorna "None".

Ejemplos de uso:

   >>> import sysconfig
   >>> sysconfig.get_config_var('Py_ENABLE_SHARED')
   0
   >>> sysconfig.get_config_var('LIBDIR')
   '/usr/local/lib'
   >>> sysconfig.get_config_vars('AR', 'CXX')
   ['ar', 'g++']

## Rutas de instalación

Python uses an installation scheme that differs depending on the
platform and on the installation options.  These schemes are stored in
"sysconfig" under unique identifiers based on the value returned by
"os.name". The schemes are used by package installers to determine
where to copy files to.

Python actualmente admite nueve esquemas:

* *posix_prefix*: esquema para plataformas POSIX como Linux o macOS.
  Este es el esquema predeterminado que se usa cuando se instala
  Python o un componente.

* *posix_home*: scheme for POSIX platforms, when the *home* option is
  used. This scheme defines paths located under a specific home
  prefix.

* *posix_user*: scheme for POSIX platforms, when the *user* option is
  used. This scheme defines paths located under the user's home
  directory ("site.USER_BASE").

* *posix_venv*: scheme for "Python virtual environments" on POSIX
  platforms; by default it is the same as *posix_prefix*.

* *nt*: scheme for Windows. This is the default scheme used when
  Python or a component is installed.

* *nt_user*: scheme for Windows, when the *user* option is used.

* *nt_venv*: scheme for "Python virtual environments" on Windows; by
  default it is the same as *nt*.

* *venv*: a scheme with values from either *posix_venv* or *nt_venv*
  depending on the platform Python runs on.

* *nt_user*: esquema para macOS, cuando se usa la opción *user*.

Cada esquema está compuesto por una serie de rutas y cada ruta tiene
un identificador único. Python actualmente usa ocho rutas:

* *stdlib*: directorio que contiene los archivos de la biblioteca
  estándar de Python que no son específicos de la plataforma.

* *platstdlib*: directorio que contiene los archivos de la biblioteca
  estándar de Python que son específicos de la plataforma.

* *platlib*: directorio para archivos específicos del sitio,
  específicos de la plataforma.

* *purelib*: directory for site-specific, non-platform-specific files
  ('pure' Python).

* *include*: directorio para plataformas no especificadas para
  archivos de encabezado de Python C-API.

* *include*: directorio para plataformas especificadas para archivos
  de encabezado de Python C-API.

* *scripts*: directorio para archivos de script.

* *data*: directorio para archivos de datos.

## User scheme

This scheme is designed to be the most convenient solution for users
that don't have write permission to the global site-packages directory
or don't want to install into it.

Files will be installed into subdirectories of "site.USER_BASE"
(written as "*userbase*" hereafter).  This scheme installs pure Python
modules and extension modules in the same location (also known as
"site.USER_SITE").

### "posix_user"

+----------------+-------------------------------------------------------------+
| Path           | Installation directory                                      |
|================|=============================================================|
## | *stdlib*       | "*userbase*/lib/python*X.Y*"                                |

## | *platstdlib*   | "*userbase*/lib/python*X.Y*"                                |

## | *platlib*      | "*userbase*/lib/python*X.Y*/site-packages"                  |

## | *purelib*      | "*userbase*/lib/python*X.Y*/site-packages"                  |

## | *include*      | "*userbase*/include/python*X.Y*"                            |

## | *scripts*      | "*userbase*/bin"                                            |

## | *data*         | "*userbase*"                                                |

### "nt_user"

+----------------+-------------------------------------------------------------+
| Path           | Installation directory                                      |
|================|=============================================================|
## | *stdlib*       | "*userbase*\Python*XY*"                                     |

## | *platstdlib*   | "*userbase*\Python*XY*"                                     |

## | *platlib*      | "*userbase*\Python*XY*\site-packages"                       |

## | *purelib*      | "*userbase*\Python*XY*\site-packages"                       |

## | *include*      | "*userbase*\Python*XY*\Include"                             |

## | *scripts*      | "*userbase*\Python*XY*\Scripts"                             |

## | *data*         | "*userbase*"                                                |

### "osx_framework_user"

+----------------+-------------------------------------------------------------+
| Path           | Installation directory                                      |
|================|=============================================================|
## | *stdlib*       | "*userbase*/lib/python"                                     |

## | *platstdlib*   | "*userbase*/lib/python"                                     |

## | *platlib*      | "*userbase*/lib/python/site-packages"                       |

## | *purelib*      | "*userbase*/lib/python/site-packages"                       |

## | *include*      | "*userbase*/include/python*X.Y*"                            |

## | *scripts*      | "*userbase*/bin"                                            |

## | *data*         | "*userbase*"                                                |

## Home scheme

The idea behind the "home scheme" is that you build and maintain a
personal stash of Python modules.  This scheme's name is derived from
the idea of a "home" directory on Unix, since it's not unusual for a
Unix user to make their home directory have a layout similar to
"/usr/" or "/usr/local/". This scheme can be used by anyone,
regardless of the operating system they are installing for.

### "posix_home"

+----------------+-------------------------------------------------------------+
| Path           | Installation directory                                      |
|================|=============================================================|
## | *stdlib*       | "*home*/lib/python"                                         |

## | *platstdlib*   | "*home*/lib/python"                                         |

## | *platlib*      | "*home*/lib/python"                                         |

## | *purelib*      | "*home*/lib/python"                                         |

## | *include*      | "*home*/include/python"                                     |

## | *platinclude*  | "*home*/include/python"                                     |

## | *scripts*      | "*home*/bin"                                                |

## | *data*         | "*home*"                                                    |

## Prefix scheme

The "prefix scheme" is useful when you wish to use one Python
installation to perform the build/install (i.e., to run the setup
script), but install modules into the third-party module directory of
a different Python installation (or something that looks like a
different Python installation).  If this sounds a trifle unusual, it
is---that's why the user and home schemes come before.  However, there
are at least two known cases where the prefix scheme will be useful.

First, consider that many Linux distributions put Python in "/usr",
rather than the more traditional "/usr/local".  This is entirely
appropriate, since in those cases Python is part of "the system"
rather than a local add-on. However, if you are installing Python
modules from source, you probably want them to go in
"/usr/local/lib/python2.*X*" rather than "/usr/lib/python2.*X*".

Another possibility is a network filesystem where the name used to
write to a remote directory is different from the name used to read
it: for example, the Python interpreter accessed as
"/usr/local/bin/python" might search for modules in
"/usr/local/lib/python2.*X*", but those modules would have to be
installed to, say, "/mnt/*@server*/export/lib/python2.*X*".

### "posix_prefix"

+----------------+------------------------------------------------------------+
| Path           | Installation directory                                     |
|================|============================================================|
## | *stdlib*       | "*prefix*/lib/python*X.Y*"                                 |

## | *platstdlib*   | "*prefix*/lib/python*X.Y*"                                 |

## | *platlib*      | "*prefix*/lib/python*X.Y*/site-packages"                   |

## | *purelib*      | "*prefix*/lib/python*X.Y*/site-packages"                   |

## | *include*      | "*prefix*/include/python*X.Y*"                             |

## | *platinclude*  | "*prefix*/include/python*X.Y*"                             |

## | *scripts*      | "*prefix*/bin"                                             |

## | *data*         | "*prefix*"                                                 |

### "nt"

+----------------+------------------------------------------------------------+
| Path           | Installation directory                                     |
|================|============================================================|
## | *stdlib*       | "*prefix*\Lib"                                             |

## | *platstdlib*   | "*prefix*\Lib"                                             |

## | *platlib*      | "*prefix*\Lib\site-packages"                               |

## | *purelib*      | "*prefix*\Lib\site-packages"                               |

## | *include*      | "*prefix*\Include"                                         |

## | *platinclude*  | "*prefix*\Include"                                         |

## | *scripts*      | "*prefix*\Scripts"                                         |

## | *data*         | "*prefix*"                                                 |

## Installation path functions

"sysconfig" provides some functions to determine these installation
paths.

sysconfig.get_scheme_names()

   Return a tuple containing all schemes currently supported in
   "sysconfig".

sysconfig.get_default_scheme()

   Retorna el nombre del esquema predeterminado para la plataforma
   actual.

   Added in version 3.10: Esta función se llamaba anteriormente
   "_get_default_scheme()" y se consideraba un detalle de
   implementación.

   Distinto en la versión 3.11: Cuando Python se ejecuta desde un
   entorno virtual, este retorna el esquema *venv*.

sysconfig.get_preferred_scheme(key)

   Retorna un nombre de esquema preferido para un diseño de
   instalación especificado por *key*.

   *key* debe ser ""prefix"", ""home"" o ""user"".

   The return value is a scheme name listed in "get_scheme_names()".
   It can be passed to "sysconfig" functions that take a *scheme*
   argument, such as "get_paths()".

   Added in version 3.10.

   Distinto en la versión 3.11: Cuando Python se ejecuta desde un
   entorno virtual con "key="prefix"", este retorna el esquema *venv*.

sysconfig._get_preferred_schemes()

   Retorna un diccionario que contiene los nombres de los esquemas
   preferidos en la plataforma actual. Los implementadores y
   redistribuidores de Python pueden agregar sus esquemas preferidos
   al valor global de nivel de módulo "_INSTALL_SCHEMES" y modificar
   esta función para devolver esos nombres de esquema, p. Ej.
   proporcionan diferentes esquemas para que los utilicen los
   administradores de paquetes de idioma y sistema, de modo que los
   paquetes instalados por uno no se mezclen con los del otro.

   End users should not use this function, but "get_default_scheme()"
   and "get_preferred_scheme()" instead.

   Added in version 3.10.

sysconfig.get_path_names()

   Return a tuple containing all path names currently supported in
   "sysconfig".

sysconfig.get_path(name[, scheme[, vars[, expand]]])

   Retorna una ruta de instalación correspondiente a la ruta *name*,
   del esquema de instalación denominado *scheme*.

   *name* tiene que ser un valor de la lista retornado por
   "get_path_names()".

   "sysconfig" stores installation paths corresponding to each path
   name, for each platform, with variables to be expanded.  For
   instance the *stdlib* path for the *nt* scheme is: "{base}/Lib".

   "get_path()" utilizará las variables retornadas por
   "get_config_vars()" para expandir la ruta. Todas las variables
   tienen valores predeterminados para cada plataforma, por lo que se
   puede llamar a esta función y obtener el valor predeterminado.

   Si se proporciona el esquema (*scheme*), debe ser un valor de la
   lista retornada por "get_scheme_names()". De lo contrario, se
   utiliza el esquema predeterminado para la plataforma actual.

   If *vars* is provided, it must be a dictionary of variables that
   will update the dictionary returned by "get_config_vars()".

   Si *expand* se establece en "False", la ruta no se expandirá usando
   las variables.

   Si no se encuentra *name*, lanza un "KeyError".

sysconfig.get_paths([scheme[, vars[, expand]]])

   Retorna un diccionario de contiene todas las rutas de instalación
   correspondientes a un esquema de instalación. Consulte "get_path()"
   para obtener más información.

   Si no se proporciona el esquema (*scheme*), utilizará el esquema
   predeterminado para la plataforma actual.

   Si se proporciona *vars*, debe ser un diccionario de variables que
   actualizará el diccionario utilizado para expandir las rutas.

   Si *expand* se establece en falso, las rutas no se expandirán.

   Si *scheme* no es un esquema existente, "get_paths()" lanzará un
   "KeyError".

## Otras funciones

sysconfig.get_python_version()

   Retorna el número de versión versión "MAJOR.MINOR" de Python como
   una cadena. Similar a "'%d.%d' % sys.version_info[:2]".

sysconfig.get_platform()

   Retorna una cadena que identifica la plataforma actual.

   This is used mainly to distinguish platform-specific build
   directories and platform-specific built distributions.  Typically
   includes the OS name and version and the architecture (as supplied
   by "os.uname()"), although the exact information included depends
   on the OS; e.g., on Linux, the kernel version isn't particularly
   important.

   Ejemplo de valores retornados:

   Windows:

   * win-amd64 (64-bit Windows on AMD64, aka x86_64, Intel64, and
     EM64T)

   * win-arm64 (64-bit Windows on ARM64, aka AArch64)

   * win32 (todos los demás - específicamente se retorna sys.platform)

   POSIX based OS:

   * linux-x86_64

   * macosx-15.5-arm64

   * macosx-26.0-universal2 (macOS on Apple Silicon or Intel)

   * android-24-arm64_v8a

   Para otras plataformas que no son POSIX, actualmente solo retorna
   "sys.platform".

sysconfig.is_python_build()

   Retorna "True" si el intérprete de Python en ejecución se compiló a
   partir de la fuente y se está ejecutando desde su ubicación
   compilada, y no desde una ubicación resultante de por ejemplo
   ejecutando "make install" o instalando a través de un instalador
   binario.

sysconfig.parse_config_h(fp[, vars])

   Analiza un archivo de estilo "config.h".

   *fp* es un objeto similar a un archivo que apunta al archivo
   similar a "config.h".

   Se retorna un diccionario que contiene pares de nombre/valor. Si se
   pasa un diccionario opcional como un segundo argumento, se utiliza
   en lugar de un nuevo diccionario y se actualiza con los valores
   leídos en el archivo.

sysconfig.get_config_h_filename()

   Retorna la ruta de "pyconfig.h".

sysconfig.get_makefile_filename()

   Retorna la ruta de "Makefile".

## Command-line usage

You can use "sysconfig" as a script with Python's *-m* option:

   $ python -m sysconfig
   Platform: "macosx-10.4-i386"
   Python version: "3.2"
   Current installation scheme: "posix_prefix"

   Paths:
           data = "/usr/local"
           include = "/Users/tarek/Dev/svn.python.org/py3k/Include"
           platinclude = "."
           platlib = "/usr/local/lib/python3.2/site-packages"
           platstdlib = "/usr/local/lib/python3.2"
           purelib = "/usr/local/lib/python3.2/site-packages"
           scripts = "/usr/local/bin"
           stdlib = "/usr/local/lib/python3.2"

   Variables:
           AC_APPLE_UNIVERSAL_BUILD = "0"
           AIX_GENUINE_CPLUSPLUS = "0"
           AR = "ar"
           ARFLAGS = "rc"
           ...

Esta llamada imprimirá en la salida estándar la información retornada
por "get_platform()", "get_python_version()", "get_path()" y
"get_config_vars()".
