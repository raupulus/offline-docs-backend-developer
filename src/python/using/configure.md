---
title: 3. Configurar Python
source_url: https://docs.python.org/es/3
source_path: using/configure.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: using
order: 5050
---

# 3. Configurar Python

## 3.1. Requisitos de compilación

To build CPython, you will need:

* Un compilador C11. Características opcionales de C11 no son
  necesarias.

* En Windows, se necesita Microsoft Visual Studio 2017 o posterior.

* Support for IEEE 754 floating-point numbers and floating-point
  Not-a-Number (NaN).

* Soporte para hilos.

Distinto en la versión 3.5: On Windows, Visual Studio 2015 or later is
now required.

Distinto en la versión 3.6: Selected C99 features, like "<stdint.h>"
and "static inline" functions, are now required.

Distinto en la versión 3.7: Thread support is now required.

Distinto en la versión 3.11: C11 compiler, IEEE 754 and NaN support
are now required. On Windows, Visual Studio 2017 or later is required.

Ver también **PEP 7** "Style Guide for C Code" y **PEP 11** "CPython
platform support".

### 3.1.1. Requirements for optional modules

Some *optional modules* of the standard library require third-party
libraries installed for development (for example, header files must be
available).

Missing requirements are reported in the "configure" output. Modules
that are missing due to missing dependencies are listed near the end
of the "make" output, sometimes using an internal name, for example,
"_ctypes" for "ctypes" module.

If you distribute a CPython interpreter without optional modules, it's
best practice to advise users, who generally expect that standard
library modules are available.

Dependencies to build optional modules are:

+-----------------------------------+-----------------------------------+-----------------------------------+
| Dependency                        | Minimum version                   | Python module                     |
|===================================|===================================|===================================|
## | libbz2                            |                                   | "bz2"                             |

## | libffi                            | 3.3.0 recommended                 | "ctypes"                          |

## | liblzma                           |                                   | "lzma"                            |

## | libmpdec                          | 2.5.0                             | "decimal" [1]                     |

## | libreadline or libedit [2]        |                                   | "readline"                        |

## | libuuid                           |                                   | "_uuid" [3]                       |

## | ncurses [4]                       |                                   | "curses"                          |

