---
title: Configuración de inicialización de Python
source_url: https://docs.python.org/es/3
source_path: c-api/init_config.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 370
---

# Configuración de inicialización de Python

## PyInitConfig C API

Added in version 3.14.

Python can be initialized with "Py_InitializeFromInitConfig()".

La función "Py_RunMain()" se puede utilizar para escribir un programa
Python personalizado.

Consulte también Inicialización, finalización y subprocesos.

Ver también: **PEP 741** "Python Configuration C API".

### Ejemplo

Example of customized Python always running with the Python
Development Mode enabled; return "-1" on error:

   int init_python(void)
   {
       PyInitConfig *config = PyInitConfig_Create();
       if (config == NULL) {
           printf("PYTHON INIT ERROR: memory allocation failed\n");
           return -1;
       }

       // Enable the Python Development Mode
       if (PyInitConfig_SetInt(config, "dev_mode", 1) < 0) {
           goto error;
       }

       // Initialize Python with the configuration
       if (Py_InitializeFromInitConfig(config) < 0) {
           goto error;
       }
       PyInitConfig_Free(config);
       return 0;

   error:
       {
           // Display the error message.
           //
           // This uncommon braces style is used, because you cannot make
           // goto targets point to variable declarations.
           const char *err_msg;
           (void)PyInitConfig_GetError(config, &err_msg);
           printf("PYTHON INIT ERROR: %s\n", err_msg);
           PyInitConfig_Free(config);
           return -1;
       }
   }

### Create Config

struct PyInitConfig

   Opaque structure to configure the Python initialization.

PyInitConfig *PyInitConfig_Create(void)

   Create a new initialization configuration using Isolated
   Configuration default values.

   It must be freed by "PyInitConfig_Free()".

   Return "NULL" on memory allocation failure.

void PyInitConfig_Free(PyInitConfig *config)

   Free memory of the initialization configuration *config*.

   If *config* is "NULL", no operation is performed.

### Error Handling

int PyInitConfig_GetError(PyInitConfig *config, const char **err_msg)

   Get the *config* error message.

   * Set **err_msg* and return "1" if an error is set.

   * Set **err_msg* to "NULL" and return "0" otherwise.

   An error message is a UTF-8 encoded string.

   If *config* has an exit code, format the exit code as an error
   message.

   The error message remains valid until another "PyInitConfig"
   function is called with *config*. The caller doesn't have to free
   the error message.

int PyInitConfig_GetExitCode(PyInitConfig *config, int *exitcode)

   Get the *config* exit code.

   * Set **exitcode* and return "1" if *config* has an exit code set.

   * Return "0" if *config* has no exit code set.

   Only the "Py_InitializeFromInitConfig()" function can set an exit
   code if the "parse_argv" option is non-zero.

   An exit code can be set when parsing the command line failed (exit
   code "2") or when a command line option asks to display the command
   line help (exit code "0").

### Get Options

The configuration option *name* parameter must be a non-NULL null-
terminated UTF-8 encoded string. See Configuration Options.

int PyInitConfig_HasOption(PyInitConfig *config, const char *name)

   Test if the configuration has an option called *name*.

   Return "1" if the option exists, or return "0" otherwise.

int PyInitConfig_GetInt(PyInitConfig *config, const char *name, int64_t *value)

   Get an integer configuration option.

   * Set **value*, and return "0" on success.

   * Set an error in *config* and return "-1" on error.

int PyInitConfig_GetStr(PyInitConfig *config, const char *name, char **value)

   Get a string configuration option as a null-terminated UTF-8
   encoded string.

   * Set **value*, and return "0" on success.

   * Set an error in *config* and return "-1" on error.

   **value* can be set to "NULL" if the option is an optional string
   and the option is unset.

   On success, the string must be released with "free(value)" if it's
   not "NULL".

int PyInitConfig_GetStrList(PyInitConfig *config, const char *name, size_t *length, char ***items)

   Get a string list configuration option as an array of null-
   terminated UTF-8 encoded strings.

   * Set **length* and **value*, and return "0" on success.

   * Set an error in *config* and return "-1" on error.

   On success, the string list must be released with
   "PyInitConfig_FreeStrList(length, items)".

void PyInitConfig_FreeStrList(size_t length, char **items)

   Free memory of a string list created by
   "PyInitConfig_GetStrList()".

### Set Options

The configuration option *name* parameter must be a non-NULL null-
terminated UTF-8 encoded string. See Configuration Options.

Some configuration options have side effects on other options. This
logic is only implemented when "Py_InitializeFromInitConfig()" is
called, not by the "Set" functions below. For example, setting
"dev_mode" to "1" does not set "faulthandler" to "1".

int PyInitConfig_SetInt(PyInitConfig *config, const char *name, int64_t value)

   Set an integer configuration option.

   * Return "0" on success.

   * Set an error in *config* and return "-1" on error.

int PyInitConfig_SetStr(PyInitConfig *config, const char *name, const char *value)

   Set a string configuration option from a null-terminated UTF-8
   encoded string. The string is copied.

   * Return "0" on success.

   * Set an error in *config* and return "-1" on error.

int PyInitConfig_SetStrList(PyInitConfig *config, const char *name, size_t length, char *const *items)

   Set a string list configuration option from an array of null-
   terminated UTF-8 encoded strings. The string list is copied.

   * Return "0" on success.

   * Set an error in *config* and return "-1" on error.

### Module

int PyInitConfig_AddModule(PyInitConfig *config, const char *name, PyObject *(*initfunc)(void))

   Add a built-in extension module to the table of built-in modules.

   The new module can be imported by the name *name*, and uses the
   function *initfunc* as the initialization function called on the
   first attempted import.

   * Return "0" on success.

   * Set an error in *config* and return "-1" on error.

   If Python is initialized multiple times, "PyInitConfig_AddModule()"
   must be called at each Python initialization.

   Similar to the "PyImport_AppendInittab()" function.

### Initialize Python

int Py_InitializeFromInitConfig(PyInitConfig *config)

   Initialize Python from the initialization configuration.

   * Return "0" on success.

   * Set an error in *config* and return "-1" on error.

   * Set an exit code in *config* and return "-1" if Python wants to
     exit.

   See "PyInitConfig_GetExitcode()" for the exit code case.

## Configuration Options

+---------------------------+---------------------------+---------------------------+---------------------------+
| Option                    | PyConfig/PyPreConfig      | Type                      | Visibility                |
|                           | member                    |                           |                           |
|===========================|===========================|===========================|===========================|
## | ""allocator""             | "allocator"               | "int"                     | Read-only                 |

## | ""argv""                  | "argv"                    | "list[str]"               | Public                    |

## | ""base_exec_prefix""      | "base_exec_prefix"        | "str"                     | Public                    |

## | ""base_executable""       | "base_executable"         | "str"                     | Public                    |

## | ""base_prefix""           | "base_prefix"             | "str"                     | Public                    |

## | ""buffered_stdio""        | "buffered_stdio"          | "bool"                    | Read-only                 |

## | ""bytes_warning""         | "bytes_warning"           | "int"                     | Public                    |

## | ""check_hash_pycs_mode""  | "check_hash_pycs_mode"    | "str"                     | Read-only                 |

## | ""code_debug_ranges""     | "code_debug_ranges"       | "bool"                    | Read-only                 |

## | ""coerce_c_locale""       | "coerce_c_locale"         | "bool"                    | Read-only                 |

## | ""coerce_c_locale_warn""  | "coerce_c_locale_warn"    | "bool"                    | Read-only                 |

## | ""configure_c_stdio""     | "configure_c_stdio"       | "bool"                    | Read-only                 |

## | ""configure_locale""      | "configure_locale"        | "bool"                    | Read-only                 |

## | ""cpu_count""             | "cpu_count"               | "int"                     | Public                    |

## | ""dev_mode""              | "dev_mode"                | "bool"                    | Read-only                 |

## | ""dump_refs""             | "dump_refs"               | "bool"                    | Read-only                 |

## | ""dump_refs_file""        | "dump_refs_file"          | "str"                     | Read-only                 |

## | ""exec_prefix""           | "exec_prefix"             | "str"                     | Public                    |

## | ""executable""            | "executable"              | "str"                     | Public                    |

## | ""faulthandler""          | "faulthandler"            | "bool"                    | Read-only                 |

## | ""filesystem_encoding""   | "filesystem_encoding"     | "str"                     | Read-only                 |

## | ""filesystem_errors""     | "filesystem_errors"       | "str"                     | Read-only                 |

