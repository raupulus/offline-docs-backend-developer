---
title: Interpreter initialization and finalization
source_url: https://docs.python.org/es/3
source_path: c-api/interp-lifecycle.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 380
---

# Interpreter initialization and finalization

See Python Initialization Configuration for details on how to
configure the interpreter prior to initialization.

## Before Python initialization

In an application embedding Python, the "Py_Initialize()" function
must be called before using any other Python/C API functions; with the
exception of a few functions and the global configuration variables.

The following functions can be safely called before Python is
initialized:

* Functions that initialize the interpreter:

  * "Py_Initialize()"

  * "Py_InitializeEx()"

  * "Py_InitializeFromConfig()"

  * "Py_BytesMain()"

  * "Py_Main()"

  * the runtime pre-initialization functions covered in Configuración
    de inicialización de Python

* Configuration functions:

  * "PyImport_AppendInittab()"

  * "PyImport_ExtendInittab()"

  * "PyInitFrozenExtensions()"

  * "PyMem_SetAllocator()"

  * "PyMem_SetupDebugHooks()"

  * "PyObject_SetArenaAllocator()"

  * "Py_SetProgramName()"

  * "Py_SetPythonHome()"

  * the configuration functions covered in Configuración de
    inicialización de Python

* Informative functions:

  * "Py_IsInitialized()"

  * "PyMem_GetAllocator()"

  * "PyObject_GetArenaAllocator()"

  * "Py_GetBuildInfo()"

  * "Py_GetCompiler()"

  * "Py_GetCopyright()"

  * "Py_GetPlatform()"

  * "Py_GetVersion()"

  * "Py_IsInitialized()"

* Utilities:

  * "Py_DecodeLocale()"

  * the status reporting and utility functions covered in
    Configuración de inicialización de Python

* Memory allocators:

  * "PyMem_RawMalloc()"

  * "PyMem_RawRealloc()"

  * "PyMem_RawCalloc()"

  * "PyMem_RawFree()"

* Synchronization:

  * "PyMutex_Lock()"

  * "PyMutex_Unlock()"

Nota:

  Despite their apparent similarity to some of the functions listed
  above, the following functions **should not be called** before the
  interpreter has been initialized: "Py_EncodeLocale()",
  "PyEval_InitThreads()", and "Py_RunMain()".

## Global configuration variables

Python has variables for the global configuration to control different
features and options. By default, these flags are controlled by
command line options.

When a flag is set by an option, the value of the flag is the number
of times that the option was set. For example, "-b" sets
"Py_BytesWarningFlag" to 1 and "-bb" sets "Py_BytesWarningFlag" to 2.

int Py_BytesWarningFlag

   This API is kept for backward compatibility: setting
   "PyConfig.bytes_warning" should be used instead, see Python
   Initialization Configuration.

   Issue a warning when comparing "bytes" or "bytearray" with "str" or
   "bytes" with "int".  Issue an error if greater or equal to "2".

   Set by the "-b" option.

   Deprecated since version 3.12, will be removed in version 3.15.

int Py_DebugFlag

   This API is kept for backward compatibility: setting
   "PyConfig.parser_debug" should be used instead, see Python
   Initialization Configuration.

   Turn on parser debugging output (for expert only, depending on
   compilation options).

   Set by the "-d" option and the "PYTHONDEBUG" environment variable.

   Deprecated since version 3.12, will be removed in version 3.15.

int Py_DontWriteBytecodeFlag

   This API is kept for backward compatibility: setting
   "PyConfig.write_bytecode" should be used instead, see Python
   Initialization Configuration.

   If set to non-zero, Python won't try to write ".pyc" files on the
   import of source modules.

   Set by the "-B" option and the "PYTHONDONTWRITEBYTECODE"
   environment variable.

   Deprecated since version 3.12, will be removed in version 3.15.

