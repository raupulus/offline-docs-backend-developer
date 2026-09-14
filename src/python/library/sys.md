---
title: '"sys" --- System-specific parameters and functions'
source_url: https://docs.python.org/es/3
source_path: library/sys.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4010
---

# "sys" --- System-specific parameters and functions

======================================================================

This module provides access to some variables used or maintained by
the interpreter and to functions that interact strongly with the
interpreter. It is always available. Unless explicitly noted
otherwise, all variables are read-only.

sys.abiflags

   En los sistemas POSIX donde Python se construyó con el script
   estándar "configure", este contiene los indicadores ABI según lo
   especificado por **PEP 3149**.

   Added in version 3.2.

   Distinto en la versión 3.8: Los flags por defecto se convirtieron
   en una cadena de caracteres vacía (el flag "m" para pymalloc ha
   sido eliminado).

   Availability: Unix.

sys.addaudithook(hook)

   Agrega el *hook* invocable a la lista de enlaces de inspección
   activos para el (sub)intérprete actual.

   Cuando se genera un evento de auditoría a través de la función
   "sys.audit()", cada hook será llamado en el orden en que se agregó
   con el nombre del evento y la tupla de argumentos. Los hooks
   nativos agregados por "PySys_AddAuditHook()" se llaman primero,
   seguidos de los hooks agregados en el (sub)intérprete actual. Los
   hooks pueden registrar un evento, lanzar una excepción para abortar
   la operación, o terminar el proceso completamente.

   Tenga en cuenta que los ganchos de auditoría son principalmente
   para recopilar información sobre acciones internas o no
   observables, ya sea por Python o bibliotecas escritas en Python. No
   son adecuados para implementar una "caja de arena" (sandbox). En
   particular, el código malicioso puede desactivar o eludir
   trivialmente los hooks añadidos mediante esta función. Como mínimo,
   cualquier hook sensible a la seguridad debe añadirse utilizando la
   API de C "PySys_AddAuditHook()" antes de inicializar el tiempo de
   ejecución, y cualquier módulo que permita la modificación
   arbitraria de la memoria (como "ctypes") debe ser completamente
   eliminado o supervisado de cerca.

   Llamar "sys.addaudithook()" lanzará por si mismo un evento de
   auditoria llamado "sys.addaudithook" sin argumentos. Si uno de los
   hooks existentes lanza un excepción derivada de "RuntimeError", el
   nuevo hook no será agregado y la excepción será suprimida. Como
   resultado, los que llaman no podrán asumir que el hook a sido
   agregado a menos que ellos controlen todos los hooks existentes.

   Consulte la tabla de eventos de auditoría para todos los eventos
   lanzados por CPython, y **PEP 578** para discusión del diseño
   original.

   Added in version 3.8.

   Distinto en la versión 3.8.1: Las excepciones derivadas de
   "Exception" pero no "RuntimeError" ya no se suprimen.

   Cuando el rastreo está habilitado (ver "settrace()"), los ganchos
   de Python solo se rastrean si el invocable tiene un miembro
   "__cantrace__" que se establece en un valor verdadero. De lo
   contrario, las funciones de seguimiento omitirán el enlace.

sys.argv

   La lista de argumentos de la línea de comandos pasados a un script
   de Python. "argv[0]" es el nombre del script (depende del sistema
   operativo si se trata de una ruta completa o no). Si el comando se
   ejecutó usando la opción "-c" de la línea de comandos del
   intérprete, "argv[0]" se establece en la cadena de caracteres
   "'-c'". Si no se pasó ningún nombre de secuencia de comandos al
   intérprete de Python, "argv[0]" es la cadena de caracteres vacía.

   Para recorrer la entrada estándar, o la lista de archivos dada en
   la línea de comando, vea el módulo "fileinput".

   También ver "sys.orig_argv".

   Nota:

     En Unix, los argumentos de la línea de comandos se pasan por
     bytes desde el sistema operativo. Python los decodifica con la
     codificación del sistema de archivos y el controlador de errores
     "surrogateescape". Cuando necesite bytes originales, puede
     obtenerlos mediante "[os.fsencode (arg) for arg in sys.argv]".

sys.audit(event, *args)

   Activar un evento de auditoría y activar cualquier hook de
   auditoría activo. *event* es una cadena que identifica el evento, y
   *args* puede contener argumentos opcionales con más información
   sobre el evento.  El número y los tipos de argumentos para un
   evento determinado se consideran una API pública y estable y no
   deberían modificarse entre versiones.

   Por ejemplo, un evento de auditoría se llama "os.chdir". Este
   evento tiene un argumento llamado *path* que contendrá el nuevo
   directorio de trabajo solicitado.

   "sys.audit()" llamará a los ganchos de auditoría existentes,
   pasando el nombre del evento y los argumentos, y volverá a lanzar
   la primera excepción de cualquier hook. En general, si se lanza una
   excepción, no debería ser manejada y el proceso debería terminar lo
   más rápidamente posible. Esto permite que las implementaciones de
   los hook decidan cómo responder a determinados eventos: pueden
   limitarse a registrar el evento o abortar la operación lanzando una
   excepción.

   Los ganchos se agregan usando las funciones "sys.addaudithook()" o
   "PySys_AddAuditHook()".

   El equivalente nativo de esta función es "PySys_Audit()". Se
   prefiere usar la función nativa cuando sea posible.

   Consulte la tabla de eventos de auditoría para todos los eventos
   lanzados por CPython.

   Added in version 3.8.

sys.base_exec_prefix

   Equivalent to "exec_prefix", but referring to the base Python
   installation.

   When running under Virtual Environments, "exec_prefix" gets
   overwritten to the virtual environment prefix. "base_exec_prefix",
   conversely, does not change, and always points to the base Python
   installation. Refer to Virtual Environments for more information.

   Added in version 3.3.

sys.base_prefix

   Equivalent to "prefix", but referring to the base Python
   installation.

   When running under virtual environment, "prefix" gets overwritten
   to the virtual environment prefix. "base_prefix", conversely, does
   not change, and always points to the base Python installation.
   Refer to Virtual Environments for more information.

   Added in version 3.3.

sys.byteorder

   Un indicador del orden de bytes nativo. Esto tendrá el valor
   "'big'" en las plataformas big-endian (el byte más significativo
   primero) y "'little'" en las plataformas little-endian (el byte
   menos significativo primero).

sys.builtin_module_names

   Una tupla de cadenas de caracteres que contiene los nombres de
   todos los módulos que se compilan en este intérprete de Python.
   (Esta información no está disponible de ninguna otra manera ---
   "modules.keys()" solo enumera los módulos importados.)

   Consulte también la lista "sys.stdlib_module_names".

sys.call_tracing(func, args)

   Call "func(*args)", while tracing is enabled.  The tracing state is
   saved, and restored afterwards.  This is intended to be called from
   a debugger from a checkpoint, to recursively debug or profile some
   other code.

   Tracing is suspended while calling a tracing function set by
   "settrace()" or "setprofile()" to avoid infinite recursion.
   "call_tracing()" enables explicit recursion of the tracing
   function.

sys.copyright

   Una cadena de caracteres que contiene los derechos de autor
   pertenecientes al intérprete de Python.

sys._clear_type_cache()

   Borre la caché de tipo interno. La caché de tipos se utiliza para
   acelerar las búsquedas de métodos y atributos. Utilice la función
   *solo* para eliminar referencias innecesarias durante la depuración
   de fugas de referencia.

   Esta función debe usarse solo para fines internos y especializados.

   Obsoleto desde la versión 3.13: Use the more general
   "_clear_internal_caches()" function instead.

sys._clear_internal_caches()

   Clear all internal performance-related caches. Use this function
   *only* to release unnecessary references and memory blocks when
   hunting for leaks.

   Added in version 3.13.

sys._current_frames()

   Retorna un diccionario que asigna el identificador de cada
   subproceso al marco de pila superior actualmente activo en ese
   subproceso en el momento en que se llama a la función. Tenga en
   cuenta que las funciones en el módulo "traceback" pueden construir
   la pila de llamadas dado tal marco.

   Esto es más útil para depurar *deadlock*: esta función no requiere
   la cooperación de los subprocesos con *deadlock*, y las pilas de
   llamadas de dichos subprocesos se congelan mientras permanezcan en
   *deadlock*. El marco retornado para un subproceso no en *deadlock*
   puede no tener relación con la actividad actual de ese subproceso
   en el momento en que el código de llamada examina el marco.

   Esta función debe usarse solo para fines internos y especializados.

   Lanza un auditing event "sys._current_frames" sin argumentos.

sys._current_exceptions()

   Retorna un diccionario que mapea el identificador de cada hilo a la
   excepción mas alta actualmente activa en ese hilo en el tiempo que
   la función fue llamada. Si un hilo no esta manejando una excepción
   en el momento, no se incluye en el resultado del diccionario.

   Esto es más útil para la elaboración de perfiles estadísticos.

   Esta función debe usarse solo para fines internos y especializados.

   Lanza un auditing event "sys._current_exceptions" sin argumentos.

   Distinto en la versión 3.12: Cada valor del diccionario es ahora
   una única instancia de excepción, en lugar de una tripleta como la
   devuelta por "sys.exc_info()".

sys.breakpointhook()

   Esta función de gancho es llamada por built-in "breakpoint()". De
   forma predeterminada, lo coloca en el depurador "pdb", pero se
   puede configurar en cualquier otra función para que pueda elegir
   qué depurador se utiliza.

   La firma de esta función depende de lo que llame. Por ejemplo, el
   enlace predeterminado (por ejemplo, "pdb.set_trace()") no espera
   argumentos, pero puede vincularlo a una función que espera
   argumentos adicionales (posicional o palabra clave). La función
   incorporada "breakpoint()" pasa sus "*args" y "**kws" directamente.
   Lo que sea que retorne "breakpointhooks()" se retorna desde
   "breakpoint()".

   La implementación predeterminada consulta primero la variable de
   entorno "PYTHONBREAKPOINT". Si se establece en ""0"", esta función
   vuelve inmediatamente; es decir, no es una operación. Si la
   variable de entorno no se establece, o se establece en la cadena
   vacía, se llama a "pdb.set_trace()". De lo contrario, esta variable
   debería nombrar una función para ejecutar, utilizando la
   nomenclatura de importación con puntos de Python, por ejemplo
   "package.subpackage.module.function". En este caso, se importaría
   "package.subpackage.module" y el módulo resultante debe tener un
   invocable llamado "function()". Esto se ejecuta, pasando "*args" y
   "**kws", y lo que sea que "function()" retorna,
   "sys.breakpointhook()" retorna a la función "breakpoint()".

   Tenga en cuenta que si algo sale mal al importar el invocable
   nombrado por "PYTHONBREAKPOINT", se informa un "RuntimeWarning" y
   se ignora el punto de interrupción (*breakpoint*).

   También tenga en cuenta que si "sys.breakpointhook()" se anula
   mediante programación, "PYTHONBREAKPOINT" *no* se consulta.

   Added in version 3.7.

