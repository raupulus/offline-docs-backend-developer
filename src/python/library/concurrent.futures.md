---
title: '"concurrent.futures" --- Launching parallel tasks'
source_url: https://docs.python.org/es/3
source_path: library/concurrent.futures.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2070
---

# "concurrent.futures" --- Launching parallel tasks

Added in version 3.2.

**Source code:** Lib/concurrent/futures/thread.py,
Lib/concurrent/futures/process.py, and
Lib/concurrent/futures/interpreter.py

======================================================================

The "concurrent.futures" module provides a high-level interface for
asynchronously executing callables.

The asynchronous execution can be performed with threads, using
"ThreadPoolExecutor" or "InterpreterPoolExecutor", or separate
processes, using "ProcessPoolExecutor". Each implements the same
interface, which is defined by the abstract "Executor" class.

"concurrent.futures.Future" must not be confused with
"asyncio.Future", which is designed for use with "asyncio" tasks and
coroutines. See the asyncio's Future documentation for a detailed
comparison of the two.

Availability: not WASI.

This module does not work or is not available on WebAssembly. See
Plataformas WebAssembly for more information.

## Objetos ejecutores

class concurrent.futures.Executor

   Una clase abstracta que proporciona métodos para ejecutar llamadas
   de forma asincrónica. No debe ser utilizada directamente, sino a
   través de sus subclases.

   submit(fn, /, *args, **kwargs)

      Programa la invocación de *fn*, que será ejecutada como
      "fn(*args, **kwargs)" y retorna un objeto "Future" que
      representa la ejecución del invocable.

         with ThreadPoolExecutor(max_workers=1) as executor:
             future = executor.submit(pow, 323, 1235)
             print(future.result())

   map(fn, *iterables, timeout=None, chunksize=1, buffersize=None)

      Similar to "map(fn, *iterables)" except:

      * The *iterables* are collected immediately rather than lazily,
        unless a *buffersize* is specified to limit the number of
        submitted tasks whose results have not yet been yielded. If
        the buffer is full, iteration over the *iterables* pauses
        until a result is yielded from the buffer.

      * *fn* is executed asynchronously and several calls to *fn* may
        be made concurrently.

      El iterador retornado lanza "TimeoutError" si "__next__()" es
      llamado y el resultado no está disponible luego de *timeout*
      segundos luego de la llamada original a "Executor.map()".
      *timeout* puede ser un int o un float. Si no se provee un
      *timeout* o es "None", no hay limite de espera.

      If a *fn* call raises an exception, then that exception will be
      raised when its value is retrieved from the iterator.

      When using "ProcessPoolExecutor", this method chops *iterables*
      into a number of chunks which it submits to the pool as separate
      tasks.  The (approximate) size of these chunks can be specified
      by setting *chunksize* to a positive integer.  For very long
      iterables, using a large value for *chunksize* can significantly
      improve performance compared to the default size of 1.  With
      "ThreadPoolExecutor" and "InterpreterPoolExecutor", *chunksize*
      has no effect.

      Distinto en la versión 3.5: Added the *chunksize* parameter.

      Distinto en la versión 3.14: Added the *buffersize* parameter.

   shutdown(wait=True, *, cancel_futures=False)

      Indica al ejecutor que debe liberar todos los recursos que está
      utilizando cuando los futuros actualmente pendientes de
      ejecución finalicen. Las llamadas a "Executor.submit()" y
      "Executor.map()" realizadas después del apagado lanzarán
      "RuntimeError".

      Si *wait* es "True" este método no retornará hasta que todos los
      futuros pendientes hayan terminado su ejecución y los recursos
      asociados al ejecutor hayan sido liberados.  Si *wait* es
      "False", este método retornará de inmediato y los recursos
      asociados al ejecutor se liberarán cuando todos los futuros
      asociados hayan finalizado su ejecución. Independientemente del
      valor de *wait*, el programa Python entero no finalizará hasta
      que todos los futuros pendientes hayan finalizado su ejecución.

      Si *cancel_futures* es "True", este método cancelará todos los
      futuros pendientes que el ejecutor no ha comenzado a ejecutar.
      Los futuros que se completen o estén en ejecución no se
      cancelarán, independientemente del valor de *cancel_futures*.

      Si tanto *cancel_futures* como *wait* son "True", todos los
      futuros que el ejecutor ha comenzado a ejecutar se completarán
      antes de que regrese este método. Los futuros restantes se
      cancelan.

      You can avoid having to call this method explicitly if you use
      the executor as a *context manager* via the  "with" statement,
      which will shutdown the "Executor" (waiting as if
      "Executor.shutdown()" were called with *wait* set to "True"):

         import shutil
         with ThreadPoolExecutor(max_workers=4) as e:
             e.submit(shutil.copy, 'src1.txt', 'dest1.txt')
             e.submit(shutil.copy, 'src2.txt', 'dest2.txt')
             e.submit(shutil.copy, 'src3.txt', 'dest3.txt')
             e.submit(shutil.copy, 'src4.txt', 'dest4.txt')

      Distinto en la versión 3.9: Agregado *cancel_futures*.

