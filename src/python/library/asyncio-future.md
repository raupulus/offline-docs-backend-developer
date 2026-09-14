---
title: Futures
source_url: https://docs.python.org/es/3
source_path: library/asyncio-future.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1630
---

# Futures

**Código fuente:** Lib/asyncio/futures.py, Lib/asyncio/base_futures.py

======================================================================

Los objetos *Future* se utilizan para conectar **código basado en
retrollamadas de bajo nivel** (*low-level callback-based code*) con
código *async/await* de alto nivel.

## Funciones Future

asyncio.isfuture(obj)

   Retorna "True" si *obj* es uno de los siguientes:

   * una instancia de "asyncio.Future",

   * una instancia de "asyncio.Task",

   * un objeto tipo Future con un atributo "_asyncio_future_blocking".

   Added in version 3.5.

asyncio.ensure_future(obj, *, loop=None)

   Retorna:

   * el argumento *obj* inalterado, si *obj* es una "Future", "Task",
     o un objeto tipo Future (esto se puede verificar con
     "isfuture()".)

   * un objeto "Task" envolviendo *obj*, si *obj* es una corrutina
     (esto se puede verificar con "iscoroutine()"); en este caso, la
     corrutina será programada por "ensure_future()".

   * un objeto "Task" que aguardará a *obj*, si *obj* es aguardable
     (esto se puede verificar con "inspect.isawaitable()".)

   Si *obj* no es ninguno de los superiores, se lanzará "TypeError".

   Importante:

     Guarda una referencia al resultado de esta función, evita que una
     tarea desaparezca a mitad de su ejecución.See also the
     "create_task()" function which is the preferred way for creating
     new tasks or use "asyncio.TaskGroup" which keeps reference to the
     task internally.

   Distinto en la versión 3.5.1: La función acepta cualquier objeto
   *awaitable*.

   Obsoleto desde la versión 3.10: Se emite una advertencia de
   desaprobación si *obj* no es un objeto tipo Future y no se
   especifica *loop* y no hay un bucle de eventos en ejecución.

asyncio.wrap_future(future, *, loop=None)

   Envuelve un objeto "concurrent.futures.Future" en un objeto
   "asyncio.Future".

   Obsoleto desde la versión 3.10: Se emite una advertencia de
   desaprobación si *future* no es un objeto tipo Future y *loop* no
   se especifica y no hay un bucle de eventos en ejecución.

## Objeto Future

