---
title: La capa de muy alto nivel
source_url: https://docs.python.org/es/3
source_path: c-api/veryhigh.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 780
---

# La capa de muy alto nivel

Las funciones en este capítulo te permitirán ejecutar código fuente de
Python desde un archivo o un búfer, pero no te permitirán interactuar
de una manera detallada con el intérprete.

Several of these functions accept a start symbol from the grammar as a
parameter.  The available start symbols are "Py_eval_input",
"Py_file_input", "Py_single_input", and "Py_func_type_input".  These
are described following the functions which accept them as parameters.

Note also that several of these functions take FILE* parameters.  One
particular issue which needs to be handled carefully is that the
"FILE" structure for different C libraries can be different and
incompatible.  Under Windows (at least), it is possible for
dynamically linked extensions to actually use different libraries, so
care should be taken that FILE* parameters are only passed to these
functions if it is certain that they were created by the same library
that the Python runtime is using.

int PyRun_AnyFile(FILE *fp, const char *filename)

   Esta es una interfaz simplificada para "PyRun_AnyFileExFlags()" más
   abajo, dejando *closeit* establecido a "0" y *flags* establecido a
   "NULL".

int PyRun_AnyFileFlags(FILE *fp, const char *filename, PyCompilerFlags *flags)

   Esta es una interfaz simplificada para "PyRun_AnyFileExFlags()" más
   abajo, dejando *closeit* establecido a "0".

int PyRun_AnyFileEx(FILE *fp, const char *filename, int closeit)

   Esta es una interfaz simplificada para "PyRun_AnyFileExFlags()" más
   abajo, dejando *flags* establecido a "NULL".

int PyRun_AnyFileExFlags(FILE *fp, const char *filename, int closeit, PyCompilerFlags *flags)

   If *fp* refers to a file associated with an interactive device
   (console or terminal input or Unix pseudo-terminal), return the
   value of "PyRun_InteractiveLoop()", otherwise return the result of
   "PyRun_SimpleFile()".  *filename* is decoded from the filesystem
   encoding ("sys.getfilesystemencoding()").  If *filename* is "NULL",
   this function uses ""???"" as the filename. If *closeit* is true,
   the file is closed before "PyRun_SimpleFileExFlags()" returns.

int PyRun_SimpleString(const char *command)

   This is a simplified interface to "PyRun_SimpleStringFlags()"
   below, leaving the "PyCompilerFlags"* argument set to "NULL".

int PyRun_SimpleStringFlags(const char *command, PyCompilerFlags *flags)

   Ejecuta el código fuente de Python desde *command* en el módulo
   "__main__" de acuerdo con el argumento *flags*. Si "__main__" aún
   no existe, se crea. Retorna "0" en caso de éxito o "-1" si se
   produjo una excepción. Si hubo un error, no hay forma de obtener la
   información de excepción. Para el significado de *flags*, ver
   abajo.

   Note that if an otherwise unhandled "SystemExit" is raised, this
   function will not return "-1", but exit the process, as long as
   "PyConfig.inspect" is zero.

int PyRun_SimpleFile(FILE *fp, const char *filename)

   Esta es una interfaz simplificada para "PyRun_SimpleStringFlags()"
   más abajo, dejando *closeit* establecido a "0" y *flags*
   establecido a "NULL".

int PyRun_SimpleFileEx(FILE *fp, const char *filename, int closeit)

   Esta es una interfaz simplificada para "PyRun_SimpleStringFlags()"
   más abajo, dejando *flags* establecido a "NULL".