## ThreadPoolExecutor

"ThreadPoolExecutor" es una subclase de "Executor" que usa un grupo de
hilos para ejecutar llamadas de forma asincrónica.

Pueden ocurrir bloqueos mutuos cuando la llamada asociada a un
"Future" espera el resultado de otro "Future". Por ejemplo:

   import time
   def wait_on_b():
       time.sleep(5)
       print(b.result())  # b will never complete because it is waiting on a.
       return 5

   def wait_on_a():
       time.sleep(5)
       print(a.result())  # a will never complete because it is waiting on b.
       return 6

   executor = ThreadPoolExecutor(max_workers=2)
   a = executor.submit(wait_on_b)
   b = executor.submit(wait_on_a)

Y:

   def wait_on_future():
       f = executor.submit(pow, 5, 2)
       # This will never complete because there is only one worker thread and
       # it is executing this function.
       print(f.result())

   executor = ThreadPoolExecutor(max_workers=1)
   future = executor.submit(wait_on_future)
   # Note: calling future.result() would also cause a deadlock because
   # the single worker thread is already waiting for wait_on_future().

class concurrent.futures.ThreadPoolExecutor(max_workers=None, thread_name_prefix='', initializer=None, initargs=())

   Subclase de "Executor" que utiliza un grupo de hilos de
   *max_workers* como máximo para ejecutar llamadas de forma
   asincrónica.

   Todos los hilos que se hayan puesto en cola en "ThreadPoolExecutor"
   se unirán antes de que el intérprete pueda salir. Tenga en cuenta
   que el controlador de salida que hace esto se ejecuta *antes* de
   cualquier controlador de salida añadido mediante "atexit". Esto
   significa que las excepciones en el hilo principal deben ser
   capturadas y manejadas para indicar a los hilos que salgan
   correctamente. Por esta razón, se recomienda no utilizar
   "ThreadPoolExecutor" para tareas de larga duración.

   *initializer* es un invocable opcional que es llamado al comienzo
   de cada hilo de trabajo; *initargs* es una tupla de argumentos
   pasados al inicializador.  Si el *initializer* lanza una excepción,
   todos los trabajos actualmente pendientes lanzarán
   "BrokenThreadPool", así como cualquier intento de enviar más
   trabajos al grupo.

   Distinto en la versión 3.5: Si *max_workers* es "None" o no es
   especificado, se tomará por defecto el número de procesadores de la
   máquina, multiplicado por "5", asumiendo que "ThreadPoolExecutor" a
   menudo se utiliza para paralelizar E/S en lugar de trabajo de CPU y
   que el numero de trabajadores debe ser mayor que el número de
   trabajadores para "ProcessPoolExecutor".

   Distinto en la versión 3.6: Added the *thread_name_prefix*
   parameter to allow users to control the "threading.Thread" names
   for worker threads created by the pool for easier debugging.

   Distinto en la versión 3.7: Se agregaron los argumentos
   *initializer* y *initargs*.

   Distinto en la versión 3.8: El valor predeterminado de
   *max_workers* fue reemplazado por "min(32, os.cpu_count() + 4)".
   Este valor predeterminado conserva al menos 5 trabajadores para las
   tareas vinculadas de E/S. Utiliza como máximo 32 núcleos de CPU
   para tareas vinculadas a la CPU que liberan el GIL. Y evita
   utilizar recursos muy grandes implícitamente en máquinas de muchos
   núcleos.ThreadPoolExecutor ahora también reutiliza hilos inactivos
   antes de crear *max_workers* hilos de trabajo.

   Distinto en la versión 3.13: Default value of *max_workers* is
   changed to "min(32, (os.process_cpu_count() or 1) + 4)".

