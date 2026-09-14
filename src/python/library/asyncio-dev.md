---
title: Desarrollando con asyncio
source_url: https://docs.python.org/es/3
source_path: library/asyncio-dev.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1590
---

# Desarrollando con asyncio

La programación asincrónica es diferente a la programación
"secuencial" clásica.

Esta página enumera errores y trampas comunes y explica cómo
evitarlos.

## Modo depuración

Por defecto asyncio se ejecuta en modo producción. Para facilitar el
desarrollo asyncio tiene un *modo depuración*.

Hay varias maneras de habilitar el modo depuración de asyncio:

* Definiendo la variable de entorno "PYTHONASYNCIODEBUG" a "1".

* Usando Modo de Desarrollo de Python.

* Pasando "debug=True" a "asyncio.run()".

* Invocando "loop.set_debug()".

Además de habilitar el modo depuración, considere también:

* definir el nivel de log del asyncio logger a "logging.DEBUG", por
  ejemplo el siguiente fragmento de código puede ser ejecutado al
  inicio de la aplicación:

     logging.basicConfig(level=logging.DEBUG)

* configurando el módulo "warnings" para mostrar advertencias
  "ResourceWarning". Una forma de hacerlo es usando la opción "-W"
  "default" de la línea de comandos.

Cuando el modo depuración está habilitado:

* Muchas APIs asyncio que no son seguras para hilos (como los métodos
  "loop.call_soon()" y "loop.call_at()") generan una excepción si son
  llamados desde un hilo equivocado.

* El tiempo de ejecución del selector E/S es registrado si tarda
  demasiado tiempo en realizar una operación E/S.

* Los callbacks que tardan más de 100ms son registrados. El atributo
  "loop.slow_callback_duration" puede ser usado para definir la
  duración mínima de ejecución en segundos que se considere como
  "lenta".

## Concurrencia y multihilo

Un bucle de eventos se ejecuta en un hilo (generalmente el hilo
principal) y ejecuta todos los callbacks y las Tareas en su hilo.
Mientras una Tarea está ejecutándose en el bucle de eventos, ninguna
otra Tarea puede ejecutarse en el mismo hilo. Cuando una Tarea ejecuta
una expresión "await", la Tarea en ejecución se suspende y el bucle de
eventos ejecuta la siguiente Tarea.

Para programar un *callback* desde otro hilo del SO, se debe usar el
método "loop.call_soon_threadsafe()". Ejemplo:

   loop.call_soon_threadsafe(callback, *args)

Casi ningún objeto asyncio es seguro entre hilos (*thread safe*), lo
cual generalmente no es un problema a no ser que haya código que
trabaje con ellos desde fuera de una Tarea o un callback. Si tal
código necesita llamar a la API de asyncio de bajo nivel, se debe usar
el método "loop.call_soon_threadsafe()", por ejemplo:

   loop.call_soon_threadsafe(fut.cancel)

Para programar un objeto de corrutina desde una hilo diferente del
sistema operativo se debe usar la función
"run_coroutine_threadsafe()". Esta retorna un
"concurrent.futures.Future" para acceder al resultado:

   async def coro_func():
        return await asyncio.sleep(1, 42)

   # Later in another OS thread:

   future = asyncio.run_coroutine_threadsafe(coro_func(), loop)
   # Wait for the result:
   result = future.result()

Para manejar señales el bucle de eventos debe ser ejecutado en el hilo
principal.

The "loop.run_in_executor()" method can be used with a
"concurrent.futures.ThreadPoolExecutor" or "InterpreterPoolExecutor"
to execute blocking code in a different OS thread without blocking the
OS thread that the event loop runs in.

Actualmente no hay forma de programar corrutinas o retrollamadas
directamente desde un proceso diferente (como uno que haya comenzado
con "multiprocessing"). La sección Event loop methods enumera las API
que pueden leer desde tuberías y descriptores de archivos sin bloquear
el bucle de eventos. Además, las API Subprocess de asyncio
proporcionan una forma de iniciar un proceso y comunicarse con él
desde el bucle de eventos. Por último, el método
"loop.run_in_executor()" mencionado anteriormente también se puede
usar con un "concurrent.futures.ProcessPoolExecutor" para ejecutar
código en un proceso diferente.

## Ejecutando código bloqueante

