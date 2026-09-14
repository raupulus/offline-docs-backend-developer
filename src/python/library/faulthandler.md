---
title: '"faulthandler" --- Dump the Python traceback'
source_url: https://docs.python.org/es/3
source_path: library/faulthandler.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2580
---

# "faulthandler" --- Dump the Python traceback

Added in version 3.3.

======================================================================

This module contains functions to dump Python tracebacks explicitly,
on a fault, after a timeout, or on a user signal. Call
"faulthandler.enable()" to install fault handlers for the "SIGSEGV",
"SIGFPE", "SIGABRT", "SIGBUS", and "SIGILL" signals. You can also
enable them at startup by setting the "PYTHONFAULTHANDLER" environment
variable or by using the "-X" "faulthandler" command line option.

The fault handler is compatible with system fault handlers like Apport
or the Windows fault handler. The module uses an alternative stack for
signal handlers if the "sigaltstack()" function is available. This
allows it to dump the traceback even on a stack overflow.

El gestor de fallos se llama en casos catastróficos y, por lo tanto,
solo puede utilizar funciones seguras en señales (por ejemplo, no
puede asignar memoria en el heap). Debido a esta limitación, el
volcado del rastreo es mínimo comparado a los rastreos normales de
Python:

* Solo se soporta ASCII. El gestor de errores "backslashreplace" se
  utiliza en la codificación.

* Cada cadena de caracteres está limitada a 500 caracteres.

* Solo se muestran el nombre de archivo, el nombre de la función y el
  número de línea. (sin código fuente)

* Está limitado a 100 frames y 100 hilos.

* El orden se invierte: la llamada más reciente se muestra primero.

Por defecto, el rastreo de Python se escribe en "sys.stderr". Para ver
los rastreos, las aplicaciones deben ejecutarse en la terminal.
Alternativamente se puede pasar un archivo de registro a
"faulthandler.enable()".

El módulo está implementado en C, así los rastreos se pueden volcar en
un fallo o cuando Python está en bloqueo mutuo.

El Modo de Desarrollo Python llama a "failurehandler.enable()" al
inicio de Python.

Ver también:

  Módulo "pdb"
     Depurador interactivo de código fuente para programas en Python.

  Módulo "traceback"
     Interfaz estándar para extraer, formatear e imprimir trazas de
     pila de programas en Python.

## Volcar el rastreo

faulthandler.dump_traceback(file=sys.stderr, all_threads=True)

   Vuelca los rastreos de todos los hilos en el archivo *file*. Si
   *all_threads* es "False", vuelca solo el hilo actual.

   Ver también:

     "traceback.print_tb()", que se puede utilizar para imprimir un
     objeto de traza de pila.

   Distinto en la versión 3.5: Se añadió soporte para pasar el
   descriptor de archivo a esta función.

## Dumping the C stack

Added in version 3.14.

faulthandler.dump_c_stack(file=sys.stderr)

   Dump the C stack trace of the current thread into *file*.

   If the Python build does not support it or the operating system
   does not provide a stack trace, then this prints an error in place
   of a dumped C stack.

### C Stack Compatibility

If the system does not support the C-level *backtrace(3)* or
*dladdr1(3)*, then C stack dumps will not work. An error will be
printed instead of the stack.

Additionally, some compilers do not support *CPython's* implementation
of C stack dumps. As a result, a different error may be printed
instead of the stack, even if the operating system supports dumping
stacks.

Nota:

  Dumping C stacks can be arbitrarily slow, depending on the DWARF
  level of the binaries in the call stack.

## Estado del gestor de fallos

