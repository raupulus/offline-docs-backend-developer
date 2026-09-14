---
title: '"collections" --- Container datatypes'
source_url: https://docs.python.org/es/3
source_path: library/collections.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2010
---

# "collections" --- Container datatypes

**Source code:** Lib/collections/__init__.py

======================================================================

Este módulo implementa tipos de datos de contenedores especializados
que proporcionan alternativas a los contenedores integrados de uso
general de Python, "dict", "list", "set", and "tuple".

+-----------------------+----------------------------------------------------------------------+
| "namedtuple()"        | función *factory* para crear subclases de *tuplas* con campos con    |
## |                       | nombre                                                               |

| "deque"               | contenedor similar a una lista con *appends* y *pops* rápidos en     |
## |                       | ambos extremos                                                       |

| "ChainMap"            | clase similar a *dict* para crear una vista única de múltiples       |
## |                       | *mapeados*                                                           |

## | "Counter"             | subclase de *dict* para contar objetos *hashable*                    |

| "OrderedDict"         | subclase de *dict* que recuerda las entradas de la orden que se      |
## |                       | agregaron                                                            |

| "defaultdict"         | subclase de *dict* que llama a una función de *factory* para         |
## |                       | suministrar valores faltantes                                        |

| "UserDict"            | envoltura alrededor de los objetos de diccionario para facilitar     |
## |                       | subclasificaciones *dict*                                            |

| "UserList"            | envoltura alrededor de los objetos de lista para facilitar la        |
## |                       | subclasificación de un *list*                                        |

| "UserString"          | envoltura alrededor de objetos de cadena para facilitar la           |
## |                       | subclasificación de *string*                                         |

## Objetos "ChainMap"

Added in version 3.3.

Una clase "ChainMap" se proporciona para vincular rápidamente una
serie de *mappings* de modo que puedan tratarse como una sola unidad.
Suele ser mucho más rápido que crear un diccionario nuevo y ejecutar
varias llamadas a "update()".

La clase se puede utilizar para simular ámbitos anidados y es útil
para crear plantillas.

class collections.ChainMap(*maps)

   Un "ChainMap" agrupa varios diccionarios u otros *mappings* para
   crear una vista única y actualizable. Si no se especifican *maps*,
   se proporciona un solo diccionario vacío para que una nueva cadena
   siempre tenga al menos un *mapeo*.

   Las asignaciones subyacentes se almacenan en una lista. Esa lista
   es pública y se puede acceder a ella o actualizarla usando el
   atributo *maps*. No hay otro estado.

   Las búsquedas buscan los mapeos subyacentes sucesivamente hasta que
   se encuentra una clave. Por el contrario, las escrituras,
   actualizaciones y eliminaciones solo operan en el primer *mapeo*.

   Un "ChainMap" incorpora los mapeos subyacentes por referencia.
   Entonces, si una de los mapeos subyacentes se actualiza, esos
   cambios se reflejarán en "ChainMap".

   Se admiten todos los métodos habituales de un diccionario. Además,
   hay un atributo *maps*, un método para crear nuevos sub contextos y
   una propiedad para acceder a todos menos al primer mapeo:

   maps

      Una lista de mapeos actualizable por el usuario. La lista está
      ordenada desde la primera búsqueda hasta la última búsqueda. Es
      el único estado almacenado y se puede modificar para cambiar los
      mapeos que se buscan. La lista siempre debe contener al menos un
      mapeo.

   new_child(m=None, **kwargs)

      Retorna un nuevo "ChainMap" conteniendo un nuevo mapa seguido de
      todos los mapas de la instancia actual.  Si se especifica "m",
      se convierte en el nuevo mapa al principio de la lista de
      asignaciones; si no se especifica, se usa un diccionario vacío,
      de modo que una llamada a "d.new_child()" es equivalente a:
      "ChainMap({}, *d.maps)". Si se especifica algún argumento de
      palabra clave, actualiza el mapa pasado o el nuevo diccionario
      vacío. Este método se utiliza para crear sub contextos que se
      pueden actualizar sin alterar los valores en ninguna de los
      mapeos padre.

      Distinto en la versión 3.4: Se agregó el parámetro opcional "m"
      .

      Distinto en la versión 3.10: Se añadió soporte para argumentos
      por palabras clave.

   parents

      Propiedad que retorna un nuevo "ChainMap" conteniendo todos los
      mapas de la instancia actual excepto el primero.  Esto es útil
      para omitir el primer mapa en la búsqueda.  Los casos de uso son
      similares a los de "nonlocal" la palabra clave usada en
      *alcances anidados*.  Los casos de uso también son paralelos a
      los de la función incorporada "super()".  Una referencia a
      "d.parents" es equivalente a: "ChainMap(*d.maps[1:])".

   Note, the iteration order of a "ChainMap" is determined by scanning
   the mappings last to first:

      >>> baseline = {'music': 'bach', 'art': 'rembrandt'}
      >>> adjustments = {'art': 'van gogh', 'opera': 'carmen'}
      >>> list(ChainMap(adjustments, baseline))
      ['music', 'art', 'opera']

   Esto da el mismo orden que una serie de llamadas a "dict.update()"
   comenzando con el último mapeo:

      >>> combined = baseline.copy()
      >>> combined.update(adjustments)
      >>> list(combined)
      ['music', 'art', 'opera']

   Distinto en la versión 3.9: Se agregó soporte para los operadores
   "|" y "|=", especificados en **PEP 584**.

Ver también:

  * La clase MultiContext en el paquete de Enthought llamado CodeTools
    tiene opciones para admitir la escritura en cualquier mapeo de la
    cadena.

  * La clase de Django Context para crear plantillas es una cadena de
    mapeo de solo lectura. También presenta características de pushing
    y popping de contextos similar al método "new_child()" y a la
    propiedad "parents" .

  * The Nested Contexts recipe has options to control whether writes
    and other mutations apply only to the first mapping or to any
    mapping in the chain.

  * Una versión de solo lectura muy simplificada de Chainmap.

### Ejemplos y recetas "ChainMap"

Esta sección muestra varios enfoques para trabajar con mapas
encadenados.

Ejemplo de simulación de la cadena de búsqueda interna de Python:

   import builtins
   pylookup = ChainMap(locals(), globals(), vars(builtins))

