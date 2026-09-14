---
title: 3. Modelo de datos
source_url: https://docs.python.org/es/3
source_path: reference/datamodel.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: reference
order: 4760
---

# 3. Modelo de datos

## 3.1. Objetos, valores y tipos

*Objects* are Python's abstraction for data.  All data in a Python
program is represented by objects or by relations between objects.
Even code is represented by objects.

Cada objeto tiene una identidad, un tipo y un valor. La *identidad* de
un objeto nunca cambia una vez que ha sido creado; puede pensar en
ello como la dirección del objeto en la memoria. El operador "is"
compara la identidad de dos objetos; la función "id()" retorna un
número entero que representa su identidad.

Para CPython, "id(x)" es la dirección de memoria donde se almacena
"x".

El tipo de un objeto determina las operaciones que admite el objeto
(por ejemplo, "¿tiene una longitud?") y también define los posibles
valores para los objetos de ese tipo. La función "type()" retorna el
tipo de un objeto (que es un objeto en sí mismo). Al igual que su
identidad, también el *type* de un objeto es inmutable. [1]

El *valor* de algunos objetos puede cambiar. Se dice que los objetos
cuyo valor puede cambiar son *mutables*; Los objetos cuyo valor no se
puede modificar una vez que se crean se denominan *inmutables*. (El
valor de un objeto contenedor inmutable que contiene una referencia a
un objeto mutable puede cambiar cuando se cambia el valor de este
último; sin embargo, el contenedor todavía se considera inmutable,
porque la colección de objetos que contiene no se puede cambiar. Por
lo tanto, la inmutabilidad no es estrictamente lo mismo que tener un
valor inmutable, es más sutil). La mutabilidad de un objeto está
determinada por su tipo; por ejemplo, los números, las cadenas de
caracteres y las tuplas son inmutables, mientras que los diccionarios
y las listas son mutables.

Los objetos nunca se destruyen explícitamente; sin embargo, cuando se
vuelven inalcanzables, se pueden recolectar basura. Se permite a una
implementación posponer la recolección de basura u omitirla por
completo; es una cuestión de calidad de la implementación cómo se
implementa la recolección de basura, siempre que no se recolecten
objetos que todavía sean accesibles.

CPython actualmente utiliza un esquema de conteo de referencias con
detección retardada (opcional) de basura enlazada cíclicamente, que
recolecta la mayoría de los objetos tan pronto como se vuelven
inalcanzables, pero no se garantiza que recolecte basura que contenga
referencias circulares. Vea la documentación del módulo "gc" para
información sobre el control de la recolección de basura cíclica.
Otras implementaciones actúan de manera diferente y CPython puede
cambiar. No dependa de la finalización inmediata de los objetos cuando
se vuelvan inalcanzables (por lo que siempre debe cerrar los archivos
explícitamente).

Tenga en cuenta que el uso de las funciones de rastreo o depuración de
la implementación puede mantener activos los objetos que normalmente
serían coleccionables. También tenga en cuenta que la captura de una
excepción con una sentencia "try"..."except" puede mantener objetos
activos.

Algunos objetos contienen referencias a recursos "externos" como
archivos abiertos o ventanas.  Se entiende que estos recursos se
liberan cuando el objeto es eliminado por el recolector de basura,
pero como no se garantiza que la recolección de basura suceda, dichos
objetos también proporcionan una forma explícita de liberar el recurso
externo, generalmente un método "close()". Se recomienda
encarecidamente a los programas cerrar explícitamente dichos objetos.
La declaración "try" ... "finally" y la declaración "with"
proporcionan formas convenientes de hacer esto.

Algunos objetos contienen referencias a otros objetos; estos se llaman
*contenedores*. Ejemplos de contenedores son tuplas, listas y
diccionarios. Las referencias son parte del valor de un contenedor. En
la mayoría de los casos, cuando hablamos del valor de un contenedor,
implicamos los valores, no las identidades de los objetos contenidos;
sin embargo, cuando hablamos de la mutabilidad de un contenedor, solo
se implican las identidades de los objetos contenidos inmediatamente.
Entonces, si un contenedor inmutable (como una tupla) contiene una
referencia a un objeto mutable, su valor cambia si se cambia ese
objeto mutable.

Los tipos afectan a casi todos los aspectos del comportamiento del
objeto. Incluso la importancia de la identidad del objeto se ve
afectada en cierto sentido: para los tipos inmutables, las operaciones
que calculan nuevos valores en realidad pueden retornar una referencia
a cualquier objeto existente con el mismo tipo y valor, mientras que
para los objetos mutables esto no está permitido. Por ejemplo, al
hacer "a = 1; b = 1", *a* y *b* puede o no referirse al mismo objeto
con el valor 1, dependiendo de la implementación. Esto se debe a que
"int" es un tipo inmutable, así que la referencia a "1" se puede
reusar. Este comportamiento depende de la implementación utilizada,
así que no se debe confiar en ello, pero es algo que hay que tener en
cuenta al utilizar pruebas de identidad de objetos. Sin embargo, al
hacer "c = []; d = []", *c* y *d* se garantiza que se refieren a dos
listas vacías diferentes, únicas y recién creadas. (Tenga en cuenta
que "e = f = []" asigna el *mismo* objeto a ambos *e* y *f*.)

## 3.2. Jerarquía de tipos estándar

A continuación se muestra una lista de los tipos integrados en Python.
Los módulos de extensión (escritos en C, Java u otros lenguajes,
dependiendo de la implementación) pueden definir tipos adicionales.
Las versiones futuras de Python pueden agregar tipos a la jerarquía de
tipos (por ejemplo, números racionales, matrices de enteros
almacenados de manera eficiente, etc.), aunque tales adiciones a
menudo se proporcionarán a través de la biblioteca estándar.

Algunas de las descripciones de tipos a continuación contienen un
párrafo que enumera 'atributos especiales'. Estos son atributos que
proporcionan acceso a la implementación y no están destinados para uso
general. Su definición puede cambiar en el futuro.

### 3.2.1. None

Este tipo tiene un solo valor. Hay un solo objeto con este valor. Se
accede a este objeto a través del nombre incorporado "None". Se
utiliza para indicar la ausencia de un valor en muchas situaciones,
por ejemplo, se retorna desde funciones que no retornan nada
explícitamente. Su valor de verdad es falso.

### 3.2.2. NotImplemented

Este tipo tiene un solo valor. Hay un solo objeto con este valor. Se
accede a este objeto a través del nombre integrado "NotImplemented".
Los métodos numéricos y los métodos de comparación enriquecidos deben
retornar este valor si no implementan la operación para los operandos
proporcionados. (El intérprete intentará entonces la operación
reflejada, o alguna otra alternativa, dependiendo del operador). No
debe evaluarse en un contexto booleano.

Vea Implementar operaciones aritméticas para más detalles.

Distinto en la versión 3.9: Evaluating "NotImplemented" in a boolean
context was deprecated.

Distinto en la versión 3.14: Evaluating "NotImplemented" in a boolean
context now raises a "TypeError". It previously evaluated to "True"
and emitted a "DeprecationWarning" since Python 3.9.

### 3.2.3. Elipsis

Este tipo tiene un solo valor. Hay un solo objeto con este valor. Se
accede a este objeto a través del literal "..." o el nombre
incorporado "Ellipsis". Su valor de verdad es verdadero.

### 3.2.4. "numbers.Number"

Estos son creados por literales numéricos y retornados como resultados
por operadores aritméticos y funciones aritméticas integradas. Los
objetos numéricos son inmutables; una vez creado su valor nunca
cambia. Los números de Python están, por supuesto, fuertemente
relacionados con los números matemáticos, pero están sujetos a las
limitaciones de la representación numérica en las computadoras.

Las representaciones de cadena de caracteres de las clases numéricas,
calculadas por "__repr__()" y "__str__()", tienen las siguientes
propiedades:

* Son literales numéricos válidos que, cuando se pasan a su
  constructor de clase, producen un objeto que tiene el valor del
  numérico original.

* La representación está en base 10, cuando sea posible.

* Los ceros iniciales, posiblemente excepto un solo cero antes de un
  punto decimal, no se muestran.

* Los ceros finales, posiblemente excepto un solo cero después de un
  punto decimal, no se muestran.

* Solo se muestra un signo cuando el número es negativo.

Python distingue entre números enteros, números de coma flotante y
números complejos:

#### 3.2.4.1. "numbers.Integral"

Estos representan elementos del conjunto matemático de números enteros
(positivo y negativo).

Nota:

  Las reglas para la representación de enteros están destinadas a dar
  la interpretación más significativa de las operaciones de cambio y
  máscara que involucran enteros negativos.

Hay dos tipos de números enteros:

Enteros ("int")
   Estos representan números en un rango ilimitado, sujetos solo a la
   memoria (virtual) disponible. Para las operaciones de
   desplazamiento y máscara, se asume una representación binaria, y
   los números negativos se representan en una variante del
   complemento de 2 que da la ilusión de una cadena de caracteres
   infinita de bits con signo que se extiende hacia la izquierda.

Booleanos ("bool")
   Estos representan los valores de verdad Falso y Verdadero. Los dos
   objetos que representan los valores "False" y "True" son los únicos
   objetos booleanos. El tipo booleano es un subtipo del tipo entero y
   los valores booleanos se comportan como los valores 0 y 1
   respectivamente, en casi todos los contextos, con la excepción de
   que cuando se convierten en una cadena de caracteres, las cadenas
   de caracteres ""False"" o ""True"" son retornadas respectivamente.

#### 3.2.4.2. "numbers.Real" ("float")

Estos representan números de punto flotante de precisión doble a nivel
de máquina. Está a merced de la arquitectura de la máquina subyacente
(y la implementación de C o Java) para el rango aceptado y el manejo
del desbordamiento. Python no admite números de coma flotante de
precisión simple; el ahorro en el uso del procesador y la memoria, que
generalmente son la razón para usarlos, se ven reducidos por la
sobrecarga del uso de objetos en Python, por lo que no hay razón para
complicar el lenguaje con dos tipos de números de coma flotante.

#### 3.2.4.3. "numbers.Complex" ("complex")

Estos representan números complejos como un par de números de coma
flotante de precisión doble a nivel de máquina. Se aplican las mismas
advertencias que para los números de coma flotante. Las partes reales
e imaginarias de un número complejo "z" se pueden obtener a través de
los atributos de solo lectura "z.real" y "z.imag".

### 3.2.5. Secuencias

Estos representan conjuntos ordenados finitos indexados por números no
negativos. La función incorporada "len()" retorna el número de
elementos de una secuencia. Cuando la longitud de una secuencia es
*n*, el conjunto de índices contiene los números 0, 1, ..., *n*-1. El
elemento *i* de la secuencia *a* se selecciona mediante "a[i]".
Algunas secuencias, incluidas las secuencias integradas, interpretan
los subíndices negativos sumando la longitud de la secuencia. Por
ejemplo, "a[-2]" es igual a "a[n-2]", el penúltimo elemento de la
secuencia a con longitud "n".

The resulting value must be a nonnegative integer less than the number
of items in the sequence. If it is not, an "IndexError" is raised.

Sequences also support slicing: "a[start:stop]" selects all items with
index *k* such that *start* "<=" *k* "<" *stop*.  When used as an
expression, a slice is a sequence of the same type. The comment above
about negative subscripts also applies to negative slice positions.
Note that no error is raised if a slice position is less than zero or
larger than the length of the sequence.

If *start* is missing or "None", slicing behaves as if *start* was
zero. If *stop* is missing or "None", slicing behaves as if *stop* was
equal to the length of the sequence.

Algunas secuencias también admiten "segmentación extendida" con un
tercer parámetro "paso" : "a[i:j:k]" selecciona todos los elementos de
*a* con índice *x* donde "x = i + n*k", *n* ">=" "0" y *i* "<=" *x*
"<" *j*.

Las secuencias se distinguen según su mutabilidad:

#### 3.2.5.1. Secuencias inmutables

Un objeto de un tipo de secuencia inmutable no puede cambiar una vez
que se crea. (Si el objeto contiene referencias a otros objetos, estos
otros objetos pueden ser mutables y pueden cambiarse; sin embargo, la
colección de objetos a los que hace referencia directamente un objeto
inmutable no puede cambiar).

Los siguientes tipos son secuencias inmutables:

Cadenas de caracteres
   A string ("str") is a sequence of values that represent
   *characters*, or more formally, *Unicode code points*. All the code
   points in the range "0" to "0x10FFFF" can be represented in a
   string.

   Python doesn't have a dedicated *character* type. Instead, every
   code point in the string is represented as a string object with
   length "1".

   The built-in function "ord()" converts a code point from its string
   form to an integer in the range "0" to "0x10FFFF"; "chr()" converts
   an integer in the range "0" to "0x10FFFF" to the corresponding
   length "1" string object. "str.encode()" can be used to convert a
   "str" to "bytes" using the given text encoding, and
   "bytes.decode()" can be used to achieve the opposite.

Tuplas
   The items of a "tuple" are arbitrary Python objects. Tuples of two
   or more items are formed by comma-separated lists of expressions.
   A tuple of one item (a 'singleton') can be formed by affixing a
   comma to an expression (an expression by itself does not create a
   tuple, since parentheses must be usable for grouping of
   expressions).  An empty tuple can be formed by an empty pair of
   parentheses.

Bytes
   A "bytes" object is an immutable array.  The items are 8-bit bytes,
   represented by integers in the range 0 <= x < 256.  Bytes literals
   (like "b'abc'") and the built-in "bytes()" constructor can be used
   to create bytes objects.  Also, bytes objects can be decoded to
   strings via the "decode()" method.

#### 3.2.5.2. Secuencias mutables

Las secuencias mutables se pueden cambiar después de su creación. Las
anotaciones de suscripción y segmentación se pueden utilizar como el
objetivo de asignaciones y declaraciones "del" (eliminar).

Nota:

  Los módulos "collections" y "array" proporcionan ejemplos
  adicionales de tipos de secuencias mutables.

Actualmente hay dos tipos intrínsecos de secuencias mutable:

Listas
   Los elementos de una lista son objetos de Python arbitrarios.  Las
   listas se forman colocando una lista de expresiones separadas por
   comas entre corchetes. (Tome en cuenta que no hay casos especiales
   necesarios para formar listas de longitud 0 o 1.)

Colecciones de bytes
   Un objeto bytearray es una colección mutable. Son creados por el
   constructor incorporado "bytearray()".  Además de ser mutables (y,
   por lo tanto, inquebrantable), las colecciones de bytes
   proporcionan la misma interfaz y funcionalidad que los objetos
   inmutables "bytes".

### 3.2.6. Tipos de conjuntos

Estos representan conjuntos finitos no ordenados de objetos únicos e
inmutables. Como tal, no pueden ser indexados por ningún *subscript*.
Sin embargo, pueden repetirse y la función incorporada "len()" retorna
el número de elementos en un conjunto. Los usos comunes de los
conjuntos son pruebas rápidas de membresía, eliminación de duplicados
de una secuencia y cálculo de operaciones matemáticas como
intersección, unión, diferencia y diferencia simétrica.

Para elementos del conjunto, se aplican las mismas reglas de
inmutabilidad que para las claves de diccionario. Tenga en cuenta que
los tipos numéricos obedecen las reglas normales para la comparación
numérica: si dos números se comparan igual (por ejemplo, "1" y "1.0"),
solo uno de ellos puede estar contenido en un conjunto.

Actualmente hay dos tipos de conjuntos intrínsecos:

Conjuntos
   These represent a mutable set. They are created by the built-in
   "set()" constructor and can be modified afterwards by several
   methods, such as "add()".

Conjuntos congelados
   Estos representan un conjunto inmutable. Son creados por el
   constructor incorporado "frozenset()". Como un conjunto congelado
   es inmutable y *hashable*, se puede usar nuevamente como un
   elemento de otro conjunto o como una clave de un diccionario.

### 3.2.7. Mapeos

Estos representan conjuntos finitos de objetos indexados por conjuntos
de índices arbitrarios. La notación de subíndice "a[k]" selecciona el
elemento indexado por "k" del mapeo "a"; esto se puede usar en
expresiones y como el objetivo de asignaciones o declaraciones "del".
La función incorporada "len()" retorna el número de elementos en un
mapeo.

Actualmente hay un único tipo de mapeo intrínseco:

#### 3.2.7.1. Diccionarios

Estos representan conjuntos finitos de objetos indexados por valores
casi arbitrarios. Los únicos tipos de valores no aceptables como
claves son valores que contienen listas o diccionarios u otros tipos
mutables que se comparan por valor en lugar de por identidad de
objeto, la razón es que la implementación eficiente de los
diccionarios requiere que el valor *hash* de una clave permanezca
constante. Los tipos numéricos utilizados para las claves obedecen las
reglas normales para la comparación numérica: si dos números se
comparan igual (por ejemplo, "1" y "1.0") entonces se pueden usar
indistintamente para indexar la misma entrada del diccionario.

