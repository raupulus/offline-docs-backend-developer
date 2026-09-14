---
title: 6. Expresiones
source_url: https://docs.python.org/es/3
source_path: reference/expressions.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: reference
order: 4780
---

# 6. Expresiones

Este capítulo explica el significado de los elementos de expresiones
en Python.

**Syntax Notes:** In this and the following chapters, grammar notation
will be used to describe syntax, not lexical analysis.

When (one alternative of) a syntax rule has the form:

   name: othername

y no han sido dadas semánticas, las semánticas de esta forma de "name"
son las mismas que para "othername".

## 6.1. Conversiones aritméticas

When a description of an arithmetic operator below uses the phrase
"the numeric arguments are converted to a common real type", this
means that the operator implementation for built-in numeric types
works as described in the Numeric Types section of the standard
library documentation.

Some additional rules apply for certain operators and non-numeric
operands (for example, a string as a left argument to the "%"
operator). Extensions must define their own conversion behavior.

## 6.2. Átomos

Atoms are the most basic elements of expressions. The simplest atoms
are names or literals. Forms enclosed in parentheses, brackets or
braces are also categorized syntactically as atoms.

Formally, the syntax for atoms is:

   atom:
      | 'True'
      | 'False'
      | 'None'
      | '...'
      | identifier
      | literal
      | enclosure
   enclosure:
      | parenth_form
      | list_display
      | dict_display
      | set_display
      | generator_expression
      | yield_atom

### 6.2.1. Built-in constants

The keywords "True", "False", and "None" name built-in constants. The
token "..." names the "Ellipsis" constant.

Evaluation of these atoms yields the corresponding value.

Nota:

  Several more built-in constants are available as global variables,
  but only the ones mentioned here are keywords. In particular, these
  names cannot be reassigned or used as attributes:

     >>> False = 123
       File "<input>", line 1
        False = 123
        ^^^^^
     SyntaxError: cannot assign to False

### 6.2.2. Identificadores (Nombres)

Un identificador encontrándose como un átomo es un nombre. Vea la
sección Names (identifiers and keywords) para la definición léxica y
la sección Nombres y vínculos para documentación de nombrar y
vincular.

Cuando el nombre es vinculado a un objeto, la evaluación del átomo
genera ese objeto. Cuando un nombre no es vinculado, un intento de
evaluarlo genera una excepción "NameError".

#### 6.2.2.1. Alteración de nombre privado

Cuando un identificador que ocurre textualmente en una definición de
clase comienza con dos o más caracteres de guión bajo y no termina en
dos o más guiones bajos, es considerado un *private name* de esa
clase.

Ver también: La class specifications.

Más concretamente, los nombres privados son transformados a una forma
más larga antes de que se genere código para ellos.  Si el nombre
transformado tiene más de 255 caracteres, puede producirse un
truncamiento definido por la implementación.

La transformación es independiente del contexto sintáctico en el que
se utilice el identificador, pero sólo se alteran los siguientes
identificadores privados:

* Cualquier nombre utilizado como nombre de una variable que se asigna
  o se lee o cualquier nombre de un atributo al que se accede.

  Sin embargo, el atributo  "__name__" de funciones anidadas, clases y
  alias de tipo no son alterados.

* El nombre de módulos importados, por ejemplo "__spam" en "import
  __spam". Si el módulo es parte de un paquete (por ejemplo, si su
  nombre contiene un punto), el nombre *no* es alterado. Por ejemplo,
  "__foo" en "import __foo.bar" no es alterado.

* El nombre de un miembro importado, por ejemplo "__f" en "from spam
  import __f".

La norma de transformación se define de la siguiente forma:

* El nombre de la clase, con los caracteres de guión bajo iniciales
  eliminados y un único caracter de guión bajo inicial insertado, se
  inserta delante del identificador. Por ejemplo, el identificador
  "__spam" que aparece en la clase llamada "Foo", "_Foo" o "__Foo" se
  transforma en "_Foo__spam".

* Si el nombre de la clase consiste únicamente en caracteres de guión
  bajo, la transformación es la identidad. Por ejemplo, el
  identificador "__spam" que aparece en una clase llamada "_" o "__"
  permanece igual.

### 6.2.3. Literales

A *literal* is a textual representation of a value. Python supports
numeric, string and bytes literals. Format strings and template
strings are treated as string literals.

Numeric literals consist of a single "NUMBER" token, which names an
integer, floating-point number, or an imaginary number. See the
Literales numéricos section in Lexical analysis documentation for
details.

String and bytes literals may consist of several tokens. See section
String literal concatenation for details.

Note that negative and complex numbers, like "-3" or "3+4.2j", are
syntactically not literals, but unary or binary arithmetic operations
involving the "-" or "+" operator.

Evaluation of a literal yields an object of the given type ("int",
"float", "complex", "str", "bytes", or "Template") with the given
value. The value may be approximated in the case of floating-point and
imaginary literals.

The formal grammar for literals is:

   literal: strings | NUMBER

#### 6.2.3.1. Literals and object identity

Todos los literales corresponden a tipos de datos inmutables y, por lo
tanto, la identidad del objeto es menos importante que su valor.
Múltiples evaluaciones de literales con el mismo valor (ya sea la
misma ocurrencia en el texto del programa o una ocurrencia diferente)
pueden obtener el mismo objeto o un objeto diferente con el mismo
valor.

CPython implementation detail: For example, in CPython, *small*
integers with the same value evaluate to the same object:

   >>> x = 7
   >>> y = 7
   >>> x is y
   True

However, large integers evaluate to different objects:

   >>> x = 123456789
   >>> y = 123456789
   >>> x is y
   False

This behavior may change in future versions of CPython. In particular,
the boundary between "small" and "large" integers has already changed
in the past.CPython will emit a "SyntaxWarning" when you compare
literals using "is":

   >>> x = 7
   >>> x is 7
   <input>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
   True

See ¿Cuándo puedo fiarme de pruebas de identidad con el operador is?
for more information.

Template strings are immutable but may reference mutable objects as
"Interpolation" values. For the purposes of this section, two
t-strings have the "same value" if both their structure and the
*identity* of the values match.

**Detalles de implementación de CPython:** Currently, each evaluation
of a template string results in a different object.

#### 6.2.3.2. String literal concatenation

Multiple adjacent string or bytes literals, possibly using different
quoting conventions, are allowed, and their meaning is the same as
their concatenation:

   >>> "hello" 'world'
   "helloworld"

This feature is defined at the syntactical level, so it only works
with literals. To concatenate string expressions at run time, the '+'
operator may be used:

   >>> greeting = "Hello"
   >>> space = " "
   >>> name = "Blaise"
   >>> print(greeting + space + name)   # not: print(greeting space name)
   Hello Blaise

Literal concatenation can freely mix raw strings, triple-quoted
strings, and formatted string literals. For example:

   >>> "Hello" r', ' f"{name}!"
   "Hello, Blaise!"

This feature can be used to reduce the number of backslashes needed,
to split long strings conveniently across long lines, or even to add
comments to parts of strings. For example:

   re.compile("[A-Za-z_]"       # letter or underscore
              "[A-Za-z0-9_]*"   # letter, digit or underscore
             )

However, bytes literals may only be combined with other byte literals;
not with string literals of any kind. Also, template string literals
may only be combined with other template string literals:

   >>> t"Hello" t"{name}!"
   Template(strings=('Hello', '!'), interpolations=(...))

Formally:

   strings: (STRING | fstring)+ | tstring+

### 6.2.4. Formas entre paréntesis

Una forma entre paréntesis es una lista de expresiones opcionales
encerradas entre paréntesis:

   parenth_form: "(" [starred_expression] ")"

Una expresión entre paréntesis produce lo que la lista de expresión
*yield*: si la lista contiene al menos una coma, produce una tupla; en
caso contrario, produce la única expresión que que forma la lista de
expresiones.

Un par de paréntesis vacío produce un objeto de tupla vacío. Debido a
que las tuplas son inmutables, se aplican las mismas reglas que
aplican para literales (ej., dos ocurrencias de una tupla vacía puede
o no produce el mismo objeto).

Tenga en cuenta que las tuplas no se forman con paréntesis, sino
mediante el uso de coma. La excepción es la tupla vacía, para la cual
*se* requieren paréntesis. Permitir "nada" sin paréntesis en las
expresiones causaría ambigüedades y permitiría que errores
tipográficos comunes pasaran sin detectarse.

### 6.2.5. Despliegues para listas, conjuntos y diccionarios

Para construir una lista, un conjunto o un diccionario, Python provee
sintaxis especial denominada "despliegue", cada una de ellas en dos
sabores:

* los contenidos del contenedor son listados explícitamente o

* son calculados mediante un conjunto de instrucciones de bucle y
  filtrado, denominadas una *comprehension*.

Los elementos comunes de sintaxis para las comprensiones son:

   comprehension: assignment_expression comp_for
   comp_for:      ["async"] "for" target_list "in" or_test [comp_iter]
   comp_iter:     comp_for | comp_if
   comp_if:       "if" or_test [comp_iter]

La comprensión consiste en una única expresión seguida por al menos
una cláusula "for" y cero o más cláusulas "for" o "if". En este caso,
los elementos del nuevo contenedor son aquellos que serían producidos
mediante considerar cada una de las cláusulas "for" o "if" un bloque,
anidado de izquierda a derecha y evaluando la expresión para producir
un elemento cada vez que se alcanza el bloque más interno.

Sin embargo, aparte de la expresión iterable en la cláusula "for" más
a la izquierda, la comprensión es ejecutada en un alcance separado
implícitamente anidado. Esto asegura que los nombres asignados a en la
lista objetiva no se "filtren" en el alcance adjunto.