| OpenSSL                           | 3.0.18 recommended (1.1.1         | "ssl", "hashlib" [5]              |
## |                                   | minimum)                          |                                   |

## | SQLite                            | 3.15.2                            | "sqlite3"                         |

## | Tcl/Tk                            | 8.5.12                            | "tkinter", IDLE, "turtle"         |

## | zlib                              | 1.2.2.1                           | "zlib", "gzip", "ensurepip"       |

## | zstd                              | 1.4.5                             | "compression.zstd"                |

[1] If *libmpdec* is not available, the "decimal" module will use a
    pure-Python implementation. See "--with-system-libmpdec" for
    details.

[2] See "--with-readline" for choosing the backend for the "readline"
    module.

[3] The "uuid" module uses "_uuid" to generate "safe" UUIDs. See the
    module documentation for details.

[4] The "curses" module requires the "libncurses" or "libncursesw"
    library. The "curses.panel" module additionally requires the
    "libpanel" or "libpanelw" library.

[5] If OpenSSL is not available, the "hashlib" module will use bundled
    implementations of several hash functions. See "--with-builtin-
    hashlib-hashes" for *forcing* usage of OpenSSL.

Note that the table does not include all optional modules; in
particular, platform-specific modules like "winreg" are not listed
here.

Ver también:

  * The devguide includes a full list of dependencies required to
    build all modules and instructions on how to install them on
    common platforms.

  * "--with-system-expat" allows building with an external libexpat
    library.

  * Options for third-party dependencies

Distinto en la versión 3.1: Tcl/Tk version 8.3.1 is now required for
"tkinter".

Distinto en la versión 3.5: Tcl/Tk version 8.4 is now required for
"tkinter".

Distinto en la versión 3.7: OpenSSL 1.0.2 is now required for
"hashlib" and "ssl".

Distinto en la versión 3.10: OpenSSL 1.1.1 is now required for
"hashlib" and "ssl". SQLite 3.7.15 is now required for "sqlite3".

Distinto en la versión 3.11: Tcl/Tk version 8.5.12 is now required for
"tkinter".

Distinto en la versión 3.13: SQLite 3.15.2 is now required for
"sqlite3".

## 3.2. Archivos generados

Para reducir las dependencias de compilación, el código fuente de
Python contiene varios archivos generados. Comandos para regenerar
todos los archivos generados:

   make regen-all
   make regen-stdlib-module-names
   make regen-limited-abi
   make regen-configure

El archivo "Makefile.pre.in" documenta archivos generados, sus
entradas y las herramientas que se usaron para regenerarlos. Busque
los objetivos make "regen-*".

### 3.2.1. configure script

The "make regen-configure" command regenerates the "aclocal.m4" file
and the "configure" script using the "Tools/build/regen-configure.sh"
shell script which uses an Ubuntu container to get the same tools
versions and have a reproducible output.

The container is optional, the following command can be run locally:

   autoreconf -ivf -Werror

The generated files can change depending on the exact versions of the
tools used. The container that CPython uses has Autoconf 2.72,
"aclocal" from Automake 1.16.5, and pkg-config 1.8.1.

Distinto en la versión 3.13: Autoconf 2.71 and aclocal 1.16.5 and are
now used to regenerate "configure".

Distinto en la versión 3.14: Autoconf 2.72 is now used to regenerate
"configure".

## 3.3. Configurar opciones

List all "configure" script options using:

   ./configure --help

Consultar también "Misc/SpecialBuilds.txt" en la distribución fuente
de Python.

### 3.3.1. Opciones generales

--enable-loadable-sqlite-extensions

   Admite extensiones cargables en el módulo de extensión "_sqlite"
   (el valor por defecto es no) del módulo "sqlite3".

   Consultar el método "sqlite3.Connection.enable_load_extension()"
   del módulo "sqlite3".

   Added in version 3.6.

--disable-ipv6

   Deshabilita la compatibilidad con IPv6 (habilitada de forma
   predeterminada si es compatible), consulte el módulo "socket".

--enable-big-digits=[15|30]

   Define el tamaño en bits de los dígitos "int" de Python: 15 o 30
   bits.

   Por defecto, el tamaño del dígito es 30.

   Define el "PYLONG_BITS_IN_DIGIT" en "15" o "30".

   Consultar "sys.int_info.bits_per_digit".

--with-suffix=SUFFIX

   Establece el sufijo ejecutable de Python en *SUFFIX*.

   El sufijo predeterminado es ".exe" en Windows y macOS (ejecutable
   "python.exe"), ".js" en el nodo Emscripten, ".html" en el navegador
   Emscripten, ".wasm" en WASI y una cadena vacía en otras plataformas
   (ejecutable "python").

   Distinto en la versión 3.11: El sufijo predeterminado en la
   plataforma WASM es uno de ".js", ".html" o ".wasm".

--with-tzpath=<list of absolute paths separated by pathsep>

   Selecciona la ruta de búsqueda de zona horaria predeterminada para
   "zoneinfo.TZPATH". Consultar la Configuración en tiempo de
   compilación del módulo "zoneinfo".

   Por defecto: "/usr/share/zoneinfo:/usr/lib/zoneinfo:/usr/share/lib
   /zoneinfo:/etc/zoneinfo".

   Consultar separador de rutas "os.pathsep" .

   Added in version 3.9.

--without-decimal-contextvar

   Construye el módulo de extensión "_decimal" usando un contexto
   local de hilos en lugar de un contexto local de corutinas
   (predeterminado), consultar el módulo "decimal".

   Consultar "decimal.HAVE_CONTEXTVAR" y el módulo "contextvars".

   Added in version 3.9.

--with-dbmliborder=<list of backend names>

   Sobrescribe el orden para verificar los de las bases datos para el
   módulo "dbm"

   Un valor válido es una cadena de caracteres separada por dos puntos
   (":") con los nombres de los backends:

   * "ndbm";

   * "gdbm";

   * "bdb".

--without-c-locale-coercion

   Deshabilita la coerción de configuración regional C a una
   configuración regional basada en UTF-8 (habilitada de forma
   predeterminada).

   No define la macro "PY_COERCE_C_LOCALE".

   Consultar "PYTHONCOERCECLOCALE" y el **PEP 538**.

--with-platlibdir=DIRNAME

   Nombre del directorio de la biblioteca de Python (por defecto es
   "lib").

   Fedora y SuSE usan "lib64" en plataformas 64-bit.

   Consultar "sys.platlibdir".

   Added in version 3.9.

--with-wheel-pkg-dir=PATH

   Directorio de los paquetes *wheel* usados por el módulo "ensurepip"
   (ninguno por defecto)

   Algunas políticas de empaquetado de distribución de Linux
   recomiendan no empaquetar dependencias. Por ejemplo, Fedora instala
   paquetes *wheel* en el directorio "/usr/share/python-wheels/" y no
   instala el paquete "ensurepip._bundled".

   Added in version 3.10.

--with-pkg-config=[check|yes|no]

   Si configure debe usar **pkg-config** para detectar dependencias de
   compilación.

   * "check" (predeterminado): **pkg-config** es opcional

   * "yes": **pkg-config** es obligatorio

   * "no": configure no usa **pkg-config** incluso cuando está
     presente

   Added in version 3.11.

--enable-pystats

   Turn on internal Python performance statistics gathering.

   By default, statistics gathering is off. Use "python3 -X pystats"
   command or set "PYTHONSTATS=1" environment variable to turn on
   statistics gathering at Python startup.

   At Python exit, dump statistics if statistics gathering was on and
   not cleared.

   Efectos:

   * Add "-X pystats" command line option.

   * Add "PYTHONSTATS" environment variable.

   * Define the "Py_STATS" macro.

   * Add functions to the "sys" module:

     * "sys._stats_on()": Turns on statistics gathering.

     * "sys._stats_off()": Turns off statistics gathering.

     * "sys._stats_clear()": Clears the statistics.

     * "sys._stats_dump()": Dump statistics to file, and clears the
       statistics.

   The statistics will be dumped to a arbitrary (probably unique) file
   in "/tmp/py_stats/" (Unix) or "C:\temp\py_stats\" (Windows). If
   that directory does not exist, results will be printed on stderr.

   Usa "Tools/scripts/summarize_stats.py" para leer las estadísticas.

   Statistics:

   * Opcode:

     * Specialization: success, failure, hit, deferred, miss, deopt,
       failures;

     * Execution count;

     * Pair count.

   * Call:

     * Inlined Python calls;

     * PyEval calls;

     * Frames pushed;

     * Frame object created;

     * Eval calls: vector, generator, legacy, function VECTORCALL,
       build class, slot, function "ex", API, method.

   * Object:

     * incref and decref;

     * interpreter incref and decref;

     * allocations: all, 512 bytes, 4 kiB, big;

     * free;

     * to/from free lists;

     * dictionary materialized/dematerialized;

     * type cache;

     * optimization attempts;

     * optimization traces created/executed;

     * uops executed.

   * Garbage collector:

     * Garbage collections;

     * Objects visited;

     * Objects collected.

   Added in version 3.11.

--disable-gil

   Enables support for running Python without the *global interpreter
   lock* (GIL): *free-threaded build*.

   Defines the "Py_GIL_DISABLED" macro and adds ""t"" to
   "sys.abiflags".

   See Free-threaded CPython for more detail.

   Added in version 3.13.

--enable-experimental-jit=[no|yes|yes-off|interpreter]

   Indicate how to integrate the experimental just-in-time compiler.

   * "no": Don't build the JIT.

   * "yes": Enable the JIT. To disable it at runtime, set the
     environment variable "PYTHON_JIT=0".

   * "yes-off": Build the JIT, but disable it by default. To enable it
     at runtime, set the environment variable "PYTHON_JIT=1".

   * "interpreter": Enable the "JIT interpreter" (only useful for
     those debugging the JIT itself). To disable it at runtime, set
     the environment variable "PYTHON_JIT=0".

   "--enable-experimental-jit=no" is the default behavior if the
   option is not provided, and "--enable-experimental-jit" is
   shorthand for "--enable-experimental-jit=yes".  See
   "Tools/jit/README.md" for more information, including how to
   install the necessary build-time dependencies.

   Nota:

     When building CPython with JIT enabled, ensure that your system
     has Python 3.11 or later installed.

   Added in version 3.13.

PKG_CONFIG

   Path to "pkg-config" utility.

PKG_CONFIG_LIBDIR

PKG_CONFIG_PATH

   "pkg-config" options.

### 3.3.2. C compiler options

CC

   Comando del compilador C.

CFLAGS

   Banderas del compilador de C.

CPP

   C preprocessor command.

CPPFLAGS

   C preprocessor flags, e.g. "-I*include_dir*".

### 3.3.3. Opciones del enlazador

LDFLAGS

   Linker flags, e.g. "-L*library_directory*".

LIBS

   Libraries to pass to the linker, e.g. "-l*library*".

MACHDEP

   Name for machine-dependent library files.

### 3.3.4. Options for third-party dependencies

Added in version 3.11.

BZIP2_CFLAGS

BZIP2_LIBS

   C compiler and linker flags to link Python to "libbz2", used by
   "bz2" module, overriding "pkg-config".

CURSES_CFLAGS

CURSES_LIBS

   C compiler and linker flags for "libncurses" or "libncursesw", used
   by "curses" module, overriding "pkg-config".

GDBM_CFLAGS

GDBM_LIBS

   C compiler and linker flags for "gdbm".

LIBEDIT_CFLAGS

LIBEDIT_LIBS

   C compiler and linker flags for "libedit", used by "readline"
   module, overriding "pkg-config".

LIBFFI_CFLAGS

LIBFFI_LIBS

   C compiler and linker flags for "libffi", used by "ctypes" module,
   overriding "pkg-config".

LIBMPDEC_CFLAGS

LIBMPDEC_LIBS

   C compiler and linker flags for "libmpdec", used by "decimal"
   module, overriding "pkg-config".

   Nota:

     These environment variables have no effect unless "--with-system-
     libmpdec" is specified.

LIBLZMA_CFLAGS

LIBLZMA_LIBS

   C compiler and linker flags for "liblzma", used by "lzma" module,
   overriding "pkg-config".

LIBREADLINE_CFLAGS

LIBREADLINE_LIBS

   C compiler and linker flags for "libreadline", used by "readline"
   module, overriding "pkg-config".

LIBSQLITE3_CFLAGS

LIBSQLITE3_LIBS

   C compiler and linker flags for "libsqlite3", used by "sqlite3"
   module, overriding "pkg-config".

LIBUUID_CFLAGS

LIBUUID_LIBS

   C compiler and linker flags for "libuuid", used by "uuid" module,
   overriding "pkg-config".

LIBZSTD_CFLAGS

LIBZSTD_LIBS

   C compiler and linker flags for "libzstd", used by
   "compression.zstd" module, overriding "pkg-config".

   Added in version 3.14.

PANEL_CFLAGS

PANEL_LIBS

   C compiler and linker flags for PANEL, overriding "pkg-config".

   C compiler and linker flags for "libpanel" or "libpanelw", used by
   "curses.panel" module, overriding "pkg-config".

TCLTK_CFLAGS

TCLTK_LIBS

   C compiler and linker flags for TCLTK, overriding "pkg-config".

ZLIB_CFLAGS

ZLIB_LIBS

   C compiler and linker flags for "libzlib", used by "gzip" module,
   overriding "pkg-config".

### 3.3.5. Opciones de WebAssembly

--enable-wasm-dynamic-linking

   Active la compatibilidad con enlaces dinámicos para WASM.

   La vinculación dinámica habilita "dlopen". El tamaño del archivo
   del ejecutable aumenta debido a la eliminación limitada de código
   muerto y características adicionales.

   Added in version 3.11.

--enable-wasm-pthreads

   Active la compatibilidad con pthreads para WASM.

   Added in version 3.11.

### 3.3.6. Opciones de instalación

--prefix=PREFIX

   Instala archivos independientes de la arquitectura en PREFIX. En
   Unix, el valor predeterminado es "/usr/local".

   Este valor se puede recuperar en tiempo de ejecución al usar
   "sys.prefix".

   Como ejemplo, se puede utilizar "--prefix="$HOME/.local/"" para
   instalar Python en su directorio raíz.

--exec-prefix=EPREFIX

   Instala archivos independientes de la arquitectura en EPREFIX, el
   valor predeterminado es "--prefix".

   Este valor se puede recuperar en tiempo de ejecución al usar
   "sys.exec_prefix".

--disable-test-modules

   No construya ni instale módulos de prueba, como el paquete "test" o
   el módulo de extensión "_testcapi" (construido e instalado por
   defecto).

   Added in version 3.10.

--with-ensurepip=[upgrade|install|no]

   Selecciona el comando "ensurepip" que se ejecuta en la instalación
   de Python:

   * "upgrade" (por defecto): ejecutar el comando "python -m ensurepip
     --altinstall --upgrade".

   * "install": ejecutar el comando "python -m ensurepip
     --altinstall";

   * "no": no ejecuta ensurepip;

   Added in version 3.6.

### 3.3.7. Opciones de desempeño

Se recomienda configurar Python usando "--enable-optimizations --with-
lto" (PGO + LTO) para obtener el mejor rendimiento. El indicador
experimental "--enable-bolt" también se puede usar para mejorar el
rendimiento.

--enable-optimizations

   Habilite la Optimización Guiada por Perfiles (*PGO* por sus siglas
   en inglés) usando "PROFILE_TASK" (deshabilitado de forma
   predeterminada).

   El compilador de C Clang requiere el programa "llvm-profdata" para
   PGO. En macOS, GCC también lo requiere: GCC es solo un alias de
   Clang en macOS.

   Desactiva también la interposición semántica en libpython si se usa
   "--enable-shared" y GCC: agregar "-fno-semantic-interposition" a
   los flags del compilador y del enlazador.

   Nota:

     During the build, you may encounter compiler warnings about
     profile data not being available for some source files. These
     warnings are harmless, as only a subset of the code is exercised
     during profile data acquisition. To disable these warnings on
     Clang, manually suppress them by adding "-Wno-profile-instr-
     unprofiled" to "CFLAGS".

   Added in version 3.6.

   Distinto en la versión 3.10: Usar "-fno-semantic-interposition" en
   GCC.

PROFILE_TASK

   Variable de entorno utilizada en el Makefile: argumentos de la
   línea de comando Python para la tarea de generación de PGO.

   Por defecto: "-m test --pgo --timeout=$(TESTTIMEOUT)".

   Added in version 3.8.

   Distinto en la versión 3.13: Task failure is no longer ignored
   silently.

--with-lto=[full|thin|no|yes]

   Habilita la Optimización de Tiempo de Enlace (*LTO* por sus siglas
   en inglés) en cualquier compilación (deshabilitado de forma
   predeterminada).

   El compilador de C Clang requiere "llvm-ar" para LTO ("ar" en
   macOS), así como un enlazador compatible con LTO ("ld.gold" o
   "lld").

   Added in version 3.6.

   Added in version 3.11: Para usar la función ThinLTO, use "--with-
   lto=thin" en Clang.

   Distinto en la versión 3.12: Utiliza ThinLTO como política de
   optimización predeterminada en Clang si el compilador acepta el
   indicador.

--enable-bolt

   Habilita el uso del optimizador binario post-enlace BOLT
   (deshabilitado de forma predeterminada).

   BOLT es parte del proyecto LLVM pero no siempre se incluye en sus
   distribuciones binarias. Este indicador necesita que "llvm-bolt" y
   "merge-fdata" estén disponibles.

   BOLT aún es un proyecto bastante nuevo, así que este indicador
   debería considerarse experimental por ahora. Debido a que esta
   herramienta opera en código máquina, su éxito depende de una
   combinación del entorno de compilación + los otros argumentos de
   configuración de optimización + la arquitectura del CPU, y no todas
   las combinaciones son compatibles. Se sabe que las versiones de
   BOLT anteriores a LLVM 16 bloquean BOLT en algunos escenarios. Se
   recomienda encarecidamente utilizar LLVM 16 o posterior para la
   optimización de BOLT.

   Las variables **configure** "BOLT_INSTRUMENT_FLAGS" y
   "BOLT_APPLY_FLAGS" se pueden definir para sobrescribir el conjunto
   predeterminado de argumentos de **llvm-bolt** para instrumentar y
   aplicar datos BOLT a binarios, respectivamente.

   Added in version 3.12.

BOLT_APPLY_FLAGS

   Arguments to "llvm-bolt" when creating a BOLT optimized binary.

   Added in version 3.12.

BOLT_INSTRUMENT_FLAGS

   Arguments to "llvm-bolt" when instrumenting binaries.

   Added in version 3.12.

--with-computed-gotos

   Habilita los *gotos* calculados en el ciclo de evaluación
   (habilitado de forma predeterminada en los compiladores
   compatibles).

--with-tail-call-interp

   Enable interpreters using tail calls in CPython. If enabled,
   enabling PGO ("--enable-optimizations") is highly recommended. This
   option specifically requires a C compiler with proper tail call
   support, and the preserve_none calling convention. For example,
   Clang 19 and newer supports this feature.

   Added in version 3.14.

--without-mimalloc

   Disable the fast mimalloc allocator (enabled by default).

   This option cannot be used together with "--disable-gil" because
   the *free-threaded* build requires mimalloc.

   Consultar también la variable de entorno "PYTHONMALLOC".

--without-pymalloc

   Deshabilita el asignador de memoria especializado de Python
   pymalloc (habilitado de forma predeterminada).

   Consultar también la variable de entorno "PYTHONMALLOC".

--without-doc-strings

   Deshabilita las cadenas de caracteres de documentación estáticas
   para reducir el espacio de memoria (habilitado de forma
   predeterminada). Las cadenas de caracteres de documentación
   definidas en Python no se ven afectadas.

   No define la macro "WITH_DOC_STRINGS".

   Consultar la macro "PyDoc_STRVAR()".

--enable-profiling

   Habilita el análisis de rendimiento de código (*profiling*) de
   nivel C con "gprof" (deshabilitado de forma predeterminada).

--with-strict-overflow

   Agrega "-fstrict-overflow" a los indicadores del compilador de C
   (el valor predeterminado que agregamos en su lugar es "-fno-strict-
   overflow").

--without-remote-debug

   Deactivate remote debugging support described in **PEP 768**
   (enabled by default). When this flag is provided the code that
   allows the interpreter to schedule the execution of a Python file
   in a separate process as described in **PEP 768** is not compiled.
   This includes both the functionality to schedule code to be
   executed and the functionality to receive code to be executed.

   Py_REMOTE_DEBUG

      This macro is defined by default, unless Python is configured
      with "--without-remote-debug".

      Note that even if the macro is defined, remote debugging may not
      be available (for example, on an incompatible platform).

   Added in version 3.14.

### 3.3.8. Compilación de depuración de Python

Una compilación de depuración es Python construido con la opción de
configuración "--with-pydebug".

Efectos de una compilación de depuración:

* Muestra todas las advertencias de forma predeterminada: la lista de
  filtros de advertencia predeterminados está vacía en el módulo
  "warnings".

* Agrega "d" a "sys.abiflags".

* Agrega la función "sys.gettotalrefcount()".

* Agrega la opción de línea de comando "-X showrefcount".

* Agrega la opción de línea de comando "-d" y la variable de entorno
  "PYTHONDEBUG" para depurar el analizador.

* Agregue soporte para la variable "__lltrace__": habilite el
  seguimiento de bajo nivel en el ciclo de evaluación del código de
  bytes si la variable está definida.

* Instala ganchos de depuración en los asignadores de memoria para
  detectar el desbordamiento del búfer y otros errores de memoria.

* Define las macros "Py_DEBUG" y "Py_REF_DEBUG".

* Agregue verificaciones de tiempo de ejecución: código rodeado por
  "#ifdef Py_DEBUG" y "#endif". Habilite las aserciones "assert(...)"
  y "_PyObject_ASSERT(...)": no configure la macro "NDEBUG" (vea
  también la opción de configuración "--with-assertions").
  Comprobaciones principales de tiempo de ejecución:

  * Agregue controles de sanidad en los argumentos de la función.

  * Los objetos unicode e int se crean con su memoria completa con un
    patrón para detectar el uso de objetos no inicializados.

  * Asegúrese de que las funciones que pueden borrar o reemplazar la
    excepción actual no se invocan con una excepción lanzada.

  * Verifique que las funciones de desasignador no cambien la
    excepción actual.

  * El recolector de basura (función "gc.collect()") ejecuta algunas
    comprobaciones básicas sobre la consistencia de los objetos.

  * La macro "Py_SAFE_DOWNCAST()" comprueba el subdesbordamiento y el
    desbordamiento de enteros al realizar una conversión descendente
    de tipos anchos a tipos estrechos.

Consultar también Modo de Desarrollo de Python y la opción de
configuración "--with-trace-refs".

Distinto en la versión 3.8: Release builds are now ABI compatible with
debug builds: defining the "Py_DEBUG" macro no longer implies the
"Py_TRACE_REFS" macro (see the "--with-trace-refs" option). However,
debug builds still expose more symbols than release builds and code
built against a debug build is not necessarily compatible with a
release build.

### 3.3.9. Opciones de depuración

--with-pydebug

   Compila Python en modo de depuración: define la macro "Py_DEBUG"
   (deshabilitada por defecto).

--with-trace-refs

   Habilita las referencias de seguimiento con fines de depuración
   (deshabilitado de forma predeterminada).

   Efectos:

   * Define la macro "Py_TRACE_REFS".

   * Add "sys.getobjects()" function.

   * Agrega la variable de entorno "PYTHONDUMPREFS".

   The "PYTHONDUMPREFS" environment variable can be used to dump
   objects and reference counts still alive at Python exit.

   Statically allocated objects are not traced.

   Added in version 3.8.

   Distinto en la versión 3.13: This build is now ABI compatible with
   release build and debug build.

--with-assertions

   Compila con las aserciones de C habilitadas (el valor
   predeterminado es no): "assert(...);" y "_PyObject_ASSERT(...);".

   Si se establece, la macro "NDEBUG" no está definida en la variable
   del compilador "OPT".

   Consultar también la opción "--with-pydebug" (compilación de
   depuración) que también habilita las aserciones.

   Added in version 3.6.

--with-valgrind

   Habilite la compatibilidad con Valgrind (el valor predeterminado es
   no).

--with-dtrace

   Habilite la compatibilidad con DTrace (el valor predeterminado es
   no).

   Consultar Instrumentación de CPython con DTrace y SystemTap.

   Added in version 3.6.

--with-address-sanitizer

   Enable AddressSanitizer memory error detector, "asan" (default is
   no). To improve ASan detection capabilities you may also want to
   combine this with "--without-pymalloc" to disable the specialized
   small-object allocator whose allocations are not tracked by ASan.

   Added in version 3.6.

--with-memory-sanitizer

   Habilita el detector de errores de asignación MemorySanitizer,
   "msan" (el valor predeterminado es no).

   Added in version 3.6.

--with-undefined-behavior-sanitizer

   Habilita el detector de comportamiento indefinido
   UndefinedBehaviorSanitizer, "ubsan" (el valor predeterminado es
   no).

   Added in version 3.6.

--with-thread-sanitizer

   Enable ThreadSanitizer data race detector, "tsan" (default is no).

   Added in version 3.13.

### 3.3.10. Opciones del enlazador

--enable-shared

   Habilita la compilación de una biblioteca compartida de Python
   :"libpython" (el valor predeterminado es no).

--without-static-libpython

   No compila "libpythonMAJOR.MINOR.a" y no instala "python.o"
   (compilado y habilitado de forma predeterminada).

   Added in version 3.10.

### 3.3.11. Opciones de bibliotecas

--with-libs='lib1 ...'

   Enlace con bibliotecas adicionales (el valor predeterminado es no).

--with-system-expat

   Compila el módulo "pyexpat" usando la biblioteca instalada "expat"
   instalada (por defecto es no).

--with-system-libmpdec

   Build the "_decimal" extension module using an installed
   "mpdecimal" library, see the "decimal" module (default is yes).

   Added in version 3.3.

   Distinto en la versión 3.13: Default to using the installed
   "mpdecimal" library.

   Distinto en la versión 3.15: A bundled copy of the library will no
   longer be selected implicitly if an installed "mpdecimal" library
   is not found. In Python 3.15 only, it can still be selected
   explicitly using "--with-system-libmpdec=no" or "--without-system-
   libmpdec".

   Deprecated since version 3.13, will be removed in version 3.16: A
   copy of the "mpdecimal" library sources will no longer be
   distributed with Python 3.16.

   Ver también: "LIBMPDEC_CFLAGS" and "LIBMPDEC_LIBS".

--with-readline=readline|editline

   Designate a backend library for the "readline" module.

   * readline: Use readline as the backend.

   * editline: Use editline as the backend.

   Added in version 3.10.

--without-readline

   No cree el módulo "readline" (es construido por defecto).

   No defina la macro "HAVE_LIBREADLINE".

   Added in version 3.10.

--with-libm=STRING

   Sobreescribe la biblioteca matemática "libm" a *STRING* (el valor
   predeterminado es dependiente del sistema).

--with-libc=STRING

   Sobreescribe la biblioteca C "libc" a *STRING* (el valor
   predeterminado es dependiente del sistema).

--with-openssl=DIR

   Raíz del directorio OpenSSL.

   Added in version 3.7.

--with-openssl-rpath=[no|auto|DIR]

   Configura el directorio de la biblioteca en tiempo de ejecución
   (rpath) para las bibliotecas OpenSSL:

   * "no" (por defecto): no establece rpath;

   * "auto": autodetecta rpath desde "--with-openssl" y "pkg-config";

   * *DIR*: establece un rpath explícito.

   Added in version 3.10.

### 3.3.12. Opciones de seguridad

--with-hash-algorithm=[fnv|siphash13|siphash24]

   Selecciona el algoritmo hash para usar en "Python/pyhash.c":

   * "siphash13" (por defecto);

   * "siphash24";

   * "fnv".

   Added in version 3.4.

   Added in version 3.11: Se agrega "siphash13" y es el nuevo valor
   predeterminado.

--with-builtin-hashlib-hashes=md5,sha1,sha256,sha512,sha3,blake2

   Módulos hash incorporados:

   * "md5";

   * "sha1";

   * "sha256";

   * "sha512";

   * "sha3" (con shake);

   * "blake2".

   Added in version 3.9.

--with-ssl-default-suites=[python|openssl|STRING]

   Sobreescribe la cadena de conjuntos de cifrado predeterminada de
   OpenSSL:

   * "python" (por defecto): usa la selección principal de Python;

   * "openssl": deja intactos los valores predeterminados de OpenSSL;

   * *STRING*: usa una cadena de caracteres personalizada

   Consultar el módulo "ssl".

   Added in version 3.7.

   Distinto en la versión 3.10: Las configuraciones "python" y
   *STRING* también establecen TLS 1.2 como versión mínima del
   protocolo.

--disable-safety

   Disable compiler options that are recommended by OpenSSF for
   security reasons with no performance overhead. If this option is
   not enabled, CPython will be built based on safety compiler options
   with no slow down. When this option is enabled, CPython will not be
   built with the compiler options listed below.

   The following compiler options are disabled with "--disable-
   safety":

   * -fstack-protector-strong: Enable run-time checks for stack-based
     buffer overflows.

   * -Wtrampolines: Enable warnings about trampolines that require
     executable stacks.

   Added in version 3.14.

--enable-slower-safety

   Enable compiler options that are recommended by OpenSSF for
   security reasons which require overhead. If this option is not
   enabled, CPython will not be built based on safety compiler options
   which performance impact. When this option is enabled, CPython will
   be built with the compiler options listed below.

   The following compiler options are enabled with "--enable-slower-
   safety":

   * -D_FORTIFY_SOURCE=3: Fortify sources with compile- and run-time
     checks for unsafe libc usage and buffer overflows.

   Added in version 3.14.

### 3.3.13. Opciones macOS

See Mac/README.rst.

--enable-universalsdk

--enable-universalsdk=SDKDIR

   Crea una compilación binaria universal. *SDKDIR* especifica qué
   macOS SDK debe usarse para realizar la compilación (el valor
   predeterminado es no).

--enable-framework

--enable-framework=INSTALLDIR

   Crear un Python.framework en lugar de una instalación Unix
   tradicional. Opcionalmente *INSTALLDIR* especifica la ruta de
   instalación (el valor predeterminado es no).

--with-universal-archs=ARCH

   Especifique el tipo de binario universal que se debe crear. Esta
   opción solo es válida cuando se establece "--enable-universalsdk".

   Opciones:

   * "universal2" (x86-64 and arm64);

   * "32-bit" (PPC and i386);

   * "64-bit"  (PPC64 and x86-64);

   * "3-way" (i386, PPC and x86-64);

   * "intel" (i386 and x86-64);

   * "intel-32" (i386);

   * "intel-64" (x86-64);

   * "all"  (PPC, i386, PPC64 and x86-64).

   Note that values for this configuration item are *not* the same as
   the identifiers used for universal binary wheels on macOS. See the
   Python Packaging User Guide for details on the packaging platform
   compatibility tags used on macOS

--with-framework-name=FRAMEWORK

   Especifica el nombre del framework de Python en macOS, solo es
   válido cuando "--enable-framework" está configurada (por defecto:
   "Python").

--with-app-store-compliance

--with-app-store-compliance=PATCH-FILE

   The Python standard library contains strings that are known to
   trigger automated inspection tool errors when submitted for
   distribution by the macOS and iOS App Stores. If enabled, this
   option will apply the list of patches that are known to correct app
   store compliance. A custom patch file can also be specified. This
   option is disabled by default.

   Added in version 3.13.

### 3.3.14. iOS Options

See iOS/README.rst.

--enable-framework=INSTALLDIR

   Create a Python.framework. Unlike macOS, the *INSTALLDIR* argument
   specifying the installation path is mandatory.

--with-framework-name=FRAMEWORK

   Specify the name for the framework (default: "Python").

### 3.3.15. Opciones de compilación cruzada

La compilación cruzada, también conocida como construcción cruzada, se
puede usar para construir Python para otra plataforma o arquitectura
de CPU. La compilación cruzada requiere un intérprete de Python para
la plataforma de compilación. La versión de Python de compilación debe
coincidir con la versión de Python host de compilación cruzada.

--build=BUILD

   configure para construir en BUILD, generalmente adivinado por
   **config.guess**.

--host=HOST

   compilación cruzada para crear programas que se ejecuten en HOST
   (plataforma de destino)

--with-build-python=path/to/python

   ruta para construir el binario "python" para compilación cruzada

   Added in version 3.11.

CONFIG_SITE=file

   Una variable de entorno que apunta a un archivo con anulaciones de
   configuración.

   Example *config.site* file:

      # config.site-aarch64
      ac_cv_buggy_getaddrinfo=no
      ac_cv_file__dev_ptmx=yes
      ac_cv_file__dev_ptc=no

HOSTRUNNER

   Program to run CPython for the host platform for cross-compilation.

   Added in version 3.11.

Ejemplo de compilación cruzada:

   CONFIG_SITE=config.site-aarch64 ../configure \
       --build=x86_64-pc-linux-gnu \
       --host=aarch64-unknown-linux-gnu \
       --with-build-python=../x86_64/python

## 3.4. Sistema de compilación Python

### 3.4.1. Archivos principales del sistema de compilación

* "configure.ac" => "configure";

* "Makefile.pre.in" => "Makefile" (creado por "configure");

* "pyconfig.h" (creado por "configure");

* "Modules/Setup": Extensiones C creadas por Makefile usando el script
  de shell "Module/makesetup";

### 3.4.2. Pasos principales de compilación

* Los archivos C (".c") se crean como archivos objeto (".o").

* La biblioteca estática "libpython" (".a") se crea a a partir de
  archivos de objetos.

* "python.o" y la biblioteca estática "libpython" están enlazadas al
  programa final "python".

* Las extensiones C son creadas por Makefile (ver "Modules/Setup").

### 3.4.3. Objetivos principales de Makefile

#### 3.4.3.1. make

For the most part, when rebuilding after editing some code or
refreshing your checkout from upstream, all you need to do is execute
"make", which (per Make's semantics) builds the default target, the
first one defined in the Makefile.  By tradition (including in the
CPython project) this is usually the "all" target. The "configure"
script expands an "autoconf" variable, "@DEF_MAKE_ALL_RULE@" to
describe precisely which targets "make all" will build. The three
choices are:

* "profile-opt" (configured with "--enable-optimizations")

* "build_wasm" (chosen if the host platform matches "wasm32-wasi*" or
  "wasm32-emscripten")

* "build_all" (configured without explicitly using either of the
  others)

Depending on the most recent source file changes, Make will rebuild
any targets (object files and executables) deemed out-of-date,
including running "configure" again if necessary. Source/target
dependencies are many and maintained manually however, so Make
sometimes doesn't have all the information necessary to correctly
detect all targets which need to be rebuilt.  Depending on which
targets aren't rebuilt, you might experience a number of problems. If
you have build or test problems which you can't otherwise explain,
"make clean && make" should work around most dependency problems, at
the expense of longer build times.

#### 3.4.3.2. make platform

Build the "python" program, but don't build the standard library
extension modules. This generates a file named "platform" which
contains a single line describing the details of the build platform,
e.g., "macosx-14.3-arm64-3.12" or "linux-x86_64-3.13".

#### 3.4.3.3. make profile-opt

Build Python using profile-guided optimization (PGO).  You can use the
configure "--enable-optimizations" option to make this the default
target of the "make" command ("make all" or just "make").

#### 3.4.3.4. make clean

Remove built files.

#### 3.4.3.5. make distclean

In addition to the work done by "make clean", remove files created by
the configure script.  "configure" will have to be run before building
again. [6]

#### 3.4.3.6. make install

Build the "all" target and install Python.

#### 3.4.3.7. make test

Build the "all" target and run the Python test suite with the "--fast-
ci" option without GUI tests. Variables:

* "TESTOPTS": additional regrtest command-line options.

* "TESTPYTHONOPTS": additional Python command-line options.

* "TESTTIMEOUT": timeout in seconds (default: 10 minutes).

#### 3.4.3.8. make ci

This is similar to "make test", but uses the "-ugui" to also run GUI
tests.

Added in version 3.14.

#### 3.4.3.9. make buildbottest

This is similar to "make test", but uses the "--slow-ci" option and
default timeout of 20 minutes, instead of "--fast-ci" option.

#### 3.4.3.10. make regen-all

Regenerate (almost) all generated files. These include (but are not
limited to) bytecode cases, and parser generator file. "make regen-
stdlib-module-names" and "autoconf" must be run separately for the
remaining generated files.

### 3.4.4. Extensiones C

Some C extensions are built as built-in modules, like the "sys"
module. They are built with the "Py_BUILD_CORE_BUILTIN" macro defined.
Built-in modules have no "__file__" attribute:

   >>> import sys
   >>> sys
   <module 'sys' (built-in)>
   >>> sys.__file__
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   AttributeError: module 'sys' has no attribute '__file__'

Other C extensions are built as dynamic libraries, like the "_asyncio"
module. They are built with the "Py_BUILD_CORE_MODULE" macro defined.
Example on Linux x86-64:

   >>> import _asyncio
   >>> _asyncio
   <module '_asyncio' from '/usr/lib64/python3.9/lib-dynload/_asyncio.cpython-39-x86_64-linux-gnu.so'>
   >>> _asyncio.__file__
   '/usr/lib64/python3.9/lib-dynload/_asyncio.cpython-39-x86_64-linux-gnu.so'

"Modules/Setup" se usa para generar objetivos Makefile para compilar
extensiones C. Al principio de los archivos, las extensiones C se
crean como módulos incorporados. Las extensiones definidas después del
marcador "*shared*" se crean como bibliotecas dinámicas.

Las macros "PyAPI_FUNC()", "PyAPI_DATA()" y "PyMODINIT_FUNC" de
"Include/exports.h" se definen de manera diferente dependiendo si es
definida la macro "Py_BUILD_CORE_MODULE":

* Use "Py_EXPORTED_SYMBOL" si "Py_BUILD_CORE_MODULE" es definido

* Use "Py_IMPORTED_SYMBOL" de lo contrario.

Si la macro "Py_BUILD_CORE_BUILTIN" se usa por error en una extensión
de C compilada como una biblioteca compartida, su función
"PyInit_*xxx*()" no se exporta, provocando un "ImportError" en la
importación.

## 3.5. Banderas de compilador y vinculación

Opciones establecidas por el script "./configure" y las variables de
entorno y utilizadas por "Makefile".

### 3.5.1. Banderas del preprocesador

CONFIGURE_CPPFLAGS

   Valor de la variable "CPPFLAGS" pasado al script "./configure".

   Added in version 3.6.

CPPFLAGS

   (Objetivo) Indicadores del preprocesador C/C++, p. ej.
   "-I*include_dir*" si tiene encabezados en un directorio no estándar
   *include_dir*.

   Ambos "CPPFLAGS" y "LDFLAGS" necesitan contener el valor del shell
   para poder compilar módulos de extensión usando los directorios
   especificados en las variables de entorno.

BASECPPFLAGS

   Added in version 3.4.

PY_CPPFLAGS

   Se agregaron indicadores de preprocesador adicionales para
   construir los archivos de objeto del intérprete.

   Por defecto: "$(BASECPPFLAGS) -I. -I$(srcdir)/Include
   $(CONFIGURE_CPPFLAGS) $(CPPFLAGS)".

   Added in version 3.2.

### 3.5.2. Banderas del compilador

CC

   Comando del compilador C.

   Ejemplo: "gcc -pthread".

CXX

   Comando del compilador de C++.

   Ejemplo: "g++ -pthread".

CFLAGS

   Banderas del compilador de C.

CFLAGS_NODIST

   "CFLAGS_NODIST" se usa para compilar el intérprete y las
   extensiones stdlib C. Úselo cuando un indicador del compilador *no*
   deba ser parte de "CFLAGS" una vez que Python esté instalado
   (gh-65320).

   En particular, "CFLAGS" no debe contener:

   * el indicador del compilador "-I" (para configurar la ruta de
     búsqueda de archivos de inclusión). Los indicadores "-I" se
     procesan de izquierda a derecha, y cualquier indicador en
     "CFLAGS" tendrá prioridad sobre los indicadores "-I"
     proporcionados por el usuario y el paquete.

   * banderas de endurecimiento como "-Werror" porque las
     distribuciones no pueden controlar si los paquetes instalados por
     los usuarios cumplen con estándares tan elevados.

   Added in version 3.5.

COMPILEALL_OPTS

   Las opciones pasadas a la línea de comando "compileall" al crear
   archivos PYC en "make install". El valor predeterminado: "-j0".

   Added in version 3.12.

EXTRA_CFLAGS

   Banderas adicionales del compilador de C.

CONFIGURE_CFLAGS

   Valor de la variable "CFLAGS" pasada al script "./configure".

   Added in version 3.2.

CONFIGURE_CFLAGS_NODIST

   Valor de la variable "CFLAGS_NODIST" pasada al script
   "./configure".

   Added in version 3.5.

BASECFLAGS

   Banderas base del compilador.

OPT

   Banderas de optimización.

CFLAGS_ALIASING

   Banderas de alias estrictos o no estrictos que se utilizan para
   compilar "Python/dtoa.c".

   Added in version 3.7.

CFLAGS_CEVAL

   Flags used to compile "Python/ceval.c".

   Added in version 3.14.5.

CCSHARED

   Banderas del compilador que se utilizan para compilar una
   biblioteca compartida.

   Por ejemplo, "-fPIC" se usa en Linux y BSD.

CFLAGSFORSHARED

   Se agregaron banderas C adicionales para compilar los archivos de
   objeto del intérprete.

   Por defecto: "$(CCSHARED)" cuando se usa "--enable-shared", o una
   cadena de caracteres vacía en caso contrario.

PY_CFLAGS

   Por defecto: "$(BASECFLAGS) $(OPT) $(CONFIGURE_CFLAGS) $(CFLAGS)
   $(EXTRA_CFLAGS)".

PY_CFLAGS_NODIST

   Por defecto: "$(CONFIGURE_CFLAGS_NODIST) $(CFLAGS_NODIST)
   -I$(srcdir)/Include/internal".

   Added in version 3.5.

PY_STDMODULE_CFLAGS

   Banderas de C que se utilizan para compilar los archivos de objeto
   del intérprete.

   Por defecto: "$(PY_CFLAGS) $(PY_CFLAGS_NODIST) $(PY_CPPFLAGS)
   $(CFLAGSFORSHARED)".

   Added in version 3.7.

PY_CORE_CFLAGS

   Por defecto: "$(PY_STDMODULE_CFLAGS) -DPy_BUILD_CORE".

   Added in version 3.2.

PY_BUILTIN_MODULE_CFLAGS

   Banderas del compilador para construir un módulo de extensión de
   biblioteca estándar como un módulo incorporado, como el módulo
   "posix".

   Por defecto: "$(PY_STDMODULE_CFLAGS) -DPy_BUILD_CORE_BUILTIN".

   Added in version 3.8.

PURIFY

   Comando Purify. Purify es un programa de depuración de memoria.

   Por defecto: cadena de caracteres vacía (no utilizado).

### 3.5.3. Banderas de vinculación

LINKCC

   Comando de vinculación usado para compilar programas como "python"
   y "_testembed".

   Por defecto: "$(PURIFY) $(CC)".

CONFIGURE_LDFLAGS

   Valor de la variable "LDFLAGS" pasada al script "./configure".

   Evite asignar "CFLAGS", "LDFLAGS", etc. así los usuarios pueden
   usarlos en la línea de comando para agregar estos valores sin pisar
   los valores preestablecidos.

   Added in version 3.2.

LDFLAGS_NODIST

   "LDFLAGS_NODIST" se usa de la misma manera que "CFLAGS_NODIST".
   Usar cuando un indicador del enlazador *no* deba ser parte de
   "LDFLAGS" una vez que Python esté instalado (gh-65320).

   En particular, "LDFLAGS" no debe contener:

   * el indicador del compilador "-L" (para establecer la ruta de
     búsqueda de bibliotecas). Los indicadores "-L" se procesan de
     izquierda a derecha, y cualquier indicador en "LDFLAGS" tendrá
     prioridad sobre los indicadores "-L" proporcionados por el
     usuario y el paquete.

CONFIGURE_LDFLAGS_NODIST

   Valor de la variable "LDFLAGS_NODIST" pasado al script
   "./configure".

   Added in version 3.8.

LDFLAGS

   Indicadores de vinculación, p. ej. "-L*lib_dir*" si tiene
   bibliotecas en un directorio no estándar *lib_dir*.

   Ambos "CPPFLAGS" y "LDFLAGS" necesitan contener el valor del shell
   para poder compilar módulos de extensión usando los directorios
   especificados en las variables de entorno.

LIBS

   Banderas de vinculación para pasar bibliotecas al vinculador al
   enlazar el ejecutable de Python.

   Ejemplo: "-lrt".

LDSHARED

   Comando para construir una biblioteca compartida.

   Por defecto: "@LDSHARED@ $(PY_LDFLAGS)".

BLDSHARED

   Comando para compilar la biblioteca compartida "libpython".

   Por defecto: "@BLDSHARED@ $(PY_CORE_LDFLAGS)".

PY_LDFLAGS

   Por defecto: "$(CONFIGURE_LDFLAGS) $(LDFLAGS)".

PY_LDFLAGS_NODIST

   Por defecto: "$(CONFIGURE_LDFLAGS_NODIST) $(LDFLAGS_NODIST)".

   Added in version 3.8.

PY_CORE_LDFLAGS

   Banderas de vinculación que se utilizan para crear los archivos de
   objeto del intérprete.

   Added in version 3.8.

-[ Footnotes ]-

[6] "git clean -fdx" is an even more extreme way to "clean" your
    checkout. It removes all files not known to Git. When bug hunting
    using "git bisect", this is recommended between probes to
    guarantee a completely clean build. **Use with care**, as it will
    delete all files not checked into Git, including your new,
    uncommitted work.