### Ejemplo de ThreadPoolExecutor

   import concurrent.futures
   import urllib.request

   URLS = ['http://www.foxnews.com/',
           'http://www.cnn.com/',
           'http://europe.wsj.com/',
           'http://www.bbc.co.uk/',
           'http://nonexistent-subdomain.python.org/']

   # Retrieve a single page and report the URL and contents
   def load_url(url, timeout):
       with urllib.request.urlopen(url, timeout=timeout) as conn:
           return conn.read()

   # We can use a with statement to ensure threads are cleaned up promptly
   with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
       # Start the load operations and mark each future with its URL
       future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
       for future in concurrent.futures.as_completed(future_to_url):
           url = future_to_url[future]
           try:
               data = future.result()
           except Exception as exc:
               print('%r generated an exception: %s' % (url, exc))
           else:
               print('%r page is %d bytes' % (url, len(data)))

## InterpreterPoolExecutor

Added in version 3.14.

The "InterpreterPoolExecutor" class uses a pool of interpreters to
execute calls asynchronously.  It is a "ThreadPoolExecutor" subclass,
which means each worker is running in its own thread. The difference
here is that each worker has its own interpreter, and runs each task
using that interpreter.

The biggest benefit to using interpreters instead of only threads is
true multi-core parallelism.  Each interpreter has its own *Global
Interpreter Lock*, so code running in one interpreter can run on one
CPU core, while code in another interpreter runs unblocked on a
different core.

The tradeoff is that writing concurrent code for use with multiple
interpreters can take extra effort.  However, this is because it
forces you to be deliberate about how and when interpreters interact,
and to be explicit about what data is shared between interpreters.
This results in several benefits that help balance the extra effort,
including true multi-core parallelism,  For example, code written this
way can make it easier to reason about concurrency.  Another major
benefit is that you don't have to deal with several of the big pain
points of using threads, like race conditions.

Each worker's interpreter is isolated from all the other interpreters.
"Isolated" means each interpreter has its own runtime state and
operates completely independently.  For example, if you redirect
"sys.stdout" in one interpreter, it will not be automatically
redirected to any other interpreter.  If you import a module in one
interpreter, it is not automatically imported in any other.  You would
need to import the module separately in interpreter where you need it.
In fact, each module imported in an interpreter is a completely
separate object from the same module in a different interpreter,
including "sys", "builtins", and even "__main__".

Isolation means a mutable object, or other data, cannot be used by
more than one interpreter at the same time.  That effectively means
interpreters cannot actually share such objects or data.  Instead,
each interpreter must have its own copy, and you will have to
synchronize any changes between the copies manually.  Immutable
objects and data, like the builtin singletons, strings, and tuples of
immutable objects, don't have these limitations.

Communicating and synchronizing between interpreters is most
effectively done using dedicated tools, like those proposed in **PEP
734**.  One less efficient alternative is to serialize with "pickle"
and then send the bytes over a shared "socket" or "pipe".