Los diccionarios conservan el orden de inserción, lo que significa que
las claves se mantendrán en el mismo orden en que se agregaron
secuencialmente sobre el diccionario. Reemplazar una clave existente
no cambia el orden, sin embargo, eliminar una clave y volver a
insertarla la agregará al final en lugar de mantener su lugar
anterior.

Los diccionarios son mutables; pueden ser creados por la notación "{}"
(vea la sección Despliegues de diccionario).

Los módulos de extensión "dbm.ndbm" y "dbm.gnu" proporcionan ejemplos
adicionales de tipos de mapeo, al igual que el módulo "collections".

Distinto en la versión 3.7: Los diccionarios no conservaban el orden
de inserción en las versiones de Python anteriores a 3.6. En CPython
3.6, el orden de inserción se conserva, pero se consideró un detalle
de implementación en ese momento en lugar de una garantía de idioma.

### 3.2.8. Tipos invocables

Estos son los tipos a los que la operación de llamada de función (vea
la sección Invocaciones) puede ser aplicado:

#### 3.2.8.1. Funciones definidas por el usuario

Un objeto función definido por el usuario, es creado por un definición
de función (vea la sección Definiciones de funciones). Debe llamarse
con una lista de argumentos que contenga el mismo número de elementos
que la lista de parámetros formales de la función.

###### 3.2.8.1.1. Atributos especiales de solo lectura

+----------------------------------------------------+----------------------------------------------------+
| Atributo                                           | Significado                                        |
|====================================================|====================================================|
| function.__builtins__                              | A reference to the "dictionary" that holds the     |
|                                                    | function's builtins namespace.  Added in version   |
## |                                                    | 3.10.                                              |

| function.__globals__                               | Una referencia al "dictionary" que contiene las    |
|                                                    | global variables de la función -- el espacio de    |
|                                                    | nombres global del módulo en el que se definió la  |
## |                                                    | función.                                           |

| function.__closure__                               | "None" or a "tuple" of cells that contain bindings |
|                                                    | for the names specified in the "co_freevars"       |
|                                                    | attribute of the function's "code object".  Un     |
|                                                    | objeto de celda tiene el atributo "cell_contents". |
|                                                    | Esto se puede usar para obtener el valor de la     |
## |                                                    | celda, así como para establecer el valor.          |

###### 3.2.8.1.2. Atributos especiales de escritura

La mayoría de estos atributos verifican el tipo del valor asignado:

+----------------------------------------------------+----------------------------------------------------+
| Atributo                                           | Significado                                        |
|====================================================|====================================================|
| function.__doc__                                   | El texto de documentación de la función, o "None"  |
## |                                                    | si no está disponible.                             |

| function.__name__                                  | El nombre de la función. Vea también: "atributos   |
## |                                                    | __name__".                                         |

| function.__qualname__                              | El *qualified name* de la función. Vea también     |
## |                                                    | "atributos __qualname__".  Added in version 3.3.   |

| function.__module__                                | El nombre del módulo en el que se definió la       |
## |                                                    | función, o "None" si no está disponible.           |

| function.__defaults__                              | Una "tuple" que contiene valores de *parameter*    |
|                                                    | predeterminados para aquellos argumentos que       |
|                                                    | tienen valores predeterminados, o "None" si ningún |
## |                                                    | parámetro tiene un valor predeterminado.           |

| function.__code__                                  | El objeto de código que representa el cuerpo de la |
## |                                                    | función compilada.                                 |

| function.__dict__                                  | El espacio de nombres que admite atributos de      |
|                                                    | funciones arbitrarias. Vea también: "atributos     |
## |                                                    | __dict__".                                         |

| function.__annotations__                           | A "dictionary" containing annotations of           |
|                                                    | *parameters*. The keys of the dictionary are the   |
|                                                    | parameter names, and "'return'" for the return     |
|                                                    | annotation, if provided. See also:                 |
|                                                    | "object.__annotations__".  Distinto en la versión  |
|                                                    | 3.14: Annotations are now lazily evaluated. See    |
## |                                                    | **PEP 649**.                                       |

| function.__annotate__                              | The *annotate function* for this function, or      |
|                                                    | "None" if the function has no annotations. See     |
## |                                                    | "object.__annotate__".  Added in version 3.14.     |

| function.__kwdefaults__                            | Un "diccionario" que contiene valores              |
|                                                    | predeterminados para *parámetros* de solo palabras |
## |                                                    | clave.                                             |

| function.__type_params__                           | Un objeto "tuple" que contiene los parámetros de   |
|                                                    | tipo de una función genérica.  Added in version    |
## |                                                    | 3.12.                                              |

Los objetos de función también admiten la obtención y configuración de
atributos arbitrarios, que se pueden usar, por ejemplo, para adjuntar
metadatos a funciones. La notación de puntos de atributo regular se
utiliza para obtener y establecer dichos atributos.

La implementación actual de CPython solo admite atributos de función
en funciones definidas por el usuario. Los atributos de función en
funciones incorporadas se pueden soportar en el futuro.

Se puede obtener información adicional sobre la definición de una
función a partir de su código de objeto (accesible a través del
atributo "__code__").

#### 3.2.8.2. Métodos de instancia

Un objeto de método de instancia combina una clase, una instancia de
clase y cualquier objeto invocable (normalmente una función definida
por el usuario).

Atributos especiales de solo lectura:

+----------------------------------------------------+----------------------------------------------------+
| method.__self__                                    | Hace referencia al objeto de instancia de la clase |
## |                                                    | al que está vinculado el método                    |

## | method.__func__                                    | Hace referencia al objeto de función original      |

| method.__doc__                                     | La documentación del método (igual que             |
|                                                    | "method.__func__.__doc__"). Una "cadena de         |
|                                                    | caracteres" si la función original tenía un        |
## |                                                    | docstring, de lo contrario "None".                 |