## | ""hash_seed""             | "hash_seed"               | "int"                     | Read-only                 |

## | ""home""                  | "home"                    | "str"                     | Read-only                 |

## | ""import_time""           | "import_time"             | "int"                     | Read-only                 |

## | ""inspect""               | "inspect"                 | "bool"                    | Public                    |

| ""install_signal_handler  | "install_signal_handlers" | "bool"                    | Read-only                 |
## | s""                       |                           |                           |                           |

## | ""int_max_str_digits""    | "int_max_str_digits"      | "int"                     | Public                    |

## | ""interactive""           | "interactive"             | "bool"                    | Public                    |

## | ""isolated""              | "isolated"                | "bool"                    | Read-only                 |

| ""legacy_windows_fs_enco  | "legacy_windows_fs_encod  | "bool"                    | Read-only                 |
## | ding""                    | ing"                      |                           |                           |

## | ""legacy_windows_stdio""  | "legacy_windows_stdio"    | "bool"                    | Read-only                 |

## | ""malloc_stats""          | "malloc_stats"            | "bool"                    | Read-only                 |

## | ""module_search_paths""   | "module_search_paths"     | "list[str]"               | Public                    |

## | ""optimization_level""    | "optimization_level"      | "int"                     | Public                    |

## | ""orig_argv""             | "orig_argv"               | "list[str]"               | Read-only                 |

## | ""parse_argv""            | "parse_argv"              | "bool"                    | Read-only                 |

## | ""parser_debug""          | "parser_debug"            | "bool"                    | Public                    |

## | ""pathconfig_warnings""   | "pathconfig_warnings"     | "bool"                    | Read-only                 |

## | ""perf_profiling""        | "perf_profiling"          | "bool"                    | Read-only                 |

## | ""platlibdir""            | "platlibdir"              | "str"                     | Public                    |

## | ""prefix""                | "prefix"                  | "str"                     | Public                    |

## | ""program_name""          | "program_name"            | "str"                     | Read-only                 |

## | ""pycache_prefix""        | "pycache_prefix"          | "str"                     | Public                    |

## | ""quiet""                 | "quiet"                   | "bool"                    | Public                    |

## | ""run_command""           | "run_command"             | "str"                     | Read-only                 |

## | ""run_filename""          | "run_filename"            | "str"                     | Read-only                 |

## | ""run_module""            | "run_module"              | "str"                     | Read-only                 |

## | ""run_presite""           | "run_presite"             | "str"                     | Read-only                 |

## | ""safe_path""             | "safe_path"               | "bool"                    | Read-only                 |

## | ""show_ref_count""        | "show_ref_count"          | "bool"                    | Read-only                 |

## | ""site_import""           | "site_import"             | "bool"                    | Read-only                 |

| ""skip_source_first_line  | "skip_source_first_line"  | "bool"                    | Read-only                 |
## | ""                        |                           |                           |                           |

## | ""stdio_encoding""        | "stdio_encoding"          | "str"                     | Read-only                 |

## | ""stdio_errors""          | "stdio_errors"            | "str"                     | Read-only                 |

## | ""stdlib_dir""            | "stdlib_dir"              | "str"                     | Public                    |

## | ""tracemalloc""           | "tracemalloc"             | "int"                     | Read-only                 |

## | ""use_environment""       | "use_environment"         | "bool"                    | Public                    |

## | ""use_frozen_modules""    | "use_frozen_modules"      | "bool"                    | Read-only                 |

## | ""use_hash_seed""         | "use_hash_seed"           | "bool"                    | Read-only                 |

## | ""use_system_logger""     | "use_system_logger"       | "bool"                    | Read-only                 |

## | ""user_site_directory""   | "user_site_directory"     | "bool"                    | Read-only                 |

## | ""utf8_mode""             | "utf8_mode"               | "bool"                    | Read-only                 |

## | ""verbose""               | "verbose"                 | "int"                     | Public                    |

## | ""warn_default_encoding"" | "warn_default_encoding"   | "bool"                    | Read-only                 |

## | ""warnoptions""           | "warnoptions"             | "list[str]"               | Public                    |

## | ""write_bytecode""        | "write_bytecode"          | "bool"                    | Public                    |

## | ""xoptions""              | "xoptions"                | "dict[str, str]"          | Public                    |

## | ""_pystats""              | "_pystats"                | "bool"                    | Read-only                 |

Visibility:

* Public: Can be retrieved by "PyConfig_Get()" and set by
  "PyConfig_Set()".

* Read-only: Can be retrieved by "PyConfig_Get()", but cannot be set
  by "PyConfig_Set()".

## Runtime Python configuration API

At runtime, it's possible to get and set configuration options using
"PyConfig_Get()" and  "PyConfig_Set()" functions.

The configuration option *name* parameter must be a non-NULL null-
terminated UTF-8 encoded string. See Configuration Options.

Some options are read from the "sys" attributes. For example, the
option ""argv"" is read from "sys.argv".

PyObject *PyConfig_Get(const char *name)

   Get the current runtime value of a configuration option as a Python
   object.

   * Return a new reference on success.

   * Set an exception and return "NULL" on error.

   The object type depends on the configuration option. It can be:

   * "bool"

   * "int"

   * "str"

   * "list[str]"

   * "dict[str, str]"

   The caller must have an *attached thread state*. The function
   cannot be called before Python initialization nor after Python
   finalization.

   Added in version 3.14.

int PyConfig_GetInt(const char *name, int *value)

   Similar to "PyConfig_Get()", but get the value as a C int.

   * Return "0" on success.

   * Set an exception and return "-1" on error.

   Added in version 3.14.

PyObject *PyConfig_Names(void)

   Get all configuration option names as a "frozenset".

   * Return a new reference on success.

   * Set an exception and return "NULL" on error.

   The caller must have an *attached thread state*. The function
   cannot be called before Python initialization nor after Python
   finalization.

   Added in version 3.14.

int PyConfig_Set(const char *name, PyObject *value)

   Set the current runtime value of a configuration option.

   * Raise a "ValueError" if there is no option *name*.

   * Raise a "ValueError" if *value* is an invalid value.

   * Raise a "ValueError" if the option is read-only (cannot be set).

   * Raise a "TypeError" if *value* has not the proper type.

   The caller must have an *attached thread state*. The function
   cannot be called before Python initialization nor after Python
   finalization.

   Raises an auditing event "cpython.PyConfig_Set" with arguments
   "name", "value".

   Added in version 3.14.

   Distinto en la versión 3.14.6 (unreleased): The function now
   replaces "sys.flags" (create a new object), instead of modifying
   "sys.flags" in-place.

## PyConfig C API

Added in version 3.8.

Python se puede inicializar con "Py_InitializeFromConfig()" y la
estructura "PyConfig". Se puede preinicializar con
"Py_PreInitialize()" y la estructura "PyPreConfig".

Hay dos tipos de configuración:

* La Configuración de Python se puede utilizar para crear un Python
  personalizado que se comporte como el Python normal. Por ejemplo,
  las variables de entorno y los argumentos de la línea de comandos se
  utilizan para configurar Python.

* La Configuración Aislada se puede utilizar para incrustar Python en
  una aplicación. Aísla a Python del sistema. Por ejemplo, las
  variables de entorno se ignoran, la configuración regional LC_CTYPE
  se deja sin cambios y no se registra ningún manejador de señales.

La función "Py_RunMain()" se puede utilizar para escribir un programa
Python personalizado.

Consulte también Inicialización, finalización y subprocesos.

Ver también: **PEP 587** "Configuración de inicialización de Python".

### Ejemplo

Ejemplo de Python personalizado que siempre se ejecuta en modo
aislado:

   int main(int argc, char **argv)
   {
       PyStatus status;

       PyConfig config;
       PyConfig_InitPythonConfig(&config);
       config.isolated = 1;

       /* Decode command line arguments.
          Implicitly preinitialize Python (in isolated mode). */
       status = PyConfig_SetBytesArgv(&config, argc, argv);
       if (PyStatus_Exception(status)) {
           goto exception;
       }

       status = Py_InitializeFromConfig(&config);
       if (PyStatus_Exception(status)) {
           goto exception;
       }
       PyConfig_Clear(&config);

       return Py_RunMain();

   exception:
       PyConfig_Clear(&config);
       if (PyStatus_IsExit(status)) {
           return status.exitcode;
       }
       /* Display the error message and exit the process with
          non-zero exit code */
       Py_ExitStatusException(status);
   }