class concurrent.futures.InterpreterPoolExecutor(max_workers=None, thread_name_prefix='', initializer=None, initargs=())

   A "ThreadPoolExecutor" subclass that executes calls asynchronously
   using a pool of at most *max_workers* threads.  Each thread runs
   tasks in its own interpreter.  The worker interpreters are isolated
   from each other, which means each has its own runtime state and
   that they can't share any mutable objects or other data.  Each
   interpreter has its own *Global Interpreter Lock*, which means code
   run with this executor has true multi-core parallelism.

   The optional *initializer* and *initargs* arguments have the same
   meaning as for "ThreadPoolExecutor": the initializer is run when
   each worker is created, though in this case it is run in the
   worker's interpreter.  The executor serializes the *initializer*
   and *initargs* using "pickle" when sending them to the worker's
   interpreter.

   Nota:

     The executor may replace uncaught exceptions from *initializer*
     with "ExecutionFailed".

   Other caveats from parent "ThreadPoolExecutor" apply here.

"submit()" and "map()" work like normal, except the worker serializes
the callable and arguments using "pickle" when sending them to its
interpreter.  The worker likewise serializes the return value when
sending it back.

When a worker's current task raises an uncaught exception, the worker
always tries to preserve the exception as-is.  If that is successful
then it also sets the "__cause__" to a corresponding "ExecutionFailed"
instance, which contains a summary of the original exception. In the
uncommon case that the worker is not able to preserve the original as-
is then it directly preserves the corresponding "ExecutionFailed"
instance instead.

## ProcessPoolExecutor

La clase "ProcessPoolExecutor" es una subclase "Executor" que usa un
grupo de procesos para ejecutar llamadas de forma asíncrona.
"ProcessPoolExecutor" usa el módulo "multiprocessing", que le permite
eludir el *Global Interpreter Lock* pero también significa que solo
los objetos seleccionables pueden ser ejecutados y retornados.

El módulo "__main__" debe ser importable por los subprocesos
trabajadores. Esto significa que "ProcessPoolExecutor" no funcionará
en el intérprete interactivo.

Llamar a métodos de "Executor" o "Future" desde el invocable enviado a
"ProcessPoolExecutor" resultará en bloqueos mutuos.

Note that the restrictions on functions and arguments needing to
picklable as per "multiprocessing.Process" apply when using "submit()"
and "map()" on a "ProcessPoolExecutor". A function defined in a REPL
or a lambda should not be expected to work.

