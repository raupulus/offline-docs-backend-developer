---
title: Runners
source_url: https://docs.python.org/es/3
source_path: library/asyncio-runner.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1700
---

# Runners

**Código fuente:** Lib/asyncio/runners.py

Esta sección describe las primitivas asyncio de alto nivel para
ejecutar código asyncio.

Están construidos sobre un event loop con el objetivo de simplificar
el uso de código async para escenarios comunes de alta difusión.

* Ejecutando un programa asyncio

* Gestor de contexto del runner

* Manejando interrupciones de teclado

## Ejecutando un programa asyncio

asyncio.run(coro, *, debug=None, loop_factory=None)

   Execute *coro* in an asyncio event loop and return the result.

   The argument can be any awaitable object.

   This function runs the awaitable, taking care of managing the
   asyncio event loop, *finalizing asynchronous generators*, and
   closing the executor.

   Esta función no puede ser llamada cuando otro bucle de eventos
   asyncio está corriendo en el mismo hilo.

   Si *debug* es "True", el bucle de eventos se ejecutará en modo
   depuración. "False" deshabilita el modo depuración de manera
   explícita. "None" se usa para respetar la configuración global Modo
   depuración.

   If *loop_factory* is not "None", it is used to create a new event
   loop; otherwise "asyncio.new_event_loop()" is used. The loop is
   closed at the end. This function should be used as a main entry
   point for asyncio programs, and should ideally only be called once.
   It is recommended to use *loop_factory* to configure the event loop
   instead of policies. Passing "asyncio.EventLoop" allows running
   asyncio without the policy system.

   Al ejecutor se le da un tiempo de espera de 5 minutos para
   apagarse. Si el ejecutor no ha finalizado en ese tiempo, se emite
   una advertencia y se cierra el ejecutor.

   Ejemplo:

      async def main():
          await asyncio.sleep(1)
          print('hello')

      asyncio.run(main())

   Added in version 3.7.

   Distinto en la versión 3.9: Actualizado para usar
   "loop.shutdown_default_executor()".

   Distinto en la versión 3.10: *debug* es "None" por defecto para
   respetar la configuración global del modo depuración.

   Distinto en la versión 3.12: Añadido el parámetro *loop_factory*.

   Distinto en la versión 3.14: *coro* can be any awaitable object.

   Nota:

     The "asyncio" policy system is deprecated and will be removed in
     Python 3.16; from there on, an explicit *loop_factory* is needed
     to configure the event loop.

## Gestor de contexto del runner

class asyncio.Runner(*, debug=None, loop_factory=None)

   Un gestor de contexto que simplifica *múltiples* llamadas a
   funciones asíncronas en el mismo contexto.

   A veces varias funciones asíncronas de alto nivel deben ser
   llamadas en el mismo event loop y "contextvars.Context".

   Si *debug* es "True", el bucle de eventos se ejecutará en modo
   depuración. "False" deshabilita el modo depuración de manera
   explícita. "None" se usa para respetar la configuración global Modo
   depuración.

   *loop_factory* puede ser usado para redefinir la creación de
   bucles. Es responsabilidad del *loop_factory* establecer el bucle
   creado como el actual. Por defecto "asyncio.new_event_loop()" es
   usado y configura el nuevo bucle de eventos como el actual con
   "asyncio.set_event_loop()" si *loop_factory* es "None".

   Basically, "asyncio.run()" example can be rewritten with the runner
   usage:

      async def main():
          await asyncio.sleep(1)
          print('hello')

      with asyncio.Runner() as runner:
          runner.run(main())

   Added in version 3.11.

   run(coro, *, context=None)

      Execute *coro* in the embedded event loop.

      The argument can be any awaitable object.

      If the argument is a coroutine, it is wrapped in a Task.

      An optional keyword-only *context* argument allows specifying a
      custom "contextvars.Context" for the code to run in. The
      runner's default context is used if context is "None".

      Returns the awaitable's result or raises an exception.

      Esta función no puede ser llamada cuando otro bucle de eventos
      asyncio está corriendo en el mismo hilo.

      Distinto en la versión 3.14: *coro* can be any awaitable object.

   close()

      Cierra el runner.

      Termina los generadores asíncronos, apaga el ejecutor por
      defecto, cierra el bucle de eventos y libera el
      "contextvars.Context" embebido.

   get_loop()

      Retorna el bucle de eventos asociado a la instancia del runner.

   Nota:

     "Runner" usa una estrategia de inicialización perezosa, su
     constructor no inicializa las estructuras de bajo nivel
     subyacentes.El *loop* y el *context* embebidos son creados al
     entrar al cuerpo "with" o en la primera llamada a "run()" o a
     "get_loop()".

## Manejando interrupciones de teclado

Added in version 3.11.

Cuando "signal.SIGINT" es lanzada por "Ctrl"-"C", la excepción
"KeyboardInterrupt" es lanzada en el hilo principal por defecto. Sin
embargo, esto no funciona con "asyncio" porque puede interrumpir las
funciones internas a asyncio e impedir la salida del programa.

Para mitigar este problema, "asyncio" maneja "signal.SIGINT" de la
siguiente forma:

1. "asyncio.Runner.run()" instala un administrador "signal.SIGINT"
   personalizado antes que cualquier código de usuario sea ejecutado y
   lo remueve a la salida de la función.

2. La "Runner" crea la tarea principal que será pasada a la co-rutina
   para su ejecución.

3. Cuando "signal.SIGINT" es lanzada por "Ctrl"-"C", el administrador
   de señales personalizado cancela la tarea principal llamando a
   "asyncio.Task.cancel()" que lanza "asyncio.CancelledError" dentro
   de la tarea principal.  Esto hace que la pila de Python se
   desenrolle, los bloques "try/except" y "try/finally" se pueden
   utilizar para la limpieza de recursos.  Luego que la tarea
   principal es cancelada, "asyncio.Runner.run()" lanza
   "KeyboardInterrupt".

4. Un usuario podría escribir un bucle cerrado que no puede ser
   interrumpido por "asyncio.Task.cancel()", en cuyo caso la segunda
   llamada a "Ctrl"-"C" lanza inmediatamente "KeyboardInterrupt" sin
   cancelar la tarea principal.