### PyWideStringList

type PyWideStringList

   Lista de cadenas de caracteres "wchar_t*".

   Si *length* no es cero, *items* no deben ser "NULL" y todas las
   cadenas de caracteres deben ser no "NULL".

   Métodos:

   PyStatus PyWideStringList_Append(PyWideStringList *list, const wchar_t *item)

      Agregar *item* a *list*.

      Python debe estar preinicializado para llamar a esta función.

   PyStatus PyWideStringList_Insert(PyWideStringList *list, Py_ssize_t index, const wchar_t *item)

      Inserta *item* en *list* en *index*.

      Si *index* es mayor o igual que el largo de *list*, agrega
      *item* a *list*.

      *index* debe ser mayor o igual que "0".

      Python debe estar preinicializado para llamar a esta función.

   Campos de estructura:

   Py_ssize_t length

      Longitud de la lista.

   wchar_t **items

      Elementos de la lista.

### PyStatus

type PyStatus

   Estructura para almacenar el estado de una función de
   inicialización: éxito, error o salida.

   Para un error, puede almacenar el nombre de la función C que creó
   el error.

   Campos de estructura:

   int exitcode

      Código de salida El argumento pasó a "exit()".

   const char *err_msg

      Mensaje de error.

   const char *func

      El nombre de la función que creó un error puede ser "NULL".

   Funciones para crear un estado:

   PyStatus PyStatus_Ok(void)

      Éxito.

   PyStatus PyStatus_Error(const char *err_msg)

      Error de inicialización con un mensaje.

      *err_msg* no debe ser "NULL".

   PyStatus PyStatus_NoMemory(void)

      Error de asignación de memoria (sin memoria).

   PyStatus PyStatus_Exit(int exitcode)

      Sale de Python con el código de salida especificado.

   Funciones para manejar un estado:

   int PyStatus_Exception(PyStatus status)

      ¿Es el estado un error o una salida? Si es verdadero, la
      excepción debe ser manejada; por ejemplo llamando a
      "Py_ExitStatusException()".

   int PyStatus_IsError(PyStatus status)

      ¿Es el resultado un error?

   int PyStatus_IsExit(PyStatus status)

      ¿El resultado es una salida?

   void Py_ExitStatusException(PyStatus status)

      Llama a "exit(exitcode)" si *status* es una salida. Imprime el
      mensaje de error y sale con un código de salida distinto de cero
      si *status* es un error. Solo se debe llamar si
      "PyStatus_Exception(status)" no es cero.

Nota:

  Internamente, Python usa macros que establecen "PyStatus.func",
  mientras que las funciones para crear un estado establecen "func" en
  "NULL".

Ejemplo:

   PyStatus alloc(void **ptr, size_t size)
   {
       *ptr = PyMem_RawMalloc(size);
       if (*ptr == NULL) {
           return PyStatus_NoMemory();
       }
       return PyStatus_Ok();
   }

   int main(int argc, char **argv)
   {
       void *ptr;
       PyStatus status = alloc(&ptr, 16);
       if (PyStatus_Exception(status)) {
           Py_ExitStatusException(status);
       }
       PyMem_Free(ptr);
       return 0;
   }

### PyPreConfig

type PyPreConfig

   Estructura utilizada para preinicializar Python.

   Función para inicializar una preconfiguración:

   void PyPreConfig_InitPythonConfig(PyPreConfig *preconfig)

      Inicializa la preconfiguración con Configuración de Python.

   void PyPreConfig_InitIsolatedConfig(PyPreConfig *preconfig)

      Inicializa la preconfiguración con Configuración aislada.

   Campos de estructura:

   int allocator

      Nombre de los asignadores de memoria de Python:

      * "PYMEM_ALLOCATOR_NOT_SET" ("0"): no cambia asignadores de
        memoria (usa los valores predeterminados)

      * "PYMEM_ALLOCATOR_DEFAULT" ("1"): asignadores de memoria
        predeterminados.

      * "PYMEM_ALLOCATOR_DEBUG" ("2"): asignadores de memoria
        predeterminados con ganchos de depuración.

      * "PYMEM_ALLOCATOR_MALLOC" ("3"): usa "malloc()" de la
        biblioteca C.

      * "PYMEM_ALLOCATOR_MALLOC_DEBUG" ("4"): fuerza el uso de
        "malloc()" con ganchos de depuración.

      * "PYMEM_ALLOCATOR_PYMALLOC" ("5"): asignador de memoria
        pymalloc de Python.

      * "PYMEM_ALLOCATOR_PYMALLOC_DEBUG" ("6"): asignador de memoria
        pymalloc de Python con ganchos de depuración.

      * "PYMEM_ALLOCATOR_MIMALLOC" ("6"): usa "mimalloc", un reemplazo
        rápido de malloc.

      * "PYMEM_ALLOCATOR_MIMALLOC_DEBUG" ("7"): usa "mimalloc", un
        reemplazo rápido de malloc con ganchos de depuración.

      "PYMEM_ALLOCATOR_PYMALLOC" y "PYMEM_ALLOCATOR_PYMALLOC_DEBUG" no
      son compatibles si Python es "configurado usando --without-
      pymalloc".

      "PYMEM_ALLOCATOR_MIMALLOC" y "PYMEM_ALLOCATOR_MIMALLOC_DEBUG" no
      son compatibles si Python es "configurado usando --without-
      mimalloc" o si el soporte atómico subyacente no está disponible.

      Ver Administración de memorias.

      Predeterminado: "PYMEM_ALLOCATOR_NOT_SET".

   int configure_locale

      Establece la configuración regional LC_CTYPE a la configuración
      regional preferida del usuario.

      Si es igual a "0", establece los miembros "coerce_c_locale" y
      "coerce_c_locale_warn" a "0".

      Vea el *locale encoding*.

      Predeterminado: "1" en la configuración de Python, "0" en la
      configuración aislada.

   int coerce_c_locale

      Si es igual a "2", imponga la configuración regional C.

      Si es igual a "1", lee la configuración regional LC_CTYPE para
      decidir si debe ser forzada.

      Vea el *locale encoding*.

      Predeterminado: "-1" en la configuración de Python, "0" en la
      configuración aislada.

   int coerce_c_locale_warn

      Si no es cero, emita una advertencia si la configuración
      regional C está coaccionada.

      Predeterminado: "-1" en la configuración de Python, "0" en la
      configuración aislada.

   int dev_mode

      Modo de desarrollo de Python: consulte "PyConfig.dev_mode".

      Por defecto: "-1" en modo Python, "0" en modo aislado.

   int isolated

      Modo aislado: consulte "PyConfig.isolated".

      Por defecto: "0" en modo Python, "1" en modo aislado.

   int legacy_windows_fs_encoding

      Si no es cero:

      * Establezca "PyPreConfig.utf8_mode" en "0",

      * Establezca "PyConfig.filesystem_encoding" en ""mbcs"",

      * Establezca "PyConfig.filesystem_errors" en ""replace"".

      Inicializado desde el valor de la variable de entorno
      "PYTHONLEGACYWINDOWSFSENCODING".

      Solo disponible en Windows. La macro "#ifdef MS_WINDOWS" se
      puede usar para el código específico de Windows.

      Predeterminado: "0".

   int parse_argv

      Si no es cero, "Py_PreInitializeFromArgs()" y
      "Py_PreInitializeFromBytesArgs()" analizan su argumento "argv"
      de la misma manera que Python analiza los argumentos de la línea
      de comandos: ver Argumentos de línea de comandos.

      Predeterminado: "1" en la configuración de Python, "0" en la
      configuración aislada.

   int use_environment

      ¿Utiliza variables de entorno? Consulte
      "PyConfig.use_environment".

      Predeterminado: "1" en la configuración de Python y "0" en la
      configuración aislada.

   int utf8_mode

      Si es distinto de cero, habilite Python UTF-8 Mode.

      Establecido a "0" o "1" por la opción de línea de comandos "-X
      utf8" y la variable de entorno "PYTHONUTF8".

      También se pone a "1" si la configuración regional "LC_CTYPE" es
      "C" o "POSIX".

      Predeterminado: "-1" en la configuración de Python y "0" en la
      configuración aislada.

### Preinicialización de Python con PyPreConfig

La preinicialización de Python:

* Establecer los asignadores de memoria de Python
  ("PyPreConfig.allocator")

* Configurar la configuración regional LC_CTYPE (*locale encoding*)

* Establecer el Python UTF-8 Mode ("PyPreConfig.utf8_mode")