class concurrent.futures.ProcessPoolExecutor(max_workers=None, mp_context=None, initializer=None, initargs=(), max_tasks_per_child=None)

   An "Executor" subclass that executes calls asynchronously using a
   pool of at most *max_workers* processes.  If *max_workers* is
   "None" or not given, it will default to "os.process_cpu_count()".
   If *max_workers* is less than or equal to "0", then a "ValueError"
   will be raised. On Windows, *max_workers* must be less than or
   equal to "61". If it is not then "ValueError" will be raised. If
   *max_workers* is "None", then the default chosen will be at most
   "61", even if more processors are available. *mp_context* can be a
   "multiprocessing" context or "None". It will be used to launch the
   workers. If *mp_context* is "None" or not given, the default
   "multiprocessing" context is used. See Contextos y métodos de
   inicio.

   *initializer* es un invocable opcional que es llamado al comienzo
   de cada proceso trabajador; *initargs* es una tupla de argumentos
   pasados al inicializador. Si el *initializer* lanza una excepción,
   todos los trabajos actualmente pendientes lanzarán
   "BrokenProcessPool", así como cualquier intento de enviar más
   trabajos al grupo.

   *max_tasks_per_child* es un argumento opcional que especifica el
   número máximo de tareas que un único proceso puede ejecutar antes
   de salir y ser reemplazado por un nuevo proceso de trabajo. Por
   defecto, *max_tasks_per_child* es "None", lo que significa que los
   procesos de trabajo vivirán tanto como el pool. Cuando se
   especifica un máximo, el método de inicio de multiprocesamiento
   "spawn" se utilizará por defecto en ausencia de un parámetro
   *mp_context*. Esta característica es incompatible con el método de
   inicio "fork".

   Distinto en la versión 3.3: When one of the worker processes
   terminates abruptly, a "BrokenProcessPool" error is now raised.
   Previously, behaviour was undefined but operations on the executor
   or its futures would often freeze or deadlock.

   Distinto en la versión 3.7: El argumento *mp_context* se agregó
   para permitir a los usuarios controlar el método de iniciación para
   procesos de trabajo creados en el grupo.Se agregaron los argumentos
   *initializer* y *initargs*.

   Distinto en la versión 3.11: El argumento *max_tasks_per_child* se
   agregó para permitir a los usuarios controlar el tiempo de vida
   para procesos de trabajo creados en el grupo.

   Distinto en la versión 3.12: En sistemas POSIX, si su aplicación
   tiene múltiples hilos y el contexto "multiprocessing" utiliza el
   método de inicio ""fork"": La función "os.fork()" llamada
   internamente para generar trabajadores puede lanzar un mensaje
   "DeprecationWarning". Pase un *mp_context* configurado para
   utilizar un método de inicio diferente. Consulte la documentación
   de "os.fork()" para más información.

   Distinto en la versión 3.13: *max_workers* uses
   "os.process_cpu_count()" by default, instead of "os.cpu_count()".

   Distinto en la versión 3.14: The default process start method (see
   Contextos y métodos de inicio) changed away from *fork*. If you
   require the *fork* start method for "ProcessPoolExecutor" you must
   explicitly pass "mp_context=multiprocessing.get_context("fork")".

   Distinto en la versión 3.14.6 (unreleased): Fixed a deadlock
   (gh-115634) where the executor could hang after a worker process
   exited upon reaching its *max_tasks_per_child* limit while tasks
   remained queued.

   terminate_workers()

      Attempt to terminate all living worker processes immediately by
      calling "Process.terminate" on each of them. Internally, it will
      also call "Executor.shutdown()" to ensure that all other
      resources associated with the executor are freed.

      After calling this method the caller should no longer submit
      tasks to the executor.

      Added in version 3.14.

   kill_workers()

      Attempt to kill all living worker processes immediately by
      calling "Process.kill" on each of them. Internally, it will also
      call "Executor.shutdown()" to ensure that all other resources
      associated with the executor are freed.

      After calling this method the caller should no longer submit
      tasks to the executor.

      Added in version 3.14.

### Ejemplo de *ProcessPoolExecutor*

   import concurrent.futures
   import math

   PRIMES = [
       112272535095293,
       112582705942171,
       112272535095293,
       115280095190773,
       115797848077099,
       1099726899285419]

   def is_prime(n):
       if n < 2:
           return False
       if n == 2:
           return True
       if n % 2 == 0:
           return False

       sqrt_n = int(math.floor(math.sqrt(n)))
       for i in range(3, sqrt_n + 1, 2):
           if n % i == 0:
               return False
       return True

   def main():
       with concurrent.futures.ProcessPoolExecutor() as executor:
           for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
               print('%d is prime: %s' % (number, prime))

   if __name__ == '__main__':
       main()

## Objetos futuro

La clase "Future" encapsula la ejecución asincrónica del invocable.
Las instancias de "Future" son creadas por "Executor.submit()".

