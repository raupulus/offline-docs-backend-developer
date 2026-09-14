---
title: '"multiprocessing" --- Process-based parallelism'
source_url: https://docs.python.org/es/3
source_path: library/multiprocessing.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3290
---

# "multiprocessing" --- Process-based parallelism

**Código fuente:** Lib/multiprocessing/

======================================================================

Availability: not Android, not iOS, not WASI.

This module is not supported on mobile platforms or WebAssembly
platforms.

## Introducción

"multiprocessing" is a package that supports spawning processes using
an API similar to the "threading" module.  The "multiprocessing"
package offers both local and remote concurrency, effectively side-
stepping the *Global Interpreter Lock* by using subprocesses instead
of threads.  Due to this, the "multiprocessing" module allows the
programmer to fully leverage multiple processors on a given machine.
It runs on both POSIX and Windows.

The "multiprocessing" module also introduces the "Pool" object which
offers a convenient means of parallelizing the execution of a function
across multiple input values, distributing the input data across
processes (data parallelism).  The following example demonstrates the
common practice of defining such functions in a module so that child
processes can successfully import that module.  This basic example of
data parallelism using "Pool",

   from multiprocessing import Pool

   def f(x):
       return x*x

   if __name__ == '__main__':
       with Pool(5) as p:
           print(p.map(f, [1, 2, 3]))

imprimirá la salida estándar

   [1, 4, 9]

The "multiprocessing" module also introduces APIs which do not have
analogs in the "threading" module, like the ability to "terminate",
"interrupt" or "kill" a running process.

Ver también:

  "concurrent.futures.ProcessPoolExecutor" ofrece una interfaz de
  nivel superior para enviar tareas a un proceso en segundo plano sin
  bloquear la ejecución del proceso de llamada. En comparación con el
  uso directo de la interfaz "Pool", la API "concurrent.futures"
  permite separar el envío de trabajo al grupo de procesos subyacente
  de la espera de los resultados.

### La clase "Process"

In "multiprocessing", processes are spawned by creating a "Process"
object and then calling its "start()" method.  "Process" follows the
API of "threading.Thread".  A trivial example of a multiprocess
program is

   from multiprocessing import Process

   def f(name):
       print('hello', name)

   if __name__ == '__main__':
       p = Process(target=f, args=('bob',))
       p.start()
       p.join()

Para mostrar las IDs individuales involucradas en el proceso, aquí hay
un ejemplo ampliado:

   from multiprocessing import Process
   import os

   def info(title):
       print(title)
       print('module name:', __name__)
       print('parent process:', os.getppid())
       print('process id:', os.getpid())

   def f(name):
       info('function f')
       print('hello', name)

   if __name__ == '__main__':
       info('main line')
       p = Process(target=f, args=('bob',))
       p.start()
       p.join()

Para obtener una explicación de por qué es necesaria la parte "if
__name__ == '__main__'" , consulte Pautas de programación.

The arguments to "Process" usually need to be picklable so they can be
passed to the child process. If you tried typing the above example
directly into a REPL it could lead to an "AttributeError" in the child
process trying to locate the *f* function in the "__main__" module.

### Contextos y métodos de inicio

Depending on the platform, "multiprocessing" supports three ways to
start a process.  These *start methods* are

   Generación (*spawn*)
      El proceso principal inicia un nuevo proceso de interpretación
      de Python. El proceso secundario solo heredará los recursos
      necesarios para ejecutar el método "run()" del objeto de
      proceso. En particular, los identificadores y descriptores de
      archivo innecesarios del proceso principal no se heredarán.
      Iniciar un proceso con este método es bastante lento en
      comparación con *fork* o *forkserver*.

      Available on POSIX and Windows platforms.  The default on
      Windows and macOS.

   *fork*
      El proceso parental usa "os.fork()" para bifurcar el intérprete
      de Python. El proceso hijo, cuando comienza, es efectivamente
      idéntico al proceso parental. Todos los recursos del proceso
      parental son heredados por el proceso hijo. Tenga en cuenta que
      bifurcar (*forking*) de forma segura un proceso multihilo es
      problemático.

      Available on POSIX systems.

      Distinto en la versión 3.14: This is no longer the default start
      method on any platform. Code that requires *fork* must
      explicitly specify that via "get_context()" or
      "set_start_method()".

      Distinto en la versión 3.12: If Python is able to detect that
      your process has multiple threads, the "os.fork()" function that
      this start method calls internally will raise a
      "DeprecationWarning". Use a different start method. See the
      "os.fork()" documentation for further explanation.

   *forkserver*
      When the program starts and selects the *forkserver* start
      method, a server process is spawned.  From then on, whenever a
      new process is needed, the parent process connects to the server
      and requests that it fork a new process.  The fork server
      process is single threaded unless system libraries or preloaded
      imports spawn threads as a side-effect so it is generally safe
      for it to use "os.fork()". No unnecessary resources are
      inherited.

      Available on POSIX platforms which support passing file
      descriptors over Unix pipes such as Linux.  The default on
      those.

      Distinto en la versión 3.14: This became the default start
      method on POSIX platforms.

Distinto en la versión 3.4: *spawn* added on all POSIX platforms, and
*forkserver* added for some POSIX platforms. Child processes no longer
inherit all of the parents inheritable handles on Windows.

Distinto en la versión 3.8: On macOS, the *spawn* start method is now
the default.  The *fork* start method should be considered unsafe as
it can lead to crashes of the subprocess as macOS system libraries may
start threads. See bpo-33725.

Distinto en la versión 3.14: On POSIX platforms the default start
method was changed from *fork* to *forkserver* to retain the
performance but avoid common multithreaded process incompatibilities.
See gh-84559.

On POSIX using the *spawn* or *forkserver* start methods will also
start a *resource tracker* process which tracks the unlinked named
system resources (such as named semaphores or "SharedMemory" objects)
created by processes of the program.  When all processes have exited
the resource tracker unlinks any remaining tracked object. Usually
there should be none, but if a process was killed by a signal there
may be some "leaked" resources.  (Neither leaked semaphores nor shared
memory segments will be automatically unlinked until the next reboot.
This is problematic for both objects because the system allows only a
limited number of named semaphores, and shared memory segments occupy
some space in the main memory.)

Para seleccionar un método de inicio, utilice la función
"set_start_method()" en la cláusula "if __name__ == '__main__'" del
módulo principal. Por ejemplo:

   import multiprocessing as mp

   def foo(q):
       q.put('hello')

   if __name__ == '__main__':
       mp.set_start_method('spawn')
       q = mp.Queue()
       p = mp.Process(target=foo, args=(q,))
       p.start()
       print(q.get())
       p.join()

"set_start_method()" no debería ser usada más de una vez en el
programa.

Alternativamente, se puede usar "get_context()" para obtener un objeto
de contexto. Los objetos de contexto tienen la misma API que el módulo
de multiprocesamiento, y permiten utilizar múltiples métodos de inicio
en el mismo programa.

   import multiprocessing as mp

   def foo(q):
       q.put('hello')

   if __name__ == '__main__':
       ctx = mp.get_context('spawn')
       q = ctx.Queue()
       p = ctx.Process(target=foo, args=(q,))
       p.start()
       print(q.get())
       p.join()

Tenga en cuenta que los objetos relacionados con un contexto pueden no
ser compatibles con procesos para un contexto diferente. En
particular, los *locks* creados con el contexto *fork* no se pueden
pasar a los procesos iniciados con los métodos de inicio *spawn* o
*forkserver* .

Libraries using "multiprocessing" or "ProcessPoolExecutor" should be
designed to allow their users to provide their own multiprocessing
context.  Using a specific context of your own within a library can
lead to incompatibilities with the rest of the library user's
application.  Always document if your library requires a specific
start method.

Advertencia:

  The "'spawn'" and "'forkserver'" start methods generally cannot be
  used with "frozen" executables (i.e., binaries produced by packages
  like **PyInstaller** and **cx_Freeze**) on POSIX systems. The
  "'fork'" start method may work if code does not use threads.

### Intercambiando objetos entre procesos

"multiprocessing" supports two types of communication channel between
processes:

**Colas (*queues*)**

   La clase "Queue" es prácticamente un clon de "queue.Queue". Por
   ejemplo:

      from multiprocessing import Process, Queue

      def f(q):
          q.put([42, None, 'hello'])

      if __name__ == '__main__':
          q = Queue()
          p = Process(target=f, args=(q,))
          p.start()
          print(q.get())    # prints "[42, None, 'hello']"
          p.join()

   Queues are thread and process safe. Any object put into a
   "multiprocessing" queue will be serialized.

**Tuberías (*Pipes*)**

   La función "Pipe()" retorna un par de objetos de conexión
   conectados por una tubería (*pipe*) que, por defecto, es un dúplex
   (bidireccional). Por ejemplo:

      from multiprocessing import Process, Pipe

      def f(conn):
          conn.send([42, None, 'hello'])
          conn.close()

      if __name__ == '__main__':
          parent_conn, child_conn = Pipe()
          p = Process(target=f, args=(child_conn,))
          p.start()
          print(parent_conn.recv())   # prints "[42, None, 'hello']"
          p.join()

   Los dos objetos de conexión retornados por "Pipe()" representan los
   dos extremos de la tubería (*pipe*). Cada objeto de conexión tiene
   los métodos "send()" y "recv()" (entre otros). Tenga en cuenta que
   los datos en una tubería pueden corromperse si dos procesos (o
   hilos) intentan leer o escribir en el *mismo* (*same*) extremo de
   la tubería al mismo tiempo. Por supuesto, no hay riesgo de
   corrupción por procesos que utilizan diferentes extremos de la
   tubería (*pipe*) al mismo tiempo.

   The "send()" method serializes the object and "recv()" re-creates
   the object.

### Sincronización entre procesos

"multiprocessing" contains equivalents of all the synchronization
primitives from "threading".  For instance one can use a lock to
ensure that only one process prints to standard output at a time:

   from multiprocessing import Process, Lock

   def f(l, i):
       l.acquire()
       try:
           print('hello world', i)
       finally:
           l.release()

   if __name__ == '__main__':
       lock = Lock()

       for num in range(10):
           Process(target=f, args=(lock, num)).start()

Sin usar el candado (*lock*) de salida de los diferentes procesos, es
probable que todo se mezcle.

### Compartiendo estado entre procesos

Como se mencionó anteriormente, cuando se realiza una programación
concurrente, generalmente es mejor evitar el uso del estado compartido
en la medida de lo posible. Esto es particularmente cierto cuando se
utilizan múltiples procesos.

However, if you really do need to use some shared data then
"multiprocessing" provides a couple of ways of doing so.

