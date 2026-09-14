---
title: Primitivas de sincronización
source_url: https://docs.python.org/es/3
source_path: library/asyncio-sync.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1730
---

# Primitivas de sincronización

**Código fuente:** Lib/asyncio/locks.py

======================================================================

las primitivas de sincronización de asyncio están diseñadas para ser
similares a las del módulo "threading", con dos importantes
advertencias:

* las primitivas de asyncio no son seguras en hilos, por lo tanto, no
  deben ser usadas para la sincronización de hilos del sistema
  operativo (usa "threading" para esto);

* los métodos de estas primitivas de sincronización no aceptan el
  argumento *timeout*. Usa la función "asyncio.wait_for()" para
  realizar operaciones que involucren tiempos de espera.

asyncio tiene las siguientes primitivas de sincronización básicas:

* "Lock"

* "Event"

* "Condition"

* "Semaphore"

* "BoundedSemaphore"

* "Barrier"

======================================================================

## Lock

class asyncio.Lock

   Implementa un cierre de exclusión mutua para tareas asyncio. No es
   seguro en hilos.

   Un cierre asyncio puede usarse para garantizar el acceso en
   exclusiva a un recurso compartido.

   La forma preferida de usar un Lock es mediante una declaración
   "async with":

      lock = asyncio.Lock()

      # ... later
      async with lock:
          # access shared state

   lo que es equivalente a:

      lock = asyncio.Lock()

      # ... later
      await lock.acquire()
      try:
          # access shared state
      finally:
          lock.release()

   Distinto en la versión 3.10: Eliminado el parámetro *loop*.

   async acquire()

      Adquiere el cierre.

      Este método espera hasta que el cierre está *abierto*, lo
      establece como *cerrado* y retorna "True".

      Cuando más de una corrutina está bloqueada en "acquire()",
      esperando a que el cierre se abra, solo una de las corrutinas
      proseguirá finalmente.

      Adquirir un cierre es *justo*: la corrutina que prosigue será la
      primera corrutina que comenzó a esperarlo.

   release()

      Libera el cierre.

      Cuando el cierre está *cerrado*, lo restablece al estado
      *abierto* y retorna.

      Si el cierre está *abierto*, se lanza una excepción
      "RuntimeError".

   locked()

      Retorna "True" si el cierre está *cerrado*.

## Event

class asyncio.Event

   Un objeto de eventos. No es seguro en hilos.

   Un evento asyncio puede usarse para notificar a múltiples tareas
   asyncio que ha ocurrido algún evento.

   Un objeto Event administra una bandera interna que se puede
   establecer en *true* con el método "set()" y se restablece en
   *false* con el método "clear()". El método "wait()" se bloquea
   hasta que la bandera se establece en *true*. El flag se establece
   en *false* inicialmente.

   Distinto en la versión 3.10: Eliminado el parámetro *loop*.

   Ejemplo:

      async def waiter(event):
          print('waiting for it ...')
          await event.wait()
          print('... got it!')

      async def main():
          # Create an Event object.
          event = asyncio.Event()

          # Spawn a Task to wait until 'event' is set.
          waiter_task = asyncio.create_task(waiter(event))

          # Sleep for 1 second and set the event.
          await asyncio.sleep(1)
          event.set()

          # Wait until the waiter task is finished.
          await waiter_task

      asyncio.run(main())

   async wait()

      Espera hasta que se establezca el evento.

      Si el evento está configurado, retorna "True" inmediatamente. De
      lo contrario, bloquea hasta que otra tarea llame a "set()".

   set()

      Establece el evento.

      Todas las tareas esperando a que el evento se establezca serán
      activadas inmediatamente.

   clear()

      Borra (restablece) el evento.

      Subsequent tasks awaiting on "wait()" will now block until the
      "set()" method is called again.

   is_set()

      Retorna "True" si el evento está establecido.

## Condition