faulthandler.enable(file=sys.stderr, all_threads=True, c_stack=True)

   Enable the fault handler: install handlers for the "SIGSEGV",
   "SIGFPE", "SIGABRT", "SIGBUS" and "SIGILL" signals to dump the
   Python traceback. If *all_threads* is "True", produce tracebacks
   for every running thread. Otherwise, dump only the current thread.

   El archivo *file* se debe mantener abierto hasta que se desactive
   el gestor de fallos: ver problema con descriptores de archivo.

   If *c_stack* is "True", then the C stack trace is printed after the
   Python traceback, unless the system does not support it. See
   "dump_c_stack()" for more information on compatibility.

   Distinto en la versión 3.5: Se añadió soporte para pasar el
   descriptor de archivo a esta función.

   Distinto en la versión 3.6: En Windows, también se instaló un
   gestor para la excepción de Windows.

   Distinto en la versión 3.10: Ahora el volcado menciona si se está
   ejecutando una colección de recolectores de basura si *all_threads*
   es verdadero.

   Distinto en la versión 3.14: Only the current thread is dumped if
   the *GIL* is disabled to prevent the risk of data races.

   Distinto en la versión 3.14: The dump now displays the C stack
   trace if *c_stack* is true.

faulthandler.disable()

   Desactiva el gestor de fallos: desinstala los gestores de señales
   instalados por "enable()".

faulthandler.is_enabled()

   Comprueba si el gestor de fallos está activado.

## Volcar los rastreos después de un tiempo de espera

