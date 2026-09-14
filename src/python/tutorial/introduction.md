---
title: 3. Una introducción informal a Python
source_url: https://docs.python.org/es/3
source_path: tutorial/introduction.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: tutorial
order: 4970
---

# 3. Una introducción informal a Python

En los siguientes ejemplos, la entrada y la salida se distinguen por
la presencia o ausencia de prompts (*>>>* y *...*): para repetir el
ejemplo, escribe todo después del prompt, cuando aparece; las líneas
que no comienzan con un prompt son emitidas desde el intérprete. Ten
en cuenta que en un ejemplo un prompt secundario en una linea en
solitario significa que debes escribir una línea en blanco. Esto se
utiliza para finalizar un comando multilínea.

Muchos de los ejemplos de este manual, incluso aquellos ingresados en
el prompt interactivo, incluyen comentarios. Los comentarios en Python
comienzan con el carácter numeral, "#", y se extienden hasta el final
visible de la línea. Un comentario quizás aparezca al comienzo de la
línea o seguido de espacios en blanco o código, pero no dentro de una
cadena de caracteres. Un carácter numeral dentro de una cadena de
caracteres es sólo un carácter numeral. Ya que los comentarios son
para aclarar código y no son interpretados por Python, pueden omitirse
cuando se escriben los ejemplos.

Algunos ejemplos:

   # this is the first comment
   spam = 1  # and this is the second comment
             # ... and now a third!
   text = "# This is not a comment because it's inside quotes."

## 3.1. Usando Python como una calculadora

Probemos algunos comandos simples de Python. Inicia el intérprete y
espera el prompt primario, ">>>". (No debería tardar mucho.)

### 3.1.1. Números

The interpreter acts as a simple calculator: you can type an
expression into it and it will write the value.  Expression syntax is
straightforward: the operators "+", "-", "*" and "/" can be used to
perform arithmetic; parentheses ("()") can be used for grouping. For
example:

   >>> 2 + 2
   4
   >>> 50 - 5*6
   20
   >>> (50 - 5*6) / 4
   5.0
   >>> 8 / 5  # division always returns a floating-point number
   1.6

Los números enteros (ej. "2", "4", "20") tienen tipo "int", los que
tienen una parte fraccionaria (por ejemplo "5.0", "1.6") tiene el tipo
"float". Vamos a ver más acerca de los tipos numéricos más adelante en
el tutorial.

La división ("/") siempre retorna un número decimal de punto flotante.
Para hacer *floor division* y obtener un número entero como resultado
puede usarse el operador "//"; para calcular el resto puedes usar "%":

   >>> 17 / 3  # classic division returns a float
   5.666666666666667
   >>>
   >>> 17 // 3  # floor division discards the fractional part
   5
   >>> 17 % 3  # the % operator returns the remainder of the division
   2
   >>> 5 * 3 + 2  # floored quotient * divisor + remainder
   17

Con Python, es posible usar el operador "**" para calcular potencias
[1]:

   >>> 5 ** 2  # 5 squared
   25
   >>> 2 ** 7  # 2 to the power of 7
   128

El signo igual ("=") se usa para asignar un valor a una variable.
Después, no se muestra ningún resultado antes del siguiente prompt
interactivo:

   >>> width = 20
   >>> height = 5 * 9
   >>> width * height
   900

Si una variable no está "definida" (no se le ha asignado un valor), al
intentar usarla dará un error:

   >>> n  # try to access an undefined variable
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   NameError: name 'n' is not defined

Hay soporte completo de punto flotante; operadores con operando
mezclados convertirán los enteros a punto flotante:

   >>> 4 * 3.75 - 1
   14.0

En el modo interactivo, la última expresión impresa se asigna a la
variable "_".  Esto significa que cuando se está utilizando Python
como calculadora, es más fácil seguir calculando, por ejemplo:

   >>> tax = 12.5 / 100
   >>> price = 100.50
   >>> price * tax
   12.5625
   >>> price + _
   113.0625
   >>> round(_, 2)
   113.06