La preconfiguración actual (tipo "PyPreConfig") se almacena en
"_PyRuntime.preconfig".

Funciones para preinicializar Python:

PyStatus Py_PreInitialize(const PyPreConfig *preconfig)

   Preinicializa Python desde la preconfiguración *preconfig*.

   *preconfig* no debe ser "NULL".

PyStatus Py_PreInitializeFromBytesArgs(const PyPreConfig *preconfig, int argc, char *const *argv)

   Preinicializa Python desde la preconfiguración *preconfig*.

   Analice los argumentos de la línea de comando *argv* (cadenas de
   bytes) si "parse_argv" de *preconfig* no es cero.

   *preconfig* no debe ser "NULL".

PyStatus Py_PreInitializeFromArgs(const PyPreConfig *preconfig, int argc, wchar_t *const *argv)

   Preinicializa Python desde la preconfiguración *preconfig*.

   Analice los argumentos de la línea de comando *argv* (cadenas
   anchas) si "parse_argv" de *preconfig* no es cero.

   *preconfig* no debe ser "NULL".

La persona que llama es responsable de manejar las excepciones (error
o salida) usando "PyStatus_Exception()" y "Py_ExitStatusException()".

Para Configuración de Python ("PyPreConfig_InitPythonConfig()"), si
Python se inicializa con argumentos de línea de comando, los
argumentos de la línea de comando también deben pasarse para
preinicializar Python, ya que tienen un efecto en la preconfiguración
como codificaciones. Por ejemplo, la opción de línea de comando "-X
utf8" habilita el Python UTF-8 Mode.

"PyMem_SetAllocator()" se puede llamar después de "Py_PreInitialize()"
y antes "Py_InitializeFromConfig()" para instalar un asignador de
memoria personalizado. Se puede llamar antes "Py_PreInitialize()" si
"PyPreConfig.allocator" está configurado en "PYMEM_ALLOCATOR_NOT_SET".

Las funciones de asignación de memoria de Python como
"PyMem_RawMalloc()" no deben usarse antes de la preinicialización de
Python, mientras que llamar directamente a "malloc()" y "free()"
siempre es seguro. No se debe llamar a "Py_DecodeLocale()" antes de la
preinicialización de Python.

Ejemplo usando la preinicialización para habilitar el Python UTF-8
Mode

   PyStatus status;
   PyPreConfig preconfig;
   PyPreConfig_InitPythonConfig(&preconfig);

   preconfig.utf8_mode = 1;

   status = Py_PreInitialize(&preconfig);
   if (PyStatus_Exception(status)) {
       Py_ExitStatusException(status);
   }

   /* at this point, Python speaks UTF-8 */

   Py_Initialize();
   /* ... use Python API here ... */
   Py_Finalize();

### PyConfig