Ejemplo de dejar que los argumentos de la línea de comandos
especificados por el usuario tengan prioridad sobre las variables de
entorno que, a su vez, tienen prioridad sobre los valores
predeterminados:

   import os, argparse

   defaults = {'color': 'red', 'user': 'guest'}

   parser = argparse.ArgumentParser()
   parser.add_argument('-u', '--user')
   parser.add_argument('-c', '--color')
   namespace = parser.parse_args()
   command_line_args = {k: v for k, v in vars(namespace).items() if v is not None}

   combined = ChainMap(command_line_args, os.environ, defaults)
   print(combined['color'])
   print(combined['user'])

Patrones de ejemplo para usar la clase "ChainMap" para simular
contextos anidados:

   c = ChainMap()        # Create root context
   d = c.new_child()     # Create nested child context
   e = c.new_child()     # Child of c, independent from d
   e.maps[0]             # Current context dictionary -- like Python's locals()
   e.maps[-1]            # Root context -- like Python's globals()
   e.parents             # Enclosing context chain -- like Python's nonlocals

   d['x'] = 1            # Set value in current context
   d['x']                # Get first key in the chain of contexts
   del d['x']            # Delete from current context
   list(d)               # All nested values
   k in d                # Check all nested values
   len(d)                # Number of nested values
   d.items()             # All nested items
   dict(d)               # Flatten into a regular dictionary

La clase "ChainMap" solo realiza actualizaciones (escrituras y
eliminaciones) en el primer mapeo de la cadena, mientras que las
búsquedas buscarán en la cadena completa. Sin embargo, si se desean
escrituras y eliminaciones profundas, es fácil crear una subclase que
actualice las claves que se encuentran más profundas en la cadena:

   class DeepChainMap(ChainMap):
       'Variant of ChainMap that allows direct updates to inner scopes'

       def __setitem__(self, key, value):
           for mapping in self.maps:
               if key in mapping:
                   mapping[key] = value
                   return
           self.maps[0][key] = value

       def __delitem__(self, key):
           for mapping in self.maps:
               if key in mapping:
                   del mapping[key]
                   return
           raise KeyError(key)

   >>> d = DeepChainMap({'zebra': 'black'}, {'elephant': 'blue'}, {'lion': 'yellow'})
   >>> d['lion'] = 'orange'         # update an existing key two levels down
   >>> d['snake'] = 'red'           # new keys get added to the topmost dict
   >>> del d['elephant']            # remove an existing key one level down
   >>> d                            # display result
   DeepChainMap({'zebra': 'black', 'snake': 'red'}, {}, {'lion': 'orange'})

## Objetos "Counter"

Se proporciona una herramienta de contador para respaldar recuentos
rápidos y convenientes. Por ejemplo:

   >>> # Tally occurrences of words in a list
   >>> cnt = Counter()
   >>> for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
   ...     cnt[word] += 1
   ...
   >>> cnt
   Counter({'blue': 3, 'red': 2, 'green': 1})

   >>> # Find the ten most common words in Hamlet
   >>> import re
   >>> words = re.findall(r'\w+', open('hamlet.txt').read().lower())
   >>> Counter(words).most_common(10)
   [('the', 1143), ('and', 966), ('to', 762), ('of', 669), ('i', 631),
    ('you', 554),  ('a', 546), ('my', 514), ('hamlet', 471), ('in', 451)]

class collections.Counter(**kwargs)
class collections.Counter(iterable, /, **kwargs)
class collections.Counter(mapping, /, **kwargs)

   Una clase "Counter" es una subclase "dict" para contar objetos
   *hashable*. Es una colección donde los elementos se almacenan como
   claves de diccionario y sus conteos se almacenan como valores de
   diccionario. Se permite que los conteos sean cualquier valor
   entero, incluidos los conteos de cero o negativos. La clase
   "Counter" es similar a los *bags* o multiconjuntos en otros
   idiomas.

   Los elementos se cuentan desde un *iterable* o se inicializan desde
   otro *mapeo* (o contador):

   >>> c = Counter()                           # a new, empty counter
   >>> c = Counter('gallahad')                 # a new counter from an iterable
   >>> c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
   >>> c = Counter(cats=4, dogs=8)             # a new counter from keyword args

   Los objetos Counter tienen una interfaz de diccionario, excepto que
   retornan un conteo de cero para los elementos faltantes en lugar de
   levantar una "KeyError":

   >>> c = Counter(['eggs', 'ham'])
   >>> c['bacon']                              # count of a missing element is zero
   0

   Establecer un conteo en cero no elimina un elemento de un contador.
   Utilice "del" para eliminarlo por completo:

   >>> c['sausage'] = 0                        # counter entry with a zero count
   >>> del c['sausage']                        # del actually removes the entry

   Added in version 3.1.

   Distinto en la versión 3.7: Como subclase de "dict" , "Counter"
   heredó la capacidad de recordar el orden de inserción. Las
   operaciones matemáticas en objetos *Counter* también preservan el
   orden. Los resultados se ordenan en función de cuándo se encuentra
   un elemento por primera vez en el operando izquierdo y, a
   continuación, por el orden en que se encuentra en el operando
   derecho.

   Los objetos Counter admiten métodos adicionales a los disponibles
   para todos los diccionarios:

   elements()

      Retorna un iterador sobre los elementos que se repiten tantas
      veces como su conteo. Los elementos se retornan en el orden en
      que se encontraron por primera vez. Si el conteo de un elemento
      es menor que uno, "elements()" lo ignorará.

      >>> c = Counter(a=4, b=2, c=0, d=-2)
      >>> sorted(c.elements())
      ['a', 'a', 'a', 'a', 'b', 'b']

   most_common(n=None)

      Retorna una lista de los *n* elementos mas comunes y sus
      conteos, del mas común al menos común. Si se omite *n* o "None",
      "most_common()" retorna *todos* los elementos del contador. Los
      elementos con conteos iguales se ordenan en el orden en que se
      encontraron por primera vez:

      >>> Counter('abracadabra').most_common(3)
      [('a', 5), ('b', 2), ('r', 2)]

   subtract(**kwargs)
   subtract(iterable, /, **kwargs)
   subtract(mapping, /, **kwargs)

      Los elementos se restan de un *iterable* o de otro *mapeo* (o
      contador). Como "dict.update()" pero resta los conteos en lugar
      de reemplazarlos. Tanto las entradas como las salidas pueden ser
      cero o negativas.

      >>> c = Counter(a=4, b=2, c=0, d=-2)
      >>> d = Counter(a=1, b=2, c=3, d=4)
      >>> c.subtract(d)
      >>> c
      Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

      Added in version 3.2.

   total()

      Computa la suma de las cuentas.

      >>> c = Counter(a=10, b=5, c=0)
      >>> c.total()
      15

      Added in version 3.10.

   Los métodos de diccionario habituales están disponibles para
   objetos "Counter" excepto dos que funcionan de manera diferente
   para los contadores.

   fromkeys(iterable)

      Este método de clase no está implementado para objetos "Counter"
      .

   update(**kwargs)
   update(iterable, /, **kwargs)
   update(mapping, /, **kwargs)

      Los elementos se cuentan desde un *iterable* o agregados desde
      otro *mapeo* (o contador). Como "dict.update()" pero agrega
      conteos en lugar de reemplazarlos. Además, se espera que el
      *iterable* sea una secuencia de elementos, no una secuencia de
      parejas "(clave, valor)" .