int Py_FrozenFlag

   This API is kept for backward compatibility: setting
   "PyConfig.pathconfig_warnings" should be used instead, see Python
   Initialization Configuration.

   Private flag used by "_freeze_module" and "frozenmain" programs.

   Deprecated since version 3.12, will be removed in version 3.15.

int Py_HashRandomizationFlag

   This API is kept for backward compatibility: setting
   "PyConfig.hash_seed" and "PyConfig.use_hash_seed" should be used
   instead, see Python Initialization Configuration.

   Set to "1" if the "PYTHONHASHSEED" environment variable is set to a
   non-empty string.

   If the flag is non-zero, read the "PYTHONHASHSEED" environment
   variable to initialize the secret hash seed.

   Deprecated since version 3.12, will be removed in version 3.15.

int Py_IgnoreEnvironmentFlag

   This API is kept for backward compatibility: setting
   "PyConfig.use_environment" should be used instead, see Python
   Initialization Configuration.

   Ignore all "PYTHON*" environment variables, e.g. "PYTHONPATH" and
   "PYTHONHOME", that might be set.

   Set by the "-E" and "-I" options.

   Deprecated since version 3.12, will be removed in version 3.15.

int Py_InspectFlag

   This API is kept for backward compatibility: setting
   "PyConfig.inspect" should be used instead, see Python
   Initialization Configuration.

   When a script is passed as first argument or the "-c" option is
   used, enter interactive mode after executing the script or the
   command, even when "sys.stdin" does not appear to be a terminal.

   Set by the "-i" option and the "PYTHONINSPECT" environment
   variable.

   Deprecated since version 3.12, will be removed in version 3.15.

int Py_InteractiveFlag

   This API is kept for backward compatibility: setting
   "PyConfig.interactive" should be used instead, see Python
   Initialization Configuration.

   Set by the "-i" option.

   Deprecated since version 3.12, will be removed in version 3.15.

int Py_IsolatedFlag

   This API is kept for backward compatibility: setting
   "PyConfig.isolated" should be used instead, see Python
   Initialization Configuration.

   Run Python in isolated mode. In isolated mode "sys.path" contains
   neither the script's directory nor the user's site-packages
   directory.

   Set by the "-I" option.

   Added in version 3.4.

   Deprecated since version 3.12, will be removed in version 3.15.

int Py_LegacyWindowsFSEncodingFlag

   This API is kept for backward compatibility: setting
   "PyPreConfig.legacy_windows_fs_encoding" should be used instead,
   see Python Initialization Configuration.

   If the flag is non-zero, use the "mbcs" encoding with "replace"
   error handler, instead of the UTF-8 encoding with "surrogatepass"
   error handler, for the *filesystem encoding and error handler*.

   Set to "1" if the "PYTHONLEGACYWINDOWSFSENCODING" environment
   variable is set to a non-empty string.

   See **PEP 529** for more details.

   Availability: Windows.

   Deprecated since version 3.12, will be removed in version 3.15.

int Py_LegacyWindowsStdioFlag

   This API is kept for backward compatibility: setting
   "PyConfig.legacy_windows_stdio" should be used instead, see Python
   Initialization Configuration.

   If the flag is non-zero, use "io.FileIO" instead of
   "io._WindowsConsoleIO" for "sys" standard streams.

   Set to "1" if the "PYTHONLEGACYWINDOWSSTDIO" environment variable
   is set to a non-empty string.

   See **PEP 528** for more details.

   Availability: Windows.

   Deprecated since version 3.12, will be removed in version 3.15.

int Py_NoSiteFlag

   This API is kept for backward compatibility: setting
   "PyConfig.site_import" should be used instead, see Python
   Initialization Configuration.

   Disable the import of the module "site" and the site-dependent
   manipulations of "sys.path" that it entails.  Also disable these
   manipulations if "site" is explicitly imported later (call
   "site.main()" if you want them to be triggered).

   Set by the "-S" option.

   Deprecated since version 3.12, will be removed in version 3.15.