sys._debugmallocstats()

   Imprime información de bajo nivel para stderr sobre el estado del
   asignador de memoria de CPython.

   Si Python es built in debug mode ("configure --with-pydebug
   option"), también realiza algunas costosas comprobaciones de
   coherencia interna.

   Added in version 3.3.

   Esta función es específica de CPython. El formato exacto de salida
   no se define aquí y puede cambiar.

sys.dllhandle

   Número entero que especifica el identificador de la DLL de Python.

   Availability: Windows.

sys.displayhook(value)

   Si *value* no es "None", esta función imprime "repr(value)" en
   "sys.stdout" y guarda *value* en "builtins._". Si "repr(value)" no
   se puede codificar en "sys.stdout.encoding" con el controlador de
   errores "sys.stdout.errors" (que probablemente sea "'strict'"),
   codifíquelo para "sys.stdout.encoding" con el controlador de
   errores "'backslashreplace'".

   Se llama a "sys.displayhook" como resultado de evaluar un
   *expression* ingresado en una sesión interactiva de Python. La
   visualización de estos valores se puede personalizar asignando otra
   función de un argumento a "sys.displayhook".

   Pseudo-código:

      def displayhook(value):
          if value is None:
              return
          # Set '_' to None to avoid recursion
          builtins._ = None
          text = repr(value)
          try:
              sys.stdout.write(text)
          except UnicodeEncodeError:
              bytes = text.encode(sys.stdout.encoding, 'backslashreplace')
              if hasattr(sys.stdout, 'buffer'):
                  sys.stdout.buffer.write(bytes)
              else:
                  text = bytes.decode(sys.stdout.encoding, 'strict')
                  sys.stdout.write(text)
          sys.stdout.write("\n")
          builtins._ = value

   Distinto en la versión 3.2: Usa el manejador de error
   "'backslashreplace'" en "UnicodeEncodeError".

sys.dont_write_bytecode

   Si esto es cierto, Python no intentará escribir archivos ".pyc" en
   la importación de módulos fuente. Este valor se establece
   inicialmente en "True" o "False" según la opción "-B" de la línea
   de comando y la variable de entorno "PYTHONDONTWRITEBYTECODE", pero
   puede configurarlo usted mismo para controlar el código de bytes
   generación de archivos.

sys._emscripten_info

   Un *named tuple* que contiene información sobre el medio ambiente
   en la plataforma *wasm32-emscripten*. La tupla nombrada es
   provisional y puede cambiar en el futuro.

   _emscripten_info.emscripten_version

      Versión de Emscripten como tupla de enteros (mayor, menor,
      micro), por ejemplo "(3, 1, 8)".

   _emscripten_info.runtime

      Cadena de tiempo de ejecución, por ejemplo, agente de usuario
      del navegador, "'Node.js v14.18.2'", o "'UNKNOWN'".

   _emscripten_info.pthreads

      "True" si Python está compilado con soporte para pthreads de
      Emscripten.

   _emscripten_info.shared_memory

      "True" si Python está compilado con soporte de memoria
      compartida.

   Availability: Emscripten.

   Added in version 3.11.

sys.pycache_prefix

   Si se establece esto (no "None"), Python escribirá archivos ".pyc"
   de caché de código de bytes en (y los leerá desde) un árbol de
   directorios paralelo con raíz en este directorio, en lugar de los
   directorios "__pycache__" en el árbol de código fuente. Se
   ignorarán todos los directorios "__pycache__" en el árbol del
   código fuente y se escribirán nuevos archivos ".pyc" dentro del
   prefijo de pycache. Por lo tanto, si usa "compileall" como paso
   previo a la compilación, debe asegurarse de ejecutarlo con el mismo
   prefijo de pycache (si corresponde) que usará en tiempo de
   ejecución.

   Una ruta relativa se interpreta en relación con el directorio de
   directorio actual.

   Este valor se establece inicialmente en función del valor de la
   opción de línea de comandos "-X" "pycache_prefix=PATH" o la
   variable de entorno "PYTHONPYCACHEPREFIX" (la línea de comandos
   tiene prioridad). Si no se establece ninguno, es "None".

   Added in version 3.8.

sys.excepthook(type, value, traceback)

   Esta función imprime un rastreo y una excepción dados a
   "sys.stderr".

   Cuando se genera y no se detecta una excepción distinta de
   "SystemExit", el intérprete llama a "sys.excepthook" con tres
   argumentos: la clase de excepción, la instancia de excepción y un
   objeto de rastreo. En una sesión interactiva, esto sucede justo
   antes de que se devuelva el control al indicador; en un programa
   Python esto sucede justo antes de que salga el programa. El manejo
   de dichas excepciones de nivel superior se puede personalizar
   asignando otra función de tres argumentos a "sys.excepthook".

   Genere un evento de auditoría "sys.excepthook" con argumentos
   "hook", "type", "value", "traceback" cuando se produzca una
   excepción no detectada. Si no se ha colocado ningún gancho, "hook"
   puede ser "None". Si algún gancho (*hook*) lanza una excepción
   derivada de "RuntimeError", la llamada al gancho será suprimida. De
   lo contrario, se informará que la excepción del gancho de auditoría
   no se puede evaluar y se llamará a "sys.excepthook".

   Ver también:

     La función "sys.unraisablehook()" maneja las excepciones que no
     se pueden evaluar y la función "threading.excepthook()" maneja la
     excepción lanzada por "threading.Thread.run()".

sys.__breakpointhook__
sys.__displayhook__
sys.__excepthook__
sys.__unraisablehook__

   Estos objetos contienen los valores originales de "breakpointhook",
   "displayhook", "excepthook" y "unraisablehook" al inicio del
   programa. Se guardan para que "breakpointhook", "displayhook" y
   "excepthook", "unraisablehook" se puedan restaurar en caso de que
   sean reemplazados por objetos rotos o alternativos.

   Added in version 3.7: __breakpointhook__

   Added in version 3.8: __unraisablehook__

sys.exception()

   Esta función, cuando se llama mientras se ejecuta un manejador de
   excepciones (como una cláusula "except" o "except*"), retorna la
   instancia de la excepción que fue capturada por este manejador.
   Cuando los manejadores de excepciones están anidados unos dentro de
   otros, sólo la excepción manejada por el manejador más interno es
   accesible.

   Si no se está ejecutando ningún manejador de excepciones, esta
   función retorna "None".

   Added in version 3.11.

sys.exc_info()

   Esta función retorna la representación de estilo antiguo de la
   excepción manejada. Si se maneja una excepción "e" (por lo que
   "exception()" retornaría "e"), "exc_info()" retorna la tupla
   "(type(e), e, e.__traceback__)". Es decir, una tupla que contiene
   el tipo de la excepción (una subclase de "BaseException"), la
   propia excepción, y un objeto objeto traceback que suele encapsular
   la pila de llamadas en el punto en el que se produjo la última
   excepción.

   Si no se está manejando ninguna excepción en ninguna parte de la
   pila, esta función retorna una tupla que contiene tres valores
   "None".

   Distinto en la versión 3.11: Los campos "type" y "traceback" ahora
   se derivan del "value" (la instancia de excepción), de modo que
   cuando se modifica una excepción mientras se maneja, los cambios se
   reflejan en los resultados de las subsiguientes llamadas a
   "exc_info()".

sys.exec_prefix

   Una cadena de caracteres que proporciona el prefijo de directorio
   específico del sitio donde están instalados los archivos Python
   dependientes de la plataforma; de forma predeterminada, también es
   "'/usr/local'". Esto se puede configurar en el momento de la
   compilación con el argumento "--exec-prefix" del script
   **configure**. Específicamente, todos los archivos de configuración
   (por ejemplo, el archivo de encabezado "pyconfig.h") se instalan en
   el directorio "*exec_prefix*/lib/python*XY*/config", y los módulos
   de la biblioteca compartida se instalan en
   "*exec_prefix*/lib/python*XY*/lib-dynload", donde *XY* es el número
   de versión de Python, por ejemplo,``3.2``.

   Nota:

     If a virtual environment is in effect, this "exec_prefix" will
     point to the virtual environment. The value for the Python
     installation will still be available, via "base_exec_prefix".
     Refer to Virtual Environments for more information.

   Distinto en la versión 3.14: When running under a virtual
   environment, "prefix" and "exec_prefix" are now set to the virtual
   environment prefix by the path initialization, instead of "site".
   This means that "prefix" and "exec_prefix" always point to the
   virtual environment, even when "site" is disabled ("-S").

sys.executable

   Una cadena de caracteres que proporciona la ruta absoluta del
   binario ejecutable para el intérprete de Python, en sistemas donde
   esto tiene sentido. Si Python no puede recuperar la ruta real a su
   ejecutable, "sys.executable" será una cadena de caracteres vacía o
   "None".

sys.exit([arg])

   Genera una excepción "SystemExit", indicando la intención de salir
   del intérprete.

   The optional argument *arg* can be an integer giving the exit
   status (defaulting to zero), or another type of object.  If it is
   an integer, zero is considered "successful termination" and any
   nonzero value is considered "abnormal termination" by shells and
   the like.  Most systems require it to be in the range 0--127, and
   produce undefined results otherwise.  Some systems have a
   convention for assigning specific meanings to specific exit codes,
   but these are generally underdeveloped; Unix programs generally use
   2 for command line syntax errors and 1 for all other kinds of
   errors.  If another type of object is passed, "None" is equivalent
   to passing zero, and any other object is printed to "stderr" and
   results in an exit code of 1.  In particular, "sys.exit("some error
   message")" is a quick way to exit a program when an error occurs.

   Dado que "exit()" en última instancia "sólo" genera una excepción,
   sólo saldrá del proceso cuando se le llame desde el hilo principal
   y la excepción no se interceptará. Se respetan las acciones de
   limpieza especificadas por las cláusulas finalmente de las
   declaraciones "try" y es posible interceptar el intento de salida
   en un nivel externo.

   Distinto en la versión 3.6: Si se produce un error en la limpieza
   después de que el intérprete de Python haya detectado "SystemSalir"
   (como un error al vaciar los datos almacenados en el búfer en los
   flujos estándar), el estado de salida cambia a 120.

sys.flags

   The *named tuple* *flags* exposes the status of command line flags.
   Flags should only be accessed only by name and not by index.  The
   attributes are read only.

   +----------------------------------------------------+----------------------------------------------------+
   | flags.debug                                        | "-d"                                               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.inspect                                      | "-i"                                               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.interactive                                  | "-i"                                               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.isolated                                     | "-I"                                               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.optimize                                     | "-O" o "-OO"                                       |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.dont_write_bytecode                          | "-B"                                               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.no_user_site                                 | "-s"                                               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.no_site                                      | "-S"                                               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.ignore_environment                           | "-E"                                               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.verbose                                      | "-v"                                               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.bytes_warning                                | "-b"                                               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.quiet                                        | "-q"                                               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.hash_randomization                           | "-R"                                               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.dev_mode                                     | "-X dev" (Modo de desarrollo de Python)            |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.utf8_mode                                    | "-X utf8"                                          |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.safe_path                                    | "-P"                                               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.int_max_str_digits                           | "-X int_max_str_digits" (integer string conversion |
   |                                                    | length limitation)                                 |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.warn_default_encoding                        | "-X warn_default_encoding"                         |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.gil                                          | "-X gil" and "PYTHON_GIL"                          |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.thread_inherit_context                       | "-X thread_inherit_context" and                    |
   |                                                    | "PYTHON_THREAD_INHERIT_CONTEXT"                    |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.context_aware_warnings                       | "-X context_aware_warnings" and                    |
   |                                                    | "PYTHON_CONTEXT_AWARE_WARNINGS"                    |
   +----------------------------------------------------+----------------------------------------------------+

   Distinto en la versión 3.2: Agregado el atributo "quiet" para el
   nuevo flag "-q".

   Added in version 3.2.3: El atributo "hash_randomization".

   Distinto en la versión 3.3: Eliminado el atributo obsoleto
   "division_warning".

   Distinto en la versión 3.4: Agregado el atributo "isolated" para
   el flag "-I" "isolated".

   Distinto en la versión 3.7: Se agregó el atributo "dev_mode" para
   el nuevo Modo de Desarrollo de Python y el atributo "utf8_mode"
   para la bandera "-X" "utf8".

   Distinto en la versión 3.10: Se agregó el atributo
   "warn_default_encoding" para el indicador "-X"
   "warn_default_encoding".

   Distinto en la versión 3.11: Se agregó el atributo "safe_path" para
   la opción "-P".

   Distinto en la versión 3.11: Se agregó el atributo
   "int_max_str_digits".

   Distinto en la versión 3.13: Added the "gil" attribute.

   Distinto en la versión 3.14: Added the "thread_inherit_context"
   attribute.

   Distinto en la versión 3.14: Added the "context_aware_warnings"
   attribute.

sys.float_info

   Un *named tuple* que contiene información sobre el tipo de
   flotante. Contiene información de bajo nivel sobre la precisión y
   la representación interna. Los valores corresponden a las diversas
   constantes de coma flotante definidas en el archivo de encabezado
   estándar "float.h" para el lenguaje de programación 'C'; consulte
   la sección 5.2.4.2.2 de la norma *ISO/IEC* C de 1999 [C99],
   'Características de los tipos flotantes', para obtener más
   detalles.

   Atributos de "float_info" *named tuple*
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   +-----------------------------------+-----------------------------------+-----------------------------------+
   | atributo                          | macro float.h                     | explicación                       |
   |===================================|===================================|===================================|
   | float_info.epsilon                | "DBL_EPSILON"                     | diferencia entre 1,0 y el valor   |
   |                                   |                                   | mínimo mayor que 1,0 que se puede |
   |                                   |                                   | representar como un flotante.     |
   |                                   |                                   | Vea también "math.ulp()".         |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | float_info.dig                    | "DBL_DIG"                         | El número máximo de dígitos       |
   |                                   |                                   | decimales que se pueden           |
   |                                   |                                   | representar fielmente en un       |
   |                                   |                                   | flotante; vea abajo.              |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | float_info.mant_dig               | "DBL_MANT_DIG"                    | Precisión de flotador: el número  |
   |                                   |                                   | de dígitos en base "radix" en el  |
   |                                   |                                   | significado de un flotador.       |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | float_info.max                    | "DBL_MAX"                         | El flotador finito positivo       |
   |                                   |                                   | máximo representable.             |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | float_info.max_exp                | "DBL_MAX_EXP"                     | El entero máximo *e* tal que      |
   |                                   |                                   | "radix**(e-1)" es un flotante     |
   |                                   |                                   | finito representable.             |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | float_info.max_10_exp             | "DBL_MAX_10_EXP"                  | El entero máximo *e* tal que      |
   |                                   |                                   | "10**e" esté en el rango de       |
   |                                   |                                   | flotadores finitos                |
   |                                   |                                   | representables.                   |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | float_info.min                    | "DBL_MIN"                         | El flotador *normalized* positivo |
   |                                   |                                   | mínimo representable.  Usa        |
   |                                   |                                   | "math.ulp(0.0)" para obtener el   |
   |                                   |                                   | menor flotante positivo           |
   |                                   |                                   | *denormalizado* representable.    |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | float_info.min_exp                | "DBL_MIN_EXP"                     | El entero mínimo *e* tal que      |
   |                                   |                                   | "radix**(e-1)" sea un flotante    |
   |                                   |                                   | normalizado.                      |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | float_info.min_10_exp             | "DBL_MIN_10_EXP"                  | El entero mínimo *e* tal que      |
   |                                   |                                   | "10**e" sea un flotante           |
   |                                   |                                   | normalizado.                      |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | float_info.radix                  | "FLT_RADIX"                       | La base de la representación del  |
   |                                   |                                   | exponente.                        |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | float_info.rounds                 | "FLT_ROUNDS"                      | Un número entero que representa   |
   |                                   |                                   | el modo de redondeo para la       |
   |                                   |                                   | aritmética de punto flotante.     |
   |                                   |                                   | Esto refleja el valor de la macro |
   |                                   |                                   | "FLT_ROUNDS" del sistema en el    |
   |                                   |                                   | momento de inicio del intérprete: |
   |                                   |                                   | * "-1": indeterminable  * "0":    |
   |                                   |                                   | toward zero  * "1": to nearest  * |
   |                                   |                                   | "2": toward positive infinity  *  |
   |                                   |                                   | "3": toward negative infinity     |
   |                                   |                                   | Todos los demás valores de        |
   |                                   |                                   | "FLT_ROUNDS" caracterizan el      |
   |                                   |                                   | comportamiento de redondeo        |
   |                                   |                                   | definido por la implementación.   |
   +-----------------------------------+-----------------------------------+-----------------------------------+

   El atributo "sys.float_info.dig" necesita más explicación. Si "s"
   es cualquier cadena que representa un número decimal con como
   máximo "sys.float_info.dig" dígitos significativos, entonces al
   convertir "s" a un flotante y viceversa se recuperará una cadena
   que representa el mismo valor decimal:

      >>> import sys
      >>> sys.float_info.dig
      15
      >>> s = '3.14159265358979'    # decimal string with 15 significant digits
      >>> format(float(s), '.15g')  # convert to float and back -> same value
      '3.14159265358979'

   Pero para cadenas con más de "sys.float_info.dig" dígitos
   significativos, esto no siempre es cierto:

      >>> s = '9876543211234567'    # 16 significant digits is too many!
      >>> format(float(s), '.16g')  # conversion changes value
      '9876543211234568'

sys.float_repr_style

   Una cadena que indica cómo se comporta la función "repr()" para los
   flotantes. Si la cadena tiene el valor "'short'", entonces para un
   flotante finito "x", "repr(x)" tiene como objetivo producir una
   cadena corta con la propiedad de que "float(repr(x)) == x". Este es
   el comportamiento habitual en Python 3.1 y posteriores. De lo
   contrario, "float_repr_style" tiene el valor "'legacy'" y "repr(x)"
   se comporta de la misma manera que en las versiones de Python
   anteriores a la 3.1.

   Added in version 3.1.

sys.getallocatedblocks()

   Return the number of memory blocks currently allocated by the
   interpreter, regardless of their size.  This function is mainly
   useful for tracking and debugging memory leaks.  Because of the
   interpreter's internal caches, the result can vary from call to
   call; you may have to call "_clear_internal_caches()" and
   "gc.collect()" to get more predictable results.

   If a Python build or implementation cannot reasonably compute this
   information, "getallocatedblocks()" is allowed to return 0 instead.

   Added in version 3.4.

sys.getunicodeinternedsize()

   Devuelve el número de objetos unicode que han sido internados.

   Added in version 3.12.

sys.getandroidapilevel()

   Return the build-time API level of Android as an integer. This
   represents the minimum version of Android this build of Python can
   run on. For runtime version information, see
   "platform.android_ver()".

   Availability: Android.

   Added in version 3.7.

sys.getdefaultencoding()

   Return "'utf-8'". This is the name of the default string encoding,
   used in methods like "str.encode()".

sys.getdlopenflags()

   Devuelve el valor actual de los indicadores que se utilizan para
   las llamadas "dlopen()". Los nombres simbólicos para los valores de
   las banderas se pueden encontrar en el módulo "os" (constantes
   "RTLD_*xxx*", por ejemplo, "os.RTLD_LAZY").

   Availability: Unix.

sys.getfilesystemencoding()

   Obtenga *filesystem encoding*: la codificación utilizada con
   *filesystem error handler* para convertir entre nombres de archivos
   Unicode y nombres de archivos en bytes. El controlador de errores
   del sistema de archivos se devuelve desde
   "getfilesystemencodeerrors()".

   Para la mejor compatibilidad, str debe ser usado por nombres de
   archivos en todos los casos, aunque representar nombres de archivos
   en bytes también es soportado. Funciones que acepta o retornan
   nombres de archivos deben soportar tanto str como bytes e
   internamente convertir el valor a representación preferida por el
   sistema.

   "os.fsencode()" y "os.fsdecode()" deben usarse para garantizar que
   se utilizan la codificación correcta y el modo de errores.

   El *codificación del sistema de archivos y manejo de errores* está
   configurado en el inicio de Python por la función
   "PyConfig_Read()": ver "filesystem_encoding" y "filesystem_errors"
   que son miembros de "PyConfig".

   Distinto en la versión 3.2: el resultado de
   "getfilesystemencoding()" ya no puede ser "None".

   Distinto en la versión 3.6: Ya no se garantiza que Windows retorne
   "'mbcs'". Consulte **PEP 529** y "_enablelegacywindowsfsencoding()"
   para obtener más información.

   Distinto en la versión 3.7: Retorna "'utf-8'" si Modo UTF-8 de
   Python esta habilitado.

sys.getfilesystemencodeerrors()

   Obtener la *codificación de sistema de archivos*: La codificación
   usada con el *gestor de errores de sistema de archivos* para
   convertir nombres de archivos en Unicode a nombres de archivos en
   bytes. El gestor de errores del sistema de archivos es retornado
   desde "getfilesystemencoding()".

   "os.fsencode()" y "os.fsdecode()" deben usarse para garantizar que
   se utilizan la codificación correcta y el modo de errores.

   El *codificación del sistema de archivos y manejo de errores* está
   configurado en el inicio de Python por la función
   "PyConfig_Read()": ver "filesystem_encoding" y "filesystem_errors"
   que son miembros de "PyConfig".

   Added in version 3.6.

sys.get_int_max_str_digits()

   Devuelve el valor actual de integer string conversion length
   limitation. Véase también "set_int_max_str_digits()".

   Added in version 3.11.

sys.getrefcount(object)

   Retorna el recuento de referencias del *object*. El recuento
   retornado es generalmente uno más alto de lo que cabría esperar,
   porque incluye la referencia (temporal) como argumento para
   "getrefcount()".

   Note that the returned value may not actually reflect how many
   references to the object are actually held.  For example, some
   objects are *immortal* and have a very high refcount that does not
   reflect the actual number of references.  Consequently, do not rely
   on the returned value to be accurate, other than a value of 0 or 1.

   **Detalles de implementación de CPython:** *Immortal* objects with
   a large reference count can be identified via "_is_immortal()".

   Distinto en la versión 3.12: Los objetos inmortales tienen
   refcounts muy grandes que no coinciden con el número real de
   referencias al objeto.

sys.getrecursionlimit()

   Retorna el valor actual del límite de recursividad, la profundidad
   máxima de la pila de intérpretes de Python. Este límite evita que
   la recursividad infinita cause un desbordamiento de la pila C y
   bloquee Python. Se puede configurar mediante "setrecursionlimit()".

sys.getsizeof(object[, default])

   Retorna el tamaño de un objeto en bytes. El objeto puede ser
   cualquier tipo de objeto. Todos los objetos integrados retornarán
   resultados correctos, pero esto no tiene por qué ser cierto para
   las extensiones de terceros, ya que es una implementación
   específica.

   Solo se tiene en cuenta el consumo de memoria atribuido
   directamente al objeto, no el consumo de memoria de los objetos a
   los que se refiere.

   Si se proporciona, se retornará *predeterminado* si el objeto no
   proporciona los medios para recuperar el tamaño. De lo contrario,
   se lanzará un "TypeError".

   "getsizeof()" llama al método "__sizeof__" del objeto y agrega una
   sobrecarga adicional del recolector de basura si el objeto es
   administrado por el recolector de basura.

   See recursive sizeof recipe for an example of using "getsizeof()"
   recursively to find the size of containers and all their contents.

sys.getswitchinterval()

   Return the interpreter's "thread switch interval" in seconds; see
   "setswitchinterval()".

   Added in version 3.2.

sys._getframe([depth])

   Retorna un objeto de marco de la pila de llamadas. Si se
   proporciona un entero opcional *depth*, retorna el objeto de marco
   que muchas llamadas debajo de la parte superior de la pila. Si eso
   es más profundo que la pila de llamadas, se lanza "ValueError". El
   valor predeterminado de *depth* es cero, lo que retorna el marco en
   la parte superior de la pila de llamadas.

   Genera un auditing event "sys._getframe" con el argumento "frame".

   Esta función debe utilizarse únicamente para fines internos y
   especializados. No se garantiza que exista en todas las
   implementaciones de Python.

sys._getframemodulename([depth])

   Devuelve el nombre de un módulo de la pila de llamadas. Si se
   proporciona el entero opcional *depth*, devuelve el módulo que
   muchas llamadas se encuentran debajo de la parte superior de la
   pila. Si es más profundo que la pila de llamadas, o si el módulo no
   es identificable, se devuelve "None". El valor predeterminado para
   *depth* es cero, lo que devuelve el módulo a la parte superior de
   la pila de llamadas.

   Genera un auditing event "sys._getframemodulename" con el argumento
   "depth".

   Esta función debe utilizarse únicamente para fines internos y
   especializados. No se garantiza que exista en todas las
   implementaciones de Python.

   Added in version 3.12.

sys.getobjects(limit[, type])

   This function only exists if CPython was built using the
   specialized configure option "--with-trace-refs". It is intended
   only for debugging garbage-collection issues.

   Return a list of up to *limit* dynamically allocated Python
   objects. If *type* is given, only objects of that exact type (not
   subtypes) are included.

   Objects from the list are not safe to use. Specifically, the result
   will include objects from all interpreters that share their object
   allocator state (that is, ones created with
   "PyInterpreterConfig.use_main_obmalloc" set to 1 or using
   "Py_NewInterpreter()", and the main interpreter). Mixing objects
   from different interpreters may lead to crashes or other unexpected
   behavior.

   **Detalles de implementación de CPython:** This function should be
   used for specialized purposes only. It is not guaranteed to exist
   in all implementations of Python.

   Distinto en la versión 3.14: The result may include objects from
   other interpreters.

sys.getprofile()

   Obtiene la función de generador de perfiles establecida por
   "setprofile()".

sys.gettrace()

   Obtiene la función de seguimiento (*trace*) establecida por
   "settrace()".

   La función "gettrace()" está pensada solo para implementar
   depuradores, perfiladores, herramientas de cobertura y similares.
   Su comportamiento es parte de la plataforma de implementación, en
   lugar de parte de la definición del lenguaje y, por lo tanto, es
   posible que no esté disponible en todas las implementaciones de
   Python.

sys.getwindowsversion()

   Retorna una tupla con nombre que describe la versión de Windows que
   se está ejecutando actualmente. Los elementos nombrados son
   *major*, *minor*, *build*, *platform*, *service_pack*,
   *service_pack_minor*, *service_pack_major*, *suite_mask*,
   *product_type* y *platform_version*. *service_pack* contiene una
   cadena de caracteres, *platform_version* una tupla de 3 y todos los
   demás valores son números enteros. También se puede acceder a los
   componentes por su nombre, por lo que "sys.getwindowsversion()[0]"
   es equivalente a "sys.getwindowsversion().major". Para
   compatibilidad con versiones anteriores, solo los primeros 5
   elementos se pueden recuperar mediante la indexación.

   *platform* será "2" (VER_PLATFORM_WIN32_NT).

   *product_type* puede ser uno de los siguientes valores:

   +-----------------------------------------+-----------------------------------+
   | Constante                               | Significado                       |
   |=========================================|===================================|
   | "1" (VER_NT_WORKSTATION)                | El sistema es una estación de     |
   |                                         | trabajo.                          |
   +-----------------------------------------+-----------------------------------+
   | "2" (VER_NT_DOMAIN_CONTROLLER)          | El sistema es un controlador de   |
   |                                         | dominio.                          |
   +-----------------------------------------+-----------------------------------+
   | "3" (VER_NT_SERVER)                     | El sistema es un servidor, pero   |
   |                                         | no un controlador de dominio.     |
   +-----------------------------------------+-----------------------------------+

   Esta función envuelve la función Win32 "GetVersionEx()"; consulte
   la documentación de Microsoft sobre "OSVERSIONINFOEX()" para
   obtener más información sobre estos campos.

   *platform_version* retorna la versión principal, la versión
   secundaria y el número de compilación del sistema operativo actual,
   en lugar de la versión que se está emulando para el proceso. Está
   diseñado para su uso en el registro en lugar de para la detección
   de características.

   Nota:

     *platform_version* deriva la versión desde kernel32.dll que puede
     ser de una versión diferente a la versión de SO. Por favor usar
     el módulo "platform" para obtener una versión de SO precisa.

   Availability: Windows.

   Distinto en la versión 3.2: Cambiada a una tupla con nombre y
   agregado *service_pack_minor*, *service_pack_major*, *suite_mask*,
   y *product_type*.

   Distinto en la versión 3.6: Agregado *platform_version*

sys.get_asyncgen_hooks()

   Devuelve un objeto *asyncgen_hooks*, que es similar a un
   "namedtuple" con el formato "(firstiter, finalizer)", donde se
   espera que *firstiter* y *finalizer* sean "None" o funciones que
   toman un *asynchronous generator iterator* como argumento y se
   utilizan para programar la finalización de un generador asíncrono
   mediante un bucle de eventos. .

   Added in version 3.6: Ver **PEP 525** para más detalles.

   Nota:

     Esta función se ha añadido de forma provisional (consulte **PEP
     411** para obtener más detalles).

sys.get_coroutine_origin_tracking_depth()

   Obtiene la profundidad de seguimiento del origen de la corrutina
   actual, según lo establecido por
   "set_coroutine_origin_tracking_depth()".

   Added in version 3.7.

   Nota:

     Esta función se ha añadido de forma provisional (consulte **PEP
     411** para obtener más detalles). Úsela sólo para fines de
     depuración.

sys.hash_info

   A *named tuple* dando parámetros de la implementación de hash
   numérico. Para obtener más detalles sobre el hash de tipos
   numéricos, consulte Calculo del hash de tipos numéricos.

   hash_info.width

      El ancho en bits utilizado para los valores hash.

   hash_info.modulus

      El módulo principal P utilizado para el esquema hash numérico

   hash_info.inf

      El valor hash devuelto para un infinito positivo

   hash_info.nan

      (Este atributo ya no se utiliza)

   hash_info.imag

      El multiplicador utilizado para la parte imaginaria de un número
      complejo.

   hash_info.algorithm

      El nombre del algoritmo para el hash de cadena, bytes y vista de
      memoria.

   hash_info.hash_bits

      El tamaño de salida interno del algoritmo hash.

   hash_info.seed_bits

      El tamaño de la clave semilla del algoritmo hash.

   hash_info.cutoff

      Cutoff for small string DJBX33A optimization in range "[1,
      cutoff)".

   Added in version 3.2.

   Distinto en la versión 3.4: Added *algorithm*, *hash_bits*,
   *seed_bits*, and *cutoff*.