La expresión iterable en la cláusula más a la izquierda "for" es
evaluada directamente en el alcance anidado y luego pasada como un
argumento al alcance implícitamente anidado. Subsecuentes cláusulas
"for" y cualquier condición de filtro en la cláusula "for" más a la
izquierda no pueden ser evaluadas en el alcance adjunto ya que pueden
depender de los valores obtenidos del iterable de más a la izquierda.
Por ejemplo, "[x*y for x in range(10) for y in range(x, x+10)]".

Para asegurar que la comprensión siempre resulta en un contenedor del
tipo apropiado, las expresiones "yield" y "yield from" están
prohibidas en el alcance implícitamente anidado.

Desde Python 3.6, en una función "async def", se puede usar una
cláusula "async for" para iterar sobre un *asynchronous iterator*. Una
comprensión en una función "async def" puede consistir en una cláusula
"for" o "async for" después de la expresión inicial, puede contener
cláusulas adicionales "for" o "async for" y también puede usar
expresiones "await".

Si una comprensión contiene cláusulas "async for" or si contiene
expresiones "await" u otra comprensión asíncrona en cualquier sitio
excepto la expresión iterable en la cláusula "for" más a la izquierda,
se le llama una *asynchronous comprehension*. Una comprensión
asíncrona podría suspender la ejecución de la función de corutina en
la que aparece. Consulte también **PEP 530**.

Added in version 3.6: Fueron introducidas las comprensiones
asincrónicas.

Distinto en la versión 3.8: Prohibidas "yield" y "yield from" en el
alcance implícitamente anidado.

Distinto en la versión 3.11: Las comprensiones asincrónicas ahora
están permitidas dentro de las comprensiones en funciones
asincrónicas. Las comprensiones externas implícitamente se vuelven
asincrónicas.

### 6.2.6. Despliegues de lista

Un despliegue de lista es una serie de expresiones posiblemente vacía
encerrada entre corchetes:

   list_display: "[" [flexible_expression_list | comprehension] "]"

Un despliegue de lista produce un nuevo objeto lista, el contenido se
especifica por una lista de expresiones o una comprensión. Cuando se
proporciona una lista de expresiones, sus elementos son evaluados
desde la izquierda a la derecha y colocados en el objeto lista en ese
orden. Cuando se proporciona una comprensión, la lista es construida
desde los elementos resultantes de la comprensión.

### 6.2.7. Despliegues de conjuntos

Un despliegue de conjunto se denota mediante llaves y se distinguen de
los despliegues de diccionarios por la ausencia de caracteres de doble
punto separando claves y valores:

   set_display: "{" (flexible_expression_list | comprehension) "}"

Un despliegue de conjunto produce un nuevo objeto conjunto mutable, el
contenido se especifica mediante una secuencia de expresiones o una
comprensión. Cuando se proporciona una lista de expresiones separadas
por comas, sus elementos son evaluados desde la izquierda a la derecha
y añadidos al objeto de conjunto. Cuando se proporciona una
comprensión, el conjunto es construido de los elementos resultantes de
la comprensión.

Un conjunto vacío no puede ser construido con "{}"; este literal
construye un diccionario vacío.

### 6.2.8. Despliegues de diccionario

La visualización de un diccionario es una serie posiblemente vacía de
elementos de dictado (pares clave/valor) encerrados entre llaves:

   dict_display:       "{" [dict_item_list | dict_comprehension] "}"
   dict_item_list:     dict_item ("," dict_item)* [","]
   dict_item:          expression ":" expression | "**" or_expr
   dict_comprehension: expression ":" expression comp_for

Un despliegue de diccionario produce un nuevo objeto diccionario.

Si se proporciona una secuencia de elementos dict separados por comas,
se evalúan de izquierda a derecha para definir las entradas del
diccionario: cada objeto clave se utiliza como clave en el diccionario
para almacenar el valor correspondiente. Esto significa que puede
especificar la misma clave varias veces en la lista de elementos de
dictado, y el valor final del diccionario para esa clave será el
último que se proporcione.

Un asterisco doble "**" indica *descomprimiendo el diccionario*. Su
operando debe ser un *mapping*. Cada elemento de mapeo se agrega al
nuevo diccionario. Los valores posteriores reemplazan los valores ya
establecidos por elementos de dictado anteriores y desempaquetados de
diccionarios anteriores.

Added in version 3.5: Desempaquetar en despliegues de diccionarios,
originalmente propuesto por **PEP 448**.

Una comprensión de diccionario, en contraste a las compresiones de
lista y conjunto, necesita dos expresiones separadas con un caracter
de doble punto seguido por las cláusulas usuales "for" e "if". Cuando
la comprensión se ejecuta, los elementos resultantes clave y valor son
insertados en el nuevo diccionario en el orden que son producidos.

Las restricciones sobre los tipos de valores clave se enumeran
anteriormente en la sección Jerarquía de tipos estándar. (En resumen,
el tipo de clave debe ser *hashable*, que excluye todos los objetos
mutables). No se detectan conflictos entre claves duplicadas;
prevalece el último valor (textualmente más a la derecha en la
pantalla) almacenado para un valor clave determinado.

Distinto en la versión 3.8: Antes de Python 3.8, en las comprensiones
de diccionarios, el orden de evaluación de clave y valor no fue bien
definido. En CPython, el valor fue evaluado antes de la clave. A
partir de 3.8, la clave es evaluada antes que el valor, como fue
propuesto por **PEP 572**.

### 6.2.9. Expresiones de generador

The syntax for *generator expressions* is the same as for list
comprehensions, except that they are enclosed in parentheses instead
of brackets. For example:

   >>> iterator = (x ** 2 for x in range(10))
   >>> iterator
   <generator object <genexpr> at ...>