int PyRun_SimpleFileExFlags(FILE *fp, const char *filename, int closeit, PyCompilerFlags *flags)

   Similar a "PyRun_SimpleStringFlags()", pero el código fuente de
   Python se lee desde *fp* en lugar de una cadena de caracteres en
   memoria. *filename* debe ser el nombre del fichero, se decodifica
   desde *filesystem encoding and error handler*. Si *closeit* es
   verdadero, el fichero se cierra antes de que
   "PyRun_SimpleFileExFlags()" retorne.

   Nota:

     En Windows, *fp* debe abrirse en modo binario (por ejemplo,
     "fopen(filename, "rb")". De lo contrario, Python puede no manejar
     correctamente el archivo de script con la terminación de línea
     LF.

int PyRun_InteractiveOneObject(FILE *fp, PyObject *filename, PyCompilerFlags *flags)

   Read and execute a single statement from a file associated with an
   interactive device according to the *flags* argument.  The user
   will be prompted using "sys.ps1" and "sys.ps2". *filename* must be
   a Python "str" object.

   Retorna "0" cuando la entrada se ejecuta con éxito, "-1" si hubo
   una excepción, o un código de error del archivo "errcode.h"
   distribuido como parte de Python si hubo un error de análisis
   gramatical. (Tenga en cuenta que "errcode.h" no está incluido en
   "Python.h", por lo que debe incluirse específicamente si es
   necesario).

int PyRun_InteractiveOne(FILE *fp, const char *filename)

   Esta es una interfaz simplificada para
   "PyRun_InteractiveOneFlags()" más abajo, dejando *flags*
   establecido a "NULL".

int PyRun_InteractiveOneFlags(FILE *fp, const char *filename, PyCompilerFlags *flags)

   Similar to "PyRun_InteractiveOneObject()", but *filename* is a
   const char*, which is decoded from the *filesystem encoding and
   error handler*.

int PyRun_InteractiveLoop(FILE *fp, const char *filename)

   Esta es una interfaz simplificada para
   "PyRun_InteractiveLoopFlags()" más abajo, dejando *flags*
   establecido a "NULL".

int PyRun_InteractiveLoopFlags(FILE *fp, const char *filename, PyCompilerFlags *flags)

   Lee y ejecuta declaraciones de un archivo asociado con un
   dispositivo interactivo hasta llegar al EOF. Se le solicitará al
   usuario usando "sys.ps1" y "sys.ps2".*filename* se decodifica a
   partir del *manejador de codificación y errores del sistema de
   archivos*. Retorna "0" en EOF o un número negativo en caso de
   falla.

int (*PyOS_InputHook)(void)
    * Part of the Stable ABI.*

   Can be set to point to a function with the prototype "int
   func(void)".  The function will be called when Python's interpreter
   prompt is about to become idle and wait for user input from the
   terminal.  The return value is ignored.  Overriding this hook can
   be used to integrate the interpreter's prompt with other event
   loops, as done in "Modules/_tkinter.c" in the Python source code.

   Distinto en la versión 3.12: This function is only called from the
   main interpreter.

char *(*PyOS_ReadlineFunctionPointer)(FILE*, FILE*, const char*)

   Se puede configurar para que apunte a una función con el prototipo
   "char *func (FILE *stdin, FILE *stdout, char *prompt)",
   sobrescribiendo la función predeterminada utilizada para leer una
   sola línea de entrada desde el intérprete. Se espera que la función
   genere la cadena de caracteres *prompt* si no es "NULL", y luego
   lea una línea de entrada del archivo de entrada estándar
   proporcionado, retornando la cadena de caracteres resultante. Por
   ejemplo, el módulo "readline" establece este enlace para
   proporcionar funciones de edición de línea y finalización de
   tabulación.

   El resultado debe ser una cadena de caracteres alocado por
   "PyMem_RawMalloc()" o "PyMem_RawRealloc()", o "NULL" si ocurre un
   error.

   Distinto en la versión 3.4: El resultado debe ser alocado por
   "PyMem_RawMalloc()" o "PyMem_RawRealloc()", en vez de ser alocado
   por "PyMem_Malloc()" o "PyMem_Realloc()".

   Distinto en la versión 3.12: This function is only called from the
   main interpreter.

PyObject *PyRun_String(const char *str, int start, PyObject *globals, PyObject *locals)
    *Return value: New reference.*

   Esta es una interfaz simplificada para "PyRun_StringFlags()" más
   abajo, dejando *flags* establecido a "NULL".

PyObject *PyRun_StringFlags(const char *str, int start, PyObject *globals, PyObject *locals, PyCompilerFlags *flags)
    *Return value: New reference.*

   Execute Python source code from *str* in the context specified by
   the objects *globals* and *locals* with the compiler flags
   specified by *flags*.  *globals* must be a dictionary; *locals* can
   be any object that implements the mapping protocol.  The parameter
   *start* specifies the start symbol and must be one of the available
   start symbols.

   Retorna el resultado de ejecutar el código como un objeto Python, o
   "NULL"' si se produjo una excepción.

PyObject *PyRun_File(FILE *fp, const char *filename, int start, PyObject *globals, PyObject *locals)
    *Return value: New reference.*

   Esta es una interfaz simplificada para "PyRun_FileExFlags()" más
   abajo, dejando *closeit* establecido a "0" y *flags* establecido a
   "NULL".

PyObject *PyRun_FileEx(FILE *fp, const char *filename, int start, PyObject *globals, PyObject *locals, int closeit)
    *Return value: New reference.*

   Esta es una interfaz simplificada para "PyRun_FileExFlags()" más
   abajo, dejando *flags* establecido a "NULL".

PyObject *PyRun_FileFlags(FILE *fp, const char *filename, int start, PyObject *globals, PyObject *locals, PyCompilerFlags *flags)
    *Return value: New reference.*

   Esta es una interfaz simplificada para "PyRun_FileExFlags()" más
   abajo, dejando *closeit* establecido a "0".

PyObject *PyRun_FileExFlags(FILE *fp, const char *filename, int start, PyObject *globals, PyObject *locals, int closeit, PyCompilerFlags *flags)
    *Return value: New reference.*

   Similar a "PyRun_StringFlags()", pero el código fuente de Python se
   lee de *fp* en lugar de una cadena de caracteres en memoria.
   *filename* debe ser el nombre del fichero, es decodificado desde el
   *filesystem encoding and error handler*. Si *closeit* es verdadero,
   el fichero se cierra antes de que "PyRun_FileExFlags()" retorne.

PyObject *Py_CompileString(const char *str, const char *filename, int start)
    *Return value: New reference.** Part of the Stable ABI.*

   Esta es una interfaz simplificada para "Py_CompileStringFlags()"
   más abajo, dejando *flags* establecido a "NULL".

PyObject *Py_CompileStringFlags(const char *str, const char *filename, int start, PyCompilerFlags *flags)
    *Return value: New reference.*

   Esta es una interfaz simplificada para "Py_CompileStringExFlags()"
   más abajo, con *optimize* establecido a "-1".

PyObject *Py_CompileStringObject(const char *str, PyObject *filename, int start, PyCompilerFlags *flags, int optimize)
    *Return value: New reference.*

   Parse and compile the Python source code in *str*, returning the
   resulting code object.  The start symbol is given by *start*; this
   can be used to constrain the code which can be compiled and should
   be available start symbols.  The filename specified by *filename*
   is used to construct the code object and may appear in tracebacks
   or "SyntaxError" exception messages.  This returns "NULL" if the
   code cannot be parsed or compiled.

   El número entero *optimize* especifica el nivel de optimización del
   compilador; un valor de "-1" selecciona el nivel de optimización
   del intérprete como se indica en las opciones "-O". Los niveles
   explícitos son "0" (sin optimización; "__debug__" es verdadero),
   "1" (los *asserts* se eliminan, "__debug__" es falso) o "2" (los
   docstrings también se eliminan) )

   Added in version 3.4.