sys.hexversion

   El número de versión codificado como un solo entero. Se garantiza
   que esto aumentará con cada versión, incluido el soporte adecuado
   para versiones que no son de producción. Por ejemplo, para probar
   que el intérprete de Python es al menos la versión 1.5.2, use:

      if sys.hexversion >= 0x010502F0:
          # use some advanced feature
          ...
      else:
          # use an alternative implementation or warn the user
          ...

   Esto se llama "hexversion" ya que solo parece realmente
   significativo cuando se ve como el resultado de pasarlo a la
   función incorporada "hex()". El *named tuple* "sys.version_info"
   puede usarse para una codificación más amigable para los humanos de
   la misma información.

   Se pueden encontrar más detalles de "hexversion" en Versiones de
   API y ABI.

sys.implementation

   Un objeto que contiene información sobre la implementación del
   intérprete de Python en ejecución. Los siguientes atributos deben
   existir en todas las implementaciones de Python.

   *name* es el identificador de la implementación, por ejemplo
   "'cpython'". La cadena de caracteres real está definida por la
   implementación de Python, pero se garantiza que estará en
   minúsculas.

   *version* es una tupla con nombre, en el mismo formato que
   "sys.version_info". Representa la versión de la *implementación* de
   Python. Esto tiene un significado distinto de la versión específica
   del *lenguaje* de Python al que se ajusta el intérprete que se está
   ejecutando actualmente, que representa "sys.version_info". Por
   ejemplo, para PyPy 1.8 "sys.implementation.version" podría ser
   "sys.version_info(1, 8, 0, 'final', 0)", mientras que
   "sys.version_info" sería "sys.version_info(2, 7, 2, 'final', 0)".
   Para CPython tienen el mismo valor, ya que es la implementación de
   referencia.

   *hexversion* es la versión de implementación en formato
   hexadecimal, como "sys.hexversion".

   *cache_tag* es la etiqueta utilizada por la maquinaria de
   importación en los nombres de archivo de los módulos almacenados en
   caché. Por convención, sería una combinación del nombre y la
   versión de la implementación, como "'cpython-33'". Sin embargo, una
   implementación de Python puede usar algún otro valor si
   corresponde. Si "cache_tag" está configurado como "None", indica
   que el almacenamiento en caché del módulo debe estar deshabilitado.

   *supports_isolated_interpreters* is a boolean value, whether this
   implementation supports multiple isolated interpreters. It is
   "True" for CPython on most platforms.  Platforms with this support
   implement the low-level "_interpreters" module.

   Ver también:

     **PEP 684**, **PEP 734**, and "concurrent.interpreters".

   "sys.implementation" puede contener atributos adicionales
   específicos de la implementación de Python. Estos atributos no
   estándar deben comenzar con un guion bajo y no se describen aquí.
   Independientemente de su contenido, "sys.implementation" no
   cambiará durante la ejecución del intérprete, ni entre las
   versiones de implementación. (Sin embargo, puede cambiar entre las
   versiones del lenguaje Python). Consulte **PEP 421** para obtener
   más información.

   Added in version 3.3.

   Distinto en la versión 3.14: Added "supports_isolated_interpreters"
   field.

   Nota:

     La adición de nuevos atributos obligatorios debe pasar por el
     proceso normal de PEP. Consulte **PEP 421** para obtener más
     información.