int Py_NoUserSiteDirectory

   This API is kept for backward compatibility: setting
   "PyConfig.user_site_directory" should be used instead, see Python
   Initialization Configuration.

   Don't add the "user site-packages directory" to "sys.path".

   Set by the "-s" and "-I" options, and the "PYTHONNOUSERSITE"
   environment variable.

   Deprecated since version 3.12, will be removed in version 3.15.

int Py_OptimizeFlag

   This API is kept for backward compatibility: setting
   "PyConfig.optimization_level" should be used instead, see Python
   Initialization Configuration.

   Set by the "-O" option and the "PYTHONOPTIMIZE" environment
   variable.

   Deprecated since version 3.12, will be removed in version 3.15.

int Py_QuietFlag

   This API is kept for backward compatibility: setting
   "PyConfig.quiet" should be used instead, see Python Initialization
   Configuration.

   Don't display the copyright and version messages even in
   interactive mode.

   Set by the "-q" option.

   Added in version 3.2.

   Deprecated since version 3.12, will be removed in version 3.15.

int Py_UnbufferedStdioFlag

   This API is kept for backward compatibility: setting
   "PyConfig.buffered_stdio" should be used instead, see Python
   Initialization Configuration.

   Force the stdout and stderr streams to be unbuffered.

   Set by the "-u" option and the "PYTHONUNBUFFERED" environment
   variable.

   Deprecated since version 3.12, will be removed in version 3.15.

int Py_VerboseFlag

   This API is kept for backward compatibility: setting
   "PyConfig.verbose" should be used instead, see Python
   Initialization Configuration.

   Print a message each time a module is initialized, showing the
   place (filename or built-in module) from which it is loaded.  If
   greater or equal to "2", print a message for each file that is
   checked for when searching for a module. Also provides information
   on module cleanup at exit.

   Set by the "-v" option and the "PYTHONVERBOSE" environment
   variable.

   Deprecated since version 3.12, will be removed in version 3.15.

## Initializing and finalizing the interpreter

void Py_Initialize()
    * Part of the Stable ABI.*

   Initialize the Python interpreter.  In an application embedding
   Python, this should be called before using any other Python/C API
   functions; see Before Python Initialization for the few exceptions.

   This initializes the table of loaded modules ("sys.modules"), and
   creates the fundamental modules "builtins", "__main__" and "sys".
   It also initializes the module search path ("sys.path"). It does
   not set "sys.argv"; use the Python Initialization Configuration API
   for that. This is a no-op when called for a second time (without
   calling "Py_FinalizeEx()" first).  There is no return value; it is
   a fatal error if the initialization fails.

   Use "Py_InitializeFromConfig()" to customize the Python
   Initialization Configuration.

   Nota:

     On Windows, changes the console mode from "O_TEXT" to "O_BINARY",
     which will also affect non-Python uses of the console using the C
     Runtime.

void Py_InitializeEx(int initsigs)
    * Part of the Stable ABI.*

   This function works like "Py_Initialize()" if *initsigs* is "1". If
   *initsigs* is "0", it skips initialization registration of signal
   handlers, which may be useful when CPython is embedded as part of a
   larger application.

   Use "Py_InitializeFromConfig()" to customize the Python
   Initialization Configuration.

PyStatus Py_InitializeFromConfig(const PyConfig *config)

   Initialize Python from *config* configuration, as described in
   Inicialización con PyConfig.

   See the Configuración de inicialización de Python section for
   details on pre-initializing the interpreter, populating the runtime
   configuration structure, and querying the returned status
   structure.

int Py_IsInitialized()
    * Part of the Stable ABI.*

   Return true (nonzero) when the Python interpreter has been
   initialized, false (zero) if not.  After "Py_FinalizeEx()" is
   called, this returns false until "Py_Initialize()" is called again.

int Py_IsFinalizing()
    * Part of the Stable ABI since version 3.13.*

   Return true (non-zero) if the main Python interpreter is *shutting
   down*. Return false (zero) otherwise.

   Added in version 3.13.

