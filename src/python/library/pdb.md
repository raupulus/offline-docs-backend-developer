---
title: '"pdb" --- The Python Debugger'
source_url: https://docs.python.org/es/3
source_path: library/pdb.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3420
---

# "pdb" --- The Python Debugger

**Código fuente:** Lib/unittest/mock.py

======================================================================

The module "pdb" defines an interactive source code debugger for
Python programs.  It supports setting (conditional) breakpoints and
single stepping at the source line level, inspection of stack frames,
source code listing, and evaluation of arbitrary Python code in the
context of any stack frame.  It also supports post-mortem debugging
and can be called under program control.

El depurador es extensible -- en realidad se define como la clase
"Pdb". Esto no está actualmente documentado pero se entiende
fácilmente leyendo la fuente.  La interfaz de extensión usa los
módulos "bdb" y "cmd".

Ver también:

  Module "faulthandler"
     Used to dump Python tracebacks explicitly, on a fault, after a
     timeout, or on a user signal.

  Module "traceback"
     Standard interface to extract, format and print stack traces of
     Python programs.

The typical usage to break into the debugger is to insert:

   import pdb; pdb.set_trace()

Or:

   breakpoint()

at the location you want to break into the debugger, and then run the
program. You can then step through the code following this statement,
and continue running without the debugger using the "continue"
command.

Distinto en la versión 3.7: The built-in "breakpoint()", when called
with defaults, can be used instead of "import pdb; pdb.set_trace()".

   def double(x):
      breakpoint()
      return x * 2
   val = 3
   print(f"{val} * 2 is {double(val)}")

The debugger's prompt is "(Pdb)", which is the indicator that you are
in debug mode:

   > ...(2)double()
   -> breakpoint()
   (Pdb) p x
   3
   (Pdb) continue
   3 * 2 is 6

Distinto en la versión 3.3: La finalización de tabulación a través del
módulo "readline" está disponible para comandos y argumentos de
comando, por ejemplo. Los nombres globales y locales actuales se
ofrecen como argumentos del comando "p".

## Command-line interface

You can also invoke "pdb" from the command line to debug other
scripts.  For example:

   python -m pdb [-c command] (-m module | -p pid | pyfile) [args ...]

When invoked as a module, pdb will automatically enter post-mortem
debugging if the program being debugged exits abnormally.  After post-
mortem debugging (or after normal exit of the program), pdb will
restart the program.  Automatic restarting preserves pdb's state (such
as breakpoints) and in most cases is more useful than quitting the
debugger upon program's exit.

-c, --command <command>

   To execute commands as if given in a ".pdbrc" file; see Debugger
   commands.

   Distinto en la versión 3.2: Added the "-c" option.

-m <module>

   To execute modules similar to the way "python -m" does. As with a
   script, the debugger will pause execution just before the first
   line of the module.

   Distinto en la versión 3.7: Added the "-m" option.

-p, --pid <pid>

   Attach to the process with the specified PID.

   Added in version 3.14.

To attach to a running Python process for remote debugging, use the
"-p" or "--pid" option with the target process's PID:

   python -m pdb -p 1234

Nota:

  Attaching to a process that is blocked in a system call or waiting
  for I/O will only work once the next bytecode instruction is
  executed or when the process receives a signal.

Typical usage to execute a statement under control of the debugger is:

   >>> import pdb
   >>> def f(x):
   ...     print(1 / x)
   >>> pdb.run("f(2)")
   > <string>(1)<module>()
   (Pdb) continue
   0.5
   >>>

El uso típico para inspeccionar un programa que se ha estrellado es:

   >>> import pdb
   >>> def f(x):
   ...     print(1 / x)
   ...
   >>> f(0)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "<stdin>", line 2, in f
   ZeroDivisionError: division by zero
   >>> pdb.pm()
   > <stdin>(2)f()
   (Pdb) p x
   0
   (Pdb)