Los contadores admiten operadores de comparación ricos para las
relaciones de igualdad, subconjunto, y superconjunto: "==", "!=", "<",
"<=", ">", ">=". Todas esas pruebas tratan los elementos faltantes
como si tuvieran cero recuentos, por lo que "Counter(a=1) ==
Counter(a=1, b=0)" retorne verdadero.

Distinto en la versión 3.10: Se han añadido operaciones de comparación
enriquecidas.

Distinto en la versión 3.10: En pruebas de igualdad, los elementos
faltantes son tratados como si tuvieran cero recuentos. Anteriormente,
"Counter(a=3)" y "Counter(a=3, b=0)" se consideraban distintos.

Patrones comunes para trabajar con objetos "Counter":

   c.total()                       # total of all counts
   c.clear()                       # reset all counts
   list(c)                         # list unique elements
   set(c)                          # convert to a set
   dict(c)                         # convert to a regular dictionary
   c.items()                       # access the (elem, cnt) pairs
   Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
   c.most_common()[:-n-1:-1]       # n least common elements
   +c                              # remove zero and negative counts

Existen varias operaciones matemáticas que permiten combinar objetos
"Counter" para producir conjuntos múltiples (contadores con recuentos
superiores a cero). La suma y la resta combinan contadores sumando o
restando los recuentos de los elementos correspondientes.  La
intersección y la unión retornan el mínimo y el máximo de los
recuentos correspondientes.  La igualdad y la inclusión comparan los
recuentos correspondientes.  Cada operación puede aceptar entradas con
recuentos con signo, pero la salida excluirá los resultados con
recuentos iguales o inferiores a cero.

   >>> c = Counter(a=3, b=1)
   >>> d = Counter(a=1, b=2)
   >>> c + d                       # add two counters together:  c[x] + d[x]
   Counter({'a': 4, 'b': 3})
   >>> c - d                       # subtract (keeping only positive counts)
   Counter({'a': 2})
   >>> c & d                       # intersection:  min(c[x], d[x])
   Counter({'a': 1, 'b': 1})
   >>> c | d                       # union:  max(c[x], d[x])
   Counter({'a': 3, 'b': 2})
   >>> c == d                      # equality:  c[x] == d[x]
   False
   >>> c <= d                      # inclusion:  c[x] <= d[x]
   False

La suma y resta unaria son atajos para agregar un contador vacío o
restar de un contador vacío.

>>> c = Counter(a=2, b=-4)
>>> +c
Counter({'a': 2})
>>> -c
Counter({'b': 4})

Added in version 3.3: Se agregó soporte para operaciones unarias de
adición, resta y multiconjunto en su lugar (*in-place*).

Nota:

  Los Counters se diseñaron principalmente para trabajar con números
  enteros positivos para representar conteos continuos; sin embargo,
  se tuvo cuidado de no excluir innecesariamente los casos de uso que
  necesitan otros tipos o valores negativos. Para ayudar con esos
  casos de uso, esta sección documenta el rango mínimo y las
  restricciones de tipo.

  * La clase "Counter" en sí misma es una subclase de diccionario sin
    restricciones en sus claves y valores. Los valores están pensados
    para ser números que representan conteos, pero *podría* almacenar
    cualquier cosa en el campo de valor.

  * El método "most_common()" solo requiere que los valores se puedan
    ordenar.

  * Para operaciones en su lugar (*in-place*) como "c[key] += 1", el
    tipo de valor solo necesita admitir la suma y la resta. Por lo
    tanto, las fracciones, flotantes y decimales funcionarían y se
    admiten valores negativos. Lo mismo ocurre con "update()" y
    "subtract()" que permiten valores negativos y cero para las
    entradas y salidas.

  * Los métodos de multiconjuntos están diseñados solo para casos de
    uso con valores positivos. Las entradas pueden ser negativas o
    cero, pero solo se crean salidas con valores positivos. No hay
    restricciones de tipo, pero el tipo de valor debe admitir la suma,
    la resta y la comparación.

  * El método "elements()" requiere conteos enteros. Ignora los
    conteos de cero y negativos.

Ver también:

  * Clase Bag en Smalltalk.

  * Entrada de Wikipedia para Multiconjuntos.

  * Tutorial de multiconjuntos de C++ con ejemplos.

  * Para operaciones matemáticas en multiconjuntos y sus casos de uso,
    consulte *Knuth, Donald. The Art of Computer Programming Volume
    II, Sección 4.6.3, Ejercicio 19*.

  * Para enumerar todos los distintos multiconjuntos de un tamaño dado
    sobre un conjunto dado de elementos, consulte
    "itertools.combinations_with_replacement()":

       map(Counter, combinations_with_replacement('ABC', 2)) # --> AA AB AC BB BC CC

## Objetos "deque"