class asyncio.Condition(lock=None)

   Un objeto Condition. No seguro en hilos.

   Una tarea puede usar una condición primitiva de asyncio para
   esperar a que suceda algún evento y luego obtener acceso exclusivo
   a un recurso compartido.

   En esencia, un objeto Condition combina la funcionalidad de un
   objeto "Event" y un objeto "Lock". Es posible tener múltiples
   objetos Condition que compartan un mismo Lock, lo que permite
   coordinar el acceso exclusivo a un recurso compartido entre
   diferentes tareas interesadas en estados particulares de ese
   recurso compartido.

   El argumento opcional *lock* debe ser un objeto "Lock" o "None". En
   este último caso, se crea automáticamente un nuevo objeto Lock.

   Distinto en la versión 3.10: Eliminado el parámetro *loop*.

   La forma preferida de usar una condición es mediante una
   declaración "async with":

      cond = asyncio.Condition()

      # ... later
      async with cond:
          await cond.wait()

   lo que es equivalente a:

      cond = asyncio.Condition()

      # ... later
      await cond.acquire()
      try:
          await cond.wait()
      finally:
          cond.release()

   async acquire()

      Adquiere el cierre (lock) subyacente.

      Este método espera hasta que el cierre subyacente esté
      *abierto*, lo establece en *cerrado* y retorna "True".

   notify(n=1)

      Wake up *n* tasks (1 by default) waiting on this condition.  If
      fewer than *n* tasks are waiting they are all awakened.

      El cierre debe adquirirse antes de llamar a este método y
      liberarse poco después. Si se llama con un cierre *abierto*, se
      lanza una excepción "RuntimeError".

   locked()

      Retorna "True" si el cierre subyacente está adquirido.

   notify_all()

      Despierta todas las tareas que esperan a esta condición.

      Este método actúa como "notify()", pero despierta todas las
      tareas en espera.

      El cierre debe adquirirse antes de llamar a este método y
      liberarse poco después. Si se llama con un cierre *abierto*, se
      lanza una excepción "RuntimeError".

   release()

      Libera el cierre subyacente.

      Cuando se invoca en un cierre abierto, se lanza una excepción
      "RuntimeError".

   async wait()

      Espera hasta que se le notifique.

      Si la tarea que llama no ha adquirido el cierre cuando se llama
      a este método, se lanza una excepción "RuntimeError".

      Este método libera el cierre subyacente y luego se bloquea hasta
      que lo despierte una llamada "notify()" o "notify_all()". Una
      vez despertado, la condición vuelve a adquirir su cierre y este
      método retorna "True".

      Note that a task *may* return from this call spuriously, which
      is why the caller should always re-check the state and be
      prepared to "wait()" again. For this reason, you may prefer to
      use "wait_for()" instead.

   async wait_for(predicate)

      Espera hasta que un predicado se vuelva *verdadero*.

      The predicate must be a callable which result will be
      interpreted as a boolean value.  The method will repeatedly
      "wait()" until the predicate evaluates to *true*. The final
      value is the return value.

## Semaphore

class asyncio.Semaphore(value=1)

   Un objeto Semaphore. No es seguro en hilos.

   Un semáforo gestiona un contador interno que se reduce en cada
   llamada al método "acquire()" y se incrementa en cada llamada al
   método "release()". El contador nunca puede bajar de cero, cuando
   "acquire()" encuentra que es cero, se bloquea, esperando hasta que
   alguna tarea llame a "release()".

   El argumento opcional *value* proporciona el valor inicial para el
   contador interno ("1" por defecto). Si el valor dado es menor que
   "0" se lanza una excepción "ValueError".

   Distinto en la versión 3.10: Eliminado el parámetro *loop*.

   La forma preferida de utilizar un semáforo es mediante una
   declaración "async with":

      sem = asyncio.Semaphore(10)

      # ... later
      async with sem:
          # work with shared resource

   lo que es equivalente a:

      sem = asyncio.Semaphore(10)

      # ... later
      await sem.acquire()
      try:
          # work with shared resource
      finally:
          sem.release()

   async acquire()

      Adquiere un semáforo.

      Si el contador interno es mayor que cero, lo reduce en uno y
      retorna "True" inmediatamente. Si es cero, espera hasta que se
      llame al método "release()" y retorna "True".

   locked()

      Retorna "True" si el semáforo no se puede adquirir de inmediato.

   release()

      Libera un semáforo, incrementando el contador interno en uno.
      Puede despertar una tarea que esté a la espera para adquirir el
      semáforo.

      A diferencia de "BoundedSemaphore", "Semaphore" permite hacer
      más llamadas "release()" que llamadas "acquire()".