int Py_FinalizeEx()
    * Part of the Stable ABI since version 3.6.*

   Undo all initializations made by "Py_Initialize()" and subsequent
   use of Python/C API functions, and destroy all sub-interpreters
   (see "Py_NewInterpreter()" below) that were created and not yet
   destroyed since the last call to "Py_Initialize()".  This is a no-
   op when called for a second time (without calling "Py_Initialize()"
   again first).

   Since this is the reverse of "Py_Initialize()", it should be called
   in the same thread with the same interpreter active.  That means
   the main thread and the main interpreter. This should never be
   called while "Py_RunMain()" is running.

   Normally the return value is "0". If there were errors during
   finalization (flushing buffered data), "-1" is returned.

   Note that Python will do a best effort at freeing all memory
   allocated by the Python interpreter.  Therefore, any C-Extension
   should make sure to correctly clean up all of the previously
   allocated PyObjects before using them in subsequent calls to
   "Py_Initialize()".  Otherwise it could introduce vulnerabilities
   and incorrect behavior.

   This function is provided for a number of reasons.  An embedding
   application might want to restart Python without having to restart
   the application itself. An application that has loaded the Python
   interpreter from a dynamically loadable library (or DLL) might want
   to free all memory allocated by Python before unloading the DLL.
   During a hunt for memory leaks in an application a developer might
   want to free all memory allocated by Python before exiting from the
   application.

   **Bugs and caveats:** The destruction of modules and objects in
   modules is done in random order; this may cause destructors
   ("__del__()" methods) to fail when they depend on other objects
   (even functions) or modules.  Dynamically loaded extension modules
   loaded by Python are not unloaded.  Small amounts of memory
   allocated by the Python interpreter may not be freed (if you find a
   leak, please report it).  Memory tied up in circular references
   between objects is not freed.  Interned strings will all be
   deallocated regardless of their reference count. Some memory
   allocated by extension modules may not be freed.  Some extensions
   may not work properly if their initialization routine is called
   more than once; this can happen if an application calls
   "Py_Initialize()" and "Py_FinalizeEx()" more than once.
   "Py_FinalizeEx()" must not be called recursively from within
   itself.  Therefore, it must not be called by any code that may be
   run as part of the interpreter shutdown process, such as "atexit"
   handlers, object finalizers, or any code that may be run while
   flushing the stdout and stderr files.

   Raises an auditing event "cpython._PySys_ClearAuditHooks" with no
   arguments.

   Added in version 3.6.

void Py_Finalize()
    * Part of the Stable ABI.*

   This is a backwards-compatible version of "Py_FinalizeEx()" that
   disregards the return value.

int Py_BytesMain(int argc, char **argv)
    * Part of the Stable ABI since version 3.8.*

   Similar to "Py_Main()" but *argv* is an array of bytes strings,
   allowing the calling application to delegate the text decoding step
   to the CPython runtime.

   Added in version 3.8.

int Py_Main(int argc, wchar_t **argv)
    * Part of the Stable ABI.*

   The main program for the standard interpreter, encapsulating a full
   initialization/finalization cycle, as well as additional behaviour
   to implement reading configurations settings from the environment
   and command line, and then executing "__main__" in accordance with
   Línea de comando.

   This is made available for programs which wish to support the full
   CPython command line interface, rather than just embedding a Python
   runtime in a larger application.

   The *argc* and *argv* parameters are similar to those which are
   passed to a C program's "main()" function, except that the *argv*
   entries are first converted to "wchar_t" using "Py_DecodeLocale()".
   It is also important to note that the argument list entries may be
   modified to point to strings other than those passed in (however,
   the contents of the strings pointed to by the argument list are not
   modified).

   The return value is "2" if the argument list does not represent a
   valid Python command line, and otherwise the same as
   "Py_RunMain()".

   In terms of the CPython runtime configuration APIs documented in
   the runtime configuration section (and without accounting for error
   handling), "Py_Main" is approximately equivalent to:

      PyConfig config;
      PyConfig_InitPythonConfig(&config);
      PyConfig_SetArgv(&config, argc, argv);
      Py_InitializeFromConfig(&config);
      PyConfig_Clear(&config);

      Py_RunMain();

   In normal usage, an embedding application will call this function
   *instead* of calling "Py_Initialize()", "Py_InitializeEx()" or
   "Py_InitializeFromConfig()" directly, and all settings will be
   applied as described elsewhere in this documentation. If this
   function is instead called *after* a preceding runtime
   initialization API call, then exactly which environmental and
   command line configuration settings will be updated is version
   dependent (as it depends on which settings correctly support being
   modified after they have already been set once when the runtime was
   first initialized).