PyObject *Py_CompileStringExFlags(const char *str, const char *filename, int start, PyCompilerFlags *flags, int optimize)
    *Return value: New reference.*

   Como "Py_CompileStringObject()", pero *filename* es una cadena de
   bytes decodificada a partir del *manejador de codificación y
   errores del sistema de archivos*.

   Added in version 3.2.

PyObject *PyEval_EvalCode(PyObject *co, PyObject *globals, PyObject *locals)
    *Return value: New reference.** Part of the Stable ABI.*

   Esta es una interfaz simplificada para "PyEval_EvalCodeEx()", con
   solo el objeto de código y las variables globales y locales. Los
   otros argumentos están establecidos en "NULL".

PyObject *PyEval_EvalCodeEx(PyObject *co, PyObject *globals, PyObject *locals, PyObject *const *args, int argcount, PyObject *const *kws, int kwcount, PyObject *const *defs, int defcount, PyObject *kwdefs, PyObject *closure)
    *Return value: New reference.** Part of the Stable ABI.*

   Evaluar un objeto de código precompilado, dado un entorno
   particular para su evaluación. Este entorno consta de un
   diccionario de variables globales, un objeto de mapeo de variables
   locales, arreglos de argumentos, palabras clave y valores
   predeterminados, un diccionario de valores predeterminados para
   argumentos keyword-only y  una tupla de cierre de células.