## BoundedSemaphore

class asyncio.BoundedSemaphore(value=1)

   Un objeto semáforo delimitado. No es seguro en hilos.

   BoundedSemaphore es una versión de la clase "Semaphore" que lanza
   una excepción "ValueError" en "release()" si aumenta el contador
   interno por encima del *valor* inicial.

   Distinto en la versión 3.10: Eliminado el parámetro *loop*.

## Barrera

class asyncio.Barrier(parties)

   Un objeto barrera. No es seguro en hilos.

   Una barrera es una primitiva de sincronización simple que permite
   bloquear hasta que un número *parties* de tareas estén esperando en
   ella. Las tareas pueden esperar en el método "wait()" y se
   bloquearán hasta que el número especificado de tareas termine
   esperando en "wait()". En ese momento, todas las tareas en espera
   se desbloquearán simultáneamente.

   "async with" puede utilizarse como alternativa a esperar en
   "wait()".

   La barrera puede reutilizarse tantas veces como se desee.

   Ejemplo:

      async def example_barrier():
         # barrier with 3 parties
         b = asyncio.Barrier(3)

         # create 2 new waiting tasks
         asyncio.create_task(b.wait())
         asyncio.create_task(b.wait())

         await asyncio.sleep(0)
         print(b)

         # The third .wait() call passes the barrier
         await b.wait()
         print(b)
         print("barrier passed")

         await asyncio.sleep(0)
         print(b)

      asyncio.run(example_barrier())

   El resultado de este ejemplo es:

      <asyncio.locks.Barrier object at 0x... [filling, waiters:2/3]>
      <asyncio.locks.Barrier object at 0x... [draining, waiters:0/3]>
      barrier passed
      <asyncio.locks.Barrier object at 0x... [filling, waiters:0/3]>

   Added in version 3.11.

   async wait()

      Pasa la barrera. Cuando todas las tareas que forman parte de la
      barrera han llamado a esta función, todas se desbloquean
      simultáneamente.

      Cuando se cancela una tarea en espera o bloqueada en la barrera,
      esta tarea sale de la barrera que permanece en el mismo estado.
      Si el estado de la barrera es "filling", el número de tareas en
      espera disminuye en 1.

      El valor de retorno es un entero en el rango de 0 a "parties-1",
      diferente para cada tarea. Esto se puede utilizar para
      seleccionar una tarea para hacer algún mantenimiento especial,
      por ejemplo:

         ...
         async with barrier as position:
            if position == 0:
               # Only one task prints this
               print('End of *draining phase*')

      Este método puede lanzar una excepción "BrokenBarrierError" si
      la barrera se rompe o se restablece mientras una tarea está en
      espera. Podría lanzar una excepción "CancelledError" si se
      cancela una tarea.

   async reset()

      Devuelve la barrera al estado vacío por defecto.  Cualquier
      tarea que espere en ella recibirá la excepción
      "BrokenBarrierError".

      Si se rompe una barrera, puede ser mejor dejarla y crear una
      nueva.

   async abort()

      Put the barrier into a broken state.  This causes any active or
      future calls to "wait()" to fail with the "BrokenBarrierError".
      Use this for example if one of the tasks needs to abort, to
      avoid infinite waiting tasks.

   parties

      El número de tareas necesarias para pasar la barrera.

   n_waiting

      El número de tareas que esperan actualmente en la barrera
      mientras se llena.

   broken

      Un booleano que es "True" si la barrera está en estado roto.

exception asyncio.BrokenBarrierError

   Esta excepción, una subclase de "RuntimeError", se lanza cuando el
   objeto "Barrier" se reinicia o se rompe.

======================================================================

Distinto en la versión 3.9: Adquirir un bloqueo usando "await lock" o
"yield from lock" o una declaración "with" ("with await lock", "with
(yield from lock)") se eliminó . En su lugar, use "async with lock".