| method.__name__                                    | El nombre del método (igual que                    |
## |                                                    | "method.__func__.__name__")                        |

| method.__module__                                  | El nombre del módulo en el que se definió el       |
## |                                                    | método, o "None" si no está disponible.            |

Los métodos también admiten obtener (más no establecer) los atributos
arbitrarios de la función en el objeto de función subyacente.

Los objetos de métodos definidos por usuarios pueden ser creados al
obtener el atributo de una clase (probablemente a través de la
instancia de dicha clase), si tal atributo es un objeto de función
definido por el usuario o un objeto "classmethod".

Cuando un objeto de instancia de método es creado al obtener un objeto
de función definida por el usuario desde una clase a través de una de
sus instancias, su atributo "__self__" es la instancia, y el objeto de
método se dice que está *enlazado*. El nuevo atributo de método
"__func__" es el objeto de función original.

Cuando un objeto de instancia de método es creado al obtener un objeto
"classmethod" a partir de una clase o instancia, su atributo
"__self__" es la clase misma, y su atributo "__func__" es el objeto de
función subyacente al método de la clase.

Cuando el objeto de la instancia de método es invocado, la función
subyacente ("__func__") es llamada, insertando la instancia de clase
("__self__") delante de la lista de argumentos. Por ejemplo, cuando
"C" es una clase que contiene la definición de una función "f()", y
"x" es una instancia de "C", invocar "x.f(1)" es equivalente a invocar
"C.f(x, 1)".

Cuando el objeto de instancia de método es derivado del objeto
"classmethod", la "instancia de clase" almacenada en "__self__" en
realidad será la clase misma, de manera que invocar ya sea "x.f(1)" o
"C.f(1)" es equivalente a invocar "f(C,1)" donde "f" es la función
subyacente.

Es importante señalar que las funciones definidas por el usuario que
son atributos de una instancia de una clase no se convierten en
métodos enlazados; esto *solo* ocurre cuando la función es un atributo
de la clase.

#### 3.2.8.3. Funciones generadoras

Una función o método que utiliza la instrucción "yield" (consulte la
sección La declaración yield) se denomina *función generadora*. Una
función de este tipo, cuando se llama, siempre retorna un objeto
*iterator* que se puede usar para ejecutar el cuerpo de la función:
llamar al método "iterator.__next__()" del iterador hará que la
función se ejecute hasta que proporcione un valor usando la
instrucción "yield". Cuando la función ejecuta una instrucción
"return" o se sale del final, se genera una excepción "StopIteration"
y el iterador habrá llegado al final del conjunto de valores que se
retornarán.

#### 3.2.8.4. Funciones de corrutina

Una función o método que es definido utilizando "async def" se llama
*coroutine function*.  Dicha función, cuando es invocada, retorna un
objeto *coroutine*.  Éste puede contener expresiones "await", así como
declaraciones "async with" y "async for". Ver también la sección
Objetos de corrutina.

#### 3.2.8.5. Funciones generadoras asincrónicas

Una función o método que se define usando "async def" y que usa la
declaración "yield" se llama *función generadora asíncrona*. Una
función de este tipo, cuando se llama, retorna un objeto *asynchronous
iterator* que se puede utilizar en una instrucción "async for" para
ejecutar el cuerpo de la función.

Llamar al método "aiterator.__anext__" del iterador asíncrono
retornará un *awaitable* que, cuando se espere, se ejecutará hasta que
proporcione un valor utilizando la expresión "yield". Cuando la
función ejecuta una instrucción "return" vacía o se sale del final, se
genera una excepción "StopAsyncIteration" y el iterador asincrónico
habrá llegado al final del conjunto de valores que se generarán.

#### 3.2.8.6. Funciones incorporadas

Un objeto de función incorporada es un envoltorio (wrapper) alrededor
de una función C. Ejemplos de funciones incorporadas son "len()" y
"math.sin()" ("math" es un módulo estándar incorporado). El número y
tipo de argumentos son determinados por la función C. Atributos
especiales de solo lectura:

* "__doc__" es el texto de documentación de la función, o "None" si no
  está disponible. Vea "function.__doc__".

* "__name__" es el nombre de la función. Vea "function.__name__".

* "__self__" se establece en "None" (pero vea el siguiente punto).

* "__module__" es el nombre del módulo en el que se definió la función
  o "None" si no está disponible. Vea "function.__module__".

#### 3.2.8.7. Métodos incorporados

Éste es realmente un disfraz distinto de una función incorporada, esta
vez teniendo un objeto que se pasa a la función C como un argumento
extra implícito. Un ejemplo de un método incorporado es
"alist.append()", asumiendo que *alist* es un objeto de lista. En este
caso, el atributo especial de solo lectura "__self__" es establecido
al objeto indicado por *alist*. (El atributo tiene la misma semántica
que con "otros métodos de instancia".)

#### 3.2.8.8. Clases

Las clases son invocables. Estos objetos normalmente actúan como
fábricas para nuevas instancias de sí mismos, pero son posibles
variaciones para los tipos de clases que anulan "__new__()". Los
argumentos de la llamada se pasan a "__new__()" y, en el caso típico,
a "__init__()" para inicializar la nueva instancia.

#### 3.2.8.9. Instancias de clases

Las instancias de clases arbitrarias se pueden hacer invocables
definiendo un método "__call__()" en su clase.

### 3.2.9. Módulos

Los módulos son una unidad básica organizacional en código Python, y
son creados por el sistema de importación al ser invocados ya sea por
la declaración "import", o invocando funciones como
"importlib.import_module()" y la incorporada "__import__()". Un objeto
de módulo tiene un espacio de nombres implementado por un objeto
"diccionario" (éste es el diccionario al que hace referencia el
atributo de funciones "__globals__" definido en el módulo). Las
referencias de atributos son traducidas a búsquedas en este
diccionario, p. ej., "m.x" es equivalente a "m.__dict__["x"]". Un
objeto de módulo no contiene el objeto de código utilizado para
iniciar el módulo (ya que no es necesario una vez que la
inicialización es realizada).

La asignación de atributos actualiza el diccionario de espacio de
nombres del módulo, p. ej., "m.x = 1" es equivalente a
"m.__dict__[“x”] = 1".

#### 3.2.9.1. Import-related attributes on module objects

Module objects have the following attributes that relate to the import
system. When a module is created using the machinery associated with
the import system, these attributes are filled in based on the
module's *spec*, before the *loader* executes and loads the module.

To create a module dynamically rather than using the import system,
it's recommended to use "importlib.util.module_from_spec()", which
will set the various import-controlled attributes to appropriate
values. It's also possible to use the "types.ModuleType" constructor
to create modules directly, but this technique is more error-prone, as
most attributes must be manually set on the module object after it has
been created when using this approach.

Prudencia:

  With the exception of "__name__", it is **strongly** recommended
  that you rely on "__spec__" and its attributes instead of any of the
  other individual attributes listed in this subsection. Note that
  updating an attribute on "__spec__" will not update the
  corresponding attribute on the module itself:

     >>> import typing
     >>> typing.__name__, typing.__spec__.name
     ('typing', 'typing')
     >>> typing.__spec__.name = 'spelling'
     >>> typing.__name__, typing.__spec__.name
     ('typing', 'spelling')
     >>> typing.__name__ = 'keyboard_smashing'
     >>> typing.__name__, typing.__spec__.name
     ('keyboard_smashing', 'spelling')

module.__name__

   The name used to uniquely identify the module in the import system.
   For a directly executed module, this will be set to ""__main__"".

   This attribute must be set to the fully qualified name of the
   module. It is expected to match the value of
   "module.__spec__.name".

module.__spec__

   A record of the module's import-system-related state.

   Set to the "module spec" that was used when importing the module.
   See Module specs for more details.

   Added in version 3.4.

module.__package__

   The *package* a module belongs to.

   If the module is top-level (that is, not a part of any specific
   package) then the attribute should be set to "''" (the empty
   string). Otherwise, it should be set to the name of the module's
   package (which can be equal to "module.__name__" if the module
   itself is a package). See **PEP 366** for further details.

   This attribute is used instead of "__name__" to calculate explicit
   relative imports for main modules. It defaults to "None" for
   modules created dynamically using the "types.ModuleType"
   constructor; use "importlib.util.module_from_spec()" instead to
   ensure the attribute is set to a "str".

   It is **strongly** recommended that you use
   "module.__spec__.parent" instead of "module.__package__".
   "__package__" is now only used as a fallback if "__spec__.parent"
   is not set, and this fallback path is deprecated.

   Distinto en la versión 3.4: This attribute now defaults to "None"
   for modules created dynamically using the "types.ModuleType"
   constructor. Previously the attribute was optional.

   Distinto en la versión 3.6: The value of "__package__" is expected
   to be the same as "__spec__.parent". "__package__" is now only used
   as a fallback during import resolution if "__spec__.parent" is not
   defined.

   Distinto en la versión 3.10: "ImportWarning" is raised if an import
   resolution falls back to "__package__" instead of
   "__spec__.parent".

   Distinto en la versión 3.12: Raise "DeprecationWarning" instead of
   "ImportWarning" when falling back to "__package__" during import
   resolution.

   Deprecated since version 3.13, will be removed in version 3.15:
   "__package__" will cease to be set or taken into consideration by
   the import system or standard library.

module.__loader__

   The *loader* object that the import machinery used to load the
   module.

   This attribute is mostly useful for introspection, but can be used
   for additional loader-specific functionality, for example getting
   data associated with a loader.

   "__loader__" defaults to "None" for modules created dynamically
   using the "types.ModuleType" constructor; use
   "importlib.util.module_from_spec()" instead to ensure the attribute
   is set to a *loader* object.

   It is **strongly** recommended that you use
   "module.__spec__.loader" instead of "module.__loader__".

   Distinto en la versión 3.4: This attribute now defaults to "None"
   for modules created dynamically using the "types.ModuleType"
   constructor. Previously the attribute was optional.

   Deprecated since version 3.12, will be removed in version 3.16:
   Setting "__loader__" on a module while failing to set
   "__spec__.loader" is deprecated. In Python 3.16, "__loader__" will
   cease to be set or taken into consideration by the import system or
   the standard library.

module.__path__

   A (possibly empty) *sequence* of strings enumerating the locations
   where the package's submodules will be found. Non-package modules
   should not have a "__path__" attribute. See __path__ attributes on
   modules for more details.

   It is **strongly** recommended that you use
   "module.__spec__.submodule_search_locations" instead of
   "module.__path__".

module.__file__

module.__cached__

   "__file__" and "__cached__" are both optional attributes that may
   or may not be set. Both attributes should be a "str" when they are
   available.

   "__file__" indicates the pathname of the file from which the module
   was loaded (if loaded from a file), or the pathname of the shared
   library file for extension modules loaded dynamically from a shared
   library. It might be missing for certain types of modules, such as
   C modules that are statically linked into the interpreter, and the
   import system may opt to leave it unset if it has no semantic
   meaning (for example, a module loaded from a database).

   If "__file__" is set then the "__cached__" attribute might also be
   set,  which is the path to any compiled version of the code (for
   example, a byte-compiled file). The file does not need to exist to
   set this attribute; the path can simply point to where the compiled
   file *would* exist (see **PEP 3147**).

   Note that "__cached__" may be set even if "__file__" is not set.
   However, that scenario is quite atypical.  Ultimately, the *loader*
   is what makes use of the module spec provided by the *finder* (from
   which "__file__" and "__cached__" are derived).  So if a loader can
   load from a cached module but otherwise does not load from a file,
   that atypical scenario may be appropriate.

   It is **strongly** recommended that you use
   "module.__spec__.cached" instead of "module.__cached__".

   Deprecated since version 3.13, will be removed in version 3.15:
   Setting "__cached__" on a module while failing to set
   "__spec__.cached" is deprecated. In Python 3.15, "__cached__" will
   cease to be set or taken into consideration by the import system or
   standard library.

#### 3.2.9.2. Other writable attributes on module objects

As well as the import-related attributes listed above, module objects
also have the following writable attributes:

module.__doc__

   The module's documentation string, or "None" if unavailable. See
   also: "__doc__ attributes".

module.__annotations__

   A dictionary containing *variable annotations* collected during
   module body execution.  For best practices on working with
   "__annotations__", see "annotationlib".

   Distinto en la versión 3.14: Annotations are now lazily evaluated.
   See **PEP 649**.

module.__annotate__

   The *annotate function* for this module, or "None" if the module
   has no annotations. See also: "__annotate__" attributes.

   Added in version 3.14.

#### 3.2.9.3. Module dictionaries

Module objects also have the following special read-only attribute:

module.__dict__

   The module's namespace as a dictionary object. Uniquely among the
   attributes listed here, "__dict__" cannot be accessed as a global
   variable from within a module; it can only be accessed as an
   attribute on module objects.

   Debido a la manera en la que CPython limpia los diccionarios de
   módulo, el diccionario de módulo será limpiado cuando el módulo se
   encuentra fuera de alcance, incluso si el diccionario aún tiene
   referencias existentes.  Para evitar esto, copie el diccionario o
   mantenga el módulo cerca mientras usa el diccionario directamente.

### 3.2.10. Clases personalizadas

Los tipos de clases personalizadas son normalmente creadas por
definiciones de clases (ver sección Definiciones de clase). Una clase
tiene implementado un espacio de nombres por un objeto de diccionario.
Las referencias de atributos de clase son traducidas a búsquedas en
este diccionario, p. ej., "C.x" es traducido a "C.__dict__["x"]"
(aunque hay una serie de enlaces que permiten la ubicación de
atributos por otros medios). Cuando el nombre de atributo no es
encontrado ahí, la búsqueda de atributo continúa en las clases base.
Esta búsqueda de las clases base utiliza la orden de resolución de
métodos C3 que se comporta correctamente aún en la presencia de
estructuras de herencia 'diamante' donde existen múltiples rutas de
herencia que llevan a un ancestro común. Detalles adicionales en el
MRO C3 utilizados por Python pueden ser encontrados en The Python 2.3
Method Resolution Order.

Cuando la referencia de un atributo de clase (digamos, para la clase
"C") produce un objeto de método de clase, éste es transformado a un
objeto de método de instancia cuyo atributo "__self__" es "C". Cuando
produce un objeto "staticmethod", éste es transformado al objeto
envuelto por el objeto de método estático. Ver sección Implementando
descriptores para otra manera en la que los atributos obtenidos de una
clase pueden diferir de los que en realidad están contenidos en su
"__dict__".

Las asignaciones de atributos de clase actualizan el diccionario de la
clase, nunca el diccionario de la clase base.

Un objeto de clase puede ser invocado (ver arriba) para producir una
instancia de clase (ver a continuación).

#### 3.2.10.1. Atributos especiales

+----------------------------------------------------+----------------------------------------------------+
| Atributo                                           | Significado                                        |
|====================================================|====================================================|
| type.__name__                                      | El nombre de la clase. Vea también: "atributos     |
## |                                                    | __name__".                                         |

| type.__qualname__                                  | El *qualified name* de la clase. Vea también:      |
## |                                                    | "atributos __qualname__".                          |

| type.__module__                                    | El nombre del módulo en el que se definió la       |
## |                                                    | clase.                                             |

| type.__dict__                                      | Un "proxy de mapeo" que proporciona una vista de   |
|                                                    | solo lectura del espacio de nombres de la clase.   |
## |                                                    | Vea también: "atributos __dict__".                 |

| type.__bases__                                     | Un objeto "tuple" que contiene las bases de la     |
|                                                    | clase. En la mayoría de los casos, para una clase  |
|                                                    | definida como "class X(A, B, C)", "X.__bases__"    |
## |                                                    | será exactamente igual a "(A, B, C)".              |

| type.__base__                                      | **Detalles de implementación de CPython:** The     |
|                                                    | single base class in the inheritance chain that is |
|                                                    | responsible for the memory layout of instances.    |
|                                                    | This attribute corresponds to "tp_base" at the C   |
## |                                                    | level.                                             |

| type.__doc__                                       | El texto de documentación de la clase, o "None" si |
## |                                                    | no está disponible. No heredado por subclases.     |

| type.__annotations__                               | A dictionary containing *variable annotations*     |
|                                                    | collected during class body execution. See also:   |
|                                                    | "__annotations__ attributes".  For best practices  |
|                                                    | on working with "__annotations__", please see      |
|                                                    | "annotationlib". Use                               |
|                                                    | "annotationlib.get_annotations()" instead of       |
|                                                    | accessing this attribute directly.  Advertencia:   |
|                                                    | Accessing the "__annotations__" attribute directly |
|                                                    | on a class object may return annotations for the   |
|                                                    | wrong class, specifically in certain cases where   |
|                                                    | the class, its base class, or a metaclass is       |
|                                                    | defined under "from __future__ import              |
|                                                    | annotations". See **749** for details.This         |
|                                                    | attribute does not exist on certain builtin        |
|                                                    | classes. On user-defined classes without           |
|                                                    | "__annotations__", it is an empty dictionary.      |
|                                                    | Distinto en la versión 3.14: Annotations are now   |
## |                                                    | lazily evaluated. See **PEP 649**.                 |

| type.__annotate__()                                | The *annotate function* for this class, or "None"  |
|                                                    | if the class has no annotations. See also:         |
## |                                                    | "__annotate__ attributes".  Added in version 3.14. |

| type.__type_params__                               | Una objeto "tuple" que contiene parámetros de tipo |
## |                                                    | de una clase genérica.  Added in version 3.12.     |

| type.__static_attributes__                         | Un objeto "tuple" que contiene nombres de          |
|                                                    | atributos de esta clase que se asignan a través de |
|                                                    | "self.X" desde cualquier función en su cuerpo.     |
## |                                                    | Added in version 3.13.                             |

| type.__firstlineno__                               | The line number of the first line of the class     |
|                                                    | definition, including decorators. Setting the      |
|                                                    | "__module__" attribute removes the                 |
|                                                    | "__firstlineno__" item from the type's dictionary. |
## |                                                    | Added in version 3.13.                             |

| type.__mro__                                       | El objeto "tuple" de clases que se consideran al   |
|                                                    | buscar clases base durante la resolución del       |
## |                                                    | métodos.                                           |

#### 3.2.10.2. Métodos especiales

Además de los atributos especiales descritos anteriormente, todas las
clases de Python también tienen los siguientes dos métodos
disponibles:

type.mro()

   Este método se puede anular por una metaclase para personalizar el
   orden de resolución de métodos para sus instancias. Se llama en la
   instanciación de la clase, y su resultado se almacena en "__mro__".

type.__subclasses__()

   Cada clase mantiene una lista de referencias débiles a sus
   subclases inmediatas. Este método retorna una lista de todas esas
   referencias aún vivas. La lista está en orden de definición.
   Ejemplo:

      >>> class A: pass
      >>> class B(A): pass
      >>> A.__subclasses__()
      [<class 'B'>]

### 3.2.11. Instancias de clase

Una instancia de clase se crea llamando a un objeto de clase (ver
arriba). Una instancia de clase tiene un espacio de nombres
implementado como un diccionario, que es el primer lugar en el que se
buscan las referencias de atributos. Cuando no se encuentra un
atributo allí y la clase de la instancia tiene un atributo con ese
nombre, la búsqueda continúa con los atributos de la clase. Si se
encuentra un atributo de clase que es un objeto de función definido
por el usuario, se transforma en un objeto de método de instancia cuyo
atributo "__self__" es la instancia. Los objetos de métodos estáticos
y de clases también se transforman; consulte más arriba en "Clases".
Consulte la sección Implementando descriptores para conocer otra forma
en la que los atributos de una clase recuperados a través de sus
instancias pueden diferir de los objetos realmente almacenados en el
"__dict__" de la clase. Si no se encuentra ningún atributo de clase y
la clase del objeto tiene un método "__getattr__()", se llama para
satisfacer la búsqueda.

Las asignaciones y eliminaciones de atributos actualizan el
diccionario de la instancia, nunca el diccionario de una clase. Si la
clase tiene un método "__setattr__()" o "__delattr__()", se llama a
este en lugar de actualizar el diccionario de instancia directamente.

Instancias de clases pueden pretender ser números, secuencias o mapeos
si tienen métodos con ciertos nombres especiales.  Ver sección Nombres
especiales de método.

#### 3.2.11.1. Atributos especiales

object.__class__

   La clase a la que pertenece una instancia de clase.

object.__dict__

   Un diccionario u otro objeto de mapeo utilizado para almacenar los
   atributos (escribibles) de un objeto. No todas las instancias
   tienen un atributo "__dict__"; vea la sección sobre __slots__ para
   más detalles.

### 3.2.12. Objetos E/S (también conocidos como objetos de archivo)

Un *file object* representa un archivo abierto.  Diversos accesos
directos se encuentran disponibles para crear objetos de archivo: la
función incorporada "open()", así como "os.popen()", "os.fdopen()", y
el método de objetos socket "makefile()" (y quizás por otras funciones
y métodos proporcionados por módulos de extensión).

File objects implement common methods, listed below, to simplify usage
in generic code. They are expected to be Gestores de Contexto en la
Declaración with.

Los objetos "sys.stdin", "sys.stdout" y "sys.stderr" son iniciados a
objetos de archivos correspondientes a la entrada y salida estándar
del intérprete, así como flujos de error; todos ellos están abiertos
en el modo de texto y por lo tanto siguen la interface definida por la
clase abstracta "io.TextIOBase".

file.read(size=-1, /)

   Retrieve up to *size* data from the file. As a convenience if
   *size* is unspecified or -1 retrieve all data available.

file.write(data, /)

   Store *data* to the file.

file.close()

   Flush any buffers and close the underlying file.

### 3.2.13. Tipos internos

Algunos tipos utilizados internamente por el intérprete son expuestos
al usuario. Sus definiciones pueden cambiar en futuras versiones del
intérprete, pero son mencionadas aquí para complementar.

#### 3.2.13.1. Objetos de código

Los objetos de código representan código de Python ejecutable
*compilado por bytes*, o *bytecode*. La diferencia entre un objeto de
código y un objeto de función es que el objeto de función contiene una
referencia explícita a los globales de la función (el módulo en el que
fue definido), mientras el objeto de código no contiene contexto; de
igual manera los valores por defecto de los argumentos son almacenados
en el objeto de función, no en el objeto de código (porque representan
valores calculados en tiempo de ejecución).  A diferencia de objetos
de función, los objetos de código son inmutables y no contienen
referencias (directas o indirectas) a objetos mutables.

###### 3.2.13.1.1. Atributos especiales de solo lectura

# | codeobject.co_name                                 | El nombre de la función                            |

| codeobject.co_qualname                             | El nombre de la función completamente calificado   |
## |                                                    | Added in version 3.11.                             |

| codeobject.co_argcount                             | El número total de *parámetros* posicionales       |
|                                                    | (incluye los parámetros solo posicionales y los    |
|                                                    | parámetros con valores predeterminados) que tiene  |
## |                                                    | la función                                         |

| codeobject.co_posonlyargcount                      | El número de *parámetros* solo posicionales        |
|                                                    | (incluye argumentos con valores predeterminados)   |
## |                                                    | que tiene la función                               |

| codeobject.co_kwonlyargcount                       | El número de *parámetros* de solo palabras clave   |
|                                                    | (incluye argumentos con valores predeterminados)   |
## |                                                    | que tiene la función                               |

| codeobject.co_nlocals                              | El número de variables locales utilizadas por la   |
## |                                                    | función (incluye los parámetros)                   |

| codeobject.co_varnames                             | Un objeto "tuple" que contiene los nombres de las  |
|                                                    | variables locales en la función (empezando por los |
## |                                                    | nombres de los parámetros)                         |

| codeobject.co_cellvars                             | A "tuple" containing the names of local variables  |
|                                                    | that are referenced from at least one *nested      |
## |                                                    | scope* inside the function                         |

| codeobject.co_freevars                             | A "tuple" containing the names of *free (closure)  |
|                                                    | variables* that a *nested scope* references in an  |
|                                                    | outer scope. See also "function.__closure__".      |
|                                                    | Note: references to global and builtin names are   |
## |                                                    | *not* included.                                    |

| codeobject.co_code                                 | Una cadena de caracteres que representa la         |
|                                                    | secuencia de instrucciones *bytecode* en la        |
## |                                                    | función                                            |

| codeobject.co_consts                               | Un objeto "tuple" que contiene los literales       |
## |                                                    | utilizados por *bytecode* en la función            |

| codeobject.co_names                                | Un objeto "tuple" que contiene los nombres         |
## |                                                    | utilizados por *bytecode* en la función            |

| codeobject.co_filename                             | El nombre del archivo en el que se compiló el      |
## |                                                    | código                                             |

| codeobject.co_firstlineno                          | El número de línea de la primer línea de la        |
## |                                                    | función                                            |

| codeobject.co_lnotab                               | Una cadena de caracteres que codifica la           |
|                                                    | asignación de los desplazamientos de *bytecode* a  |
|                                                    | los números de línea. Para obtener más detalles,   |
|                                                    | vea el código fuente del intérprete.  Obsoleto     |
|                                                    | desde la versión 3.12: This attribute of code      |
|                                                    | objects is deprecated, and may be removed in       |
## |                                                    | Python 3.15.                                       |

## | codeobject.co_stacksize                            | El tamaño de pila requerido del objeto de código   |

| codeobject.co_flags                                | Un "entero" que codifica un número de banderas     |
## |                                                    | para el intérprete.                                |

Los siguientes bits de bandera son definidos por "co_flags": el bit
"0x04" es establecido si la función utiliza la sintaxis "*arguments"
para aceptar un número arbitrario de argumentos posicionales; el bit
"0x08" es establecido si la función utiliza la sintaxis "**keywords"
para aceptar argumentos de palabras clave arbitrarios; el bit "0x20"
es establecido si la función es un generador. Vea Objetos de código
Bit Flags para más detalles sobre la semántica de cada bandera que
pueda estar presente.

Future feature declarations (for example, "from __future__ import
division") also use bits in "co_flags" to indicate whether a code
object was compiled with a particular feature enabled. See
"compiler_flag".

Otros bits en "co_flags" son reservados para uso interno.

If a code object represents a function and has a docstring, the
"CO_HAS_DOCSTRING" bit is set in "co_flags" and the first item in
"co_consts" is the docstring of the function.

###### 3.2.13.1.2. Métodos en objetos de código

codeobject.co_positions()

   Retorna un iterable sobre las posiciones del código fuente de cada
   instrucción de *bytecode* en el objeto de código.

   El iterador retorna objetos "tuple" que contienen "(start_line,
   end_line, start_column, end_column)". La tupla *i-ésima*
   corresponde a la posición del código fuente que se compiló en la
   unidad de código *i-ésima*. La información de la columna son
   desplazamientos de bytes utf-8 indexados en 0 en la línea de origen
   dada.

   Esta información posicional puede faltar. Una lista no exhaustiva
   de casos en los que esto puede suceder:

   * Ejecutando el intérprete con "-X" "no_debug_ranges".

   * Cargando un archivo pyc compilado usando "-X" "no_debug_ranges".

   * Tuplas de posición correspondientes a instrucciones artificiales.

   * Números de línea y columna que no se pueden representar debido a
     limitaciones específicas de la implementación.

   Cuando esto ocurre, algunos o todos los elementos de la tupla
   pueden ser "None".

   Added in version 3.11.

   Nota:

     Esta función requiere el almacenamiento de posiciones de columna
     en objetos de código, lo que puede resultar en un pequeño aumento
     del uso del disco de archivos de Python compilados o del uso de
     la memoria del intérprete. Para evitar almacenar la información
     extra y/o desactivar la impresión de la información extra de
     seguimiento, se puede usar el indicador de línea de comando "-X"
     "no_debug_ranges" o la variable de entorno "PYTHONNODEBUGRANGES".

codeobject.co_lines()

   Retorna un iterador que produce información sobre rangos sucesivos
   de objetos *bytecode*. Cada elemento que se produjo es un objeto
   "tuple" "(start, end, lineno)":

   * "start" (un objeto "int") representa el desplazamiento
     (inclusivo) del inicio del rango de *bytecode*

   * "end" (un objeto "int") representa el desplazamiento (exclusivo)
     del final del rango de *bytecode*

   * "lineno" es un objeto "int" que representa el número de línea del
     rango de *bytecode*, o "None" si los códigos de bytes en el rango
     dado no tienen número de línea

   Los elementos producidos tendrán las siguientes propiedades:

   * El primer rango producido tendrá un elemento "start" de 0.

   * Los rangos "(start, end)" serán no decrecientes y consecutivos.
     Esto es, para cualquier par de objetos "tuple", el elemento
     "start" del segundo será igual al elemento "end" del primero.

   * Ningún rango será inverso: "end >= start" para todas las
     tripletas.

   * El último objeto "tuple" producido tendrá el elemento "end" igual
     al tamaño de *bytecode*.

   Se permiten rangos de ancho cero, donde "start == end". Los rangos
   de ancho cero se utilizan para las líneas que están presentes en el
   código fuente, pero que han sido eliminadas por el compilador
   *bytecode*.

   Added in version 3.10.

   Ver también:

     **PEP 626** - Números de línea precisos para depuración y otras
     herramientas.
        El PEP que introdujo el método "co_lines()".

codeobject.replace(**kwargs)

   Retorna una copia del objeto de código con nuevos valores para los
   campos especificados.

   Los objetos de código también son compatibles con la función
   genérica "copy.replace()".

   Added in version 3.8.

#### 3.2.13.2. Objetos de marco

Los objetos de marco representan marcos de ejecución. Pueden ocurrir
en objetos de rastreo, y son también pasados hacia funciones de
rastreo registradas.

###### 3.2.13.2.1. Atributos especiales de solo lectura

+----------------------------------------------------+----------------------------------------------------+
| frame.f_back                                       | Apunta al marco de pila anterior (hacia el que     |
|                                                    | hace la llamada), o "None" si este es el marco de  |
## |                                                    | pila inferior                                      |

| frame.f_code                                       | El objeto de código que se está ejecutando en este |
|                                                    | marco. Al acceder a este atributo se lanza un      |
|                                                    | evento de auditoría "object.__getattr__" con los   |
## |                                                    | argumentos "obj" y ""f_code"".                     |

| frame.f_locals                                     | La asignación que utiliza el marco para buscar     |
|                                                    | variables locales. Si el marco hace referencia a   |
|                                                    | un *ámbito optimizado*, esto puede retornar un     |
|                                                    | objeto proxy de escritura directa.  Distinto en la |
|                                                    | versión 3.13: Retorna un proxy para ámbitos        |
## |                                                    | optimizados.                                       |

| frame.f_globals                                    | El diccionario utilizado por el marco para buscar  |
## |                                                    | variables globales                                 |

| frame.f_builtins                                   | El diccionario utilizado por el marco para buscar  |
## |                                                    | nombres incorporados (intrínsecos)                 |

| frame.f_lasti                                      | La "instrucción precisa" del objeto de marco (es   |
|                                                    | un índice en la cadena *bytecode* del objeto de    |
## |                                                    | código)                                            |

| frame.f_generator                                  | The *generator* or *coroutine* object that owns    |
|                                                    | this frame, or "None" if the frame is a normal     |
## |                                                    | function.  Added in version 3.14.                  |

###### 3.2.13.2.2. Atributos especiales de escritura

+----------------------------------------------------+----------------------------------------------------+
| frame.f_trace                                      | Si no es "None", esta es una función llamada por   |
|                                                    | distintos eventos durante la ejecución del código  |
|                                                    | (esto es utilizado por depuradores). Normalmente   |
|                                                    | un evento es desencadenado por cada nueva línea    |
## |                                                    | fuente (vea "f_trace_lines").                      |

| frame.f_trace_lines                                | Establece este atributo a "False" para             |
|                                                    | deshabilitar la activación de un evento de         |
## |                                                    | seguimiento para cada línea de origen.             |

| frame.f_trace_opcodes                              | Establece este atributo a "True" para permitir que |
|                                                    | se soliciten eventos por código de operación.      |
|                                                    | Tenga en cuenta que esto puede llevar a un         |
|                                                    | comportamiento indefinido del intérprete si se     |
|                                                    | levantan excepciones por la función de rastreo     |
## |                                                    | escape hacia la función que está siendo rastreada. |

| frame.f_lineno                                     | El número de línea actual del marco -- escribiendo |
|                                                    | a esta forma dentro de una función de rastreo      |
|                                                    | salta a la línea dada (solo para el último marco). |
|                                                    | Un depurador puede implementar un comando de salto |
|                                                    | (*Jump*) (también conocido como *Set Next          |
## |                                                    | Statement*) al escribir en este atributo.          |

###### 3.2.13.2.3. Métodos de objeto de marco

Objetos de marco soportan un método:

frame.clear()

   Este método limpia todas las referencias a variables locales
   mantenidas por el marco. También, si el marco pertenecía a un
   *generator*, éste es finalizado. Esto ayuda a interrumpir los
   ciclos de referencia que involucran objetos de marco (por ejemplo
   al detectar una excepción y almacenando su rastro para uso
   posterior).

   "RuntimeError" es lanzado si el marco se encuentra actualmente en
   ejecución o suspendido.

   Added in version 3.4.

   Distinto en la versión 3.13: Al intentar borrar un marco suspendido
   lanza "RuntimeError" (como siempre ha sido el caso con los marcos
   en ejecución).

#### 3.2.13.3. Objetos de seguimiento de pila (traceback)

Los objetos de seguimiento de pila representan el trazo de pila
(*stack trace*) de una excepción. Un objeto de rastreo es creado de
manera implícita cuando se da una excepción, y puede ser creada de
manera explícita al llamar "types.TracebackType".

Distinto en la versión 3.7: Los objetos de seguimiento de pila ya
pueden ser instanciados de manera explícita desde código de Python.

Para seguimientos de pila (tracebacks) creados de manera implícita,
cuando la búsqueda por un manejo de excepciones desenvuelve la pila de
ejecución, en cada nivel de desenvolvimiento se inserta un objeto de
rastreo al frente del rastreo actual. Cuando se entra a un manejo de
excepción, la pila de rastreo se vuelve disponible para el programa.
(Ver sección La sentencia try.) Es accesible como el tercer elemento
de la tupla retornada por "sys.exc_info()", y como el atributo
"__traceback__" de la excepción capturada.

Cuando el programa no contiene un gestor apropiado, el trazo de pila
es escrito (muy bien formateado) en el flujo de error estándar; si el
intérprete es interactivo, también se vuelve disponible al usuario
como "sys.last_traceback".

Para seguimientos de pila creados de forma explícita, depende de su
creador determinar cómo los atributos "tb_next" deberían ser ligados
para formar un trazo de pila completo (*full stack trace*).

Atributos especiales de solo lectura:

+----------------------------------------------------+----------------------------------------------------+
| traceback.tb_frame                                 | Apunta al marco de ejecución del nivel actual.     |
|                                                    | Acceder a este atributo lanza un objeto evento de  |
|                                                    | auditoría "object.__getattr__" con argumentos      |
## |                                                    | "obj" y ""tb_frame"".                              |

| traceback.tb_lineno                                | Indica el número de línea en la que se ha          |
## |                                                    | producido la excepción                             |

## | traceback.tb_lasti                                 | Indica la "instrucción precisa".                   |

El número de línea y la última instrucción en el seguimiento de pila
puede diferir del número de línea de su objeto de marco si la
excepción ocurrió en una declaración "try" sin una cláusula de
excepción (except) correspondiente o con una cláusula "finally".

traceback.tb_next

   El atributo especial escribible "tb_next" es el siguiente nivel en
   el trazo de pila (hacia el marco en donde ocurrió la excepción), o
   "None" si no existe un siguiente nivel.

   Distinto en la versión 3.7: Este atributo es ahora escribible

#### 3.2.13.4. Objetos de segmento (Slice objects)

Los objetos de sector se utilizan para representar sectores para
métodos "__getitem__()". También son creados por la función integrada
"slice()".

Atributos especiales de solo lectura: "start" es el límite inferior;
"stop" es el límite superior; "step" es el valor de paso; cada uno es
"None" si es omitido. Estos atributos pueden ser de cualquier tipo.

Los objetos de segmento soportan un método:

slice.indices(self, length)

   Este método toma un argumento *length* de entero simple y calcula
   información relacionada con el segmento que el mismo describiría si
   fuera aplicado a una secuencia de elementos *length*. Retorna una
   tupla de tres enteros; respectivamente estos son los índices
   *start* y *stop* y el *step* o longitud del paso del segmento.
   Índices faltantes o fuera de los límites son manipulados de manera
   consistente con segmentos regulares.

#### 3.2.13.5. Objetos de método estático

Los objetos de método estático proveen una forma de anular la
transformación de objetos de función a objetos de método descritos
anteriormente. Un objeto de método estático es una envoltura
(*wrapper*) alrededor de cualquier otro objeto, usualmente un objeto
de método definido por usuario. Cuando un objeto de método estático es
obtenido desde una clase o una instancia de clase, usualmente el
objeto retornado es el objeto envuelto, el cual no está objeto a
ninguna transformación adicional. Los objetos de método estático
también pueden ser llamados. Los objetos de método estático son
creados por el constructor incorporado "staticmethod()".

#### 3.2.13.6. Objetos de método de clase

Un objeto de método de clase, igual que un objeto de método estático,
es un envoltorio (wrapper) alrededor de otro objeto que altera la
forma en la que el objeto es obtenido desde las clases y las
instancias de clase. El comportamiento de los objetos de método de
clase sobre tal obtención es descrita más arriba, debajo de "métodos
de instancia". Objetos de clase de método son creados por el
constructor incorporado "classmethod()".

## 3.3. Nombres especiales de método

Una clase puede implementar ciertas operaciones que se invocan
mediante una sintaxis especial (como operaciones aritméticas o
subíndices y divisiones) definiendo métodos con nombres especiales.
Este es el enfoque de Python para *sobrecarga de operadores*,
permitiendo a las clases definir su propio comportamiento con respecto
a los operadores del lenguaje. Por ejemplo, si una clase define un
método denominado "__getitem__()" y "x" es una instancia de esta
clase, entonces "x[i]" es aproximadamente equivalente a
"type(x).__getitem__(x, i)". Excepto donde se mencione, los intentos
de ejecutar una operación generan una excepción cuando no se define
ningún método apropiado (normalmente "AttributeError" o "TypeError").

Establecer un método especial en "None" indica que la operación
correspondiente no está disponible. Por ejemplo, si una clase
establece "__iter__()" en "None", la clase no es iterable, por lo que
llamar a "iter()" en sus instancias generará un "TypeError" (sin
recurrir a "__getitem__()"). [2]

When implementing a class that emulates any built-in type, it is
important that the emulation only be implemented to the degree that it
makes sense for the object being modelled.  For example, some
sequences may work well with retrieval of individual elements, but
extracting a slice may not make sense. (One example of this is the
NodeList interface in the W3C's Document Object Model.)

### 3.3.1. Personalización básica

object.__new__(cls[, ...])

   Es llamado para crear una nueva instancia de clase *cls*.
   "__new__()" es un método estático (como un caso especial, así que
   no se necesita declarar como tal) que toma la clase de donde fue
   solicitada una instancia como su primer argumento. Los argumentos
   restantes son aquellos que se pasan a la expresión del constructor
   de objetos (para llamar a la clase). El valor retornado de
   "__new__()" deberá ser la nueva instancia de objeto (normalmente
   una instancia de *cls*).

   Las implementaciones típicas crean una nueva instancia de la clase
   invocando el método "__new__()" de la superclase usando
   "super().__new__(cls[, ...])" con los argumentos apropiados y luego
   modificando la instancia recién creada según sea necesario antes de
   retornarla.

   Si "__new__()" es invocado durante la construcción del objeto y
   éste retorna una instancia de *cls*, entonces el nuevo método
   "__init__()" de la instancia será invocado como "__init__(self[,
   …])", donde *self* es la nueva instancia y los argumentos restantes
   son iguales a como fueron pasados hacia el constructor de objetos.

   Si "__new__()" no retorna una instancia de *cls*, entonces el nuevo
   método "__init__()" de la instancia no será invocado.

   "__new__()" es destinado principalmente para permitir a subclases
   de tipos inmutables (como int, str, o tuple) personalizar la
   creación de instancias. También es comúnmente anulado en metaclases
   personalizadas con el fin de personalizar la creación de clase.

object.__init__(self[, ...])

   Llamado después de que la instancia ha sido creada (por
   "__new__()"), pero antes es retornada a quien produce la llamada.
   Los argumentos son aquellos pasados a la expresión del constructor
   de la clase. Si una clase base tiene un método "__init__()", el
   método "__init__()" de clase derivada, de existir, debe llamarlo
   explícitamente para asegurar la inicialización apropiada de la
   clase base que es parte de la instancia; por ejemplo:
   "super().__init__([args…])".

   Debido a que "__new__()" y "__init__()" trabajan juntos
   construyendo objetos ("__new__()" para crearlo y "__init__()" para
   personalizarlo), ningún valor distinto a "None" puede ser retornado
   por "__init__()"; hacer esto puede causar que se lance una
   excepción "TypeError" en tiempo de ejecución.

object.__del__(self)

   Llamado cuando la instancia es a punto de ser destruida. Esto
   también es llamado finalizador o (indebidamente) destructor. Si una
   clase base tiene un método "__del__()" el método "__del__()" de la
   clase derivada, de existir, debe llamarlo explícitamente para
   asegurar la eliminación adecuada de la parte de la clase base de la
   instancia.

   Es posible (¡aunque no recomendable!) para el método "__del__()"
   posponer la destrucción de la instancia al crear una nueva
   referencia hacia ésta. Esto es llamado *resurrección* de objeto. Es
   dependiente de la implementación si "__del__()" es llamado una
   segunda vez cuando un objeto resucitado está por ser destruido; la
   implementación *CPython* actual únicamente lo llama una vez.

   No está garantizado que los métodos "__del__()" sean llamados para
   objetos que aún existen cuando el intérprete se cierra.
   "weakref.finalize" proporciona una forma directa de registrar una
   función de limpieza para ser llamada cuando un objeto es recogido
   de la basura.

   Nota:

     "del x" no llama directamente "x.__del__()" --- el primero
     disminuye el conteo de referencia para "x" uno por uno, y el
     segundo es llamado únicamente cuando el conteo de referencias de
     "x" llega a cero.

   Es posible que un ciclo de referencia evite que el recuento de
   referencia de un objeto llegue a cero. En este caso, el ciclo será
   posteriormente detectado y eliminado por el *cyclic garbage
   collector*. Una causa común de los ciclos de referencia es cuando
   se detecta una excepción en una variable local. Luego, los locales
   del marco hacen referencia a la excepción, que hace referencia a su
   propio rastreo, que hace referencia a los locales de todos los
   marcos capturados en el rastreo.

   Ver también: Documentación para el módulo "gc".

   Advertencia:

     Debido a las circunstancias inciertas bajo las que los métodos
     "__del__()" son invocados, las excepciones que ocurren durante su
     ejecución son ignoradas, y una advertencia es mostrada hacia
     "sys.stderr". En particular:

     * "__del__()" puede ser invocado cuando código arbitrario es
       ejecutado, incluyendo el de cualquier hilo arbitrario. Si
       "__del__()" necesita realizar un cierre de exclusión mutua
       (*lock*) o invocar cualquier otro recurso que lo esté
       bloqueando, podría provocar un bloqueo muto (*deadlock*) ya que
       el recurso podría estar siendo utilizado por el código que se
       interrumpe al ejecutar "__del__()".

     * "__del__()" puede ser ejecutado durante el cierre del
       intérprete. Como consecuencia, las variables globales que
       necesita para acceder (incluyendo otros módulos) podrían haber
       sido borradas o establecidas a "None". Python garantiza que los
       globales cuyo nombre comienza con un guión bajo simple sean
       borrados de su módulo antes que los globales sean borrados; si
       no existen otras referencias a dichas globales, esto puede
       ayudar asegurando que los módulos importados aún se encuentren
       disponibles al momento de llamar al método "__del__()".

object.__repr__(self)

   Llamado por la función incorporada "repr()" para calcular la cadena
   “oficial” de representación de un objeto. Si es posible, esto
   debería verse como una expresión de Python válida que puede ser
   utilizada para recrear un objeto con el mismo valor (bajo el
   ambiente adecuado). Si no es posible, una cadena con la forma
   "<…some useful description…>" debe ser retornada. El valor de
   retorno debe ser un objeto de cadena (*string*). Si una clase
   define "__repr__()" pero no "__str__()", entonces "__repr__()"
   también es utilizado cuando una cadena “informal” de representación
   de instancias de esas clases son requeridas.

   This is typically used for debugging, so it is important that the
   representation is information-rich and unambiguous. A default
   implementation is provided by the "object" class itself.

object.__str__(self)

   Called by "str(object)", the default "__format__()" implementation,
   and the built-in function "print()", to compute the "informal" or
   nicely printable string representation of an object.  The return
   value must be a str object.

   Este método difiere de "object.__repr__()" en que no hay
   expectativas de que "__str__()" retorne una expresión de Python
   válida: una representación más conveniente o concisa pueda ser
   utilizada.

   La implementación por defecto definida por el tipo incorporado
   "object" llama a "object.__repr__()".

object.__bytes__(self)

   Called by bytes to compute a byte-string representation of an
   object. This should return a "bytes" object. The "object" class
   itself does not provide this method.

object.__format__(self, format_spec)

   Llamado por la función incorporada "format()", y por extensión, la
   evaluación de formatted string literals y el método "str.format()",
   para producir la representación “formateada” de un objeto. El
   argumento *format_spec* es una cadena que contiene una descripción
   de las opciones de formato deseadas. La interpretación del
   argumento *format_spec* depende del tipo que implementa
   "__format__()", sin embargo, ya sea que la mayoría de las clases
   deleguen el formato a uno de los tipos incorporados, o utilicen una
   sintaxis de opción de formato similar.

   Ver Format specification mini-language para una descripción de la
   sintaxis de formato estándar.

   El valor de retorno debe ser un objeto de cadena.

   The default implementation by the "object" class should be given an
   empty *format_spec* string. It delegates to "__str__()".

   Distinto en la versión 3.4: El método __format__ del mismo "object"
   lanza un "TypeError" si se la pasa una cadena no vacía.

   Distinto en la versión 3.7: "object.__format__(x, ‘’)" es ahora
   equivalente a "str(x)" en lugar de "format(str(self), ‘’)".

object.__lt__(self, other)
object.__le__(self, other)
object.__eq__(self, other)
object.__ne__(self, other)
object.__gt__(self, other)
object.__ge__(self, other)

   Estos son los llamados métodos de comparación *rich*. La
   correspondencia entre símbolos de operador y los nombres de método
   es de la siguiente manera: "x<y" llama "x.__lt__(y)", "x<=y" llama
   "x.__le__(y)", "x==y" llama "x.__eq__(y)", "x!=y" llama
   "x.__ne__(y)", "x>y" llama "x.__gt__(y)", y "x>=y" llama
   "x.__ge__(y)".

   Un método de comparación enriquecido puede retornar el único
   "NotImplemented" si no implementa la operación para un par de
   argumentos dados. Por convención, "False" y "True" son retornados
   para una comparación exitosa. Sin embargo, estos métodos pueden
   retornar cualquier valor, así que si el operador de comparación es
   utilizado en un contexto Booleano (p. ej. en la condición de una
   sentencia "if"), Python llamará "bool()" en dicho valor para
   determinar si el resultado es verdadero (*true*) o falso (*false*).

   By default, "object" implements "__eq__()" by using "is", returning
   "NotImplemented" in the case of a false comparison: "True if x is y
   else NotImplemented". For "__ne__()", by default it delegates to
   "__eq__()" and inverts the result unless it is "NotImplemented".
   There are no other implied relationships among the comparison
   operators or default implementations; for example, the truth of
   "(x<y or x==y)" does not imply "x<=y". To automatically generate
   ordering operations from a single root operation, see
   "@functools.total_ordering".

   By default, the "object" class provides implementations consistent
   with Comparaciones de valor: equality compares according to object
   identity, and order comparisons raise "TypeError". Each default
   method may generate these results directly, but may also return
   "NotImplemented".

   Ver el párrafo sobre "__hash__()" para más notas importantes sobre
   la creación de objetos *hashable* que soportan operaciones de
   comparación personalizadas y son utilizables como llaves de
   diccionario.

   No existen versiones con argumento intercambiado de estos métodos
   (a ser utilizados cuando el argumento de la izquierda no soporta la
   operación pero el de la derecha sí); más bien, "__lt__()" y
   "__gt__()" son el reflejo del otro, "__le__()" y "__ge__()" son un
   reflejo del otro, y "__eq__()" y "__ne__()" son su propio reflejo.
   Si los operandos son de tipos distintos, y el tipo de operando de
   la derecha es una subclase directa o indirecta del tipo de operando
   de la izquierda, el método reflejado del operando de la derecha
   tiene prioridad, de otro modo el método del operando de la
   izquierda tiene prioridad. Subclases virtuales no son consideradas.

   Cuando ningún método retorna un valor distinto de "NotImplemented",
   los operadores "==" y "!=" vuelven a "is" y "is not",
   respectivamente.

object.__hash__(self)

   Lo llama la función integrada "hash()" y para operaciones en
   miembros de colecciones hash, incluidas "set", "frozenset" y
   "dict". El método "__hash__()" debería retornar un número entero.
   La única propiedad requerida es que los objetos que se comparan
   iguales tengan el mismo valor hash; Se recomienda mezclar los
   valores hash de los componentes del objeto que también desempeñan
   un papel en la comparación de objetos empaquetándolos en una tupla
   y aplicando hash a la tupla. Ejemplo:

      def __hash__(self):
          return hash((self.name, self.nick, self.color))

   Nota:

     "hash()" trunca el valor retornado del método personalizado
     "__hash__()" del objeto al tamaño de "Py_ssize_t". Esto
     normalmente son 8 bytes en estructuras de 64-bits y 4 bytes en
     estructuras de 32 bits. Si el "__hash__()" de un objeto debe
     interoperar en estructuras de tamaños de bits diferentes,
     asegúrese de revisar la amplitud en todas las estructuras
     soportadas. Una forma fácil de hacer esto es con "python -c
     “import sys; print(sys.hash_info.width)”".

   Si una clase no define un método "__eq__()" tampoco debería definir
   una operación "__hash__()"; si define "__eq__()" pero no
   "__hash__()", sus instancias no se podrán utilizar como elementos
   en colecciones hash. Si una clase define objetos mutables e
   implementa un método "__eq__()", no debería implementar
   "__hash__()", ya que la implementación de colecciones *hashable*
   requiere que el valor hash de una clave sea inmutable (si el valor
   hash del objeto cambia, estará en el depósito hash incorrecto).

   User-defined classes have "__eq__()" and "__hash__()" methods by
   default (inherited from the "object" class); with them, all objects
   compare unequal (except with themselves) and "x.__hash__()" returns
   an appropriate value such that "x == y" implies both that "x is y"
   and "hash(x) == hash(y)".

   Una clase que anula "__eq__()" y no define "__hash__()" tendrá
   implícito su "__hash__()" establecido a "None". Cuando el método
   "__hash__()" de una clase es "None", instancias de la clase
   lanzarán un "TypeError" cuando el programa intente obtener el valor
   del hash, y también será correctamente identificado como de hash no
   calculable cuando se verifique "isinstance(obj,
   collections.abc.Hashable)".

   Si una clase que anula "__eq__()" necesita conservar la
   implementación de "__hash__()" de una clase padre, al intérprete se
   le debe informar explícitamente estableciendo "__hash__ =
   <ParentClass>.__hash__".

   Si una clase que no anula "__eq__()" desea eliminar el soporte de
   *hash*, debe incluir "__hash__ = None" en la definición de clase.
   Una clase que define su propio "__hash__()" y que explícitamente
   lanza un "TypeError" será identificado de manera incorrecta como de
   hash calculable por una llamada "isinstance(obj,
   collections.abc.Hashable)".

   Nota:

     Por defecto los valores de objetos str y bytes de "__hash__()"
     son “salados” con un valor aleatorio impredecible. Aunque se
     mantienen constantes dentro de un proceso Python particular, no
     son predecibles entre invocaciones repetidas de Python.This is
     intended to provide protection against a denial-of-service caused
     by carefully chosen inputs that exploit the worst case
     performance of a dict insertion, *O*(*n*^2) complexity.  See
     https://ocert.org/advisories/ocert-2011-003.html for
     details.Cambiar los valores hash afectan el orden de la iteración
     de los sets. Python nunca ha dado garantías en relación a este
     orden (y típicamente varía entre estructuras de 32-bits y
     64-bits).Ver también "PYTHONHASHSEED".

   Distinto en la versión 3.3: La aleatorización de hash es habilitada
   por defecto.

object.__bool__(self)

   Called to implement truth value testing and the built-in operation
   "bool()"; should return "False" or "True".  When this method is not
   defined, "__len__()" is called, if it is defined, and the object is
   considered true if its result is nonzero.  If a class defines
   neither "__len__()" nor "__bool__()" (which is true of the "object"
   class itself), all its instances are considered true.

### 3.3.2. Personalizando acceso a atributos

Los siguientes métodos pueden ser definidos para personalizar el
significado de acceso a atributos (uso de, asignación a, o borrado de
"x.name") para instancias de clase.

object.__getattr__(self, name)

   Called when the default attribute access fails with an
   "AttributeError" (either "__getattribute__()" raises an
   "AttributeError" because *name* is not an instance attribute or an
   attribute in the class tree for "self"; or "__get__()" of a *name*
   property raises "AttributeError").  This method should either
   return the (computed) attribute value or raise an "AttributeError"
   exception. The "object" class itself does not provide this method.

   Tome en cuenta que si el atributo es encontrado a través del
   mecanismo normal, "__getattr__()" no es llamado. (Esto es una
   desigualdad intencional entre "__getattr__()" y "__setattr__()".)
   Esto es realizado tanto por motivos de eficiencia y porque de otra
   manera "__getattr__()" no tendría manera de acceder a otros
   atributos de la instancia. Tome en cuenta que al menos para
   variables de instancia, se puede fingir control total al no
   insertar ningún valor en el diccionario de atributo de instancia
   (sino insertándolos en otro objeto). Ver el método
   "__getattribute__()" a continuación para una forma de tener control
   total sobre el acceso de atributo.

object.__getattribute__(self, name)

   Es llamado incondicionalmente para implementar acceso de atributo
   por instancias de clase. Si la clase también define
   "__getattr__()", éste no será llamado a menos que
   "__getattribute__()" lo llame de manera explícita o lance una
   excepción "AttributeError". Este método deberá retornar el valor de
   atributo (calculado) o lanzar una excepción "AttributeError". Para
   evitar la recursividad infinita en este método, su implementación
   deberá siempre llamar al método de la clase base con el mismo
   nombre para acceder cualquier atributo que necesite, por ejemplo,
   "object.__getattribute__(self, name)".

   Nota:

     Este método aún puede ser sobrepasado cuando se buscan métodos
     especiales como resultado de una invocación implícita a través de
     sintaxis de lenguaje o funciones incorporadas. Ver Búsqueda de
     método especial.

   Para ciertos accesos a atributos sensibles, lanza un evento de
   auditoría "object.__getattr__" con los argumentos "obj" y "name".

object.__setattr__(self, name, value)

   Es llamado cuando se intenta la asignación de atributos. Éste es
   llamado en lugar del mecanismo normal (p. ej. guardar el valor en
   el diccionario de instancias). *name* es el nombre de atributo,
   *value* es el valor que se le asigna.

   Si "__setattr__()" quiere asignar a un atributo de instancia, debe
   llamar al método de la clase base con el mismo nombre, por ejemplo,
   "object.__setattr__(self, name, value)".

   Para ciertas asignaciones de atributos sensibles, lanza un evento
   de auditoría "object.__setattr__" con argumentos "obj", "name",
   "value".

object.__delattr__(self, name)

   Al igual que "__setattr__()" pero para borrado de atributos en
   lugar de establecerlos. Esto solo de ser implementado si "del
   obj.name" es significativo para el objeto.

   Para ciertas eliminaciones de atributos sensibles, lanza un evento
   de auditoría "object.__delattr__" con argumentos "obj" y "name".

object.__dir__(self)

   Es llamado cuando "dir()" es llamado en el objeto. Un iterable debe
   ser retornado. "dir()" convierte el iterable retornado a una lista
   y la ordena.

#### 3.3.2.1. Personalizando acceso a atributos de módulo

module.__getattr__()
module.__dir__()

Nombres especiales "__getattr__" y "__dir__" también pueden ser
utilizados para personalizar acceso a atributos de módulo. La función
"__getattr__" a nivel del módulo debe aceptar un argumento que es el
nombre del atributo y retornar el valor calculado o lanzar una
excepción "AttributeError". Si un atributo no es encontrado en el
objeto de módulo a través de una búsqueda normal, p. ej.
"object.__getattribute__()", entonces "__getattr__" es buscado en el
módulo "__dict__" antes de lanzar una excepción "AttributeError". Si
es encontrado, es llamado con el nombre de atributo y el resultado es
retornado.

La función "__dir__" no debe aceptar argumentos y retorna un iterable
de cadena de caracteres que representan los nombres accesibles en el
módulo. De existir, esta función anula la búsqueda estándar "dir()" en
un módulo.

module.__class__

Para una personalización más precisa sobre el comportamiento del
módulo (estableciendo atributos, propiedades, etc.), se puede
establecer el atributo "__class__" de un objeto de módulo a una
subclase de "types.ModuleType". Por ejemplo:

   import sys
   from types import ModuleType

   class VerboseModule(ModuleType):
       def __repr__(self):
           return f'Verbose {self.__name__}'

       def __setattr__(self, attr, value):
           print(f'Setting {attr}...')
           super().__setattr__(attr, value)

   sys.modules[__name__].__class__ = VerboseModule

Nota:

  Definiendo un módulo "__getattr__" y estableciendo un módulo
  "__class__" solo afecta búsquedas que utilizan la sintaxis de acceso
  a atributo -- acceder directamente a las globales del módulo (ya sea
  por código dentro del módulo, o a través de una referencia al
  diccionario de globales del módulo) no se ve afectado.

Distinto en la versión 3.5: El atributo de módulo "__class__" es ahora
escribible.

Added in version 3.7: Atributos de módulo "__getattr__" y "__dir__".

Ver también:

  **PEP 562** - Módulos __getattr__ y __dir__
     Describe las funciones "__getattr__" y "__dir__" en módulos.

#### 3.3.2.2. Implementando descriptores

The following methods only apply when an instance of the class
containing the method (a so-called *descriptor* class) appears in an
*owner* class (the descriptor must be in either the owner's class
dictionary or in the class dictionary for one of its parents).  In the
examples below, "the attribute" refers to the attribute whose name is
the key of the property in the owner class' "__dict__".  The "object"
class itself does not implement any of these protocols.

object.__get__(self, instance, owner=None)

   Es llamado para obtener el atributo de la clase propietaria (acceso
   a atributos de clase) o de una instancia de dicha clase (acceso a
   atributos de instancia). El argumento opcional *owner* es la clase
   propietaria, mientras que *instance* es la instancia a través de la
   cual el atributo fue accedido, o "None" cuando el atributo es
   accedido a través de *owner*.

   Este método debe retornar el valor de atributo calculado o lanzar
   una excepción "AttributeError".

   **PEP 252** especifica que "__get__()" puede ser llamado con uno o
   dos argumentos. Los propios descriptores incorporados de Python
   soportan esta especificación; sin embargo, es probable que algunas
   herramientas de terceros tengan descriptores que requieran ambos
   argumentos. La propia implementación de "__getattribute__()" en
   Python siempre pasa ambos argumentos si son requeridos o no.

object.__set__(self, instance, value)

   Es llamado para establecer el atributo en una instancia *instance*
   de la clase propietaria a un nuevo valor *value*.

   Nota, agregar "__set__()" o "__delete__()" cambia el tipo de
   descriptor a un “descriptor de datos”. Ver Invocando descriptores
   para más detalles.

object.__delete__(self, instance)

   Es llamado para borrar el atributo en una instancia *instance* de
   la clase propietaria.

Las instancias de descriptores también pueden tener presente el
atributo "__objclass__":

object.__objclass__

   El atributo "__objclass__" es interpretado por el módulo "inspect"
   como la especificación de la clase donde el objeto fue definido
   (establecer esto adecuadamente puede ayudar en introspección de
   atributos dinámicos de clases en tiempo de ejecución). Para
   invocables, puede indicar que una instancia de un tipo (o subclase)
   dado es esperado o requerido como el primer argumento posicional
   (por ejemplo, CPython establece este atributo para métodos
   independientes que son implementados en C).

#### 3.3.2.3. Invocando descriptores

En general, un descriptor es un atributo de objeto con "comportamiento
vinculante", uno cuyo acceso al atributo ha sido anulado por métodos
en el protocolo del descriptor: "__get__()", "__set__()" y
"__delete__()". Si alguno de esos métodos está definido para un
objeto, se dice que es un descriptor.

El comportamiento por defecto para atributos de acceso es obtener
(*get*), establecer (*set*) o borrar (*delete*) el atributo del
diccionario del objeto. Por ejemplo, "a.x" tiene una cadena de
búsqueda que comienza con "a.__dict__[‘x’]", luego
"type(a).__dict__[‘x’]", y continúa por las clases base de "type(a)"
excluyendo metaclases.

Sin embargo, si el valor buscado es un objeto definiendo uno de los
métodos del descriptor, entonces Python puede anular el comportamiento
por defecto e invocar al método del descriptor en su lugar. Dónde
ocurre esto en la cadena de precedencia depende de qué métodos de
descriptor fueron definidos y cómo son llamados.

El punto de inicio por invocación de descriptor es un enlace "a.x".
Cómo los argumentos son ensamblados dependen de "a":

Llamado directo
   El llamado más simple y menos común es cuando el código de usuario
   invoca directamente un método descriptor: "x.__get__(a)".

Enlace de instancia
   Al enlazar a una instancia de objeto, "a" es transformado en un
   llamado: "type(a).__dict__[‘x’].__get__(a, type(a))".

Enlace de clase
   Al enlazar a una clase, "A.x" es transformado en un llamado:
   "A.__dict__[‘x’].__get__(None, A)".

Súper enlace
   Una búsqueda punteada como "super(A, a).x" busca en
   "a.__class__.__mro__" una clase base "B" después de "A" y luego
   retorna "B.__dict__['x'].__get__(a, A)". Si no es un descriptor,
   "x" se retorna sin cambios.

En el caso de los enlaces de instancias, la precedencia de la
invocación de descriptores depende de qué métodos de descriptores
están definidos. Un descriptor puede definir cualquier combinación de
"__get__()", "__set__()" y "__delete__()". Si no define "__get__()",
acceder al atributo retornará el objeto descriptor en sí, a menos que
haya un valor en el diccionario de instancia del objeto. Si el
descriptor define "__set__()" y/o "__delete__()", es un descriptor de
datos; si no define ninguno de los dos, es un descriptor que no es de
datos. Normalmente, los descriptores de datos definen tanto
"__get__()" como "__set__()", mientras que los descriptores que no son
de datos tienen solo el método "__get__()". Los descriptores de datos
con "__get__()" y "__set__()" (y/o "__delete__()") definidos siempre
anulan una redefinición en un diccionario de instancia. Por el
contrario, las instancias pueden anular los descriptores que no son
datos.

Python methods (including those decorated with "@staticmethod" and
"@classmethod") are implemented as non-data descriptors.  Accordingly,
instances can redefine and override methods.  This allows individual
instances to acquire behaviors that differ from other instances of the
same class.

The "@property" decorator is implemented as a data descriptor.
Accordingly, instances cannot override the behavior of a property.

#### 3.3.2.4. __slots__

*__slots__* nos permite declarar explícitamente miembros de datos
(como propiedades) y denegar la creación de "__dict__" y *__weakref__*
(a menos que se declare explícitamente en *__slots__* o esté
disponible en un padre).

El espacio ahorrado al usar "__dict__" puede ser significativo. La
velocidad de búsqueda de atributos también se puede mejorar
significativamente.

object.__slots__

   A esta variable de clase se le puede asignar una cadena, un
   iterable o una secuencia de cadenas con nombres de variables
   utilizados por las instancias. *__slots__* reserva espacio para las
   variables declaradas y evita la creación automática de "__dict__" y
   *__weakref__* para cada instancia.

Notas sobre el uso de *__slots__*:

* Al heredar de una clase sin *__slots__*, los atributos "__dict__" y
  *__weakref__* de las instancias siempre estarán accesibles.

* Sin una variable "__dict__", a las instancias no se les pueden
  asignar nuevas variables que no figuran en la definición
  *__slots__*. Los intentos de asignar un nombre de variable no
  listado generan "AttributeError". Si desea una asignación dinámica
  de nuevas variables, agregue "'__dict__'" a la secuencia de cadenas
  en la declaración *__slots__*.

* Sin una variable *__weakref__* para cada instancia, las clases que
  definen *__slots__* no admiten "weak references" en sus instancias.
  Si se necesita soporte de referencia débil, agregue "'__weakref__'"
  a la secuencia de cadenas en la declaración *__slots__*.

* *__slots__* se implementa a nivel de clase creando descriptors para
  cada nombre de variable. Como resultado, los atributos de clase no
  se pueden utilizar para establecer valores predeterminados, por
  ejemplo, variables definidas por *__slots__*; de lo contrario, el
  atributo de clase sobrescribiría la asignación del descriptor.

* La acción de una declaración *__slots__* no se limita a la clase
  donde se define. *__slots__* declarado en clases principales está
  disponible en clases secundarias. Sin embargo, las subclases
  secundarias obtendrán "__dict__" y *__weakref__* a menos que las
  subclases también definan *__slots__* (que solo debe contener
  nombres de cualquier ranura *additional*).

* Si una clase define un espacio (*slot*) también definido en una
  clase base, la variable de instancia definida por el espacio de la
  clase base es inaccesible (excepto al obtener su descriptor
  directamente de la clase base). Esto hace que el significado del
  programa sea indefinido. En el futuro se podría agregar una
  verificación para prevenir esto.

* "TypeError" se generará si se definen *__slots__* no vacíos para una
  clase derivada de un ""variable-length" built-in type" como "int",
  "bytes" y "tuple".

* Cualquier *iterable* que no sea una cadena se puede asignar a
  *__slots__*.

* Si se utiliza un "dictionary" para asignar *__slots__*, las claves
  del diccionario se utilizarán como nombres de ranura. Los valores
  del diccionario se pueden usar para proporcionar cadenas de
  documentos por atributo que "inspect.getdoc()" reconocerá y mostrará
  en la salida de "help()".

* La asignación de "__class__" solo funciona si ambas clases tienen el
  mismo *__slots__*.

* Se puede usar Multiple inheritance con varias clases principales con
  ranuras, pero solo a una de las clases principales se le permite
  tener atributos creados por ranuras (las otras bases deben tener
  diseños de ranuras vacías); las infracciones generan "TypeError".

* Si se utiliza un *iterator* para *__slots__*, entonces se crea un
  *descriptor* para cada uno de los valores del iterador. Sin embargo,
  el atributo *__slots__* será un iterador vacío.

### 3.3.3. Personalización de creación de clases

Siempre que una clase hereda de otra clase, se llama a
"__init_subclass__()" en la clase principal. De esta forma, es posible
escribir clases que cambien el comportamiento de las subclases. Esto
está estrechamente relacionado con los decoradores de clases, pero
mientras los decoradores de clases solo afectan la clase específica a
la que se aplican, "__init_subclass__" solo se aplica a futuras
subclases de la clase que define el método.

classmethod object.__init_subclass__(cls)

   Este método es llamado siempre que la clase que lo contiene sea
   heredada. *cls* es entonces, la nueva subclase. Si se define como
   un método de instancia normal, éste es convertido de manera
   implícita a un método de clase.

   Los argumentos de palabra clave que fueron dados a una nueva clase,
   son pasados a la clase "__init_subclass__" del padre. Por temas de
   compatibilidad con otras clases que usan "__init_subclass__", uno
   debería quitar los argumentos de palabra clave y pasar los otros a
   la clase base, como en:

      class Philosopher:
          def __init_subclass__(cls, /, default_name, **kwargs):
              super().__init_subclass__(**kwargs)
              cls.default_name = default_name

      class AustralianPhilosopher(Philosopher, default_name="Bruce"):
          pass

   La implementación por defecto "object.__init_subclass__" no hace
   nada, pero lanza un error si es llamado con cualquier argumento.

   Nota:

     La sugerencia de metaclase "metaclass" es consumido por el resto
     de la maquinaria de tipos, y nunca se pasa a las implementaciones
     "__init_subclass__". La clase meta actual (más que la sugerencia
     explícita) puede ser accedida como "type(cls)".

   Added in version 3.6.

When a class is created, "type.__new__()" scans the class variables
and makes callbacks to those with a "__set_name__()" hook.

object.__set_name__(self, owner, name)

   Llamado automáticamente al momento en el que se crea la clase
   propietaria *owner*. El objeto es asignado a *name* en esa clase:

      class A:
          x = C()  # Llama automáticamente: x.__set_name__(A, 'x')

   Si la variable de clase se asigna después de crear la clase,
   "__set_name__()" no se llamará automáticamente. Si es necesario,
   "__set_name__()" se puede llamar directamente:

      class A:
         pass

      c = C()
      A.x = c                  # No se llama el enlace
      c.__set_name__(A, 'x')   # Invoca manualmente el enlace

   Ver Creando el objeto de clase para más detalles.

   Added in version 3.6.

#### 3.3.3.1. Metaclases

Por defecto, las clases son construidas usando "type()". El cuerpo de
la clase es ejecutado en un nuevo espacio de nombres y el nombre de la
clase es ligado de forma local al resultado de "type(name, bases,
namespace)".

