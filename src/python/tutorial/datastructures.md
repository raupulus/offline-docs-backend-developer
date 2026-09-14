---
title: 5. Estructuras de datos
source_url: https://docs.python.org/es/3
source_path: tutorial/datastructures.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: tutorial
order: 4900
---

# 5. Estructuras de datos

Este capítulo describe en más detalle algunas cosas que ya has
aprendido y agrega algunas cosas nuevas también.

## 5.1. Más sobre listas

The list data type has some more methods. Here are all of the methods
of list objects:

list.append(value, /)

   Add an item to the end of the list.  Similar to "a[len(a):] = [x]".

list.extend(iterable, /)

   Extend the list by appending all the items from the iterable.
   Similar to "a[len(a):] = iterable".

list.insert(index, value, /)

   Inserta un ítem en una posición dada. El primer argumento es el
   índice del ítem delante del cual se insertará, por lo tanto
   "a.insert(0, x)" inserta al principio de la lista y
   "a.insert(len(a), x)" equivale a "a.append(x)".

list.remove(value, /)

   Remove the first item from the list whose value is equal to
   *value*.  It raises a "ValueError" if there is no such item.

list.pop(index=-1, /)

   Remove the item at the given position in the list, and return it.
   If no index is specified, "a.pop()" removes and returns the last
   item in the list. It raises an "IndexError" if the list is empty or
   the index is outside the list range.

list.clear()

   Remove all items from the list.  Similar to "del a[:]".

list.index(value[, start[, stop]])

   Return zero-based index of the first occurrence of *value* in the
   list. Raises a "ValueError" if there is no such item.

   Los argumentos opcionales *start* y *end* son interpretados como la
   notación de rebanadas y se usan para limitar la búsqueda a un
   segmento particular de la lista. El índice retornado se calcula de
   manera relativa al inicio de la secuencia completa en lugar de
   hacerlo con respecto al argumento *start*.

list.count(value, /)

   Return the number of times *value* appears in the list.

list.sort(*, key=None, reverse=False)

   Ordena los elementos de la lista in situ (los argumentos pueden ser
   usados para personalizar el orden de la lista, ver "sorted()" para
   su explicación).

list.reverse()

   Invierte los elementos de la lista in situ.

list.copy()

   Return a shallow copy of the list.  Similar to "a[:]".

Un ejemplo que usa la mayoría de los métodos de la lista:

   >>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
   >>> fruits.count('apple')
   2
   >>> fruits.count('tangerine')
   0
   >>> fruits.index('banana')
   3
   >>> fruits.index('banana', 4)  # Find next banana starting at position 4
   6
   >>> fruits.reverse()
   >>> fruits
   ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
   >>> fruits.append('grape')
   >>> fruits
   ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
   >>> fruits.sort()
   >>> fruits
   ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
   >>> fruits.pop()
   'pear'

Quizás hayas notado que métodos como "insert", "remove" o "sort" que
únicamente modifican la lista no tienen un valor de retorno impreso --
retornan el valor por defecto "None". [1] Esto es un principio de
diseño para todas las estructuras de datos mutables en Python.

Another thing you might notice is that not all data can be sorted or
compared.  For instance, "[None, 'hello', 10]" doesn't sort because
integers can't be compared to strings and "None" can't be compared to
other types.  Also, there are some types that don't have a defined
ordering relation.  For example, "3+4j < 5+7j" isn't a valid
comparison.

### 5.1.1. Usar listas como pilas

Los métodos de lista hacen que resulte muy fácil usar una lista como
una pila, donde el último elemento añadido es el primer elemento
retirado ("último en entrar, primero en salir"). Para agregar un
elemento a la cima de la pila, utiliza "append()". Para retirar un
elemento de la cima de la pila, utiliza "pop()" sin un índice
explícito. Por ejemplo:

   >>> stack = [3, 4, 5]
   >>> stack.append(6)
   >>> stack.append(7)
   >>> stack
   [3, 4, 5, 6, 7]
   >>> stack.pop()
   7
   >>> stack
   [3, 4, 5, 6]
   >>> stack.pop()
   6
   >>> stack.pop()
   5
   >>> stack
   [3, 4]

### 5.1.2. Usar listas como colas