Código bloqueante (dependiente de la CPU) no debe ser ejecutado
directamente. Por ejemplo, si una función realiza un cálculo intensivo
de CPU durante 1 segundo, todas las Tareas y operaciones de
Entrada/Salida (IO) concurrentes se retrasarían 1 segundo.

An executor can be used to run a task in a different thread, including
in a different interpreter, or even in a different process to avoid
blocking the OS thread with the event loop.  See the
"loop.run_in_executor()" method for more details.

## Logueando

asyncio usa el módulo "logging" y todo el logueo es realizado mediante
el logger ""asyncio"".

El nivel de log por defecto es "logging.INFO", el cual puede ser
fácilmente ajustado:

   logging.getLogger("asyncio").setLevel(logging.WARNING)

Loguear por la red puede bloquear el bucle de eventos. Se recomienda
usar un subproceso separado para manejar registros o usar sin bloqueo
IO. Por ejemplo, consulte Tratar con gestores que bloquean.

## Detectar corrutinas no esperadas

Cuando una función de corrutina es invocada, pero no esperada (por
ejemplo "coro()" en lugar de "await coro()") o la corrutina no es
programada con "asyncio.create_task()", asyncio emitirá una
"RuntimeWarning":

   import asyncio

   async def test():
       print("never scheduled")

   async def main():
       test()

   asyncio.run(main())

Salida:

   test.py:7: RuntimeWarning: coroutine 'test' was never awaited
     test()

Salida en modo depuración:

   test.py:7: RuntimeWarning: coroutine 'test' was never awaited
   Coroutine created at (most recent call last)
     File "../t.py", line 9, in <module>
       asyncio.run(main(), debug=True)

     < .. >

     File "../t.py", line 7, in main
       test()
     test()

La solución habitual es esperar la corrutina o llamar a la función
"asyncio.create_task()":

   async def main():
       await test()

## Detectar excepciones nunca recuperadas

Si un "Future.set_exception()" es invocado pero el objeto Futuro nunca
es esperado, la excepción nunca será propagada al código del usuario.
En este caso, asyncio emitiría un mensaje de registro cuando el objeto
Futuro fuera recolectado como basura.

Ejemplo de una excepción no manejada:

   import asyncio

   async def bug():
       raise Exception("not consumed")

   async def main():
       asyncio.create_task(bug())

   asyncio.run(main())

Salida:

   Task exception was never retrieved
   future: <Task finished coro=<bug() done, defined at test.py:3>
     exception=Exception('not consumed')>

   Traceback (most recent call last):
     File "test.py", line 4, in bug
       raise Exception("not consumed")
   Exception: not consumed

Habilita el modo depuración para obtener el seguimiento de pila
(*traceback*) donde la tarea fue creada:

   asyncio.run(main(), debug=True)

Salida en modo depuración:

   Task exception was never retrieved
   future: <Task finished coro=<bug() done, defined at test.py:3>
       exception=Exception('not consumed') created at asyncio/tasks.py:321>

   source_traceback: Object created at (most recent call last):
     File "../t.py", line 9, in <module>
       asyncio.run(main(), debug=True)

   < .. >

   Traceback (most recent call last):
     File "../t.py", line 4, in bug
       raise Exception("not consumed")
   Exception: not consumed

## Asynchronous generators best practices

Writing correct and efficient asyncio code requires awareness of
certain pitfalls. This section outlines essential best practices that
can save you hours of debugging.

### Close asynchronous generators explicitly

It is recommended to manually close the *asynchronous generator*. If a
generator exits early - for example, due to an exception raised in the
body of an "async for" loop - its asynchronous cleanup code may run in
an unexpected context. This can occur after the tasks it depends on
have completed, or during the event loop shutdown when the async-
generator's garbage collection hook is called.

To avoid this, explicitly close the generator by calling its
"aclose()" method, or use the "contextlib.aclosing()" context manager:

   import asyncio
   import contextlib

   async def gen():
     yield 1
     yield 2

   async def func():
     async with contextlib.aclosing(gen()) as g:
       async for x in g:
         break  # Don't iterate until the end

   asyncio.run(func())