Esta variable debe ser tratada como de sólo lectura por el usuario. No
le asignes explícitamente un valor; crearás una variable local
independiente con el mismo nombre enmascarando la variable con el
comportamiento mágico.

Además de "int" y "float", Python admite otros tipos de números, como
"Decimal" y "Fraction". Python también tiene soporte incorporado para
complex numbers, y usa el sufijo "j" o "J" para indicar la parte
imaginaria (por ejemplo, "3+5j").

### 3.1.2. Texto

Python puede manipular texto (representado por el tipo "str", conocido
como "cadenas de caracteres") al igual que números. Esto incluye
caracteres ""!"", palabras ""conejo"", nombres ""París"", oraciones
""¡Te tengo a la vista!"", etc. ""Yay! :)"". Se pueden encerrar en
comillas simples ("'...'") o comillas dobles (""..."") con el mismo
resultado [2].

   >>> 'spam eggs'  # single quotes
   'spam eggs'
   >>> "Paris rabbit got your back :)! Yay!"  # double quotes
   'Paris rabbit got your back :)! Yay!'
   >>> '1975'  # digits and numerals enclosed in quotes are also strings
   '1975'

Para citar una cita, debemos "escapar" la cita precediéndola con "\".
Alternativamente, podemos usar el otro tipo de comillas:

   >>> 'doesn\'t'  # use \' to escape the single quote...
   "doesn't"
   >>> "doesn't"  # ...or use double quotes instead
   "doesn't"
   >>> '"Yes," they said.'
   '"Yes," they said.'
   >>> "\"Yes,\" they said."
   '"Yes," they said.'
   >>> '"Isn\'t," they said.'
   '"Isn\'t," they said.'

En el intérprete de Python, la definición de cadena y la cadena de
salida pueden verse diferentes. La función "print()" produce una
salida más legible, omitiendo las comillas de encuadre e imprimiendo
caracteres escapados y especiales:

   >>> s = 'First line.\nSecond line.'  # \n means newline
   >>> s  # without print(), special characters are included in the string
   'First line.\nSecond line.'
   >>> print(s)  # with print(), special characters are interpreted, so \n produces new line
   First line.
   Second line.

Si no quieres que los caracteres precedidos por "\" se interpreten
como caracteres especiales, puedes usar *cadenas sin formato*
agregando una "r" antes de la primera comilla:

   >>> print('C:\this\name')  # here \t means tab, \n means newline
   C:      his
   ame
   >>> print(r'C:\this\name')  # note the r before the quote
   C:\this\name

Hay un aspecto sutil en las cadenas sin formato: una cadena sin
formato no puede terminar en un número impar de caracteres "\";
consultar en preguntas frequentes para obtener más información y
soluciones.

String literals can span multiple lines.  One way is using triple-
quotes: """"..."""" or "'''...'''".  End-of-line characters are
automatically included in the string, but it's possible to prevent
this by adding a "\" at the end of the line.  In the following
example, the initial newline is not included:

   >>> print("""\
   ... Usage: thingy [OPTIONS]
   ...      -h                        Display this usage message
   ...      -H hostname               Hostname to connect to
   ... """)
   Usage: thingy [OPTIONS]
        -h                        Display this usage message
        -H hostname               Hostname to connect to

   >>>

Las cadenas se pueden concatenar (pegar juntas) con el operador "+" y
se pueden repetir con "*":

   >>> # 3 times 'un', followed by 'ium'
   >>> 3 * 'un' + 'ium'
   'unununium'

Dos o más *cadenas literales* (es decir, las encerradas entre
comillas) una al lado de la otra se concatenan automáticamente.

   >>> 'Py' 'thon'
   'Python'

Esta característica es particularmente útil cuando quieres dividir
cadenas largas:

   >>> text = ('Put several strings within parentheses '
   ...         'to have them joined together.')
   >>> text
   'Put several strings within parentheses to have them joined together.'