At runtime, a generator expression evaluates to a *generator iterator*
which yields the same values as the corresponding list comprehension:

   >>> list(iterator)
   [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

Thus, the example above is roughly equivalent to defining and calling
the following generator function:

   def make_generator_of_squares(iterator):
       for x in iterator:
           yield x ** 2

   make_generator_of_squares(iter(range(10)))

The enclosing parentheses can be omitted in calls when the generator
expression is the only positional argument and there are no keyword
arguments. See the Calls section for details. For example:

   # The parentheses after `sum` are part of the call syntax:
   >>> sum(x ** 2 for x in range(10))
   285

   # The generator needs its own parentheses if it's not the only argument:
   >>> sum((x ** 2 for x in range(10)), start=1000)
   1285

The iterable expression in the leftmost "for" clause is evaluated
immediately, so that an error raised by this expression will be
emitted at the point where the generator expression is defined, rather
than at the point where the first value is retrieved:

   >>> (x ** 2 for x in nonexistent_iterable)
   Traceback (most recent call last):
     ...
   NameError: name 'nonexistent_iterable' is not defined

After the expression is evaluated, an iterator is created from the
result, as if "iter()" was called on it. Any error raised when
creating the iterator is also emitted immediately:

   >>> (x ** 2 for x in None)
   Traceback (most recent call last):
     ...
   TypeError: 'NoneType' object is not iterable

All other expressions are evaluated lazily, in the same fashion as
normal generators (that is, when the iterator is asked to yield a
value):

   >>> iterator = (nonexistent_value for x in range(10))
   >>> iterator
   <generator object <genexpr> at ...>
   >>> list(iterator)
   Traceback (most recent call last):
     ...
   NameError: name 'nonexistent_value' is not defined

   >>> iterator = (x * y for x in range(10) for y in nonexistent_iterable)
   >>> iterator
   <generator object <genexpr> at ...>
   >>> list(iterator)
   Traceback (most recent call last):
     ...
   NameError: name 'nonexistent_iterable' is not defined

To avoid interfering with the expected operation of the generator
expression itself, "yield" and "yield from" expressions are prohibited
inside the implicitly nested scope.

If a generator expression contains either "async for" clauses or
"await" expressions it is called an *asynchronous generator
expression*. An asynchronous generator expression returns a new
asynchronous generator object, which is an asynchronous iterator (see
Iteradores asíncronos).

The formal grammar for generator expressions is:

   generator_expression: "(" expression comp_for ")"

Added in version 3.6: Las expresiones de generador asincrónico fueron
introducidas.

Distinto en la versión 3.7: Antes de Python 3.7, las expresiones de
generador asincrónico podrían aparecer sólo en corrutinas "async def".
Desde 3.7, cualquier función puede usar expresiones de generador
asincrónico.

Distinto en la versión 3.8: Prohibidas "yield" y "yield from" en el
alcance implícitamente anidado.

### 6.2.10. Expresiones *yield*

   yield_atom:       "(" yield_expression ")"
   yield_from:       "yield" "from" expression
   yield_expression: "yield" yield_list | yield_from

La expresión *yield* se usa al definir una función *generator* o una
función *asynchronous generator* y, por lo tanto, solo se puede usar
en el cuerpo de una definición de función. El uso de una expresión
*yield* en el cuerpo de una función hace que esa función sea una
función generadora, y su uso en el cuerpo de una función "async def"
hace que la función corrutina sea una función generadora asíncrona.
Por ejemplo:

   def gen():  # define una función generadora
       yield 123

   async def agen(): # define una función generadora asíncrona

Debido a sus efectos secundarios sobre el alcance contenedor, las
expresiones "yield" no están permitidas como parte de los alcances
implícitamente definidos usados para implementar comprensiones y
expresiones de generador.

Distinto en la versión 3.8: Expresiones *yield* prohibidas en los
ámbitos anidados implícitamente utilizados para implementar
comprensiones y expresiones de generador.

Las funciones generadoras son descritas a continuación, mientras que
las funciones generadoras asincrónicas son descritas separadamente en
la sección Funciones generadoras asincrónicas.

Cuando se llama a una función generadora, retorna un iterador conocido
como generador. Ese generador luego controla la ejecución de la
función del generador. La ejecución comienza cuando se llama a uno de
los métodos del generador. En ese momento, la ejecución procede con la
primera expresión *yield*, donde se suspende nuevamente, retornando el
valor de "yield_list" a quien llame al generador, o "None" si
"yield_list" se omite. Por suspendido entiéndase que se retiene todo
el estado local, incluyendo los enlaces actuales de las variables
locales, el puntero de instrucción, la pila de evaluación interna y el
estado de cualquier manejo de excepciones. Cuando se reanuda la
ejecución llamando a uno de los métodos del generador, la función
puede continuar exactamente como si la expresión *yield* fuera
simplemente otra llamada externa. El valor de la expresión *yield*
después de la reanudación depende del método que reanudó la ejecución.
Si se utiliza "__next__()" (normalmente a través de un "for" o la
función incorporada "next()"), el resultado es "None". De lo
contrario, si se utiliza "send()", el resultado será el valor pasado a
ese método.

Todo este hace a las funciones generadores similar a las corrutinas;
producen múltiples veces, tienen más de un punto de entrada y su
ejecución puede ser suspendida. La única diferencia es que una función
generadora no puede controlar si la ejecución debe continuar después
de que ceda; el control siempre es transferido al invocador del
generador.

Las expresiones *yield* están permitidas en cualquier lugar en un
constructo "try". Si el generador no es reanudado antes de finalizar
(alcanzando un recuento de referencia cero o colectando basura), el
método generador-iterador "close()" será invocado, permitiendo la
ejecución de cualquier cláusula "finally" pendiente.

Cuando se usa "yield from <expr>", la expresión proporcionada debe ser
iterable. Los valores producidos al iterar ese iterable se pasan
directamente al llamador de los métodos del generador actual.
Cualquier valor pasado con "send()" y cualquier excepción pasada con
"throw()" se pasan al iterador subyacente si tiene los métodos
apropiados. Si este no es el caso, entonces "send()" lanzará
"AttributeError" o "TypeError", mientras que "throw()" solo lanzará la
excepción pasada inmediatamente.

Cuando el iterador subyacente está completo, el atributo "value" de la
instancia "StopIteration" generada se convierte en el valor de la
expresión *yield*. Puede ser establecido explícitamente al generar
"StopIteration" o automáticamente cuando el subiterador es un
generador (retornando un valor del subgenerador).

Distinto en la versión 3.3: Añadido "yield from <expr>" para delegar
el control de flujo a un subiterador.

Los paréntesis pueden ser omitidos cuando la expresión *yield* es la
única expresión en el lado derecho de una sentencia de asignación.

Ver también:

  **PEP 255** - Generadores Simples
     La propuesta para añadir generadores y la sentencia "yield" a
     Python.

  **PEP 342** - Corrutinas mediante Generadores Mejorados
     La propuesta para mejorar la API y la sintaxis de generadores,
     haciéndolos utilizables como corrutinas simples.

  **PEP 380** - Sintaxis para Delegar a un Subgenerador
     La propuesta para introducir la sintaxis "yield_from",
     facilitando la delegación a subgeneradores.

  **PEP 525**- Generadores Asincrónicos
     La propuesta que expandió **PEP 492** añadiendo capacidades de
     generador a las funciones corrutina.

#### 6.2.10.1. Métodos generador-iterador

Esta subsección describe los métodos de un generador iterador. Estos
pueden ser usados para controlar la ejecución de una función
generadora.

Tenga en cuenta que invocar cualquiera de los métodos de generador
siguientes cuando el generador está todavía en ejecución genera una
excepción "ValueError".

generator.__next__()

   Inicia la ejecución de una función generadora o la reanuda en la
   última expresión de rendimiento ejecutada. Cuando se reanuda una
   función de generador con un método "send()", la expresión de
   rendimiento actual siempre se evalúa como "None". Luego, la
   ejecución continúa con la siguiente expresión de rendimiento, donde
   el generador se suspende nuevamente y el valor de "yield_list" se
   retorna a la aquello que llame "__next__()". Si el generador sale
   sin generar otro valor, se lanza una excepción "StopIteration".

   Este método es normalmente invocado implícitamente, por ejemplo,
   por un bucle "for" o por la función incorporada "next()".

generator.send(value)

   Reanuda la ejecución y "envía" un valor dentro de la función
   generadora. El argumento *value* se convierte en el resultado de la
   expresión *yield* actual. El método "send()" retorna el siguiente
   valor producido por el generador o genera "StopIteration" si el
   generador termina sin producir otro valor. Cuando se ejecuta
   "send()" para comenzar el generador, debe ser invocado con "None"
   como el argumento, debido a que no hay expresión yield que pueda
   recibir el valor.

generator.throw(value)
generator.throw(type[, value[, traceback]])

   Genera una excepción en el punto donde se pausó el generador y
   retorna el siguiente valor generado por la función del generador.
   Si el generador sale sin generar otro valor, se genera una
   excepción "StopIteration". Si la función generadora no detecta la
   excepción pasada o genera una excepción diferente, esa excepción se
   propaga a la persona que llama.

   En el uso típico, esto se llama con una sola instancia de excepción
   similar a la forma en que se usa la palabra clave "raise".

   Sin embargo, para la compatibilidad con versiones anteriores, se
   admite la segunda firma, siguiendo una convención de versiones
   anteriores de Python. El argumento *type* debe ser una clase de
   excepción y *value* debe ser una instancia de excepción. Si no se
   proporciona *value*, se llama al constructor *type* para obtener
   una instancia. Si se proporciona *traceback*, se establece en la
   excepción; de lo contrario, se puede borrar cualquier atributo
   "__traceback__" existente almacenado en *value*.

   Distinto en la versión 3.12: La segunda firma (type[, value[,
   traceback]]) está obsoleta y puede eliminarse en una versión futura
   de Python.

generator.close()

   Raises a "GeneratorExit" exception at the point where the generator
   function was paused (equivalent to calling "throw(GeneratorExit)").
   The exception is raised by the yield expression where the generator
   was paused. If the generator function catches the exception and
   returns a value, this value is returned from "close()".  If the
   generator function is already closed, or raises "GeneratorExit" (by
   not catching the exception), "close()" returns "None".  If the
   generator yields a value, a "RuntimeError" is raised.  If the
   generator raises any other exception, it is propagated to the
   caller.  If the generator has already exited due to an exception or
   normal exit, "close()" returns "None" and has no other effect.

   Distinto en la versión 3.13: Si un generador retorna un valor al
   cerrarse, el valor es retornado por "close()".

#### 6.2.10.2. Ejemplos

Aquí hay un ejemplo simple que demuestra el comportamiento de
generadores y funciones generadoras:

   >>> def echo(value=None):
   ...     print("Execution starts when 'next()' is called for the first time.")
   ...     try:
   ...         while True:
   ...             try:
   ...                 value = (yield value)
   ...             except Exception as e:
   ...                 value = e
   ...     finally:
   ...         print("Don't forget to clean up when 'close()' is called.")
   ...
   >>> generator = echo(1)
   >>> print(next(generator))
   Execution starts when 'next()' is called for the first time.
   1
   >>> print(next(generator))
   None
   >>> print(generator.send(2))
   2
   >>> generator.throw(TypeError, "spam")
   TypeError('spam',)
   >>> generator.close()
   Don't forget to clean up when 'close()' is called.

Para ejemplos usando "yield from", ver PEP 380: Sintaxis para delegar
en un subgenerador en "Qué es nuevo en Python."

#### 6.2.10.3. Funciones generadoras asincrónicas

La presencia de una expresión *yield* en una función o método definido
usando "async def" adicionalmente define la función como una función
*asynchronous generator*.

Cuando se invoca una función generadora asincrónica, retorna un
iterador asincrónico conocido como un objeto generador asincrónico.
Este objeto entonces controla la ejecución de la función generadora.
Un objeto generador asincrónico se usa típicamente en una sentencia
"async for" en una función corrutina análogamente a como sería usado
un objeto generador en una sentencia "for".

Llamar a uno de los métodos del generador asíncrono retorna un objeto
*awaitable* y la ejecución comienza cuando se espera este objeto. En
ese momento, la ejecución procede a la primera expresión *yield*,
donde se suspende nuevamente, retornando el valor de "yield_list" a la
corutina en espera. Al igual que con un generador, la suspensión
significa que se retiene todo el estado local, incluidos los enlaces
actuales de las variables locales, el puntero de instrucción, la pila
de evaluación interna y el estado de cualquier manejo de excepción.
Cuando se reanuda la ejecución esperando el siguiente objeto retornado
por los métodos del generador asíncrono, la función puede proceder
exactamente como si la expresión *yield* fuera simplemente otra
llamada externa. El valor de la expresión *yield* después de reanudar
depende del método que reanudó la ejecución. Si se utiliza
"__anext__()", el resultado es "None". De lo contrario, si se usa
"asend()", el resultado será el valor pasado a ese método.

Si un generador asincrónico sale temprano por "break", la tarea de la
persona que llama se cancela u otras excepciones, el código de
limpieza asíncrono del generador se ejecutará y posiblemente lanzará
excepciones o accederá a variables de contexto en un contexto
inesperado, tal vez después de la vida útil de las tareas de las que
depende, o durante el cierre del ciclo de eventos cuando se llama al
gancho de recolección de basura del generador asíncrono. Para evitar
esto, la persona que llama debe cerrar explícitamente el generador
asíncrono llamando al método "aclose()" para finalizar el generador y
finalmente desconectarlo del bucle de eventos.

En una función generadora asincrónica, las expresiones *yield* están
permitidas en cualquier lugar de un constructo "try". Sin embargo, si
un generador asincrónico no es reanudado antes de finalizar
(alcanzando un contador de referencia cero o recogiendo basura),
entonces una expresión *yield* dentro de un constructo "try" podría
fallar al ejecutar cláusulas "finally" pendientes. En este caso, es
responsabilidad del bucle de eventos o del planificador ejecutando el
generador asincrónico invocar el método "aclose()" del generador-
iterador asincrónico y ejecutar el objeto corrutina resultante,
permitiendo así la ejecución de cualquier cláusula "finally"
pendiente.

Para encargarse de la finalización tras la finalización del ciclo de
eventos, un ciclo de eventos debe definir una función *finalizer* que
tome un generador-iterador asíncrono y presumiblemente llame a
"aclose()" y ejecute la rutina. Este *finalizer* se puede registrar
llamando a "sys.set_asyncgen_hooks()". Cuando se itera por primera
vez, un generador-iterador asíncrono almacenará el *finalizer*
registrado para ser llamado al finalizar. Para obtener un ejemplo de
referencia de un método *finalizer*, consulte la implementación de
"asyncio.Loop.shutdown_asyncgens" en Lib/asyncio/base_events.py.

La expresión "yield from <expr>" es un error de sintaxis cuando es
usada en una función generadora asincrónica.

#### 6.2.10.4. Métodos asincrónicos de generador-iterador

Esta subsección describe los métodos de un generador iterador
asincrónico, los cuales son usados para controlar la ejecución de una
función generadora.

async agen.__anext__()

   Retorna un aguardable que, cuando se ejecuta, comienza a ejecutar
   el generador asíncrono o lo reanuda en la última expresión *yield*
   ejecutada. Cuando se reanuda una función de generador asíncrono con
   un método  "__anext__()", la expresión *yield* actual siempre se
   evalúa como "None" en el aguardable retornado, que cuando se
   ejecute continuará con la siguiente expresión *yield*. El valor de
   "yield_list" de la expresión *yield* es el valor de la excepción
   "StopIteration" generada por la corutina de finalización. Si el
   generador asincrónico finaliza sin generar otro valor, el
   aguardable genera una excepción "StopAsyncIteration", lo que indica
   que la iteración asincrónica se ha completado.

   Este método es invocado normalmente de forma implícita por un bucle
   "async for".

async agen.asend(value)

   Retorna un aguardable el cual ejecuta cuando se reanude la
   ejecución del generador asincrónico. Como el método "send()" para
   un generador, este "envía" un valor a la función generadora
   asincrónica y el argumento *value* se convierte en el resultado de
   la expresión *yield* actual. El aguardable retornado por el método
   "asend()" retornará el siguiente valor producido por el generador
   como el valor de la "StopIteration" generada o genera
   "StopAsyncIteration" si el generador asincrónico termina sin
   generar otro valor. Cuando se invoca "asend()" para empezar el
   generador asincrónico, debe ser invocado con "None" como argumento,
   porque no hay expresión *yield* que pueda recibir el valor.

async agen.athrow(value)
async agen.athrow(type[, value[, traceback]])

   Retorna un aguardable que genera una excepción de tipo "type" en el
   punto donde el generador asincrónico fue pausado y retorna el
   siguiente valor producido por la función generadora como el valor
   de la excepción "StopIteration" generada. Si el generador
   asincrónico termina sin producir otro valor, el aguardable genera
   una excepción "StopAsyncIteration". Si la función generadora no
   caza la excepción pasada o genera una excepción diferente, entonces
   cuando se ejecuta el aguardable esa excepción se propaga al
   invocador del aguardable.

   Distinto en la versión 3.12: La segunda firma (type[, value[,
   traceback]]) está obsoleta y puede eliminarse en una versión futura
   de Python.

async agen.aclose()

   Retorna un aguardable que cuando corre lanza un "GeneratorExit" a
   la función generadora asincrónica en el punto donde fue pausada. Si
   la función generadora asincrónica termina exitosamente, ya está
   cerrada o genera "GeneratorExit" (sin cazar la excepción), el
   aguardable retornado lanzará una excepción "StopIteration". Otros
   aguardables retornados por subsecuentes invocaciones al generador
   asincrónico lanzarán una excepción "StopAsyncIteration". Si el
   generador asincrónico produce un valor, el aguardable genera un
   "RuntimeError". Si el generador asincrónico genera cualquier otra
   excepción, esta es propagada al invocador del aguardable. Si el
   generador asincrónico ha terminado debido a una excepción o una
   terminación normal, entonces futuras invocaciones a "aclose()"
   retornarán un aguardable que no hace nada.

## 6.3. Primarios

Los primarios representan las operaciones más fuertemente ligadas al
lenguaje. Su sintaxis es:

   primary: atom | attributeref | subscription | call

### 6.3.1. Referencias de atributos

Una referencia de atributo es un primario seguido de un punto y un
nombre:

   attributeref: primary "." identifier

El primario debe evaluar a un objeto de un tipo que soporte
referencias de atributos, lo cual la mayoría de los objetos soportan.
Luego se le pide a este objeto que produzca el atributo cuyo nombre es
el identificador. Este tipo y valor producidos son determinados por el
objeto. Múltiples evaluaciones sobre la misma referencia de atributo
pueden producir objetos diferentes.

Esta producción puede ser personalizada al sobreescribir el método
"__getattribute__()" o "__getattr__()". El método "__getattribute__()"
es llamado primero y retorna un valor o se genera la excepción
"AttributeError" si el atributo no está disponible.

Si se genera una excepción "AttributeError" y el objeto tiene un
método "__getattr__()", dicho método es llamado como respaldo.

### 6.3.2. Subscriptions and slicings

The *subscription* syntax is usually used for selecting an element
from a container -- for example, to get a value from a "dict":

   >>> digits_by_name = {'one': 1, 'two': 2}
   >>> digits_by_name['two']  # Subscripting a dictionary using the key 'two'
   2

In the subscription syntax, the object being subscribed -- a primary
-- is followed by a *subscript* in square brackets. In the simplest
case, the subscript is a single expression.

Depending on the type of the object being subscribed, the subscript is
sometimes called a *key* (for mappings), *index* (for sequences), or
*type argument* (for *generic types*). Syntactically, these are all
equivalent:

   >>> colors = ['red', 'blue', 'green', 'black']
   >>> colors[3]  # Subscripting a list using the index 3
   'black'

   >>> list[str]  # Parameterizing the list type using the type argument str
   list[str]

At runtime, the interpreter will evaluate the primary and the
subscript, and call the primary's "__getitem__()" or
"__class_getitem__()" *special method* with the subscript as argument.
For more details on which of these methods is called, see
__class_getitem__ frente a __getitem__.

To show how subscription works, we can define a custom object that
implements "__getitem__()" and prints out the value of the subscript:

   >>> class SubscriptionDemo:
   ...     def __getitem__(self, key):
   ...         print(f'subscripted with: {key!r}')
   ...
   >>> demo = SubscriptionDemo()
   >>> demo[1]
   subscripted with: 1
   >>> demo['a' * 3]
   subscripted with: 'aaa'

See "__getitem__()" documentation for how built-in types handle
subscription.

Subscriptions may also be used as targets in assignment or deletion
statements. In these cases, the interpreter will call the subscripted
object's "__setitem__()" or "__delitem__()" *special method*,
respectively, instead of "__getitem__()".

   >>> colors = ['red', 'blue', 'green', 'black']
   >>> colors[3] = 'white'  # Setting item at index
   >>> colors
   ['red', 'blue', 'green', 'white']
   >>> del colors[3]  # Deleting item at index 3
   >>> colors
   ['red', 'blue', 'green']

All advanced forms of *subscript* documented in the following sections
are also usable for assignment and deletion.

#### 6.3.2.1. Segmentos

A more advanced form of subscription, *slicing*, is commonly used to
extract a portion of a sequence. In this form, the subscript is a
*slice*: up to three expressions separated by colons. Any of the
expressions may be omitted, but a slice must contain at least one
colon:

   >>> number_names = ['zero', 'one', 'two', 'three', 'four', 'five']
   >>> number_names[1:3]
   ['one', 'two']
   >>> number_names[1:]
   ['one', 'two', 'three', 'four', 'five']
   >>> number_names[:3]
   ['zero', 'one', 'two']
   >>> number_names[:]
   ['zero', 'one', 'two', 'three', 'four', 'five']
   >>> number_names[::2]
   ['zero', 'two', 'four']
   >>> number_names[:-3]
   ['zero', 'one', 'two']
   >>> del number_names[4:]
   >>> number_names
   ['zero', 'one', 'two', 'three']

When a slice is evaluated, the interpreter constructs a "slice" object
whose "start", "stop" and "step" attributes, respectively, are the
results of the expressions between the colons. Any missing expression
evaluates to "None". This "slice" object is then passed to the
"__getitem__()" or "__class_getitem__()" *special method*, as above.

   # continuing with the SubscriptionDemo instance defined above:
   >>> demo[2:3]
   subscripted with: slice(2, 3, None)
   >>> demo[::'spam']
   subscripted with: slice(None, None, 'spam')

#### 6.3.2.2. Comma-separated subscripts

The subscript can also be given as two or more comma-separated
expressions or slices:

   # continuing with the SubscriptionDemo instance defined above:
   >>> demo[1, 2, 3]
   subscripted with: (1, 2, 3)
   >>> demo[1:2, 3]
   subscripted with: (slice(1, 2, None), 3)

This form is commonly used with numerical libraries for slicing multi-
dimensional data. In this case, the interpreter constructs a "tuple"
of the results of the expressions or slices, and passes this tuple to
the "__getitem__()" or "__class_getitem__()" *special method*, as
above.

The subscript may also be given as a single expression or slice
followed by a comma, to specify a one-element tuple:

   >>> demo['spam',]
   subscripted with: ('spam',)

#### 6.3.2.3. "Starred" subscriptions

Added in version 3.11: Expressions in *tuple_slices* may be starred.
See **PEP 646**.

The subscript can also contain a starred expression. In this case, the
interpreter unpacks the result into a tuple, and passes this tuple to
"__getitem__()" or "__class_getitem__()":

   # continuing with the SubscriptionDemo instance defined above:
   >>> demo[*range(10)]
   subscripted with: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

Starred expressions may be combined with comma-separated expressions
and slices:

   >>> demo['a', 'b', *range(3), 'c']
   subscripted with: ('a', 'b', 0, 1, 2, 'c')

#### 6.3.2.4. Formal subscription grammar

   subscription:     primary '[' subscript ']'
   subscript:        single_subscript | tuple_subscript
   single_subscript: proper_slice | assignment_expression
   proper_slice:     [expression] ":" [expression] [ ":" [expression] ]
   tuple_subscript:  ','.(single_subscript | starred_expression)+ [',']

Recall that the "|" operator denotes ordered choice. Specifically, in
"subscript", if both alternatives would match, the first
("single_subscript") has priority.

### 6.3.3. Invocaciones

Una invocación invoca un objeto invocable (ej., una *function*) con
una serie posiblemente vacía de *argumentos*:

   call:                 primary "(" [argument_list [","] | comprehension] ")"
   argument_list:        positional_arguments ["," starred_and_keywords]
                           ["," keywords_arguments]
                         | starred_and_keywords ["," keywords_arguments]
                         | keywords_arguments
   positional_arguments: positional_item ("," positional_item)*
   positional_item:      assignment_expression | "*" expression
   starred_and_keywords: ("*" expression | keyword_item)
                         ("," "*" expression | "," keyword_item)*
   keywords_arguments:   (keyword_item | "**" expression)
                         ("," keyword_item | "," "**" expression)*
   keyword_item:         identifier "=" expression

Una coma final opcional puede estar presente después de los argumentos
posicionales y de palabra clave pero no afecta a las semánticas.

La clave primaria debe evaluar a un objeto invocable (funciones
definidas por el usuario, funciones incorporadas, métodos de objetos
incorporados, métodos de instancias de clases y todos los objetos que
tienen un método "__call__()" son invocables). Todas las expresiones
de argumento son evaluadas antes de que la invocación sea intentada.
Por favor, consulte la sección Definiciones de funciones para saber
más sobre la sintaxis de listas *parameter* formales.

Si hay argumentos de palabras clave, primero se convierten en
argumentos posicionales, de la siguiente manera. Primero, se crea una
lista de espacios vacantes para los parámetros formales. Si hay N
argumentos posicionales, se colocan en los primeros N espacios. A
continuación, para cada argumento de palabra clave, se utiliza el
identificador para determinar la ranura correspondiente (si el
identificador es el mismo que el nombre del primer parámetro formal,
se utiliza la primera ranura, y así sucesivamente). Si el espacio ya
está ocupado, se genera una excepción "TypeError". De lo contrario, el
argumento se coloca en el espacio, llenándolo (incluso si la expresión
es "None", llena el espacio). Cuando se han procesado todos los
argumentos, los espacios que aún están vacíos se llenan con el valor
predeterminado correspondiente de la definición de función. (Los
valores predeterminados se calculan, una vez, cuando se define la
función; por lo tanto, un objeto mutable como una lista o diccionario
usado como valor predeterminado será compartido por todas las llamadas
que no especifican un valor de argumento para la ranura
correspondiente; esto debería normalmente se evita.) Si hay espacios
vacíos para los cuales no se especifica ningún valor predeterminado,
se genera una excepción "TypeError". De lo contrario, la lista de
espacios ocupados se utiliza como lista de argumentos para la llamada.

Una implementación puede proveer funciones incorporadas cuyos
argumentos posicionales no tienen nombres, incluso si son "nombrados"
a efectos de documentación y los cuales por consiguiente no pueden ser
suplidos por palabras clave. En CPython, este es el caso para
funciones implementadas en C que usan "PyArg_ParseTuple()" para
analizar sus argumentos.

Si hay más argumentos posicionales que ranuras formales de parámetros,
se genera una excepción "TypeError", a no ser que un parámetro formal
usando la sintaxis "*identifier" se encuentre presente; en este caso,
ese parámetro formal recibe una tupla conteniendo los argumentos
posicionales sobrantes (o una tupla vacía su no hay argumentos
posicionales sobrantes).

Si un argumento de palabra clave no corresponde a un nombre de
parámetro formal, se genera una excepción "TypeError", a no ser que un
parámetro formal usando la sintaxis "**identifier" esté presente; en
este caso, ese parámetro formal recibe un diccionario que contiene los
argumentos de palabra clave sobrantes (usando las palabras clave como
claves y los valores de argumento como sus valores correspondientes),
o un (nuevo) diccionario vacío si no hay argumentos de palabra clave
sobrantes.

Si la sintaxis "*expression" aparece en la invocación de función,
"expression" debe evaluar a un *iterable*. Elementos de esos iterables
son tratados como si fueran argumentos posicionales adicionales. Para
la invocación "f(x1, x2, *y, x3, x4)", si *y* evalúa a una secuencia
*y1*, ..., *yM*, equivale a una invocación con M+4 argumentos
posicionales *x1*, *x2*, *y1*, ..., *yM*, *x3*, *x4*.

Una consecuencia de esto es que aunque la sintaxis "*expression" puede
aparecer *después* de argumentos de palabra clave explícitos, es
procesada *antes* de los argumentos de palabra clave (y cualquiera de
los argumentos "*expression" -- ver abajo). Así que:

   >>> def f(a, b):
   ...     print(a, b)
   ...
   >>> f(b=1, *(2,))

Es inusual que se utilicen argumentos de palabras clave y la sintaxis
"*expression" en la misma llamada, por lo que en la práctica esta
confusión no suele surgir.

Si la sintaxis "**expression" aparece en la llamada de función,
"expression" debe evaluarse como *mapping*, cuyo contenido se trata
como argumentos de palabras clave adicionales. Si a un parámetro que
coincide con una clave ya se le ha asignado un valor (mediante un
argumento de palabra clave explícito o de otro desempaquetado), se
genera una excepción "TypeError".

Cuando se usa "**expression", cada clave en esta asignación debe ser
una cadena. Cada valor del mapeo se asigna al primer parámetro formal
elegible para la asignación de palabras clave cuyo nombre es igual a
la clave. No es necesario que una clave sea un identificador de Python
(por ejemplo, ""max-temp °F"" es aceptable, aunque no coincidirá con
ningún parámetro formal que pueda declararse). Si no hay ninguna
coincidencia con un parámetro formal, el par clave-valor se recopila
mediante el parámetro "**"; si lo hay, o si no lo hay, se genera una
excepción "TypeError".

No pueden ser usados parámetros formales usando la sintaxis
"*identifier" o "**identifier" como ranuras de argumentos posicionales
o como nombres de argumentos de palabra clave.

Distinto en la versión 3.5: Las invocaciones de función aceptan
cualquier número de desempaquetados "*" y "**", los argumentos
posicionales pueden seguir a desempaquetados de iterable ("*") y los
argumentos de palabra clave pueden seguir a desempaquetados de
diccionario ("*"). Originalmente propuesto por **PEP 448**.

Una invocación siempre retorna algún valor, posiblemente "None", a no
ser que genere una excepción. Cómo se calcula este valor depende del
tipo del objeto invocable.

Si es---

una función definida por el usuario:
   The code block for the function is executed, passing it the
   argument list.  The first thing the code block will do is bind the
   formal parameters to the arguments; this is described in section
   Definiciones de funciones.  When the code block executes a "return"
   statement, this specifies the return value of the function call.
   If execution reaches the end of the code block without executing a
   "return" statement, the return value is "None".

una función o método incorporado:
   El resultado depende del intérprete; ver Funciones incorporadas
   para las descripciones de funciones y métodos incorporados.

un objeto de clase:
   Se retorna una nueva instancia de esa clase.

un método de una instancia de clase:
   Se invoca la función definida por el usuario correspondiente, con
   una lista de argumentos con un largo uno mayor que la lista de
   argumentos de la invocación: la instancia se convierte en el primer
   argumento.

una instancia de clase:
   La clase debe definir un método "__call__()" ; el efecto es
   entonces el mismo que si ese método fuera invocado.

## 6.4. Expresión await

Suspende la ejecución de *coroutine* o un objeto *awaitable*. Puede
ser usado sólo dentro de una *coroutine function*.

   await_expr: "await" primary

Added in version 3.5.

## 6.5. El operador de potencia

El operador de potencia se vincula más estrechamente que los
operadores unarios a su izquierda; se vincula con menos fuerza que los
operadores unarios a su derecha. La sintaxis es:

   power: (await_expr | primary) ["**" u_expr]

Por lo tanto, en una secuencia sin paréntesis de operadores unarios y
de potencia, los operadores son evaluados desde la derecha a la
izquierda (este no se constriñe al orden de evaluación para los
operandos): "-1**2" resulta en "-1".

The power operator has the same semantics as the built-in "pow()"
function, when called with two arguments: it yields its left argument
raised to the power of its right argument. Numeric arguments are first
converted to a common type, and the result is of that type.

Para operandos int, el resultado tiene el mismo tipo que los operandos
a no ser que el segundo argumento sea negativo; en ese caso, todos los
argumentos son convertidos a float y se entrega un resultado float.
Por ejemplo, "10**2" retorna "100", pero "10**-2" retorna "0.01".

Elevar "0.0" a una potencia negativa resulta en un
"ZeroDivisionError". Elevar un número negativo a una potencia
fraccional resulta en un número "complex". (En versiones anteriores se
genera un "ValueError".)

Esta operación se puede personalizar utilizando los métodos especiales
"__pow__()" y "__rpow__()".

## 6.6. Aritmética unaria y operaciones bit a bit

Toda la aritmética unaria y las operaciones bit a bit tienen la misma
prioridad:

   u_expr: power | "-" u_expr | "+" u_expr | "~" u_expr

El operador unario "-" (menos) genera la negación de su argumento
numérico; la operación se puede sobreescribir con el método especial
"__neg__()".

El operador unario "+" (más) genera su argumento numérico sin cambios;
la operación se puede sobreescribir con el método especial
"__pos__()".

El operador unario "~" (invertir) genera la inversión bit a bit de su
argumento entero. La inversión bit a bit de "x" se define como
"-(x+1)". Solo se aplica a números enteros o a objetos personalizados
que anulan el método especial "__invert__()".

En todos los tres casos, si el argumento no tiene el tipo apropiado,
se genera una excepción "TypeError".

## 6.7. Operaciones aritméticas binarias

Las operaciones aritméticas binarias tienen los niveles convencionales
de prioridad. Tenga en cuenta que algunas de esas operaciones también
aplican a ciertos tipos no numéricos. Aparte del operador de potencia,
hay sólo dos niveles, uno para operadores multiplicativos y uno para
aditivos:

   m_expr: u_expr | m_expr "*" u_expr | m_expr "@" m_expr |
           m_expr "//" u_expr | m_expr "/" u_expr |
           m_expr "%" u_expr
   a_expr: m_expr | a_expr "+" m_expr | a_expr "-" m_expr

The "*" (multiplication) operator yields the product of its arguments.
The arguments must either both be numbers, or one argument must be an
integer and the other must be a sequence. In the former case, the
numbers are converted to a common real type and then multiplied
together.  In the latter case, sequence repetition is performed; a
negative repetition factor yields an empty sequence.

Esta operación se puede personalizar utilizando los métodos especiales
"__mul__()" y "__rmul__()".

Distinto en la versión 3.14: If only one operand is a complex number,
the other operand is converted to a floating-point number.

El operador "@" (en) está destinado a ser usado para multiplicación de
matrices. Ningún tipo incorporado en Python implementa este operador.

Esta operación se puede personalizar utilizando los métodos especiales
"__matmul__()" y "__rmatmul__()".

Added in version 3.5.

The "/" (division) and "//" (floor division) operators yield the
quotient of their arguments.  The numeric arguments are first
converted to a common type. Division of integers yields a float, while
floor division of integers results in an integer; the result is that
of mathematical division with the 'floor' function applied to the
result.  Division by zero raises the "ZeroDivisionError" exception.

La operación de división se puede personalizar usando los métodos
especiales "__truediv__()" y "__rtruediv__()". La operación de
división entera se puede personalizar usando los métodos especiales
"__floordiv__()" y "__rfloordiv__()".

The "%" (modulo) operator yields the remainder from the division of
the first argument by the second.  The numeric arguments are first
converted to a common type. A zero right argument raises the
"ZeroDivisionError" exception.  The arguments may be floating-point
numbers, e.g., "3.14%0.7" equals "0.34" (since "3.14" equals "4*0.7 +
0.34".)  The modulo operator always yields a result with the same sign
as its second operand (or zero); the absolute value of the result is
strictly smaller than the absolute value of the second operand [1].

El operador de división entera a la baja y el de módulo están
conectados por la siguiente identidad: "x == (x//y)*y + (x%y)". La
división entera a la baja y el módulo también están conectadas por la
función incorporada "divmod()": "divmod(x, y) == (x//y, x%y)". [2].

Adicionalmente a realizar la operación módulo en números, el operador
"%" también está sobrecargado por objetos cadena de caracteres para
realizar formateo de cadenas al estilo antiguo (también conocido como
interpolación). La sintaxis para el formateo de cadenas está descrita
en la Referencia de la Biblioteca de Python, sección Formateo de
cadenas al estilo *printf*.

La operación *_modulo_* se puede personalizar utilizando los métodos
especiales "__mod__()" y "__rmod__()".

El operador de división entera a la baja, el operador de módulo y la
función "divmod()" no están definidas para números complejos. En su
lugar, convierta a un número de punto flotante usando la función
"abs()" si es necesario.

The "+" (addition) operator yields the sum of its arguments.  The
arguments must either both be numbers or both be sequences of the same
type.  In the former case, the numbers are converted to a common real
type and then added together. In the latter case, the sequences are
concatenated.

Esta operación se puede personalizar utilizando los métodos especiales
"__add__()" y "__radd__()".

Distinto en la versión 3.14: If only one operand is a complex number,
the other operand is converted to a floating-point number.

The "-" (subtraction) operator yields the difference of its arguments.
The numeric arguments are first converted to a common real type.

Esta operación se puede personalizar utilizando los métodos especiales
"__sub__()" y "__rsub__()".

Distinto en la versión 3.14: If only one operand is a complex number,
the other operand is converted to a floating-point number.

## 6.8. Operaciones de desplazamiento

Las operaciones de desplazamiento tienen menos prioridad que las
operaciones aritméticas:

   shift_expr: a_expr | shift_expr ("<<" | ">>") a_expr

Estos operadores aceptan enteros como argumentos. Ellos desplazan el
primer argumento a la izquierda o derecha el número de dígitos dados
por el segundo argumento.

Las operaciones de desplazamiento a la izquierda se pueden
personalizar usando los métodos especiales "__lshift__()" y
"__rlshift__()". Las operaciones de desplazamiento a la derecha se
pueden personalizar usando los métodos especiales "__rshift__()" y
"__rrshift__()".

Un desplazamiento de *n* bits hacia la derecha se define como una
división entera a la baja entre "pow(2,n)". Un desplazamiento de *n*
bits hacia la izquierda se define como una multiplicación por
"pow(2,n)".

## 6.9. Operaciones bit a bit binarias

Cada una de las tres operaciones de bits binarias tienen diferente
nivel de prioridad:

   and_expr: shift_expr | and_expr "&" shift_expr
   xor_expr: and_expr | xor_expr "^" and_expr
   or_expr:  xor_expr | or_expr "|" xor_expr

El operador "&" genera el AND bit a bit de sus argumentos, que deben
ser números enteros o uno de ellos debe ser un objeto personalizado
que sobreescriba los métodos especiales "__and__()" o "__rand__()".

El operador "^" genera el XOR bit a bit (OR exclusivo) de sus
argumentos, que deben ser números enteros o uno de ellos debe ser un
objeto personalizado que sobreescriba los métodos especiales
"__xor__()" o "__rxor__()".

El operador "|" genera el OR bit a bit (inclusive) de sus argumentos,
que deben ser números enteros o uno de ellos debe ser un objeto
personalizado que sobreescriba los métodos especiales "__or__()" o
"__ror__()".

## 6.10. Comparaciones

A diferencia de C, todas las operaciones de comparación en Python
tienen la misma prioridad, la cual es menor que la de cualquier
operación aritmética, de desplazamiento o bit a bit. También, a
diferencia de C, expresiones como "a < b < c" tienen la interpretación
convencional en matemáticas:

   comparison:    or_expr (comp_operator or_expr)*
   comp_operator: "<" | ">" | "==" | ">=" | "<=" | "!="
                  | "is" ["not"] | ["not"] "in"

Las comparaciones generan valores booleanos: "True" o "False".: dfn:
los *Métodos de comparación enriquecidos* personalizados pueden
retornar valores no booleanos. En este caso, Python llamará a "bool()"
en dicho valor en contextos booleanos.

Las comparaciones pueden ser encadenadas arbitrariamente, ej., "x < y
<= z" es equivalente a "x < y and y <= z", excepto que "y" es evaluado
sólo una vez (pero en ambos casos "z" no es evaluado para nada cuando
"x < y" se encuentra que es falso).

Formalmente, si *a*, *b*, *c*, ..., *y*, *z* son expresiones y *op1*,
*op2*, ..., *opN* son operadores de comparación, entonces "a op1 b op2
c ... y opN z" es equivalente a "a op1 b and b op2 c and ... y opN z",
excepto que cada expresión es evaluada como mucho una vez.

Tenga en cuenta que "a op1 b op2 c" no implica ningún tipo de
comparación entre *a* y *c*, por lo que, por ejemplo, "x < y > z" es
perfectamente legal (aunque quizás no es bonito).

### 6.10.1. Comparaciones de valor

Los operadores "<", ">", "==", ">=", "<=", y "!=" comparan los valores
de dos objetos. Los objetos no necesitan ser del mismo tipo.

El capítulo Objetos, valores y tipos afirma que los objetos tienen un
valor (en adición al tipo e identidad). El valor de un objeto es una
noción bastante abstracta en Python: Por ejemplo, no existe un método
de acceso canónico para el valor de un objeto. Además, no se requiere
que el valor de un objeto deba ser construido de una forma particular,
ej. compuesto de todos sus atributos de datos. Los operadores de
comparación implementan una noción particular de lo que es el valor de
un objeto. Uno puede pensar en ellos definiendo el valor de un objeto
indirectamente, mediante su implementación de comparación.

Debido a que todos los tipos son subtipos (directos o indirectos) de
"object", ellos heredan el comportamiento de comparación
predeterminado desde "object". Los tipos pueden personalizar su
comportamiento de comparación implementando *rich comparison methods*
como "__lt__()", descritos en Personalización básica.

El comportamiento predeterminado para comparación de igualdad ("==" y
"!=") se basa en la identidad de los objetos. Por lo tanto, la
comparación de instancias con la misma identidad resulta en igualdad,
y la comparación de igualdad de instancias con diferentes entidades
resulta en desigualdad. Una motivación para este comportamiento
predeterminado es el deseo de que todos los objetos sean reflexivos
(ej. "x is y" implica "x == y").

No se provee un orden de comparación por defecto ("<", ">", "<=", and
">="); un intento genera "TypeError". Una motivación para este
comportamiento predeterminado es la falta de una invariante similar
como para la igualdad.

El comportamiento de la comparación de igualdad predeterminado, que
instancias con diferentes identidades siempre son desiguales, puede
estar en contraste a que los tipos que necesitarán que tengan una
definición sensata de valor de objeto e igualdad basada en el valor.
Tales tipos necesitarán personalizar su comportamiento de comparación
y, de hecho, un número de tipos incorporados lo han realizado.

La siguiente lista describe el comportamiento de comparación de los
tipos incorporados más importantes.

* Números de tipos numéricos incorporadas (Tipos numéricos --- int,
  float, complex) y tipos de la biblioteca estándar
  "fractions.Fraction" y "decimal.Decimal" pueden ser comparados
  consigo mismos y entre sus tipos, con la restricción de que números
  complejos no soportan orden de comparación. Dentro de los límites de
  los tipos involucrados, se comparan matemáticamente
  (algorítmicamente) correctos sin pérdida de precisión.

  Los valores no-un-número "float('NaN')" y "decimal.Decimal('NaN')"
  son especiales. Cualquier comparación ordenada de un número a un no-
  un-número es falsa. Una implicación contraintuitiva es que los
  valores no-un-número son son iguales a sí mismos. Por ejemplo, si "x
  = float('NaN')", "3 < x", "x < 3" y "x == x" son todos falso,
  mientras "x != x" es verdadero. Este comportamiento cumple con IEEE
  754.

* "None" y "NotImplemented" son singletons. **PEP 8** recomienda que
  las comparaciones para singletons deben ser realizadas siempre con
  "is" o "is not", nunca los operadores de igualdad.

* Las secuencias binarias (instancias de "bytes" o "bytearray") pueden
  ser comparadas entre sí y con otros tipos. Ellas comparan
  lexicográficamente utilizando los valores numéricos de sus
  elementos.

* Las cadenas de caracteres (instancias de "str") comparan
  lexicográficamente usando los puntos de códigos numéricos Unicode
  (el resultado de la función incorporada "ord()") o sus caracteres.
  [3]

  Las cadenas de caracteres y las secuencias binarias no pueden ser
  comparadas directamente.

* Las secuencias (instancias de "tuple", "list", o "range") pueden ser
  comparadas sólo entre cada uno de sus tipos, con la restricción de
  que los rangos no soportan comparación de orden. Comparación de
  igualdad entre esos tipos resulta en desigualdad y la comparación de
  orden entre esos tipos genera "TypeError".

  Las secuencias comparan lexicográficamente usando comparación de sus
  correspondientes elementos. Los contenedores incorporados asumen que
  los objetos idénticos son iguales a sí mismos. Eso les permite
  omitir las pruebas de igualdad para objetos idénticos para mejorar
  el rendimiento y mantener sus invariantes internos.

  La comparación lexicográfica entre colecciones incorporadas funciona
  de la siguiente forma:

  * Para que dos colecciones sean comparadas iguales, ellas deben ser
    del mismo tipo, tener el mismo largo, y cada para de elementos
    correspondientes deben comparar iguales (por ejemplo, "[1,2] ==
    (1,2)" es falso debido a que el tipo no es el mismo).

  * Las colecciones que soportan comparación de orden son ordenadas
    igual que sus primeros elementos desiguales (por ejemplo, "[1,2,x]
    <= [1,2,y]" tiene el mismo valor que "x <= y"). Si un elemento
    correspondiente no existe, la colección más corta es ordenada
    primero (por ejemplo, "[1,2] < [1,2,3]" es verdadero).

* Las asignaciones (instancias de "dict") se comparan iguales si y
  solo si tienen pares "(key, value)" iguales. La comparación
  equitativa de las claves y los valores impone la reflexividad.

  Comparaciones de orden ("<", ">", "<=", and ">=") generan
  "TypeError".

* Conjuntos (instancias de "set" o "frozenset") pueden ser comparadas
  entre sí y entre sus tipos.

  Ellas definen operadores de comparación de orden con la intención de
  comprobar subconjuntos y superconjuntos. Tales relaciones no definen
  ordenaciones completas (por ejemplo, los dos conjuntos "{1,2}" y
  "{2,3}" no son iguales, ni subconjuntos ni superconjuntos uno de
  otro). Acordemente, los conjuntos no son argumentos apropiados para
  funciones que dependen de ordenación completa (por ejemplo, "min()",
  "max()" y "sorted()" producen resultados indefinidos dados una lista
  de conjuntos como entradas).

  La comparación de conjuntos refuerza la reflexibilidad de sus
  elementos.

* La mayoría de los otros tipos incorporados no tienen métodos de
  comparación implementados, por lo que ellos heredan el
  comportamiento de comparación predeterminado.

Las clases definidas por el usuario que personalizan su comportamiento
de comparación deben seguir algunas reglas de consistencia, si es
posible:

* La comparación de igualdad debe ser reflexiva. En otras palabras,
  los objetos idénticos deben comparar iguales:

     "x is y" implica "x == y"

* La comparación debe ser simétrica. En otras palabras, las siguientes
  expresiones deben tener el mismo resultado:

     "x == y" y "y == x"

     "x != y" y "y != x"

     "x < y" y "y > x"

     "x <= y" y "y >= x"

* La comparación debe ser transitiva. Los siguientes ejemplos (no
  exhaustivos) ilustran esto:

     "x > y and y > z" implica "x > z"

     "x < y and y <= z" implica "x < z"

* La comparación inversa debe resultar en la negación booleana. En
  otras palabras, las siguientes expresiones deben tener el mismo
  resultado:

     "x == y" y "not x != y"

     "x < y" y "not x >= y" (para ordenación completa)

     "x > y" y "not x <= y" (para ordenación completa)

  The last two expressions apply to totally ordered collections (e.g.
  to sequences, but not to sets or mappings). See also the
  "@~functools.total_ordering" decorator.

* La función "hash()" debe ser consistente con la igualdad. Los
  objetos que son iguales deben tener el mismo valor de hash o ser
  marcados como inhashables.

Python no fuerza a cumplir esas reglas de coherencia. De hecho, los
valores no-un-número son u ejemplo para no seguir esas reglas.

### 6.10.2. Operaciones de prueba de membresía

Los operadores "in" y "not in" comprueban membresía. "x in s" evalúa a
"True" si *x* es un miembro de *s* y "False" en caso contrario. "x not
in s" retorna la negación de "x in s". Todas las secuencias
incorporadas y tipos conjuntos soportan esto, así como diccionarios,
para los cuales "in" comprueba si un diccionario tiene una clave dada.
Para tipos contenedores como list, tuple, set, frozenset, dict o
collections.deque, la expresión "x in y" es equivalente a "any(x is e
or x == e for e in y)".

Para los tipos cadenas de caracteres y bytes, "x in y" es "True" si y
sólo si *x* es una subcadena de *y*. Una comprobación equivalente es
"y.find(x) != -1". Las cadenas de caracteres vacías siempre son
consideradas como subcadenas de cualquier otra cadena de caracteres,
por lo que """ in "abc"" retornará "True".

Para clases definidas por el usuario las cuales definen el método
"__contains__()", "x in y" retorna "True" si "y.__contains__(x)"
retorna un valor verdadero y "False" en caso contrario.

Para clases definidas por el usuario las cuales no definen
"__contains__()" pero sí definen "__iter__()", "x in y" es "True" si
algún valor "z", para el cual la expresión "x is z or x == z" es
verdadera, es producido iterando sobre "y". Si una excepción es
generada durante la iteración, es como si "in" hubiera generado esa
excepción.

Por último, se intenta el protocolo de iteración al estilo antiguo: si
una clase define "__getitem__()", "x in y" es "True" si y sólo si hay
un índice entero no negativo *i* tal que "x is y[i] or x == y[i]" y
ningún índice entero menor genera la excepción "IndexError". (Si
cualquier otra excepción es generada, es como si "in" hubiera generado
esa excepción).

El operador "not in" es definido para tener el valor de veracidad
inverso de "in".

### 6.10.3. Comparaciones de identidad

Los operadores "is" y "is not" comprueban la identidad de un objeto.
"x is y" es verdadero si y sólo si *x* e *y* son el mismo objeto. La
identidad de un Objeto se determina usando la función "id()". "x is
not y" produce el valor de veracidad inverso. [4]

## 6.11. Operaciones booleanas

   or_test:  and_test | or_test "or" and_test
   and_test: not_test | and_test "and" not_test
   not_test: comparison | "not" not_test

En el contexto de operaciones booleanas, y también cuando las
declaraciones de flujo de control utilizan expresiones, los siguientes
valores se interpretan como falsos: "False", "None", cero numérico de
todos los tipos y cadenas y contenedores vacíos (incluidas cadenas,
tuplas, listas, diccionarios). , conjuntos y conjuntos congelados).
Todos los demás valores se interpretan como verdaderos. Los objetos
definidos por el usuario pueden personalizar su valor de verdad
proporcionando un método "__bool__()".

El operador "not" produce "True" si su argumento es falso, "False" si
no.

La expresión "x and y" primero evalúa *x*; si *x* es falso, se retorna
su valor; de otra forma, *y* es evaluado y se retorna el valor
resultante.

La expresión "x or y" primero evalúa *x*; si *x* es verdadero, se
retorna su valor; de otra forma, *y* es evaluado y se retorna el valor
resultante.

Tenga en cuenta que ni "and" ni "or" restringen el valor y el tipo que
retornan a "False" y "True", sino retornan el último argumento
evaluado. Esto es útil a veces, ej., si "s" es una cadena de
caracteres que debe ser remplazada por un valor predeterminado si está
vacía, la expresión "s or 'foo'" produce el valor deseado. Debido a
que "not" tiene que crear un nuevo valor, retorna un valor booleano
indiferentemente del tipo de su argumento (por ejemplo, "not 'foo'"
produce "False" en lugar de "''".)

## 6.12. Expresiones de asignación

   assignment_expression: [identifier ":="] expression

Una expresión de asignación (a veces también llamada "expresión con
nombre" o "morsa") asigna un "expression" a un "identifier", al mismo
tiempo que retorna el valor de el "expresión".

Un caso de uso común es cuando se manejan expresiones regulares
coincidentes:

   if matching := pattern.search(data):
       do_something(matching)

O, al procesar un flujo de archivos en fragmentos:

   while chunk := file.read(9000):
       process(chunk)

Las expresiones de asignación deben estar entre paréntesis cuando se
usan como expresiones de sentencia y cuando se usan como
subexpresiones en expresiones de segmentación, condicional, lambda,
argumento de palabra clave y expresiones de comprensión-condicional y
en sentencias "assert", "with" y "assignment". En todos los demás
lugares donde se pueden usar, no se requieren paréntesis, incluidas
las sentencias "if" y "while".

Added in version 3.8: Vea **PEP 572** para más detalles sobre las
expresiones de asignación.

## 6.13. Expresiones condicionales

   conditional_expression: or_test ["if" or_test "else" expression]
   expression:             conditional_expression | lambda_expr

A conditional expression (sometimes called a "ternary operator") is an
alternative to the if-else statement. As it is an expression, it
returns a value and can appear as a sub-expression.

La expresión "x if C else y" primero evalúa la condición, *C* en lugar
de *x*. Si *C* es verdadero, *x* es evaluado y se retorna su valor; en
caso contrario, *y* es evaluado y se retorna su valor.

Vea **PEP 308** para más detalles sobre expresiones condicionales.

## 6.14. Lambdas

   lambda_expr: "lambda" [parameter_list] ":" expression

Las expresiones lambda (a veces denominadas formas lambda) son usadas
para crear funciones anónimas. La expresión "lambda parameters:
expression" produce un objeto de función. El objeto sin nombre se
comporta como un objeto función con:

   def <lambda>(parameters):
       return expression

Vea la sección Definiciones de funciones para la sintaxis de listas de
parámetros. Tenga en cuenta que las funciones creadas con expresiones
lambda no pueden contener sentencias ni anotaciones.

## 6.15. Listas de expresiones

   starred_expression:       "*" or_expr | expression
   flexible_expression:      assignment_expression | starred_expression
   flexible_expression_list: flexible_expression ("," flexible_expression)* [","]
   starred_expression_list:  starred_expression ("," starred_expression)* [","]
   expression_list:          expression ("," expression)* [","]
   yield_list:               expression_list | starred_expression "," [starred_expression_list]

Excepto cuando son parte de un despliegue de lista o conjunto, una
lista de expresión conteniendo al menos una coma produce una tupla. El
largo de la tupla es el número de expresiones en la lista. Las
expresiones son evaluadas de izquierda a derecha.

Un asterisco "*" denota *iterable unpacking*. Su operando deben ser un
*iterable*. El iterable es expandido en una secuencia de elementos,
los cuales son incluidos en la nueva tupla, lista o conjunto en el
lugar del desempaquetado.

Added in version 3.5: Desempaquetado iterable en listas de
expresiones, originalmente propuesto por **PEP 488**.

Added in version 3.11: Cualquier elemento en una lista de expresiones
puede ser destacado. Vea **PEP 646**.

La coma final sólo es requerida para crear una tupla de un único
elemento, como "1,"; es opcional en otros casos. Una única expresión
sin una coma final no crea una tupla, si no genera el valor de esa
expresión. (Para crear una tupla vacía, usa un par de paréntesis
vacío: "()".)

## 6.16. Orden de evaluación

Python evalúa las expresiones de izquierda a derecha. Note que
mientras se evalúa una asignación, la parte derecha es evaluada antes
que la parte izquierda.

En las siguientes líneas, las expresiones serán evaluadas en el orden
aritmético de sus sufijos:

   expr1, expr2, expr3, expr4
   (expr1, expr2, expr3, expr4)
   {expr1: expr2, expr3: expr4}
   expr1 + expr2 * (expr3 - expr4)
   expr1(expr2, expr3, *expr4, **expr5)
   expr3, expr4 = expr1, expr2

## 6.17. Prioridad de operador

La siguiente tabla resume la precedencia de operadores en Python,
desde la precedencia más alta (más vinculante) hasta la precedencia
más baja (menos vinculante). Los operadores en el mismo cuadro tienen
la misma prioridad. A menos que la sintaxis se proporcione
explícitamente, los operadores son binarios. Los operadores en el
mismo cuadro se agrupan de izquierda a derecha (excepto la
exponenciación y las expresiones condicionales, que se agrupan de
derecha a izquierda).

Tenga en cuenta que las comparaciones, comprobaciones de membresía y
las comprobaciones de identidad tienen la misma prioridad y una
característica de encadenado de izquierda a derecha como son descritas
en la sección Comparaciones.

+-------------------------------------------------+---------------------------------------+
| Operador                                        | Descripción                           |
|=================================================|=======================================|
| "(expressions...)",  "[expressions...]", "{key: | Expresión de enlace o entre           |
| value...}", "{expressions...}"                  | paréntesis, despliegues de lista,     |
## |                                                 | diccionario y conjunto                |

| "x[index]", "x[index:index]" "x(arguments...)", | Subscription (including slicing),     |
## | "x.attribute"                                   | call, attribute reference             |

## | "await x"                                       | Expresión await                       |

## | "**"                                            | Exponenciación [5]                    |

## | "+x", "-x", "~x"                                | NOT positivo, negativo, bit a bit     |

| "*", "@", "/", "//", "%"                        | Multiplicación, multiplicación de     |
|                                                 | matrices, división, división entera a |
## |                                                 | la baja, resto (módulo) [6]           |

## | "+", "-"                                        | Adición y sustracción                 |

## | "<<", ">>"                                      | Desplazamientos                       |

## | "&"                                             | AND bit a bit                         |

## | "^"                                             | XOR bit a bit                         |

## | "|"                                             | OR bit a bit                          |

| "in", "not in", "is", "is not", "<", "<=", ">", | Comparaciones, incluyendo             |
| ">=", "!=", "=="                                | comprobaciones de membresía y de      |
## |                                                 | identidad                             |

## | "not x"                                         | Booleano NOT                          |

## | "and"                                           | Booleano AND                          |

## | "or"                                            | Booleano OR                           |

## | "if" -- "else"                                  | Expresión condicional                 |

## | "lambda"                                        | Expresión lambda                      |

## | ":="                                            | Expresión de asignación               |

-[ Notas al pie ]-

[1] Mientras "abs(x%y) < abs(y)" es matemáticamente verdadero, para
    números de punto flotante puede no ser verdadero numéricamente
    debido al redondeo. Por ejemplo, y asumiendo una plataforma en la
    cual un número de punto flotante de Python es un número de doble
    precisión IEEE 754, a fin de que "-1e-100 % 1e100" tenga el mismo
    signo que "1e100", el resultado calculado es "-1e-100 + 1e100", el
    cual es numéricamente exactamente igual a "1e100". La función
    "math.fmod()" retorna un resultado cuyo signo concuerda con el
    signo del primer argumento en su lugar, y por ello retorna
    "-1e-100" en este caso. La aproximación más apropiada depende de
    su aplicación.

[2] Si x está muy cerca de un entero exacto múltiple de y, es posible
    para "x//y" que sea uno mayor que "(x-x%y)//y" debido al redondeo.
    En tales casos, Python retorna el último resultado, a fin de
    preservar que "divmod(x,y)[0] * y + x % y" sea muy cercano a "x".

[3] El estándar Unicode distingue entre *code points* (ej. U+0041) y
    *abstract characters* (ej. "LETRA MAYÚSCULA LATINA A"). Mientras
    la mayoría de caracteres abstractos en Unicode sólo son
    representados usando un punto de código, hay un número de
    caracteres abstractos que pueden adicionalmente ser representados
    usado una secuencia de más de un punto de código. Por ejemplo, el
    caracter abstracto "LETRA MAYÚSCULA C LATINA CON CEDILLA" puede
    ser representado como un único *precomposed character* en la
    posición de código U+00C7, o como una secuencia de un *base
    character* en la posición de código U+0043 (LETRA MAYÚSCULA C
    LATINA), seguida de un *combining character* en la posición de
    código U+0327 (CEDILLA COMBINADA).

    Los operadores de comparación comparan en cadenas de caracteres al
    nivel de puntos de código Unicode. Esto puede ser contraintuitivo
    para humanos. Por ejemplo, ""\u00C7" == "\u0043\u0327"" es
    "False", incluso aunque ambas cadenas presenten el mismo caracter
    abstracto "LETRA MAYÚSCULA C LATINA CON CEDILLA".

    Para comparar cadenas al nivel de caracteres abstractos (esto es,
    de una forma intuitiva para humanos), usa
    "unicodedata.normalize()".

[4] Debido a la recolección automática de basura, listas libres y a la
    naturaleza dinámica de los descriptores, puede notar un
    comportamiento aparentemente inusual en ciertos usos del operador
    "is", como aquellos involucrando comparaciones entre métodos de
    instancia, o constantes. Compruebe su documentación para más
    información.

[5] El operador de potencia "**" vincula con menos fuerza que un
    operador unario aritmético uno bit a bit en su derecha, esto
    significa que "2**-1" is "0.5".

[6] El operador "%" también es usado para formateo de cadenas; aplica
    la misma prioridad.