class collections.deque([iterable[, maxlen]])

   Retorna un nuevo objeto deque inicializado de izquierda a derecha
   (usando "append()") con datos de *iterable*. Si no se especifica
   *iterable*, el nuevo deque estará vacío.

   Deques are a generalization of stacks and queues (the name is
   pronounced "deck" and is short for "double-ended queue").  Deques
   support thread-safe, memory efficient appends and pops from either
   side of the deque with approximately the same *O*(1) performance in
   either direction.

   Though "list" objects support similar operations, they are
   optimized for fast fixed-length operations and incur *O*(*n*)
   memory movement costs for "pop(0)" and "insert(0, v)" operations
   which change both the size and position of the underlying data
   representation.

   Si no se especifica *maxlen* o es "None", los deques pueden crecer
   hasta una longitud arbitraria. De lo contrario, el deque está
   limitado a la longitud máxima especificada. Una vez que un deque de
   longitud limitada esta lleno, cuando se agregan nuevos elementos,
   se descarta el número correspondiente de elementos del extremo
   opuesto. Los deques de longitud limitada proporcionan una
   funcionalidad similar al filtro "tail" en Unix. También son útiles
   para rastrear transacciones y otros grupos de datos donde solo la
   actividad más reciente es de interés.

   Deques are generic over the type of their contents.

   Los objetos deque admiten los siguientes métodos:

   append(item, /)

      Add *item* to the right side of the deque.

   appendleft(item, /)

      Add *item* to the left side of the deque.

   clear()

      Retire todos los elementos del deque dejándolo con longitud 0.

   copy()

      Crea una copia superficial del deque.

      Added in version 3.5.

   count(value, /)

      Count the number of deque elements equal to *value*.

      Added in version 3.2.

   extend(iterable, /)

      Extienda el lado derecho del deque agregando elementos del
      argumento iterable.

   extendleft(iterable, /)

      Extienda el lado izquierdo del deque agregando elementos de
      *iterable*. Tenga en cuenta que la serie de appends a la
      izquierda da como resultado la inversión del orden de los
      elementos en el argumento iterable.

   index(value[, start[, stop]])

      Return the position of *value* in the deque (at or after index
      *start* and before index *stop*).  Returns the first match or
      raises "ValueError" if not found.

      Added in version 3.5.

   insert(index, value, /)

      Insert *value* into the deque at position *index*.

      Si la inserción causara que un deque limitado crezca más allá de
      *maxlen*, se lanza un "IndexError".

      Added in version 3.5.

   pop()

      Elimina y retorna un elemento del lado derecho del deque. Si no
      hay elementos presentes, lanza un "IndexError".

   popleft()

      Elimina y retorna un elemento del lado izquierdo del deque. Si
      no hay elementos presentes, lanza un "IndexError".

   remove(value, /)

      Elimina la primera aparición de *value*. Si no se encuentra,
      lanza un "ValueError".

   reverse()

      Invierte los elementos del deque en su lugar (*in-place*) y
      luego retorna "None".

      Added in version 3.2.

   rotate(n=1, /)

      Gira el deque *n* pasos a la derecha. Si *n* es negativo, lo
      gira hacia la izquierda.

      Cuando el deque no está vacío, girar un paso hacia la derecha
      equivale a "d.appendleft(d.pop())", y girar un paso hacia la
      izquierda equivale a "d.append(d.popleft())".

   Los objetos deque también proporcionan un atributo de solo lectura:

   maxlen

      Tamaño máximo de un deque o "None" si no está limitado.

      Added in version 3.1.

In addition to the above, deques support iteration, pickling,
"len(d)", "reversed(d)", "copy.copy(d)", "copy.deepcopy(d)",
membership testing with the "in" operator, and subscript references
such as "d[0]" to access the first element.  Indexed access is *O*(1)
at both ends but slows to *O*(*n*) in the middle.  For fast random
access, use lists instead.

A partir de la versión 3.5, los deques admiten "__add__()",
"__mul__()", y "__imul__()".

Ejemplo:

   >>> from collections import deque
   >>> d = deque('ghi')                 # make a new deque with three items
   >>> for elem in d:                   # iterate over the deque's elements
   ...     print(elem.upper())
   G
   H
   I

   >>> d.append('j')                    # add a new entry to the right side
   >>> d.appendleft('f')                # add a new entry to the left side
   >>> d                                # show the representation of the deque
   deque(['f', 'g', 'h', 'i', 'j'])

   >>> d.pop()                          # return and remove the rightmost item
   'j'
   >>> d.popleft()                      # return and remove the leftmost item
   'f'
   >>> list(d)                          # list the contents of the deque
   ['g', 'h', 'i']
   >>> d[0]                             # peek at leftmost item
   'g'
   >>> d[-1]                            # peek at rightmost item
   'i'

   >>> list(reversed(d))                # list the contents of a deque in reverse
   ['i', 'h', 'g']
   >>> 'h' in d                         # search the deque
   True
   >>> d.extend('jkl')                  # add multiple elements at once
   >>> d
   deque(['g', 'h', 'i', 'j', 'k', 'l'])
   >>> d.rotate(1)                      # right rotation
   >>> d
   deque(['l', 'g', 'h', 'i', 'j', 'k'])
   >>> d.rotate(-1)                     # left rotation
   >>> d
   deque(['g', 'h', 'i', 'j', 'k', 'l'])

   >>> deque(reversed(d))               # make a new deque in reverse order
   deque(['l', 'k', 'j', 'i', 'h', 'g'])
   >>> d.clear()                        # empty the deque
   >>> d.pop()                          # cannot pop from an empty deque
   Traceback (most recent call last):
       File "<pyshell#6>", line 1, in -toplevel-
           d.pop()
   IndexError: pop from an empty deque

   >>> d.extendleft('abc')              # extendleft() reverses the input order
   >>> d
   deque(['c', 'b', 'a'])

### Recetas "deque"

Esta sección muestra varios enfoques para trabajar con deques.

Los deques de longitud limitada proporcionan una funcionalidad similar
al filtro "tail" en Unix:

   def tail(filename, n=10):
       'Return the last n lines of a file'
       with open(filename) as f:
           return deque(f, n)

Otro enfoque para usar deques es mantener una secuencia de elementos
agregados recientemente haciendo appending a la derecha y popping a la
izquierda:

   def moving_average(iterable, n=3):
       # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
       # https://en.wikipedia.org/wiki/Moving_average
       it = iter(iterable)
       d = deque(itertools.islice(it, n-1))
       d.appendleft(0)
       s = sum(d)
       for elem in it:
           s += elem - d.popleft()
           d.append(elem)
           yield s / n

