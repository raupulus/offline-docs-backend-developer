---
title: '"heapq" --- Heap queue algorithm'
source_url: https://docs.python.org/es/3
source_path: library/heapq.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2800
---

# "heapq" --- Heap queue algorithm

**Código fuente:** Lib/heapq.py

======================================================================

Este módulo proporciona una implementación del algoritmo de
montículos, también conocido como algoritmo de cola con prioridad.

Min-heaps are binary trees for which every parent node has a value
less than or equal to any of its children. We refer to this condition
as the heap invariant.

For min-heaps, this implementation uses lists for which "heap[k] <=
heap[2*k+1]" and "heap[k] <= heap[2*k+2]" for all *k* for which the
compared elements exist.  Elements are counted from zero.  The
interesting property of a min-heap is that its smallest element is
always the root, "heap[0]".

Max-heaps satisfy the reverse invariant: every parent node has a value
*greater* than any of its children.  These are implemented as lists
for which "maxheap[2*k+1] <= maxheap[k]" and "maxheap[2*k+2] <=
maxheap[k]" for all *k* for which the compared elements exist. The
root, "maxheap[0]", contains the *largest* element;
"heap.sort(reverse=True)" maintains the max-heap invariant.

The "heapq" API differs from textbook heap algorithms in two aspects:
(a) We use zero-based indexing.  This makes the relationship between
the index for a node and the indexes for its children slightly less
obvious, but is more suitable since Python uses zero-based indexing.
(b) Textbooks often focus on max-heaps, due to their suitability for
in-place sorting. Our implementation favors min-heaps as they better
correspond to Python "lists".

These two aspects make it possible to view the heap as a regular
Python list without surprises: "heap[0]" is the smallest item, and
"heap.sort()" maintains the heap invariant!

Like "list.sort()", this implementation uses only the "<" operator for
comparisons, for both min-heaps and max-heaps.

In the API below, and in this documentation, the unqualified term
*heap* generally refers to a min-heap. The API for max-heaps is named
using a "_max"  suffix.

To create a heap, use a list initialized as "[]", or transform an
existing list into a min-heap or max-heap using the "heapify()" or
"heapify_max()" functions, respectively.

The following functions are provided for min-heaps:

heapq.heapify(x)

   Transform list *x* into a min-heap, in-place, in linear time.

heapq.heappush(heap, item)

   Push the value *item* onto the *heap*, maintaining the min-heap
   invariant.

heapq.heappop(heap)

   Pop and return the smallest item from the *heap*, maintaining the
   min-heap invariant.  If the heap is empty, "IndexError" is raised.
   To access the smallest item without popping it, use "heap[0]".

heapq.heappushpop(heap, item)

   Apila el elemento o *iem* en el montículo, y luego desapila y
   retorna el elemento más pequeño del montículo. La acción combinada
   se ejecuta más eficientemente que "heappush()" seguido de una
   llamada separada a "heappop()".

heapq.heapreplace(heap, item)

   Desapila y retorna el elemento más pequeño del *heap*, y también
   apile el nuevo *item*. El tamaño del montículo no cambia. Si el
   montículo está vacío, "IndexError" se lanza.

   Esta operación de un solo paso es más eficiente que un "heappop()"
   seguido por "heappush()" y puede ser más apropiada cuando se
   utiliza un montículo de tamaño fijo. La combinación pop/push
   siempre retorna un elemento del montículo y lo reemplaza con
   *item*.

   El valor retornado puede ser mayor que el *item* añadido. Si no se
   desea eso, considere usar "heappushpop()" en su lugar. Su
   combinación push/pop retorna el menor de los dos valores, dejando
   el mayor valor en el montículo.

For max-heaps, the following functions are provided:

heapq.heapify_max(x)

   Transform list *x* into a max-heap, in-place, in linear time.

   Added in version 3.14.

heapq.heappush_max(heap, item)

   Push the value *item* onto the max-heap *heap*, maintaining the
   max-heap invariant.

   Added in version 3.14.

heapq.heappop_max(heap)

   Pop and return the largest item from the max-heap *heap*,
   maintaining the max-heap invariant.  If the max-heap is empty,
   "IndexError" is raised. To access the largest item without popping
   it, use "maxheap[0]".

   Added in version 3.14.

