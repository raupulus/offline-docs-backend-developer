---
title: '"bisect" --- Array bisection algorithm'
source_url: https://docs.python.org/es/3
source_path: library/bisect.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1860
---

# "bisect" --- Array bisection algorithm

**Código fuente:** Lib/bisect.py

======================================================================

Este módulo brinda soporte para mantener una lista ordenada sin tener
que reordenar la lista tras cada nueva inserción. Para listas largas
de elementos que tienen operaciones de comparación costosas, esto
puede suponer una mejora con respecto a las búsquedas lineales o el
reordenado frecuente.

The module is called "bisect" because it uses a basic bisection
algorithm to do its work.  Unlike other bisection tools that search
for a specific value, the functions in this module are designed to
locate an insertion point. Accordingly, the functions never call an
"__eq__()" method to determine whether a value has been found.
Instead, the functions only call the "__lt__()" method and will return
an insertion point between values in an array.

Nota:

  The functions in this module are not thread-safe. If multiple
  threads concurrently use "bisect" functions on the same sequence,
  this may result in undefined behaviour. Likewise, if the provided
  sequence is mutated by a different thread while a "bisect" function
  is operating on it, the result is undefined. For example, using
  "insort_left()" on the same list from multiple threads may result in
  the list becoming unsorted.

Las siguientes funciones están disponibles:

bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)

   Ubicar el punto de inserción para *x* en *a* para mantener el
   ordenamiento. Los parámetros *lo* (inferior) y *hi* (superior)
   pueden utilizarse para especificar un subconjunto de la lista que
   debería considerarse; por defecto se utiliza la lista completa. Si
   *x* ya está presente en *a*, el punto de inserción será antes (a la
   izquierda) de cualquier elemento existente. El valor de retorno es
   adecuado para que se utilice como primer parámetro para
   "list.insert()", suponiendo que *a* ya está ordenada.

   El punto de inserción retornado *ip* divide el arreglo *a* en dos
   partes, de modo que "all(elem < x for elem in a[lo : ip])" es
   verdadero para el lado izquierdo y "all(elem >= x for elem in a[ip
   : hi])" es verdadero para el lado derecho.

   *key* especifica una *función clave* de un argumento que es usada
   para extraer una clave de comparación de cada elemento en el
   arreglo. La función clave no se aplica a *x* para facilitar la
   búsqueda de registros complejos.

   Si *key* es "None", los elementos se comparan directamente y
   ninguna función clave es llamada.

   Distinto en la versión 3.10: Se agregó el parámetro *key*.

bisect.bisect_right(a, x, lo=0, hi=len(a), *, key=None)
bisect.bisect(a, x, lo=0, hi=len(a), *, key=None)

   Similar a "bisect_left()", pero retorna un punto de inserción que
   viene después (a la derecha) de cualquier entrada existente de *x*
   en *a*.

   El punto de inserción retornado *ip* divide el arreglo *a* en dos
   partes, de modo que "all(elem  <= x for elem in a[lo : ip])" es
   verdadero para el lado izquierdo y "all(elem > x for elem in a[ip :
   hi])" es verdadero para el lado derecho.

   Distinto en la versión 3.10: Se agregó el parámetro *key*.

bisect.insort_left(a, x, lo=0, hi=len(a), *, key=None)

   Inserte *x* en *a* en orden ordenado.

   This function first runs "bisect_left()" to locate an insertion
   point. Next, it runs the "insert()" method on *a* to insert *x* at
   the appropriate position to maintain sort order.

   Para mantener la inserción de registros en una tabla, la función
   *key* (en caso de existir) se aplica a *x* en el paso de búsqueda
   pero no en el paso de inserción.

   Keep in mind that the *O*(log *n*) search is dominated by the slow
   *O*(*n*) insertion step.

   Distinto en la versión 3.10: Se agregó el parámetro *key*.

bisect.insort_right(a, x, lo=0, hi=len(a), *, key=None)
bisect.insort(a, x, lo=0, hi=len(a), *, key=None)

   Similar a "insort_left()", pero inserta *x* en *a* después de
   cualquier entrada de *x* existente.

   This function first runs "bisect_right()" to locate an insertion
   point. Next, it runs the "insert()" method on *a* to insert *x* at
   the appropriate position to maintain sort order.

   Para mantener la inserción de registros en una tabla, la función
   *key* (en caso de existir) se aplica a *x* en el paso de búsqueda
   pero no en el paso de inserción.

   Keep in mind that the *O*(log *n*) search is dominated by the slow
   *O*(*n*) insertion step.

   Distinto en la versión 3.10: Se agregó el parámetro *key*.

## Notas de rendimiento

Al escribir código sensible al tiempo usando *bisect()* y *insort()*,
tenga en cuenta estos pensamientos:

* La bisección es eficaz para buscar rangos de valores. Para localizar
  valores específicos, los diccionarios son más eficaces.

