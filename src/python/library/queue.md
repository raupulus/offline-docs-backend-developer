---
title: '"queue" --- A synchronized queue class'
source_url: https://docs.python.org/es/3
source_path: library/queue.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3610
---

# "queue" --- A synchronized queue class

**Código fuente:** Lib/queue.py

======================================================================

The "queue" module implements multi-producer, multi-consumer queues.
It is especially useful in threaded programming when information must
be exchanged safely between multiple threads.  The "Queue" class in
this module implements all the required locking semantics.

El módulo implementa tres tipos de cola, que difieren sólo en el orden
en que se recuperan las entradas.  En una cola FIFO (first-in, first-
out), las primeras tareas añadidas son las primeras recuperadas. En
una cola LIFO (last-in, first-out), la última entrada añadida es la
primera recuperada (operando como una pila).  En una cola de
prioridad, las entradas se mantienen ordenadas (usando el módulo
"heapq") y la entrada de menor valor se recupera primero.

Internamente, estos tres tipos de colas utilizan bloqueos para
bloquear temporalmente los hilos que compiten entre sí; sin embargo,
no están diseñadas para manejar la reposición dentro de un hilo.

Además, el módulo implementa un tipo de cola "simple" FIFO (first-in,
first-out), "SimpleQueue", cuya implementación específica proporciona
garantías adicionales a cambio de una funcionalidad menor.

The "queue" module defines the following classes and exceptions:

class queue.Queue(maxsize=0)

   Constructor para una cola FIFO (first-in, first-out).  *maxsize* es
   un número entero que establece el límite superior del número de
   elementos que pueden ser colocados en la cola.  La inserción se
   bloqueará una vez que se haya alcanzado este tamaño, hasta que se
   consuman los elementos de la cola.  Si *maxsize* es menor o igual a
   cero, el tamaño de la cola es infinito.

class queue.LifoQueue(maxsize=0)

   Constructor para una cola LIFO (último en entrar, primero en
   salir).  *maxsize* es un número entero que establece el límite
   superior del número de elementos que pueden ser colocados en la
   cola.  La inserción se bloqueará una vez que se haya alcanzado este
   tamaño, hasta que se consuman los elementos de la cola.  Si
   *maxsize* es menor o igual a cero, el tamaño de la cola es
   infinito.

class queue.PriorityQueue(maxsize=0)

   Constructor para una cola de prioridad.  *maxsize* es un número
   entero que establece el límite superior del número de elementos que
   pueden ser colocados en la cola.  La inserción se bloqueará una vez
   que se haya alcanzado este tamaño, hasta que se consuman los
   elementos de la cola.  Si *maxsize* es menor o igual a cero, el
   tamaño de la cola es infinito.

   Las entradas de menor valor se recuperan primero (la entrada de
   menor valor es la retornada por "min(entries)").  Un patrón típico
   para las entradas es una tupla en la forma: "(priority_number,
   data)".

   Si los elementos de *datos* no son comparables, los datos pueden
   envolverse en una clase que ignore el elemento de datos y sólo
   compare el número de prioridad:

      from dataclasses import dataclass, field
      from typing import Any

      @dataclass(order=True)
      class PrioritizedItem:
          priority: int
          item: Any=field(compare=False)

class queue.SimpleQueue

   Constructor de una cola sin límites FIFO (first-in, first-out). Las
   colas simples carecen de funcionalidad avanzada como el seguimiento
   de tareas.

   Simple queues are generic over the type of their items.

   Added in version 3.7.

exception queue.Empty

   Excepción lanzada cuando el objeto "get()" (o "get_nowait()") que
   no se bloquea es llamado en un objeto "Queue" que está vacío.

exception queue.Full

   Excepción lanzada cuando el objeto "put()" (o "put_nowait()") que
   no se bloquea es llamado en un objeto "Queue" que está lleno.

exception queue.ShutDown

   Exception raised when "put()" or "get()" is called on a "Queue"
   object which has been shut down.

   Added in version 3.13.

## Objetos de la cola