heapq.heappushpop_max(heap, item)

   Push *item* on the max-heap *heap*, then pop and return the largest
   item from *heap*. The combined action runs more efficiently than
   "heappush_max()" followed by a separate call to "heappop_max()".

   Added in version 3.14.

heapq.heapreplace_max(heap, item)

   Pop and return the largest item from the max-heap *heap* and also
   push the new *item*. The max-heap size doesn't change. If the max-
   heap is empty, "IndexError" is raised.

   The value returned may be smaller than the *item* added.  Refer to
   the analogous function "heapreplace()" for detailed usage notes.

   Added in version 3.14.

El módulo también ofrece tres funciones de propósito general basadas
en los montículos.

heapq.merge(*iterables, key=None, reverse=False)

   Fusionar varias entradas ordenadas en una sola salida ordenada (por
   ejemplo, fusionar entradas con marca de tiempo de varios archivos
   de registro). Retorna un *iterator* sobre los valores ordenados.

   Similar a "sorted(itertools.chain(*iterables))" pero retorna un
   iterable, no hala los datos a la memoria de una sola vez, y asume
   que cada uno de los flujos de entrada ya están ordenado (de menor a
   mayor).

   Tiene dos argumentos opcionales que deben ser especificados como
   argumentos de palabras clave.

   *key* especifica una *key function* de un argumento que se utiliza
   para extraer una clave de comparación de cada elemento de entrada.
   El valor por defecto es "None" (compara los elementos
   directamente).

   *reverse* es un valor booleano. Si se establece en "True", entonces
   los elementos de entrada se fusionan como si cada comparación se
   invirtiera. Para lograr un comportamiento similar a
   "sorted(itertools.chain(*iterables), reverse=True)", todos los
   iterables deben ser ordenados de mayor a menor.

   Distinto en la versión 3.5: Añadió los parámetros opcionales de
   *key* y *reverse*.

heapq.nlargest(n, iterable, key=None)

   Retorna una lista con los *n* elementos más grandes del conjunto de
   datos definidos por *iterable*. *key*, si se proporciona,
   especifica una función de un argumento que se utiliza para extraer
   una clave de comparación de cada elemento en *iterable* (por
   ejemplo, "key=str.lower"). Equivalente a:  "sorted(iterable,
   key=clave, reverse=True)[:n]".

heapq.nsmallest(n, iterable, key=None)

   Retorna una lista con los *n* elementos más pequeños del conjunto
   de datos definidos por *iterable*. *key*, si se proporciona,
   especifica una función de un argumento que se utiliza para extraer
   una clave de comparación de cada elemento en *iterable* (por
   ejemplo, "key=str.lower"). Equivalente a:  "sorted(iterable,
   key=clave)[:n]".

Las dos últimas funciones funcionan mejor para valores más pequeños de
*n*. Para valores más grandes, es más eficiente usar la función
"sorted()". Además, cuando "n==1", es más eficiente usar las funciones
incorporadas "min()" y "max`()". Si se requiere el uso repetido de
estas funciones, considere convertir lo iterable en un verdadero
montículo.

## Ejemplos Básicos

Un heapsort" puede ser implementado empujando todos los valores en un
montículo y luego desapilando los valores más pequeños uno a la vez:

   >>> def heapsort(iterable):
   ...     h = []
   ...     for value in iterable:
   ...         heappush(h, value)
   ...     return [heappop(h) for i in range(len(h))]
   ...
   >>> heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Esto es similar a "sorted(iterable)", pero a diferencia de "sorted()",
esta implementación no es estable.

Los elementos del montículo pueden ser tuplas. Esto es útil para
asignar valores de comparación (como las prioridades de las tareas)
junto con el registro principal que se está rastreando:

   >>> h = []
   >>> heappush(h, (5, 'write code'))
   >>> heappush(h, (7, 'release product'))
   >>> heappush(h, (1, 'write spec'))
   >>> heappush(h, (3, 'create tests'))
   >>> heappop(h)
   (1, 'write spec')

## Other Applications

Medians are a measure of central tendency for a set of numbers.  In
distributions skewed by outliers, the median provides a more stable
estimate than an average (arithmetic mean).  A running median is an
online algorithm that updates continuously as new data arrives.