El proceso de creación de clase puede ser personalizado pasando el
argumento de palabra clave "metaclass" en la línea de definición de la
clase, o al heredar de una clase existente que incluya dicho
argumento. En el siguiente ejemplo, ambos "MyClass" y "MySubclass" son
instancias de "Meta":

   class Meta(type):
       pass

   class MyClass(metaclass=Meta):
       pass

   class MySubclass(MyClass):
       pass

Cualquier otro argumento de palabra clave que sea especificado en la
definición de clase es pasado mediante todas las operaciones de
metaclase descritas a continuación.

Cuando una definición de clase es ejecutada, los siguientes pasos
ocurren:

* Entradas de la orden de resolución de método (MRU) son resueltas;

* se determina la metaclase adecuada;

* se prepara el espacio de nombres de clase;

* se ejecuta el cuerpo de la clase;

* se crea el objeto de clase.

#### 3.3.3.2. Resolviendo entradas de la Orden de Resolución de Métodos (MRU)

object.__mro_entries__(self, bases)

   Si una base que aparece en una definición de clase no es una
   instancia de "type", entonces se busca un método
   "__mro_entries__()" en la base. Si se encuentra un método
   "__mro_entries__()", la base se sustituye por el resultado de una
   llamada a "__mro_entries__()" al crear la clase. El método se llama
   con la tupla de bases original pasada al parámetro *bases* y debe
   retornar una tupla de clases que se utilizará en lugar de la base.
   La tupla retornada puede estar vacía: en estos casos, se ignora la
   base original.