class concurrent.futures.Future

   Encapsula la ejecución asincrónica del invocable. Las instancias de
   "Future" son creadas por "Executor.submit()" y no deberían ser
   creadas directamente, excepto para pruebas.

   cancel()

      Intenta cancelar la llamada.  Si el invocable está siendo
      ejecutado o ha finalizado su ejecución y no puede ser cancelado
      el método retornará "False", de lo contrario la llamada será
      cancelada y el método retornará "True".

   cancelled()

      Retorna "True" si la llamada fue cancelada exitosamente.

   running()

      Retorna "True" si la llamada está siendo ejecutada y no puede
      ser cancelada.

   done()

      Retorna "True" si la llamada fue cancelada exitosamente o
      terminó su ejecución.

   result(timeout=None)

      Retorna el valor retornado por la llamada. Si la llamada aún no
      se ha completado, este método esperará hasta *timeout* segundos.
      Si la llamada no se ha completado en *timeout* segundos,
      entonces se lanzará un "TimeoutError". *timeout* puede ser un
      int o un float. Si *timeout* no se especifica o es "None", no
      hay límite para el tiempo de espera.

      Si el futuro es cancelado antes de finalizar su ejecución,
      "CancelledError" será lanzada.

      Si la llamada lanzó una excepción, este método lanzará la misma
      excepción.

   exception(timeout=None)

      Retorna la excepción lanzada por la llamada. Si la llamada aún
      no se ha completado, este método esperará hasta *timeout*
      segundos. Si la llamada no se ha completado en *timeout*
      segundos, entonces se lanzará un "TimeoutError". *timeout* puede
      ser un int o un float. Si *timeout* no se especifica o es
      "None", no hay límite para el tiempo de espera.

      Si el futuro es cancelado antes de finalizar su ejecución,
      "CancelledError" será lanzada.

      Si la llamada es completada sin excepciones, se retornará
      "`None".

   add_done_callback(fn)

      Asocia el invocable *fn* al futuro. *fn* va a ser llamada, con
      el futuro como su único argumento, cuando el futuro sea
      cancelado o finalice su ejecución.

      Los invocables agregados se llaman en el orden en que se
      agregaron y siempre se llaman en un hilo que pertenece al
      proceso que los agregó. Si el invocable genera una subclase
      "Exception", se registrará y se ignorará. Si el invocable genera
      una subclase "BaseException", el comportamiento no está
      definido.

      Si el futuro ya ha finalizado su ejecución o fue cancelado, *fn*
      retornará inmediatamente.

   Los siguientes métodos de "Future" están pensados para ser usados
   en pruebas unitarias e implementaciones de "Executor".

   set_running_or_notify_cancel()

      Este método sólo debe ser llamado en implementaciones de
      "Executor" antes de ejecutar el trabajo asociado al "Future" y
      por las pruebas unitarias.

      Si el método retorna "False" entonces el "Future" fue cancelado,
      es decir, "Future.cancel()" fue llamado y retornó "True".
      Cualquier hilo que esté esperando a que el "Future" se complete
      (es decir, a través de "as_completed()" o "wait()") será
      despertado.

      Si el método retorna "True" entonces el "Future" no se ha
      cancelado y se ha puesto en estado de ejecución, es decir, las
      llamadas a "Future.running`()" retornarán "True".

      Este método solo puede ser llamado una sola vez y no puede ser
      llamado luego de haber llamado a "Future.set_result()" o a
      "Future.set_exception()".

   set_result(result)

      Establece *result* como el resultado del trabajo asociado al
      "Future".

      Este método solo debe ser usado por implementaciones de
      "Executor" y pruebas unitarias.

      Distinto en la versión 3.8: Este método lanza
      "concurrent.futures.InvalidStateError" si "Future" ya ha
      finalizado su ejecución.

   set_exception(exception)

      Establece *exception*, subclase de "Exception", como el
      resultado del trabajo asociado al "Future".

      Este método solo debe ser usado por implementaciones de
      "Executor" y pruebas unitarias.

      Distinto en la versión 3.8: Este método lanza
      "concurrent.futures.InvalidStateError" si "Future" ya ha
      finalizado su ejecución.

## Funciones del módulo