type PyConfig

   Estructura que contiene la mayoría de los parámetros para
   configurar Python.

   Cuando termine, se debe utilizar la función "PyConfig_Clear()" para
   liberar la memoria de configuración.

   Métodos de estructura:

   void PyConfig_InitPythonConfig(PyConfig *config)

      Inicialice la configuración con la Configuración de Python.

   void PyConfig_InitIsolatedConfig(PyConfig *config)

      Inicialice la configuración con la Configuración Aislada.

   PyStatus PyConfig_SetString(PyConfig *config, wchar_t *const *config_str, const wchar_t *str)

      Copia la cadena de caracteres anchos *str* en "*config_str".

      Preinicializa Python si es necesario.

   PyStatus PyConfig_SetBytesString(PyConfig *config, wchar_t *const *config_str, const char *str)

      Decodifique *str* usando "Py_DecodeLocale()" y establezca el
      resultado en "*config_str".

      Preinicializa Python si es necesario.

   PyStatus PyConfig_SetArgv(PyConfig *config, int argc, wchar_t *const *argv)

      Configure los argumentos de la línea de comando (miembro "argv"
      de *config*) de la lista *argv* de cadenas de caracteres anchas.

      Preinicializa Python si es necesario.

   PyStatus PyConfig_SetBytesArgv(PyConfig *config, int argc, char *const *argv)

      Establezca argumentos de línea de comando (miembro "argv" de
      *config*) de la lista *argv* de cadenas de bytes. Decodifica
      bytes usando "Py_DecodeLocale()".

      Preinicializa Python si es necesario.

   PyStatus PyConfig_SetWideStringList(PyConfig *config, PyWideStringList *list, Py_ssize_t length, wchar_t **items)

      Establece la lista de cadenas de caracteres anchas *list* a
      *length* y *items*.

      Preinicializa Python si es necesario.

   PyStatus PyConfig_Read(PyConfig *config)

      Lee toda la configuración de Python.

      Los campos que ya están inicializados no se modifican.

      Los campos para la configuración de ruta ya no se calculan ni
      modifican al llamar a esta función, a partir de Python 3.11.

      La función "PyConfig_Read()" solo analiza los argumentos
      "PyConfig.argv" una vez: "PyConfig.parse_argv" se establece en
      "2" después de que se analizan los argumentos. Como los
      argumentos de Python se eliminan de "PyConfig.argv", analizar
      los argumentos dos veces analizaría las opciones de la
      aplicación como opciones de Python.

      Preinicializa Python si es necesario.

      Distinto en la versión 3.10: Los argumentos "PyConfig.argv"
      ahora solo se analizan una vez, "PyConfig.parse_argv" se
      establece en "2" después de analizar los argumentos y los
      argumentos solo se analizan si "PyConfig.parse_argv" es igual a
      "1".

      Distinto en la versión 3.11: "PyConfig_Read()" ya no calcula
      todas las rutas, por lo que los campos listados en Python Path
      Configuration ya no pueden ser actualizados hasta que se llame a
      "Py_InitializeFromConfig()".

   void PyConfig_Clear(PyConfig *config)

      Libera memoria de configuración.

   Most "PyConfig" methods preinitialize Python if needed. In that
   case, the Python preinitialization configuration ("PyPreConfig") is
   based on the "PyConfig". If configuration fields which are in
   common with "PyPreConfig" are tuned, they must be set before
   calling a "PyConfig" method:

   * "PyConfig.dev_mode"

   * "PyConfig.isolated"

   * "PyConfig.parse_argv"

   * "PyConfig.use_environment"

   Además, si se usa "PyConfig_SetArgv()" o "PyConfig_SetBytesArgv()",
   este método debe llamarse antes que otros métodos, ya que la
   configuración de preinicialización depende de los argumentos de la
   línea de comando (si "parse_argv" no es cero).

   Quien llama de estos métodos es responsable de manejar las
   excepciones (error o salida) usando "PyStatus_Exception()" y
   "Py_ExitStatusException()".

   Campos de estructura:

   PyWideStringList argv

      Establece los argumentos de la línea de comandos "sys.argv"
      basados en "argv". Estos parámetros son similares a los pasados
      a la función "main()" del programa con la diferencia de que la
      primera entrada debe referirse al archivo de script a ejecutar
      en lugar del ejecutable que aloja al intérprete de Python. Si no
      hay un script que se vaya a ejecutar, la primera entrada en
      "argv" puede ser una cadena vacía.

      Configure "parse_argv" en "1" para analizar "argv" de la misma
      manera que Python normal analiza los argumentos de la línea de
      comandos de Python y luego quita los argumentos de Python de
      "argv".

      Si "argv" está vacío, se agrega una cadena vacía para garantizar
      que "sys.argv" siempre exista y nunca esté vacío.

      Valor predeterminado: "NULL".

      Consulte también el miembro "orig_argv".

   int safe_path

      Si es igual a cero, "Py_RunMain()" agrega una ruta
      potencialmente insegura a "sys.path" al inicio:

      * Si "argv[0]" es igual a "L"-m"" ("python -m module"), añade el
        directorio de trabajo actual.

      * Si se ejecuta un script ("python script.py"), anteponer el
        directorio del script. Si es un enlace simbólico, resuelve los
        enlaces simbólicos.

      * En caso contrario ("python -c code" and "python"), añade una
        cadena vacía, que significa el directorio de trabajo actual.

      Establecido en "1" por la opción de la línea de comandos "-P" y
      la variable de entorno "PYTHONSAFEPATH".

      Predeterminado: "0" en la configuración de Python, "1" en la
      configuración aislada.

      Added in version 3.11.

   wchar_t *base_exec_prefix

      "sys.base_exec_prefix".

      Valor predeterminado: "NULL".

      Parte de la salida Python Path Configuration.

      Consulte también "PyConfig.exec_prefix".

   wchar_t *base_executable

      Python base executable: "sys._base_executable".

      Set by the "__PYVENV_LAUNCHER__" environment variable.

      Establecido desde "PyConfig.executable" si "NULL".

      Valor predeterminado: "NULL".

      Parte de la salida Python Path Configuration.

      Consulte también "PyConfig.executable".

   wchar_t *base_prefix

      "sys.base_prefix".

      Valor predeterminado: "NULL".

      Parte de la salida Python Path Configuration.

      Consulte también "PyConfig.prefix".

   int buffered_stdio

      Si es igual a "0" y "configure_c_stdio" no es cero, deshabilite
      el almacenamiento en búfer en las secuencias C stdout y stderr.

      Establecido en "0" por la opción de línea de comando "-u" y la
      variable de entorno "PYTHONUNBUFFERED".

      stdin siempre se abre en modo de búfer.

      Predeterminado: "1".

   int bytes_warning

      Si es igual a "1", emite una advertencia al comparar "bytes" o
      "bytearray" con "str", o al comparar "bytes" con "int".

      Si es igual o mayor a "2", lanza una excepción "BytesWarning" en
      estos casos.

      Incrementado por la opción de línea de comando "-b".

      Predeterminado: "0".

   int warn_default_encoding

      Si no es cero, emite una advertencia "EncodingWarning" cuando
      "io.TextIOWrapper" usa su codificación predeterminada. Consulte
      EncodingWarning opcional para obtener más detalles.

      Predeterminado: "0".

      Added in version 3.10.

   int code_debug_ranges

      Si es igual a "0", desactiva la inclusión de la línea final y
      las asignaciones de columna en los objetos de código. También
      desactiva la impresión de indicadores de rastreo a ubicaciones
      de error específicas.

      Establecido en "0" por la variable de entorno
      "PYTHONNODEBUGRANGES" y por la opción de línea de comando "-X
      no_debug_ranges".

      Predeterminado: "1".

      Added in version 3.11.

   wchar_t *check_hash_pycs_mode

      Controla el comportamiento de validación de archivos ".pyc"
      basados en hash: valor de la opción de línea de comando "--
      check-hash-based-pycs".

      Valores válidos:

      * "L"always"": Calcula el hash el archivo fuente para
        invalidación independientemente del valor de la marca
        'check_source'.

      * "L"never"": suponga que los pycs basados en hash siempre son
        válidos.

      * "L"default"": El indicador 'check_source' en pycs basados en
        hash determina la invalidación.

      Predeterminado: "L"default"".

      Consulte también **PEP 552** "Pycs deterministas".

   int configure_c_stdio

      Si es distinto de cero, configure los flujos estándar de C:

      * En Windows, configure el modo binario ("O_BINARY") en stdin,
        stdout y stderr.

      * Si "buffered_stdio" es igual a cero, deshabilite el
        almacenamiento en búfer de los flujos stdin, stdout y stderr.

      * Si "interactive" no es cero, habilite el almacenamiento en
        búfer de flujo en stdin y stdout (solo stdout en Windows).

      Predeterminado: "1" en la configuración de Python, "0" en la
      configuración aislada.

   int dev_mode

      Si es distinto de cero, habilita Modo de desarrollo de Python.

      Establecido en "1" por la opción "-X dev" y la variable de
      entorno "PYTHONDEVMODE".

      Por defecto: "-1" en modo Python, "0" en modo aislado.

   int dump_refs

      ¿Volcar referencias de Python?

      Si no es cero, volcar todos los objetos que aún están vivos en
      la salida.

      Establecido en "1" por la variable de entorno "PYTHONDUMPREFS".

      Necesita una compilación especial de Python con la macro
      "Py_TRACE_REFS" definida: consulte la opción "configure --with-
      trace-refs".

      Predeterminado: "0".

   wchar_t *dump_refs_file

      Filename where to dump Python references.

      Set by the "PYTHONDUMPREFSFILE" environment variable.

      Valor predeterminado: "NULL".

      Added in version 3.11.

   wchar_t *exec_prefix

      El prefijo de directorio específico del sitio donde se instalan
      los archivos Python dependientes de la plataforma:
      "sys.exec_prefix".

      Valor predeterminado: "NULL".

      Parte de la salida Python Path Configuration.

      Consulte también "PyConfig.base_exec_prefix".

   wchar_t *executable

      La ruta absoluta del binario ejecutable para el intérprete de
      Python: "sys.executable".

      Valor predeterminado: "NULL".

      Parte de la salida Python Path Configuration.

      Consulte también "PyConfig.base_executable".

   int faulthandler

      ¿Habilitar administrador de fallas?

      Si no es cero, llama a "faulthandler.enable()" al inicio.

      Establecido en "1" por "-X faulthandler" y la variable de
      entorno "PYTHONFAULTHANDLER".

      Por defecto: "-1" en modo Python, "0" en modo aislado.

   wchar_t *filesystem_encoding

      *Codificación del sistema de archvios*:
      "sys.getfilesystemencoding()".

      En macOS, Android y VxWorks: use ""utf-8"" de forma
      predeterminada.

      En Windows: utilice ""utf-8"" de forma predeterminada o ""mbcs""
      si "legacy_windows_fs_encoding" de "PyPreConfig" no es cero.

      Codificación predeterminada en otras plataformas:

      * ""utf-8"" si "PyPreConfig.utf8_mode" es distinto de cero.

      * ""ascii"" si Python detecta que "nl_langinfo(CODESET)" anuncia
        la codificación ASCII, mientras que la función "mbstowcs()"
        decodifica desde una codificación diferente (usualmente
        Latin1).

      * ""utf-8"" si "nl_langinfo(CODESET)" retorna una cadena vacía.

      * De lo contrario, utilice el resultado *locale encoding*:
        "nl_langinfo(CODESET)".

      Al inicio de Python, el nombre de codificación se normaliza al
      nombre del códec de Python. Por ejemplo, ""ANSI_X3.4-1968"" se
      reemplaza por ""ascii"".

      Consulte también el miembro "filesystem_errors".

   wchar_t *filesystem_errors

      *Manejador de errores del sistema de archivos*:
      "sys.getfilesystemencodeerrors()".

      En Windows: utilice ""surrogatepass"" de forma predeterminada o
      ""replace"" si "legacy_windows_fs_encoding" de "PyPreConfig" no
      es cero.

      En otras plataformas: utilice ""surrogateescape"" de forma
      predeterminada.

      Controladores de errores admitidos:

      * ""strict""

      * ""surrogateescape""

      * ""surrogatepass"" (solo compatible con la codificación UTF-8)

      Consulte también el miembro "filesystem_encoding".

   int use_frozen_modules

      If non-zero, use frozen modules.

      Set by the "PYTHON_FROZEN_MODULES" environment variable.

      Default: "1" in a release build, or "0" in a debug build.

   unsigned long hash_seed

   int use_hash_seed

      Funciones de semillas aleatorias hash.

      Si "use_hash_seed" es cero, se elige una semilla al azar en el
      inicio de Python y se ignora "hash_seed".

      Establecido por la variable de entorno "PYTHONHASHSEED".

      Valor predeterminado de *use_hash_seed*: "-1" en modo Python,
      "0" en modo aislado.

   wchar_t *home

      Establece el directorio "home" de Python por defecto, es decir,
      la ubicación de las bibliotecas estándar de Python (ver
      "PYTHONHOME").

      Establecido por la variable de entorno "PYTHONHOME".

      Valor predeterminado: "NULL".

      Parte de la entrada Python Path Configuration.

   int import_time

         If "1", profile import time. If "2", include additional
         output that indicates when an imported module has already
         been loaded.

         Set by the "-X importtime" option and the
         "PYTHONPROFILEIMPORTTIME" environment variable.

         Predeterminado: "0".

      Distinto en la versión 3.14: Added support for "import_time = 2"

   int inspect

      Ingresa al modo interactivo después de ejecutar un script o un
      comando.

      Si es mayor que "0", habilite la inspección: cuando se pasa un
      script como primer argumento o se usa la opción -c, ingrese al
      modo interactivo después de ejecutar el script o el comando,
      incluso cuando "sys.stdin" no parezca ser una terminal.

      Incrementado por la opción de línea de comando "-i". Establecido
      en "1" si la variable de entorno "PYTHONINSPECT" no está vacía.

      Predeterminado: "0".

   int install_signal_handlers

      ¿Instalar controladores de señales de Python?

      Por defecto: "1" en modo Python, "0" en modo aislado.

   int interactive

      Si es mayor que "0", habilita el modo interactivo (REPL).

      Incrementado por la opción de línea de comando "-i".

      Predeterminado: "0".

   int int_max_str_digits

      Configura la limitación de la longitud de conversión de entero a
      cadena. Un valor inicial de "-1" significa que el valor se
      tomará de la línea de comandos o del entorno o, de lo contrario,
      será por defecto 4300 ("sys.int_info.default_max_str_digits").
      Un valor de "0" deshabilita la limitación. Los valores mayores
      que cero pero menores que 640
      ("sys.int_info.str_digits_check_threshold") no son compatibles y
      producirán un error.

      Configurado por la bandera de línea de comandos "-X
      int_max_str_digits" o la variable de entorno
      "PYTHONINTMAXSTRDIGITS".

      Predeterminado: "-1" en modo Python. 4300
      ("sys.int_info.default_max_str_digits") en modo aislado.

      Added in version 3.12.

   int cpu_count

      Si el valor de "cpu_count" no es "-1", entonces anulará los
      valores de retorno de "os.cpu_count()", "os.process_cpu_count()"
      y "multiprocessing.cpu_count()".

      Configurado por la bandera de línea de comandos "-X
      cpu_count=*n|default*" o la variable de entorno
      "PYTHON_CPU_COUNT".

      Predeterminado: "-1".

      Added in version 3.13.

   int isolated

      Si es mayor que "0", habilite el modo aislado:

      * Establezca "safe_path" en "1": no anteponga una ruta
        potencialmente insegura a "sys.path" al inicio de Python, como
        el directorio actual, el directorio del script o una cadena
        vacía.

      * Establezca "use_environment" en "0": ignore las variables de
        entorno "PYTHON".

      * Establezca "user_site_directory" en "0": no agregue el
        directorio del sitio del usuario a "sys.path".

      * Python REPL no importa "readline" ni habilita la configuración
        predeterminada de readline en mensajes interactivos.

      Establecido en "1" por la opción de línea de comando "-I".

      Por defecto: "0" en modo Python, "1" en modo aislado.

      Consulte también la Configuración Aislada y
      "PyPreConfig.isolated".

   int legacy_windows_stdio

      Si no es cero, use "io.FileIO" en lugar de
      "io._WindowsConsoleIO" para "sys.stdin", "sys.stdout" y
      "sys.stderr".

      Establecido en "1" si la variable de entorno
      "PYTHONLEGACYWINDOWSSTDIO" está establecida en una cadena no
      vacía.

      Solo disponible en Windows. La macro "#ifdef MS_WINDOWS" se
      puede usar para el código específico de Windows.

      Predeterminado: "0".

      Consulte también **PEP 528** (Cambiar la codificación de la
      consola de Windows a UTF-8).

   int malloc_stats

      Si no es cero, volcar las estadísticas en Asignador de memoria
      Python pymalloc en la salida.

      Establecido en "1" por la variable de entorno
      "PYTHONMALLOCSTATS".

      La opción se ignora si Python es "configurado usando la opción
      --without-pymalloc".

      Predeterminado: "0".

   wchar_t *platlibdir

      Nombre del directorio de la biblioteca de la plataforma:
      "sys.platlibdir".

      Establecido por la variable de entorno "PYTHONPLATLIBDIR".

      Predeterminado: valor de la macro "PLATLIBDIR" que se establece
      mediante la opción "configure --with-platlibdir"
      (predeterminado: ""lib"", o ""DLLs"" en Windows).

      Parte de la entrada Python Path Configuration.

      Added in version 3.9.

      Distinto en la versión 3.11: Esta macro se utiliza ahora en
      Windows para localizar los módulos de extensión de la biblioteca
      estándar, normalmente en "DLLs". Sin embargo, por
      compatibilidad, tenga en cuenta que este valor se ignora para
      cualquier disposición no estándar, incluyendo las construcciones
      dentro del árbol y los entornos virtuales.

   wchar_t *pythonpath_env

      Rutas de búsqueda de módulos ("sys.path") como una cadena
      separada por "DELIM" ("os.pathsep").

      Establecido por la variable de entorno "PYTHONPATH".

      Valor predeterminado: "NULL".

      Parte de la entrada Python Path Configuration.

   PyWideStringList module_search_paths

   int module_search_paths_set

      Rutas de búsqueda del módulo: "sys.path".

      Si "module_search_paths_set" es igual a "0",
      "Py_InitializeFromConfig()" reemplazará "module_search_paths" y
      establecerá "module_search_paths_set" en "1".

      Por defecto: lista vacía ("module_search_paths") y "0"
      ("module_search_paths_set").

      Parte de la salida Python Path Configuration.

   int optimization_level

      Nivel de optimización de compilación:

      * "0": Optimizador de mirilla, configure "__debug__" en "True".

      * "1": Nivel 0, elimina las aserciones, establece "__debug__" en
        "False".

      * "2": Nivel 1, elimina docstrings.

      Incrementado por la opción de línea de comando "-O". Establecido
      en el valor de la variable de entorno "PYTHONOPTIMIZE".

      Predeterminado: "0".

   PyWideStringList orig_argv

      La lista de los argumentos originales de la línea de comandos
      pasados al ejecutable de Python: "sys.orig_argv".

      Si la lista "orig_argv" está vacía y "argv" no es una lista que
      solo contiene una cadena vacía, "PyConfig_Read()" copia "argv"
      en "orig_argv" antes de modificar "argv" (si "parse_argv" no es
      cero).

      Consulte también el miembro "argv" y la función
      "Py_GetArgcArgv()".

      Predeterminado: lista vacía.

      Added in version 3.10.

   int parse_argv

      ¿Analizar los argumentos de la línea de comando?

      Si es igual a "1", analiza "argv" de la misma forma que Python
      normal analiza argumentos de línea de comando y elimina los
      argumentos de Python de "argv".

      La función "PyConfig_Read()" solo analiza los argumentos
      "PyConfig.argv" una vez: "PyConfig.parse_argv" se establece en
      "2" después de que se analizan los argumentos. Como los
      argumentos de Python se eliminan de "PyConfig.argv", analizar
      los argumentos dos veces analizaría las opciones de la
      aplicación como opciones de Python.

      Por defecto: "1" en modo Python, "0" en modo aislado.

      Distinto en la versión 3.10: Los argumentos "PyConfig.argv"
      ahora solo se analizan si "PyConfig.parse_argv" es igual a "1".

   int parser_debug

      Modo de depuración del analizador. Si es mayor que "0", active
      la salida de depuración del analizador (solo para expertos,
      dependiendo de las opciones de compilación).

      Incrementado por la opción de línea de comando "-d". Establecido
      en el valor de la variable de entorno "PYTHONDEBUG".

      Necesita una compilación de depuración de Python (se debe
      definir la macro "Py_DEBUG").

      Predeterminado: "0".

   int pathconfig_warnings

      Si no es cero, se permite que el cálculo de la configuración de
      ruta registre advertencias en "stderr". Si es igual a "0",
      suprima estas advertencias.

      Por defecto: "1" en modo Python, "0" en modo aislado.

      Parte de la entrada Python Path Configuration.

      Distinto en la versión 3.11: Ahora también se aplica en Windows.

   wchar_t *prefix

      El prefijo de directorio específico del sitio donde se instalan
      los archivos Python independientes de la plataforma:
      "sys.prefix".

      Valor predeterminado: "NULL".

      Parte de la salida Python Path Configuration.

      Consulte también "PyConfig.base_prefix".

   wchar_t *program_name

      Nombre del programa utilizado para inicializar "executable" y en
      los primeros mensajes de error durante la inicialización de
      Python.

      * En macOS, usa la variable de entorno "PYTHONEXECUTABLE" si
        está configurada.

      * If the "WITH_NEXT_FRAMEWORK" macro is defined, use
        "__PYVENV_LAUNCHER__" environment variable if set.

      * Utiliza "argv[0]" de "argv" si está disponible y no está
        vacío.

      * De lo contrario, utiliza "L"python"" en Windows o "L"python3""
        en otras plataformas.

      Valor predeterminado: "NULL".

      Parte de la entrada Python Path Configuration.

   wchar_t *pycache_prefix

      Directorio donde se escriben los archivos ".pyc" almacenados en
      caché: "sys.pycache_prefix".

      Establecido por la opción de línea de comando "-X
      pycache_prefix=PATH" y la variable de entorno
      "PYTHONPYCACHEPREFIX". La opción de línea de comandos tiene
      prioridad.

      Si "NULL", "sys.pycache_prefix" es establecido a "None".

      Valor predeterminado: "NULL".

   int quiet

      Modo silencioso. Si es mayor que "0", no muestre los derechos de
      autor y la versión al inicio de Python en modo interactivo.

      Incrementado por la opción de línea de comando "-q".

      Predeterminado: "0".

   wchar_t *run_command

      Valor de la opción de línea de comando "-c".

      Usado por "Py_RunMain()".

      Valor predeterminado: "NULL".

   wchar_t *run_filename

      Nombre de archivo pasado en la línea de comandos: argumento
      final de la línea de comandos sin "-c" o "-m". Es utilizado por
      la función "Py_RunMain()".

      Por ejemplo, se establece en "script.py" mediante la línea de
      comandos "python3 script.py arg".

      Consulte también la opción "PyConfig.skip_source_first_line".

      Valor predeterminado: "NULL".

   wchar_t *run_module

      Valor de la opción de línea de comando "-m".

      Usado por "Py_RunMain()".

      Valor predeterminado: "NULL".

   wchar_t *run_presite

      Ruta "package.module" al módulo que debe ser importado antes de
      que se ejecute "site.py".

      Establecido por la opción de línea de comandos "-X
      presite=package.module" y la variable de entorno
      "PYTHON_PRESITE". La opción de línea de comandos tiene
      precedencia.

      Necesita una compilación de depuración de Python (se debe
      definir la macro "Py_DEBUG").

      Valor predeterminado: "NULL".

   int show_ref_count

      ¿Mostrar el recuento total de referencias al salir (excluyendo
      objetos *immortal*)?

      Establecido en "1" por la opción de línea de comando "-X
      showrefcount".

      Necesita una compilación de depuración de Python (la macro
      "Py_REF_DEBUG" debe estar definida).

      Predeterminado: "0".

   int site_import

      ¿Importar el módulo "site" al inicio?

      Si es igual a cero, desactive la importación del sitio del
      módulo y las manipulaciones dependientes del sitio de "sys.path"
      que conlleva.

      También deshabilite estas manipulaciones si el módulo "site" se
      importa explícitamente más tarde (llame a "site.main()" si desea
      que se activen).

      Establecido en "0" mediante la opción de línea de comando "-S".

      "sys.flags.no_site" se establece en el valor invertido de
      "site_import".

      Predeterminado: "1".

   int skip_source_first_line

      Si no es cero, omita la primera línea de la fuente
      "PyConfig.run_filename".

      Permite el uso de formas de "#!cmd" que no son Unix. Esto está
      destinado únicamente a un truco específico de DOS.

      Establecido en "1" mediante la opción de línea de comando "-x".

      Predeterminado: "0".

   wchar_t *stdio_encoding

   wchar_t *stdio_errors

      Codificación y errores de codificación de "sys.stdin",
      "sys.stdout" y "sys.stderr" (pero "sys.stderr" siempre usa el
      controlador de errores ""backslashreplace"").

      Utilice la variable de entorno "PYTHONIOENCODING" si no está
      vacía.

      Codificación predeterminada:

      * ""UTF-8"" si "PyPreConfig.utf8_mode" es distinto de cero.

      * De lo contrario, usa el *locale encoding*.

      Manejador de errores predeterminado:

      * En Windows: use ""surrogateescape"".

      * ""surrogateescape"" si "PyPreConfig.utf8_mode" no es cero o si
        la configuración regional LC_CTYPE es "C" o "POSIX".

      * ""strict"" de lo contrario.

      Consulte también "PyConfig.legacy_windows_stdio".

   int tracemalloc

      ¿Habilitar tracemalloc?

      Si no es cero, llama a "tracemalloc.start()" al inicio.

      Establecido por la opción de línea de comando "-X tracemalloc=N"
      y por la variable de entorno "PYTHONTRACEMALLOC".

      Por defecto: "-1" en modo Python, "0" en modo aislado.

   int perf_profiling

      Enable the Linux "perf" profiler support?

      If equals to "1", enable support for the Linux "perf" profiler.

      If equals to "2", enable support for the Linux "perf" profiler
      with DWARF JIT support.

      Set to "1" by "-X perf" command-line option and the
      "PYTHONPERFSUPPORT" environment variable.

      Set to "2" by the "-X perf_jit" command-line option and the
      "PYTHON_PERF_JIT_SUPPORT" environment variable.

      Predeterminado: "-1".

      Ver también:

        See Soporte de Python para el perfilador perf de Linux for
        more information.

      Added in version 3.12.

   wchar_t *stdlib_dir

      Directory of the Python standard library.

      Valor predeterminado: "NULL".

      Added in version 3.11.

   int use_environment

      ¿Utiliza variables de entorno?

      Si es igual a cero, ignora las variables de entorno.

      Establecido en "0" por la variable de entorno "-E".

      Predeterminado: "1" en la configuración de Python y "0" en la
      configuración aislada.

   int use_system_logger

      If non-zero, "stdout" and "stderr" will be redirected to the
      system log.

      Only available on macOS 10.12 and later, and on iOS.

      Default: "0" (don't use the system log) on macOS; "1" on iOS
      (use the system log).

      Added in version 3.14.

   int user_site_directory

      Si es distinto de cero, agregue el directorio del sitio del
      usuario a "sys.path".

      Establecido en "0" por las opciones de línea de comando "-s" y
      "-I".

      Establecido en "0" por la variable de entorno
      "PYTHONNOUSERSITE".

      Por defecto: "1" en modo Python, "0" en modo aislado.

   int verbose

      Modo detallado. Si es mayor que "0", imprime un mensaje cada vez
      que se importa un módulo, mostrando el lugar (nombre de archivo
      o módulo incorporado) desde el que se carga.

      Si es mayor o igual a "2", imprime un mensaje para cada archivo
      que se verifica al buscar un módulo. También proporciona
      información sobre la limpieza del módulo al salir.

      Incrementado por la opción de línea de comando "-v".

      Establecido por el valor de la variable de entorno
      "PYTHONVERBOSE".

      Predeterminado: "0".

   PyWideStringList warnoptions

      Opciones del módulo "warnings" para crear filtros de
      advertencias, de menor a mayor prioridad: "sys.warnoptions".

      The "warnings" module adds "sys.warnoptions" in the reverse
      order: the last "PyConfig.warnoptions" item becomes the first
      item of "warnings.filters" which is checked first (highest
      priority).

      Las opciones de la línea de comando "-W" agregan su valor a
      "warnoptions", se puede usar varias veces.

      La variable de entorno "PYTHONWARNINGS" también se puede
      utilizar para agregar opciones de advertencia. Se pueden
      especificar varias opciones, separadas por comas (",").

      Predeterminado: lista vacía.

   int write_bytecode

      Si es igual a "0", Python no intentará escribir archivos ".pyc"
      al importar módulos fuente.

      Establecido en "0" por la opción de línea de comando "-B" y la
      variable de entorno "PYTHONDONTWRITEBYTECODE".

      "sys.dont_write_bytecode" se inicializa al valor invertido de
      "write_bytecode".

      Predeterminado: "1".

   PyWideStringList xoptions

      Valores de las opciones de la línea de comando "-X":
      "sys._xoptions".

      Predeterminado: lista vacía.

   int _pystats

      If non-zero, write performance statistics at Python exit.

      Need a special build with the "Py_STATS" macro: see "--enable-
      pystats".

      Predeterminado: "0".

Si "parse_argv" no es cero, los argumentos de "argv" se analizan de la
misma forma que Python normal analiza argumentos de línea de comando,
y los argumentos de Python se eliminan de "argv".

Las opciones de "xoptions" se analizan para establecer otras opciones:
consulte la opción de línea de comando "-X".

Distinto en la versión 3.9: El campo "show_alloc_count" fue removido.

### Inicialización con PyConfig

Initializing the interpreter from a populated configuration struct is
handled by calling "Py_InitializeFromConfig()".

La persona que llama es responsable de manejar las excepciones (error
o salida) usando "PyStatus_Exception()" y "Py_ExitStatusException()".

Si se utilizan "PyImport_FrozenModules()", "PyImport_AppendInittab()"
o "PyImport_ExtendInittab()", deben establecerse o llamarse después de
la preinicialización de Python y antes de la inicialización de Python.
Si Python se inicializa varias veces, se debe llamar a
"PyImport_AppendInittab()" o "PyImport_ExtendInittab()" antes de cada
inicialización de Python.

La configuración actual (tipo "PyConfig") se almacena en
"PyInterpreterState.config".

Ejemplo de configuración del nombre del programa:

   void init_python(void)
   {
       PyStatus status;

       PyConfig config;
       PyConfig_InitPythonConfig(&config);

       /* Set the program name. Implicitly preinitialize Python. */
       status = PyConfig_SetString(&config, &config.program_name,
                                   L"/path/to/my_program");
       if (PyStatus_Exception(status)) {
           goto exception;
       }

       status = Py_InitializeFromConfig(&config);
       if (PyStatus_Exception(status)) {
           goto exception;
       }
       PyConfig_Clear(&config);
       return;

   exception:
       PyConfig_Clear(&config);
       Py_ExitStatusException(status);
   }

Ejemplo más completo modificando la configuración predeterminada, lee
la configuración y luego anula algunos parámetros. Ten en cuenta que,
desde la versión 3.11, muchos parámetros no se calculan hasta la
inicialización, por lo que los valores no se pueden leer desde la
estructura de configuración. Cualquier valor establecido antes de
llamar a la inicialización se dejará sin cambios por la
inicialización:

   PyStatus init_python(const char *program_name)
   {
       PyStatus status;

       PyConfig config;
       PyConfig_InitPythonConfig(&config);

       /* Set the program name before reading the configuration
          (decode byte string from the locale encoding).

          Implicitly preinitialize Python. */
       status = PyConfig_SetBytesString(&config, &config.program_name,
                                        program_name);
       if (PyStatus_Exception(status)) {
           goto done;
       }

       /* Read all configuration at once */
       status = PyConfig_Read(&config);
       if (PyStatus_Exception(status)) {
           goto done;
       }

       /* Specify sys.path explicitly */
       /* If you want to modify the default set of paths, finish
          initialization first and then use PySys_GetObject("path") */
       config.module_search_paths_set = 1;
       status = PyWideStringList_Append(&config.module_search_paths,
                                        L"/path/to/stdlib");
       if (PyStatus_Exception(status)) {
           goto done;
       }
       status = PyWideStringList_Append(&config.module_search_paths,
                                        L"/path/to/more/modules");
       if (PyStatus_Exception(status)) {
           goto done;
       }

       /* Override executable computed by PyConfig_Read() */
       status = PyConfig_SetString(&config, &config.executable,
                                   L"/path/to/my_executable");
       if (PyStatus_Exception(status)) {
           goto done;
       }

       status = Py_InitializeFromConfig(&config);

   done:
       PyConfig_Clear(&config);
       return status;
   }

### Configuración aislada

"PyPreConfig_InitIsolatedConfig()" y las funciones
"PyConfig_InitIsolatedConfig()" crean una configuración para aislar
Python del sistema. Por ejemplo, para incrustar Python en una
aplicación.

Esta configuración ignora las variables de configuración global, las
variables de entorno, los argumentos de la línea de comandos
("PyConfig.argv" no se analizan) y el directorio del sitio del
usuario. Los flujos estándar de C (por ejemplo, "stdout") y la
configuración regional LC_CTYPE no se modifican. Los manejadores de
señales no están instalados.

Los archivos de configuración se siguen utilizando con esta
configuración para determinar las rutas que no se especifican.
Asegúrese de que se especifica "PyConfig.home" para evitar que se
calcule la configuración de la ruta por defecto.

### Configuración de Python

"PyPreConfig_InitPythonConfig()" y las funciones
"PyConfig_InitPythonConfig()" crean una configuración para construir
un Python personalizado que se comporta como el Python normal.

Las variables de entorno y los argumentos de la línea de comandos se
utilizan para configurar Python, mientras que las variables de
configuración global se ignoran.

Esta función habilita la coerción de configuración regional C (**PEP
538**) y Python UTF-8 Mode (**PEP 540**) según la configuración
regional LC_CTYPE, las variables de entorno "PYTHONUTF8" y
"PYTHONCOERCECLOCALE".

### Configuración de la ruta de Python

"PyConfig" contiene múltiples campos para la configuración de ruta:

* Entradas de configuración de ruta:

  * "PyConfig.home"

  * "PyConfig.platlibdir"

  * "PyConfig.pathconfig_warnings"

  * "PyConfig.program_name"

  * "PyConfig.pythonpath_env"

  * directorio de trabajo actual: para obtener rutas absolutas

  * Variable de entorno "PATH" para obtener la ruta completa del
    programa (de "PyConfig.program_name")

  * Variable de entorno "__PYVENV_LAUNCHER__"

  * (Solo Windows) Rutas de aplicación en el registro en
    "SoftwarePythonPythonCoreX.YPythonPath" de HKEY_CURRENT_USER y
    HKEY_LOCAL_MACHINE (donde X.Y es la versión de Python).

* Campos de salida de configuración de ruta:

  * "PyConfig.base_exec_prefix"

  * "PyConfig.base_executable"

  * "PyConfig.base_prefix"

  * "PyConfig.exec_prefix"

  * "PyConfig.executable"

  * "PyConfig.module_search_paths_set", "PyConfig.module_search_paths"

  * "PyConfig.prefix"

Si al menos un "campo de salida" no está establecido, Python calcula
la configuración de la ruta para rellenar los campos no establecidos.
Si "module_search_paths_set" es igual a "0", "module_search_paths" se
anula y "module_search_paths_set" se establece en "1".

Es posible ignorar completamente la función que calcula la
configuración de ruta predeterminada estableciendo explícitamente
todos los campos de salida de configuración de ruta mencionados
anteriormente. Una cadena se considera establecida incluso si no está
vacía. "module_search_paths" se considera establecido si
"module_search_paths_set" se establece en "1". En este caso,
"module_search_paths" se utilizará sin modificaciones.

Establezca "pathconfig_warnings" en "0" para suprimir las advertencias
al calcular la configuración de la ruta (solo Unix, Windows no
registra ninguna advertencia).

Si "base_prefix" o los campos "base_exec_prefix" no están
establecidos, heredan su valor de "prefix" y "exec_prefix"
respectivamente.

"Py_RunMain()" y "Py_Main()" modifican "sys.path":

* Si "run_filename" está configurado y es un directorio que contiene
  un script "__main__.py", anteponga "run_filename" a "sys.path".

* Si "isolated" es cero:

  * Si "run_module" está configurado, anteponga el directorio actual a
    "sys.path". No haga nada si el directorio actual no se puede leer.

  * Si "run_filename" está configurado, anteponga el directorio del
    nombre del archivo a "sys.path".

  * De lo contrario, anteponga una cadena de caracteres vacía a
    "sys.path".

Si "site_import" no es cero, "sys.path" puede ser modificado por el
módulo "site". Si "user_site_directory" no es cero y el directorio del
paquete del sitio del usuario existe, el módulo "site" agrega el
directorio del paquete del sitio del usuario a "sys.path".

La configuración de ruta utiliza los siguientes archivos de
configuración:

* "pyvenv.cfg"

* archivo "._pth" (ej: "python._pth")

* "pybuilddir.txt" (sólo Unix)

Si un archivo "._pth" está presente:

* Establezca "isolated" en "1".

* Establezca "use_environment" en "0".

* Establezca "site_import" en "0".

* Establezca "safe_path" en "1".

If "home" is not set and a "pyvenv.cfg" file is present in the same
directory as "executable", or its parent, "prefix" and "exec_prefix"
are set that location. When this happens, "base_prefix" and
"base_exec_prefix" still keep their value, pointing to the base
installation. See Virtual Environments for more information.

La variable de entorno "__PYVENV_LAUNCHER__" se usa para establecer
"PyConfig.base_executable".

Distinto en la versión 3.14: "prefix", and "exec_prefix", are now set
to the "pyvenv.cfg" directory. This was previously done by "site",
therefore affected by "-S".

## Py_GetArgcArgv()

void Py_GetArgcArgv(int *argc, wchar_t ***argv)

   Obtiene los argumentos originales de la línea de comandos, antes de
   que Python los modificara.

   Ver también el miembro "PyConfig.orig_argv".

## Delaying main module execution

In some embedding use cases, it may be desirable to separate
interpreter initialization from the execution of the main module.

This separation can be achieved by setting "PyConfig.run_command" to
the empty string during initialization (to prevent the interpreter
from dropping into the interactive prompt), and then subsequently
executing the desired main module code using "__main__.__dict__" as
the global namespace.