faulthandler.dump_traceback_later(timeout, repeat=False, file=sys.stderr, exit=False)

   Dump the tracebacks of all threads, after a timeout of *timeout*
   seconds, or every *timeout* seconds if *repeat* is "True".  If
   *exit* is "True", call "_exit()" with status=1 after dumping the
   tracebacks.  (Note "_exit()" exits the process immediately, which
   means it doesn't do any cleanup like flushing file buffers.) If the
   function is called twice, the new call replaces previous parameters
   and resets the timeout. The timer has a sub-second resolution.

   El archivo *file* se debe mantener abierto hasta que se vuelque el
   rastreo o se llame a "cancel_dump_traceback_later()": ver problema
   con descriptores de archivo.

   Esta función está implementada utilizando un hilo vigilante.

   Distinto en la versión 3.5: Se añadió soporte para pasar el
   descriptor de archivo a esta función.

   Distinto en la versión 3.7: Ahora esta función está siempre
   disponible.

faulthandler.cancel_dump_traceback_later()

   Cancela la última llamada a "dump_traceback_later()".

## Volcar el rastreo en una señal del usuario

faulthandler.register(signum, file=sys.stderr, all_threads=True, chain=False)

   Registra una señal del usuario: instala un gestor para la señal
   *signum* para volcar el rastreo de todos los hilos, o del hilo
   actual si *all_threads* es "False", en el archivo file. Llama al
   gestor previo si chain es "True".

   El archivo *file* se debe mantener abierto hasta que la señal sea
   anulada por "unregister()": ver problema con descriptores de
   archivo.

   No está disponible en Windows.

   Distinto en la versión 3.5: Se añadió soporte para pasar el
   descriptor de archivo a esta función.

faulthandler.unregister(signum)

   Anula una señal del usuario: desinstala el gestor de la señal
   *signum* instalada por "register()". Retorna "True" si la señal fue
   registrada, "False" en otro caso.

   No está disponible en Windows.

## Problema con descriptores de archivo

"enable()", "dump_traceback_later()" y "register()" guardan el
descriptor de archivo de su argumento *file*. Si se cierra el archivo
y su descriptor de archivo es reutilizado por un nuevo archivo, o si
se usa "os.dup2()" para reemplazar el descriptor de archivo, el
rastreo se escribirá en un archivo diferente. Llame a estas funciones
nuevamente cada vez que se reemplace el archivo.

## Ejemplo

Ejemplo de un fallo de segmentación en Linux con y sin activar el
gestor de fallos:

   $ python -c "import ctypes; ctypes.string_at(0)"
   Segmentation fault

   $ python -q -X faulthandler
   >>> import ctypes
   >>> ctypes.string_at(0)
   Fatal Python error: Segmentation fault

   Current thread 0x00007fb899f39700 (most recent call first):
     File "/opt/python/Lib/ctypes/__init__.py", line 486 in string_at
     File "<stdin>", line 1 in <module>

   Current thread's C stack trace (most recent call first):
     Binary file "/opt/python/python", at _Py_DumpStack+0x42 [0x5b27f7d7147e]
     Binary file "/opt/python/python", at +0x32dcbd [0x5b27f7d85cbd]
     Binary file "/opt/python/python", at +0x32df8a [0x5b27f7d85f8a]
     Binary file "/usr/lib/libc.so.6", at +0x3def0 [0x77b73226bef0]
     Binary file "/usr/lib/libc.so.6", at +0x17ef9c [0x77b7323acf9c]
     Binary file "/opt/python/build/lib.linux-x86_64-3.14/_ctypes.cpython-314d-x86_64-linux-gnu.so", at +0xcdf6 [0x77b7315dddf6]
     Binary file "/usr/lib/libffi.so.8", at +0x7976 [0x77b73158f976]
     Binary file "/usr/lib/libffi.so.8", at +0x413c [0x77b73158c13c]
     Binary file "/usr/lib/libffi.so.8", at ffi_call+0x12e [0x77b73158ef0e]
     Binary file "/opt/python/build/lib.linux-x86_64-3.14/_ctypes.cpython-314d-x86_64-linux-gnu.so", at +0x15a33 [0x77b7315e6a33]
     Binary file "/opt/python/build/lib.linux-x86_64-3.14/_ctypes.cpython-314d-x86_64-linux-gnu.so", at +0x164fa [0x77b7315e74fa]
     Binary file "/opt/python/build/lib.linux-x86_64-3.14/_ctypes.cpython-314d-x86_64-linux-gnu.so", at +0xc624 [0x77b7315dd624]
     Binary file "/opt/python/python", at _PyObject_MakeTpCall+0xce [0x5b27f7b73883]
     Binary file "/opt/python/python", at +0x11bab6 [0x5b27f7b73ab6]
     Binary file "/opt/python/python", at PyObject_Vectorcall+0x23 [0x5b27f7b73b04]
     Binary file "/opt/python/python", at _PyEval_EvalFrameDefault+0x490c [0x5b27f7cbb302]
     Binary file "/opt/python/python", at +0x2818e6 [0x5b27f7cd98e6]
     Binary file "/opt/python/python", at +0x281aab [0x5b27f7cd9aab]
     Binary file "/opt/python/python", at PyEval_EvalCode+0xc5 [0x5b27f7cd9ba3]
     Binary file "/opt/python/python", at +0x255957 [0x5b27f7cad957]
     Binary file "/opt/python/python", at +0x255ab4 [0x5b27f7cadab4]
     Binary file "/opt/python/python", at _PyEval_EvalFrameDefault+0x6c3e [0x5b27f7cbd634]
     Binary file "/opt/python/python", at +0x2818e6 [0x5b27f7cd98e6]
     Binary file "/opt/python/python", at +0x281aab [0x5b27f7cd9aab]
     Binary file "/opt/python/python", at +0x11b6e1 [0x5b27f7b736e1]
     Binary file "/opt/python/python", at +0x11d348 [0x5b27f7b75348]
     Binary file "/opt/python/python", at +0x11d626 [0x5b27f7b75626]
     Binary file "/opt/python/python", at PyObject_Call+0x20 [0x5b27f7b7565e]
     Binary file "/opt/python/python", at +0x32a67a [0x5b27f7d8267a]
     Binary file "/opt/python/python", at +0x32a7f8 [0x5b27f7d827f8]
     Binary file "/opt/python/python", at +0x32ac1b [0x5b27f7d82c1b]
     Binary file "/opt/python/python", at Py_RunMain+0x31 [0x5b27f7d82ebe]
     <truncated rest of calls>
   Segmentation fault