Un scheduler round-robin se puede implementar con iteradores de
entrada almacenados en "deque". Los valores son producidos del
iterador activo en la posición cero. Si ese iterador está agotado, se
puede eliminar con "popleft()"; de lo contrario, se puede volver en
ciclos al final con el método "rotate()"

   def roundrobin(*iterables):
       "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
       iterators = deque(map(iter, iterables))
       while iterators:
           try:
               while True:
                   yield next(iterators[0])
                   iterators.rotate(-1)
           except StopIteration:
               # Remove an exhausted iterator.
               iterators.popleft()

El método "rotate()" proporciona una forma de implementar eliminación
y rebanado de "deque". Por ejemplo, una implementación pura de Python
de "del d[n]" se basa en el método "rotate()" para colocar los
elementos que se van a extraer:

   def delete_nth(d, n):
       d.rotate(-n)
       d.popleft()
       d.rotate(n)

Para implementar el rebanado de un "deque", use un enfoque similar
aplicando "rotate()" para traer un elemento objetivo al lado izquierdo
del deque. Elimine las entradas antiguas con "popleft()", agregue
nuevas entradas con "extend()", y luego invierta la rotación. Con
variaciones menores en ese enfoque, es fácil implementar
manipulaciones de pila de estilo hacia adelante como "dup", "drop",
"swap", "over", "pick", "rot", y "roll".

## Objetos "defaultdict"

class collections.defaultdict(default_factory=None, /, **kwargs)
class collections.defaultdict(default_factory, mapping, /, **kwargs)
class collections.defaultdict(default_factory, iterable, /, **kwargs)

   Retorna un nuevo objeto similar a un diccionario. "defaultdict" es
   una subclase de la clase incorporada "dict".  Anula un método y
   agrega una variable de instancia de escritura.  La funcionalidad
   restante es la misma que para la clase "dict" y no está documentada
   aquí.

   El primer argumento proporciona el valor inicial para el atributo
   "default_factory"; por defecto es "None". Todos los argumentos
   restantes se tratan de la misma forma que si se pasaran al
   constructor "dict", incluidos los argumentos de palabras clave.

   "defaultdict"s are generic over two types, signifying
   (respectively) the types of the dictionary's keys and values.

   Los objetos "defaultdict" admiten el siguiente método además de las
   operaciones estándar de "dict":

   __missing__(key, /)

      Si el atributo "default_factory" es "None", lanza una excepción
      "KeyError" con la *key* como argumento.

      Si "default_factory" no es "None", se llama sin argumentos para
      proporcionar un valor predeterminado para la *key* dada, este
      valor se inserta en el diccionario para la *key* y se retorna.

      Si llamar a "default_factory" lanza una excepción, esta
      excepción se propaga sin cambios.

      This method is called by the "__getitem__()" method of the
      "dict" class when the requested key is not found; whatever it
      returns or raises is then returned or raised by "__getitem__()".

      Note that "__missing__()" is *not* called for any operations
      besides "__getitem__()". This means that "get()" will, like
      normal dictionaries, return "None" as a default rather than
      using "default_factory".

   los objetos "defaultdict" admiten la siguiente variable de
   instancia:

   default_factory

      This attribute is used by the "__missing__()" method; it is
      initialized from the first argument to the constructor, if
      present, or to "None", if absent.

   Distinto en la versión 3.9: Se agregaron los operadores unir ("|")
   y actualizar ("|="), especificados en **PEP 584**.

### Ejemplos "defaultdict"

Usando "list" como "default_factory", es fácil agrupar una secuencia
de pares clave-valor en un diccionario de listas:

>>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
>>> d = defaultdict(list)
>>> for k, v in s:
...     d[k].append(v)
...
>>> sorted(d.items())
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

Cuando se encuentra cada clave por primera vez, no está ya en el
mapping; por lo que una entrada se crea automáticamente usando la
función "default_factory" que retorna una "list" vacía. La operación
"list.append()" luego adjunta el valor a la nueva lista. Cuando se
vuelven a encontrar claves, la búsqueda procede normalmente
(retornando la lista para esa clave) y la operación "list.append()"
agrega otro valor a la lista. Esta técnica es más simple y rápida que
una técnica equivalente usando "dict.setdefault()":

>>> d = {}
>>> for k, v in s:
...     d.setdefault(k, []).append(v)
...
>>> sorted(d.items())
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

Establecer "default_factory" en "int" hace que "defaultdict" sea útil
para contar (como un bag o multiconjunto en otros idiomas):

>>> s = 'mississippi'
>>> d = defaultdict(int)
>>> for k in s:
...     d[k] += 1
...
>>> sorted(d.items())
[('i', 4), ('m', 1), ('p', 2), ('s', 4)]

Cuando se encuentra una letra por primera vez, falta en el mapping,
por lo que la función "default_factory" llama a "int()" para
proporcionar una cuenta predeterminada de cero. La operación de
incremento luego acumula el conteo de cada letra.

La función "int()" que siempre retorna cero es solo un caso especial
de funciones constantes. Una forma más rápida y flexible de crear
funciones constantes es utilizar una función lambda que pueda
proporcionar cualquier valor constante (no solo cero):

>>> def constant_factory(value):
...     return lambda: value
...
>>> d = defaultdict(constant_factory('<missing>'))
>>> d.update(name='John', action='ran')
>>> '%(name)s %(action)s to %(object)s' % d
'John ran to <missing>'

Establecer "default_factory" en "set" hace que "defaultdict" sea útil
para construir un diccionario de conjuntos:

>>> s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
>>> d = defaultdict(set)
>>> for k, v in s:
...     d[k].add(v)
...
>>> sorted(d.items())
[('blue', {2, 4}), ('red', {1, 3})]

## "namedtuple()" Funciones *Factory* para Tuplas y Campos con Nombres

Las tuplas con nombre asignan significado a cada posición en una tupla
y permiten un código más legible y autodocumentado. Se pueden usar
donde se usen tuplas regulares y agregan la capacidad de acceder a los
campos por nombre en lugar del índice de posición.

collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)

   Returns a new tuple subclass named *typename*.  The new subclass is
   used to create tuple-like objects that have fields accessible by
   attribute lookup as well as being indexable and iterable.
   Instances of the subclass also have a helpful docstring (with
   *typename* and *field_names*) and a helpful "__repr__()" method
   which lists the tuple contents in a "name=value" format.

   Los *nombres de campo* son una secuencia de cadenas como "[‘x’,
   ‘y’]". Alternativamente, *nombres de campo* puede ser una sola
   cadena con cada nombre de campo separado por espacios en blanco y/o
   comas, por ejemplo "’x y’" or "’x, y’".

   Se puede usar cualquier identificador de Python válido para un
   *fieldname*, excepto para los nombres que comienzan con un guión
   bajo. Los identificadores válidos constan de letras, dígitos y
   guiones bajos, pero no comienzan con un dígito o guion bajo y no
   pueden ser "keyword" como *class*, *for*, *return*, *global*,
   *pass*, o *raise*.

   Si *rename* es verdadero, los nombres de campo no válidos se
   reemplazan automáticamente con nombres posicionales. Por ejemplo,
   "[‘abc’, ‘def’, ‘ghi’, ‘abc’]" se convierte en "[‘abc’, ‘_1’,
   ‘ghi’, ‘_3’]", eliminando la palabra clave "def" y el nombre de
   campo duplicado "abc".

   *defaults* pueden ser "None" o un *iterable* de los valores
   predeterminados. Dado que los campos con un valor predeterminado
   deben venir después de cualquier campo sin un valor predeterminado,
   los *defaults* se aplican a los parámetros situados más a la
   derecha. Por ejemplo, si los nombres de campo son "[‘x’, ‘y’, ‘z’]"
   y los valores predeterminados son "(1, 2)", entonces "x" será un
   argumento obligatorio, "y" tendrá el valor predeterminado de "1", y
   "z" el valor predeterminado de "2".

   If *module* is defined, the "__module__" attribute of the named
   tuple is set to that value.

   Las instancias de tuplas con nombre no tienen diccionarios por
   instancia, por lo que son livianas y no requieren más memoria que
   las tuplas normales.

   Para admitir el serializado (*pickling*), la clase tupla con nombre
   debe asignarse a una variable que coincida con *typename*.

   Distinto en la versión 3.1: Se agregó soporte para *rename*.

   Distinto en la versión 3.6: Los parámetros *verbose* y *rename* se
   convirtieron en argumentos de solo palabra clave.

   Distinto en la versión 3.6: Se agregó el parámetro *module*.

   Distinto en la versión 3.7: Removed the *verbose* parameter and the
   "_source" attribute.

   Distinto en la versión 3.7: Added the *defaults* parameter and the
   "_field_defaults" attribute.

   >>> # Basic example
   >>> Point = namedtuple('Point', ['x', 'y'])
   >>> p = Point(11, y=22)     # instantiate with positional or keyword arguments
   >>> p[0] + p[1]             # indexable like the plain tuple (11, 22)
   33
   >>> x, y = p                # unpack like a regular tuple
   >>> x, y
   (11, 22)
   >>> p.x + p.y               # fields also accessible by name
   33
   >>> p                       # readable __repr__ with a name=value style
   Point(x=11, y=22)

Las tuplas con nombre son especialmente útiles para asignar nombres de
campo a las tuplas de resultado retornadas por los módulos "csv" o
"sqlite3":

   EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')

   import csv
   for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
       print(emp.name, emp.title)

   import sqlite3
   conn = sqlite3.connect('/companydata')
   cursor = conn.cursor()
   cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
   for emp in map(EmployeeRecord._make, cursor.fetchall()):
       print(emp.name, emp.title)

Además de los métodos heredados de las tuplas, las tuplas con nombre
admiten tres métodos adicionales y dos atributos. Para evitar
conflictos con los nombres de campo, los nombres de método y atributo
comienzan con un guión bajo.

classmethod somenamedtuple._make(iterable, /)

   Método de clase que crea una nueva instancia a partir de una
   secuencia existente o iterable.

      >>> t = [11, 22]
      >>> Point._make(t)
      Point(x=11, y=22)

somenamedtuple._asdict()

   Retorna un nuevo "dict" que asigna los nombres de los campos a sus
   valores correspondientes:

      >>> p = Point(x=11, y=22)
      >>> p._asdict()
      {'x': 11, 'y': 22}

   Distinto en la versión 3.1: Retorna un "OrderedDict" en lugar de un
   "dict" regular.

   Distinto en la versión 3.8: Retorna un "dict" normal en lugar de un
   "OrderedDict". A partir de Python 3.7, se garantiza el orden de los
   diccionarios normales. Si se requieren las características
   adicionales de "OrderedDict" , la corrección sugerida es emitir el
   resultado al tipo deseado: "OrderedDict(nt._asdict())".

somenamedtuple._replace(**kwargs)

   Retorna una nueva instancia de la tupla nombrada reemplazando los
   campos especificados con nuevos valores:

      >>> p = Point(x=11, y=22)
      >>> p._replace(x=33)
      Point(x=33, y=22)

      >>> for partnum, record in inventory.items():
      ...     inventory[partnum] = record._replace(price=newprices[partnum], timestamp=time.now())

   Named tuples are also supported by generic function
   "copy.replace()".

   Distinto en la versión 3.13: Raise "TypeError" instead of
   "ValueError" for invalid keyword arguments.

somenamedtuple._fields

   Tupla de cadenas que lista los nombres de los campos. Útil para la
   introspección y para crear nuevos tipos de tuplas con nombre a
   partir de tuplas con nombre existentes.

      >>> p._fields            # view the field names
      ('x', 'y')

      >>> Color = namedtuple('Color', 'red green blue')
      >>> Pixel = namedtuple('Pixel', Point._fields + Color._fields)
      >>> Pixel(11, 22, 128, 255, 0)
      Pixel(x=11, y=22, red=128, green=255, blue=0)

somenamedtuple._field_defaults

   Diccionario de nombres de campos mapeados a valores
   predeterminados.

      >>> Account = namedtuple('Account', ['type', 'balance'], defaults=[0])
      >>> Account._field_defaults
      {'balance': 0}
      >>> Account('premium')
      Account(type='premium', balance=0)

Para recuperar un campo cuyo nombre está almacenado en una cadena, use
la función "getattr()":

>>> getattr(p, 'x')
11

Para convertir un diccionario en una tupla con nombre, use el operador
de doble estrella (como se describe en Desempaquetando una lista de
argumentos):

>>> d = {'x': 11, 'y': 22}
>>> Point(**d)
Point(x=11, y=22)