sys.int_info

   Un *named tuple* que contiene información sobre la representación
   interna de Python de los enteros. Los atributos son de solo
   lectura.

   int_info.bits_per_digit

      El número de bits contenidos en cada dígito. Los enteros de
      Python se almacenan internamente en la base
      "2**int_info.bits_per_digit".

   int_info.sizeof_digit

      El tamaño en bytes del tipo C utilizado para representar un
      dígito.

   int_info.default_max_str_digits

      El valor predeterminado para "sys.get_int_max_str_digits()"
      cuando no está configurado explícitamente de otra manera.

   int_info.str_digits_check_threshold

      El valor mínimo distinto de cero para
      "sys.set_int_max_str_digits()", "PYTHONINTMAXSTRDIGITS" o "-X
      int_max_str_digits".

   Added in version 3.1.

   Distinto en la versión 3.11: Se agregaron "default_max_str_digits"
   y "str_digits_check_threshold".

sys.__interactivehook__

   Cuando existe este atributo, su valor se llama automáticamente (sin
   argumentos) cuando se lanza el intérprete en modo interactivo. Esto
   se hace después de leer el archivo "PYTHONSTARTUP", para que pueda
   establecer este enlace allí. El módulo "site" establece este.

   Lanza un auditing event "cpython.run_interactivehook" con el objeto
   gancho (*hook*) como argumento cuando se llama al gancho en el
   inicio.

   Added in version 3.4.