As noted above, the cleanup code for these asynchronous generators is
deferred. The following example demonstrates that the finalization of
an asynchronous generator can occur in an unexpected order:

   import asyncio
   work_done = False

   async def cursor():
       try:
           yield 1
       finally:
           assert work_done

   async def rows():
       global work_done
       try:
           yield 2
       finally:
           await asyncio.sleep(0.1) # immitate some async work
           work_done = True

   async def main():
       async for c in cursor():
           async for r in rows():
               break
           break

   asyncio.run(main())

For this example, we get the following output:

   unhandled exception during asyncio.run() shutdown
   task: <Task finished name='Task-3' coro=<<async_generator_athrow without __name__>()> exception=AssertionError()>
   Traceback (most recent call last):
     File "example.py", line 6, in cursor
       yield 1
   asyncio.exceptions.CancelledError

   During handling of the above exception, another exception occurred:

   Traceback (most recent call last):
     File "example.py", line 8, in cursor
       assert work_done
              ^^^^^^^^^
   AssertionError

The "cursor()" asynchronous generator was finalized before the "rows"
generator - an unexpected behavior.

The example can be fixed by explicitly closing the "cursor" and "rows"
async-generators:

   async def main():
       async with contextlib.aclosing(cursor()) as cursor_gen:
           async for c in cursor_gen:
               async with contextlib.aclosing(rows()) as rows_gen:
                   async for r in rows_gen:
                       break
               break

### Create asynchronous generators only when the event loop is running

It is recommended to create *asynchronous generators* only after the
event loop has been created.

To ensure that asynchronous generators close reliably, the event loop
uses the "sys.set_asyncgen_hooks()" function to register callback
functions. These callbacks update the list of running asynchronous
generators to keep it in a consistent state.

When the "loop.shutdown_asyncgens()" function is called, the running
generators are stopped gracefully and the list is cleared.

The asynchronous generator invokes the corresponding system hook
during its first iteration. At the same time, the generator records
that the hook has been called and does not call it again.

Therefore, if iteration begins before the event loop is created, the
event loop will not be able to add the generator to its list of active
generators because the hooks are set after the generator attempts to
call them. Consequently, the event loop will not be able to terminate
the generator if necessary.

Consider the following example:

   import asyncio

   async def agenfn():
       try:
           yield 10
       finally:
           await asyncio.sleep(0)

   with asyncio.Runner() as runner:
       agen = agenfn()
       print(runner.run(anext(agen)))
       del agen

Salida:

   10
   Exception ignored while closing generator <async_generator object agenfn at 0x000002F71CD10D70>:
   Traceback (most recent call last):
     File "example.py", line 13, in <module>
       del agen
           ^^^^
   RuntimeError: async generator ignored GeneratorExit

This example can be fixed as follows:

   import asyncio

   async def agenfn():
       try:
           yield 10
       finally:
           await asyncio.sleep(0)

   async def main():
       agen = agenfn()
       print(await anext(agen))
       del agen

   asyncio.run(main())

### Avoid concurrent iteration and closure of the same generator

Async generators may be reentered while another "__anext__()" /
"athrow()" / "aclose()" call is in progress. This may lead to an
inconsistent state of the async generator and can cause errors.

Let's consider the following example:

   import asyncio

   async def consumer():
       for idx in range(100):
           await asyncio.sleep(0)
           message = yield idx
           print('received', message)

   async def amain():
       agenerator = consumer()
       await agenerator.asend(None)

       fa = asyncio.create_task(agenerator.asend('A'))
       fb = asyncio.create_task(agenerator.asend('B'))
       await fa
       await fb

   asyncio.run(amain())

Salida:

   received A
   Traceback (most recent call last):
     File "test.py", line 38, in <module>
       asyncio.run(amain())
       ~~~~~~~~~~~^^^^^^^^^
     File "Lib/asyncio/runners.py", line 204, in run
       return runner.run(main)
              ~~~~~~~~~~^^^^^^
     File "Lib/asyncio/runners.py", line 127, in run
       return self._loop.run_until_complete(task)
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
     File "Lib/asyncio/base_events.py", line 719, in run_until_complete
       return future.result()
              ~~~~~~~~~~~~~^^
     File "test.py", line 36, in amain
       await fb
   RuntimeError: anext(): asynchronous generator is already running

Therefore, it is recommended to avoid using asynchronous generators in
parallel tasks or across multiple event loops.