class asyncio.Future(*, loop=None)

   Un Future representa un resultado eventual de una operación
   asíncrona. No es seguro en hilos (*thread-safe*).

   Future es un objeto *awaitable*. Las corrutinas pueden esperar a
   objetos Future hasta que obtengan un resultado o excepción, o hasta
   que se cancelen. Un Future puede esperarse varias veces y el
   resultado es el mismo.

   Normalmente, los Futures se utilizan para permitir que código
   basado en retrollamadas de bajo nivel (*low-level callback-based
   code*) (por ejemplo, en protocolos implementados utilizando
   *asyncio* transports) interactúe con código *async/await* de alto
   nivel.

   Es recomendable no exponer nunca objetos Future en APIs expuestas
   al usuario, y la forma recomendada de crear un objeto Future es
   llamando a "loop.create_future()". De esta forma, implementaciones
   alternativas de bucles de eventos (*event loop*) pueden inyectar
   sus propias implementaciones optimizadas de un objeto Future.

   Futures are generic over the type of their results.

   Distinto en la versión 3.7: Añadido soporte para el módulo
   "contextvars".

   Obsoleto desde la versión 3.10: Se emite una advertencia de
   desaprobación si no se especifica *loop* y no hay un bucle de
   eventos en ejecución.

   result()

      Retorna el resultado del Future.

      Si el Future es *done* y tiene un resultado establecido por el
      método "set_result()", el valor resultante es retornado.

      Si el Future es *done* y tiene una excepción establecida por el
      método "set_exception()", este método lanzará esta excepción.

      Si un evento es *cancelled*, este método lanzará una excepción
      "CancelledError".

      If the Future's result isn't yet available, this method raises
      an "InvalidStateError" exception.

   set_result(result)

      Marca el Future como *done* y establece su resultado.

      Raises an "InvalidStateError" error if the Future is already
      *done*.

   set_exception(exception)

      Marca el Future como *done* y establece una excepción.

      Raises an "InvalidStateError" error if the Future is already
      *done*.

   done()

      Retorna "True" si el Future está *done*.

      Un Future está *done* si estaba *cancelled* o si tiene un
      resultado o excepción establecidos mediante llamadas a
      "set_result()" o "set_exception()".

   cancelled()

      Retorna "True" si el Future fue *cancelled*.

      El método suele utilizarse para comprobar que un Future no es
      *cancelled* antes de establecer un resultado o excepción al
      mismo:

         if not fut.cancelled():
             fut.set_result(42)

   add_done_callback(callback, *, context=None)

      Añade una retrollamada (*callback*) a ser ejecutada cuando el
      Future es *done*.

      La retrollamada (*callback*) es llamada con el objeto Future
      como su único argumento.

      Si el Future ya es *done* cuando se llama a este método, la
      retrollamada (*callback*) es programada con "loop.call_soon()".

      Un argumento opcional de contexto, por palabra clave, permite
      especificar un "contextvars.Context" personalizado para ser
      ejecutado en la retrollamada (*callback*). El contexto actual se
      utiliza cuando no se provee un contexto (*context*).

      "functools.partial()" se puede utilizar para dar parámetros a la
      retrollamada (*callback*), por ejemplo:

         # Call 'print("Future:", fut)' when "fut" is done.
         fut.add_done_callback(
             functools.partial(print, "Future:"))

      Distinto en la versión 3.7: El parámetro de contexto (*context*)
      por palabra clave fue añadido. Ver **PEP 567** para más
      detalles.

   remove_done_callback(callback)

      Elimina la retrollamada (*callback*) de la lista de
      retrollamadas.

      Retorna el número de retrollamadas (*callbacks*) eliminadas, que
      normalmente es 1, excepto si una retrollamada fue añadida más de
      una vez.

   cancel(msg=None)

      Cancela el Future y programa retrollamadas (*callbacks*).

      Si el Future ya está *done* o *cancelled*, retorna "False". De
      lo contrario, cambia el estado del Future a *cancelled*,
      programa las retrollamadas, y retorna "True".

      The optional string argument *msg* is passed as the argument to
      the "CancelledError" exception raised when a cancelled Future is
      awaited.

      Distinto en la versión 3.9: Se agregó el parámetro *msg*.

   exception()

      Retorna la excepción definida en este Future.

      La excepción (o "None" si no se había establecido ninguna
      excepción) es retornada sólo si Future es *done*.

      Si un evento es *cancelled*, este método lanzará una excepción
      "CancelledError".

      Si el Future todavía no es *done*, este método lanza una
      excepción "InvalidStateError".

   get_loop()

      Retorna el bucle de eventos (*event loop*) al cual el objeto
      Future está asociado.

      Added in version 3.7.

Este ejemplo crea un objeto Future, crea y programa una Task asíncrona
para establecer el resultado para el Future, y espera hasta que el
Future tenga un resultado:

   async def set_after(fut, delay, value):
       # Sleep for *delay* seconds.
       await asyncio.sleep(delay)

       # Set *value* as a result of *fut* Future.
       fut.set_result(value)

   async def main():
       # Get the current event loop.
       loop = asyncio.get_running_loop()

       # Create a new Future object.
       fut = loop.create_future()

       # Run "set_after()" coroutine in a parallel Task.
       # We are using the low-level "loop.create_task()" API here because
       # we already have a reference to the event loop at hand.
       # Otherwise we could have just used "asyncio.create_task()".
       loop.create_task(
           set_after(fut, 1, '... world'))

       print('hello ...')

       # Wait until *fut* has a result (1 second) and print it.
       print(await fut)

   asyncio.run(main())

Importante:

  El objeto Future fue diseñado para imitar a
  "concurrent.futures.Future". Entre las principales diferencias
  están:

  * al contrario que Futures de *asyncio*, las instancias de
    "concurrent.futures.Future" no son aguardables (*await*).

  * "asyncio.Future.result()" y "asyncio.Future.exception()" no
    aceptan el argumento *timeout*.

  * "asyncio.Future.result()" y "asyncio.Future.exception()" lanzan
    una excepción "InvalidStateError" cuando el Future no es *done*.

  * Las retrollamadas (*callbacks*) registradas con
    "asyncio.Future.add_done_callback()" no son llamadas
    inmediatamente, sino que son programadas con "loop.call_soon()".

  * *asyncio* Future no es compatible con las funciones
    "concurrent.futures.wait()" ni
    "concurrent.futures.as_completed()".

  * "asyncio.Future.cancel()" acepta un argumento opcional "msg", pero
    "concurrent.futures.Future.cancel()" no.