PyObject *PyEval_EvalFrame(PyFrameObject *f)
    *Return value: New reference.** Part of the Stable ABI.*

   Evaluar un marco de ejecución. Esta es una interfaz simplificada
   para "PyEval_EvalFrameEx()", para compatibilidad con versiones
   anteriores.

PyObject *PyEval_EvalFrameEx(PyFrameObject *f, int throwflag)
    *Return value: New reference.** Part of the Stable ABI.*

   Esta es la función principal sin barnizar de la interpretación de
   Python. El objeto de código asociado con el marco de ejecución del
   marco *f* se ejecuta, interpretando el código de bytes y ejecutando
   llamadas según sea necesario. El parámetro adicional *throwflag* se
   puede ignorar por lo general; si es verdadero, entonces se lanza
   una excepción de inmediato; esto se usa para los métodos "throw()"
   de objetos generadores.

   Distinto en la versión 3.4: Esta función ahora incluye una
   afirmación de depuración para ayudar a garantizar que no descarte
   silenciosamente una excepción activa.

int PyEval_MergeCompilerFlags(PyCompilerFlags *cf)

   Esta función cambia los flags del marco de evaluación actual, y
   retorna verdad (*true*) en caso de éxito, falso (*false*) en caso
   de fallo.

struct PyCompilerFlags

   Esta es la estructura usada para contener los flags del compilador.
   En casos donde el código es sólo compilado, es pasado como "int
   flags", y en casos donde el código es ejecutado, es pasado como
   "PyCompilerFlags *flags".  En este caso,  "from __future__ import"
   puede modificar los *flags*.

   Whenever "PyCompilerFlags *flags" is "NULL", "cf_flags" is treated
   as equal to "0", and any modification due to "from __future__
   import" is discarded.

   int cf_flags

      Flags del compilador.

   int cf_feature_version

      *cf_feature_version* es la versión menor de Python. Debe ser
      inicializado a "PY_MINOR_VERSION".

      The field is ignored by default, it is used if and only if
      "PyCF_ONLY_AST" flag is set in "cf_flags".

   Distinto en la versión 3.8: Agregado el campo *cf_feature_version*.

   The available compiler flags are accessible as macros:

   PyCF_ALLOW_TOP_LEVEL_AWAIT
   PyCF_ONLY_AST
   PyCF_OPTIMIZED_AST
   PyCF_TYPE_COMMENTS

      See compiler flags in documentation of the "ast" Python module,
      which exports these constants under the same names.

   -[ Low-level flags ]-

   The following flags and masks serve narrow needs of the standard
   library and interactive interpreters.  Code outside the standard
   library rarely has a reason to use them.  They are considered
   implementation details and may change at any time.

   PyCF_ALLOW_INCOMPLETE_INPUT

      This flag is a private interface between the compiler and the
      "codeop" module.  Do not use it; its behavior is unsupported and
      may change without warning.

      With this flag set, when compilation fails because the source
      text ends where more input is expected, for example in the
      middle of an indented block or an unterminated string literal,
      the error raised is the undocumented "_IncompleteInputError", a
      subclass of "SyntaxError".  The "codeop" module sets this flag,
      together with "PyCF_DONT_IMPLY_DEDENT", to tell input that is
      incomplete apart from input with a real syntax error, so that
      interactive interpreters know when to prompt for another line
      instead of reporting an error.

      Added in version 3.11.

   PyCF_DONT_IMPLY_DEDENT

      By default, when compiling with the "Py_single_input" start
      symbol, reaching the end of the source text implicitly closes
      any open indented blocks.  With this flag set, open blocks are
      only closed if the last line of the source ends with a newline;
      otherwise, compilation fails with a "SyntaxError":

         PyCompilerFlags flags = {
             .cf_flags = 0,
             .cf_feature_version = PY_MINOR_VERSION,
         };
         const char *source = "if a:\n    pass";

         /* The "if" block is closed implicitly;
            this returns a code object: */
         Py_CompileStringFlags(source, "<input>", Py_single_input, &flags);

         /* With the flag, this fails with a SyntaxError,
            because the last line does not end with a newline: */
         flags.cf_flags = PyCF_DONT_IMPLY_DEDENT;
         Py_CompileStringFlags(source, "<input>", Py_single_input, &flags);

      The "codeop" module uses this flag to detect incomplete
      interactive input.  While the user is still typing inside an
      indented block, the source does not yet end with a newline, so
      it fails to compile and the user is prompted for another line.

   PyCF_IGNORE_COOKIE

      Read the source text as UTF-8, ignoring its **PEP 263** encoding
      declaration ("coding cookie"), if any:

         PyCompilerFlags flags = {
             .cf_flags = 0,
             .cf_feature_version = PY_MINOR_VERSION,
         };
         const char *source = "# coding: latin-1\ns = '\xe9'\n";

         /* The coding cookie is honored: byte 0xE9 is decoded as
            Latin-1, and this returns a code object that sets s to "é": */
         Py_CompileStringFlags(source, "<input>", Py_file_input, &flags);

         /* With the flag, the cookie is ignored and compilation fails
            with a SyntaxError, because 0xE9 is not valid UTF-8: */
         flags.cf_flags = PyCF_IGNORE_COOKIE;
         Py_CompileStringFlags(source, "<input>", Py_file_input, &flags);

      The "compile()", "eval()" and "exec()" built-in functions set
      this flag when the source is a "str" object, because they pass
      the text to the parser encoded as UTF-8.

   PyCF_SOURCE_IS_UTF8

      Mark the source text as known to be UTF-8 encoded. The
      "compile()", "eval()" and "exec()" built-in functions set this
      flag, but it currently has no effect.

   The ""PyCF"" flags above can be combined with ""CO_FUTURE"" flags
   such as "CO_FUTURE_ANNOTATIONS" to enable features normally
   selectable using future statements. See Code Object Flags for a
   complete list.

   The following masks combine several flags:

   PyCF_MASK

      Bitmask of all "CO_FUTURE" flags (see Code Object Flags), which
      select features normally enabled by future statements. When code
      compiled with a "PyCompilerFlags *flags" argument contains a
      "from __future__ import" statement, the flag for the imported
      feature is added to *flags*, so that code executed later in the
      same context inherits it.

   PyCF_MASK_OBSOLETE

      Do not use this mask in new code.  It is kept only so that old
      code passing its flags to "compile()" keeps working.

      Bitmask of flags for obsolete future features that no longer
      have any effect.

   PyCF_COMPILE_MASK

      Bitmask of all "PyCF" flags that change how the source is
      compiled, such as "PyCF_ONLY_AST". The "compile()" built-in
      function uses this mask to validate its *flags* argument.