Ver también:

  "types.resolve_bases()"
     Resuelva dinámicamente bases que no sean instancias de "type".

  "types.get_original_bases()"
     Recupera las "bases originales" de una clase antes de las
     modificaciones realizadas por "__mro_entries__()".

  **PEP 560**
     Soporte principal para módulos de escritura y tipos genéricos.

#### 3.3.3.3. Determinando la metaclase adecuada

La metaclase adecuada para la definición de una clase es determinada
de la siguiente manera:

* si no se dan bases ni metaclases explícitas, entonces se utiliza
  "type()";

* si se da una metaclase explícita y *no* es una instancia de
  "type()", entonces se utiliza directamente como la metaclase;

* si se da una instancia de "type()" como la metaclase explícita, o se
  definen bases, entonces se utiliza la metaclase más derivada.

La metaclase más derivada es elegida de la metaclase especificada
explícitamente (si existe) y de la metaclase (p. ej. "type(cls)") de
todas las clases base especificadas.

#### 3.3.3.4. Preparando el espacio de nombres de la clase

Una vez que se ha identificado la metaclase adecuada, se prepara el
espacio de nombres de la clase. Si la metaclase tiene un atributo
"__prepare__", se llama "namespace = metaclass.__prepare__(name,
bases, **kwds)" (donde los argumentos de palabras clave adicionales,
si los hay, provienen de la definición de clase). El método
"__prepare__" debe implementarse como "classmethod". El espacio de
nombres retornado por "__prepare__" se pasa a "__new__", pero cuando
se crea el objeto de clase final, el espacio de nombres se copia en un
nuevo "dict".