A running median can be efficiently implemented by balancing two
heaps, a max-heap for values at or below the midpoint and a min-heap
for values above the midpoint.  When the two heaps have the same size,
the new median is the average of the tops of the two heaps; otherwise,
the median is at the top of the larger heap:

   def running_median(iterable):
       "Yields the cumulative median of values seen so far."

       lo = []  # max-heap
       hi = []  # min-heap (same size as or one smaller than lo)

       for x in iterable:
           if len(lo) == len(hi):
               heappush_max(lo, heappushpop(hi, x))
               yield lo[0]
           else:
               heappush(hi, heappushpop_max(lo, x))
               yield (lo[0] + hi[0]) / 2

For example:

   >>> list(running_median([5.0, 9.0, 4.0, 12.0, 8.0, 9.0]))
   [5.0, 7.0, 5.0, 7.0, 8.0, 8.5]

## Notas de Aplicación de la Cola de Prioridades

Una cola de prioridad es de uso común para un montículo, y presenta
varios desafíos de implementación:

* Estabilidad de la clasificación: ¿cómo se consigue que dos tareas
  con iguales prioridades sean retornadas en el orden en que fueron
  añadidas originalmente?

* Interrupciones de comparación en tupla para pares (prioridad, tarea)
  si las prioridades son iguales y las tareas no tienen un orden de
  comparación por defecto.

* ¿Si la prioridad de una tarea cambia, cómo la mueves a una nueva
  posición en el montículo?

* ¿O si una tarea pendiente necesita ser borrada, cómo la encuentras y
  la eliminas de la cola?

Una solución a los dos primeros desafíos es almacenar las entradas
como una lista de 3 elementos que incluya la prioridad, un recuento de
entradas y la tarea. El recuento de entradas sirve como un desempate
para que dos tareas con la misma prioridad sean retornadas en el orden
en que fueron añadidas. Y como no hay dos recuentos de entradas
iguales, la comparación tupla nunca intentará comparar directamente
dos tareas.

Otra solución al problema de las tareas no comparables es crear una
clase envolvente que ignore el elemento de la tarea y sólo compare el
campo de prioridad:

   from dataclasses import dataclass, field
   from typing import Any

   @dataclass(order=True)
   class PrioritizedItem:
       priority: int
       item: Any=field(compare=False)

Los desafíos restantes giran en torno a encontrar una tarea pendiente
y hacer cambios en su prioridad o eliminarla por completo. Encontrar
una tarea se puede hacer con un diccionario que apunta a una entrada
en la cola.

Eliminar la entrada o cambiar su prioridad es más difícil porque
rompería las invariantes de la estructura del montículo. Por lo tanto,
una posible solución es marcar la entrada como eliminada y añadir una
nueva entrada con la prioridad revisada:

   pq = []                         # list of entries arranged in a heap
   entry_finder = {}               # mapping of tasks to entries
   REMOVED = '<removed-task>'      # placeholder for a removed task
   counter = itertools.count()     # unique sequence count

   def add_task(task, priority=0):
       'Add a new task or update the priority of an existing task'
       if task in entry_finder:
           remove_task(task)
       count = next(counter)
       entry = [priority, count, task]
       entry_finder[task] = entry
       heappush(pq, entry)

   def remove_task(task):
       'Mark an existing task as REMOVED.  Raise KeyError if not found.'
       entry = entry_finder.pop(task)
       entry[-1] = REMOVED

   def pop_task():
       'Remove and return the lowest priority task. Raise KeyError if empty.'
       while pq:
           priority, count, task = heappop(pq)
           if task is not REMOVED:
               del entry_finder[task]
               return task
       raise KeyError('pop from an empty priority queue')

## Teoría

Los montículos son conjuntos para los cuales "a[k] <= a[2*k+1]" y
"a[k] <= a[2*k+2]" para todos los *k*, contando los elementos desde 0.
Para comparar, los elementos no existentes se consideran infinitos. La
interesante propiedad de un montículo es que "a[0]" es siempre su
elemento más pequeño.

La extraña invariante de arriba intenta ser una representación
eficiente de la memoria para un torneo. Los números de abajo son *k*,
no "a[k]":

                                  0

                 1                                 2

         3               4                5               6

     7       8       9       10      11      12      13      14

   15 16   17 18   19 20   21 22   23 24   25 26   27 28   29 30