int Py_RunMain(void)

   Executes the main module in a fully configured CPython runtime.

   Executes the command ("PyConfig.run_command"), the script
   ("PyConfig.run_filename") or the module ("PyConfig.run_module")
   specified on the command line or in the configuration. If none of
   these values are set, runs the interactive Python prompt (REPL)
   using the "__main__" module's global namespace.

   If "PyConfig.inspect" is not set (the default), the return value
   will be "0" if the interpreter exits normally (that is, without
   raising an exception), the exit status of an unhandled
   "SystemExit", or "1" for any other unhandled exception.

   If "PyConfig.inspect" is set (such as when the "-i" option is
   used), rather than returning when the interpreter exits, execution
   will instead resume in an interactive Python prompt (REPL) using
   the "__main__" module's global namespace. If the interpreter exited
   with an exception, it is immediately raised in the REPL session.
   The function return value is then determined by the way the *REPL
   session* terminates: "0", "1", or the status of a "SystemExit", as
   specified above.

   This function always finalizes the Python interpreter before it
   returns.

   See Python Configuration for an example of a customized Python that
   always runs in isolated mode using "Py_RunMain()".

int PyUnstable_AtExit(PyInterpreterState *interp, void (*func)(void*), void *data)

   *This is Unstable API. It may change without warning in minor
   releases.*

   Register an "atexit" callback for the target interpreter *interp*.
   This is similar to "Py_AtExit()", but takes an explicit interpreter
   and data pointer for the callback.

   There must be an *attached thread state* for *interp*.

   Added in version 3.13.

## Cautions regarding runtime finalization

In the late stage of *interpreter shutdown*, after attempting to wait
for non-daemon threads to exit (though this can be interrupted by
"KeyboardInterrupt") and running the "atexit" functions, the runtime
is marked as *finalizing*: "Py_IsFinalizing()" and
"sys.is_finalizing()" return true.  At this point, only the
*finalization thread* that initiated finalization (typically the main
thread) is allowed to acquire the *GIL*.

If any thread, other than the finalization thread, attempts to attach
a *thread state* during finalization, either explicitly or implicitly,
the thread enters **a permanently blocked state** where it remains
until the program exits.  In most cases this is harmless, but this can
result in deadlock if a later stage of finalization attempts to
acquire a lock owned by the blocked thread, or otherwise waits on the
blocked thread.

Gross? Yes. This prevents random crashes and/or unexpectedly skipped
C++ finalizations further up the call stack when such threads were
forcibly exited here in CPython 3.13 and earlier. The CPython runtime
*thread state* C APIs have never had any error reporting or handling
expectations at *thread state* attachment time that would've allowed
for graceful exit from this situation. Changing that would require new
stable C APIs and rewriting the majority of C code in the CPython
ecosystem to use those with error handling.

## Process-wide parameters