Si la metaclase no tiene atributo "__prepare__", entonces el espacio
de nombres de clase es iniciado como un mapeo vacío ordenado.

Ver también:

  **PEP 3115** - Metaclases en Python 3000
     Introduce el enlace de espacio de nombres "__prepare__"

#### 3.3.3.5. Ejecutando el cuerpo de la clase

El cuerpo de la clase es ejecutado como "exec(body, globals(),
namespace)" (aproximadamente). La diferencia clave con un llamado
normal a "exec()" es que el alcance léxico permite que el cuerpo de la
clase (incluyendo cualquier método) haga referencia a nombres de los
alcances actuales y externos cuando la definición de clase sucede
dentro de la función.

Sin embargo, aún cuando la definición de clase sucede dentro de la
función, los métodos definidos dentro de la clase aún no pueden ver
nombres definidos dentro del alcance de la clase. Variables de clase
deben ser accedidas a través del primer parámetro de instancia o
métodos de clase, o a través de la referencia al léxico implícito
"__class__" descrita en la siguiente sección.

#### 3.3.3.6. Creando el objeto de clase

Una vez que el espacio de nombres de la clase ha sido poblado al
ejecutar el cuerpo de la clase, el objeto de clase es creado al llamar
"metaclass(name, bases, namespace, **kwds)" (las palabras clave
adicionales que se pasan aquí, son las mismas que aquellas pasadas en
"__prepare__").

Este objeto de clase es el que será referenciado por la forma sin
argumentos de "super()". "__class__" es una referencia de cierre
implícita creada por el compilador si cualquier método en el cuerpo de
una clase se refiere tanto a "__class__" o "super". Esto permite que
la forma sin argumentos de "super()" identifique correctamente la
clase definida en base al alcance léxico, mientras la clase o
instancia que fue utilizada para hacer el llamado actual es
identificado en base al primer argumento que se pasa al método.

En CPython 3.6 y posterior, la celda "__class__" se pasa a la
metaclase como una entrada "__classcell__" en el espacio de nombres de
la clase. En caso de existir, esto debe ser propagado hacia el llamado
"type.__new__" para que la clase se inicie correctamente. No hacerlo
resultará en un error "RuntimeError" en Python 3.8.

Cuando se utiliza la metaclase por defecto "type", o cualquier
metaclase que finalmente llama a "type.__new__", los siguientes pasos
de personalización adicional son invocados después de crear el objeto
de clase:

1. El método "type.__new__" recolecta todos los atributos en el
   espacio de nombres de la clase que definen un método
   "__set_name__()";

2. Esos métodos "__set_name__" son llamados con la clase siendo
   definida y el nombre de ese atributo particular asignado;

3. El gancho "__init_subclass__()" llama al padre inmediato de la
   nueva clase en su orden de resolución del método.

Después de que el objeto de clase es creado, se pasa al decorador de
clase incluido en su definición (si existe) y el objeto resultante es
enlazado en el espacio de nombres local como la clase definida.

Cuando una nueva clase es creada por "type.__new__", el objeto
proporcionado como el parámetro de espacio de nombres es copiado a un
nuevo trazado ordenado y el objeto original es descartado. La nueva
copia es *envuelta* en un proxy de solo lectura, que se convierte en
el atributo "__dict__" del objeto de clase.

Ver también:

  **PEP 3135** - Nuevo súper
     Describe la referencia de cierre implícita "__class__"

#### 3.3.3.7. Usos para metaclases

Los usos potenciales para metaclases son ilimitados. Algunas ideas que
ya han sido exploradas incluyen enumeración, registros, revisión de
interface, delegación automática, creación de propiedades automática,
proxy, infraestructuras, y bloqueo/sincronización automática de
recursos.

### 3.3.4. Personalizando revisiones de instancia y subclase

Los siguientes métodos son utilizados para anular el comportamiento
por defecto de las funciones incorporadas "isinstance()" y
"issubclass()".

En particular, la metaclase "abc.ABCMeta" implementa estos métodos
para permitir la adición de Clases Base Abstractas (ABCs, por su
nombre en inglés *Abstract Base Clases*) como “clases base virtuales”
a cualquier clase o tipo (incluyendo tipos incorporados), incluyendo
otros ABCs.

type.__instancecheck__(self, instance)

   Retorna *true* si la instancia *instance* debe ser considerada una
   instancia (directa o indirecta) de clase *class*. De ser definida,
   es llamado para implementar "isinstance(instance, class)".

type.__subclasscheck__(self, subclass)

   Retorna *true* si la subclase *subclass* debe ser considerada una
   subclase (directa o indirecta) de clase *class*. De ser definida,
   es llamado para implementar "issubclass(subclass, class)".

Tome en cuenta que estos métodos son buscados en el tipo (metaclase)
de una clase. No pueden ser definidos como métodos de clase en la
clase actual. Esto es consistente con la búsqueda de métodos
especiales que son llamados en instancias, solo en este caso la
instancia es por sí misma una clase.

Ver también:

  **PEP 3119** - Introducción a Clases Base Abstractas (*Abstract Base
  Classes*)
     Incluye la especificación para personalizar el comportamiento de
     "isinstance()" y "issubclass()" a través de "__instancecheck__()"
     y "__subclasscheck__()", con motivación para esta funcionalidad
     en el contexto de agregar Clases Base Abstractas (ver el módulo
     "abc") al lenguaje.

### 3.3.5. Emulando tipos genéricos

Cuando se usa *type annotations*, a menudo es útil *parameterize* a
*generic type* usando la notación de corchetes de Python. Por ejemplo,
la anotación "list[int]" podría usarse para indicar un "list" en el
que todos los elementos son del tipo "int".