**Memoria compartida**

   Los datos se pueden almacenar en un mapa de memoria compartida
   usando "Value" o "Array". Por ejemplo, el siguiente código

      from multiprocessing import Process, Value, Array

      def f(n, a):
          n.value = 3.1415927
          for i in range(len(a)):
              a[i] = -a[i]

      if __name__ == '__main__':
          num = Value('d', 0.0)
          arr = Array('i', range(10))

          p = Process(target=f, args=(num, arr))
          p.start()
          p.join()

          print(num.value)
          print(arr[:])

   imprimirá

      3.1415927
      [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

   Los argumentos "'d'" y "'i'" utilizados al crear "num" y "arr" son
   códigos de tipo del tipo utilizado por "array" module: "'d'" indica
   un flotador de doble precisión y "'i'" indica un entero con signo.
   Estos objetos compartidos serán seguros para procesos y
   subprocesos.

   Para una mayor flexibilidad en el uso de la memoria compartida, se
   puede usar el módulo "multiprocessing.sharedctypes" que admite la
   creación arbitraria de objetos *ctypes* asignados desde la memoria
   compartida.

**Proceso servidor (*Server process*)**

   Un objeto de administrador retornado por "Manager()" controla un
   proceso de servidor que contiene objetos de Python y permite que
   otros procesos los manipulen usando proxies.

   A manager returned by "Manager()" will support types "list",
   "dict", "set", "Namespace", "Lock", "RLock", "Semaphore",
   "BoundedSemaphore", "Condition", "Event", "Barrier", "Queue",
   "Value" and "Array".  For example,

      from multiprocessing import Process, Manager

      def f(d, l, s):
          d[1] = '1'
          d['2'] = 2
          d[0.25] = None
          l.reverse()
          s.add('a')
          s.add('b')

      if __name__ == '__main__':
          with Manager() as manager:
              d = manager.dict()
              l = manager.list(range(10))
              s = manager.set()

              p = Process(target=f, args=(d, l, s))
              p.start()
              p.join()

              print(d)
              print(l)
              print(s)

   imprimirá

      {0.25: None, 1: '1', '2': 2}
      [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
      {'a', 'b'}

   Los administradores de procesos del servidor son más flexibles que
   el uso de objetos de memoria compartida porque pueden hacerse para
   admitir tipos de objetos arbitrarios. Por lo tanto, un solo
   administrador puede ser compartido por procesos en diferentes
   ordenadores a través de una red. Sin embargo, son más lentos que
   usar memoria compartida.

### Usando una piscina de trabajadores (*pool of workers*)

La clase "Pool" representa procesos de piscina de trabajadores (*pool
of workers*). Tiene métodos que permiten que las tareas se descarguen
a los procesos de trabajo de diferentes maneras.

Por ejemplo:

   from multiprocessing import Pool, TimeoutError
   import time
   import os

   def f(x):
       return x*x

   if __name__ == '__main__':
       # start 4 worker processes
       with Pool(processes=4) as pool:

           # print "[0, 1, 4,..., 81]"
           print(pool.map(f, range(10)))

           # print same numbers in arbitrary order
           for i in pool.imap_unordered(f, range(10)):
               print(i)

           # evaluate "f(20)" asynchronously
           res = pool.apply_async(f, (20,))      # runs in *only* one process
           print(res.get(timeout=1))             # prints "400"

           # evaluate "os.getpid()" asynchronously
           res = pool.apply_async(os.getpid, ()) # runs in *only* one process
           print(res.get(timeout=1))             # prints the PID of that process

           # launching multiple evaluations asynchronously *may* use more processes
           multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
           print([res.get(timeout=1) for res in multiple_results])

           # make a single worker sleep for 10 seconds
           res = pool.apply_async(time.sleep, (10,))
           try:
               print(res.get(timeout=1))
           except TimeoutError:
               print("We lacked patience and got a multiprocessing.TimeoutError")

           print("For the moment, the pool remains available for more work")

       # exiting the 'with'-block has stopped the pool
       print("Now the pool is closed and no longer available")

Tenga en cuenta que los métodos de una piscina (*pool*) solo deben ser
utilizados por el proceso que lo creó.

Nota:

  La funcionalidad en este paquete requiere que los procesos hijos
  (*children*) puedan importar el módulo "__main__". Esto está
  cubierto en Pautas de programación sin embargo, vale la pena
  señalarlo aquí. Esto significa que algunos ejemplos, como
  "multiprocessing.pool.Pool" no funcionarán en el intérprete
  interactivo. Por ejemplo:

     >>> from multiprocessing import Pool
     >>> p = Pool(5)
     >>> def f(x):
     ...     return x*x
     ...
     >>> with p:
     ...     p.map(f, [1,2,3])
     Process PoolWorker-1:
     Process PoolWorker-2:
     Process PoolWorker-3:
     Traceback (most recent call last):
     Traceback (most recent call last):
     Traceback (most recent call last):
     AttributeError: Can't get attribute 'f' on <module '__main__' (<class '_frozen_importlib.BuiltinImporter'>)>
     AttributeError: Can't get attribute 'f' on <module '__main__' (<class '_frozen_importlib.BuiltinImporter'>)>
     AttributeError: Can't get attribute 'f' on <module '__main__' (<class '_frozen_importlib.BuiltinImporter'>)>

  (Si intenta esto, en realidad generará tres trazas completas
  intercaladas de forma semialeatoria, y luego tendrá que detener el
  proceso principal de alguna manera)

## Referencia

The "multiprocessing" package mostly replicates the API of the
"threading" module.

### Global start method

Python supports several ways to create and initialize a process. The
global start method sets the default mechanism for creating a process.

Several multiprocessing functions and methods that may also
instantiate certain objects will implicitly set the global start
method to the system's default, if it hasn’t been set already. The
global start method can only be set once. If you need to change the
start method from the system default, you must proactively set the
global start method before calling functions or methods, or creating
these objects.

### "Process" y excepciones

class multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)

   Los objetos de proceso representan la actividad que se ejecuta en
   un proceso separado. La clase "Process" tiene equivalentes para
   todos los métodos "threading.Thread".

   The constructor should always be called with keyword arguments.
   *group* should always be "None"; it exists solely for compatibility
   with "threading.Thread".  *target* is the callable object to be
   invoked by the "run()" method.  It defaults to "None", meaning
   nothing is called. *name* is the process name (see "name" for more
   details). *args* is the argument tuple for the target invocation.
   *kwargs* is a dictionary of keyword arguments for the target
   invocation.  If provided, the keyword-only *daemon* argument sets
   the process "daemon" flag to "True" or "False".  If "None" (the
   default), this flag will be inherited from the creating process.

   De forma predeterminada, no se pasan argumentos a *target*. El
   argumento *args*, que por defecto es "()", se puede usar para
   especificar una lista o tupla de los argumentos para pasar a
   *target*.

   If a subclass overrides the constructor, it must make sure it
   invokes the base class constructor ("super().__init__()") before
   doing anything else to the process.

   Nota:

     In general, all arguments to "Process" must be picklable.  This
     is frequently observed when trying to create a "Process" or use a
     "concurrent.futures.ProcessPoolExecutor" from a REPL with a
     locally defined *target* function.Passing a callable object
     defined in the current REPL session causes the child process to
     die via an uncaught "AttributeError" exception when starting as
     *target* must have been defined within an importable module in
     order to be loaded during unpickling.Example of this uncatchable
     error from the child:

        >>> import multiprocessing as mp
        >>> def knigit():
        ...     print("Ni!")
        ...
        >>> process = mp.Process(target=knigit)
        >>> process.start()
        >>> Traceback (most recent call last):
          File ".../multiprocessing/spawn.py", line ..., in spawn_main
          File ".../multiprocessing/spawn.py", line ..., in _main
        AttributeError: module '__main__' has no attribute 'knigit'
        >>> process
        <SpawnProcess name='SpawnProcess-1' pid=379473 parent=378707 stopped exitcode=1>

     See Los métodos de inicio spawn y forkserver.  While this
     restriction is not true if using the ""fork"" start method, as of
     Python "3.14" that is no longer the default on any platform.  See
     Contextos y métodos de inicio. See also gh-132898.

   Distinto en la versión 3.3: Added the *daemon* parameter.

   run()

      Método que representa la actividad del proceso.

      Puede anular este método en una subclase. El método estándar
      "run()" invoca el objeto invocable pasado al constructor del
      objeto como argumento objetivo, si lo hay, con argumentos
      posicionares y de palabras clave tomados de los argumentos
      *args* y *kwargs*, respectivamente.

      El uso de una lista o tupla como argumento *args* pasado a
      "Process" logra el mismo efecto.

      Ejemplo:

         >>> from multiprocessing import Process
         >>> p = Process(target=print, args=[1])
         >>> p.run()
         1
         >>> p = Process(target=print, args=(1,))
         >>> p.run()
         1

   start()

      Comienza la actividad del proceso.

      Esto debe llamarse como máximo una vez por objeto de proceso.
      Organiza la invocación del método "run()" del objeto en un
      proceso separado.

   join([timeout])

      Si el argumento opcional *timeout* es "None" (el valor
      predeterminado), el método se bloquea hasta que el proceso cuyo
      método "join()" se llama termina. Si *timeout* es un número
      positivo, bloquea como máximo *timeout* segundos. Tenga en
      cuenta que el método retorna "None" si su proceso finaliza o si
      el método agota el tiempo de espera. Verifique el proceso
      "exitcode" para determinar si terminó.

      Un proceso puede unirse muchas veces.

      Un proceso no puede unirse a sí mismo porque esto provocaría un
      punto muerto. Es un error intentar unirse a un proceso antes de
      que se haya iniciado.

   name

      El nombre del proceso. El nombre es una cadena utilizada solo
      con fines de identificación. No tiene semántica. Múltiples
      procesos pueden tener el mismo nombre.

      El nombre inicial es establecido por el constructor. Si no se
      proporciona un nombre explícito al constructor, se forma un
      nombre usando *'Process-N:sub:`1`:N:sub:`2`:...:N:sub:`k`'* se
      construye, donde cada *N:sub:`k`* es el *N-enésimo* hijo del
      parental.

   is_alive()

      Retorna si el proceso está vivo.

      Aproximadamente, un objeto de proceso está vivo desde el momento
      en que el método "start()" retorna hasta que finaliza el proceso
      hijo.

   daemon

      La bandera del proceso *daemon* , es un valor booleano. Esto
      debe establecerse antes de que "start()" sea llamado.

      El valor inicial se hereda del proceso de creación.

      Cuando un proceso sale, intenta terminar todos sus procesos
      demoníacos (*daemonic*) hijos.

      Tenga en cuenta que un proceso demoníaco (*daemonic*) no puede
      crear procesos hijos. De lo contrario, un proceso demoníaco
      (*daemonic*) dejaría a sus hijos huérfanos si se termina cuando
      finaliza su proceso parental. Además, estos **no** son *daemons*
      o servicios de Unix, son procesos normales qué finalizarán (y no
      se unirán) si los procesos no demoníacos han salido.

   Además de API "threading.Thread", los objetos "Process" también
   admiten los siguientes atributos y métodos:

   pid

      Retorna el ID del proceso. Antes de que se genere el proceso,
      esto será "None".

   exitcode

      El código de salida del proceso secundario. Será "None" si el
      proceso aún no ha finalizado.

      Si el método "run()" del proceso secundario se retornó
      normalmente, el código de salida será 0. Si terminó a través de
      "sys.exit()" con un argumento entero *N*, el código de salida
      será *N*.

      Si el proceso secundario finalizó debido a una excepción no
      capturada dentro de "run()", el código de salida será 1. Si fue
      terminado por la señal *N*, el código de salida será el valor
      negativo *-N*.

   authkey

      La clave de autenticación del proceso (una cadena de bytes).

      When "multiprocessing" is initialized the main process is
      assigned a random string using "os.urandom()".

      Cuando se crea un objeto "Process", este heredará la clave de
      autenticación de su proceso parental, aunque esto puede
      cambiarse configurando "authkey" a otra cadena de bytes.

      Consulte Llaves de autentificación.

   sentinel

      Un identificador numérico de un objeto del sistema que estará
      "listo" cuando finalice el proceso.

      You can use this value if you want to wait on several events at
      once using "multiprocessing.connection.wait()".  Otherwise
      calling "join()" is simpler.

      On Windows, this is an OS handle usable with the
      "WaitForSingleObject" and "WaitForMultipleObjects" family of API
      calls.  On POSIX, this is a file descriptor usable with
      primitives from the "select" module.

      Added in version 3.3.

   interrupt()

      Terminate the process. Works on POSIX using the "SIGINT" signal.
      Behavior on Windows is undefined.

      By default, this terminates the child process by raising
      "KeyboardInterrupt". This behavior can be altered by setting the
      respective signal handler in the child process "signal.signal()"
      for "SIGINT".

      Note: if the child process catches and discards
      "KeyboardInterrupt", the process will not be terminated.

      Note: the default behavior will also set "exitcode" to "1" as if
      an uncaught exception was raised in the child process. To have a
      different "exitcode" you may simply catch "KeyboardInterrupt"
      and call "exit(your_code)".

      Added in version 3.14.

   terminate()

      Terminate the process.  On POSIX this is done using the
      "SIGTERM" signal; on Windows "TerminateProcess()" is used.  Note
      that exit handlers and finally clauses, etc., will not be
      executed.

      Tenga en cuenta que los procesos descendientes del proceso *no*
      finalizarán -- simplemente quedarán huérfanos.

      Advertencia:

        Si este método se usa cuando el proceso asociado está usando
        una tubería (*pipe*) o una cola(*queue*), entonces la tubería
        o la cola pueden corromperse y pueden quedar inutilizables por
        otro proceso. Del mismo modo, si el proceso ha adquirido un
        *lock* o un semáforo, etc., su finalización puede provocar el
        bloqueo de otros procesos.

   kill()

      Same as "terminate()" but using the "SIGKILL" signal on POSIX.

      Added in version 3.7.

   close()

      El cierre del objeto "Process", libera todos los recursos
      asociados a él.  "ValueError" se lanza si el proceso subyacente
      aún se está ejecutando. Una vez "close()" se retorna con éxito,
      la mayoría de los otros métodos y atributos del objeto "Process"
      lanzará "ValueError".

      Added in version 3.7.

   Tenga en cuenta que los métodos "start()", "join()", "is_alive()",
   "terminate()" y "exitcode" deberían solo ser llamados por el
   proceso que creó el objeto del proceso.

   Ejemplo de uso de algunos métodos de la "Process":

      >>> import multiprocessing, time, signal
      >>> mp_context = multiprocessing.get_context('spawn')
      >>> p = mp_context.Process(target=time.sleep, args=(1000,))
      >>> print(p, p.is_alive())
      <...Process ... initial> False
      >>> p.start()
      >>> print(p, p.is_alive())
      <...Process ... started> True
      >>> p.terminate()
      >>> time.sleep(0.1)
      >>> print(p, p.is_alive())
      <...Process ... stopped exitcode=-SIGTERM> False
      >>> p.exitcode == -signal.SIGTERM
      True

exception multiprocessing.ProcessError

   The base class of all "multiprocessing" exceptions.

exception multiprocessing.BufferTooShort

   Exception raised by "Connection.recv_bytes_into()" when the
   supplied buffer object is too small for the message read.

   Si "e" es una instancia de "BufferTooShort" entonces "e.args[0]"
   dará el mensaje como una cadena de *bytes*.

exception multiprocessing.AuthenticationError

   Lanzada cuando hay un error de autenticación.

exception multiprocessing.TimeoutError

   Lanzada por métodos con un tiempo de espera (*timeout*) cuando este
   expira.

### Tuberías (*Pipes*) y Colas (*Queues*)

Cuando se usan múltiples procesos, uno generalmente usa el paso de
mensajes para la comunicación entre procesos y evita tener que usar
primitivas de sincronización como *locks*.

Para pasar mensajes se puede usar "Pipe()" (para una conexión entre
dos procesos) o una cola (*queue*)(que permite múltiples productores y
consumidores).

Los tipos "Queue", "SimpleQueue" y "JoinableQueue" son colas multi-
productor, multi-consumidor FIFO (first-in, first-out) (primero en
entrar, primero en salir) modeladas en "queue.Queue" en la biblioteca
estándar. Se diferencian en que "Queue" carece de "task_done()" y
"join()" métodos introducidos en Python 2.5 "queue.Queue" class.

Si usa "JoinableQueue", entonces **debe** llamar a
"JoinableQueue.task_done()" para cada tarea eliminada de la cola
(*queue*) o de lo contrario el semáforo utilizado para contar el
número de tareas sin terminar puede eventualmente desbordarse,
lanzando un excepción.

One difference from other Python queue implementations, is that
"multiprocessing" queues serializes all objects that are put into them
using "pickle". The object returned by the get method is a re-created
object that does not share memory with the original object.

Tenga en cuenta que también se puede crear una cola compartida
mediante el uso de un objeto de administrador -- consulte
Administradores (Managers).

Nota:

  "multiprocessing" uses the usual "queue.Empty" and "queue.Full"
  exceptions to signal a timeout.  They are not available in the
  "multiprocessing" namespace so you need to import them from "queue".

Nota:

  Cuando un objeto se coloca en una cola (*queue*), el objeto se
  serializa (*pickled*) y luego un subproceso de fondo vacía los datos
  serializados a una tubería (*pipe*) subyacente. Esto tiene algunas
  consecuencias que son un poco sorprendentes, pero no deberían causar
  dificultades prácticas: si realmente causan molestias, se puede usar
  una cola creada con un manager.

  1. Después de poner un objeto en una cola vacía, puede haber un
     retraso infinitesimal antes de que el método de la cola "empty()"
     retorne "False" y "get_nowait()" puede retornar sin lanzar
     "queue.Empty".

  2. Si varios procesos están poniendo en cola objetos, es posible que
     los objetos se reciban en el otro extremo fuera de orden. Sin
     embargo, los objetos en cola por el mismo proceso siempre estarán
     en el orden esperado entre sí.

Advertencia:

  Si se termina un proceso usando "Process.terminate()" o "os.kill()"
  mientras intenta usar una clase "Queue", es probable que los datos
  de la cola(*queue*) se corrompan. Esto puede hacer que cualquier
  otro proceso obtenga una excepción cuando intente usar la cola más
  adelante.

Advertencia:

  Como se mencionó anteriormente, si un proceso hijo ha puesto
  elementos en una cola (*queue*) (y no ha utilizado
  "JoinableQueue.cancel_join_thread"), entonces ese proceso no
  terminará hasta que todos los elementos almacenados en búfer hayan
  sido vaciados a la tubería (*pipe*).Esto significa que si intenta
  unirse a ese proceso, puede obtener un punto muerto a menos que esté
  seguro de que todos los elementos que se han puesto en la cola
  (*queue*) se han consumido. Del mismo modo, si el proceso hijo no es
  *daemonic*, el proceso parental puede bloquearse en la salida cuando
  intenta unir todos sus elementos hijos no *daemonic*.Tenga en cuenta
  que una cola (*queue*) creada con un administrador no tiene este
  problema. Consulte Pautas de programación.

Para ver un ejemplo del uso de colas para la comunicación entre
procesos, consulte Ejemplos.

multiprocessing.Pipe(duplex=True)

   Retorna un par de objetos *``(conn1, conn2)``* de la "Connection"
   que representan los extremos de una tubería (*pipe*).

   Si *duplex* es "True" (el valor predeterminado), entonces la
   tubería (*pipe*) es bidireccional. Si *duplex* es "False", entonces
   la tubería es unidireccional: "conn1" solo se puede usar para
   recibir mensajes y "conn2" solo se puede usar para enviar mensajes.

   The "send()" method serializes the object using "pickle" and the
   "recv()" re-creates the object.

class multiprocessing.Queue([maxsize])

   Retorna un proceso de cola (*queue*) compartida implementado
   utilizando una tubería (*pipe*) y algunos candados/semáforos
   (*locks/semaphores*). Cuando un proceso pone por primera vez un
   elemento en la cola, se inicia un hilo alimentador que transfiere
   objetos desde un búfer a la tubería.

   Instantiating this class may set the global start method. See
   Global start method for more details.

   Las excepciones habituales "queue.Empty" y "queue.Full" del módulo
   de la biblioteca estándar "queue" se generan para indicar tiempos
   de espera.

   "Queue" implements all the methods of "queue.Queue" except for
   "task_done()", "join()", and "shutdown()".

   qsize()

      Retorna el tamaño aproximado de la cola (*queue*). Debido a la
      semántica multiproceso/multiprocesamiento, este número no es
      confiable.

      Note that this may raise "NotImplementedError" on platforms like
      macOS where "sem_getvalue()" is not implemented.

   empty()

      Retorna "True" si la cola (*queue*) está vacía, de lo contrario
      retorna "False" . Debido a la semántica
      multiproceso/multiprocesamiento, esto no es confiable.

      May raise an "OSError" on closed queues. (not guaranteed)

   full()

      Retorna "True" si la cola (*queue*) está llena, de lo contrario
      retorna "False" . Debido a la semántica
      multiproceso/multiprocesamiento, esto no es confiable.

   put(obj[, block[, timeout]])

      Pone *obj* en la cola. Si el argumento opcional *block* es
      "True" (el valor predeterminado) y *timeout* es "None" (el valor
      predeterminado), se bloquea si es necesario hasta que haya un
      espacio disponible. Si *timeout* es un número positivo, bloquea
      a lo sumo *timeout* segundos y genera la excepción "queue.Full"
      si no hay espacio libre disponible en ese tiempo. De lo
      contrario (*block* es "False"), y coloca un elemento en la cola
      si hay un espacio libre disponible de inmediato, de lo
      contrario, genera la excepción "queue.Full" (*timeout* se ignora
      en ese caso).

      Distinto en la versión 3.8: Si la cola (*queue*) está cerrada,
      "ValueError" se lanza en lugar de "AssertionError".

   put_nowait(obj)

      Equivalente a "put(obj, False)".

   get([block[, timeout]])

      Elimina y retorna un artículo de la cola (*queue*). Si un
      argumento opcional *block* es "True" (el valor predeterminado) y
      el *timeout* es "None" (el valor predeterminado), es bloqueado
      si es necesario hasta que un elemento esté disponible. Si el
      *timeout* es un número positivo, bloquea a lo sumo segundos y
      genera la excepción "queue.Empty" si no había ningún elemento
      disponible dentro de ese tiempo. De lo contrario (el bloque es
      "False"), retorna un elemento si hay uno disponible de
      inmediato, de lo contrario, levante la excepción "queue.Empty"
      (*timeout* se ignora en ese caso).

      Distinto en la versión 3.8: Si la cola está cerrada, se lanza
      "ValueError" en lugar de "OSError".

   get_nowait()

      Equivalente a "get(False)".

   La "multiprocessing.Queue" tiene algunos métodos adicionales que no
   se encuentran en "queue.Queue". Estos métodos suelen ser
   innecesarios para la mayoría de los códigos:

   close()

      Cierra la cola: libera recursos internos.

      A queue must not be used anymore after it is closed. For
      example, "get()", "put()" and "empty()" methods must no longer
      be called.

      The background thread will quit once it has flushed all buffered
      data to the pipe.  This is called automatically when the queue
      is garbage collected.

   join_thread()

      Unifica al hilo de fondo. Esto solo se puede usar después de que
      se ha llamado a "close()". Esto se bloquea hasta que salga el
      hilo de fondo, asegurando que todos los datos en el búfer se
      hayan vaciado a la tubería (*pipe*).

      Por defecto, si un proceso no es el creador de la cola
      (*queue*), al salir intentará unirse al hilo de fondo de la
      cola. El proceso puede llamar a "cancel_join_thread()" para
      hacer que el "join_thread()" no haga nada.

   cancel_join_thread()

      Evita que "join_thread()" bloquee. En particular, esto evita que
      el subproceso en segundo plano se una automáticamente cuando
      finaliza el proceso; consulte "join_thread()".

      Un mejor nombre para este método podría ser
      "allow_exit_without_flush()".  Es probable que provoque la
      pérdida de datos encolados, y es casi seguro que no necesitará
      usarlo. Realmente solo está allí si necesita que el proceso
      actual salga inmediatamente sin esperar a vaciar los datos en en
      la tubería (*pipe*) subyacente, y no le importan los datos
      perdidos.

   Nota:

     La funcionalidad de esta clase requiere una implementación de
     semáforo compartido en funcionamiento en el sistema operativo que
     es huésped (*host*). Sin uno, la funcionalidad en esta clase se
     deshabilitará, y los intentos de instanciar a "Queue" resultarán
     en "ImportError". Consulte bpo-3770 para información adicional.
     Lo mismo es válido para cualquiera de los tipos de cola
     especializados que se enumeran a continuación.

class multiprocessing.SimpleQueue

   Es un tipo simplificado "Queue", muy similar a un *lock* de "Pipe".

   Instantiating this class may set the global start method. See
   Global start method for more details.

   close()

      Cierra la cola: libera recursos internos.

      Una cola no se debe usar más después de ser cerrada. Por ejemplo
      los métodos "get()", "put()" y "empty()" no deben ser llamados.

      Added in version 3.9.

   empty()

      Retorna "True" si la cola (*queue*) está vacía, de otra manera
      retorna "False".

      Always raises an "OSError" if the SimpleQueue is closed.

   get()

      Eliminar y retornar un artículo de la cola (*queue*).

   put(item)

      Pone *item* en la cola.

class multiprocessing.JoinableQueue([maxsize])

   "JoinableQueue", una subclase "Queue" , es una cola (*queue*) que
   además tiene los métodos "task_done()" y "join()".

   Instantiating this class may set the global start method. See
   Global start method for more details.

   task_done()

      Indica que una tarea anteriormente en cola (*queue*) está
      completa. Usado por los consumidores de la cola. Por cada
      "get()" utilizado para recuperar una tarea, una llamada
      posterior a "task_done()" le dice a la cola que el procesamiento
      de la tarea se ha completado.

      Si un "join()" se está bloqueando actualmente, se reanudará
      cuando se hayan procesado todos los elementos (lo que significa
      que "task_done()" es llamado para cada elemento que había sido
      puesto en cola (*queue*) por "put()").

      Lanza un "ValueError" si es llamado más veces que elementos hay
      en una cola.

   join()

      Se bloquea hasta que todos los elementos en una cola han sido
      recibidos y procesados.

      El recuento de tareas no finalizadas aumenta cada vez que se
      agrega un elemento a la cola. El recuento disminuye cada vez que
      un consumidor llama a "task_done()" para indicar que el artículo
      se recuperó y todo el trabajo en él está completo. Cuando el
      recuento de tareas inacabadas cae a cero, "join()" se
      desbloquea.

### Miscelánea

multiprocessing.active_children()

   Retorna una lista con todos los hijos del proceso actual.

   Llamar a esto tiene el efecto secundario de "unir" (*joining*)
   cualquier proceso que ya haya finalizado.

multiprocessing.cpu_count()

   Retorna el número de CPU en el sistema.

   This number is not equivalent to the number of CPUs the current
   process can use.  The number of usable CPUs can be obtained with
   "os.process_cpu_count()" (or "len(os.sched_getaffinity(0))").

   Cuando no se puede determinar el número de CPUs, se lanza un
   "NotImplementedError".

   Ver también: "os.cpu_count()" "os.process_cpu_count()"

   Distinto en la versión 3.13: The return value can also be
   overridden using the "-X cpu_count" flag or "PYTHON_CPU_COUNT" as
   this is merely a wrapper around the "os" cpu count APIs.

multiprocessing.current_process()

   Retorna el objeto de la "Process" correspondiente al proceso
   actual.

   Un análogo de la "threading.current_thread()".

multiprocessing.parent_process()

   Retorna el objeto de la "Process" correspondiente al proceso
   parental de "current_process()". Para el proceso principal,
   "parent_process" será "None".

   Added in version 3.8.

multiprocessing.freeze_support()

   Add support for when a program which uses "multiprocessing" has
   been frozen to produce an executable.  (Has been tested with
   **py2exe**, **PyInstaller** and **cx_Freeze**.)

   Es necesario llamar a esta función inmediatamente después de la
   línea principal del módulo "if __name__ == '__main__'" . Por
   ejemplo:

      from multiprocessing import Process, freeze_support

      def f():
          print('hello world!')

      if __name__ == '__main__':
          freeze_support()
          Process(target=f).start()

   Si se omite la línea "freeze_support()" entonces se intenta
   comenzar el ejecutable congelado que lanzará "RuntimeError".

   Calling "freeze_support()" has no effect when the start method is
   not *spawn*. In addition, if the module is being run normally by
   the Python interpreter (the program has not been frozen), then
   "freeze_support()" has no effect.

multiprocessing.get_all_start_methods()

   Returns a list of the supported start methods, the first of which
   is the default.  The possible start methods are "'fork'", "'spawn'"
   and "'forkserver'".  Not all platforms support all methods.  See
   Contextos y métodos de inicio.

   Added in version 3.4.

multiprocessing.get_context(method=None)

   Return a context object which has the same attributes as the
   "multiprocessing" module.

   If *method* is "None" then the default context is returned. Note
   that if the global start method has not been set, this will set it
   to the system default See Global start method for more details.
   Otherwise *method* should be "'fork'", "'spawn'", "'forkserver'".
   "ValueError" is raised if the specified start method is not
   available.  See Contextos y métodos de inicio.

   Added in version 3.4.

multiprocessing.get_start_method(allow_none=False)

   Retorna el nombre del método de inicio que es utilizado para
   iniciar procesos.

   If the global start method is not set and *allow_none* is "False",
   the global start method is set to the default, and its name is
   returned. See Global start method for more details.

   The return value can be "'fork'", "'spawn'", "'forkserver'" or
   "None".  See Contextos y métodos de inicio.

   Added in version 3.4.

   Distinto en la versión 3.8: En macOS, el método de inicio *spawn*
   ahora es el predeterminado. El método de inicio *fork* debe
   considerarse inseguro ya que puede provocar bloqueos del
   subproceso. Consulte bpo-33725.

multiprocessing.set_executable(executable)

   Set the path of the Python interpreter to use when starting a child
   process. (By default "sys.executable" is used).  Embedders will
   probably need to do something like

      set_executable(os.path.join(sys.exec_prefix, 'pythonw.exe'))

   antes ellos pueden crear procesos hijos.

   Distinto en la versión 3.4: Now supported on POSIX when the
   "'spawn'" start method is used.

   Distinto en la versión 3.11: Acepta un *path-like object*.

multiprocessing.set_forkserver_preload(module_names)

   Set a list of module names for the forkserver main process to
   attempt to import so that their already imported state is inherited
   by forked processes. Any "ImportError" when doing so is silently
   ignored. This can be used as a performance enhancement to avoid
   repeated work in every process.

   For this to work, it must be called before the forkserver process
   has been launched (before creating a "Pool" or starting a
   "Process").

   Only meaningful when using the "'forkserver'" start method. See
   Contextos y métodos de inicio.

   Added in version 3.4.

multiprocessing.set_start_method(method, force=False)

   Set the method which should be used to start child processes. The
   *method* argument can be "'fork'", "'spawn'" or "'forkserver'".
   Raises "RuntimeError" if the start method has already been set and
   *force* is not "True".  If *method* is "None" and *force* is "True"
   then the start method is set to "None".  If *method* is "None" and
   *force* is "False" then the context is set to the default context.

   Tenga en cuenta que esto debería llamarse como máximo una vez, y
   debería protegerse dentro de la cláusula "if __name__ ==
   '__main__'" del módulo principal.

   See Contextos y métodos de inicio.

   Added in version 3.4.

Nota:

  "multiprocessing" contains no analogues of
  "threading.active_count()", "threading.enumerate()",
  "threading.settrace()", "threading.setprofile()", "threading.Timer",
  or "threading.local".

### Objetos de conexión *Connection Objects*

Los objetos de conexión permiten el envío y la recepción de objetos
serializables (*pickable*) o cadenas de caracteres seleccionables.
Pueden considerarse como sockets conectados orientados a mensajes.

Los objetos de conexión usualmente son creados usando "Pipe" -- ver
también Oyentes y clientes (Listeners and Clients).

class multiprocessing.connection.Connection

   send(obj)

      Envía un objeto al otro extremo de la conexión que debe leerse
      usando "recv()".

      El objeto debe ser serializable (*pickable*). Los serializados
      (*pickable*) muy grandes (aproximadamente 32 *MiB+* , aunque
      depende del sistema operativo) pueden generar una excepción
      "ValueError".

   recv()

      Retorna un objeto enviado desde el otro extremo de la conexión
      usando "send()". Se bloquea hasta que haya algo para recibir. Se
      lanza "EOFError" si no queda nada por recibir y el otro extremo
      está cerrado.

   fileno()

      Retorna el descriptor de archivo o identificador utilizado por
      la conexión.

   close()

      Cierra la conexión.

      Esto se llama automáticamente cuando la conexión es basura
      recolectada.

   poll([timeout])

      Retorna si hay datos disponibles para leer.

      Si no se especifica *timeout*, se retornará de inmediato. Si
      *timeout* es un número, esto especifica el tiempo máximo en
      segundos para bloquear. Si *timeout* es "None", se usa un tiempo
      de espera infinito.

      Tenga en cuenta que se pueden sondear varios objetos de conexión
      a la vez utilizando "multiprocessing.connection.wait()".

   send_bytes(buf[, offset[, size]])

      Envía datos de *bytes* desde a *bytes-like object* como un
      mensaje completo.

      If *offset* is given then data is read from that position in
      *buf*.  If *size* is given then that many bytes will be read
      from *buf*.  Very large buffers (approximately 32 MiB+, though
      it depends on the OS) may raise a "ValueError" exception

   recv_bytes([maxlength])

      Retorna un mensaje completo de datos de *bytes* enviados desde
      el otro extremo de la conexión como una cadena de caracteres. Se
      bloquea hasta que haya algo para recibir. Aumenta "EOFError" si
      no queda nada por recibir y el otro extremo se ha cerrado.

      Si se especifica *maxlength* y el mensaje es más largo que
      *maxlength*, entonces se lanza un "OSError" y la conexión ya no
      será legible.

      Distinto en la versión 3.3: Esta función solía lanzar un
      "IOError", que ahora es un alias de "OSError".

   recv_bytes_into(buf[, offset])

      Read into *buf* a complete message of byte data sent from the
      other end of the connection and return the number of bytes in
      the message.  Blocks until there is something to receive.
      Raises "EOFError" if there is nothing left to receive and the
      other end was closed.

      *buf* must be a writable *bytes-like object*.  If *offset* is
      given then the message will be written into the buffer from that
      position.  Offset must be a non-negative integer less than the
      length of *buf* (in bytes).

      Si el búfer es demasiado corto, se genera una excepción
      "BufferTooShort" y el mensaje completo está disponible como
      "e.args[0]" donde "e" es la instancia de excepción.

   Distinto en la versión 3.3: Los objetos de conexión ahora pueden
   transferirse entre procesos usando "Connection.send()" y
   "Connection.recv()".Connection objects also now support the context
   management protocol -- see Tipos gestores de contexto.
   "__enter__()" returns the connection object, and "__exit__()" calls
   "close()".

Por ejemplo:

   >>> from multiprocessing import Pipe
   >>> a, b = Pipe()
   >>> a.send([1, 'hello', None])
   >>> b.recv()
   [1, 'hello', None]
   >>> b.send_bytes(b'thank you')
   >>> a.recv_bytes()
   b'thank you'
   >>> import array
   >>> arr1 = array.array('i', range(5))
   >>> arr2 = array.array('i', [0] * 10)
   >>> a.send_bytes(arr1)
   >>> count = b.recv_bytes_into(arr2)
   >>> assert count == len(arr1) * arr1.itemsize
   >>> arr2
   array('i', [0, 1, 2, 3, 4, 0, 0, 0, 0, 0])

Advertencia:

  El método "Connection.recv()" desempaqueta automáticamente los datos
  que recibe, lo que puede ser un riesgo de seguridad a menos que
  pueda confiar en el proceso que envió el mensaje.Por lo tanto, a
  menos que el objeto de conexión se haya producido usando "Pipe()"
  solo debe usar los métodos "recv()" y "send()" después de realizar
  algún tipo de autenticación. Consulte Llaves de autentificación.

Advertencia:

  Si se mata un proceso mientras intenta leer o escribir en una
  tubería (*pipe*), entonces es probable que los datos en la tubería
  se corrompan, porque puede ser imposible estar seguro de dónde se
  encuentran los límites del mensaje.

### Primitivas de sincronización (*Synchronization primitives*)

En general, las primitivas de sincronización no son tan necesarias en
un programa multiproceso como en un programa *multihilos*
(*multithreaded*). Consulte la documentación para "threading" .

Tenga en cuenta que también se pueden crear primitivas de
sincronización utilizando un objeto administrador -- consulte
Administradores (Managers).

class multiprocessing.Barrier(parties[, action[, timeout]])

   Un objeto de barrera: un clon de "threading.Barrier".

   Instantiating this class may set the global start method. See
   Global start method for more details.

   Added in version 3.3.

class multiprocessing.BoundedSemaphore([value])

   Un objeto semáforo (*semaphore object*) acotado: un análogo cercano
   de la "threading.BoundedSemaphore".

   Instantiating this class may set the global start method. See
   Global start method for more details.

   Existe una diferencia solitaria de su análogo cercano: el primer
   argumento de su método "acquire" es nombrado *block*, es
   consistente con "Lock.acquire()".

   locked()

      Return a boolean indicating whether this object is locked right
      now.

      Added in version 3.14.

   Nota:

     En macOS, esto no se puede distinguir de "Semaphore" porque
     "sem_getvalue()" no está implementado en esa plataforma.

class multiprocessing.Condition([lock])

   Una variable de condición: un alias para la "threading.Condition".

   If *lock* is specified then it should be a "Lock" or "RLock" object
   from "multiprocessing".

   Instantiating this class may set the global start method. See
   Global start method for more details.

   Distinto en la versión 3.3: El método "wait_for()" fue a añadido.

class multiprocessing.Event

   Un clon de "threading.Event".

   Instantiating this class may set the global start method. See
   Global start method for more details.

class multiprocessing.Lock

   Un objeto candado no recursivo: un análogo cercano de
   "threading.Lock" . Una vez que un proceso o subproceso ha adquirido
   un bloqueo, los intentos posteriores de adquirirlo de cualquier
   proceso o subproceso se bloquearán hasta que se libere; cualquier
   proceso o hilo puede liberarlo. Los conceptos y comportamientos de
   "threading.Lock" como se aplica a los subprocesos se replican aquí
   en "multiprocessing.Lock" como se aplica a los procesos o
   subprocesos, excepto como se indica.

   Tenga en cuenta que "Lock" es en realidad una función de fábrica
   que retorna una instancia de "multiprocessing.synchronize.Lock"
   inicializada con un contexto predeterminado.

   Instantiating this class may set the global start method. See
   Global start method for more details.

   La "Lock" soporta el protocolo *context manager* y, por lo tanto,
   se puede usar en la declaración "with".

   acquire(block=True, timeout=None)

      Adquiriendo un candado (*lock*), bloqueante o no bloqueante.

      Con el argumento *block* establecido en "True" (el valor
      predeterminado), la llamada al método se bloqueará hasta que el
      bloqueo esté en un estado desbloqueado, luego configúrelo como
      bloqueado y retorne "True". Tenga en cuenta que el nombre de
      este primer argumento difiere del que aparece en
      "threading.Lock.acquire()".

      Con el argumento *block* establecido en "False", la llamada al
      método no se bloquea. Si el bloqueo está actualmente en un
      estado bloqueado, retorna "False"; de lo contrario, configure el
      bloqueo en un estado bloqueado y retorne "True".

      Cuando se invoca con un valor positivo de punto flotante para
      *timeout*, bloquea como máximo el número de segundos
      especificado por *timeout* siempre que no se pueda obtener el
      bloqueo. Las invocaciones con un valor negativo para *timeout*
      de cero. Las invocaciones con un valor *timeout* de "None" (el
      valor predeterminado) establecen el período de tiempo de espera
      en infinito. Tenga en cuenta que el tratamiento de valores
      negativos o "None" para *timeout* difiere del comportamiento
      implementado en "threading.Lock.acquire()". El argumento
      *timeout* no tiene implicaciones prácticas si el argumento
      *block* se establece en "False" y, por lo tanto, se ignora.
      Retorna "True" si se ha adquirido el candado o "False" si ha
      transcurrido el tiempo de espera.

   release()

      Suelta un candado. Esto se puede llamar desde cualquier proceso
      o subproceso, no solo desde el proceso o subproceso que
      originalmente adquirió el candado.

      El comportamiento es el mismo que en "threading.Lock.release()"
      excepto que cuando se invoca en un bloqueo desbloqueado, se
      genera a "ValueError".

   locked()

      Return a boolean indicating whether this object is locked right
      now.

      Added in version 3.14.

class multiprocessing.RLock

   Un objeto de candado recursivo: un análogo cercano a
   "threading.RLock". El proceso o el hilo que lo adquirió debe
   liberar un candado recursivo. Una vez que un proceso o subproceso
   ha adquirido un candado recursivo, el mismo proceso o subproceso
   puede volver a adquirirlo sin bloquearlo; ese proceso o hilo debe
   liberarlo una vez por cada vez que se haya adquirido.

   Tenga en cuenta que "RLock" es en realidad una función de fábrica
   que retorna una instancia de "multiprocessing.synchronize.RLock"
   inicializada con un contexto predeterminado.

   Instantiating this class may set the global start method. See
   Global start method for more details.

   La "RLock" admite el protocolo *context manager* y, por lo tanto,
   puede usarse en "with".

   acquire(block=True, timeout=None)

      Adquiriendo un candado (*lock*), bloqueante o no bloqueante.

      Cuando se invoca con el argumento *block* establecido en "True"
      , bloquea hasta que el candado esté en un estado desbloqueado
      (que no sea propiedad de ningún proceso o subproceso) a menos
      que el candado o el subproceso actual ya sea de su propiedad. El
      proceso o subproceso actual se apropia del candado (si aún no lo
      tiene) y el nivel de recursión dentro de este  aumenta en uno,
      lo que da como resultado un valor de retorno de "True". Tenga en
      cuenta que hay varias diferencias en el comportamiento de este
      primer argumento en comparación con la implementación de
      "threading.RLock.acquire()", comenzando con el nombre del
      argumento en sí.

      Cuando se invoca con el argumento *block* establecido en
      "False", no bloquea. Si el candado ya ha sido adquirido (y por
      lo tanto es propiedad) de otro proceso o subproceso, el proceso
      o subproceso actual no se apropia y el nivel de recursión dentro
      del candado no cambia, lo que resulta en un valor de retorno de
      "False". Si el candado está en un estado desbloqueado, el
      proceso o subproceso actual toma posesión y el nivel de
      recurrencia se incrementa, lo que resulta en un valor de retorno
      de "True".

      El uso y los comportamientos del argumento *timeout* son los
      mismos que en "Lock.acquire()". Tenga en cuenta que algunos de
      estos comportamientos de *timeout* difieren de los
      comportamientos implementados en "threading.RLock.acquire()".

   release()

      Libera un candado, disminuyendo el nivel de recursión. Si
      después del decremento el nivel de recursión es cero, restablece
      el candado a desbloqueado (que no sea propiedad de ningún
      proceso o subproceso) y si se bloquean otros procesos o
      subprocesos esperando que el candado se desbloquee, permite que
      continúe exactamente uno de ellos. Si después del decremento el
      nivel de recursión sigue siendo distinto de cero, el candado
      permanece bloqueado y pertenece al proceso de llamada o
      subproceso.

      Solo llame a este método cuando el proceso o subproceso de
      llamada sea el propietario del candado. Se lanza un
      "AssertionError" si se llama a este método mediante un proceso o
      subproceso que no sea el propietario o si el candado está en un
      estado desbloqueado (sin propietario). Tenga en cuenta que el
      tipo de excepción planteada en esta situación difiere del
      comportamiento implementado en "threading.RLock.release()".

   locked()

      Return a boolean indicating whether this object is locked right
      now.

      Added in version 3.14.

class multiprocessing.Semaphore([value])

   Un objeto semáforo: un análogo cercano de "threading.Semaphore".

   Instantiating this class may set the global start method. See
   Global start method for more details.

   Existe una diferencia solitaria de su análogo cercano: el primer
   argumento de su método "acquire" es nombrado *block*, es
   consistente con "Lock.acquire()".

   get_value()

      Return the current value of semaphore.

      Note that this may raise "NotImplementedError" on platforms like
      macOS where "sem_getvalue()" is not implemented.

   locked()

      Return a boolean indicating whether this object is locked right
      now.

      Added in version 3.14.

Nota:

  En macOS, "sem_timedwait" no es compatible, por lo que llamar a
  "acquire()" con un tiempo de espera emulará el comportamiento de esa
  función utilizando un bucle inactivo.

Nota:

  Parte de la funcionalidad de este paquete requiere una
  implementación de semáforo compartido que funcione en el sistema
  operativo. Sin uno, el módulo "multiprocessing.synchronize" se
  desactivará, y los intentos de importarlo darán como resultado
  "ImportError". Consulte bpo-3770 para información adicional.

### Objetos compartidos "ctypes"

Es posible crear objetos compartidos utilizando memoria compartida que
puede ser heredada por procesos secundarios.

multiprocessing.Value(typecode_or_type, *args, lock=True)

   Retorna un objeto "ctypes" asignado desde la memoria compartida.
   Por defecto, el valor de retorno es en realidad un contenedor
   sincronizado para el objeto. Se puede acceder al objeto en sí a
   través del atributo *value* de la "Value".

   *typecode_or_type* determina el tipo del objeto retornado: es un
   tipo *ctypes* o un código de tipo de un carácter del tipo utilizado
   por el módulo "array". **args* se pasa al constructor para el tipo.

   Si *lock* es "True" (el valor predeterminado), se crea un nuevo
   objeto de candado recursivo para sincronizar el acceso al valor. Si
   *lock* es un objeto "Lock" o "RLock", se usará para sincronizar el
   acceso al valor. Si *lock* es "False", entonces el acceso al objeto
   retornado no estará protegido automáticamente por un candado, por
   lo que no será necesariamente "proceso-seguro".

   Operaciones como "+=" que implican una lectura y escritura no son
   atómicas. Entonces, si, por ejemplo, desea incrementar atómicamente
   un valor compartido, es insuficiente simplemente hacer:

      counter.value += 1

   Suponiendo que el candado asociado es recursivo (que es por
   defecto), puede hacer

      with counter.get_lock():
          counter.value += 1

   Véase que *lock* es un argumento de solo una palabra clave.

multiprocessing.Array(typecode_or_type, size_or_initializer, *, lock=True)

   Retorna una matriz *ctypes* asignada desde la memoria compartida.
   Por defecto, el valor de retorno es en realidad un contenedor
   sincronizado para el arreglo.

   *typecode_or_type* determines the type of the elements of the
   returned array: it is either a ctypes type or a one character
   typecode of the kind used by the "array" module with the exception
   of "'w'", which is not supported.  In addition, the "'c'" typecode
   is an alias for "ctypes.c_char".  If *size_or_initializer* is an
   integer, then it determines the length of the array, and the array
   will be initially zeroed. Otherwise, *size_or_initializer* is a
   sequence which is used to initialize the array and whose length
   determines the length of the array.

   Si *lock* es "True" (el valor predeterminado), se crea un nuevo
   objeto de bloqueo para sincronizar el acceso al valor. Si *lock* es
   un objeto "Lock" o "RLock", se usará para sincronizar el acceso al
   valor. Si *lock* es "False", entonces el acceso al objeto retornado
   no estará protegido automáticamente por un candado, por lo que no
   será necesariamente "proceso seguro".

   Véase que *lock* es un argumento de solo una palabra clave.

   Note that an array of "ctypes.c_char" has *value* and *raw*
   attributes which can both be used to store and retrieve byte
   strings. While *raw* allows interaction with a "bytes" object the
   full size of the array, reading *value* will terminate after a null
   byte, like most programming languages handle strings.

#### The "multiprocessing.sharedctypes" module

The "multiprocessing.sharedctypes" module provides functions for
allocating "ctypes" objects from shared memory which can be inherited
by child processes.

Nota:

  Aunque es posible almacenar un puntero en la memoria compartida,
  recuerde que esto se referirá a una ubicación en el espacio de
  direcciones de un proceso específico. Sin embargo, es muy probable
  que el puntero sea inválido en el contexto de un segundo proceso y
  tratar de desreferenciar el puntero del segundo proceso puede causar
  un bloqueo.

multiprocessing.sharedctypes.RawArray(typecode_or_type, size_or_initializer)

   Retorna una matriz *ctypes* asignada desde la memoria compartida.

   *typecode_or_type* determina el tipo de los elementos de la matriz
   retornada: es un tipo de tipo *ctypes* o un código de tipo de un
   carácter del tipo utilizado por el módulo "array". Si
   *size_or_initializer* es un entero, entonces determina la longitud
   de la matriz, y la matriz se pondrá a cero inicialmente. De lo
   contrario, *size_or_initializer* es una secuencia que se usa para
   inicializar la matriz y cuya longitud determina la longitud del
   arreglo.

   Tenga en cuenta que configurar y obtener un elemento es
   potencialmente no atómico -- utiliza "Array()" en su lugar para
   asegurarse de que el acceso se sincronice automáticamente mediante
   un candado.

multiprocessing.sharedctypes.RawValue(typecode_or_type, *args)

   Retorna un objeto *ctypes* asignado desde la memoria compartida.

   *typecode_or_type* determina el tipo del objeto retornado: es un
   tipo *ctypes* o un código de tipo de un carácter del tipo utilizado
   por el módulo "array". **args* se pasa al constructor para el tipo.

   Tenga en cuenta que configurar y obtener el valor es potencialmente
   no atómico -- use "Value()" en su lugar para asegurarse de que el
   acceso se sincronice automáticamente mediante un candado.

   Tenga en cuenta que una matriz de "ctypes.c_char" tiene atributos
   "value" y "raw" que le permiten a uno usarlo para almacenar y
   recuperar cadenas de caracteres -- consulte la documentación para
   "ctypes".

multiprocessing.sharedctypes.Array(typecode_or_type, size_or_initializer, *, lock=True, ctx=None)

   Lo mismo que "RawArray()", excepto que, dependiendo del valor de
   *lock*, se puede retornar un contenedor de sincronización seguro
   para el proceso en lugar de un arreglo de tipos crudos.

   Si *lock* es "True" (el valor predeterminado), se crea un nuevo
   objeto candado para sincronizar el acceso al valor. Si *lock* es un
   objeto "Lock" o "RLock", se utilizará para sincronizar el acceso al
   valor. Si *lock* es "False", entonces el acceso al objeto retornado
   no estará protegido automáticamente por un candado, por lo que no
   será necesariamente "seguro para el proceso".

   *ctx* is a context object, or "None" (use the current context). If
   "None", calling this may set the global start method. See Global
   start method for more details.

   Note that *lock* and *ctx* are keyword-only parameters.

multiprocessing.sharedctypes.Value(typecode_or_type, *args, lock=True, ctx=None)

   Lo mismo que "RawValue()" excepto que, dependiendo del valor de
   *lock*, se puede retornar una envoltura de sincronización segura
   para el proceso en lugar de un objeto *ctypes* sin procesar.

   Si *lock* es "True" (el valor predeterminado), se crea un nuevo
   objeto candado para sincronizar el acceso al valor. Si *lock* es un
   objeto "Lock" o "RLock", se utilizará para sincronizar el acceso al
   valor. Si *lock* es "False", entonces el acceso al objeto retornado
   no estará protegido automáticamente por un candado, por lo que no
   será necesariamente "seguro para el proceso".

   *ctx* is a context object, or "None" (use the current context). If
   "None", calling this may set the global start method. See Global
   start method for more details.

   Note that *lock* and *ctx* are keyword-only parameters.

multiprocessing.sharedctypes.copy(obj)

   Retorna un objeto *ctypes* asignado de la memoria compartida, que
   es una copia del objeto *ctypes* *obj*.

multiprocessing.sharedctypes.synchronized(obj, lock=None, ctx=None)

   Retorna un objeto contenedor seguro para un objeto *ctypes* que usa
   *lock* para sincronizar el acceso. Si *lock* es "None" (el valor
   predeterminado), se crea automáticamente un objeto
   "multiprocessing.RLock".

   *ctx* is a context object, or "None" (use the current context). If
   "None", calling this may set the global start method. See Global
   start method for more details.

   Un contenedor sincronizado tendrá dos métodos además de los del
   objeto que envuelve: "get_obj()" retorna el objeto envuelto y
   "get_lock()" retorna el objeto de bloqueo utilizado para la
   sincronización.

   Tenga en cuenta que acceder al objeto *ctypes* a través del
   contenedor puede ser mucho más lento que acceder al objeto *ctypes*
   sin formato.

   Distinto en la versión 3.5: Los objetos sincronizados admiten el
   protocolo: *context manager*.

La siguiente tabla compara la sintaxis para crear objetos *ctypes*
compartidos desde la memoria compartida con la sintaxis *ctypes*
normal. (En la tabla "MyStruct" hay alguna subclase de
"ctypes.Structure".)

+----------------------+----------------------------+-----------------------------+
| *ctypes*             | *sharedctypes* usando      | *sharedctypes* usando       |
|                      | *type*                     | *typecode*                  |
|======================|============================|=============================|
## | *c_double(2.4)*      | *RawValue(c_double, 2.4)*  | *RawValue('d', 2.4)*        |

## | *MyStruct(4, 6)*     | *RawValue(MyStruct, 4, 6)* |                             |

## | *(c_short * 7)()*    | *RawArray(c_short, 7)*     | *RawArray(‘h’, 7)*          |

| *(c_int * 3)(9, 2,   | *RawArray(c_int, (9, 2,    | *RawArray('i', (9, 2, 8))*  |
## | 8)*                  | 8))*                       |                             |

A continuación se muestra un ejemplo donde un número de objetos
*ctypes* son modificados por un proceso hijo:

   from multiprocessing import Process, Lock
   from multiprocessing.sharedctypes import Value, Array
   from ctypes import Structure, c_double

   class Point(Structure):
       _fields_ = [('x', c_double), ('y', c_double)]

   def modify(n, x, s, A):
       n.value **= 2
       x.value **= 2
       s.value = s.value.upper()
       for a in A:
           a.x **= 2
           a.y **= 2

   if __name__ == '__main__':
       lock = Lock()

       n = Value('i', 7)
       x = Value(c_double, 1.0/3.0, lock=False)
       s = Array('c', b'hello world', lock=lock)
       A = Array(Point, [(1.875,-6.25), (-5.75,2.0), (2.375,9.5)], lock=lock)

       p = Process(target=modify, args=(n, x, s, A))
       p.start()
       p.join()

       print(n.value)
       print(x.value)
       print(s.value)
       print([(a.x, a.y) for a in A])

Los resultados impresos son

   49
   0.1111111111111111
   HELLO WORLD
   [(3.515625, 39.0625), (33.0625, 4.0), (5.640625, 90.25)]

### Administradores (*Managers*)

Los administradores (*managers*) proporcionan una forma de crear datos
que se pueden compartir entre diferentes procesos, incluido el
intercambio en una red entre procesos que se ejecutan en diferentes
máquinas. Un objeto administrador controla un proceso de servidor que
gestiona *shared objects* (*objetos compartidos*). Otros procesos
pueden acceder a los objetos compartidos mediante el uso de servidores
proxy.

multiprocessing.Manager()

   Retorna un objeto iniciado "SyncManager" que se puede usar para
   compartir objetos entre procesos. El objeto administrador retornado
   corresponde a un proceso hijo generado y tiene métodos que crearán
   objetos compartidos y retornarán los proxies correspondientes.

Los procesos del administrador se cerrarán tan pronto como se
recolecte la basura o salga su proceso padre. Las clases de
administrador se definen en el módulo "multiprocessing.managers":

class multiprocessing.managers.BaseManager(address=None, authkey=None, serializer='pickle', ctx=None, *, shutdown_timeout=1.0)

   Crear un objeto *BaseManager*.

   Una vez creado, debe llamar a "start()" o
   "get_server().serve_forever()" para asegurarse de que el objeto de
   administrador se refiera a un proceso de administrador iniciado.

   *address* es la dirección en la que el proceso del administrador
   escucha las nuevas conexiones. Si *address* es "None", se elige una
   arbitrariamente.

   *authkey* es la clave de autenticación que se utilizará para
   verificar la validez de las conexiones entrantes al proceso del
   servidor. Si *authkey* es "None", entonces se usa
   "current_process().authkey". De lo contrario, se usa *authkey* y
   debe ser una cadena de *bytes*.

   *serializer* debe ser "'pickle'" (usar serialización "pickle") o
   "'xmlrpclib'" (usar serialización "xmlrpc.client").

   *ctx* is a context object, or "None" (use the current context). If
   "None", calling this may set the global start method. See Global
   start method for more details.

   *shutdown_timeout* es un tiempo de espera en segundos que se
   utiliza para esperar hasta que el proceso utilizado por el
   administrador se complete en el método "shutdown()". Si se agota el
   tiempo de apagado, el proceso finaliza. Si la finalización del
   proceso también supera el tiempo de espera, el proceso se cancela.

   Distinto en la versión 3.11: Se agregó el parámetro
   *shutdown_timeout*.

   start([initializer[, initargs]])

      Se inicia un subproceso para iniciar el administrador. Si
      *initializer* no es "None", entonces el subproceso llamará
      "initializer(*initargs)" cuando se inicie.

   get_server()

      Retorna un objeto "Server" que representa el servidor real bajo
      el control del Administrador. El objeto "Server" admite el
      método "serve_forever()":

         >>> from multiprocessing.managers import BaseManager
         >>> manager = BaseManager(address=('', 50000), authkey=b'abc')
         >>> server = manager.get_server()
         >>> server.serve_forever()

      "Server" tiene un atributo adicional "address".

   connect()

      Conecta un objeto de administrador (*manager*) local a un
      proceso de administrador remoto:

         >>> from multiprocessing.managers import BaseManager
         >>> m = BaseManager(address=('127.0.0.1', 50000), authkey=b'abc')
         >>> m.connect()

   shutdown()

      Detiene el proceso utilizado por el gerente (*manager*). Esto
      solo está disponible si "start()" se ha utilizado para iniciar
      el proceso del servidor.

      Esto se puede llamar múltiples veces.

   register(typeid[, callable[, proxytype[, exposed[, method_to_typeid[, create_method]]]]])

      Un método de clase que puede usarse para registrar un tipo o
      invocarse con la clase de administrador (*manager*).

      *typeid* es un "identificador de tipo" que se utiliza para
      identificar un tipo particular de objeto compartido. Esto debe
      ser una cadena de caracteres.

      *callable* es un invocable utilizado para crear objetos para
      este identificador de tipo. Si una instancia de administrador se
      conectará al servidor utilizando el método "connect()", o si el
      argumento *create_method* es "False", esto se puede dejar como
      "None".

      *proxytype* es una subclase de "BaseProxy" que se usa para crear
      *proxies* para objetos compartidos con este *typeid*. Si "None",
      se crea automáticamente una clase proxy.

      Se utiliza *exposed* para especificar una secuencia de nombres
      de métodos a los que se debe permitir el acceso de los
      servidores proxy para este tipo de identificación utilizando
      "BaseProxy._callmethod()". (Si *exposed* es "None", entonces
      "proxytype._exposed_" se usa en su lugar si existe). En el caso
      de que no se especifique una lista expuesta, todos los "métodos
      públicos" del objeto compartido serán accesibles . (Aquí un
      "método público" significa cualquier atributo que tenga un
      método "__call__()" y cuyo nombre no comience con "'_'".)

      El *method_to_typeid* es una asignación utilizada para
      especificar el tipo de retorno de los métodos expuestos que
      deberían retornar un proxy. Asigna nombres de métodos a cadenas
      *typeid*. (Si *method_to_typeid* es "None" entonces
      "proxytype._method_to_typeid" se usa en su lugar si existe). Si
      el nombre de un método no es una clave de esta asignación o si
      la asignación es "None" entonces el objeto retornado por el
      método se copiará por valor.

      *create_method* determina si un método debe crearse con el
      nombre *typeid* que se puede usar para indicarle al proceso del
      servidor que cree un nuevo objeto compartido y retornando un
      proxy para él. Por defecto es "True".

   "BaseManager" las instancias también tienen una propiedad de solo
   lectura:

   address

      La dirección utilizada por el administrador.

   Distinto en la versión 3.3: Los objetos de administrador admiten el
   protocolo de gestión de contexto; consulte Tipos gestores de
   contexto. "__enter__()" inicia el proceso del servidor (si aún no
   se ha iniciado) y luego retorna el objeto de administrador.
   "__exit__()" llama "shutdown()".En versiones anteriores
   "__enter__()" no iniciaba el proceso del servidor del administrador
   si aún no se había iniciado.

class multiprocessing.managers.SyncManager

   Una subclase de "BaseManager" que se puede utilizar para la
   sincronización de procesos. Los objetos de este tipo son retornados
   por "multiprocessing.Manager()".

   Sus métodos crean y retornan Objetos Proxy (Proxy Objects) para
   varios tipos de datos de uso común que se sincronizarán entre
   procesos. Esto incluye notablemente listas compartidas y
   diccionarios.

   Barrier(parties[, action[, timeout]])

      "threading.Barrier" crea un objeto compartido y retorna un proxy
      para él.

      Added in version 3.3.

   BoundedSemaphore([value])

      Crea un objeto compartido "threading.BoundedSemaphore" y retorna
      un proxy para él.

   Condition([lock])

      Crea un objeto compartido "threading.Condition" y retorna un
      proxy para él.

      Si se proporciona *lock*, debería ser un proxy para un objeto
      "threading.Lock" o "threading.RLock".

      Distinto en la versión 3.3: El método "wait_for()" fue a
      añadido.

   Event()

      Crea un objeto compartido "threading.Event" y retorna un proxy
      para él.

   Lock()

      Crea un objeto compartido "threading.Lock" y retorna un proxy
      para él.

   Namespace()

      Crea un objeto compartido "Namespace" y retorna un proxy para
      él.

   Queue([maxsize])

      Crea un objeto compartido "queue.Queue" y retorna un proxy para
      él.

   RLock()

      Crea un objeto compartido "threading.RLock" y retorna un proxy
      para él.

   Semaphore([value])

      Crea un objeto compartido "threading.Semaphore" y retorna un
      proxy para él.

   Array(typecode, sequence)

      Crea un arreglo y retorna un proxy para ello.

   Value(typecode, value)

      Crea un objeto con un atributo de escritura "value" y retorna un
      proxy para él.

   dict()
   dict(mapping)
   dict(sequence)

      Crea un objeto compartido "dict" y retorna un proxy para él.

   list()
   list(sequence)

      Crea un objeto compartido "list" y retorna un proxy para él.

   set()
   set(sequence)
   set(mapping)

      Create a shared "set" object and return a proxy for it.

      Added in version 3.14: "set" support was added.

   Distinto en la versión 3.6: Los objetos compartidos pueden
   anidarse. Por ejemplo, un objeto contenedor compartido, como una
   lista compartida, puede contener otros objetos compartidos que
   serán administrados y sincronizados por "SyncManager".

class multiprocessing.managers.Namespace

   Un tipo que puede registrarse con "SyncManager".

   Un objeto de espacio de nombres no tiene métodos públicos, pero
   tiene atributos de escritura. Su representación muestra los valores
   de sus atributos.

   Sin embargo, cuando se usa un proxy para un objeto de espacio de
   nombres, un atributo que comience con "'_'" será un atributo del
   proxy y no un atributo del referente:

      >>> mp_context = multiprocessing.get_context('spawn')
      >>> manager = mp_context.Manager()
      >>> Global = manager.Namespace()
      >>> Global.x = 10
      >>> Global.y = 'hello'
      >>> Global._z = 12.3    # this is an attribute of the proxy
      >>> print(Global)
      Namespace(x=10, y='hello')

#### Administradores customizables (*Customized managers*)

Para crear su propio administrador, uno crea una subclase de
"BaseManager" y utiliza el método de clase "register()" para registrar
nuevos tipos o llamadas con la clase de administrador. Por ejemplo:

   from multiprocessing.managers import BaseManager

   class MathsClass:
       def add(self, x, y):
           return x + y
       def mul(self, x, y):
           return x * y

   class MyManager(BaseManager):
       pass

   MyManager.register('Maths', MathsClass)

   if __name__ == '__main__':
       with MyManager() as manager:
           maths = manager.Maths()
           print(maths.add(4, 3))         # prints 7
           print(maths.mul(7, 8))         # prints 56

#### Utilizando un administrador remoto

Es posible ejecutar un servidor administrador en una máquina y hacer
que los clientes lo usen desde otras máquinas (suponiendo que los
cortafuegos involucrados lo permitan).

La ejecución de los siguientes comandos crea un servidor para una
única cola compartida a la que los clientes remotos pueden acceder:

   >>> from multiprocessing.managers import BaseManager
   >>> from queue import Queue
   >>> queue = Queue()
   >>> class QueueManager(BaseManager): pass
   >>> QueueManager.register('get_queue', callable=lambda:queue)
   >>> m = QueueManager(address=('', 50000), authkey=b'abracadabra')
   >>> s = m.get_server()
   >>> s.serve_forever()

Un cliente puede tener accesos al servidor de la siguiente manera:

   >>> from multiprocessing.managers import BaseManager
   >>> class QueueManager(BaseManager): pass
   >>> QueueManager.register('get_queue')
   >>> m = QueueManager(address=('foo.bar.org', 50000), authkey=b'abracadabra')
   >>> m.connect()
   >>> queue = m.get_queue()
   >>> queue.put('hello')

Otro cliente puede también usarlo:

   >>> from multiprocessing.managers import BaseManager
   >>> class QueueManager(BaseManager): pass
   >>> QueueManager.register('get_queue')
   >>> m = QueueManager(address=('foo.bar.org', 50000), authkey=b'abracadabra')
   >>> m.connect()
   >>> queue = m.get_queue()
   >>> queue.get()
   'hello'

Los procesos locales también pueden acceder a esa cola (*queue*),
utilizando el código de arriba en el cliente para acceder de forma
remota:

   >>> from multiprocessing import Process, Queue
   >>> from multiprocessing.managers import BaseManager
   >>> class Worker(Process):
   ...     def __init__(self, q):
   ...         self.q = q
   ...         super().__init__()
   ...     def run(self):
   ...         self.q.put('local hello')
   ...
   >>> queue = Queue()
   >>> w = Worker(queue)
   >>> w.start()
   >>> class QueueManager(BaseManager): pass
   ...
   >>> QueueManager.register('get_queue', callable=lambda: queue)
   >>> m = QueueManager(address=('', 50000), authkey=b'abracadabra')
   >>> s = m.get_server()
   >>> s.serve_forever()

### Objetos Proxy (*Proxy Objects*)

Un proxy es un objeto que *se refiere* a un objeto compartido que vive
(presumiblemente) en un proceso diferente. Se dice que el objeto
compartido es el *referente* del proxy. Varios objetos proxy pueden
tener el mismo referente.

Un objeto proxy tiene métodos que invocan los métodos correspondientes
de su referente (aunque no todos los métodos del referente estarán
necesariamente disponibles a través del proxy). De esta manera, un
proxy se puede usar al igual que su referente:

   >>> mp_context = multiprocessing.get_context('spawn')
   >>> manager = mp_context.Manager()
   >>> l = manager.list([i*i for i in range(10)])
   >>> print(l)
   [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
   >>> print(repr(l))
   <ListProxy object, typeid 'list' at 0x...>
   >>> l[4]
   16
   >>> l[2:5]
   [4, 9, 16]

Tenga en cuenta que la aplicación "str()" a un proxy retornará la
representación del referente, mientras que la aplicación "repr()"
retornará la representación del proxy.

Una característica importante de los objetos proxy es que son
seleccionables para que puedan pasarse entre procesos. Como tal, un
referente puede contener Objetos Proxy (Proxy Objects). Esto permite
anidar estas listas administradas, dictados y otros Objetos Proxy
(Proxy Objects):

   >>> a = manager.list()
   >>> b = manager.list()
   >>> a.append(b)         # referent of a now contains referent of b
   >>> print(a, b)
   [<ListProxy object, typeid 'list' at ...>] []
   >>> b.append('hello')
   >>> print(a[0], b)
   ['hello'] ['hello']

Del mismo modo, los proxies *dict* y *list* pueden estar anidados uno
dentro del otro:

   >>> l_outer = manager.list([ manager.dict() for i in range(2) ])
   >>> d_first_inner = l_outer[0]
   >>> d_first_inner['a'] = 1
   >>> d_first_inner['b'] = 2
   >>> l_outer[1]['c'] = 3
   >>> l_outer[1]['z'] = 26
   >>> print(l_outer[0])
   {'a': 1, 'b': 2}
   >>> print(l_outer[1])
   {'c': 3, 'z': 26}

Si los objetos estándar (no proxy) "list" or "dict" están contenidos
en un referente, las modificaciones a esos valores mutables no se
propagarán a través del administrador porque el proxy no tiene forma
de saber cuándo los valores contenidos dentro son modificados. Sin
embargo, almacenar un valor en un proxy de contenedor (que desencadena
un "__setitem__" en el objeto proxy) se propaga a través del
administrador y, por lo tanto, para modificar efectivamente dicho
elemento, uno podría reasignar el valor modificado al proxy de
contenedor:

   # create a list proxy and append a mutable object (a dictionary)
   lproxy = manager.list()
   lproxy.append({})
   # now mutate the dictionary
   d = lproxy[0]
   d['a'] = 1
   d['b'] = 2
   # at this point, the changes to d are not yet synced, but by
   # updating the dictionary, the proxy is notified of the change
   lproxy[0] = d

Este enfoque es quizás menos conveniente que emplear anidado Objetos
Proxy (Proxy Objects) para la mayoría de los casos de uso, pero
también demuestra un nivel de control sobre la sincronización.

Nota:

  The proxy types in "multiprocessing" do nothing to support
  comparisons by value.  So, for instance, we have:

     >>> manager.list([1,2,3]) == [1,2,3]
     False

  En su lugar, se debe usar una copia del referente al hacer
  comparaciones.

class multiprocessing.managers.BaseProxy

   Los objetos proxy son instancias de subclases de "BaseProxy".

   _callmethod(methodname[, args[, kwds]])

      Llama y retorna el resultado de un método del referente del
      proxy.

      Si "proxy" es un proxy cuyo referente es "obj" entonces la
      expresión

         proxy._callmethod(methodname, args, kwds)

      evaluará la expresión

         getattr(obj, methodname)(*args, **kwds)

      en el proceso del administrador.

      El valor retornado será una copia del resultado de la llamada o
      un proxy a un nuevo objeto compartido; consulte la documentación
      del argumento *method_to_typeid* de "BaseManager.register()".

      Si la llamada genera una excepción, entonces se vuelve a generar
      "_callmethod()". Si se genera alguna otra excepción en el
      proceso del administrador, esto se convierte en una excepción
      "RemoteError" y se genera mediante  "_callmethod()".

      Tenga en cuenta en particular que se lanzará una excepción si
      *methodname* no ha sido *exposed*.

      Un ejemplo de uso de "_callmethod()":

         >>> l = manager.list(range(10))
         >>> l._callmethod('__len__')
         10
         >>> l._callmethod('__getitem__', (slice(2, 7),)) # equivalent to l[2:7]
         [2, 3, 4, 5, 6]
         >>> l._callmethod('__getitem__', (20,))          # equivalent to l[20]
         Traceback (most recent call last):
         ...
         IndexError: list index out of range

   _getvalue()

      Retorna una copia del referente.

      Si el referente no se puede deserializar (*unpicklable*), esto
      lanzará una excepción.

   __repr__()

      Retorna una representación de un objeto proxy.

   __str__()

      Retorna una representación del referente.

#### Limpieza (*Cleanup*)

Un objeto proxy utiliza una devolución de llamada (*callback*) de
referencia débil (*weakref*) para que cuando sea recolectado por el
recolector de basura se da de baja del administrador que posee su
referente.

Un objeto compartido se elimina del proceso del administrador cuando
ya no hay ningún proxy que se refiera a él.

### Piscinas de procesos (*Process Pools*)

Se puede crear un grupo de procesos que llevarán a cabo las tareas que
se le presenten con la  "Pool" class.

class multiprocessing.pool.Pool([processes[, initializer[, initargs[, maxtasksperchild[, context]]]]])

   Un objeto de grupo de procesos que controla un grupo de procesos de
   trabajo a los que se pueden enviar trabajos. Admite resultados
   asincrónicos con tiempos de espera y devoluciones de llamada y
   tiene una implementación de mapa paralelo.

   *processes* is the number of worker processes to use.  If
   *processes* is "None" then the number returned by
   "os.process_cpu_count()" is used.

   Si *initializer* no es "None", cada proceso de trabajo llamará
   "initializer(*initargs)" cuando se inicie.

   *maxtasksperchild* es el número de tareas que un proceso de trabajo
   puede completar antes de salir y ser reemplazado por un proceso de
   trabajo nuevo, para permitir que se liberen los recursos no
   utilizados. El valor predeterminado *maxtasksperchild* es "None",
   lo que significa que los procesos de trabajo vivirán tanto tiempo
   como el grupo.

   *context* can be used to specify the context used for starting the
   worker processes.  Usually a pool is created using the function
   "multiprocessing.Pool()" or the "Pool()" method of a context
   object.  In both cases *context* is set appropriately. If "None",
   calling this function will have the side effect of setting the
   current global start method if it has not been set already. See the
   "get_context()" function.

   Tenga en cuenta que los métodos del objeto de grupo solo deben ser
   invocados por el proceso que creó el grupo.

   Advertencia:

     Los objetos "multiprocessing.pool" tienen recursos internos que
     necesitan ser administrados adecuadamente (como cualquier otro
     recurso) utilizando el grupo como administrador de contexto o
     llamando a "close()" y "terminate()" manualmente. De lo
     contrario, el proceso puede demorarse en la finalización.Tenga en
     cuenta que **no es correcto** confiar en el recolector de basura
     para destruir el grupo ya que *CPython* no asegura que se llamará
     al finalizador del grupo (consulte "object.__del__()" para
     obtener más información).

   Distinto en la versión 3.2: Added the *maxtasksperchild* parameter.

   Distinto en la versión 3.4: Added the *context* parameter.

   Distinto en la versión 3.13: *processes* uses
   "os.process_cpu_count()" by default, instead of "os.cpu_count()".

   Nota:

     Worker processes within a "Pool" typically live for the complete
     duration of the Pool's work queue. A frequent pattern found in
     other systems (such as Apache, mod_wsgi, etc) to free resources
     held by workers is to allow a worker within a pool to complete
     only a set amount of work before exiting, being cleaned up and a
     new process spawned to replace the old one. The
     *maxtasksperchild* argument to the "Pool" exposes this ability to
     the end user.

   apply(func[, args[, kwds]])

      Llama a *func* con argumentos *args* y argumentos de palabras
      clave *kwds*. Se bloquea hasta que el resultado esté listo.
      Dados estos bloques, "apply_async()" es más adecuado para
      realizar trabajos en paralelo. Además, *func* solo se ejecuta en
      uno de los trabajadores de piscina.

   apply_async(func[, args[, kwds[, callback[, error_callback]]]])

      Una variante del método "apply()" que retorna un objeto
      "AsyncResult".

      Si se especifica *callback*, debería ser un invocable que acepte
      un único argumento. Cuando el resultado está listo, se le aplica
      *callback*, a menos que la llamada falle, en cuyo caso se aplica
      *error_callback*.

      Si se especifica *error_callback*, debería ser un invocable que
      acepte un único argumento. Si la función de destino falla, se
      llama a *error_callback* con la instancia de excepción.

      Las devoluciones de llamada deben completarse inmediatamente ya
      que de lo contrario el hilo que maneja los resultados se
      bloqueará.

   map(func, iterable[, chunksize])

      Un equivalente paralelo de la función incorporada "map()"
      (aunque solo admite un argumento *iterable*, para varios
      iterables consulte "starmap()"). Bloquea hasta que el resultado
      esté listo.

      Este método corta el iterable en varios trozos que envía al
      grupo de procesos como tareas separadas. El tamaño (aproximado)
      de estos fragmentos se puede especificar estableciendo
      *chunksize* en un entero positivo.

      Tenga en cuenta que puede causar un alto uso de memoria para
      iterables muy largos. Considere usar "imap()" o
      "imap_unordered()" con la opción explícita *chunksize* para una
      mejor eficiencia.

   map_async(func, iterable[, chunksize[, callback[, error_callback]]])

      Una variante del método "map()" que retorna un objeto
      "AsyncResult".

      Si se especifica *callback*, debería ser un invocable que acepte
      un único argumento. Cuando el resultado está listo, se le aplica
      *callback*, a menos que la llamada falle, en cuyo caso se aplica
      *error_callback*.

      Si se especifica *error_callback*, debería ser un invocable que
      acepte un único argumento. Si la función de destino falla, se
      llama a *error_callback* con la instancia de excepción.

      Las devoluciones de llamada deben completarse inmediatamente ya
      que de lo contrario el hilo que maneja los resultados se
      bloqueará.

   imap(func, iterable[, chunksize])

      Una versión más perezosa (*lazier*) de "map()".

      El argumento *chunksize* es el mismo que el utilizado por el
      método "map()". Para iterables muy largos, usar un valor grande
      para *chunksize* puede hacer que el trabajo se complete **much**
      (**mucho**) más rápido que usar el valor predeterminado de "1".

      Además, si *chunksize* es "1", el método "next()" del iterador
      retornado por el método "imap()" tiene un parámetro opcional
      *timeout* :"next (timeout)" lanzará
      "multiprocessing.TimeoutError" si el resultado no puede
      retornarse dentro de *timeout* segundos.

   imap_unordered(func, iterable[, chunksize])

      Lo mismo que "imap()", excepto que el orden de los resultados
      del iterador retornado debe considerarse arbitrario. (Solo
      cuando hay un solo proceso de trabajo se garantiza que el orden
      sea "correcto").

   starmap(func, iterable[, chunksize])

      Como "map()", excepto que se espera que los elementos de
      *iterable* sean iterables que se desempaquetan como argumentos.

      Por lo tanto, un *iterable* de "[(1,2), (3, 4)]" da como
      resultado "[func(1,2), func(3,4)]".

      Added in version 3.3.

   starmap_async(func, iterable[, chunksize[, callback[, error_callback]]])

      Una combinación de "starmap()" y "map_async()" que itera sobre
      *iterable* de iterables y llama a *func* con los iterables
      desempaquetados. Como resultado se retorna un objeto.

      Added in version 3.3.

   close()

      Impide que se envíen más tareas a la piscina (*pool*). Una vez
      que se hayan completado todas las tareas, se cerrarán los
      procesos de trabajo.

   terminate()

      Detiene los procesos de trabajo inmediatamente sin completar el
      trabajo pendiente. Cuando el objeto del grupo es basura
      recolectada "terminate()" se llamará inmediatamente.

   join()

      Espera a que salgan los procesos de trabajo. Se debe llamar
      "close()" o "terminate()" antes de usar "join()".

   Distinto en la versión 3.3: Los objetos de piscina (*pool*) ahora
   admiten el protocolo de administración de contexto; consulte Tipos
   gestores de contexto. "__ enter__()" retorna el objeto de grupo, y
   "__ exit__()" llama "terminate()".

class multiprocessing.pool.AsyncResult

   La clase del resultado retornado por "Pool.apply_async()" y
   "Pool.map_async()".

   get([timeout])

      Retorna el resultado cuando llegue. Si *timeout* no es "None" y
      el resultado no llega dentro de *timeout* segundos, entonces se
      lanza "multiprocessing.TimeoutError". Si la llamada remota
      generó una excepción, esa excepción se volverá a plantear
      mediante "get()".

   wait([timeout])

      Espera hasta que el resultado esté disponible o hasta que pase
      *timeout* segundos.

   ready()

      Retorna si la llamada se ha completado.

   successful()

      Retorna si la llamada se completó sin generar una excepción.
      Lanzará "ValueError" si el resultado no está listo.

      Distinto en la versión 3.7: Si el resultado no está listo
      "ValueError" aparece en lugar de "AssertionError".

El siguiente ejemplo demuestra el uso de una piscina(*pool*):

   from multiprocessing import Pool
   import time

   def f(x):
       return x*x

   if __name__ == '__main__':
       with Pool(processes=4) as pool:         # start 4 worker processes
           result = pool.apply_async(f, (10,)) # evaluate "f(10)" asynchronously in a single process
           print(result.get(timeout=1))        # prints "100" unless your computer is *very* slow

           print(pool.map(f, range(10)))       # prints "[0, 1, 4,..., 81]"

           it = pool.imap(f, range(10))
           print(next(it))                     # prints "0"
           print(next(it))                     # prints "1"
           print(it.next(timeout=1))           # prints "4" unless your computer is *very* slow

           result = pool.apply_async(time.sleep, (10,))
           print(result.get(timeout=1))        # raises multiprocessing.TimeoutError

### Oyentes y clientes (*Listeners and Clients*)

Por lo general, el paso de mensajes entre procesos se realiza mediante
colas o mediante objetos "Connection" retornados por "Pipe()".

However, the "multiprocessing.connection" module allows some extra
flexibility.  It basically gives a high level message oriented API for
dealing with sockets or Windows named pipes.  It also has support for
*digest authentication* using the "hmac" module, and for polling
multiple connections at the same time.

multiprocessing.connection.deliver_challenge(connection, authkey)

   Envía un mensaje generado aleatoriamente al otro extremo de la
   conexión y espera una respuesta.

   Si la respuesta coincide con el resumen del mensaje utilizando
   *authkey* como clave, se envía un mensaje de bienvenida al otro
   extremo de la conexión. De lo contrario se lanza
   "AuthenticationError".

multiprocessing.connection.answer_challenge(connection, authkey)

   Recibe un mensaje, calcula el resumen del mensaje usando *authkey*
   como la clave y luego envía el resumen de vuelta.

   Si no se recibe un mensaje de bienvenida, se lanza
   "AuthenticationError".

multiprocessing.connection.Client(address[, family[, authkey]])

   Se intenta configurar una conexión con el oyente que utiliza la
   dirección *address*, retornando "Connection".

   El tipo de conexión está determinado por el argumento *family*,
   pero esto generalmente se puede omitir ya que generalmente se puede
   inferir del formato de *address*. (Consulte Formatos de dirección
   (Address formats))

   If *authkey* is given and not "None", it should be a byte string
   and will be used as the secret key for an HMAC-based authentication
   challenge. No authentication is done if *authkey* is "None".
   "AuthenticationError" is raised if authentication fails. See Llaves
   de autentificación.

class multiprocessing.connection.Listener([address[, family[, backlog[, authkey]]]])

   Un contenedor para un *socket* vinculado o una tubería (*pipe*) con
   nombre de Windows que está 'escuchando' las conexiones.

   *address* es la dirección que utilizará el *socket* vinculado o la
   conocida tubería (*pipe*) con nombre del objeto de escucha.

   Nota:

     Si se usa una dirección de '0.0.0.0' , la dirección no será un
     punto final conectable en Windows. Si necesita un punto final
     conectable, debe usar '127.0.0.1'.

   *family* es el tipo de socket (o tubería con nombre) a utilizar.
   Esta puede ser una de las cadenas de caracteres "'AF_INET'" (para
   un socket TCP), "' AF_UNIX'" (para un socket de dominio Unix) o
   "'AF_PIPE'" (para una tubería con nombre de Windows) . De estos,
   solo el primero está garantizado para estar disponible. Si *family*
   es "None" , *family* se deduce del formato de *address*. Si
   *address* también es "None" , se elige un valor predeterminado.
   Este valor predeterminado es *family* con la opción más rápida
   disponible. Consulte Formatos de dirección (Address formats). Tenga
   en cuenta que si *family* es "'AF_UNIX'" y la dirección es "None",
   el *socket* se creará en un directorio temporal privado usando
   "tempfile.mkstemp()".

   Si el objeto de escucha utiliza un *socket*, entonces *backlog* (1
   por defecto) se pasa al método "listen()" del *socket* una vez que
   se ha vinculado.

   If *authkey* is given and not "None", it should be a byte string
   and will be used as the secret key for an HMAC-based authentication
   challenge. No authentication is done if *authkey* is "None".
   "AuthenticationError" is raised if authentication fails. See Llaves
   de autentificación.

   accept()

      Acepta una conexión en el *socket* vinculado o canalización con
      nombre del objeto de escucha y retorne un objeto "Connection".
      Si se intenta la autenticación y falla, entonces se lanza una
      "AuthenticationError".

   close()

      Cierra el socket vinculado o la tubería con nombre del objeto de
      escucha. Esto se llama automáticamente cuando el oyente es
      recolectado por el recolector de basura. Sin embargo, es
      aconsejable llamarlo explícitamente.

   Los objetos de escucha tienen las siguientes propiedades de solo
   lectura:

   address

      La dirección que está utilizando el objeto *Listener*.

   last_accepted

      La dirección de donde vino la última conexión aceptada. Si esto
      no está disponible, entonces es "None".

   Distinto en la versión 3.3: Los objetos de escucha ahora admiten el
   protocolo de gestión de contexto -- consulte Tipos gestores de
   contexto. El objeto *lISTENER* retorna "__enter__()", y
   "__exit__()" llama a "close()".

multiprocessing.connection.wait(object_list, timeout=None)

   Espera hasta que un objeto en *object_list* esté listo. Retorna la
   lista de esos objetos en *object_list* que están listos. Si
   *timeout* es flotante, la llamada se bloquea durante como máximo
   tantos segundos. Si *timeout* es "`None", se bloqueará por un
   período ilimitado. Un tiempo de espera negativo es equivalente a un
   tiempo de espera cero.

   For both POSIX and Windows, an object can appear in *object_list*
   if it is

   * un objeto legible de "Connection";

   * un objeto conectado y legible de "socket.socket"; o

   * el atributo "sentinel" de un objeto "Process".

   Un objeto de conexión o *socket* está listo cuando hay datos
   disponibles para leer, o el otro extremo se ha cerrado.

   **POSIX**: "wait(object_list, timeout)" almost equivalent
   "select.select(object_list, [], [], timeout)".  The difference is
   that, if "select.select()" is interrupted by a signal, it can raise
   "OSError" with an error number of "EINTR", whereas "wait()" will
   not.

   **Windows**: An item in *object_list* must either be an integer
   handle which is waitable (according to the definition used by the
   documentation of the Win32 function "WaitForMultipleObjects()") or
   it can be an object with a "fileno()" method which returns a socket
   handle or pipe handle.  (Note that pipe handles and socket handles
   are **not** waitable handles.)

   Added in version 3.3.

**Ejemplos**

El siguiente código de servidor crea un escucha que utiliza "'secret
password'" como clave de autenticación. Luego espera una conexión y
envía algunos datos al cliente:

   from multiprocessing.connection import Listener
   from array import array

   address = ('localhost', 6000)     # family is deduced to be 'AF_INET'

   with Listener(address, authkey=b'secret password') as listener:
       with listener.accept() as conn:
           print('connection accepted from', listener.last_accepted)

           conn.send([2.25, None, 'junk', float])

           conn.send_bytes(b'hello')

           conn.send_bytes(array('i', [42, 1729]))

El siguiente código se conecta al servidor y recibe algunos datos del
servidor:

   from multiprocessing.connection import Client
   from array import array

   address = ('localhost', 6000)

   with Client(address, authkey=b'secret password') as conn:
       print(conn.recv())                  # => [2.25, None, 'junk', float]

       print(conn.recv_bytes())            # => 'hello'

       arr = array('i', [0, 0, 0, 0, 0])
       print(conn.recv_bytes_into(arr))    # => 8
       print(arr)                          # => array('i', [42, 1729, 0, 0, 0])

El siguiente código utiliza "wait()" para esperar mensajes de
múltiples procesos a la vez:

   from multiprocessing import Process, Pipe, current_process
   from multiprocessing.connection import wait

   def foo(w):
       for i in range(10):
           w.send((i, current_process().name))
       w.close()

   if __name__ == '__main__':
       readers = []

       for i in range(4):
           r, w = Pipe(duplex=False)
           readers.append(r)
           p = Process(target=foo, args=(w,))
           p.start()
           # We close the writable end of the pipe now to be sure that
           # p is the only process which owns a handle for it.  This
           # ensures that when p closes its handle for the writable end,
           # wait() will promptly report the readable end as being ready.
           w.close()

       while readers:
           for r in wait(readers):
               try:
                   msg = r.recv()
               except EOFError:
                   readers.remove(r)
               else:
                   print(msg)

#### Formatos de dirección (*Address formats*)

* Una dirección "'AF_INET'" es una tupla de la forma "(hostname,
  port)" donde *hostname* es una cadena de caracteres y *port* es un
  número entero.

* Una dirección "'AF_UNIX'" es una cadena que representa un nombre de
  archivo en el sistema de archivos.

* Una dirección "'AF_PIPE'" es una cadena con el formato
  "r'\\.\pipe\*PipeName*'". Para usar "Client()" para conectarse a una
  tubería con nombre en una computadora remota llamada *ServerName*,
  se debe usar una dirección de la forma
  "r'\\*ServerName*\pipe\*PipeName*'" en cambio.

Tenga en cuenta que cualquier cadena que comience con dos barras
inclinadas invertidas se asume por defecto como una dirección
"'AF_PIPE'" en lugar de una dirección "'AF_UNIX'".

### Llaves de autentificación

Cuando uno usa "Connection.recv", los datos recibidos se desbloquean
automáticamente. Desafortunadamente, la eliminación de datos de una
fuente no confiable es un riesgo de seguridad. Por lo tanto "Listener"
y "Client()" usan el módulo "hmac" para proporcionar autenticación de
resumen.

Una clave de autenticación es una cadena de bytes que se puede
considerar como una contraseña: una vez que se establece una conexión,
ambos extremos exigirán pruebas de que el otro conoce la clave de
autenticación. (Demostrar que ambos extremos están usando la misma
clave **no** implica enviar la clave a través de la conexión).

Si se solicita la autenticación pero no se especifica una clave de
autenticación, se utiliza el valor de retorno de
"current_process().authkey" (consulte "Process" ). Este valor será
heredado automáticamente por cualquier objeto "Process" que crea el
proceso actual. Esto significa que (por defecto) todos los procesos de
un programa multiproceso compartirán una única clave de autenticación
que se puede usar al configurar conexiones entre ellos.

Las claves de autenticación adecuadas también se pueden generar
utilizando "os.urandom()".

This authentication protects "Listener" and "Client()" connections,
which are reachable by address.  It is not applied to the anonymous
pipes created by "Pipe()" or used internally by "Queue".
"multiprocessing" treats all local processes running as the same user
as trusted; on most operating systems such processes can access each
other's pipe file descriptors regardless.  Applications that require
isolation between processes of the same user must arrange it at the
operating-system level -- for example, by running workers under a
different user account or in a sandbox.

### *Logging*

Existe cierto soporte para el registro. Sin embargo, tenga en cuenta
que el paquete "logging" no utiliza candados compartidos de proceso,
por lo que es posible (dependiendo del tipo de controlador) que los
mensajes de diferentes procesos se mezclen.

multiprocessing.get_logger()

   Returns the logger used by "multiprocessing".  If necessary, a new
   one will be created.

   When first created the logger has level "logging.NOTSET" and no
   default handler. Messages sent to this logger will not by default
   propagate to the root logger.

   Tenga en cuenta que en Windows los procesos hijos solo heredarán el
   nivel del registrador del proceso parental -- no se heredará
   ninguna otra personalización del registrador.

multiprocessing.log_to_stderr(level=None)

   Esta función realiza una llamada a "get_logger()" pero además de
   retornar el registrador creado por get_logger, agrega un
   controlador que envía la salida a "sys.stderr" usando el formato
   "'[%(levelname)s/%(processName)s] %(message)s'". Puede modificar
   "levelname" del registrador pasando un argumento "level".

A continuación se muestra una sesión de ejemplo con el registro
activado:

   >>> import multiprocessing, logging
   >>> logger = multiprocessing.log_to_stderr()
   >>> logger.setLevel(logging.INFO)
   >>> logger.warning('doomed')
   [WARNING/MainProcess] doomed
   >>> m = multiprocessing.Manager()
   [INFO/SyncManager-...] child process calling self.run()
   [INFO/SyncManager-...] created temp directory /.../pymp-...
   [INFO/SyncManager-...] manager serving at '/.../listener-...'
   >>> del m
   [INFO/MainProcess] sending shutdown message to manager
   [INFO/SyncManager-...] manager exiting with exitcode 0

Para obtener una tabla completa de niveles de registro, consulte el
módulo "logging".

### The "multiprocessing.dummy" module

"multiprocessing.dummy" replicates the API of "multiprocessing" but is
no more than a wrapper around the "threading" module.

In particular, the "Pool" function provided by "multiprocessing.dummy"
returns an instance of "ThreadPool", which is a subclass of "Pool"
that supports all the same method calls but uses a pool of worker
threads rather than worker processes.

class multiprocessing.pool.ThreadPool([processes[, initializer[, initargs]]])

   Un objeto de *pool* de hebras que controla un *pool* de hebras
   trabajadoras a las cuales se pueden enviar trabajos. La interfaz de
   las instancias de "ThreadPool" son totalmente compatibles con las
   instancias de "Pool", y sus recursos también deben ser debidamente
   administrador, ya sea usando el *pool* como un gestor de contexto,
   o llamando a "close()" y "terminate()" manualmente.

   *processes* is the number of worker threads to use.  If *processes*
   is "None" then the number returned by "os.process_cpu_count()" is
   used.

   Si *initializer* no es "None", cada proceso de trabajo llamará
   "initializer(*initargs)" cuando se inicie.

   A diferencia de "Pool", *maxtasksperchild* and *context* no se
   pueden entregar.

   Nota:

     Un "ThreadPool" comparte la misma interfaz que "Pool", la cual
     está diseñada alrededor de un *pool* de procesos, y precede la
     introducción del módulo "concurrent.futures". Como tal, hereda
     algunas operaciones que no tienen sentido para un *pool* basado
     en hebras, y tiene su propio tipo para representar el estado de
     trabajos asíncronos, "AsyncResult", el cual no es entendido por
     otras librerías.Los usuarios deberían por lo general preferir
     usar "concurrent.futures.ThreadPoolExecutor", el cual tiene una
     interfaz más simple que fue diseñada alrededor de hebras desde un
     principio, y que retorna instancias de
     "concurrent.futures.Future", las que son compatibles con muchas
     más librerías, incluyendo "asyncio".

## Pautas de programación

There are certain guidelines and idioms which should be adhered to
when using "multiprocessing".

### Todos los métodos de inicio

Lo siguiente se aplica a todos los métodos de inicio.

Evita estado compartido

   En la medida de lo posible, se debe tratar de evitar el
   desplazamiento de grandes cantidades de datos entre procesos.

   Probablemente sea mejor seguir usando colas (*queues*) o tuberías
   (*pipes*) para la comunicación entre procesos en lugar de usar las
   primitivas de sincronización de nivel inferior.

Serialización (*picklability*)

   Asegúrese que todos los argumentos de los métodos de *proxies* son
   serializables (*pickable*)

Seguridad de hilos de *proxies*

   No usa un objeto proxy de más de un hilo a menos que lo proteja con
   un candado (*lock*).

   (Nunca hay un problema con diferentes procesos que usan el *mismo*
   proxy.)

Uniéndose a procesos zombies

   On POSIX when a process finishes but has not been joined it becomes
   a zombie. There should never be very many because each time a new
   process starts (or "active_children()" is called) all completed
   processes which have not yet been joined will be joined.  Also
   calling a finished process's "Process.is_alive" will join the
   process.  Even so it is probably good practice to explicitly join
   all the processes that you start.

Mejor heredar que serializar/deserializar (*pickle/unpickle*)

   When using the *spawn* or *forkserver* start methods many types
   from "multiprocessing" need to be picklable so that child processes
   can use them.  However, one should generally avoid sending shared
   objects to other processes using pipes or queues. Instead you
   should arrange the program so that a process which needs access to
   a shared resource created elsewhere can inherit it from an ancestor
   process.

Evita procesos de finalización

   El uso del método "Process.terminate" para detener un proceso puede
   causar que los recursos compartidos (como candados, semáforos,
   tuberías  y colas) que el proceso utiliza actualmente se rompan o
   no disponible para otros procesos.

   Por lo tanto, probablemente sea mejor considerar usar
   "Process.terminate" en procesos que nunca usan recursos
   compartidos.

Unirse a procesos que usan colas

   Tenga en cuenta que un proceso que ha puesto elementos en una cola
   esperará antes de finalizar hasta que todos los elementos
   almacenados en búfer sean alimentados por el hilo "alimentador" a
   la tubería subyacente. (El proceso secundario puede llamar al
   método "Queue.cancel_join_thread" de la cola para evitar este
   comportamiento).

   Esto significa que siempre que use una cola debe asegurarse de que
   todos los elementos que se hayan puesto en la cola se eliminarán
   antes de unirse al proceso. De lo contrario, no puede estar seguro
   de que los procesos que han puesto elementos en la cola
   finalizarán. Recuerde también que los procesos no demoníacos se
   unirán automáticamente.

   Un ejemplo que de bloqueo mutuo (*deadlock*) es el siguiente

      from multiprocessing import Process, Queue

      def f(q):
          q.put('X' * 1000000)

      if __name__ == '__main__':
          queue = Queue()
          p = Process(target=f, args=(queue,))
          p.start()
          p.join()                    # this deadlocks
          obj = queue.get()

   Una solución aquí sería intercambiar las dos últimas líneas (o
   simplemente eliminar la línea "p.join()").

Se pasan recursos explícitamente a procesos hijos

   On POSIX using the *fork* start method, a child process can make
   use of a shared resource created in a parent process using a global
   resource.  However, it is better to pass the object as an argument
   to the constructor for the child process.

   Además de hacer que el código (potencialmente) sea compatible con
   Windows y los otros métodos de inicio, esto también garantiza que
   mientras el proceso secundario siga vivo, el objeto no se
   recolectará en el proceso primario. Esto podría ser importante si
   se libera algún recurso cuando el objeto es basura recolectada en
   el proceso padre.

   Entonces por ejemplo

      from multiprocessing import Process, Lock

      def f():
          ... do something using "lock" ...

      if __name__ == '__main__':
          lock = Lock()
          for i in range(10):
              Process(target=f).start()

   debería ser reescrito como

      from multiprocessing import Process, Lock

      def f(l):
          ... do something using "l" ...

      if __name__ == '__main__':
          lock = Lock()
          for i in range(10):
              Process(target=f, args=(lock,)).start()

Tenga cuidado de reemplazar "sys.stdin" con un *"file like object"*

   "multiprocessing" originally unconditionally called:

      os.close(sys.stdin.fileno())

   en el método "multiprocessing.Process._bootstrap()" --- Esto dio
   lugar a problemas con los procesos en proceso. Esto ha sido
   cambiado a:

      sys.stdin.close()
      sys.stdin = open(os.open(os.devnull, os.O_RDONLY), closefd=False)

   Which solves the fundamental issue of processes colliding with each
   other resulting in a bad file descriptor error, but introduces a
   potential danger to applications which replace "sys.stdin()" with a
   "file-like object" with output buffering.  This danger is that if
   multiple processes call "close()" on this file-like object, it
   could result in the same data being flushed to the object multiple
   times, resulting in corruption.

   Si escribe un objeto similar a un archivo e implementa su propio
   almacenamiento en caché, puede hacer que sea seguro para la
   bifurcación (*fork-safe*) almacenando el pid cada vez que se agrega
   al caché y descartando el caché cuando cambia el pid. Por ejemplo:

      @property
      def cache(self):
          pid = os.getpid()
          if pid != self._pid:
              self._pid = pid
              self._cache = []
          return self._cache

   Para más información, consulte bpo-5155, bpo-5313 y bpo-5331

### Los métodos de inicio *spawn* y *forkserver*

There are a few extra restrictions which don't apply to the *fork*
start method.

Más serialización (*pickability*)

   Ensure that all arguments to "Process" are picklable.  Also, if you
   subclass "Process.__init__", you must make sure that instances will
   be picklable when the "Process.start" method is called.

Variables globales

   Tenga en cuenta que si el código que se ejecuta en un proceso
   secundario intenta acceder a una variable global, entonces el valor
   que ve (si lo hay) puede no ser el mismo que el valor en el proceso
   primario en el momento en que fue llamado "Process.start".

   Sin embargo, las variables globales que son solo constantes de
   nivel de módulo no causan problemas.

Importando de manera segura el módulo principal

   Make sure that the main module can be safely imported by a new
   Python interpreter without causing unintended side effects (such as
   starting a new process).

   Por ejemplo, usando el método de inicio *spawn* o *forkserver*
   ejecutando este módulo fallaría produciendo "RuntimeError":

      from multiprocessing import Process

      def foo():
          print('hello')

      p = Process(target=foo)
      p.start()

   En su lugar, se debe proteger el "punto de entrada" (*"entry
   point"*) del programa utilizando como sigue "if __name__ ==
   '__main__':"

      from multiprocessing import Process, freeze_support, set_start_method

      def foo():
          print('hello')

      if __name__ == '__main__':
          freeze_support()
          set_start_method('spawn')
          p = Process(target=foo)
          p.start()

   (La línea "freeze_support()" puede omitirse si el programa se
   ejecuta normalmente en lugar de congelarse).

   Esto permite que el intérprete de Python recién generado importe de
   forma segura el módulo y luego ejecute la función del módulo
   "foo()".

   Se aplican restricciones similares si se crea un grupo o
   administrador en el módulo principal.

## Ejemplos

Demostración de cómo crear y usar gerentes y proxies personalizados:

   from multiprocessing import freeze_support
   from multiprocessing.managers import BaseManager, BaseProxy
   import operator

   ##

   class Foo:
       def f(self):
           print('you called Foo.f()')
       def g(self):
           print('you called Foo.g()')
       def _h(self):
           print('you called Foo._h()')

   # A simple generator function
   def baz():
       for i in range(10):
           yield i*i

   # Proxy type for generator objects
   class GeneratorProxy(BaseProxy):
       _exposed_ = ['__next__']
       def __iter__(self):
           return self
       def __next__(self):
           return self._callmethod('__next__')

   # Function to return the operator module
   def get_operator_module():
       return operator

   ##

   class MyManager(BaseManager):
       pass

   # register the Foo class; make `f()` and `g()` accessible via proxy
   MyManager.register('Foo1', Foo)

   # register the Foo class; make `g()` and `_h()` accessible via proxy
   MyManager.register('Foo2', Foo, exposed=('g', '_h'))

   # register the generator function baz; use `GeneratorProxy` to make proxies
   MyManager.register('baz', baz, proxytype=GeneratorProxy)

   # register get_operator_module(); make public functions accessible via proxy
   MyManager.register('operator', get_operator_module)

   ##

   def test():
       manager = MyManager()
       manager.start()

       print('-' * 20)

       f1 = manager.Foo1()
       f1.f()
       f1.g()
       assert not hasattr(f1, '_h')
       assert sorted(f1._exposed_) == sorted(['f', 'g'])

       print('-' * 20)

       f2 = manager.Foo2()
       f2.g()
       f2._h()
       assert not hasattr(f2, 'f')
       assert sorted(f2._exposed_) == sorted(['g', '_h'])

       print('-' * 20)

       it = manager.baz()
       for i in it:
           print('<%d>' % i, end=' ')
       print()

       print('-' * 20)

       op = manager.operator()
       print('op.add(23, 45) =', op.add(23, 45))
       print('op.pow(2, 94) =', op.pow(2, 94))
       print('op._exposed_ =', op._exposed_)

   ##

   if __name__ == '__main__':
       freeze_support()
       test()

Usando "Pool":

   import multiprocessing
   import time
   import random
   import sys

   #
   # Functions used by test code
   #

   def calculate(func, args):
       result = func(*args)
       return '%s says that %s%s = %s' % (
           multiprocessing.current_process().name,
           func.__name__, args, result
           )

   def calculatestar(args):
       return calculate(*args)

   def mul(a, b):
       time.sleep(0.5 * random.random())
       return a * b

   def plus(a, b):
       time.sleep(0.5 * random.random())
       return a + b

   def f(x):
       return 1.0 / (x - 5.0)

   def pow3(x):
       return x ** 3

   def noop(x):
       pass

   #
   # Test code
   #

   def test():
       PROCESSES = 4
       print('Creating pool with %d processes\n' % PROCESSES)

       with multiprocessing.Pool(PROCESSES) as pool:
           #
           # Tests
           #

           TASKS = [(mul, (i, 7)) for i in range(10)] + \
                   [(plus, (i, 8)) for i in range(10)]

           results = [pool.apply_async(calculate, t) for t in TASKS]
           imap_it = pool.imap(calculatestar, TASKS)
           imap_unordered_it = pool.imap_unordered(calculatestar, TASKS)

           print('Ordered results using pool.apply_async():')
           for r in results:
               print('\t', r.get())
           print()

           print('Ordered results using pool.imap():')
           for x in imap_it:
               print('\t', x)
           print()

           print('Unordered results using pool.imap_unordered():')
           for x in imap_unordered_it:
               print('\t', x)
           print()

           print('Ordered results using pool.map() --- will block till complete:')
           for x in pool.map(calculatestar, TASKS):
               print('\t', x)
           print()

           #
           # Test error handling
           #

           print('Testing error handling:')

           try:
               print(pool.apply(f, (5,)))
           except ZeroDivisionError:
               print('\tGot ZeroDivisionError as expected from pool.apply()')
           else:
               raise AssertionError('expected ZeroDivisionError')

           try:
               print(pool.map(f, list(range(10))))
           except ZeroDivisionError:
               print('\tGot ZeroDivisionError as expected from pool.map()')
           else:
               raise AssertionError('expected ZeroDivisionError')

           try:
               print(list(pool.imap(f, list(range(10)))))
           except ZeroDivisionError:
               print('\tGot ZeroDivisionError as expected from list(pool.imap())')
           else:
               raise AssertionError('expected ZeroDivisionError')

           it = pool.imap(f, list(range(10)))
           for i in range(10):
               try:
                   x = next(it)
               except ZeroDivisionError:
                   if i == 5:
                       pass
               except StopIteration:
                   break
               else:
                   if i == 5:
                       raise AssertionError('expected ZeroDivisionError')

           assert i == 9
           print('\tGot ZeroDivisionError as expected from IMapIterator.next()')
           print()

           #
           # Testing timeouts
           #

           print('Testing ApplyResult.get() with timeout:', end=' ')
           res = pool.apply_async(calculate, TASKS[0])
           while 1:
               sys.stdout.flush()
               try:
                   sys.stdout.write('\n\t%s' % res.get(0.02))
                   break
               except multiprocessing.TimeoutError:
                   sys.stdout.write('.')
           print()
           print()

           print('Testing IMapIterator.next() with timeout:', end=' ')
           it = pool.imap(calculatestar, TASKS)
           while 1:
               sys.stdout.flush()
               try:
                   sys.stdout.write('\n\t%s' % it.next(0.02))
               except StopIteration:
                   break
               except multiprocessing.TimeoutError:
                   sys.stdout.write('.')
           print()
           print()

   if __name__ == '__main__':
       multiprocessing.freeze_support()
       test()

Un ejemplo que muestra cómo usar las colas para alimentar tareas a una
colección de procesos de trabajo y recopilar los resultados:

   import time
   import random

   from multiprocessing import Process, Queue, current_process, freeze_support

   #
   # Function run by worker processes
   #

   def worker(input, output):
       for func, args in iter(input.get, 'STOP'):
           result = calculate(func, args)
           output.put(result)

   #
   # Function used to calculate result
   #

   def calculate(func, args):
       result = func(*args)
       return '%s says that %s%s = %s' % \
           (current_process().name, func.__name__, args, result)

   #
   # Functions referenced by tasks
   #

   def mul(a, b):
       time.sleep(0.5*random.random())
       return a * b

   def plus(a, b):
       time.sleep(0.5*random.random())
       return a + b

   #
   #
   #

   def test():
       NUMBER_OF_PROCESSES = 4
       TASKS1 = [(mul, (i, 7)) for i in range(20)]
       TASKS2 = [(plus, (i, 8)) for i in range(10)]

       # Create queues
       task_queue = Queue()
       done_queue = Queue()

       # Submit tasks
       for task in TASKS1:
           task_queue.put(task)

       # Start worker processes
       for i in range(NUMBER_OF_PROCESSES):
           Process(target=worker, args=(task_queue, done_queue)).start()

       # Get and print results
       print('Unordered results:')
       for i in range(len(TASKS1)):
           print('\t', done_queue.get())

       # Add more tasks using `put()`
       for task in TASKS2:
           task_queue.put(task)

       # Get and print some more results
       for i in range(len(TASKS2)):
           print('\t', done_queue.get())

       # Tell child processes to stop
       for i in range(NUMBER_OF_PROCESSES):
           task_queue.put('STOP')

   if __name__ == '__main__':
       freeze_support()
       test()