Dado que una tupla con nombre es una clase Python normal, es fácil
agregar o cambiar la funcionalidad con una subclase. A continuación,
se explica cómo agregar un campo calculado y un formato de impresión
de ancho fijo:

   >>> class Point(namedtuple('Point', ['x', 'y'])):
   ...     __slots__ = ()
   ...     @property
   ...     def hypot(self):
   ...         return (self.x ** 2 + self.y ** 2) ** 0.5
   ...     def __str__(self):
   ...         return 'Point: x=%6.3f  y=%6.3f  hypot=%6.3f' % (self.x, self.y, self.hypot)

   >>> for p in Point(3, 4), Point(14, 5/7):
   ...     print(p)
   Point: x= 3.000  y= 4.000  hypot= 5.000
   Point: x=14.000  y= 0.714  hypot=14.018

La subclase que se muestra arriba establece "__slots__" a una tupla
vacía. Esto ayuda a mantener bajos los requisitos de memoria al evitar
la creación de diccionarios de instancia.

La subclasificación no es útil para agregar campos nuevos almacenados.
En su lugar, simplemente cree un nuevo tipo de tupla con nombre a
partir del atributo "_fields":

>>> Point3D = namedtuple('Point3D', Point._fields + ('z',))

Los docstrings se pueden personalizar realizando asignaciones directas
a los campos "__doc__" :

>>> Book = namedtuple('Book', ['id', 'title', 'authors'])
>>> Book.__doc__ += ': Hardcover book in active collection'
>>> Book.id.__doc__ = '13-digit ISBN'
>>> Book.title.__doc__ = 'Title of first printing'
>>> Book.authors.__doc__ = 'List of authors sorted by last name'

Distinto en la versión 3.5: Los docstrings de propiedad se pueden
escribir.

Ver también:

  * Consulte "typing.NamedTuple" para ver una forma de agregar
    sugerencias de tipo para tuplas con nombre. También proporciona
    una notación elegante usando la palabra clave "class":

       class Component(NamedTuple):
           part_number: int
           weight: float
           description: Optional[str] = None

  * Vea "types.SimpleNamespace()" para un espacio de nombres mutable
    basado en un diccionario subyacente en lugar de una tupla.

  * El módulo "dataclasses" proporciona un decorador y funciones para
    agregar automáticamente métodos especiales generados a clases
    definidas por el usuario.

## Objetos "OrderedDict"

Los diccionarios ordenados son como los diccionarios normales, pero
tienen algunas capacidades adicionales relacionadas con las
operaciones de ordenado. Se han vuelto menos importantes ahora que la
clase incorporada "dict" ganó la capacidad de recordar el orden de
inserción (este nuevo comportamiento quedó garantizado en Python 3.7).

Aún quedan algunas diferencias con "dict" :

* El "dict" normal fue diseñado para ser muy bueno en operaciones de
  mapeo. El seguimiento del pedido de inserción era secundario.

* La "OrderedDict" fue diseñada para ser buena para reordenar
  operaciones. La eficiencia del espacio, la velocidad de iteración y
  el rendimiento de las operaciones de actualización fueron
  secundarios.

* El algoritmo "OrderedDict" puede manejar operaciones frecuentes de
  re-ordenamiento mejor que "dict". Como se muestra en las recetas
  siguientes, esto lo vuelve adecuado para implementar varios tipos de
  caches LRU.

* La operación de igualdad para "OrderedDict" comprueba el orden
  coincidente.

  Un "dict" regular puede emular la prueba de igualdad sensible al
  orden con "p == q and all(k1 == k2 for k1, k2 in zip(p, q))".

* The "popitem()" method of "OrderedDict" has a different signature.
  It accepts an optional argument to specify which item is popped.

  Un "dict" regular puede emular "od.popitem(last=True)" de
  OrderedDict con "d.popitem()" que se garantiza que salte el elemento
  situado más a la derecha (el último).

  Un "dict" regular puede emular "od.popitem(last=False)" de
  OrderedDict con "(k := next(iter(d)), d.pop(k))" que retornará y
  eliminará el elemento situado más a la izquierda (el primero) si
  existe.

* "OrderedDict" has a "move_to_end()" method to efficiently reposition
  an element to an endpoint.

  Un "dict" regular puede emular "od.move_to_end(k, last=True)" de
  OrderedDict con "d[k] = d.pop(k)" que desplazará la clave y su valor
  asociado a la posición más a la derecha (última).

  Un "dict" regular no tiene un equivalente eficiente para
  "od.move_to_end(k, last=False)" de OrderedDict que desplaza la clave
  y su valor asociado a la posición más a la izquierda (primera).

* Until Python 3.8, "dict" lacked a "__reversed__()" method.

class collections.OrderedDict(**kwargs)
class collections.OrderedDict(mapping, /, **kwargs)
class collections.OrderedDict(iterable, /, **kwargs)

   Retorna una instancia de una subclase "dict" que tiene métodos
   especializados para reorganizar el orden del diccionario.

   Added in version 3.1.

   popitem(last=True)

      El método "popitem()" para diccionarios ordenados retorna y
      elimina un par (clave, valor). Los pares se retornan en orden
      LIFO (last-in, first-out) si el *último* es verdadero o en orden
      FIFO (first-in, first-out) si es falso.

   move_to_end(key, last=True)

      Mueve una *clave* existente a cualquiera de los extremos de un
      diccionario ordenado.  El elemento se mueve al extremo derecho
      si *last* es verdadero (por defecto) o al principio si *last* es
      falso.  Lanza "KeyError" si la *clave* no existe:

         >>> d = OrderedDict.fromkeys('abcde')
         >>> d.move_to_end('b')
         >>> ''.join(d)
         'acdeb'
         >>> d.move_to_end('b', last=False)
         >>> ''.join(d)
         'bacde'

      Added in version 3.2.

Además de los métodos de mapeo habituales, los diccionarios ordenados
también admiten la iteración inversa usando "reversed()".

Equality tests between "OrderedDict" objects are order-sensitive and
are roughly equivalent to "list(od1.items())==list(od2.items())".

Equality tests between "OrderedDict" objects and other "Mapping"
objects are order-insensitive like regular dictionaries.  This allows
"OrderedDict" objects to be substituted anywhere a regular dictionary
is used.

Distinto en la versión 3.5: Los elementos, claves y valores *vistas*
de "OrderedDict" ahora admiten la iteración inversa usando
"reversed()".

Distinto en la versión 3.6: With the acceptance of **PEP 468**, order
is retained for keyword arguments passed to the "OrderedDict"
constructor and its "update()" method.