## Available start symbols

int Py_eval_input

   El símbolo de inicio de la gramática de Python para expresiones
   aisladas; para usar con "Py_CompileString()".

int Py_file_input

   El símbolo de inicio de la gramática de Python para secuencias de
   declaración leídos desde un archivo u otra fuente; para usar con
   "Py_CompileString()". Este es el símbolo usado cuando se compile un
   código fuente en Python arbitrariamente largo.

int Py_single_input

   El símbolo de inicio de la gramática de Python para una declaración
   única; para usar con "Py_CompileString()". Este es el símbolo usado
   para el bucle interactivo del intérprete.

int Py_func_type_input

   The start symbol from the Python grammar for a function type; for
   use with "Py_CompileString()". This is used to parse "signature
   type comments" from **PEP 484**.

   This requires the "PyCF_ONLY_AST" flag to be set.

   Ver también:

     * "ast.FunctionType"

     * **PEP 484**

   Added in version 3.8.

## Stack Effects

Ver también: "dis.stack_effect()"

PY_INVALID_STACK_EFFECT

   Sentinel value representing an invalid stack effect.

   This is currently equivalent to "INT_MAX".

   Added in version 3.8.

int PyCompile_OpcodeStackEffect(int opcode, int oparg)

   Compute the stack effect of *opcode* with argument *oparg*.

   On success, this function returns the stack effect; on failure,
   this returns "PY_INVALID_STACK_EFFECT".

   Added in version 3.4.

int PyCompile_OpcodeStackEffectWithJump(int opcode, int oparg, int jump)

   Similar to "PyCompile_OpcodeStackEffect()", but don't include the
   stack effect of jumping if *jump* is zero.

   If *jump* is "0", this will not include the stack effect of
   jumping, but if *jump* is "1" or "-1", this will include it.

   On success, this function returns the stack effect; on failure,
   this returns "PY_INVALID_STACK_EFFECT".

   Added in version 3.8.