En el árbol de arriba, cada celda *k* está coronada por "2*k+1" y
"2*k+2". En un torneo binario habitual que vemos en los deportes, cada
celda es el ganador sobre las dos celdas que supera, y podemos
rastrear al ganador hasta el árbol para ver todos los oponentes que
tuvo. Sin embargo, en muchas aplicaciones informáticas de tales
torneos, no necesitamos rastrear la historia de un ganador. Para ser
más eficientes en la memoria, cuando un ganador es ascendido, tratamos
de reemplazarlo por algo más en un nivel inferior, y la regla se
convierte en que una celda y las dos celdas que supera contienen tres
elementos diferentes, pero la celda superior "gana" sobre las dos
celdas superiores.

If this heap invariant is protected at all time, index 0 is clearly
the overall winner.  The simplest algorithmic way to remove it and
find the "next" winner is to move some loser (let's say cell 30 in the
diagram above) into the 0 position, and then percolate this new 0 down
the tree, exchanging values, until the invariant is re-established.
This is clearly logarithmic on the total number of items in the tree.
By iterating over all items, you get an *O*(*n* log *n*) sort.

Una buena característica de este tipo es que puedes insertar nuevos
elementos de manera eficiente mientras se realiza la clasificación,
siempre y cuando los elementos insertados no sean "mejores" que el
último 0'th elemento que has extraído. Esto es especialmente útil en
contextos de simulación, donde el árbol contiene todos los eventos
entrantes, y la condición de "ganar" significa el menor tiempo
programado. Cuando un evento programa otros eventos para su ejecución,
se programan en el futuro, para que puedan ir fácilmente al montículo.
Por lo tanto, un montículo es una buena estructura para implementar
planificadores o *schedulers* (esto es lo que usé para mi secuenciador
MIDI :-).

Se han estudiado extensamente varias estructuras para implementar los
planificadores, y los montículos son buenos para ello, ya que son
razonablemente rápidos, la velocidad es casi constante, y el peor de
los casos no es muy diferente del caso promedio. Sin embargo, hay
otras representaciones que son más eficientes en general, aunque los
peores casos podrían ser terribles.

Los montículos también son muy útiles en las grandes  ordenaciones de
elementos en discos de memoria. Lo más probable es que todos sepan que
un tipo grande implica la producción de "ejecuciones" (que son
secuencias preclasificadas, cuyo tamaño suele estar relacionado con la
cantidad de memoria de la CPU), seguidas de una fusión de pases para
estas ejecuciones, cuya fusión suele estar muy inteligentemente
organizada [1]. Es muy importante que la clasificación inicial
produzca las ejecuciones posibles más largas. Los torneos son una
buena manera de lograrlo. Si, utilizando toda la memoria disponible
para celebrar un torneo, sustituyes y filtras los elementos que
encajan en la carrera actual, producirás carreras que tienen el doble
del tamaño de la memoria para la entrada aleatoria, y mucho mejor para
la entrada ordenada de forma difusa.

Además, si se da salida al *0’th item* en el disco y se obtiene una
entrada que no puede caber en el torneo actual (porque el valor "gana"
sobre el último valor de salida), no puede caber en el montículo, por
lo que el tamaño del montículo disminuye. La memoria liberada podría
ser ingeniosamente reutilizada inmediatamente para construir
progresivamente un segundo montículo, que crece exactamente al mismo
ritmo que el primer montículo se está fundiendo. Cuando el primer
montículo se desvanece completamente, se cambia de montículo y se
inicia una nueva carrera. ¡Ingenioso y muy efectivo!

En una palabra, los montículos son estructuras de memoria útiles a
conocer. Las uso en algunas aplicaciones, y creo que es bueno tener un
módulo 'heap' alrededor. :-)

-[ Notas al pie de página ]-

[1] Los algoritmos de balanceo de discos que están vigentes hoy en
    día, son más molestos que inteligentes, y esto es una consecuencia
    de las capacidades de búsqueda de los discos. En los dispositivos
    que no pueden buscar, como las grandes unidades de cinta, la
    historia era muy diferente, y había que ser muy inteligente para
    asegurarse (con mucha antelación) de que cada movimiento de la
    cinta fuera el más efectivo (es decir, que participara mejor en el
    "progreso" de la fusión). Algunas cintas eran incluso capaces de
    leer al revés, y esto también se utilizó para evitar el tiempo
    rebobinado. Créanme, ¡la ordenación de elementos en cinta
    realmente buenos fueron espectaculares de ver! ¡Desde todos los
    tiempos, la ordenación de elementos siempre ha sido un Gran Arte!
    :-)