sys.intern(string)

   Ingresa *string* en la tabla de cadenas de caracteres "internadas"
   y retorna la cadena de caracteres interna, que es *string* en sí
   misma o una copia. Internar cadenas de caracteres es útil para
   obtener un poco de rendimiento en la búsqueda de diccionario: si
   las claves en un diccionario están internadas y la clave de
   búsqueda está interna, las comparaciones de claves (después del
   hash) se pueden realizar mediante una comparación de punteros en
   lugar de una comparación de cadenas. Normalmente, los nombres
   utilizados en los programas de Python se internan automáticamente,
   y los diccionarios utilizados para contener los atributos de
   módulo, clase o instancia tienen claves internas.

   Interned strings are not *immortal*; you must keep a reference to
   the return value of "intern()" around to benefit from it.

sys._is_gil_enabled()

   Return "True" if the *GIL* is enabled and "False" if it is
   disabled.

   Added in version 3.13.

   **Detalles de implementación de CPython:** It is not guaranteed to
   exist in all implementations of Python.

sys.is_finalizing()

   Return "True" if the main Python interpreter is *shutting down*.
   Return "False" otherwise.

   See also the "PythonFinalizationError" exception.

   Added in version 3.5.

sys._jit

   Utilities for observing just-in-time compilation.

   **Detalles de implementación de CPython:** JIT compilation is an
   *experimental implementation detail* of CPython. "sys._jit" is not
   guaranteed to exist or behave the same way in all Python
   implementations, versions, or build configurations.

   Added in version 3.14.

   _jit.is_available()

      Return "True" if the current Python executable supports JIT
      compilation, and "False" otherwise.  This can be controlled by
      building CPython with the "--experimental-jit" option on
      Windows, and the "--enable-experimental-jit" option on all other
      platforms.

   _jit.is_enabled()

      Return "True" if JIT compilation is enabled for the current
      Python process (implies "sys._jit.is_available()"), and "False"
      otherwise. If JIT compilation is available, this can be
      controlled by setting the "PYTHON_JIT" environment variable to
      "0" (disabled) or "1" (enabled) at interpreter startup.

   _jit.is_active()

      Return "True" if the topmost Python frame is currently executing
      JIT code (implies "sys._jit.is_enabled()"), and "False"
      otherwise.

      Nota:

        This function is intended for testing and debugging the JIT
        itself. It should be avoided for any other purpose.

      Nota:

        Due to the nature of tracing JIT compilers, repeated calls to
        this function may give surprising results. For example,
        branching on its return value will likely lead to unexpected
        behavior (if doing so causes JIT code to be entered or
        exited):

           >>> for warmup in range(BIG_NUMBER):
           ...     # This line is "hot", and is eventually JIT-compiled:
           ...     if sys._jit.is_active():
           ...         # This line is "cold", and is run in the interpreter:
           ...         assert sys._jit.is_active()
           ...
           Traceback (most recent call last):
             File "<stdin>", line 5, in <module>
               assert sys._jit.is_active()
                      ~~~~~~~~~~~~~~~~~~^^
           AssertionError

sys.last_exc

   Esta variable no siempre está definida; se establece en la
   instancia de excepción cuando no se maneja una excepción y el
   intérprete imprime un mensaje de error y un seguimiento de la pila.
   Su uso previsto es permitir que un usuario interactivo importe un
   módulo depurador y realice una depuración post-mortem sin tener que
   volver a ejecutar el comando que causó el error. (El uso típico es
   "import pdb; pdb.pm()" para ingresar al depurador post-mortem;
   consulte el módulo "pdb" para obtener más información).

   Added in version 3.12.

sys._is_immortal(op)

   Return "True" if the given object is *immortal*, "False" otherwise.

   Nota:

     Objects that are immortal (and thus return "True" upon being
     passed to this function) are not guaranteed to be immortal in
     future versions, and vice versa for mortal objects.

   Added in version 3.14.

   **Detalles de implementación de CPython:** This function should be
   used for specialized purposes only. It is not guaranteed to exist
   in all implementations of Python.

sys._is_interned(string)

   Return "True" if the given string is "interned", "False" otherwise.

   Added in version 3.13.

   **Detalles de implementación de CPython:** It is not guaranteed to
   exist in all implementations of Python.

sys.last_type
sys.last_value
sys.last_traceback

   Estas tres variables están obsoletas; utilice "sys.last_exc" en su
   lugar. Contienen la representación heredada de "sys.last_exc",
   devuelta por "exc_info()".

sys.maxsize

   Un entero que da el valor máximo que puede tomar una variable de
   tipo "Py_ssize_t". Suele ser "2**31 - 1" en una plataforma de 32
   bits y "2** 63 - 1" en una plataforma de 64 bits.

sys.maxunicode

   Un número entero que da el valor del punto de código Unicode más
   grande, es decir, "1114111" ("0x10FFFF" en hexadecimal).

   Distinto en la versión 3.3: Antes **PEP 393**, "sys.maxunicode"
   solía ser "0xFFFF" o "0x10FFFF", dependiendo de la opción de
   configuración que especificaba si los caracteres Unicode se
   almacenaban como UCS-2 o UCS-4.

sys.meta_path

   A list of *meta path finder* objects that have their "find_spec()"
   methods called to see if one of the objects can find the module to
   be imported. By default, it holds entries that implement Python's
   default import semantics. The "find_spec()" method is called with
   at least the absolute name of the module being imported. If the
   module to be imported is contained in a package, then the parent
   package's "__path__" attribute is passed in as a second argument.
   The method returns a *module spec*, or "None" if the module cannot
   be found.

   Ver también:

     "importlib.abc.MetaPathFinder"
        La clase base abstracta que define la interfaz de los objetos
        del buscador en "meta_path".

     "importlib.machinery.ModuleSpec"
        La clase concreta que "find_spec()" debería retornar
        instancias de.

   Distinto en la versión 3.4: *Module specs* were introduced in
   Python 3.4, by **PEP 451**.

   Distinto en la versión 3.12: Removed the fallback that looked for a
   "find_module()" method if a "meta_path" entry didn't have a
   "find_spec()" method.