También es posible usar una lista como una cola, donde el primer
elemento añadido es el primer elemento retirado ("primero en entrar,
primero en salir"); sin embargo, las listas no son eficientes para
este propósito. Agregar y sacar del final de la lista es rápido, pero
insertar o sacar del comienzo de una lista es lento (porque todos los
otros elementos tienen que ser desplazados en uno).

Para implementar una cola, utiliza "collections.deque" el cual fue
diseñado para añadir y quitar de ambas puntas de forma rápida. Por
ejemplo:

   >>> from collections import deque
   >>> queue = deque(["Eric", "John", "Michael"])
   >>> queue.append("Terry")           # Terry arrives
   >>> queue.append("Graham")          # Graham arrives
   >>> queue.popleft()                 # The first to arrive now leaves
   'Eric'
   >>> queue.popleft()                 # The second to arrive now leaves
   'John'
   >>> queue                           # Remaining queue in order of arrival
   deque(['Michael', 'Terry', 'Graham'])

### 5.1.3. Comprensión de listas

Las comprensiones de listas ofrecen una manera concisa de crear
listas. Sus usos comunes son para hacer nuevas listas donde cada
elemento es el resultado de algunas operaciones aplicadas a cada
miembro de otra secuencia o iterable, o para crear un segmento de la
secuencia de esos elementos para satisfacer una condición determinada.

Por ejemplo, asumamos que queremos crear una lista de cuadrados, como:

   >>> squares = []
   >>> for x in range(10):
   ...     squares.append(x**2)
   ...
   >>> squares
   [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

Nótese que esto crea (o sobreescribe) una variable llamada "x" que
sigue existiendo luego de que el bucle haya terminado. Podemos
calcular la lista de cuadrados sin ningún efecto secundario haciendo:

   squares = list(map(lambda x: x**2, range(10)))

o, un equivalente:

   squares = [x**2 for x in range(10)]

que es más conciso y legible.

Una lista de comprensión consiste de corchetes rodeando una expresión
seguida de la declaración "for" y luego cero o más declaraciones "for"
o "if".  El resultado será una nueva lista que sale de evaluar la
expresión en el contexto de los "for" o "if" que le siguen.  Por
ejemplo, esta lista de comprensión combina los elementos de dos listas
si no son iguales:

   >>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
   [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

y es equivalente a:

   >>> combs = []
   >>> for x in [1,2,3]:
   ...     for y in [3,1,4]:
   ...         if x != y:
   ...             combs.append((x, y))
   ...
   >>> combs
   [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

Nótese como el orden de los "for" y "if" es el mismo en ambos
pedacitos de código.

Si la expresión es una tupla (como el "(x, y)" en el ejemplo
anterior), debe estar entre paréntesis.

   >>> vec = [-4, -2, 0, 2, 4]
   >>> # create a new list with the values doubled
   >>> [x*2 for x in vec]
   [-8, -4, 0, 4, 8]
   >>> # filter the list to exclude negative numbers
   >>> [x for x in vec if x >= 0]
   [0, 2, 4]
   >>> # apply a function to all the elements
   >>> [abs(x) for x in vec]
   [4, 2, 0, 2, 4]
   >>> # call a method on each element
   >>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
   >>> [weapon.strip() for weapon in freshfruit]
   ['banana', 'loganberry', 'passion fruit']
   >>> # create a list of 2-tuples like (number, square)
   >>> [(x, x**2) for x in range(6)]
   [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
   >>> # the tuple must be parenthesized, otherwise an error is raised
   >>> [x, x**2 for x in range(6)]
     File "<stdin>", line 1
       [x, x**2 for x in range(6)]
        ^^^^^^^
   SyntaxError: did you forget parentheses around the comprehension target?
   >>> # flatten a list using a listcomp with two 'for'
   >>> vec = [[1,2,3], [4,5,6], [7,8,9]]
   >>> [num for elem in vec for num in elem]
   [1, 2, 3, 4, 5, 6, 7, 8, 9]

Las comprensiones de listas pueden contener expresiones complejas y
funciones anidadas:

   >>> from math import pi
   >>> [str(round(pi, i)) for i in range(1, 6)]
   ['3.1', '3.14', '3.142', '3.1416', '3.14159']

### 5.1.4. Listas por comprensión anidadas

La expresión inicial de una comprensión de listas puede ser cualquier
expresión arbitraria, incluyendo otra comprensión de listas.

Considerá el siguiente ejemplo de una matriz de 3x4 implementada como
una lista de tres listas de largo 4:

   >>> matrix = [
   ...     [1, 2, 3, 4],
   ...     [5, 6, 7, 8],
   ...     [9, 10, 11, 12],
   ... ]

La siguiente comprensión de lista transpondrá las filas y columnas:

   >>> [[row[i] for row in matrix] for i in range(4)]
   [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

Como vimos en la sección anterior, la lista de comprensión anidada se
evalúa en el contexto del "for" que lo sigue, por lo que este ejemplo
equivale a:

   >>> transposed = []
   >>> for i in range(4):
   ...     transposed.append([row[i] for row in matrix])
   ...
   >>> transposed
   [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

el cual, a la vez, es lo mismo que:

   >>> transposed = []
   >>> for i in range(4):
   ...     # the following 3 lines implement the nested listcomp
   ...     transposed_row = []
   ...     for row in matrix:
   ...         transposed_row.append(row[i])
   ...     transposed.append(transposed_row)
   ...
   >>> transposed
   [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

En el mundo real, deberías preferir funciones predefinidas a
declaraciones con flujo complejo. La función "zip()" haría un buen
trabajo para este caso de uso:

   >>> list(zip(*matrix))
   [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

Ver Desempaquetando una lista de argumentos para detalles sobre el
asterisco de esta línea.

## 5.2. La instrucción "del"

Hay una manera de quitar un ítem de una lista dado su índice en lugar
de su valor: la instrucción "del". Esta es diferente del método
"pop()", el cual retorna un valor. La instrucción "del" también puede
usarse para quitar secciones de una lista o vaciar la lista completa
(lo que hacíamos antes asignando una lista vacía a la rebanada). Por
ejemplo:

   >>> a = [-1, 1, 66.25, 333, 333, 1234.5]
   >>> del a[0]
   >>> a
   [1, 66.25, 333, 333, 1234.5]
   >>> del a[2:4]
   >>> a
   [1, 66.25, 1234.5]
   >>> del a[:]
   >>> a
   []

"del" puede usarse también para eliminar variables:

   >>> del a

Hacer referencia al nombre "a" de aquí en más es un error (al menos
hasta que se le asigne otro valor). Veremos otros usos para "del" más
adelante.

## 5.3. Tuplas y secuencias

Vimos que las listas y cadenas tienen propiedades en común, como el
indexado y las operaciones de rebanado. Estas son dos ejemplos de
datos de tipo *secuencia* (ver Tipos secuencia --- list, tuple,
range). Como Python es un lenguaje en evolución, otros datos de tipo
secuencia pueden agregarse. Existe otro dato de tipo secuencia
estándar: la *tupla*.

Una tupla está formada por un número de valores separados por comas,
por ejemplo:

   >>> t = 12345, 54321, 'hello!'
   >>> t[0]
   12345
   >>> t
   (12345, 54321, 'hello!')
   >>> # Tuples may be nested:
   >>> u = t, (1, 2, 3, 4, 5)
   >>> u
   ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
   >>> # Tuples are immutable:
   >>> t[0] = 88888
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: 'tuple' object does not support item assignment
   >>> # but they can contain mutable objects:
   >>> v = ([1, 2, 3], [3, 2, 1])
   >>> v
   ([1, 2, 3], [3, 2, 1])

Como puedes ver, en la salida las tuplas siempre se encierran entre
paréntesis para que las tuplas anidadas puedan interpretarse
correctamente; pueden ingresarse con o sin paréntesis, aunque a menudo
los paréntesis son necesarios de todas formas (si la tupla es parte de
una expresión más grande). No es posible asignar a los ítems
individuales de una tupla, pero sin embargo sí se puede crear tuplas
que contengan objetos mutables, como las listas.

A pesar de que las tuplas puedan parecerse a las listas,
frecuentemente se utilizan en distintas situaciones y para distintos
propósitos. Las tuplas son *immutable* y normalmente contienen una
secuencia heterogénea de elementos que son accedidos al desempaquetar
(ver más adelante en esta sección) o indizar (o incluso acceder por
atributo en el caso de las "namedtuples"). Las listas son *mutable*, y
sus elementos son normalmente homogéneos y se acceden iterando a la
lista.

Un problema particular es la construcción de tuplas que contengan 0 o
1 ítem: la sintaxis presenta algunas peculiaridades para estos casos.
Las tuplas vacías se construyen mediante un par de paréntesis vacío;
una tupla con un ítem se construye poniendo una coma a continuación
del valor (no alcanza con encerrar un único valor entre paréntesis).
Feo, pero efectivo. Por ejemplo:

   >>> empty = ()
   >>> singleton = 'hello',    # <-- note trailing comma
   >>> len(empty)
   0
   >>> len(singleton)
   1
   >>> singleton
   ('hello',)

La declaración "t = 12345, 54321, 'hola!'" es un ejemplo de
*empaquetado de tuplas*: los valores "12345", "54321" y "'hola!'" se
empaquetan juntos en una tupla. La operación inversa también es
posible:

   >>> x, y, z = t

Esto se llama, apropiadamente, *desempaquetado de secuencias*, y
funciona para cualquier secuencia en el lado derecho del igual. El
desempaquetado de secuencias requiere que la cantidad de variables a
la izquierda del signo igual sea el tamaño de la secuencia. Nótese que
la asignación múltiple es en realidad sólo una combinación de
empaquetado de tuplas y desempaquetado de secuencias.

## 5.4. Conjuntos

Python also includes a data type for sets.  A set is an unordered
collection with no duplicate elements.  Basic uses include membership
testing and eliminating duplicate entries.  Set objects also support
mathematical operations like union, intersection, difference, and
symmetric difference.

Las llaves o la función "set()" pueden usarse para crear conjuntos.
Notá que para crear un conjunto vacío tenés que usar "set()", no "{}";
esto último crea un diccionario vacío, una estructura de datos que
discutiremos en la sección siguiente.

Because sets are unordered, iterating over them or printing them can
produce the elements in a different order than you expect.

Una pequeña demostración:

   >>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
   >>> print(basket)                      # show that duplicates have been removed
   {'orange', 'banana', 'pear', 'apple'}
   >>> 'orange' in basket                 # fast membership testing
   True
   >>> 'crabgrass' in basket
   False

   >>> # Demonstrate set operations on unique letters from two words
   >>>
   >>> a = set('abracadabra')
   >>> b = set('alacazam')
   >>> a                                  # unique letters in a
   {'a', 'r', 'b', 'c', 'd'}
   >>> a - b                              # letters in a but not in b
   {'r', 'd', 'b'}
   >>> a | b                              # letters in a or b or both
   {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
   >>> a & b                              # letters in both a and b
   {'a', 'c'}
   >>> a ^ b                              # letters in a or b but not both
   {'r', 'd', 'b', 'm', 'z', 'l'}

De forma similar a las comprensiones de listas, la comprensión de
conjuntos está también soportada:

   >>> a = {x for x in 'abracadabra' if x not in 'abc'}
   >>> a
   {'r', 'd'}

## 5.5. Diccionarios

Otro tipo de dato útil incluido en Python es el *diccionario* (ver
Tipos mapa --- dict). Los diccionarios se encuentran a veces en otros
lenguajes como "memorias asociativas" o "arreglos asociativos". A
diferencia de las secuencias, que se indexan mediante un rango
numérico, los diccionarios se indexan con *claves*, que pueden ser
cualquier tipo inmutable; las cadenas y números siempre pueden ser
claves. Las tuplas pueden usarse como claves si solamente contienen
cadenas, números o tuplas; si una tupla contiene cualquier objeto
mutable directa o indirectamente, no puede usarse como clave. No podés
usar listas como claves, ya que las listas pueden modificarse usando
asignación por índice, asignación por sección, o métodos como
"append()" y "extend()".

Es mejor pensar en un diccionario como un conjunto de pares
*clave:valor* con el requerimiento de que las claves sean únicas
(dentro de un diccionario). Un par de llaves crean un diccionario
vacío: "{}". Colocar una lista de pares clave:valor separada por comas
dentro de las llaves añade pares clave:valor iniciales al diccionario;
esta es también la forma en que los diccionarios se muestran en la
salida.

The main operations on a dictionary are storing a value with some key
and extracting the value given the key.  It is also possible to delete
a key:value pair with "del". If you store using a key that is already
in use, the old value associated with that key is forgotten.

Extracting a value for a non-existent key by subscripting ("d[key]")
raises a "KeyError". To avoid getting this error when trying to access
a possibly non-existent key, use the "get()" method instead, which
returns "None" (or a specified default value) if the key is not in the
dictionary.

Ejecutando "list(d)" en un diccionario retornará una lista con todas
las claves usadas en el diccionario, en el orden de inserción (si
deseas que esté ordenada simplemente usa "sorted(d)" en su lugar).
Para comprobar si una clave está en el diccionario usa la palabra
clave "in".

Un pequeño ejemplo de uso de un diccionario:

   >>> tel = {'jack': 4098, 'sape': 4139}
   >>> tel['guido'] = 4127
   >>> tel
   {'jack': 4098, 'sape': 4139, 'guido': 4127}
   >>> tel['jack']
   4098
   >>> tel['irv']
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   KeyError: 'irv'
   >>> print(tel.get('irv'))
   None
   >>> del tel['sape']
   >>> tel['irv'] = 4127
   >>> tel
   {'jack': 4098, 'guido': 4127, 'irv': 4127}
   >>> list(tel)
   ['jack', 'guido', 'irv']
   >>> sorted(tel)
   ['guido', 'irv', 'jack']
   >>> 'guido' in tel
   True
   >>> 'jack' not in tel
   False

El constructor "dict()" crea un diccionario directamente desde
secuencias de pares clave-valor:

   >>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
   {'sape': 4139, 'guido': 4127, 'jack': 4098}

Además, las comprensiones de diccionarios se pueden usar para crear
diccionarios desde expresiones arbitrarias de clave y valor:

   >>> {x: x**2 for x in (2, 4, 6)}
   {2: 4, 4: 16, 6: 36}

Cuando las claves son cadenas simples, a veces resulta más fácil
especificar los pares usando argumentos por palabra clave:

   >>> dict(sape=4139, guido=4127, jack=4098)
   {'sape': 4139, 'guido': 4127, 'jack': 4098}

## 5.6. Técnicas de iteración

Cuando iteramos sobre diccionarios, se pueden obtener al mismo tiempo
la clave y su valor correspondiente usando el método "items()".

   >>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
   >>> for k, v in knights.items():
   ...     print(k, v)
   ...
   gallahad the pure
   robin the brave

Cuando se itera sobre una secuencia, se puede obtener el índice de
posición junto a su valor correspondiente usando la función
"enumerate()".

   >>> for i, v in enumerate(['tic', 'tac', 'toe']):
   ...     print(i, v)
   ...
   0 tic
   1 tac
   2 toe

Para iterar sobre dos o más secuencias al mismo tiempo, los valores
pueden emparejarse con la función "zip()".

   >>> questions = ['name', 'quest', 'favorite color']
   >>> answers = ['lancelot', 'the holy grail', 'blue']
   >>> for q, a in zip(questions, answers):
   ...     print('What is your {0}?  It is {1}.'.format(q, a))
   ...
   What is your name?  It is lancelot.
   What is your quest?  It is the holy grail.
   What is your favorite color?  It is blue.

Para iterar sobre una secuencia en orden inverso, se especifica
primero la secuencia al derecho y luego se llama a la función
"reversed()".

   >>> for i in reversed(range(1, 10, 2)):
   ...     print(i)
   ...
   9
   7
   5
   3
   1

Para iterar sobre una secuencia ordenada, se utiliza la función
"sorted()" la cual retorna una nueva lista ordenada dejando a la
original intacta.

   >>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
   >>> for i in sorted(basket):
   ...     print(i)
   ...
   apple
   apple
   banana
   orange
   orange
   pear

El uso de "set()" en una secuencia elimina los elementos duplicados.
El uso de "sorted()" en combinación con "set()" sobre una secuencia es
una forma idiomática de recorrer elementos únicos de la secuencia
ordenada.

   >>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
   >>> for f in sorted(set(basket)):
   ...     print(f)
   ...
   apple
   banana
   orange
   pear

A veces uno intenta cambiar una lista mientras la está iterando; sin
embargo, a menudo es más simple y seguro crear una nueva lista:

   >>> import math
   >>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
   >>> filtered_data = []
   >>> for value in raw_data:
   ...     if not math.isnan(value):
   ...         filtered_data.append(value)
   ...
   >>> filtered_data
   [56.2, 51.7, 55.3, 52.5, 47.8]

## 5.7. Más acerca de condiciones

Las condiciones usadas en las instrucciones "while" e "if" pueden
contener cualquier operador, no sólo comparaciones.

Los operadores de comparación "in" y "not in" verifican si un valor
ocurre (o no ocurre) en una secuencia. Los operadores "is" e "is not"
comparan si dos objetos son realmente el mismo objeto. Todos los
operadores de comparación tienen la misma prioridad, que es menor que
la de todos los operadores numéricos.

Las comparaciones pueden encadenarse. Por ejemplo, "a < b == c"
verifica si "a" es menor que "b" y además si "b" es igual a "c".

Las comparaciones pueden combinarse mediante los operadores booleanos
"and" y "or", y el resultado de una comparación (o de cualquier otra
expresión booleana) puede negarse con "not". Estos tienen prioridades
menores que los operadores de comparación; entre ellos "not" tiene la
mayor prioridad y "or" la menor, o sea que "A and not B or C" equivale
a "(A and (not B)) or C". Como siempre, los paréntesis pueden usarse
para expresar la composición deseada.

Los operadores booleanos "and" y "or" son los llamados operadores
*cortocircuito*: sus argumentos se evalúan de izquierda a derecha, y
la evaluación se detiene en el momento en que se determina su
resultado. Por ejemplo, si "A" y "C" son verdaderas pero "B" es falsa,
en "A and B and C" no se evalúa la expresión "C". Cuando se usa como
un valor general y no como un booleano, el valor retornado de un
operador cortocircuito es el último argumento evaluado.

Es posible asignar el resultado de una comparación u otra expresión
booleana a una variable. Por ejemplo,

   >>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
   >>> non_null = string1 or string2 or string3
   >>> non_null
   'Trondheim'

Nótese que en Python, a diferencia de C, asignaciones dentro de
expresiones deben realizarse explícitamente con el operador walrus
":=". Esto soluciona algunos problemas comunes encontrados en C:
escribiendo "=" en una expresión cuando se intentaba escribir "==".

## 5.8. Comparando secuencias y otros tipos

Las secuencias pueden compararse con otros objetos del mismo tipo de
secuencia. La comparación usa orden *lexicográfico*: primero se
comparan los dos primeros ítems, si son diferentes esto ya determina
el resultado de la comparación; si son iguales, se comparan los
siguientes dos ítems, y así sucesivamente hasta llegar al final de
alguna de las secuencias. Si dos ítems a comparar son ambos secuencias
del mismo tipo, la comparación lexicográfica es recursiva. Si todos
los ítems de dos secuencias resultan iguales, se considera que las
secuencias son iguales. Si una secuencia es la parte inicial de la
otra, la secuencia más corta es la más pequeña. El orden lexicográfico
de las cadenas de caracteres utiliza el punto de código Unicode para
ordenar caracteres individuales. Algunos ejemplos de comparación entre
secuencias del mismo tipo:

   (1, 2, 3)              < (1, 2, 4)
   [1, 2, 3]              < [1, 2, 4]
   'ABC' < 'C' < 'Pascal' < 'Python'
   (1, 2, 3, 4)           < (1, 2, 4)
   (1, 2)                 < (1, 2, -1)
   (1, 2, 3)             == (1.0, 2.0, 3.0)
   (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)

Observá que comparar objetos de diferentes tipos con "<" o ">" es
legal siempre y cuando los objetos tenga los métodos de comparación
apropiados. Por ejemplo, los tipos de números mezclados son comparados
de acuerdo a su valor numérico, o sea 0 es igual a 0.0, etc. Si no es
el caso, en lugar de proveer un ordenamiento arbitrario, el intérprete
lanzará una excepción "TypeError".

-[ Notas al pie ]-

[1] Otros lenguajes podrían retornar un objeto mutado, que permite
    encadenamiento de métodos como
    "d->insert("a")->remove("b")->sort();".