void Py_SetProgramName(const wchar_t *name)
    * Part of the Stable ABI.*

   This API is kept for backward compatibility: setting
   "PyConfig.program_name" should be used instead, see Python
   Initialization Configuration.

   This function should be called before "Py_Initialize()" is called
   for the first time, if it is called at all.  It tells the
   interpreter the value of the "argv[0]" argument to the "main()"
   function of the program (converted to wide characters). This is
   used by "Py_GetPath()" and some other functions below to find the
   Python run-time libraries relative to the interpreter executable.
   The default value is "'python'".  The argument should point to a
   zero-terminated wide character string in static storage whose
   contents will not change for the duration of the program's
   execution.  No code in the Python interpreter will change the
   contents of this storage.

   Use "Py_DecodeLocale()" to decode a bytes string to get a wchar_t*
   string.

   Deprecated since version 3.11, will be removed in version 3.15.

wchar_t *Py_GetProgramName()
    * Part of the Stable ABI.*

   Return the program name set with "PyConfig.program_name", or the
   default. The returned string points into static storage; the caller
   should not modify its value.

   This function should not be called before "Py_Initialize()",
   otherwise it returns "NULL".

   Distinto en la versión 3.10: It now returns "NULL" if called before
   "Py_Initialize()".

   Deprecated since version 3.13, will be removed in version 3.15: Use
   "PyConfig_Get("executable")" ("sys.executable") instead.

wchar_t *Py_GetPrefix()
    * Part of the Stable ABI.*

   Return the *prefix* for installed platform-independent files. This
   is derived through a number of complicated rules from the program
   name set with "PyConfig.program_name" and some environment
   variables; for example, if the program name is
   "'/usr/local/bin/python'", the prefix is "'/usr/local'". The
   returned string points into static storage; the caller should not
   modify its value.  This corresponds to the **prefix** variable in
   the top-level "Makefile" and the "--prefix" argument to the
   **configure** script at build time.  The value is available to
   Python code as "sys.base_prefix". It is only useful on Unix.  See
   also the next function.

   This function should not be called before "Py_Initialize()",
   otherwise it returns "NULL".

   Distinto en la versión 3.10: It now returns "NULL" if called before
   "Py_Initialize()".

   Deprecated since version 3.13, will be removed in version 3.15: Use
   "PyConfig_Get("base_prefix")" ("sys.base_prefix") instead. Use
   "PyConfig_Get("prefix")" ("sys.prefix") if virtual environments
   need to be handled.

wchar_t *Py_GetExecPrefix()
    * Part of the Stable ABI.*

   Return the *exec-prefix* for installed platform-*dependent* files.
   This is derived through a number of complicated rules from the
   program name set with "PyConfig.program_name" and some environment
   variables; for example, if the program name is
   "'/usr/local/bin/python'", the exec-prefix is "'/usr/local'".  The
   returned string points into static storage; the caller should not
   modify its value.  This corresponds to the **exec_prefix** variable
   in the top-level "Makefile" and the "--exec-prefix" argument to the
   **configure** script at build  time.  The value is available to
   Python code as "sys.base_exec_prefix".  It is only useful on Unix.

   Background: The exec-prefix differs from the prefix when platform
   dependent files (such as executables and shared libraries) are
   installed in a different directory tree.  In a typical
   installation, platform dependent files may be installed in the
   "/usr/local/plat" subtree while platform independent may be
   installed in "/usr/local".

   Generally speaking, a platform is a combination of hardware and
   software families, e.g.  Sparc machines running the Solaris 2.x
   operating system are considered the same platform, but Intel
   machines running Solaris 2.x are another platform, and Intel
   machines running Linux are yet another platform.  Different major
   revisions of the same operating system generally also form
   different platforms.  Non-Unix operating systems are a different
   story; the installation strategies on those systems are so
   different that the prefix and exec-prefix are meaningless, and set
   to the empty string. Note that compiled Python bytecode files are
   platform independent (but not independent from the Python version
   by which they were compiled!).

   System administrators will know how to configure the **mount** or
   **automount** programs to share "/usr/local" between platforms
   while having "/usr/local/plat" be a different filesystem for each
   platform.

   This function should not be called before "Py_Initialize()",
   otherwise it returns "NULL".

   Distinto en la versión 3.10: It now returns "NULL" if called before
   "Py_Initialize()".

   Deprecated since version 3.13, will be removed in version 3.15: Use
   "PyConfig_Get("base_exec_prefix")" ("sys.base_exec_prefix")
   instead. Use "PyConfig_Get("exec_prefix")" ("sys.exec_prefix") if
   virtual environments need to be handled.