sys.modules

   Este es un diccionario que asigna nombres de módulos a módulos que
   ya se han cargado. Esto se puede manipular para forzar la recarga
   de módulos y otros trucos. Sin embargo, reemplazar el diccionario
   no necesariamente funcionará como se esperaba y eliminar elementos
   esenciales del diccionario puede provocar que Python falle. Si
   desea iterar sobre este diccionario global, utilice siempre
   "sys.modules.copy()" o "tuple(sys.modules)" para evitar
   excepciones, ya que su tamaño puede cambiar durante la iteración
   como efecto secundario del código o la actividad en otros
   subprocesos.

sys.orig_argv

   La lista de los argumentos originales de la línea de comando que
   son pasados al ejecutable de Python.

   The elements of "sys.orig_argv" are the arguments to the Python
   interpreter, while the elements of "sys.argv" are the arguments to
   the user's program. Arguments consumed by the interpreter itself
   will be present in "sys.orig_argv" and missing from "sys.argv".

   Added in version 3.10.

sys.path

   Una lista de cadenas de caracteres que especifica la ruta de
   búsqueda de módulos. Inicializado desde la variable de entorno
   "PYTHONPATH", más un valor predeterminado que depende de la
   instalación.

   De forma predeterminada, tal como se inicializa al iniciar el
   programa, se antepone una ruta potencialmente insegura a "sys.path"
   (*before* son las entradas insertadas como resultado de
   "PYTHONPATH"):

   * Línea de comando "python -m module": anteponga el directorio de
     trabajo actual.

   * "python script.py" línea de comandos: anteponer el directorio del
     script. Si es un enlace simbólico, resuelve los enlaces
     simbólicos.

   * Líneas de comando "python -c code" y "python" (REPL): anteponen
     una cadena vacía, que significa el directorio de trabajo actual.

   Para no anteponer esta ruta potencialmente insegura, utilice la
   opción de línea de comando "-P" o la variable de entorno
   "PYTHONSAFEPATH".

   Un programa es libre de modificar esta lista para sus propios
   fines. Sólo se deben agregar cadenas a "sys.path"; todos los demás
   tipos de datos se ignoran durante la importación.

   Ver también:

     * Módulo "site" Esto describe cómo usar archivos .pth para
       extender "sys.path".

sys.path_hooks

   Una lista de invocables que toman un argumento de ruta para
   intentar crear un *finder* para la ruta. Si se puede crear un
   buscador, el invocable debe retornar; de lo contrario, lanza
   "ImportError".

   Especificado originalmente en **PEP 302**.

sys.path_importer_cache

   Un diccionario que actúa como caché para objetos *finder*. Las
   claves son rutas que se han pasado a "sys.path_hooks" y los valores
   son los buscadores que se encuentran. Si una ruta es una ruta de
   sistema de archivos válida pero no se encuentra ningún buscador en
   "sys.path_hooks", entonces se almacena "None".

   Especificado originalmente en **PEP 302**.

sys.platform

   A string containing a platform identifier. Known values are:

   +------------------+-----------------------------+
   | Sistema          | valor "platform"            |
   |==================|=============================|
   | AIX              | "'aix'"                     |
   +------------------+-----------------------------+
   | Android          | "'android'"                 |
   +------------------+-----------------------------+
   | Emscripten       | "'emscripten'"              |
   +------------------+-----------------------------+
   | FreeBSD          | "'freebsd'"                 |
   +------------------+-----------------------------+
   | iOS              | "'ios'"                     |
   +------------------+-----------------------------+
   | Linux            | "'linux'"                   |
   +------------------+-----------------------------+
   | macOS            | "'darwin'"                  |
   +------------------+-----------------------------+
   | Windows          | "'win32'"                   |
   +------------------+-----------------------------+
   | Windows/Cygwin   | "'cygwin'"                  |
   +------------------+-----------------------------+
   | WASI             | "'wasi'"                    |
   +------------------+-----------------------------+

   On Unix systems not listed in the table, the value is the
   lowercased OS name as returned by "uname -s", with the first part
   of the version as returned by "uname -r" appended, e.g. "'sunos5'",
   *at the time when Python was built*. Unless you want to test for a
   specific system version, it is therefore recommended to use the
   following idiom:

      if sys.platform.startswith('sunos'):
          # SunOS-specific code here...

   Distinto en la versión 3.3: On Linux, "sys.platform" doesn't
   contain the major version anymore. It is always "'linux'", instead
   of "'linux2'" or "'linux3'".

   Distinto en la versión 3.8: On AIX, "sys.platform" doesn't contain
   the major version anymore. It is always "'aix'", instead of
   "'aix5'" or "'aix7'".

   Distinto en la versión 3.13: On Android, "sys.platform" now returns
   "'android'" rather than "'linux'".

   Distinto en la versión 3.14: On FreeBSD, "sys.platform" doesn't
   contain the major version anymore. It is always "'freebsd'",
   instead of "'freebsd13'" or "'freebsd14'".

   Ver también:

     "os.name" tiene una granularidad más gruesa. "os.uname()"
     proporciona información de versión dependiente del sistema.

     El módulo "platform" proporciona comprobaciones detalladas de la
     identidad del sistema.

sys.platlibdir

   Nombre del directorio de la biblioteca específica de la plataforma.
   Se utiliza para construir la ruta de la biblioteca estándar y las
   rutas de los módulos de extensión instalados.

   Es igual a ""lib"" en la mayoría de las plataformas. En Fedora y
   SuSE, es igual a ""lib64"" en plataformas de 64 bits, lo que da las
   siguientes rutas "sys.path" (donde "X.Y" es la versión
   "mayor.menor" de Python):

   * "/usr/lib64/pythonX.Y/": Biblioteca estándar (como "os.py" del
     módulo "os")

   * "/usr/lib64/pythonX.Y/lib-dynload/": Módulos de extensión C de la
     biblioteca estándar (como el módulo "errno", el nombre exacto del
     archivo es específico de la plataforma)

   * "/usr/lib/pythonX.Y/site-packages/" (utilice siempre "lib", no
     "sys.platlibdir"): Módulos de terceros

   * "/usr/lib64/pythonX.Y/site-packages/": Módulos de extensión C de
     paquetes de terceros

   Added in version 3.9.

sys.prefix

   Una cadena que proporciona el prefijo del directorio específico del
   sitio donde se instalan los archivos Python independientes de la
   plataforma; en Unix, el valor predeterminado es "/usr/local". Esto
   se puede configurar en el momento de la compilación con el
   argumento "--prefix" del script **configure**. Consulte Rutas de
   instalación para conocer las rutas derivadas.

   Nota:

     If a virtual environment is in effect, this "prefix" will point
     to the virtual environment. The value for the Python installation
     will still be available, via "base_prefix". Refer to Virtual
     Environments for more information.

   Distinto en la versión 3.14: When running under a virtual
   environment, "prefix" and "exec_prefix" are now set to the virtual
   environment prefix by the path initialization, instead of "site".
   This means that "prefix" and "exec_prefix" always point to the
   virtual environment, even when "site" is disabled ("-S").

sys.ps1
sys.ps2

   Cadenas de caracteres que especifican el indicador principal y
   secundario del intérprete. Estos solo se definen si el intérprete
   está en modo interactivo. Sus valores iniciales en este caso son
   "'>>>'" y "'...'". Si se asigna un objeto que no es una cadena a
   cualquiera de las variables, su "str()" se vuelve a evaluar cada
   vez que el intérprete se prepara para leer un nuevo comando
   interactivo; esto se puede utilizar para implementar un mensaje
   dinámico.

sys.setdlopenflags(n)

   Configure los indicadores utilizados por el intérprete para las
   llamadas "dlopen()", como cuando el intérprete carga módulos de
   extensión. Entre otras cosas, esto permitirá una resolución
   diferida de símbolos al importar un módulo, si se llama como
   "sys.setdlopenflags(0)". Para compartir símbolos entre módulos de
   extensión, llame como "sys.setdlopenflags(os.RTLD_GLOBAL)". Los
   nombres simbólicos para los valores de las banderas se pueden
   encontrar en el módulo "os" (constantes "RTLD_*xxx*", por ejemplo,
   "os.RTLD_LAZY").

   Availability: Unix.

sys.set_int_max_str_digits(maxdigits)

   Establece la limitación de la longitud de conversión de cadenas
   enteras utilizada por este intérprete. Véase también
   "get_int_max_str_digits()".

   Added in version 3.11.

sys.setprofile(profilefunc)

   Configura la función de perfil del sistema, que le permite
   implementar un generador de perfiles de código fuente de Python en
   Python. Consulte el capítulo Los perfiladores de Python para
   obtener más información sobre el generador de perfiles de Python.
   La función de perfil del sistema se llama de manera similar a la
   función de seguimiento del sistema (ver "settrace()"), pero se
   llama con diferentes eventos, por ejemplo, no se llama para cada
   línea de código ejecutada (solo al llamar y regresar, pero el
   evento de retorno se informa incluso cuando se ha establecido una
   excepción). La función es específica de subprocesos, pero el
   generador de perfiles no tiene forma de conocer los cambios de
   contexto entre subprocesos, por lo que no tiene sentido usar esto
   en presencia de varios subprocesos. Además, su valor de retorno no
   se usa, por lo que simplemente puede retornar "None". Un error en
   la función del perfil provocará su desarmado.

   Nota:

     The same tracing mechanism is used for "setprofile()" as
     "settrace()". To trace calls with "setprofile()" inside a tracing
     function (e.g. in a debugger breakpoint), see "call_tracing()".

   Las funciones de perfil deben tener tres argumentos: *frame*,
   *event* y *arg*. *frame* es el marco de pila actual. *event* es una
   cadena de caracteres:  "'call'", "'return'", "'c_call'",
   "'c_return'", o "'c_exception'". *arg* depende del tipo de evento.

   Los eventos tienen el siguiente significado:

   "'call'"
      Se llama a una función (o se ingresa algún otro bloque de
      código). Se llama a la función de perfil; *arg* es "None".

   "'return'"
      Una función (u otro bloque de código) está a punto de regresar.
      Se llama a la función de perfil; *arg* es el valor que se
      retornará, o "None" si el evento es causado por una excepción.

   "'c_call'"
      Una función C está a punto de ser llamada. Esta puede ser una
      función de extensión o una incorporada. *arg* es el objeto de
      función de C.

   "'c_return'"
      Ha vuelto una función C. *arg* es el objeto de función de C.

   "'c_exception'"
      Una función C ha generado una excepción. *arg* es el objeto de
      función de C.

   Lanza un auditing event "sys.setprofile" sin argumentos.