Esto solo funciona con dos literales, no con variables ni expresiones:

   >>> prefix = 'Py'
   >>> prefix 'thon'  # can't concatenate a variable and a string literal
     File "<stdin>", line 1
       prefix 'thon'
              ^^^^^^
   SyntaxError: invalid syntax
   >>> ('un' * 3) 'ium'
     File "<stdin>", line 1
       ('un' * 3) 'ium'
                  ^^^^^
   SyntaxError: invalid syntax

Si quieres concatenar variables o una variable y un literal, usa "+":

   >>> prefix + 'thon'
   'Python'

Las cadenas de texto se pueden *indexar* (subíndices), el primer
carácter de la cadena tiene el índice 0. No hay un tipo de dato
diferente para los caracteres; un carácter es simplemente una cadena
de longitud uno:

   >>> word = 'Python'
   >>> word[0]  # character in position 0
   'P'
   >>> word[5]  # character in position 5
   'n'

Los índices también pueden ser números negativos, para empezar a
contar desde la derecha:

   >>> word[-1]  # last character
   'n'
   >>> word[-2]  # second-last character
   'o'
   >>> word[-6]
   'P'

Nótese que -0 es lo mismo que 0, los índice negativos comienzan desde
-1.

Además de los índices, las *rebanadas* (slicing) también están
soportadas. Mientras que la indexación se utiliza para obtener
caracteres individuales, *rebanar* te permite obtener una subcadena:

   >>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
   'Py'
   >>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
   'tho'

Los índices de las rebanadas tienen valores por defecto útiles; el
valor por defecto para el primer índice es cero, el valor por defecto
para el segundo índice es la longitud de la cadena a rebanar.

   >>> word[:2]   # character from the beginning to position 2 (excluded)
   'Py'
   >>> word[4:]   # characters from position 4 (included) to the end
   'on'
   >>> word[-2:]  # characters from the second-last (included) to the end
   'on'

Nótese cómo el inicio siempre se incluye y el final siempre se
excluye. Esto asegura que "s[:i] + s[i:]" siempre sea igual a "s":

   >>> word[:2] + word[2:]
   'Python'
   >>> word[:4] + word[4:]
   'Python'

Una forma de recordar cómo funcionan las rebanadas es pensar que los
índices apuntan *entre* caracteres, con el borde izquierdo del primer
carácter numerado 0. Luego, el punto derecho del último carácter de
una cadena de *n* caracteres tiene un índice *n*, por ejemplo

    +---+---+---+---+---+---+
    | P | y | t | h | o | n |
    +---+---+---+---+---+---+
    0   1   2   3   4   5   6
   -6  -5  -4  -3  -2  -1

La primera fila de números da la posición de los índices 0...6 en la
cadena; La segunda fila da los correspondientes indices negativos. La
rebanada desde *i* hasta *j* consta de todos los caracteres entre los
bordes etiquetados *i* y *j*, respectivamente.

Para índices no negativos, la longitud de la rebanada es la diferencia
de los índices, si ambos están dentro de los límites. Por ejemplo, la
longitud de "word[1:3]" es 2.

Intentar usar un índice que es muy grande resultará en un error:

   >>> word[42]  # the word only has 6 characters
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   IndexError: string index out of range

Sin embargo, los índices de rebanadas fuera de rango se manejan
satisfactoriamente cuando se usan para rebanar:

   >>> word[4:42]
   'on'
   >>> word[42:]
   ''

Las cadenas de Python no se pueden modificar, son *immutable*. Por
eso, asignar a una posición indexada de la cadena resulta en un error:

   >>> word[0] = 'J'
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: 'str' object does not support item assignment
   >>> word[2:] = 'py'
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: 'str' object does not support item assignment

Si necesitas una cadena diferente, deberías crear una nueva:

   >>> 'J' + word[1:]
   'Jython'
   >>> word[:2] + 'py'
   'Pypy'