Distinto en la versión 3.9: Se agregaron los operadores unir ("|") y
actualizar ("|="), especificados en **PEP 584**.

### Ejemplos y recetas "OrderedDict"

Es sencillo crear una variante de diccionario ordenado que recuerde el
orden en que las claves se insertaron por *última vez*. Si una nueva
entrada sobrescribe una entrada existente, la posición de inserción
original se cambia y se mueve al final:

   class LastUpdatedOrderedDict(OrderedDict):
       'Store items in the order the keys were last added'

       def __setitem__(self, key, value):
           super().__setitem__(key, value)
           self.move_to_end(key)

An "OrderedDict" would also be useful for implementing variants of
"@functools.lru_cache":

   from collections import OrderedDict
   from time import monotonic

   class TimeBoundedLRU:
       "LRU Cache that invalidates and refreshes old entries."

       def __init__(self, func, maxsize=128, maxage=30):
           self.cache = OrderedDict()      # { args : (timestamp, result)}
           self.func = func
           self.maxsize = maxsize
           self.maxage = maxage

       def __call__(self, *args):
           if args in self.cache:
               self.cache.move_to_end(args)
               timestamp, result = self.cache[args]
               if monotonic() - timestamp <= self.maxage:
                   return result
           result = self.func(*args)
           self.cache[args] = monotonic(), result
           if len(self.cache) > self.maxsize:
               self.cache.popitem(last=False)
           return result

   class MultiHitLRUCache:
       """ LRU cache that defers caching a result until
           it has been requested multiple times.

           To avoid flushing the LRU cache with one-time requests,
           we don't cache until a request has been made more than once.

       """

       def __init__(self, func, maxsize=128, maxrequests=4096, cache_after=1):
           self.requests = OrderedDict()   # { uncached_key : request_count }
           self.cache = OrderedDict()      # { cached_key : function_result }
           self.func = func
           self.maxrequests = maxrequests  # max number of uncached requests
           self.maxsize = maxsize          # max number of stored return values
           self.cache_after = cache_after

       def __call__(self, *args):
           if args in self.cache:
               self.cache.move_to_end(args)
               return self.cache[args]
           result = self.func(*args)
           self.requests[args] = self.requests.get(args, 0) + 1
           if self.requests[args] <= self.cache_after:
               self.requests.move_to_end(args)
               if len(self.requests) > self.maxrequests:
                   self.requests.popitem(last=False)
           else:
               self.requests.pop(args, None)
               self.cache[args] = result
               if len(self.cache) > self.maxsize:
                   self.cache.popitem(last=False)
           return result

## Objetos "UserDict"

La clase, "UserDict" actúa como un contenedor alrededor de los objetos
del diccionario. La necesidad de esta clase ha sido parcialmente
suplantada por la capacidad de crear subclases directamente desde
"dict"; sin embargo, es más fácil trabajar con esta clase porque se
puede acceder al diccionario subyacente como un atributo.

class collections.UserDict(**kwargs)
class collections.UserDict(mapping, /, **kwargs)
class collections.UserDict(iterable, /, **kwargs)

   Class that simulates a dictionary.  The instance's contents are
   kept in a regular dictionary, which is accessible via the "data"
   attribute of "UserDict" instances.  If arguments are provided, they
   are used to initialize "data", like a regular dictionary.

   In addition to supporting the methods and operations of mappings,
   "UserDict" instances provide the following attribute:

   data

      Un diccionario real utilizado para almacenar el contenido de la
      clase "UserDict" .

## Objetos "UserList"

Esta clase actúa como un contenedor alrededor de los objetos de lista.
Es una clase base útil para tus propias clases tipo lista que pueden
heredar de ellas y anular métodos existentes o agregar nuevos. De esta
forma, se pueden agregar nuevos comportamientos a las listas.

La necesidad de esta clase ha sido parcialmente suplantada por la
capacidad de crear subclases directamente desde "list"; sin embargo,
es más fácil trabajar con esta clase porque se puede acceder a la
lista subyacente como atributo.

class collections.UserList([list])

   Clase que simula una lista. El contenido de la instancia se
   mantiene en una lista normal, a la que se puede acceder mediante el
   atributo "data" de las instancias "UserList". El contenido de la
   instancia se establece inicialmente en una copia de *list*, por
   defecto a la lista vacía "[]". *list* puede ser cualquier iterable,
   por ejemplo, una lista de Python real o un objeto "UserList".

   Además de admitir los métodos y operaciones de secuencias mutables,
   las instancias "UserList" proporcionan el siguiente atributo:

   data

      Un objeto real "list" usado para almacenar el contenido de la
      clase "UserList" .

**Requisitos de subclases:** Se espera que las subclases de "UserList"
ofrezcan un constructor al que se pueda llamar sin argumentos o con un
solo argumento. Las operaciones de lista que retornan una nueva
secuencia intentan crear una instancia de la clase de implementación
real. Para hacerlo, asume que se puede llamar al constructor con un
solo parámetro, que es un objeto de secuencia utilizado como fuente de
datos.

Si una clase derivada no desea cumplir con este requisito, todos los
métodos especiales admitidos por esta clase deberán de anularse;
consulte las fuentes para obtener información sobre los métodos que
deben proporcionarse en ese caso.

## Objetos "UserString"

La clase, "UserString" actúa como un envoltorio alrededor de los
objetos de cadena. La necesidad de esta clase ha sido parcialmente
suplantada por la capacidad de crear subclases directamente de "str";
sin embargo, es más fácil trabajar con esta clase porque se puede
acceder a la cadena subyacente como atributo.

class collections.UserString(seq)

   Clase que simula un objeto de cadena. El contenido de la instancia
   se mantiene en un objeto de cadena normal, al que se puede acceder
   a través del atributo "data" de las instancias "UserString". El
   contenido de la instancia se establece inicialmente en una copia de
   *seq*. El argumento *seq* puede ser cualquier objeto que se pueda
   convertir en una cadena usando la función incorporada "str()".

   Además de admitir los métodos y operaciones de cadenas, las
   instancias "UserString" proporcionan el siguiente atributo:

   data

      Un objeto real "str" usado para almacenar el contenido de la
      clase "UserString".

   Distinto en la versión 3.5: Nuevos métodos "__getnewargs__",
   "__rmod__", "casefold", "format_map", "isprintable", y "maketrans".