sys.setrecursionlimit(limit)

   Establece la profundidad máxima de la pila de intérpretes de Python
   en *limit*. Este límite evita que la recursividad infinita cause un
   desbordamiento de la pila C y bloquee Python.

   El límite más alto posible depende de la plataforma. Un usuario
   puede necesitar establecer un límite más alto cuando tiene un
   programa que requiere una recursividad profunda y una plataforma
   que admite un límite más alto. Esto debe hacerse con cuidado, ya
   que un límite demasiado alto puede provocar un accidente.

   Si el nuevo límite es demasiado bajo en la profundidad de
   recursividad actual, se genera una excepción "RecursionError".

   Distinto en la versión 3.5.1: A la excepción "RecursionError" ahora
   se lanza si el nuevo límite es demasiado bajo en la profundidad de
   recursión actual.

sys.setswitchinterval(interval)

   Establece el intervalo de cambio de hilo del intérprete (en
   segundos). Este valor de punto flotante determina la duración ideal
   de los "segmentos de tiempo" asignados a los subprocesos de Python
   que se ejecutan simultáneamente. Tenga en cuenta que el valor real
   puede ser mayor, especialmente si se utilizan funciones o métodos
   internos de larga duración. Además, qué hilo se programa al final
   del intervalo es decisión del sistema operativo. El intérprete no
   tiene su propio programador.

   Added in version 3.2.

sys.settrace(tracefunc)

   Configura la función de seguimiento del sistema, que le permite
   implementar un depurador de código fuente de Python en Python. La
   función es específica del hilo; para que un depurador admita
   múltiples subprocesos, debe registrar una función de seguimiento
   usando "settrace()" para cada subproceso que se depura o use
   "threading.settrace()".

   Trace functions should have three arguments: *frame*, *event*, and
   *arg*. *frame* is the current stack frame. *event* is a string:
   "'call'", "'line'", "'return'", "'exception'" or "'opcode'".  *arg*
   depends on the event type.

   La función de rastreo se invoca (con *event* establecido en
   "'call'") cada vez que se ingresa un nuevo ámbito local; debe
   retornar una referencia a una función de rastreo local que se usará
   para el nuevo alcance, o "None" si no se debe rastrear el alcance.

   The local trace function should return a reference to itself, or to
   another function which would then be used as the local trace
   function for the scope.

   Si se produce algún error en la función de seguimiento, se
   desarmará, al igual que se llama a "settrace(None)".

   Nota:

     Tracing is disabled while calling the trace function (e.g. a
     function set by "settrace()"). For recursive tracing see
     "call_tracing()".

   Los eventos tienen el siguiente significado:

   "'call'"
      Se llama a una función (o se ingresa algún otro bloque de
      código). Se llama a la función de rastreo global; *arg* es
      "None"; el valor de retorno especifica la función de rastreo
      local.

   "'line'"
      The interpreter is about to execute a new line of code or re-
      execute the condition of a loop.  The local trace function is
      called; *arg* is "None"; the return value specifies the new
      local trace function.  See "Objects/lnotab_notes.txt" for a
      detailed explanation of how this works. Per-line events may be
      disabled for a frame by setting "f_trace_lines" to "False" on
      that frame.

   "'return'"
      Una función (u otro bloque de código) está a punto de regresar.
      Se llama a la función de rastreo local; *arg* es el valor que se
      retornará, o "None" si el evento es causado por una excepción.
      Se ignora el valor de retorno de la función de seguimiento.

   "'exception'"
      Ha ocurrido una excepción. Se llama a la función de rastreo
      local; *arg* es una tupla "(exception, value, traceback)"; el
      valor de retorno especifica la nueva función de rastreo local.

   "'opcode'"
      The interpreter is about to execute a new opcode (see "dis" for
      opcode details).  The local trace function is called; *arg* is
      "None"; the return value specifies the new local trace function.
      Per-opcode events are not emitted by default: they must be
      explicitly requested by setting "f_trace_opcodes" to "True" on
      the frame.

   Tenga en cuenta que como una excepción se propaga a lo largo de la
   cadena de llamadas de funciones, se lanza un evento de
   "'excepción'" en cada nivel.

   Para un uso más detallado, es posible establecer una función de
   seguimiento asignando "frame.f_trace = tracefunc" explícitamente,
   en lugar de confiar en que se establezca indirectamente a través
   del valor de retorno de una función de seguimiento ya instalada.
   Esto también es necesario para activar la función de seguimiento en
   el marco actual, lo cual "settrace()" no funciona. Tenga en cuenta
   que para que esto funcione, se debe haber instalado una función de
   rastreo global con "settrace()" para habilitar la maquinaria de
   rastreo en tiempo de ejecución, pero no necesita ser la misma
   función de rastreo (por ejemplo, podría ser una función de rastreo
   de sobrecarga baja que simplemente retorna "None" para
   deshabilitarse inmediatamente en cada cuadro).

   Para obtener más información sobre los objetos de código y marco,
   consulte Jerarquía de tipos estándar.

   Lanza un auditing event "sys.settrace" sin argumentos.

   La función "settrace()" está pensada únicamente para implementar
   depuradores, perfiladores, herramientas de cobertura y similares.
   Su comportamiento es parte de la plataforma de implementación, en
   lugar de parte de la definición del lenguaje y, por lo tanto, es
   posible que no esté disponible en todas las implementaciones de
   Python.

   Distinto en la versión 3.7: "'opcode'" event type added;
   "f_trace_lines" and "f_trace_opcodes" attributes added to frames

sys.set_asyncgen_hooks([firstiter] [, finalizer])

   Acepta dos argumentos de palabras clave opcionales que son
   invocables que aceptan un *asynchronous generator iterator* como
   argumento. Se llamará al *firstiter* invocable cuando se repita un
   generador asincrónico por primera vez. Se llamará al *finalizer*
   cuando un generador asincrónico esté a punto de ser recolectado
   como basura.

   Lanza un auditing event "sys.set_asyncgen_hooks_firstiter" sin
   argumentos.

   Lanza un auditing event "sys.set_asyncgen_hooks_finalizer" sin
   argumentos.

   Se lanzan dos eventos de auditoría porque la API subyacente consta
   de dos llamadas, cada una de las cuales debe generar su propio
   evento.

   Added in version 3.6: Ver **PEP 525** para más detalles, y para un
   ejemplo de referencia de un método *finalizer* ver la
   implementación de "asyncio.Loop.shutdown_asyncgens" en
   Lib/asyncio/base_events.py

   Nota:

     Esta función se ha añadido de forma provisional (consulte **PEP
     411** para obtener más detalles).

sys.set_coroutine_origin_tracking_depth(depth)

   Allows enabling or disabling coroutine origin tracking. When
   enabled, the "cr_origin" attribute on coroutine objects will
   contain a tuple of (filename, line number, function name) tuples
   describing the traceback where the coroutine object was created,
   with the most recent call first. When disabled, "cr_origin" will be
   "None".

   To enable, pass a *depth* value greater than zero; this sets the
   number of frames whose information will be captured. To disable,
   set *depth* to zero.

   Esta configuración es específica de cada hilo.

   Added in version 3.7.

   Nota:

     Esta función se ha añadido de forma provisional (consulte **PEP
     411** para obtener más detalles). Úsela sólo para fines de
     depuración.

sys.activate_stack_trampoline(backend, /)

   Activa el trampolín *backend* del perfilador de pila. El único
   backend soportado es ""perf"".

   Stack trampolines cannot be activated if the JIT is active.

   Availability: Linux.

   Added in version 3.12.

   Ver también:

     * Soporte de Python para el perfilador perf de Linux

     * https://perf.wiki.kernel.org

sys.deactivate_stack_trampoline()

   Desactive el backend del trampolín del perfilador de pila actual.

   Si no se está ejecutando ningún perfilador, esta función no tiene
   efecto.

   Availability: Linux.

   Added in version 3.12.

sys.is_stack_trampoline_active()

   Retorna "True" si un trampolín de perfil de pila está activo.

   Availability: Linux.

   Added in version 3.12.

sys.remote_exec(pid, script)

   Executes *script*, a file containing Python code in the remote
   process with the given *pid*.

   This function returns immediately, and the code will be executed by
   the target process's main thread at the next available opportunity,
   similarly to how signals are handled. There is no interface to
   determine when the code has been executed. The caller is
   responsible for making sure that the file still exists whenever the
   remote process tries to read it and that it hasn't been
   overwritten.

   The remote process must be running a CPython interpreter of the
   same major and minor version as the local process. If either the
   local or remote interpreter is pre-release (alpha, beta, or release
   candidate) then the local and remote interpreters must be the same
   exact version.

   See Remote debugging attachment protocol for more information about
   the remote debugging mechanism.

   When the code is executed in the remote process, an auditing event
   "sys.remote_exec" is raised with the *pid* and the path to the
   script file. This event is raised in the process that called
   "sys.remote_exec()".

   When the script is executed in the remote process, an auditing
   event "cpython.remote_debugger_script" is raised with the path in
   the remote process. This event is raised in the remote process, not
   the one that called "sys.remote_exec()".

   Availability: Unix, Windows.

   Added in version 3.14: See **PEP 768** for more details.

sys._enablelegacywindowsfsencoding()

   Cambia la *codificación del sistema de archivos y manejo de
   errores* a 'mbcs' y 'replace' respectivamente, para mantener la
   coherencia con las versiones de Python anteriores a la 3.6.

   Esto es equivalente a definir la variable de entorno
   "PYTHONLEGACYWINDOWSFSENCODING" antes de iniciar Python.

   También ver "sys.getfilesystemencoding()" y
   "sys.getfilesystemencodeerrors()".

   Availability: Windows.

   Nota:

     Changing the filesystem encoding after Python startup is risky
     because the old fsencoding or paths encoded by the old fsencoding
     may be cached somewhere. Use "PYTHONLEGACYWINDOWSFSENCODING"
     instead.

   Added in version 3.6: Consulte **PEP 529** para obtener más
   detalles.

   Deprecated since version 3.13, will be removed in version 3.16: Use
   "PYTHONLEGACYWINDOWSFSENCODING" instead.