Distinto en la versión 3.13: The implementation of **PEP 667** means
that name assignments made via "pdb" will immediately affect the
active scope, even when running inside an *optimized scope*.

El módulo define las siguientes funciones; cada una de ellas entra en
el depurador de una manera ligeramente diferente:

pdb.run(statement, globals=None, locals=None)

   Ejecutar el *statement* (dado como una cadena o un objeto de
   código) bajo el control del depurador.  El prompt del depurador
   aparece antes de que se ejecute cualquier código; puedes establecer
   puntos de ruptura y escribir "continue", o puedes pasar por la
   declaración usando "step" o "next" (todos estos comandos se
   explican más abajo).  Los argumentos opcionales *globals* y
   *locals* especifican el entorno en el que se ejecuta el código; por
   defecto se utiliza el diccionario del módulo "__main__".  (Ver la
   explicación de las funciones incorporadas "exec()" o "eval()").

pdb.runeval(expression, globals=None, locals=None)

   Evaluate the *expression* (given as a string or a code object)
   under debugger control.  When "runeval()" returns, it returns the
   value of the *expression*.  Otherwise this function is similar to
   "run()".

pdb.runcall(function, *args, **kwds)

   Llama a la *function* (un objeto de función o método, no una
   cadena) con los argumentos dados.  Cuando "runcall()" retorna,
   retorna lo que sea que la llamada de la función haya retornado.  El
   aviso del depurador aparece tan pronto como se introduce la
   función.

pdb.set_trace(*, header=None, commands=None)

   Enter the debugger at the calling stack frame.  This is useful to
   hard-code a breakpoint at a given point in a program, even if the
   code is not otherwise being debugged (e.g. when an assertion
   fails).  If given, *header* is printed to the console just before
   debugging begins. The *commands* argument, if given, is a list of
   commands to execute when the debugger starts.

   Distinto en la versión 3.7: El argumento de la palabra clave
   *header*.

   Distinto en la versión 3.13: "set_trace()" will enter the debugger
   immediately, rather than on the next line of code to be executed.

   Added in version 3.14: The *commands* argument.

awaitable pdb.set_trace_async(*, header=None, commands=None)

   async version of "set_trace()". This function should be used inside
   an async function with "await".

      async def f():
          await pdb.set_trace_async()

   "await" statements are supported if the debugger is invoked by this
   function.

   Added in version 3.14.

pdb.post_mortem(t=None)

   Enter post-mortem debugging of the given exception or traceback
   object. If no value is given, it uses the exception that is
   currently being handled, or raises "ValueError" if there isn’t one.

   Distinto en la versión 3.13: Support for exception objects was
   added.

pdb.pm()

   Enter post-mortem debugging of the exception found in
   "sys.last_exc".

pdb.set_default_backend(backend)

   There are two supported backends for pdb: "'settrace'" and
   "'monitoring'". See "bdb.Bdb" for details. The user can set the
   default backend to use if none is specified when instantiating
   "Pdb". If no backend is specified, the default is "'settrace'".

   Nota:

     "breakpoint()" and "set_trace()" will not be affected by this
     function. They always use "'monitoring'" backend.

   Added in version 3.14.

pdb.get_default_backend()

   Returns the default backend for pdb.

   Added in version 3.14.

Las funciones "run*" y "set_trace()" son alias para instanciar la
clase "Pdb" y llamar al método del mismo nombre.  Si quieres acceder a
más funciones, tienes que hacerlo tú mismo:

class pdb.Pdb(completekey='tab', stdin=None, stdout=None, skip=None, nosigint=False, readrc=True, mode=None, backend=None, colorize=False)

   "Pdb" es la clase de depuración.

   Los argumentos *completekey*, *stdin* y *stdout* se pasan a la
   subyacente "cmd.Cmd" class; ver la descripción allí.

   El argumento *skip*, si se da, debe ser un iterable de los patrones
   de nombre de los módulos de estilo global.  El depurador no entrará
   en marcos que se originen en un módulo que coincida con uno de
   estos patrones. [1]

   By default, Pdb sets a handler for the SIGINT signal (which is sent
   when the user presses "Ctrl"-"C" on the console) when you give a
   "continue" command. This allows you to break into the debugger
   again by pressing "Ctrl"-"C".  If you want Pdb not to touch the
   SIGINT handler, set *nosigint* to true.

   El argumento * readrc * por defecto es verdadero y controla si Pdb
   cargará archivos .pdbrc desde el sistema de archivos.

   The *mode* argument specifies how the debugger was invoked. It
   impacts the workings of some debugger commands. Valid values are
   "'inline'" (used by the breakpoint() builtin), "'cli'" (used by the
   command line invocation) or "None" (for backwards compatible
   behaviour, as before the *mode* argument was added).

   The *backend* argument specifies the backend to use for the
   debugger. If "None" is passed, the default backend will be used.
   See "set_default_backend()". Otherwise the supported backends are
   "'settrace'" and "'monitoring'".

   The *colorize* argument, if set to "True", will enable colorized
   output in the debugger, if color is supported. This will highlight
   source code displayed in pdb.

   Ejemplo de llamada para permitir el rastreo con *skip*:

      import pdb; pdb.Pdb(skip=['django.*']).set_trace()

   Levanta una auditing event "pdb.Pdb" sin argumentos.

   Distinto en la versión 3.1: Added the *skip* parameter.

   Distinto en la versión 3.2: Added the *nosigint* parameter.
   Previously, a SIGINT handler was never set by Pdb.

   Distinto en la versión 3.6: El argumento *readrc*.

   Added in version 3.14: Added the *mode* argument.

   Added in version 3.14: Added the *backend* argument.

   Added in version 3.14: Added the *colorize* argument.

   Distinto en la versión 3.14: Inline breakpoints like "breakpoint()"
   or "pdb.set_trace()" will always stop the program at calling frame,
   ignoring the *skip* pattern (if any).

   run(statement, globals=None, locals=None)
   runeval(expression, globals=None, locals=None)
   runcall(function, *args, **kwds)
   set_trace()

      Véase la documentación para las funciones explicadas
      anteriormente.

## Debugger commands

Los comandos reconocidos por el depurador se enumeran a continuación.
La mayoría de los comandos pueden abreviarse a una o dos letras como
se indica; por ejemplo, "h(elp)" significa que se puede usar "h" o
"help" para introducir el comando de ayuda (pero no "he" o "hel", ni
"H" o "Help" o "HELP").  Los argumentos de los comandos deben estar
separados por espacios en blanco (espacios o tabulaciones).  Los
argumentos opcionales están encerrados entre corchetes ("[]") en la
sintaxis del comando; los corchetes no deben escribirse.  Las
alternativas en la sintaxis de los comandos están separadas por una
barra vertical ("|").

Introducir una línea en blanco repite el último comando introducido.
Excepción: si el último comando fue un "list" comando, las siguientes
11 líneas están listadas.

Se supone que los comandos que el depurador no reconoce son
declaraciones en Python y se ejecutan en el contexto del programa que
se está depurando.  Las declaraciones en Python también pueden ser
precedidas por un signo de exclamación ("!").  Esta es una manera
poderosa de inspeccionar el programa que se está depurando; incluso es
posible cambiar una variable o llamar a una función.  Cuando se
produce una excepción en una sentencia de este tipo, se imprime el
nombre de la excepción pero no se cambia el estado del depurador.

Distinto en la versión 3.13: Expressions/Statements whose prefix is a
pdb command are now correctly identified and executed.

El depurador soporta aliases.  Los alias pueden tener parámetros que
permiten un cierto nivel de adaptabilidad al contexto que se está
examinando.

