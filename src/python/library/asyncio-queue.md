---
title: Colas
source_url: https://docs.python.org/es/3
source_path: library/asyncio-queue.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1690
---

# Colas

**Código fuente:** Lib/asyncio/queue.py

======================================================================

Las colas asyncio son diseñadas para ser similares a clases del módulo
"queue".  Sin embargo las colas asyncio no son seguras para hilos, son
diseñadas para usar específicamente en código async/await.

Nota que los métodos de colas de asyncio no tienen un parámetro
*timeout*; usa la función "asyncio.wait_for()" para hacer operaciones
de cola con un tiempo de espera.

Ver también la sección Examples a continuación.

## Cola

class asyncio.Queue(maxsize=0)

   Una cola primero en entrar, primero en salir (PEPS, o *FIFO* en
   inglés).

   Si *maxsize* es menor que o igual a cero, el tamaño de la cola es
   infinito.  Si es un entero mayor a "0", entonces "await put()" se
   bloquea cuando una cola alcanza su *maxsize* hasta que un elemento
   es removido por "get()".

   Diferente de los subprocesos de la biblioteca estándar "queue", el
   tamaño de la cola siempre es conocido y puede ser retornado
   llamando el método "qsize()".

   Distinto en la versión 3.10: Excluido el parámetro *loop*.

   Esta clase es no segura para hilos.

   maxsize

      Número de ítems permitidos en la cola.

   empty()

      Retorna "True" si la cola es vacía, o "False" en caso contrario.

   full()

      Retorna "True" si hay "maxsize" ítems en la cola.

      If the queue was initialized with "maxsize=0" (the default),
      then "full()" never returns "True".

   async get()

      Remueve y retorna un ítem de la cola. Si la cola es vacía,
      espera hasta que un ítem esté disponible.

      Raises "QueueShutDown" if the queue has been shut down and is
      empty, or if the queue has been shut down immediately.

   get_nowait()

      Retorna un ítem si uno está inmediatamente disponible, de otra
      manera levanta "QueueEmpty".

      Raises "QueueShutDown" if the queue has been shut down and is
      empty.

   async join()

      Se bloquea hasta que todos los ítems en la cola han sido
      recibidos y procesados.

      El conteo de tareas no terminadas sube siempre que un ítem es
      agregado a la cola. El conteo baja siempre que la ejecución de
      una corrutina "task_done()" para indicar que el ítem fue
      recuperado y todo el trabajo en él está completo.  Cuando el
      conteo de tareas inacabadas llega a cero, "join()" se
      desbloquea.

   async put(item)

      Pone un ítem en la cola. Si la cola está completa, espera hasta
      que una entrada vacía esté disponible antes de agregar el ítem.

      Raises "QueueShutDown" if the queue has been shut down.

   put_nowait(item)

      Pone un ítem en la cola sin bloquearse.

      Si no hay inmediatamente disponibles entradas vacías, lanza
      "QueueFull".

      Raises "QueueShutDown" if the queue has been shut down.

   qsize()

      Retorna el número de ítems en la cola.

   shutdown(immediate=False)

      Put a "Queue" instance into a shutdown mode.

      The queue can no longer grow. Future calls to "put()" raise
      "QueueShutDown". Currently blocked callers of "put()" will be
      unblocked and will raise "QueueShutDown" in the formerly
      awaiting task.

      If *immediate* is false (the default), the queue can be wound
      down normally with "get()" calls to extract tasks that have
      already been loaded.

      And if "task_done()" is called for each remaining task, a
      pending "join()" will be unblocked normally.

      Once the queue is empty, future calls to "get()" will raise
      "QueueShutDown".

      If *immediate* is true, the queue is terminated immediately. The
      queue is drained to be completely empty and the count of
      unfinished tasks is reduced by the number of tasks drained. If
      unfinished tasks is zero, callers of "join()" are unblocked.
      Also, blocked callers of "get()" are unblocked and will raise
      "QueueShutDown" because the queue is empty.

      Use caution when using "join()" with *immediate* set to true.
      This unblocks the join even when no work has been done on the
      tasks, violating the usual invariant for joining a queue.

      Added in version 3.13.

   task_done()

      Indicate that a formerly enqueued work item is complete.

      Used by queue consumers. For each "get()" used to fetch a work
      item, a subsequent call to "task_done()" tells the queue that
      the processing on the work item is complete.

      Si un "join()" está actualmente bloqueando, éste se resumirá
      cuando todos los ítems han sido procesados (implicado que un
      método "task_done()" fue recibido por cada ítem que ha sido
      "put()" en la cola.

      Lanza "ValueError" si fue llamado más veces que los ítems en la
      cola.

## Cola de prioridad

class asyncio.PriorityQueue

   Una variante de "Queue"; recupera entradas en su orden de prioridad
   (el más bajo primero).

   Las entradas son típicamente tuplas de la forma "(priority_number,
   data)".

## Cola UEPA (o *LIFO* en inglés)

class asyncio.LifoQueue

   Una variante de una "Queue" que recupera primero el elemento
   agregado más reciente (último en entrar, primero en salir).

## Excepciones

exception asyncio.QueueEmpty

   Esta excepción es lanzada cuando el método "get_nowait()" es
   ejecutado en una cola vacía.

exception asyncio.QueueFull

   Las excepciones son lanzadas cuando el método "put_nowait()" es
   lanzado en una cola que ha alcanzado su *maxsize*.

exception asyncio.QueueShutDown

   Exception raised when "put()", "put_nowait()", "get()" or
   "get_nowait()" is called on a queue which has been shut down.

   Added in version 3.13.

## Ejemplos

Las colas pueden ser usadas para distribuir cargas de trabajo entre
múltiples tareas concurrentes:

   import asyncio
   import random
   import time

   async def worker(name, queue):
       while True:
           # Get a "work item" out of the queue.
           sleep_for = await queue.get()

           # Sleep for the "sleep_for" seconds.
           await asyncio.sleep(sleep_for)

           # Notify the queue that the "work item" has been processed.
           queue.task_done()

           print(f'{name} has slept for {sleep_for:.2f} seconds')

   async def main():
       # Create a queue that we will use to store our "workload".
       queue = asyncio.Queue()

       # Generate random timings and put them into the queue.
       total_sleep_time = 0
       for _ in range(20):
           sleep_for = random.uniform(0.05, 1.0)
           total_sleep_time += sleep_for
           queue.put_nowait(sleep_for)

       # Create three worker tasks to process the queue concurrently.
       tasks = []
       for i in range(3):
           task = asyncio.create_task(worker(f'worker-{i}', queue))
           tasks.append(task)

       # Wait until the queue is fully processed.
       started_at = time.monotonic()
       await queue.join()
       total_slept_for = time.monotonic() - started_at

       # Cancel our worker tasks.
       for task in tasks:
           task.cancel()
       # Wait until all worker tasks are cancelled.
       await asyncio.gather(*tasks, return_exceptions=True)

       print('====')
       print(f'3 workers slept in parallel for {total_slept_for:.2f} seconds')
       print(f'total expected sleep time: {total_sleep_time:.2f} seconds')

   asyncio.run(main())