La función incorporada "len()" retorna la longitud de una cadena:

   >>> s = 'supercalifragilisticexpialidocious'
   >>> len(s)
   34

Ver también:

  Cadenas de caracteres --- str
     Las cadenas de texto son ejemplos de *tipos secuencias* y
     soportan las operaciones comunes para esos tipos.

  Métodos de las cadenas de caracteres
     Las cadenas de texto soportan una gran cantidad de métodos para
     transformaciones básicas y búsqueda.

  f-strings
     Literales de cadena que tienen expresiones embebidas.

  Format string syntax
     Aquí se da información sobre formateo de cadenas de texto con
     "str.format()".

  Formateo de cadenas al estilo *printf*
     Aquí se describen con más detalle las antiguas operaciones para
     formateo utilizadas cuando una cadena de texto está a la
     izquierda del operador "%".

### 3.1.3. Listas

Python tiene varios tipos de datos *compuestos*, utilizados para
agrupar otros valores. El más versátil es la *lista*, la cual puede
ser escrita como una lista de valores separados por coma (ítems) entre
corchetes. Las listas pueden contener ítems de diferentes tipos, pero
usualmente los ítems son del mismo tipo.

   >>> squares = [1, 4, 9, 16, 25]
   >>> squares
   [1, 4, 9, 16, 25]

Al igual que las cadenas (y todas las demás tipos integrados
*sequence*), las listas se pueden indexar y segmentar:

   >>> squares[0]  # indexing returns the item
   1
   >>> squares[-1]
   25
   >>> squares[-3:]  # slicing returns a new list
   [9, 16, 25]