Multiple commands may be entered on a single line, separated by ";;".
(A single ";" is not used as it is the separator for multiple commands
in a line that is passed to the Python parser.)  No intelligence is
applied to separating the commands; the input is split at the first
";;" pair, even if it is in the middle of a quoted string. A
workaround for strings with double semicolons is to use implicit
string concatenation "';'';'" or "";"";"".

To set a temporary global variable, use a *convenience variable*. A
*convenience variable* is a variable whose name starts with "$".  For
example, "$foo = 1" sets a global variable "$foo" which you can use in
the debugger session.  The *convenience variables* are cleared when
the program resumes execution so it's less likely to interfere with
your program compared to using normal variables like "foo = 1".

There are four preset *convenience variables*:

* "$_frame": the current frame you are debugging

* "$_retval": the return value if the frame is returning

* "$_exception": the exception if the frame is raising an exception

* "$_asynctask": the asyncio task if pdb stops in an async function

Added in version 3.12: Added the *convenience variable* feature.

Added in version 3.14: Added the "$_asynctask" convenience variable.

If a file ".pdbrc" exists in the user's home directory or in the
current directory, it is read with "'utf-8'" encoding and executed as
if it had been typed at the debugger prompt, with the exception that
empty lines and lines starting with "#" are ignored.  This is
particularly useful for aliases.  If both files exist, the one in the
home directory is read first and aliases defined there can be
overridden by the local file.

Distinto en la versión 3.2: ".pdbrc" puede ahora contener comandos que
continúan depurando, como "continue" o "next".  Anteriormente, estos
comandos no tenían ningún efecto.

Distinto en la versión 3.11: ".pdbrc" es ahora leído con codificación
"'utf-8'". Antes, era leído con la codificación correspondiente a la
configuración regional del sistema.

h(elp) [command]

   Sin argumento, imprime la lista de comandos disponibles.  Con un
   *command* como argumento, imprime la ayuda sobre ese comando.
   "help pdb" muestra la documentación completa (el docstring del
   módulo "pdb").  Como el argumento *command* debe ser un
   identificador, hay que introducir "help exec" para obtener ayuda
   sobre el comando "!".

w(here) [count]

   Print a stack trace, with the most recent frame at the bottom.  if
   *count* is 0, print the current frame entry. If *count* is
   negative, print the least recent - *count* frames. If *count* is
   positive, print the most recent *count* frames.  An arrow (">")
   indicates the current frame, which determines the context of most
   commands.

   Distinto en la versión 3.14: *count* argument is added.

d(own) [count]

   Mueve los niveles del marco actual *count* (por defecto uno) hacia
   abajo en el trazado de la pila (*stack trace*) (a un marco más
   nuevo).

u(p) [count]

   Mueve el marco actual *count* (por defecto uno) niveles hacia
   arriba en el trazado de la pila (*stack trace*) (a un marco más
   antiguo).