Los objetos de la cola ("Queue", "LifoQueue", o "PriorityQueue")
proporcionan los métodos públicos descritos a continuación.

Queue.qsize()

   Retorna el tamaño aproximado de la cola.  Nota, qsize() > 0 no
   garantiza que un get() posterior no se bloquee, ni *qsize() <
   maxsize* garantiza que put() no se bloquee.

Queue.empty()

   Retorna "True" si la cola está vacía, "False" si no.  Si empty()
   retorna "True" no garantiza que una llamada posterior a put() no se
   bloquee.  Del mismo modo, si empty() retorna "False" no garantiza
   que una llamada posterior a get() no se bloquee.

Queue.full()

   Retorna "True" si la cola está llena, "False" si no.  Si full()
   retorna "True" no garantiza que una llamada posterior a get() no se
   bloquee.  Del mismo modo, si full() retorna "False" no garantiza
   que una llamada posterior a put() no se bloquee.

Queue.put(item, block=True, timeout=None)

   Pone el *item* en la cola. Si el argumento opcional *block* es
   verdadero y *timeout* es "None" (el predeterminado), bloquea si es
   necesario hasta que un espacio libre esté disponible. Si *timeout*
   es un número positivo, bloquea como máximo *timeout* segundos y
   lanza la excepción "Full" si no había ningún espacio libre
   disponible en ese tiempo. De lo contrario (*block* es falso), pone
   un elemento en la cola si un espacio libre está disponible
   inmediatamente, o bien lanza la excepción "Full" (*timeout* es
   ignorado en ese caso).

   Raises "ShutDown" if the queue has been shut down.

Queue.put_nowait(item)

   Equivalente a "put(item, block=False)".

Queue.get(block=True, timeout=None)

   Retira y retorna un elemento de la cola.  Si los argumentos
   opcionales *block* son true y *timeout* es "None" (el
   predeterminado), bloquea si es necesario hasta que un elemento esté
   disponible. Si *timeout* es un número positivo, bloquea como máximo
   *timeout* segundos y lanza la excepción "Empty" si no había ningún
   elemento disponible en ese tiempo. De lo contrario (*block* es
   falso), retorna un elemento si uno está disponible inmediatamente,
   o bien lanza la excepción "Empty" (*timeout* es ignorado en ese
   caso).

   Antes de la 3.0 en los sistemas POSIX, y para todas las versiones
   en Windows, si *block* es verdadero y *timeout* es "None", esta
   operación entra en una espera no interrumpible en una cerradura
   subyacente. Esto significa que no puede haber excepciones, y en
   particular una SIGINT no disparará una "KeyboardInterrupt".

   Raises "ShutDown" if the queue has been shut down and is empty, or
   if the queue has been shut down immediately.

Queue.get_nowait()

   Equivalente a "get(False)".

Se ofrecen dos métodos para apoyar el seguimiento si las tareas en
cola han sido completamente procesadas por hilos *daemon* de consumo.

Queue.task_done()

   Indica que una tarea anteriormente en cola está completa.
   Utilizado por los hilos de la cola de consumo.  Por cada "get()"
   usado para recuperar una tarea, una llamada posterior a
   "task_done()" le dice a la cola que el procesamiento de la tarea
   está completo.

   Si un "join()" se está bloqueando actualmente, se reanudará cuando
   todos los ítems hayan sido procesados (lo que significa que se
   recibió una llamada "task_done()" por cada ítem que había sido
   "put()" en la cola).

   Lanza un "ValueError" si se llama más veces de las que hay
   elementos colocados en la cola.

Queue.join()

   Bloquea hasta que todos los artículos de la cola se hayan obtenido
   y procesado.

   El conteo de tareas sin terminar sube cada vez que se añade un
   elemento a la cola. El conteo baja cuando un hilo de consumidor
   llama "task_done()" para indicar que el elemento fue recuperado y
   todo el trabajo en él está completo. Cuando el conteo de tareas sin
   terminar cae a cero, "join()" se desbloquea.

### Waiting for task completion