Las listas también admiten operaciones como concatenación:

   >>> squares + [36, 49, 64, 81, 100]
   [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

A diferencia de las cadenas, que son *immutable*, las listas son de
tipo *mutable*, es decir, es posible cambiar su contenido:

   >>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
   >>> 4 ** 3  # the cube of 4 is 64, not 65!
   64
   >>> cubes[3] = 64  # replace the wrong value
   >>> cubes
   [1, 8, 27, 64, 125]

You can also add new items at the end of the list, by using the
"list.append()" *method* (we will see more about methods later):

   >>> cubes.append(216)  # add the cube of 6
   >>> cubes.append(7 ** 3)  # and the cube of 7
   >>> cubes
   [1, 8, 27, 64, 125, 216, 343]

Simple assignment in Python never copies data. When you assign a list
to a variable, the variable refers to the *existing list*. Any changes
you make to the list through one variable will be seen through all
other variables that refer to it.:

   >>> rgb = ["Red", "Green", "Blue"]
   >>> rgba = rgb
   >>> id(rgb) == id(rgba)  # they reference the same object
   True
   >>> rgba.append("Alph")
   >>> rgb
   ["Red", "Green", "Blue", "Alph"]

Todas las operaciones de rebanado retornan una nueva lista que
contiene los elementos pedidos. Esto significa que la siguiente
rebanada retorna una shallow copy de la lista:

   >>> correct_rgba = rgba[:]
   >>> correct_rgba[-1] = "Alpha"
   >>> correct_rgba
   ["Red", "Green", "Blue", "Alpha"]
   >>> rgba
   ["Red", "Green", "Blue", "Alph"]

También es posible asignar a una rebanada, y esto incluso puede
cambiar la longitud de la lista o vaciarla totalmente:

   >>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
   >>> letters
   ['a', 'b', 'c', 'd', 'e', 'f', 'g']
   >>> # replace some values
   >>> letters[2:5] = ['C', 'D', 'E']
   >>> letters
   ['a', 'b', 'C', 'D', 'E', 'f', 'g']
   >>> # now remove them
   >>> letters[2:5] = []
   >>> letters
   ['a', 'b', 'f', 'g']
   >>> # clear the list by replacing all the elements with an empty list
   >>> letters[:] = []
   >>> letters
   []

La función predefinida "len()" también sirve para las listas

   >>> letters = ['a', 'b', 'c', 'd']
   >>> len(letters)
   4

Es posible anidar listas (crear listas que contengan otras listas),
por ejemplo:

   >>> a = ['a', 'b', 'c']
   >>> n = [1, 2, 3]
   >>> x = [a, n]
   >>> x
   [['a', 'b', 'c'], [1, 2, 3]]
   >>> x[0]
   ['a', 'b', 'c']
   >>> x[0][1]
   'b'

## 3.2. Primeros pasos hacia la programación

Of course, we can use Python for more complicated tasks than adding
two and two together.  For instance, we can write an initial sub-
sequence of the Fibonacci series as follows:

   >>> # Fibonacci series:
   >>> # the sum of two elements defines the next
   >>> a, b = 0, 1
   >>> while a < 10:
   ...     print(a)
   ...     a, b = b, a+b
   ...
   0
   1
   1
   2
   3
   5
   8

Este ejemplo introduce varias características nuevas.

* La primera línea contiene una *asignación múltiple*: las variables
  "a" y "b" obtienen simultáneamente los nuevos valores 0 y 1. En la
  última línea esto se usa nuevamente, demostrando que las expresiones
  de la derecha son evaluadas primero antes de que se realice
  cualquiera de las asignaciones. Las expresiones del lado derecho se
  evalúan de izquierda a derecha.

* El bucle "while" se ejecuta mientras la condición (aquí: "a < 10")
  sea verdadera. En Python, como en C, cualquier valor entero que no
  sea cero es verdadero; cero es falso. La condición también puede ser
  una cadena de texto o una lista, de hecho, cualquier secuencia;
  cualquier cosa con una longitud distinta de cero es verdadera, las
  secuencias vacías son falsas. La prueba utilizada en el ejemplo es
  una comparación simple. Los operadores de comparación estándar se
  escriben igual que en C: "<" (menor que), ">" (mayor que), "=="
  (igual a), "<=" (menor que o igual a), ">=" (mayor que o igual a) y
  "!=" (distinto a).

* El cuerpo del bucle está *indentado*: la indentación es la forma que
  usa Python para agrupar declaraciones. En el intérprete interactivo
  debes teclear un tabulador o espacio(s) para cada línea indentada.
  En la práctica vas a preparar entradas más complicadas para Python
  con un editor de texto; todos los editores de texto modernos tienen
  la facilidad de agregar la indentación automáticamente. Cuando se
  ingresa una instrucción compuesta de forma interactiva, se debe
  finalizar con una línea en blanco para indicar que está completa (ya
  que el analizador no puede adivinar cuando tecleaste la última
  línea). Nota que cada línea de un bloque básico debe estar sangrada
  de la misma forma.

* The "print()" function writes the value of the argument(s) it is
  given. It differs from just writing the expression you want to write
  (as we did earlier in the calculator examples) in the way it handles
  multiple arguments, floating-point quantities, and strings.  Strings
  are printed without quotes, and a space is inserted between items,
  so you can format things nicely, like this:

     >>> i = 256*256
     >>> print('The value of i is', i)
     The value of i is 65536

  El parámetro nombrado *end* puede usarse para evitar el salto de
  linea al final de la salida, o terminar la salida con una cadena
  diferente:

     >>> a, b = 0, 1
     >>> while a < 1000:
     ...     print(a, end=',')
     ...     a, b = b, a+b
     ...
     0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,

-[ Notas al pie ]-

[1] Debido a que "**" tiene una prioridad mayor que "-", "-3**2" se
    interpretará como "-(3**2)", por lo tanto dará como resultado
    "-9". Para evitar esto y obtener "9", puedes usar "(-3)**2".

[2] A diferencia de otros lenguajes, caracteres especiales como "\n"
    tienen el mismo significado con simple("'...'") y dobles (""..."")
    comillas. La única diferencia entre las dos es que dentro de las
    comillas simples no existe la necesidad de escapar """ (pero
    tienes que escapar "\'") y viceversa.