sys.stdin
sys.stdout
sys.stderr

   *Objetos de archivo* utilizado por el intérprete para entradas,
   salidas y errores estándar:

   * "stdin" se usa para todas las entradas interactivas (incluidas
     las llamadas a "input()");

   * "stdout" se usa para la salida de "print()" y *expression* y para
     las solicitudes de "input()";

   * Las propias indicaciones del intérprete y sus mensajes de error
     van a "stderr".

   Estos flujos son regulares *archivos de texto* como los retornados
   por la función "open()". Sus parámetros se eligen de la siguiente
   manera:

   * The encoding and error handling are initialized from
     "PyConfig.stdio_encoding" and "PyConfig.stdio_errors".

     En Windows, se usa UTF-8 para el dispositivo de consola. Los
     dispositivos que no son caracteres, como archivos de disco y
     tuberías, utilizan la codificación de la configuración regional
     del sistema (por ejemplo, la página de códigos ANSI). Los
     dispositivos de caracteres que no son de consola, como NUL (es
     decir, donde "isatty()" retorna "True") utilizan el valor de las
     páginas de códigos de entrada y salida de la consola al inicio,
     respectivamente para stdin y stdout/stderr. Esto pasa por defecto
     al sistema de *codificación local* si el proceso no esta
     inicialmente acoplado a una consola.

     El comportamiento especial de la consola se puede anular
     configurando la variable de entorno PYTHONLEGACYWINDOWSSTDIO
     antes de iniciar Python. En ese caso, las páginas de códigos de
     la consola se utilizan como para cualquier otro dispositivo de
     caracteres.

     En todas las plataformas, puede anular la codificación de
     caracteres configurando la variable de entorno "PYTHONIOENCODING"
     antes de iniciar Python o usando la nueva "-X" "utf8" opción de
     línea de comando y "PYTHONUTF8" variable de entorno. Sin embargo,
     para la consola de Windows, esto solo se aplica cuando
     "PYTHONLEGACYWINDOWSSTDIO" también está configurado.

   * Cuando es interactivo, el flujo de "stdout" se almacena en búfer
     de línea. En caso contrario, se almacena en búfer de bloque como
     los archivos de texto normales.  El flujo "stderr" tiene un búfer
     de línea en ambos casos.  Puede hacer que ambos flujos no tengan
     búfer pasando la opción de línea de comandos "-u" o estableciendo
     la variable de entorno "PYTHONUNBUFFERED".

   Distinto en la versión 3.9: Ahora, "stderr" no interactivo tiene
   búfer de línea en lugar de búfer completo.

   Nota:

     Para escribir o leer datos binarios desde/hacia los flujos
     estándar, use el objeto binario subyacente "buffer". Por ejemplo,
     para escribir bytes en "stdout", use
     "sys.stdout.buffer.write(b'abc')".However, if you are writing a
     library (and do not control in which context its code will be
     executed), be aware that the standard streams may be replaced
     with file-like objects like "io.StringIO" which do not support
     the "buffer" attribute.

sys.__stdin__
sys.__stdout__
sys.__stderr__

   Estos objetos contienen los valores originales de "stdin", "stderr"
   y "stdout" al inicio del programa. Se utilizan durante la
   finalización y podrían ser útiles para imprimir en el flujo
   estándar real sin importar si el objeto "sys.std*" ha sido
   redirigido.

   También se puede utilizar para restaurar los archivos reales a
   objetos de archivo de trabajo conocidos en caso de que se hayan
   sobrescrito con un objeto roto. Sin embargo, la forma preferida de
   hacer esto es guardar explícitamente la secuencia anterior antes de
   reemplazarla y restaurar el objeto guardado.

   Nota:

     En algunas condiciones, "stdin", "stdout" y "stderr", así como
     los valores originales "__stdin__", "__stdout__" y "__stderr__"
     pueden ser "None" . Suele ser el caso de las aplicaciones GUI de
     Windows que no están conectadas a una consola y las aplicaciones
     Python que comienzan con **pythonw**.

sys.stdlib_module_names

   Un fronzenset de strings que contiene los nombres de los módulos de
   la librería estándar.

   Es lo mismo para todas las plataformas. Módulos que no están
   disponibles en algunas plataformas y deshabilitados durante la
   construcción de Python también son listados. Todos los tipos de
   modulo son listados: Python puro, incorporados, congelados y
   módulos de extensión. Módulos de prueba son excluidos.

   Para paquete, solo el principal es listado; sub-paquetes y sub-
   módulos no son listados. Por ejemplo, el paquete "email" es
   listado, pero el sub-paquete "email.mime" y el sub-módulo
   "email.message" no es listado.

   Consulte también la lista "sys.builtin_module_names".

   Added in version 3.10.

sys.thread_info

   Un *named tuple* que contiene información sobre la implementación
   del hilo.

   thread_info.name

      El nombre de la implementación del hilo:

      * ""nt"": hilos de Windows

      * ""pthread"": hilos de POSIX

      * ""pthread-stubs"": stub de hilos POSIX (en plataformas
        WebAssembly sin soporte de hilos)

      * ""solaris"": hilos de Solaris

   thread_info.lock

      El nombre de la implementación del bloqueo:

      * ""semaphore"": un bloqueo que utiliza un semáforo

      * ""mutex+cond"": un bloqueo que utiliza un mutex y una variable
        de condición

      * "None" si esta información es desconocida

   thread_info.version

      El nombre y la versión de la biblioteca de subprocesos. Es una
      cadena, o "None" si se desconoce esta información.

   Added in version 3.3.

sys.tracebacklimit

   Cuando esta variable se establece en un valor entero, determina el
   número máximo de niveles de información de rastreo que se imprime
   cuando ocurre una excepción no controlada. El valor predeterminado
   es "1000". Cuando se establece en "0" o menos, toda la información
   de rastreo se suprime y solo se imprimen el tipo y el valor de
   excepción.

sys.unraisablehook(unraisable, /)

   Maneja una excepción que no se puede lanzar.

   Se llama cuando se ha producido una excepción pero no hay forma de
   que Python la maneje. Por ejemplo, cuando un destructor lanza una
   excepción o durante la recolección de basura ("gc.collect()").

   El argumento *unraisable* tiene los siguientes atributos:

   * "exc_type": tipo de excepción.

   * "exc_value": Valor de excepción, puede ser "None".

   * "exc_traceback": rastreo de excepción, puede ser "None".

   * "err_msg": Mensaje de error, puede ser "None".

   * "object": Objeto que causa la excepción, puede ser "None".

   El enlace predeterminado da formato a "err_msg" y "object" como:
   "f'{err_msg}: {object!r}'"; utilice el mensaje de error "Excepción
   ignorada en" si "err_msg" es "None".

   "sys.unraisablehook()" se puede anular para controlar cómo se
   manejan las excepciones que no se pueden evaluar.

   Ver también: "excepthook()" que maneja excepciones no detectadas.

   Advertencia:

     Almacenar "exc_value" usando un gancho personalizado puede crear
     un ciclo de referencia. Se debe borrar explícitamente la
     interrupción del ciclo de referencia cuando la excepción ya no
     sea necesaria.Almacenar "object" usando un gancho personalizado
     puede resucitarlo si está configurado en un objeto que se está
     finalizando. Evite almacenar "object" después de que se complete
     el gancho personalizado para evitar resucitar objetos.

   Genera un evento de auditoría "sys.unraisablehook" con los
   argumentos *hook*, *unraisable* cuando ocurre una excepción que no
   se puede manejar. El objeto *unraisable* es el mismo que se pasará
   al gancho. Si no se ha establecido ningún gancho, *hook* puede ser
   "None".

   Added in version 3.8.

sys.version

   Una cadena de caracteres que contiene el número de versión del
   intérprete de Python más información adicional sobre el número de
   compilación y el compilador utilizado. Esta cadena se muestra
   cuando se inicia el intérprete interactivo. No extraiga información
   de la versión de él, en su lugar, use "version_info" y las
   funciones proporcionadas por el módulo "platform".

sys.api_version

   The C API version, equivalent to the C macro "PYTHON_API_VERSION".
   Defined for backwards compatibility.

   Currently, this constant is not updated in new Python versions, and
   is not useful for versioning. This may change in the future.

sys.version_info

   Una tupla que contiene los cinco componentes del número de versión:
   *major*, *minor*, *micro*, *releaselevel*, y *serial*. Todos los
   valores excepto *releaselevel* son números enteros; el nivel de
   lanzamiento es "'alpha'", "'beta'", "'candidate'", o "'final'". El
   valor de "version_info" correspondiente a la versión 2.0 de Python
   es "(2, 0, 0, 'final', 0)". También se puede acceder a los
   componentes por su nombre, por lo que "sys.version_info[0]" es
   equivalente a "sys.version_info.major" y así sucesivamente.

   Distinto en la versión 3.1: Se agregaron atributos de componentes
   con nombre.

sys.warnoptions

   Este es un detalle de implementación del marco de advertencias; No
   modifique este valor. Consulte el módulo "warnings" para obtener
   más información sobre el marco de advertencias.

sys.winver

   The version number used to form registry keys on Windows platforms.
   This is stored as string resource 1000 in the Python DLL.  The
   value is normally the major and minor versions of the running
   Python interpreter.  It is provided in the "sys" module for
   informational purposes; modifying this value has no effect on the
   registry keys used by Python.

   Availability: Windows.

sys.monitoring

   Espacio de nombres(Namespace) que contiene funciones y constantes
   para registrar retrollamadas(callbacks) y controlar eventos de
   monitorización. Véase "sys.monitoring" para más detalles.

sys._xoptions

   Un diccionario de las diversas flags específicas de la
   implementación pasa a través de la opción de línea de comandos
   "-X". Los nombres de las opciones se asignan a sus valores, si se
   dan explícitamente, o a "True". Ejemplo:

      $ ./python -Xa=b -Xc
      Python 3.2a3+ (py3k, Oct 16 2010, 20:14:50)
      [GCC 4.4.3] on linux2
      Type "help", "copyright", "credits" or "license" for more information.
      >>> import sys
      >>> sys._xoptions
      {'a': 'b', 'c': True}

   Esta es una forma específica de CPython de acceder a las opciones
   que se pasan a través de "-X". Otras implementaciones pueden
   exportarlos a través de otros medios, o no exportarlos.

   Added in version 3.2.

-[ Citas ]-

[C99] ISO/CEI 9899:1999. "Lenguajes de programación - C." Un borrador
      público de este estándar está disponible en https://www.open-
      std.org/jtc1/sc22/wg14/www/docs/n1256.pdf.