wchar_t *Py_GetProgramFullPath()
    * Part of the Stable ABI.*

   Return the full program name of the Python executable; this is
   computed as a side-effect of deriving the default module search
   path  from the program name (set by "PyConfig.program_name"). The
   returned string points into static storage; the caller should not
   modify its value.  The value is available to Python code as
   "sys.executable".

   This function should not be called before "Py_Initialize()",
   otherwise it returns "NULL".

   Distinto en la versión 3.10: It now returns "NULL" if called before
   "Py_Initialize()".

   Deprecated since version 3.13, will be removed in version 3.15: Use
   "PyConfig_Get("executable")" ("sys.executable") instead.

wchar_t *Py_GetPath()
    * Part of the Stable ABI.*

   Return the default module search path; this is computed from the
   program name (set by "PyConfig.program_name") and some environment
   variables. The returned string consists of a series of directory
   names separated by a platform dependent delimiter character.  The
   delimiter character is "':'" on Unix and macOS, "';'" on Windows.
   The returned string points into static storage; the caller should
   not modify its value.  The list "sys.path" is initialized with this
   value on interpreter startup; it can be (and usually is) modified
   later to change the search path for loading modules.

   This function should not be called before "Py_Initialize()",
   otherwise it returns "NULL".

   Distinto en la versión 3.10: It now returns "NULL" if called before
   "Py_Initialize()".

   Deprecated since version 3.13, will be removed in version 3.15: Use
   "PyConfig_Get("module_search_paths")" ("sys.path") instead.

const char *Py_GetVersion()
    * Part of the Stable ABI.*

   Return the version of this Python interpreter.  This is a string
   that looks something like

      "3.0a5+ (py3k:63103M, May 12 2008, 00:53:55) \n[GCC 4.2.3]"

   The first word (up to the first space character) is the current
   Python version; the first characters are the major and minor
   version separated by a period.  The returned string points into
   static storage; the caller should not modify its value.  The value
   is available to Python code as "sys.version".

   See also the "Py_Version" constant.

const char *Py_GetPlatform()
    * Part of the Stable ABI.*

   Return the platform identifier for the current platform.  On Unix,
   this is formed from the "official" name of the operating system,
   converted to lower case, followed by the major revision number;
   e.g., for Solaris 2.x, which is also known as SunOS 5.x, the value
   is "'sunos5'".  On macOS, it is "'darwin'".  On Windows, it is
   "'win'".  The returned string points into static storage; the
   caller should not modify its value.  The value is available to
   Python code as "sys.platform".

const char *Py_GetCopyright()
    * Part of the Stable ABI.*

   Return the official copyright string for the current Python
   version, for example

   "'Copyright 1991-1995 Stichting Mathematisch Centrum, Amsterdam'"

   The returned string points into static storage; the caller should
   not modify its value.  The value is available to Python code as
   "sys.copyright".

const char *Py_GetCompiler()
    * Part of the Stable ABI.*

   Return an indication of the compiler used to build the current
   Python version, in square brackets, for example:

      "[GCC 2.7.2.2]"

   The returned string points into static storage; the caller should
   not modify its value.  The value is available to Python code as
   part of the variable "sys.version".

const char *Py_GetBuildInfo()
    * Part of the Stable ABI.*

   Return information about the sequence number and build date and
   time of the current Python interpreter instance, for example

      "#67, Aug  1 1997, 22:34:28"

   The returned string points into static storage; the caller should
   not modify its value.  The value is available to Python code as
   part of the variable "sys.version".