Ejemplo de cómo esperar a que se completen las tareas en cola:

   import threading
   import queue

   q = queue.Queue()

   def worker():
       while True:
           item = q.get()
           print(f'Working on {item}')
           print(f'Finished {item}')
           q.task_done()

   # Turn-on the worker thread.
   threading.Thread(target=worker, daemon=True).start()

   # Send thirty task requests to the worker.
   for item in range(30):
       q.put(item)

   # Block until all tasks are done.
   q.join()
   print('All work completed')

### Terminating queues

When no longer needed, "Queue" objects can be wound down until empty
or terminated immediately with a hard shutdown.

Queue.shutdown(immediate=False)

   Put a "Queue" instance into a shutdown mode.

   The queue can no longer grow. Future calls to "put()" raise
   "ShutDown". Currently blocked callers of "put()" will be unblocked
   and will raise "ShutDown" in the formerly blocked thread.

   If *immediate* is false (the default), the queue can be wound down
   normally with "get()" calls to extract tasks that have already been
   loaded.

   And if "task_done()" is called for each remaining task, a pending
   "join()" will be unblocked normally.

   Once the queue is empty, future calls to "get()" will raise
   "ShutDown".

   If *immediate* is true, the queue is terminated immediately. The
   queue is drained to be completely empty and the count of unfinished
   tasks is reduced by the number of tasks drained. If unfinished
   tasks is zero, callers of "join()" are unblocked.  Also, blocked
   callers of "get()" are unblocked and will raise "ShutDown" because
   the queue is empty.

   Use caution when using "join()" with *immediate* set to true. This
   unblocks the join even when no work has been done on the tasks,
   violating the usual invariant for joining a queue.

   Added in version 3.13.

## Objetos de cola simple

Los objetos "SimpleQueue" proporcionan los métodos públicos descritos
a continuación.

SimpleQueue.qsize()

   Retorna el tamaño aproximado de la cola.  Nota, qsize() > 0 no
   garantiza que un get() posterior no se bloquee.

SimpleQueue.empty()

   Retorna "True" si la cola está vacía, "False" si no. Si empty()
   retorna "False" no garantiza que una llamada posterior a get() no
   se bloquee.

SimpleQueue.put(item, block=True, timeout=None)

   Pone el elemento en la cola.  El método nunca se bloquea y siempre
   tiene éxito (excepto por posibles errores de bajo nivel como la
   falta de asignación de memoria). Los argumentos opcionales *block*
   y *timeout* son ignorados y sólo se proporcionan por compatibilidad
   con "Queue.put()".

   Este método tiene una implementación en C la cual ha sido usada
   anteriormente. Los llamados "put()" o "get()" pueden ser
   interrumpidos por otro llamado "put()" en el mismo hilo sin
   bloquear o corromper el estado interno dentro de la fila. Esto lo
   hace apropiado para su uso en destructores como los métodos
   "__del__" o las retrollamadas "weakref".

SimpleQueue.put_nowait(item)

   Equivalente a "put(item, block=False)", siempre y cuando sea
   compatible con "Queue.put_nowait`()".

SimpleQueue.get(block=True, timeout=None)

   Retira y retorna un elemento de la cola.  Si los argumentos
   opcionales *block* son true y *timeout* es "None" (el
   predeterminado), bloquea si es necesario hasta que un elemento esté
   disponible. Si *timeout* es un número positivo, bloquea como máximo
   *timeout* segundos y lanza la excepción "Empty" si no había ningún
   elemento disponible en ese tiempo. De lo contrario (*block* es
   falso), retorna un elemento si uno está disponible inmediatamente,
   o bien lanza la excepción "Empty" (*timeout* es ignorado en ese
   caso).

SimpleQueue.get_nowait()

   Equivalente a "get(False)".

Ver también:

  Clase "multiprocessing.Queue"
     Una clase de cola para su uso en un contexto de
     multiprocesamiento (en lugar de multihilo).

  "collections.deque" es una implementación alternativa de colas sin
  límites con operaciones atómicas rápidas "append()" y "popleft()"
  que no requieren bloqueo y también soportan indexación.