b(reak) [([filename:]lineno | function) [, condition]]

   With a *lineno* argument, set a break at line *lineno* in the
   current file. The line number may be prefixed with a *filename* and
   a colon, to specify a breakpoint in another file (possibly one that
   hasn't been loaded yet).  The file is searched on "sys.path".
   Acceptable forms of *filename* are "/abspath/to/file.py",
   "relpath/file.py", "module" and "package.module".

   With a *function* argument, set a break at the first executable
   statement within that function. *function* can be any expression
   that evaluates to a function in the current namespace.

   Si un segundo argumento está presente, es una expresión que debe
   ser evaluada como verdadera antes de que el punto de ruptura sea
   honrado.

   Sin argumento, enumere todas las interrupciones, incluyendo para
   cada punto de interrupción, el número de veces que se ha alcanzado
   ese punto de interrupción, el conteo de ignorancia actual y la
   condición asociada, si la hay.

   Each breakpoint is assigned a number to which all the other
   breakpoint commands refer.

tbreak [([filename:]lineno | function) [, condition]]

   Punto de interrupción temporal, que se elimina automáticamente
   cuando se ejecuta por primera vez. Los argumentos son los mismos
   que para "break".

cl(ear) [filename:lineno | bpnumber ...]

   Con el argumento *filename:lineno*, despeja todos los puntos de
   interrupción en esta línea. Con una lista de números de puntos de
   interrupción separados por espacios, despeja esos puntos de
   interrupción. Sin el argumento, despeja todos los puntos de
   interrupción (pero primero pide confirmación).

disable bpnumber [bpnumber ...]

   Deshabilitar los puntos de ruptura interrupción como una lista de
   números de puntos de ruptura separados por espacios.  Desactivar un
   punto de interrupción significa que no puede hacer que el programa
   detenga la ejecución, pero a diferencia de borrar un punto de
   interrupción, permanece en la lista de puntos de interrupción y
   puede ser (re)activado.

enable bpnumber [bpnumber ...]

   Habilitar los puntos de interrupción especificados.

ignore bpnumber [count]

   Set the ignore count for the given breakpoint number.  If *count*
   is omitted, the ignore count is set to 0.  A breakpoint becomes
   active when the ignore count is zero.  When non-zero, the *count*
   is decremented each time the breakpoint is reached and the
   breakpoint is not disabled and any associated condition evaluates
   to true.

condition bpnumber [condition]

   Establece una nueva *condition* para el punto de interrupción, una
   expresión que debe evaluarse como verdadera antes de que el punto
   de ruptura sea honrado.  Si la condición está ausente, se elimina
   cualquier condición existente, es decir, el punto de ruptura se
   hace incondicional.

commands [bpnumber]

   Especifique una lista de comandos para el número del punto de
   interrupción *bpnumber*.  Los comandos mismos aparecen en las
   siguientes líneas.  Escriba una línea que contenga sólo "end" para
   terminar los comandos. Un ejemplo:

      (Pdb) commands 1
      (com) p some_variable
      (com) end
      (Pdb)

   Para eliminar todos los comandos de un punto de interrupción,
   escribe "commands"  y sigue inmediatamente con "end" , es decir, no
   des órdenes.

   Sin el argumento *bpnumber*, "commands" se refiere al último punto
   de interrupción establecido.

   Puede utilizar los comandos de punto de interrupción para iniciar
   el programa de nuevo.  Simplemente usa el comando "continue", o
   "step", o cualquier otro comando que reanude la ejecución.

   Specifying any command resuming execution (currently "continue",
   "step", "next", "return", "until", "jump", "quit" and their
   abbreviations) terminates the command list (as if that command was
   immediately followed by end). This is because any time you resume
   execution (even with a simple next or step), you may encounter
   another breakpoint—which could have its own command list, leading
   to ambiguities about which list to execute.

   If the list of commands contains the "silent" command, or a command
   that resumes execution, then the breakpoint message containing
   information about the frame is not displayed.

   Distinto en la versión 3.14: Frame information will not be
   displayed if a command that resumes execution is present in the
   command list.

s(tep)

   Ejecutar la línea actual, detenerse en la primera ocasión posible
   (ya sea en una función que se llame o en la siguiente línea de la
   función actual).

n(ext)

   Continúe la ejecución hasta que se alcance la siguiente línea de la
   función actual o vuelva.  (La diferencia entre "next" y "step" es
   que "step" se detiene dentro de una función llamada, mientras que
   "next" ejecuta las funciones llamadas a (casi) toda velocidad,
   deteniéndose sólo en la siguiente línea de la función actual).

unt(il) [lineno]

   Sin argumento, continúe la ejecución hasta que se alcance la línea
   con un número mayor que el actual.

   With *lineno*, continue execution until a line with a number
   greater or equal to *lineno* is reached.  In both cases, also stop
   when the current frame returns.

   Distinto en la versión 3.2: Permita dar un número de línea
   explícito.

r(eturn)

   Continúe la ejecución hasta que vuelva la función actual.

c(ont(inue))

   Continúa la ejecución, sólo se detiene cuando se encuentra un punto
   de ruptura.

j(ump) lineno

   Establezca la siguiente línea que será ejecutada.  Sólo disponible
   en el marco de más bajo.  Esto te permite saltar hacia atrás y
   ejecutar el código de nuevo, o saltar hacia adelante para saltar el
   código que no quieres ejecutar.

   Cabe señalar que no todos los saltos están permitidos -- por
   ejemplo, no es posible saltar en medio de un bucle "for" o fuera de
   una cláusula "finally".

l(ist) [first[, last]]

   Enumere el código fuente del archivo actual.  Sin argumentos,
   enumere 11 líneas alrededor de la línea actual o continúe la lista
   anterior.  Con "." como argumento, enumere 11 líneas alrededor de
   la línea actual.  Con un argumento, enumere 11 líneas alrededor de
   esa línea.  Con dos argumentos, enumere el rango dado; si el
   segundo argumento es menor que el primero, se interpreta como un
   conteo.

   La línea actual en el cuadro actual se indica con "->".  Si se está
   depurando una excepción, la línea donde la excepción fue
   originalmente planteada o propagada se indica con ">>", si difiere
   de la línea actual.

   Distinto en la versión 3.2: Added the ">>" marker.

ll | longlist

   Enumere todos los códigos fuente de la función o marco actual.  Las
   líneas interesantes están marcadas como "list".

   Added in version 3.2.

a(rgs)

   Print the arguments of the current function and their current
   values.

p expression

   Evaluate *expression* in the current context and print its value.

   Nota:

     "print()" también se puede usar, pero no es un comando de
     depuración --- esto ejecuta la función Python "print()".

pp expression

   Like the "p" command, except the value of *expression* is pretty-
   printed using the "pprint" module.

whatis expression

   Print the type of *expression*.

source expression

   Try to get source code of *expression* and display it.

   Added in version 3.2.

display [expression]

   Display the value of *expression* if it changed, each time
   execution stops in the current frame.

   Without *expression*, list all display expressions for the current
   frame.

   Nota:

     Display evaluates *expression* and compares to the result of the
     previous evaluation of *expression*, so when the result is
     mutable, display may not be able to pick up the changes.

   Example:

      lst = []
      breakpoint()
      pass
      lst.append(1)
      print(lst)

   Display won't realize "lst" has been changed because the result of
   evaluation is modified in place by "lst.append(1)" before being
   compared:

      > example.py(3)<module>()
      -> pass
      (Pdb) display lst
      display lst: []
      (Pdb) n
      > example.py(4)<module>()
      -> lst.append(1)
      (Pdb) n
      > example.py(5)<module>()
      -> print(lst)
      (Pdb)

   You can do some tricks with copy mechanism to make it work:

      > example.py(3)<module>()
      -> pass
      (Pdb) display lst[:]
      display lst[:]: []
      (Pdb) n
      > example.py(4)<module>()
      -> lst.append(1)
      (Pdb) n
      > example.py(5)<module>()
      -> print(lst)
      display lst[:]: [1]  [old: []]
      (Pdb)

   Added in version 3.2.

undisplay [expression]

   Do not display *expression* anymore in the current frame.  Without
   *expression*, clear all display expressions for the current frame.

   Added in version 3.2.

interact

   Start an interactive interpreter (using the "code" module) in a new
   global namespace initialised from the local and global namespaces
   for the current scope. Use "exit()" or "quit()" to exit the
   interpreter and return to the debugger.

   Nota:

     As "interact" creates a new dedicated namespace for code
     execution, assignments to variables will not affect the original
     namespaces. However, modifications to any referenced mutable
     objects will be reflected in the original namespaces as usual.

   Added in version 3.2.

   Distinto en la versión 3.13: "exit()" and "quit()" can be used to
   exit the "interact" command.

   Distinto en la versión 3.13: "interact" directs its output to the
   debugger's output channel rather than "sys.stderr".

alias [name [command]]

   Create an alias called *name* that executes *command*.  The
   *command* must *not* be enclosed in quotes.  Replaceable parameters
   can be indicated by "%1", "%2", ... and "%9", while "%*" is
   replaced by all the parameters. If *command* is omitted, the
   current alias for *name* is shown. If no arguments are given, all
   aliases are listed.

   Los alias pueden anidarse y pueden contener cualquier cosa que se
   pueda teclear legalmente en el prompt de pdb.  Tenga en cuenta que
   los comandos internos de pdb *pueden* ser anulados por los alias.
   Dicho comando se oculta hasta que se elimina el alias.  El alias se
   aplica de forma recursiva a la primera palabra de la línea de
   comandos; todas las demás palabras de la línea se dejan en paz.

   Como ejemplo, aquí hay dos alias útiles (especialmente cuando se
   colocan en el archivo ".pdbrc"):

      # Print instance variables (usage "pi classInst")
      alias pi for k in %1.__dict__.keys(): print(f"%1.{k} = {%1.__dict__[k]}")
      # Print instance variables in self
      alias ps pi self

unalias name

   Delete the specified alias *name*.

! statement

   Execute the (one-line) *statement* in the context of the current
   stack frame. The exclamation point can be omitted unless the first
   word of the statement resembles a debugger command, e.g.:

      (Pdb) ! n=42
      (Pdb)

   To set a global variable, you can prefix the assignment command
   with a "global" statement on the same line, e.g.:

      (Pdb) global list_options; list_options = ['-l']
      (Pdb)

run [args ...]
restart [args ...]

   Restart the debugged Python program.  If *args* is supplied, it is
   split with "shlex" and the result is used as the new "sys.argv".
   History, breakpoints, actions and debugger options are preserved.
   "restart" is an alias for "run".

   Distinto en la versión 3.14: "run" and "restart" commands are
   disabled when the debugger is invoked in "'inline'" mode.

q(uit)

   Quit from the debugger.  The program being executed is aborted. An
   end-of-file input is equivalent to "quit".

   A confirmation prompt will be shown if the debugger is invoked in
   "'inline'" mode. Either "y", "Y", "<Enter>" or "EOF" will confirm
   the quit.

   Distinto en la versión 3.14: A confirmation prompt will be shown if
   the debugger is invoked in "'inline'" mode. After the confirmation,
   the debugger will call "sys.exit()" immediately, instead of raising
   "bdb.BdbQuit" in the next trace event.

debug code

   Enter a recursive debugger that steps through *code* (which is an
   arbitrary expression or statement to be executed in the current
   environment).

retval

   Print the return value for the last return of the current function.

exceptions [excnumber]

   List or jump between chained exceptions.

   When using "pdb.pm()"  or "Pdb.post_mortem(...)" with a chained
   exception instead of a traceback, it allows the user to move
   between the chained exceptions using "exceptions" command to list
   exceptions, and "exceptions <number>" to switch to that exception.

   Example:

      def out():
          try:
              middle()
          except Exception as e:
              raise ValueError("reraise middle() error") from e

      def middle():
          try:
              return inner(0)
          except Exception as e:
              raise ValueError("Middle fail")

      def inner(x):
          1 / x

       out()

   calling "pdb.pm()" will allow to move between exceptions:

      > example.py(5)out()
      -> raise ValueError("reraise middle() error") from e

      (Pdb) exceptions
        0 ZeroDivisionError('division by zero')
        1 ValueError('Middle fail')
      > 2 ValueError('reraise middle() error')

      (Pdb) exceptions 0
      > example.py(16)inner()
      -> 1 / x

      (Pdb) up
      > example.py(10)middle()
      -> return inner(0)

   Added in version 3.13.

-[ Notas de pie de página ]-

[1] Si se considera que un marco se origina en un determinado módulo
    se determina por el "__name__" en el marcos globales.