concurrent.futures.wait(fs, timeout=None, return_when=ALL_COMPLETED)

   Espera a que se completen las instancias "Future" (posiblemente
   creadas por diferentes instancias "Executor") dadas por *fs*. Los
   futuros duplicados dados a *fs* se eliminan y sólo se devolverán
   una vez. Retorna una tupla nombrada de 2 conjuntos. El primer
   conjunto, llamado "done", contiene los futuros que se han
   completado (futuros finalizados o cancelados) antes de que se
   complete la espera. El segundo conjunto, llamado "not_done",
   contiene los futuros que no se completaron (futuros pendientes o en
   ejecución).

   El argumento *timeout* puede ser usado para controlar la espera
   máxima en segundos antes de retornar.  *timeout* puede ser un int o
   un float.  Si *timeout* no es especificado o es "None", no hay
   limite en el tiempo de espera.

   *return_when* indica cuando debe retornar esta función.  Debe ser
   alguna de las siguientes constantes:

   +----------------------------------------------------+----------------------------------------------------+
   | Constante                                          | Descripción                                        |
   |====================================================|====================================================|
   | concurrent.futures.FIRST_COMPLETED                 | La función retornará cuando cualquier futuro       |
   |                                                    | finalice o sea cancelado.                          |
   +----------------------------------------------------+----------------------------------------------------+
   | concurrent.futures.FIRST_EXCEPTION                 | The function will return when any future finishes  |
   |                                                    | by raising an exception. If no future raises an    |
   |                                                    | exception then it is equivalent to                 |
   |                                                    | "ALL_COMPLETED".                                   |
   +----------------------------------------------------+----------------------------------------------------+
   | concurrent.futures.ALL_COMPLETED                   | La función retornará cuando todos los futuros      |
   |                                                    | finalicen o sean cancelados.                       |
   +----------------------------------------------------+----------------------------------------------------+

concurrent.futures.as_completed(fs, timeout=None)

   Retorna un iterador sobre las instancias de "Future" (posiblemente
   creadas por distintas instancias de "Executor") dadas por *fs* que
   produce futuros a medida que van finalizando (normalmente o
   cancelados). Cualquier futuro dado por *fs* que esté duplicado será
   retornado una sola vez. Los futuros que hayan finalizado antes de
   la llamada a "as_completed()" serán entregados primero. El iterador
   retornado lanzará "TimeoutError" si "__next__()" es llamado y el
   resultado no está disponible luego de *timeout* segundos a partir
   de la llamada original a "as_completed()". *timeout* puede ser un
   int o un float. Si *timeout* no es especificado o es "None", no hay
   límite en el tiempo de espera.

Ver también:

  **PEP 3148** -- futuros - ejecutar cómputos asincrónicamente
     La propuesta que describe esta propuesta de inclusión en la
     biblioteca estándar de Python.

## Clases de Excepciones

exception concurrent.futures.CancelledError

   Lanzada cuando un futuro es cancelado.

exception concurrent.futures.TimeoutError

   Un alias obsoleto de "TimeoutError", lanzado cuando una operación
   en un futuro excede el tiempo de espera dado.

   Distinto en la versión 3.11: Esta clase se convirtió en un alias de
   "TimeoutError".

exception concurrent.futures.BrokenExecutor

   Derivada de "RuntimeError", esta excepción es lanzada cuando un
   ejecutor se encuentra corrupto por algún motivo y no puede ser
   utilizado para enviar o ejecutar nuevas tareas.

   Added in version 3.7.

exception concurrent.futures.InvalidStateError

   Lanzada cuando una operación es realizada sobre un futuro que no
   permite dicha operación en el estado actual.

   Added in version 3.8.

exception concurrent.futures.thread.BrokenThreadPool

   Derived from "BrokenExecutor", this exception class is raised when
   one of the workers of a "ThreadPoolExecutor" has failed
   initializing.

   Added in version 3.7.

exception concurrent.futures.interpreter.BrokenInterpreterPool

   Derived from "BrokenThreadPool", this exception class is raised
   when one of the workers of a "InterpreterPoolExecutor" has failed
   initializing.

   Added in version 3.14.

exception concurrent.futures.process.BrokenProcessPool

   Derived from "BrokenExecutor" (formerly "RuntimeError"), this
   exception class is raised when one of the workers of a
   "ProcessPoolExecutor" has terminated in a non-clean fashion (for
   example, if it was killed from the outside).

   Added in version 3.3.