Ver también:

  **PEP 484** - Sugerencias de tipo
     Presentamos el marco de trabajo de Python para las anotaciones de
     tipo

  Generic Alias Types
     Documentación para objetos que representan clases genéricas
     parametrizadas

  Genéricos, user-defined generics y "typing.Generic"
     Documentación sobre cómo implementar clases genéricas que se
     pueden parametrizar en tiempo de ejecución y que los
     verificadores de tipos estáticos pueden entender.

Una clase *generally* solo se puede parametrizar si define el método
de clase especial "__class_getitem__()".

classmethod object.__class_getitem__(cls, key)

   Retornar un objeto representando la especialización de una clase
   genérica por argumentos de tipo encontrados en *key*.

   When defined on a class, "__class_getitem__()" is automatically a
   class method. As such, there is no need for it to be decorated with
   "@classmethod" when it is defined.

#### 3.3.5.1. El propósito de *__class_getitem__*

El propósito de "__class_getitem__()" es permitir la parametrización
en tiempo de ejecución de clases genéricas de biblioteca estándar para
aplicar *type hints* a estas clases con mayor facilidad.

Para implementar clases genéricas personalizadas que se puedan
parametrizar en tiempo de ejecución y que los verificadores de tipos
estáticos las entiendan, los usuarios deben heredar de una clase de
biblioteca estándar que ya implementa "__class_getitem__()", o heredar
de "typing.Generic", que tiene su propia implementación de
"__class_getitem__()".

Es posible que los verificadores de tipos de terceros, como mypy, no
entiendan las implementaciones personalizadas de "__class_getitem__()"
en clases definidas fuera de la biblioteca estándar. Se desaconseja el
uso de "__class_getitem__()" en cualquier clase para fines distintos a
la sugerencia de tipo.

#### 3.3.5.2. *__class_getitem__* frente a *__getitem__*

Por lo general, el subscription de un objeto que usa corchetes llamará
al método de instancia "__getitem__()" definido en la clase del
objeto. Sin embargo, si el objeto que se suscribe es en sí mismo una
clase, se puede llamar al método de clase "__class_getitem__()" en su
lugar. "__class_getitem__()" debería retornar un objeto GenericAlias
si está definido correctamente.

Presentado con el *expression* "obj[x]", el intérprete de Python sigue
un proceso similar al siguiente para decidir si se debe llamar a
"__getitem__()" o "__class_getitem__()":

   from inspect import isclass

   def subscribe(obj, x):
       """Retorna el resultado de la expresión 'obj[x]'"""

       class_of_obj = type(obj)

       # Si la clase de obj define __getitem__,
       # llama class_of_obj.__getitem__(obj, x)
       if hasattr(class_of_obj, '__getitem__'):
           return class_of_obj.__getitem__(obj, x)

       # De lo contrario, si obj es una clase y define __class_getitem__,
       # llama obj.__class_getitem__(x)
       elif isclass(obj) and hasattr(obj, '__class_getitem__'):
           return obj.__class_getitem__(x)

       # De lo contrario, lanza una excepción
       else:
           raise TypeError(
               f"'{class_of_obj.__name__}' object is not subscriptable"
           )

En Python, todas las clases son en sí mismas instancias de otras
clases. La clase de una clase se conoce como *metaclass* de esa clase,
y la mayoría de las clases tienen la clase "type" como su metaclase.
"type" no define "__getitem__()", lo que significa que expresiones
como "list[int]", "dict[str, float]" y "tuple[str, bytes]" dan como
resultado que se llame a "__class_getitem__()":

   >>> # list tiene la clase "type" como su metaclase, como la mayoría de las clases:
   >>> type(list)
   <class 'type'>
   >>> type(dict) == type(list) == type(tuple) == type(str) == type(bytes)
   True
   >>> # "list[int]" llama "list.__class_getitem__(int)"
   >>> list[int]
   list[int]
   >>> # list.__class_getitem__ retorna un objeto GenericAlias:
   >>> type(list[int])
   <class 'types.GenericAlias'>

Sin embargo, si una clase tiene una metaclase personalizada que define
"__getitem__()", la suscripción de la clase puede generar un
comportamiento diferente. Un ejemplo de esto se puede encontrar en el
módulo "enum":

   >>> from enum import Enum
   >>> class Menu(Enum):
   ...     """Un menú de desayuno"""
   ...     SPAM = 'spam'
   ...     BACON = 'bacon'
   ...
   >>> # Las clases de enumeración tienen una metaclase personalizada:
   >>> type(Menu)
   <class 'enum.EnumMeta'>
   >>> # EnumMeta define __getitem__,
   >>> # por lo que no se llama __class_getitem__,
   >>> # y el resultado no es un objeto GenericAlias:
   >>> Menu['SPAM']
   <Menu.SPAM: 'spam'>
   >>> type(Menu['SPAM'])
   <enum 'Menu'>

Ver también:

  **PEP 560**: soporte principal para módulo de escritura y tipos
  genéricos
     Presentamos "__class_getitem__()" y describimos cuándo un
     subscription da como resultado que se llame a
     "__class_getitem__()" en lugar de "__getitem__()"

### 3.3.6. Emulando objetos que se pueden llamar

object.__call__(self[, args...])

   Called when the instance is "called" as a function; if this method
   is defined, "x(arg1, arg2, ...)" roughly translates to
   "type(x).__call__(x, arg1, ...)". The "object" class itself does
   not provide this method.

### 3.3.7. Emulando tipos de contenedores

The following methods can be defined to implement container objects.
None of them are provided by the "object" class itself. Containers
usually are *sequences* (such as "lists" or "tuples") or *mappings*
(like *dictionaries*), but can represent other containers as well.
The first set of methods is used either to emulate a sequence or to
emulate a mapping; the difference is that for a sequence, the
allowable keys should be the integers *k* for which "0 <= k < N" where
*N* is the length of the sequence, or "slice" objects, which define a
range of items.  It is also recommended that mappings provide the
methods "keys()", "values()", "items()", "get()", "clear()",
"setdefault()", "pop()", "popitem()", "copy()", and "update()"
behaving similar to those for Python's standard "dictionary" objects.
The "collections.abc" module provides a "MutableMapping" *abstract
base class* to help create those methods from a base set of
"__getitem__()", "__setitem__()", "__delitem__()", and "keys()".

Mutable sequences should provide methods "append()", "clear()",
"count()", "extend()", "index()", "insert()", "pop()", "remove()", and
"reverse()", like Python standard "list" objects. Finally, sequence
types should implement addition (meaning concatenation) and
multiplication (meaning repetition) by defining the methods
"__add__()", "__radd__()", "__iadd__()", "__mul__()", "__rmul__()" and
"__imul__()" described below; they should not define other numerical
operators.

It is recommended that both mappings and sequences implement the
"__contains__()" method to allow efficient use of the "in" operator;
for mappings, "in" should search the mapping's keys; for sequences, it
should search through the values.  It is further recommended that both
mappings and sequences implement the "__iter__()" method to allow
efficient iteration through the container; for mappings, "__iter__()"
should iterate through the object's keys; for sequences, it should
iterate through the values.

object.__len__(self)

   Llamado para implementar la función incorporada "len()". Debería
   retornar la longitud del objeto, un número entero ">=" 0. Además,
   un objeto que no define un método "__bool__()" y cuyo método
   "__len__()" retorna cero se considera falso en un contexto
   booleano.

   En CPython, se requiere que la longitud sea como máximo
   "sys.maxsize". Si la longitud es mayor que "sys.maxsize", algunas
   funciones (como "len()") pueden generar "OverflowError". Para
   evitar que se genere "OverflowError" mediante pruebas de valor de
   verdad, un objeto debe definir un método "__bool__()".

object.__length_hint__(self)

   Es llamado para implementar "operator.length_hint()". Debe retornar
   una longitud estimada para el objeto (que puede ser mayor o menor
   que la longitud actual). La longitud debe ser un entero ">=" 0. El
   valor de retorno también debe ser "NotImplemented", el cual es
   tratado de igual forma a que si el método "__length_hint__" no
   existiera en absoluto. Este método es puramente una optimización y
   nunca es requerido para precisión.

   Added in version 3.4.

object.__getitem__(self, subscript)

   Called to implement *subscription*, that is, "self[subscript]". See
   Subscriptions and slicings for details on the syntax.

   There are two types of built-in objects that support subscription
   via "__getitem__()":

   * **sequences**, where *subscript* (also called *index*) should be
     an integer or a "slice" object. See the sequence documentation
     for the expected behavior, including handling "slice" objects and
     negative indices.

   * **mappings**, where *subscript* is also called the *key*. See
     mapping documentation for the expected behavior.

   If *subscript* is of an inappropriate type, "__getitem__()" should
   raise "TypeError". If *subscript* has an inappropriate value,
   "__getitem__()" should raise an "LookupError" or one of its
   subclasses ("IndexError" for sequences; "KeyError" for mappings).

   Nota:

     Slicing is handled by "__getitem__()", "__setitem__()", and
     "__delitem__()". A call like

        a[1:2] = b

     es traducido a

        a[slice(1, 2, None)] = b

     and so forth. Missing slice items are always filled in with
     "None".

   Nota:

     The sequence iteration protocol (used, for example, in "for"
     loops), expects that an "IndexError" will be raised for illegal
     indexes to allow proper detection of the end of a sequence.

   Nota:

     When subscripting a *class*, the special class method
     "__class_getitem__()" may be called instead of "__getitem__()".
     See __class_getitem__ frente a __getitem__ for more details.

object.__setitem__(self, key, value)

   Es llamado para implementar la asignación a "self[key]". Lo mismo
   con respecto a "__getitem__()". Esto solo debe ser implementado
   para mapeos si los objetos permiten cambios a los valores de las
   llaves, o si nuevas llaves pueden ser añadidas, o para secuencias
   si los elementos pueden ser reemplazados. Las mismas excepciones
   deben ser lanzadas para valores de *key* inadecuados con respecto
   al método "__getitem__()".

object.__delitem__(self, key)

   Es llamado para implementar el borrado de "self[key]". Lo mismo con
   respecto a "__getitem__()". Esto solo debe ser implementado para
   mapeos si los objetos permiten el borrado de llaves, o para
   secuencias si los elementos pueden ser eliminados de la secuencia.
   Las mismas excepciones deben ser lanzadas por valores de *key*
   inapropiados con respecto al método "__getitem__()".

object.__missing__(self, key)

   Es llamado por "dict"."__getitem__()" para implementar "self[key]"
   para subclases de diccionarios cuando la llave no se encuentra en
   el diccionario.

object.__iter__(self)

   Se llama a este método cuando se requiere un *iterator* para un
   contenedor. Este método debería retornar un nuevo objeto iterador
   que pueda iterar sobre todos los objetos del contenedor. Para las
   asignaciones, debe iterar sobre las claves del contenedor.

object.__reversed__(self)

   Es llamado (si existe) por la función incorporada "reversed()" para
   implementar una interacción invertida. Debe retornar un nuevo
   objeto iterador que itere sobre todos los objetos en el contenedor
   en orden inverso.

   Si el método "__reversed__()" no es proporcionado, la función
   incorporada "reversed()" recurrirá a utilizar el protocolo de
   secuencia ("__len__()" y "__getitem__()"). Objetos que permiten el
   protocolo de secuencia deben únicamente proporcionar
   "__reversed__()" si no pueden proporcionar una implementación que
   sea más eficiente que la proporcionada por "reversed()".

Los operadores de prueba de pertenencia ("in" and "not in") son
normalmente implementados como una iteración sobre un contenedor. Sin
embargo, los objetos de contenedor pueden proveer el siguiente método
especial con una implementación más eficiente, que tampoco requiere
que el objeto sea iterable.

object.__contains__(self, item)

   Es llamado para implementar operadores de prueba de pertenencia.
   Deben retornar *true* si *item* se encuentra en *self*, de lo
   contrario *false*. Para objetos de mapeo, estos debe considerar las
   llaves del mapeo en lugar de los valores o los pares de llave-
   valor.

   Para objetos que no definen "__contains__()", la prueba de
   pertenencia primero intenta la iteración a través de "__iter__()",
   y luego el antiguo protocolo de iteración de secuencia a través de
   "__getitem__()", ver esta sección en la referencia del lenguaje.

### 3.3.8. Emulando tipos numéricos

Los siguientes métodos pueden ser definidos para emular objetos
numéricos. Métodos que corresponden a operaciones que no son
permitidas por el número particular implementado (por ejemplo,
operaciones bit a bit para números no enteros) se deben dejar sin
definir.

object.__add__(self, other)
object.__sub__(self, other)
object.__mul__(self, other)
object.__matmul__(self, other)
object.__truediv__(self, other)
object.__floordiv__(self, other)
object.__mod__(self, other)
object.__divmod__(self, other)
object.__pow__(self, other[, modulo])
object.__lshift__(self, other)
object.__rshift__(self, other)
object.__and__(self, other)
object.__xor__(self, other)
object.__or__(self, other)

   These methods are called to implement the binary arithmetic
   operations ("+", "-", "*", "@", "/", "//", "%", "divmod()",
   "pow()", "**", "<<", ">>", "&", "^", "|").  For instance, to
   evaluate the expression "x + y", where *x* is an instance of a
   class that has an "__add__()" method, "type(x).__add__(x, y)" is
   called.  The "__divmod__()" method should be the equivalent to
   using "__floordiv__()" and "__mod__()"; it should not be related to
   "__truediv__()".  Note that "__pow__()" should be defined to accept
   an optional third argument if the three-argument version of the
   built-in "pow()" function is to be supported.

   Si alguno de esos métodos no permiten la operación con los
   argumentos suministrados, debe retornar "NotImplemented".

object.__radd__(self, other)
object.__rsub__(self, other)
object.__rmul__(self, other)
object.__rmatmul__(self, other)
object.__rtruediv__(self, other)
object.__rfloordiv__(self, other)
object.__rmod__(self, other)
object.__rdivmod__(self, other)
object.__rpow__(self, other[, modulo])
object.__rlshift__(self, other)
object.__rrshift__(self, other)
object.__rand__(self, other)
object.__rxor__(self, other)
object.__ror__(self, other)

   These methods are called to implement the binary arithmetic
   operations ("+", "-", "*", "@", "/", "//", "%", "divmod()",
   "pow()", "**", "<<", ">>", "&", "^", "|") with reflected (swapped)
   operands.  These functions are only called if the operands are of
   different types, when the left operand does not support the
   corresponding operation [3], or the right operand's class is
   derived from the left operand's class. [4] For instance, to
   evaluate the expression "x - y", where *y* is an instance of a
   class that has an "__rsub__()" method, "type(y).__rsub__(y, x)" is
   called if "type(x).__sub__(x, y)" returns "NotImplemented" or
   "type(y)" is a subclass of "type(x)". [5]

   Note that "__rpow__()" should be defined to accept an optional
   third argument if the three-argument version of the built-in
   "pow()" function is to be supported.

   Distinto en la versión 3.14: Three-argument "pow()" now try calling
   "__rpow__()" if necessary. Previously it was only called in two-
   argument "pow()" and the binary power operator.

   Nota:

     Si el tipo del operando de la derecha es una subclase del tipo
     del operando de la izquierda y esa subclase proporciona el método
     reflejado para la operación, este método será llamado antes del
     método no reflejado del operando izquierdo. Este comportamiento
     permite que las subclases anulen las operaciones de sus
     predecesores.

object.__iadd__(self, other)
object.__isub__(self, other)
object.__imul__(self, other)
object.__imatmul__(self, other)
object.__itruediv__(self, other)
object.__ifloordiv__(self, other)
object.__imod__(self, other)
object.__ipow__(self, other[, modulo])
object.__ilshift__(self, other)
object.__irshift__(self, other)
object.__iand__(self, other)
object.__ixor__(self, other)
object.__ior__(self, other)

   Estos métodos son llamados para implementar las asignaciones
   aritméticas aumentadas ("+=", "-=", "*=", "@=", "/=", "//=", "%=",
   "**=", "<<=", ">>=", "&=", "^=", "|="). Estos métodos deben
   intentar realizar la operación *in-place* (modificando *self*) y
   retornar el resultado (que puede, pero no tiene que ser *self*). Si
   un método específico no es definido o si ese método retorna
   "NotImplemented", la asignación aumentada regresa a los métodos
   normales. Por ejemplo, si *x* es la instancia de una clase con el
   método "__iadd__()", "x += y" es equivalente a "x = x.__iadd__(y)".
   Si "__iadd__()" no existe o si "x.__iadd__(y)" retorna
   "NotImplemented", "x.__add__(y)" y "y.__radd__(x)" se consideran al
   igual que con la evaluación de "x + y". En ciertas situaciones,
   asignaciones aumentadas pueden resultar en errores no esperados
   (ver ¿Por qué hacer lo siguiente, a_tuple[i] += ['item'], lanza una
   excepción cuando la suma funciona?), pero este comportamiento es en
   realidad parte del modelo de datos.