* The *insort()* functions are *O*(*n*) because the logarithmic search
  step is dominated by the linear time insertion step.

* The search functions are stateless and discard key function results
  after they are used.  Consequently, if the search functions are used
  in a loop, the key function may be called again and again on the
  same array elements. If the key function isn't fast, consider
  wrapping it with "@functools.cache" to avoid duplicate computations.
  Alternatively, consider searching an array of precomputed keys to
  locate the insertion point (as shown in the examples section below).

Ver también:

  * Sorted Collections es un módulo de alto rendimiento que utiliza
    *bisect* para gestionar colecciones de datos ordenadas.

  * El SortedCollection recipe usa bisect para construir una clase de
    colección con todas las funciones con métodos de búsqueda
    sencillos y soporte para una función clave. Las claves se calculan
    previamente para ahorrar llamadas innecesarias a la función clave
    durante las búsquedas.

## Búsqueda en listas ordenadas

Las bisect functions anteriores son útiles para encontrar puntos de
inserción, pero pueden resultar difíciles o engorrosas para tareas de
búsqueda habituales. Las siguientes cinco funciones muestran cómo
convertirlas en búsquedas estándar para listas ordenadas:

   def index(a, x):
       'Locate the leftmost value exactly equal to x'
       i = bisect_left(a, x)
       if i != len(a) and a[i] == x:
           return i
       raise ValueError

   def find_lt(a, x):
       'Find rightmost value less than x'
       i = bisect_left(a, x)
       if i:
           return a[i-1]
       raise ValueError

   def find_le(a, x):
       'Find rightmost value less than or equal to x'
       i = bisect_right(a, x)
       if i:
           return a[i-1]
       raise ValueError

   def find_gt(a, x):
       'Find leftmost value greater than x'
       i = bisect_right(a, x)
       if i != len(a):
           return a[i]
       raise ValueError

   def find_ge(a, x):
       'Find leftmost item greater than or equal to x'
       i = bisect_left(a, x)
       if i != len(a):
           return a[i]
       raise ValueError

## Ejemplos

La función "bisect()" puede ser útil para búsquedas en tablas
numéricas. Este ejemplo utiliza "bisect()" para buscar una
calificación de un examen (digamos) dada por una letra, basándose en
un conjunto de punto de corte numéricos ordenados: 90 o más es una
'A', de 80 a 89 es una 'B', y así sucesivamente:

   >>> def grade(score):
   ...     i = bisect([60, 70, 80, 90], score)
   ...     return "FDCBA"[i]
   ...
   >>> [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
   ['F', 'A', 'C', 'C', 'B', 'A', 'A']

Las funciones "bisect()" y "insort()" también funcionan con listas de
tuplas. El argumento *key* puede usarse para extraer el campo usado
para ordenar registros en una tabla:

   >>> from collections import namedtuple
   >>> from operator import attrgetter
   >>> from bisect import bisect, insort
   >>> from pprint import pprint

   >>> Movie = namedtuple('Movie', ('name', 'released', 'director'))

   >>> movies = [
   ...     Movie('Jaws', 1975, 'Spielberg'),
   ...     Movie('Titanic', 1997, 'Cameron'),
   ...     Movie('The Birds', 1963, 'Hitchcock'),
   ...     Movie('Aliens', 1986, 'Cameron')
   ... ]

   >>> # Find the first movie released after 1960
   >>> by_year = attrgetter('released')
   >>> movies.sort(key=by_year)
   >>> movies[bisect(movies, 1960, key=by_year)]
   Movie(name='The Birds', released=1963, director='Hitchcock')

   >>> # Insert a movie while maintaining sort order
   >>> romance = Movie('Love Story', 1970, 'Hiller')
   >>> insort(movies, romance, key=by_year)
   >>> pprint(movies)
   [Movie(name='The Birds', released=1963, director='Hitchcock'),
    Movie(name='Love Story', released=1970, director='Hiller'),
    Movie(name='Jaws', released=1975, director='Spielberg'),
    Movie(name='Aliens', released=1986, director='Cameron'),
    Movie(name='Titanic', released=1997, director='Cameron')]

Para evitar llamadas repetidas a la función clave, cuando ésta usa
muchos recursos, se puede buscar en una lista de claves previamente
calculadas para encontrar el índice de un registro:

   >>> data = [('red', 5), ('blue', 1), ('yellow', 8), ('black', 0)]
   >>> data.sort(key=lambda r: r[1])       # Or use operator.itemgetter(1).
   >>> keys = [r[1] for r in data]         # Precompute a list of keys.
   >>> data[bisect_left(keys, 0)]
   ('black', 0)
   >>> data[bisect_left(keys, 1)]
   ('blue', 1)
   >>> data[bisect_left(keys, 5)]
   ('red', 5)
   >>> data[bisect_left(keys, 8)]
   ('yellow', 8)