void PySys_SetArgvEx(int argc, wchar_t **argv, int updatepath)
    * Part of the Stable ABI.*

   This API is kept for backward compatibility: setting
   "PyConfig.argv", "PyConfig.parse_argv" and "PyConfig.safe_path"
   should be used instead, see Python Initialization Configuration.

   Set "sys.argv" based on *argc* and *argv*.  These parameters are
   similar to those passed to the program's "main()" function with the
   difference that the first entry should refer to the script file to
   be executed rather than the executable hosting the Python
   interpreter.  If there isn't a script that will be run, the first
   entry in *argv* can be an empty string.  If this function fails to
   initialize "sys.argv", a fatal condition is signalled using
   "Py_FatalError()".

   If *updatepath* is zero, this is all the function does.  If
   *updatepath* is non-zero, the function also modifies "sys.path"
   according to the following algorithm:

   * If the name of an existing script is passed in "argv[0]", the
     absolute path of the directory where the script is located is
     prepended to "sys.path".

   * Otherwise (that is, if *argc* is "0" or "argv[0]" doesn't point
     to an existing file name), an empty string is prepended to
     "sys.path", which is the same as prepending the current working
     directory (""."").

   Use "Py_DecodeLocale()" to decode a bytes string to get a wchar_t*
   string.

   See also "PyConfig.orig_argv" and "PyConfig.argv" members of the
   Python Initialization Configuration.

   Nota:

     It is recommended that applications embedding the Python
     interpreter for purposes other than executing a single script
     pass "0" as *updatepath*, and update "sys.path" themselves if
     desired. See **CVE 2008-5983**.On versions before 3.1.3, you can
     achieve the same effect by manually popping the first "sys.path"
     element after having called "PySys_SetArgv()", for example using:

        PyRun_SimpleString("import sys; sys.path.pop(0)\n");

   Added in version 3.1.3.

   Deprecated since version 3.11, will be removed in version 3.15.

void PySys_SetArgv(int argc, wchar_t **argv)
    * Part of the Stable ABI.*

   This API is kept for backward compatibility: setting
   "PyConfig.argv" and "PyConfig.parse_argv" should be used instead,
   see Python Initialization Configuration.

   This function works like "PySys_SetArgvEx()" with *updatepath* set
   to "1" unless the **python** interpreter was started with the "-I".

   Use "Py_DecodeLocale()" to decode a bytes string to get a wchar_t*
   string.

   See also "PyConfig.orig_argv" and "PyConfig.argv" members of the
   Python Initialization Configuration.

   Distinto en la versión 3.4: The *updatepath* value depends on "-I".

   Deprecated since version 3.11, will be removed in version 3.15.

void Py_SetPythonHome(const wchar_t *home)
    * Part of the Stable ABI.*

   This API is kept for backward compatibility: setting
   "PyConfig.home" should be used instead, see Python Initialization
   Configuration.

   Set the default "home" directory, that is, the location of the
   standard Python libraries.  See "PYTHONHOME" for the meaning of the
   argument string.

   The argument should point to a zero-terminated character string in
   static storage whose contents will not change for the duration of
   the program's execution.  No code in the Python interpreter will
   change the contents of this storage.

   Use "Py_DecodeLocale()" to decode a bytes string to get a wchar_t*
   string.

   Deprecated since version 3.11, will be removed in version 3.15.

wchar_t *Py_GetPythonHome()
    * Part of the Stable ABI.*

   Return the default "home", that is, the value set by
   "PyConfig.home", or the value of the "PYTHONHOME" environment
   variable if it is set.

   This function should not be called before "Py_Initialize()",
   otherwise it returns "NULL".

   Distinto en la versión 3.10: It now returns "NULL" if called before
   "Py_Initialize()".

   Deprecated since version 3.13, will be removed in version 3.15: Use
   "PyConfig_Get("home")" or the "PYTHONHOME" environment variable
   instead.