object.__neg__(self)
object.__pos__(self)
object.__abs__(self)
object.__invert__(self)

   Es llamado para implementar las operaciones aritméticas unarias
   ("-", "+", "abs()" and "~").

object.__complex__(self)
object.__int__(self)
object.__float__(self)

   Es llamado para implementar las funciones incorporadas "complex()",
   "int()" y "float()". Debe retornar un valor del tipo apropiado.

object.__index__(self)

   Es llamado para implementar "operator.index()", y cuando sea que
   Python necesite convertir sin pérdidas el objeto numérico a un
   objeto entero (tal como en la segmentación o *slicing*, o las
   funciones incorporadas "bin()", "hex()" y "oct()"). La presencia de
   este método indica que el objeto numérico es un tipo entero. Debe
   retornar un entero.

   Si "__int__()", "__float__()" y "__complex__()" no son definidos,
   entonces todas las funciones incorporadas correspondientes "int()",
   "float()" y "complex()" vuelven a "__index__()".

object.__round__(self[, ndigits])
object.__trunc__(self)
object.__floor__(self)
object.__ceil__(self)

   Es llamado para implementar la función incorporada "round()" y las
   funciones "math" "trunc()", "floor()" y "ceil()". A menos que
   *ndigits* sea pasado a "__round__()" todos estos métodos deben
   retornar el valor del objeto truncado a "Integral" (normalmente
   "int").

   Distinto en la versión 3.14: "int()" no longer delegates to the
   "__trunc__()" method.

### 3.3.9. Gestores de Contexto en la Declaración *with*

Un *context manager* es un objeto que define el contexto en tiempo de
ejecución a ser establecido cuando se ejecuta una declaración "with".
El gestor de contexto maneja la entrada y la salida del contexto en
tiempo de ejecución deseado para la ejecución del bloque de código.
Los gestores de contexto son normalmente invocados utilizando la
declaración "with" (descritos en la sección La sentencia with), pero
también pueden ser utilizados al invocar directamente sus métodos.

Usos típicos de los gestores de contexto incluyen guardar y
restablecer diversos tipos de declaraciones globales, bloquear y
desbloquear recursos, cerrar archivos abiertos, etc.

For more information on context managers, see Tipos gestores de
contexto. The "object" class itself does not provide the context
manager methods.

object.__enter__(self)

   Ingresa al contexto en tiempo de ejecución relacionado con este
   objeto. La declaración "with" ligará el valor de retorno de este
   método al objetivo especificado en cláusula "as" de la declaración,
   en caso de existir.

object.__exit__(self, exc_type, exc_value, traceback)

   Sale del contexto en tiempo de ejecución relacionado a este objeto.
   Los parámetros describen la excepción que causa la salida del
   contexto. Si éste se termina sin excepción, los tres argumentos
   serán "None".

   Si se proporciona una excepción, y el método desea eliminarla (por
   ejemplo, prevenir que sea propagada), debe retornar un valor
   verdadero. De lo contrario, la excepción será procesada de forma
   normal al salir de este método.

   Se debe tomar en cuenta que los métodos "__exit__()" no deben
   lanzar de nuevo la excepción que se pasa; esto es la
   responsabilidad de quien hace el llamado.

Ver también:

  **PEP 343** - La declaración “with”
     La especificación, el antecedente, y los ejemplos para la
     declaración de Python "with".

### 3.3.10. Personalización de argumentos posicionales en la coincidencia de patrones de clase

Cuando se utiliza un nombre de clase en un patrón, los argumentos
posicionales en el patrón no están permitidos de forma predeterminada,
es decir, "case MyClass(x, y)" normalmente no es válido sin un soporte
especial en "MyClass". Para poder utilizar ese tipo de patrón, la
clase necesita definir un atributo *__match_args__*.

object.__match_args__

   A esta variable de clase se le puede asignar una tupla de cadenas.
   Cuando esta clase se utiliza en un patrón de clase con argumentos
   posicionales, cada argumento posicional se convertirá en un
   argumento de palabra clave, utilizando el valor correspondiente en
   *__match_args__* como palabra clave. La ausencia de este atributo
   es equivalente a establecerlo en "()".

Por ejemplo, si "MyClass.__match_args__" es "("left", "center",
"right")" eso significa que "case MyClass(x, y)" es equivalente a
"case MyClass(left=x, center=y)". Ten en cuenta que el número de
argumentos en el patrón debe ser menor o igual que el número de
elementos en *__match_args__*; si es más grande, el intento de
coincidencia de patrón producirá un "TypeError".

Added in version 3.10.

Ver también:

  **PEP 634** - Coincidencia de patrones estructurales
     La especificación para la declaración "match" de Python.

### 3.3.11. Emulando tipos de búfer

buffer protocol proporciona una forma para que los objetos Python
expongan un acceso eficiente a una matriz de memoria de bajo nivel.
Este protocolo se implementa mediante tipos integrados como "bytes" y
"memoryview", y bibliotecas de terceros pueden definir tipos de búfer
adicionales.

Si bien los tipos de búfer generalmente se implementan en C, también
es posible implementar el protocolo en Python.

object.__buffer__(self, flags)

   Se llama cuando se solicita un búfer desde *self* (por ejemplo, por
   el constructor "memoryview"). El argumento *flags* es un número
   entero que representa el tipo de búfer solicitado y afecta, por
   ejemplo, si el búfer retornado es de solo lectura o de escritura.
   "inspect.BufferFlags" proporciona una manera conveniente de
   interpretar las banderas. El método debe retornar un objeto
   "memoryview".

   **Thread safety:** In *free-threaded* Python, implementations must
   manage any internal export counter using atomic operations. The
   method must be safe to call concurrently from multiple threads, and
   the returned buffer's underlying data must remain valid until the
   corresponding "__release_buffer__()" call completes. See Thread
   safety for memoryview objects for details.

object.__release_buffer__(self, buffer)

   Called when a buffer is no longer needed. The *buffer* argument is
   a "memoryview" object that was previously returned by
   "__buffer__()". The method must release any resources associated
   with the buffer. This method should return "None".

   **Thread safety:** In *free-threaded* Python, any export counter
   decrement must use atomic operations. Resource cleanup must be
   thread-safe, as the final release may race with concurrent releases
   from other threads.

   Buffer objects that do not need to perform any cleanup are not
   required to implement this method.

Added in version 3.12.

Ver también:

  **PEP 688**: hacer accesible el protocolo de búfer en Python
     Presenta los métodos Python "__buffer__" y "__release_buffer__".

  "collections.abc.Buffer"
     ABC para tipos de buffer.

### 3.3.12. Annotations

Functions, classes, and modules may contain *annotations*, which are a
way to associate information (usually *type hints*) with a symbol.

object.__annotations__

   This attribute contains the annotations for an object. It is lazily
   evaluated, so accessing the attribute may execute arbitrary code
   and raise exceptions. If evaluation is successful, the attribute is
   set to a dictionary mapping from variable names to annotations.

   Distinto en la versión 3.14: Annotations are now lazily evaluated.

object.__annotate__(format)

   An *annotate function*. Returns a new dictionary object mapping
   attribute/parameter names to their annotation values.

   Takes a format parameter specifying the format in which annotations
   values should be provided. It must be a member of the
   "annotationlib.Format" enum, or an integer with a value
   corresponding to a member of the enum.

   If an annotate function doesn't support the requested format, it
   must raise "NotImplementedError". Annotate functions must always
   support "VALUE" format; they must not raise "NotImplementedError()"
   when called with this format.

   When called with  "VALUE" format, an annotate function may raise
   "NameError"; it must not raise "NameError" when called requesting
   any other format.

   If an object does not have any annotations, "__annotate__" should
   preferably be set to "None" (it can’t be deleted), rather than set
   to a function that returns an empty dict.

   Added in version 3.14.

Ver también:

  **PEP 649** --- Deferred evaluation of annotation using descriptors
     Introduces lazy evaluation of annotations and the "__annotate__"
     function.

### 3.3.13. Búsqueda de método especial

Para clases personalizadas, invocaciones implícitas de métodos
especiales solo están garantizados para trabajar correctamente si son
definidos en un tipo de objeto, no en el diccionario de instancia del
objeto. Ese comportamiento es la razón por la que el siguiente código
lanza una excepción:

   >>> class C:
   ...     pass
   ...
   >>> c = C()
   >>> c.__len__ = lambda: 5
   >>> len(c)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: object of type 'C' has no len()

La razón detrás de este comportamiento radica en una serie de métodos
especiales, como "__hash__()" y "__repr__()", que implementan todos
los objetos, incluidos los objetos de tipo. Si la búsqueda implícita
de estos métodos utilizara el proceso de búsqueda convencional,
fallarían cuando se invocaran en el objeto de tipo mismo:

   >>> 1 .__hash__() == hash(1)
   True
   >>> int.__hash__() == hash(int)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: descriptor '__hash__' of 'int' object needs an argument

Intentar invocar de manera incorrecta el método no ligado de una clase
de esta forma a veces es denominado como ‘confusión de metaclase’, y
se evita sobrepasando la instancia al buscar métodos especiales:

   >>> type(1).__hash__(1) == hash(1)
   True
   >>> type(int).__hash__(int) == hash(int)
   True

Además de omitir cualquier atributo de instancia en aras de la
corrección, la búsqueda implícita de métodos especiales generalmente
también omite el método "__getattribute__()" incluso de la metaclase
del objeto:

   >>> class Meta(type):
   ...     def __getattribute__(*args):
   ...         print("Metaclass getattribute invoked")
   ...         return type.__getattribute__(*args)
   ...
   >>> class C(object, metaclass=Meta):
   ...     def __len__(self):
   ...         return 10
   ...     def __getattribute__(*args):
   ...         print("Class getattribute invoked")
   ...         return object.__getattribute__(*args)
   ...
   >>> c = C()
   >>> c.__len__()                 # Búsqueda explícita a través de la instancia
   Class getattribute invoked
   10
   >>> type(c).__len__(c)          # Búsqueda explícita a través de type
   Metaclass getattribute invoked
   10
   >>> len(c)                      # Búsqueda implícita
   10

Omitir la maquinaria "__getattribute__()" de esta manera proporciona
un margen significativo para optimizar la velocidad dentro del
intérprete, a costa de cierta flexibilidad en el manejo de métodos
especiales (el método especial *must* debe configurarse en el propio
objeto de clase para que el intérprete lo invoque consistentemente).
).

## 3.4. Corrutinas

### 3.4.1. Objetos esperables

Un objeto *awaitable* generalmente implementa un método "__await__()".
*Coroutine objects* retornado por las funciones "async def" están a la
espera.

Nota:

  Los objetos *generator iterator* retornados por generadores
  decorados con "types.coroutine()" también están a la espera, pero no
  implementan "__await__()".

object.__await__(self)

   Must return an *iterator*.  Should be used to implement *awaitable*
   objects.  For instance, "asyncio.Future" implements this method to
   be compatible with the "await" expression. The "object" class
   itself is not awaitable and does not provide this method.

   Nota:

     El lenguaje no impone ninguna restricción sobre el tipo o valor
     de los objetos generados por el iterador retornado por
     "__await__", ya que esto es específico de la implementación del
     marco de ejecución asincrónica (por ejemplo, "asyncio") que
     administrará el objeto *awaitable*.

Added in version 3.5.

Ver también:

  **PEP 492** para información adicional sobre objetos esperables.

### 3.4.2. Objetos de corrutina

*Coroutine objects* son objetos *awaitable*. La ejecución de una
corrutina se puede controlar llamando a "__await__()" e iterando sobre
el resultado. Cuando la rutina termina de ejecutarse y regresa, el
iterador genera "StopIteration" y el atributo "value" de la excepción
contiene el valor de retorno. Si la rutina genera una excepción, el
iterador la propaga. Las corrutinas no deberían generar directamente
excepciones "StopIteration" no controladas.

Las corrutinas también tienen los métodos mencionados a continuación,
los cuales son análogos a los de los generadores. (ver Métodos
generador-iterador). Sin embargo, a diferencia de los generadores, las
corrutinas no soportan directamente iteración.

Coroutines are generic over the types of their yield, send, and return
values, respectively.

Distinto en la versión 3.5.2: Es un error "RuntimeError" esperar a una
corrutina más de una vez.

coroutine.send(value)

   Inicia o reanuda la ejecución de la corrutina. Si *value* es
   "None", esto equivale a avanzar el iterador retornado por
   "__await__()". Si *value* no es "None", este método delega en el
   método "send()" del iterador que provocó la suspensión de la
   rutina. El resultado (valor de retorno, "StopIteration" u otra
   excepción) es el mismo que cuando se itera sobre el valor de
   retorno "__await__()", descrito anteriormente.

coroutine.throw(value)
coroutine.throw(type[, value[, traceback]])

   Genera la excepción especificada en la corrutina. Este método
   delega al método "throw()" del iterador que provocó la suspensión
   de la rutina, si tiene dicho método. En caso contrario, la
   excepción se plantea en el punto de suspensión. El resultado (valor
   de retorno, "StopIteration" u otra excepción) es el mismo que
   cuando se itera sobre el valor de retorno "__await__()", descrito
   anteriormente. Si la excepción no queda atrapada en la rutina, se
   propaga de nuevo a la persona que llama.

   Distinto en la versión 3.12: La segunda firma (type[, value[,
   traceback]]) está obsoleta y puede eliminarse en una versión futura
   de Python.

coroutine.close()

   Causa que la corrutina misma se borre a sí misma y termine su
   ejecución. Si la corrutina es suspendida, este método primero
   delega a "close()", si existe, del iterador que causó la suspensión
   de la corrutina. Luego lanza una excepción "GeneratorExit" en el
   punto de suspensión, causando que la corrutina se borre a sí misma.
   Finalmente, la corrutina es marcada como completada, aún si nunca
   inició.

   Objetos de corrutina son cerrados automáticamente utilizando el
   proceso anterior cuando están a punto de ser destruidos.

### 3.4.3. Iteradores asíncronos

Un *iterador asíncrono* puede llamar código asíncrono en su método
"__anext__".

Iteradores asíncronos pueden ser utilizados en la declaración "async
for".

The "object" class itself does not provide these methods.

object.__aiter__(self)

   Debe retornar un objeto de *iterador asíncrono*.

object.__anext__(self)

   Debe retornar un *esperable* (awaitable) resultante en el siguiente
   valor del iterador. Debe levantar una excepción
   "StopAsyncIteration" cuando la iteración termina.

Un ejemplo de objeto iterable asíncrono:

   class Reader:
       async def readline(self):
           ...

       def __aiter__(self):
           return self

       async def __anext__(self):
           val = await self.readline()
           if val == b'':
               raise StopAsyncIteration
           return val

Added in version 3.5.

Distinto en la versión 3.7: Antes de Python 3.7, "__aiter__()" podía
retornar un *awaitable* que se resolvería en un *asynchronous
iterator*.A partir de Python 3.7, "__aiter__()" debe retornar un
objeto iterador asincrónico. Retornar cualquier otra cosa resultará en
un error "TypeError".

### 3.4.4. Gestores de contexto asíncronos

Un *gestor de contexto asíncrono* es un *gestor de contexto* que puede
suspender la ejecución en sus métodos "__aenter__" y "__aexit__".

Los gestores de contexto asíncronos pueden ser utilizados en una
declaración "async with".

The "object" class itself does not provide these methods.

object.__aenter__(self)

   Semánticamente similar a "__enter__()", siendo la única diferencia
   que debe retornar un *esperable*.

object.__aexit__(self, exc_type, exc_value, traceback)

   Semánticamente similar a "__exit__()", siendo la única diferencia
   que debe retornar un *esperable*.

Un ejemplo de una clase de gestor de contexto asíncrono:

   class AsyncContextManager:
       async def __aenter__(self):
           await log('entering context')

       async def __aexit__(self, exc_type, exc, tb):
           await log('exiting context')

Added in version 3.5.

-[ Notas a pie de página ]-

[1] Es posible cambiar en algunos casos un tipo de objeto bajo ciertas
    circunstancias controladas. Generalmente no es buena idea, ya que
    esto puede llevar a un comportamiento bastante extraño de no ser
    tratado correctamente.

[2] Los métodos "__hash__()", "__iter__()", "__reversed__()",
    "__contains__()", "__class_getitem__()" y "__fspath__()" tienen un
    manejo especial para esto. Otros seguirán lanzando un "TypeError",
    pero pueden hacerlo confiando en el comportamiento de que "None"
    no es invocable.

[3] "No soporta" aquí significa que la clase no tiene tal método, o el
    método retorna "NotImplemented". No establecer el método a "None"
    si se quiere forzar el retroceso al método reflejado del operando
    correcto—eso, por el contrario, tendrá un efecto opuesto de
    *bloquear* explícitamente dicho retroceso.

[4] For operands of the same type, it is assumed that if the non-
    reflected method (such as "__add__()") fails then the operation is
    not supported, which is why the reflected method is not called.

[5] If the right operand's type is a subclass of the left operand's
    type, the reflected method having precedence allows subclasses to
    override their ancestors' operations.
