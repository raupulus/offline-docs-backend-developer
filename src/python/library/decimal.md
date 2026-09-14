---
title: '"decimal" --- Decimal fixed-point and floating-point arithmetic'
source_url: https://docs.python.org/es/3
source_path: library/decimal.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2290
---

# "decimal" --- Decimal fixed-point and floating-point arithmetic

**Código fuente:** Lib/decimal.py

======================================================================

The "decimal" module provides support for fast correctly rounded
decimal floating-point arithmetic. It offers several advantages over
the "float" datatype:

* Decimal "is based on a floating-point model which was designed with
  people in mind, and necessarily has a paramount guiding principle --
  computers must provide an arithmetic that works in the same way as
  the arithmetic that people learn at school." -- excerpt from the
  decimal arithmetic specification.

* Los números decimales se pueden representar de forma exacta en coma
  flotante decimal. En cambio, números como "1.1" y "2.2" no tienen
  representaciones exactas en coma flotante binaria. Los usuarios
  finales normalmente no esperaran que "1.1 + 2.2" se muestre como
  "3.3000000000000003", como ocurre al usar la representación binaria
  en coma flotante.

* La exactitud se traslada a la aritmética. En coma flotante decimal,
  "0.1 + 0.1 + 0.1 - 0.3" es exactamente igual a cero. En coma
  flotante binaria, el resultado es "5.5511151231257827e-017". Aunque
  cercanas a cero, las diferencias impiden pruebas de igualdad
  confiables y las diferencias pueden acumularse. Por estas razones,
  se recomienda el uso de decimal en aplicaciones de contabilidad con
  estrictas restricciones de confiabilidad.

* El módulo decimal incorpora una noción de dígitos significativos, de
  modo que "1.30 + 1.20" es "2.50". El cero final se mantiene para
  indicar el número de dígitos significativos. Esta es la
  representación habitual en aplicaciones monetarias. Para la
  multiplicación, el método de "libro escolar" utilizado usa todas las
  cifras de los multiplicandos. Por ejemplo, "1.3 * 1.2" es igual a
  "1.56", mientras que "1.30 * 1.20" es igual a "1.5600".

* A diferencia del punto flotante binario basado en hardware, el
  módulo decimal tiene una precisión modificable por el usuario (por
  defecto es de 28 dígitos decimales) que puede ser tan grande como
  sea necesario para un problema dado:

  >>> from decimal import *
  >>> getcontext().prec = 6
  >>> Decimal(1) / Decimal(7)
  Decimal('0.142857')
  >>> getcontext().prec = 28
  >>> Decimal(1) / Decimal(7)
  Decimal('0.1428571428571428571428571429')

* Tanto la representación en coma flotante binaria como la decimal se
  implementan de acuerdo a estándares publicados. Mientras que el tipo
  incorporado float expone solo una pequeña parte de sus capacidades,
  el módulo decimal expone todos los componentes requeridos del
  estándar. Cuando es necesario, el desarrollador tiene control total
  sobre el redondeo y la gestión de las señales. Esto incluye la
  capacidad de forzar la aritmética exacta, utilizando excepciones
  para bloquear cualquier operación inexacta.

* El módulo decimal fue diseñado para admitir "indiscriminadamente,
  tanto aritmética decimal exacta sin redondeo (a veces llamada
  aritmética de coma fija) como la aritmética de coma flotante con
  redondeo." -- extracto (traducido) de la especificación de la
  aritmética decimal.

El módulo está diseñado en torno a tres conceptos: el número decimal,
el contexto aritmético y las señales.

Un número decimal es inmutable. Tiene un signo, un coeficiente y un
exponente. Para conservar el número de dígitos significativos, los
ceros iniciales no se truncan. Los números decimales también incluyen
valores especiales como "Infinity", "-Infinity" y "NaN". El estándar
también marca la diferencia entre "-0" y "+0".

El contexto aritmético es un entorno que permite especificar una
precisión, reglas de redondeo, límites en los exponentes, flags que
indican el resultado de las operaciones y habilitadores de trampas que
especifican si las señales (reportadas durante operaciones ilegales)
son tratadas o no como excepciones de Python. Las opciones de redondeo
incluyen "ROUND_CEILING", "ROUND_DOWN", "ROUND_FLOOR",
"ROUND_HALF_DOWN", "ROUND_HALF_EVEN", "ROUND_HALF_UP", "ROUND_UP" y
"ROUND_05UP".

Las señales son grupos de condiciones excepcionales que ocurren
durante el cálculo. Dependiendo de las necesidades de la aplicación,
las señales pueden ignorarse, tratarse como información o tratarse
como excepciones. Las señales existentes en el módulo decimal son
"Clamped", "InvalidOperation", "DivisionByZero", "Inexact", "Rounded",
"Subnormal", "Overflow", "Underflow" y "FloatOperation".

Por cada señal hay un flag y un habilitador de trampa. Cuando ocurre
una operación ilegal, su flag se establece en uno, luego, si su
habilitador de trampa está establecido en uno, se lanza una excepción.
La configuración de los flags es persistente, por lo que el usuario
debe restablecerlos antes de comenzar un cálculo que desee monitorear.

Ver también:

  * Especificación general de la aritmética decimal de IBM, The
    General Decimal Arithmetic Specification.

## Quick-start tutorial

El punto de partida habitual para usar decimales es importar el
módulo, ver el contexto actual con "getcontext()" y, si es necesario,
establecer nuevos valores para la precisión, el redondeo o trampas de
señales habilitadas:

   >>> from decimal import *
   >>> getcontext()
   Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999,
           capitals=1, clamp=0, flags=[], traps=[Overflow, DivisionByZero,
           InvalidOperation])

   >>> getcontext().prec = 7       # Set a new precision

Las instancias de la clase Decimal se pueden construir a partir de
números enteros, cadenas de caracteres, flotantes o tuplas. La
construcción a partir de un número entero o flotante realiza una
conversión exacta del valor de ese número. Los números decimales
incluyen valores especiales como "NaN", que significa "No es un
número", "Infinity" positivo y negativo o "-0":

   >>> getcontext().prec = 28
   >>> Decimal(10)
   Decimal('10')
   >>> Decimal('3.14')
   Decimal('3.14')
   >>> Decimal(3.14)
   Decimal('3.140000000000000124344978758017532527446746826171875')
   >>> Decimal((0, (3, 1, 4), -2))
   Decimal('3.14')
   >>> Decimal(str(2.0 ** 0.5))
   Decimal('1.4142135623730951')
   >>> Decimal(2) ** Decimal('0.5')
   Decimal('1.414213562373095048801688724')
   >>> Decimal('NaN')
   Decimal('NaN')
   >>> Decimal('-Infinity')
   Decimal('-Infinity')

Si la señal "FloatOperation" es atrapada, la mezcla accidental de
decimales y flotantes en constructores o comparaciones de orden
lanzará una excepción:

   >>> c = getcontext()
   >>> c.traps[FloatOperation] = True
   >>> Decimal(3.14)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   decimal.FloatOperation: [<class 'decimal.FloatOperation'>]
   >>> Decimal('3.5') < 3.7
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   decimal.FloatOperation: [<class 'decimal.FloatOperation'>]
   >>> Decimal('3.5') == 3.5
   True

Added in version 3.3.

La significación de un nuevo objeto Decimal es determinada únicamente
por el número de dígitos ingresados. La precisión y el redondeo
establecidos en el contexto solo entran en juego durante las
operaciones aritméticas.

   >>> getcontext().prec = 6
   >>> Decimal('3.0')
   Decimal('3.0')
   >>> Decimal('3.1415926535')
   Decimal('3.1415926535')
   >>> Decimal('3.1415926535') + Decimal('2.7182818285')
   Decimal('5.85987')
   >>> getcontext().rounding = ROUND_UP
   >>> Decimal('3.1415926535') + Decimal('2.7182818285')
   Decimal('5.85988')

Se lanza una excepción "InvalidOperation" si durante la construcción
de un objeto Decimal se exceden los límites internos de la versión de
C:

   >>> Decimal("1e9999999999999999999")
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   decimal.InvalidOperation: [<class 'decimal.InvalidOperation'>]

Distinto en la versión 3.3.

Decimals interact well with much of the rest of Python.  Here is a
small decimal floating-point flying circus:

   >>> data = list(map(Decimal, '1.34 1.87 3.45 2.35 1.00 0.03 9.25'.split()))
   >>> max(data)
   Decimal('9.25')
   >>> min(data)
   Decimal('0.03')
   >>> sorted(data)
   [Decimal('0.03'), Decimal('1.00'), Decimal('1.34'), Decimal('1.87'),
    Decimal('2.35'), Decimal('3.45'), Decimal('9.25')]
   >>> sum(data)
   Decimal('19.29')
   >>> a,b,c = data[:3]
   >>> str(a)
   '1.34'
   >>> float(a)
   1.34
   >>> round(a, 1)
   Decimal('1.3')
   >>> int(a)
   1
   >>> a * 5
   Decimal('6.70')
   >>> a * b
   Decimal('2.5058')
   >>> c % a
   Decimal('0.77')

Decimals can be formatted (with "format()" built-in or f-strings) in
fixed-point or scientific notation, using the same formatting syntax
(see Format specification mini-language) as builtin "float" type:

   >>> format(Decimal('2.675'), "f")
   '2.675'
   >>> format(Decimal('2.675'), ".2f")
   '2.68'
   >>> f"{Decimal('2.675'):.2f}"
   '2.68'
   >>> format(Decimal('2.675'), ".2e")
   '2.68e+0'
   >>> with localcontext() as ctx:
   ...     ctx.rounding = ROUND_DOWN
   ...     print(format(Decimal('2.675'), ".2f"))
   ...
   2.67

Y algunas funciones matemáticas también están disponibles para
Decimal:

>>> getcontext().prec = 28
>>> Decimal(2).sqrt()
Decimal('1.414213562373095048801688724')
>>> Decimal(1).exp()
Decimal('2.718281828459045235360287471')
>>> Decimal('10').ln()
Decimal('2.302585092994045684017991455')
>>> Decimal('10').log10()
Decimal('1')

El método "quantize()" redondea un número a un exponente fijo. Este
método es útil para aplicaciones monetarias, que a menudo redondean
los resultados a un número fijo de dígitos significativos:

>>> Decimal('7.325').quantize(Decimal('.01'), rounding=ROUND_DOWN)
Decimal('7.32')
>>> Decimal('7.325').quantize(Decimal('1.'), rounding=ROUND_UP)
Decimal('8')

Como se muestra arriba, la función "getcontext()" accede al contexto
actual y permite cambiar la configuración. Este enfoque satisface las
necesidades de la mayoría de las aplicaciones.

For more advanced work, it may be useful to create alternate contexts
using the "Context()" constructor.  To make an alternate active, use
the "setcontext()" function.

In accordance with the standard, the "decimal" module provides two
ready to use standard contexts, "BasicContext" and "ExtendedContext".
The former is especially useful for debugging because many of the
traps are enabled:

   >>> myothercontext = Context(prec=60, rounding=ROUND_HALF_DOWN)
   >>> setcontext(myothercontext)
   >>> Decimal(1) / Decimal(7)
   Decimal('0.142857142857142857142857142857142857142857142857142857142857')

   >>> ExtendedContext
   Context(prec=9, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999,
           capitals=1, clamp=0, flags=[], traps=[])
   >>> setcontext(ExtendedContext)
   >>> Decimal(1) / Decimal(7)
   Decimal('0.142857143')
   >>> Decimal(42) / Decimal(0)
   Decimal('Infinity')

   >>> setcontext(BasicContext)
   >>> Decimal(42) / Decimal(0)
   Traceback (most recent call last):
     File "<pyshell#143>", line 1, in -toplevel-
       Decimal(42) / Decimal(0)
   DivisionByZero: x / 0

Los objetos Context también tienen flags de señalización para detectar
condiciones excepcionales detectadas durante los cálculos. Estos flags
permanecen habilitados hasta que se restablecen explícitamente. Por
esta razón, suele ser buena idea restablecerlos mediante el método
"clear_flags()" antes de proceder con cada conjunto de cálculos
monitorizados.

   >>> setcontext(ExtendedContext)
   >>> getcontext().clear_flags()
   >>> Decimal(355) / Decimal(113)
   Decimal('3.14159292')
   >>> getcontext()
   Context(prec=9, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999,
           capitals=1, clamp=0, flags=[Inexact, Rounded], traps=[])

La entrada *flags* muestra que la aproximación racional de Pi fue
redondeada (los dígitos más allá de la precisión especificada por el
contexto se descartaron) y que el resultado es inexacto (algunos de
los dígitos descartados no eran cero).

Las trampas de señales se habilitan a través del diccionario expuesto
por el atributo "traps" del objeto Context:

   >>> setcontext(ExtendedContext)
   >>> Decimal(1) / Decimal(0)
   Decimal('Infinity')
   >>> getcontext().traps[DivisionByZero] = 1
   >>> Decimal(1) / Decimal(0)
   Traceback (most recent call last):
     File "<pyshell#112>", line 1, in -toplevel-
       Decimal(1) / Decimal(0)
   DivisionByZero: x / 0

La mayoría de los programas ajustan el contexto actual una sola vez,
al comienzo del programa. Y, en muchas aplicaciones, los datos se
convierten a "Decimal" mediante una única conversión dentro de un
bucle. Con el contexto establecido y los decimales creados, la mayor
parte del programa manipula los datos de la misma forma que con otros
tipos numéricos de Python.

## Objetos Decimal

class decimal.Decimal(value='0', context=None)

   Construye un nuevo objeto "Decimal" basado en *value*.

   *value* puede ser un entero, una cadena de caracteres, una tupla,
   un "float" u otro objeto "Decimal". Si no se proporciona *value*,
   retorna "Decimal('0')". Si *value* es una cadena, debe ajustarse a
   la sintaxis de cadena numérica decimal después de que los espacios
   en blanco iniciales y finales, así como los guiones bajos, sean
   eliminados:

      sign           ::=  '+' | '-'
      digit          ::=  '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
      indicator      ::=  'e' | 'E'
      digits         ::=  digit [digit]...
      decimal-part   ::=  digits '.' [digits] | ['.'] digits
      exponent-part  ::=  indicator [sign] digits
      infinity       ::=  'Infinity' | 'Inf'
      nan            ::=  'NaN' [digits] | 'sNaN' [digits]
      numeric-value  ::=  decimal-part [exponent-part] | infinity
      numeric-string ::=  [sign] numeric-value | [sign] nan

   Other Unicode decimal digits are also permitted where "digit"
   appears above.  These include decimal digits from various other
   alphabets (for example, Arabic-Indic and Devanāgarī digits) along
   with the fullwidth digits "'\uff10'" through "'\uff19'". Case is
   not significant, so, for example, "inf", "Inf", "INFINITY", and
   "iNfINity" are all acceptable spellings for positive infinity.

   Si *value* es un objeto "tuple", debe tener tres componentes, un
   signo ("0" para positivo o "1" para negativo), un objeto "tuple"
   con los dígitos y un exponente entero. Por ejemplo, "Decimal((0,
   (1, 4, 1, 4), -3))" retorna "Decimal('1.414')".

   If *value* is a "float", the binary floating-point value is
   losslessly converted to its exact decimal equivalent.  This
   conversion can often require 53 or more digits of precision.  For
   example, "Decimal(float('1.1'))" converts to
   "Decimal('1.100000000000000088817841970012523233890533447265625')".

   La precisión de *context* no afecta a la cantidad de dígitos
   almacenados. Eso está determinado exclusivamente por el número de
   dígitos en *value*. Por ejemplo, "Decimal('3.00000')" registra los
   cinco ceros incluso si la precisión del contexto es solo tres.

   El propósito del argumento *context* es determinar qué hacer si
   *value* es una cadena de caracteres mal formada. Si el contexto
   atrapa la señal "InvalidOperation", se genera una excepción; de lo
   contrario, el constructor retorna un nuevo decimal con el valor
   "NaN".

   Una vez construidos, los objetos "Decimal" son inmutables.

   Distinto en la versión 3.2: Ahora se permite que el argumento del
   constructor sea una instancia "float".

   Distinto en la versión 3.3: Los argumentos "float" ahora generan
   una excepción si se establece la trampa "FloatOperation". Por
   defecto, la trampa está desactivada.

   Distinto en la versión 3.6: Se permiten guiones bajos para la
   agrupación, como ocurre en el código con los literales enteros y de
   punto flotante.

   Decimal floating-point objects share many properties with the other
   built-in numeric types such as "float" and "int".  All of the usual
   math operations and special methods apply.  Likewise, decimal
   objects can be copied, pickled, printed, used as dictionary keys,
   used as set elements, compared, sorted, and coerced to another type
   (such as "float" or "int").

   Hay algunas pequeñas diferencias entre la aritmética en objetos
   decimales y la aritmética en enteros y flotantes. Cuando el
   operador de resto "%" se aplica a objetos Decimal, el signo del
   resultado es el signo del *dividendo* en lugar del signo del
   divisor:

      >>> (-7) % 4
      1
      >>> Decimal(-7) % Decimal(4)
      Decimal('-3')

   El operador de división entera "//" se comporta de manera análoga,
   retornando la parte entera del cociente verdadero (truncando hacia
   cero) en lugar del resultado de aplicarle la función suelo. Esto se
   hace con la finalidad de preservar la identidad habitual "x == (x
   // y) * y + x % y":

      >>> -7 // 4
      -2
      >>> Decimal(-7) // Decimal(4)
      Decimal('-1')

   Los operadores "%" y "//" implementan las operaciones "remainder" y
   "divide-integer" (respectivamente) como se describe en la
   especificación.

   Los objetos de la clase Decimal generalmente no se pueden combinar
   con flotantes o instancias de "fractions.Fraction" en operaciones
   aritméticas: un intento de agregar un objeto "Decimal" a un
   "float", por ejemplo, lanzará una excepción "TypeError". Sin
   embargo, es posible usar los operadores de comparación de Python
   para comparar una instancia de "Decimal" "x" con otro número "y".
   Esto evita resultados confusos al hacer comparaciones de igualdad
   entre números de diferentes tipos.

   Distinto en la versión 3.2: Las comparaciones de tipo mixto entre
   instancias de "Decimal" y otros tipos numéricos ahora son
   totalmente compatibles.

   In addition to the standard numeric properties, decimal floating-
   point objects also have a number of specialized methods:

   adjusted()

      Retorna el exponente ajustado después de desplazar los dígitos
      del extremo derecho del coeficiente hasta que solo quede el
      dígito principal: "Decimal('321e+5').adjusted()" retorna siete.
      Se utiliza para determinar la posición del dígito más
      significativo con respecto al punto decimal.

   as_integer_ratio()

      Retorna un par de enteros "(n, d)" que representan la instancia
      de "Decimal" proporcionada como una fracción irreducible y con
      un denominador positivo:

         >>> Decimal('-3.14').as_integer_ratio()
         (-157, 50)

      La conversión es exacta. Lanza una excepción OverflowError si se
      proporcionan valores infinitos y ValueError con valores NaN.

   Added in version 3.6.

   as_tuple()

      Retorna una representación en forma de *named tuple* del número:
      "DecimalTuple(sign, digits, exponent)".

   canonical()

      Retorna la codificación canónica del argumento. Actualmente, la
      codificación de una instancia de "Decimal" es siempre canónica,
      por lo que esta operación retorna su argumento sin cambios.

   compare(other, context=None)

      Compara los valores de dos instancias de Decimal. El método
      "compare()" retorna una instancia de Decimal, y si alguno de los
      operandos es un NaN, el resultado es un NaN:

         a or b is a NaN  ==> Decimal('NaN')
         a < b            ==> Decimal('-1')
         a == b           ==> Decimal('0')
         a > b            ==> Decimal('1')

   compare_signal(other, context=None)

      Esta operación es idéntica al método "compare()", excepto que
      todos los valores NaN generan una señal. Es decir, si ninguno de
      los operandos es un NaN señalizador, cualquier operando de NaN
      silencioso se trata como si fuera un NaN señalizador.

   compare_total(other, context=None)

      Compara dos operandos utilizando su representación abstracta en
      lugar de su valor numérico. Similar al método "compare()", pero
      el resultado proporciona un ordenamiento total en las instancias
      de "Decimal". Dos instancias de "Decimal" con el mismo valor
      numérico, pero diferentes representaciones, se comparan como
      desiguales usando este orden:

      >>> Decimal('12.0').compare_total(Decimal('12'))
      Decimal('-1')

      Los NaN silenciosos y señalizadores también se incluyen en el
      ordenamiento total. El resultado de esta función es
      "Decimal('0')" si ambos operandos tienen la misma
      representación, "Decimal('-1')" si el primer operando es menor
      en el orden total que el segundo y "Decimal('1')" si el primer
      operando es mayor en el orden total que el segundo operando.
      Consulta las especificaciones para obtener detalles sobre el
      ordenamiento total.

      Esta operación no se ve afectada por el contexto y es
      silenciosa: no se cambian los flags y no se realiza ningún
      redondeo. Como excepción, la versión de C puede lanzar
      InvalidOperation si el segundo operando no se puede convertir
      exactamente.

   compare_total_mag(other, context=None)

      Compara dos operandos usando su representación abstracta en
      lugar de su valor, como en "compare_total()", pero ignorando el
      signo de cada operando. "x.compare_total_mag(y)" es equivalente
      a "x.copy_abs().compare_total(y.copy_abs())".

      Esta operación no se ve afectada por el contexto y es
      silenciosa: no se cambian los flags y no se realiza ningún
      redondeo. Como excepción, la versión de C puede lanzar
      InvalidOperation si el segundo operando no se puede convertir
      exactamente.

   conjugate()

      Simplemente retorna self (el propio objeto al que pertenece el
      método invocado). Este método existe solo para cumplir con la
      Especificación decimal.

   copy_abs()

      Retorna el valor absoluto del argumento. Esta operación no se ve
      afectada por el contexto y es silenciosa: no se modifican los
      flags y no se realiza ningún redondeo.

   copy_negate()

      Retorna la negación del argumento. Esta operación no se ve
      afectada por el contexto y es silenciosa: no se cambian los
      flags y no se realiza ningún redondeo.

   copy_sign(other, context=None)

      Retorna una copia del primer operando pero con el signo
      establecido para que sea el mismo que el del segundo operando.
      Por ejemplo:

      >>> Decimal('2.3').copy_sign(Decimal('-1.5'))
      Decimal('-2.3')

      Esta operación no se ve afectada por el contexto y es
      silenciosa: no se cambian los flags y no se realiza ningún
      redondeo. Como excepción, la versión de C puede lanzar
      InvalidOperation si el segundo operando no se puede convertir
      exactamente.

   exp(context=None)

      Retorna el valor de la función exponencial (natural) "e**x" en
      el número dado. El resultado es correctamente redondeado
      utilizando el modo de redondeo "ROUND_HALF_EVEN".

      >>> Decimal(1).exp()
      Decimal('2.718281828459045235360287471')
      >>> Decimal(321).exp()
      Decimal('2.561702493119680037517373933E+139')

   classmethod from_float(f, /)

      Constructor alternativo que acepta únicamente instancias de
      "float" o "int".

      Fíjate que "Decimal.from_float(0.1)" no es lo mismo que
      "Decimal('0.1')". Dado que 0.1 no es exactamente representable
      en coma flotante binaria, el valor se almacena como el valor
      representable más cercano, que es "0x1.999999999999ap-4". Ese
      valor equivalente en decimal es
      "0.1000000000000000055511151231257827021181583404541015625".

      Nota:

        Desde Python 3.2 en adelante, una instancia de "Decimal"
        también se puede construir directamente desde una instancia de
        "float".

         >>> Decimal.from_float(0.1)
         Decimal('0.1000000000000000055511151231257827021181583404541015625')
         >>> Decimal.from_float(float('nan'))
         Decimal('NaN')
         >>> Decimal.from_float(float('inf'))
         Decimal('Infinity')
         >>> Decimal.from_float(float('-inf'))
         Decimal('-Infinity')

      Added in version 3.1.

   classmethod from_number(number, /)

      Alternative constructor that only accepts instances of "float",
      "int" or "Decimal", but not strings or tuples.

         >>> Decimal.from_number(314)
         Decimal('314')
         >>> Decimal.from_number(0.1)
         Decimal('0.1000000000000000055511151231257827021181583404541015625')
         >>> Decimal.from_number(Decimal('3.14'))
         Decimal('3.14')

      Added in version 3.14.

   fma(other, third, context=None)

      Fusión de la multiplicación y la suma. Retorna self*other+third
      sin redondeo del producto intermedio self*other.

      >>> Decimal(2).fma(3, 5)
      Decimal('11')

   is_canonical()

      Retorna "True" si el argumento es canónico y "False" en caso
      contrario. Actualmente, una instancia de "Decimal" es siempre
      canónica, por lo que esta operación siempre retorna "True".

   is_finite()

      Retorna "True" si el argumento es un número finito y "False" si
      el argumento es un valor infinito o un NaN.

   is_infinite()

      Retorna "True" si el argumento es un valor infinito positivo o
      negativo y "False" en caso contrario.

   is_nan()

      Retorna "True" si el argumento es un NaN (silencioso o
      señalizador) y "False" en caso contrario.

   is_normal(context=None)

      Retorna "True" si el argumento es un número finito *normal*.
      Retorna "False" si el argumento es cero, subnormal, infinito o
      un NaN.

   is_qnan()

      Retorna "True" si el argumento es un NaN silencioso y "False" en
      caso contrario.

   is_signed()

      Retorna "True" si el argumento tiene signo negativo y "False" en
      caso contrario. Ten en cuenta que tanto los ceros como los NaN
      pueden tener signo.

   is_snan()

      Retorna "True" si el argumento es un NaN señalizador y "False"
      en caso contrario.

   is_subnormal(context=None)

      Retorna "True" si el argumento es subnormal y "False" en caso
      contrario.

   is_zero()

      Retorna "True" si el argumento es un cero (positivo o negativo)
      y "False" en caso contrario.

   ln(context=None)

      Retorna el logaritmo natural (base e) del operando. El resultado
      es correctamente redondeado utilizando el modo de redondeo
      "ROUND_HALF_EVEN".

   log10(context=None)

      Retorna el logaritmo en base diez del operando. El resultado es
      correctamente redondeado utilizando el modo de redondeo
      "ROUND_HALF_EVEN".

   logb(context=None)

      Para un número distinto de cero, retorna el exponente ajustado
      de su operando como una instancia de "Decimal". Si el operando
      es cero, se retorna "Decimal('-Infinity')" y se activa el flag
      "DivisionByZero". Si el operando es infinito, se retorna
      "Decimal('Infinity')".

   logical_and(other, context=None)

      "logic_and()" es una operación lógica que toma dos *operandos
      lógicos* (consultar Operandos lógicos). El resultado es el "and"
      dígito por dígito de los dos operandos.

   logical_invert(context=None)

      "logic_invert()" es una operación lógica. El resultado es la
      inversión dígito a dígito del operando.

   logical_or(other, context=None)

      "logical_or()" es una operación lógica que toma dos *operandos
      lógicos* (consultar Operandos lógicos). El resultado es un "or"
      dígito a dígito de los dos operandos.

   logical_xor(other, context=None)

      "logic_xor()" es una operación lógica que toma dos *operandos
      lógicos* (consultar Operandos lógicos). El resultado es la
      disyunción exclusiva ("exclusive or") dígito a dígito de ambos
      operandos.

   max(other, context=None)

      Como "max(self, other)", excepto que la regla de redondeo del
      contexto se aplica antes de retornar y que los valores "NaN"
      generan una señal o son ignorados (dependiendo del contexto y de
      si son señalizadores o silenciosos).

   max_mag(other, context=None)

      Similar al método "max()", pero la comparación se realiza
      utilizando los valores absolutos de los operandos.

   min(other, context=None)

      Como "min(self, other)", excepto que la regla de redondeo del
      contexto se aplica antes de retornar y que los valores "NaN"
      generan una señal o se ignoran (según el contexto y si son
      señalizadores o no).

   min_mag(other, context=None)

      Similar al método "min()", pero la comparación se realiza
      utilizando los valores absolutos de los operandos.

   next_minus(context=None)

      Retorna el número más grande representable en el contexto
      proporcionado (o en el contexto del hilo actual si no se
      proporciona un contexto) que sea más pequeño que el operando
      proporcionado.

   next_plus(context=None)

      Retorna el número más pequeño representable en el contexto
      proporcionado (o en el contexto del hilo actual si no se
      proporciona ningún contexto) que sea más grande que el operando
      proporcionado.

   next_toward(other, context=None)

      Si los dos operandos no son iguales, retorna el número más
      cercano al primer operando en la dirección del segundo operando.
      Si ambos operandos son numéricamente iguales, retorna una copia
      del primer operando con el signo establecido para que sea el
      mismo que el signo del segundo operando.

   normalize(context=None)

      Usado para producir valores canónicos de una clase de
      equivalencia dentro del contexto actual o del contexto
      especificado.

      Este tiene la misma semántica que el operador unario "+",
      excepto que si el resultado final es finito, entonces se reduce
      a su forma más simple, eliminando todos los ceros finales y
      preservando el signo. Es decir, que mientras que el coeficiente
      sea distinto de cero y múltiplo de 10, el coeficiente se divide
      por 10 y el exponente se incremente por 1. En otro caso (el
      coeficiente es cero), el exponente se establece en 0. En todos
      los casos el signo no se modifica.

      Por ejemplo, "Decimal('32.100')" y "Decimal('0.321000e+2')"
      ambos se normalizan al valor equivalente "Decimal('32.1')".

      Fíjate que el redondeo se aplica *antes* de reducir a la forma
      más simple.

      En las últimas versiones de la especificación, esta operación
      también era conocida como "reduce".

   number_class(context=None)

      Retorna una cadena de caracteres que describe la *class* del
      operando. El valor retornado es una de las siguientes diez
      cadenas de caracteres.

      * ""-Infinity"", que indica que el operando es un infinito
        negativo.

      * ""-Normal"", que indica que el operando es un número normal
        negativo.

      * ""-Subnormal"", que indica que el operando es negativo y
        subnormal.

      * ""-Zero"", que indica que el operando es un cero negativo.

      * ""+Zero"", que indica que el operando es un cero positivo.

      * ""+Subnormal"",que indica que el operando es positivo y
        subnormal.

      * ""+Normal"", que indica que el operando es un número normal
        positivo.

      * ""+Infinity"", que indica que el operando es un infinito
        positivo.

      * ""NaN"", que indica que el operando es un NaN (no es un
        número) silencioso.

      * ""sNaN"", que indica que el operando es un NaN (no es un
        número) señalizador.

   quantize(exp, rounding=None, context=None)

      Retorna un valor igual al primer operando después de ser
      redondeado y de asignarle el exponente del segundo operando.

      >>> Decimal('1.41421356').quantize(Decimal('1.000'))
      Decimal('1.414')

      A diferencia de otras operaciones, se genera una señal
      "InvalidOperation" si la longitud del coeficiente después de la
      operación quantize es mayor que la precisión. Esto garantiza
      que, a menos que exista una condición de error, el exponente
      cuantificado sea siempre igual al del operando de la derecha.

      Además, a diferencia de otras operaciones, quantize nunca genera
      una señal Underflow, incluso si el resultado es subnormal e
      inexacto.

      Si el exponente del segundo operando es mayor que el del
      primero, puede ser necesario redondear. En este caso, el modo de
      redondeo está determinado por el argumento "rounding", si se
      proporciona, o por el argumento "context" en caso contrario. Si
      no se proporciona ninguno de estos dos argumentos, se utiliza el
      modo de redondeo establecido en el contexto del hilo actual.

      Se retorna un error siempre que el exponente resultante sea
      mayor que "Emax" o menor que "Etiny()".

   radix()

      Retorna "Decimal(10)", que es la raíz (base) en la que la clase
      "Decimal" hace toda su aritmética. Este método está incluido
      solo por compatibilidad con la especificación.

   remainder_near(other, context=None)

      Retorna el resto de dividir *self* entre *other*. Esto difiere
      de la operación "self % other", en la que el signo del resto se
      elige para minimizar su valor absoluto. Más precisamente, el
      valor de retorno es "self - n * other", donde "n" es el número
      entero más cercano al valor exacto de "self / other". Si dos
      enteros están igualmente cerca, entonces el valor par es el
      elegido.

      Si el resultado es cero, entonces su signo será el signo de
      *self*.

      >>> Decimal(18).remainder_near(Decimal(10))
      Decimal('-2')
      >>> Decimal(25).remainder_near(Decimal(10))
      Decimal('5')
      >>> Decimal(35).remainder_near(Decimal(10))
      Decimal('-5')

   rotate(other, context=None)

      Retorna el resultado de rotar los dígitos del primer operando en
      una cantidad especificada por el segundo operando. El segundo
      operando debe ser un número entero en el rango comprendido desde
      -precisión hasta precisión. El valor absoluto del segundo
      operando da el número de lugares a rotar. Si el segundo operando
      es positivo, la rotación es hacia la izquierda; de lo contrario,
      la rotación es hacia la derecha. El coeficiente del primer
      operando se rellena con ceros a la izquierda para satisfacer la
      precisión de longitud si es necesario. El signo y el exponente
      del primer operando no se modifican.

   same_quantum(other, context=None)

      Comprueba si self y other tienen el mismo exponente o si ambos
      son "NaN".

      Esta operación no se ve afectada por el contexto y es
      silenciosa: no se cambian los flags y no se realiza ningún
      redondeo. Como excepción, la versión de C puede lanzar
      InvalidOperation si el segundo operando no se puede convertir
      exactamente.

   scaleb(other, context=None)

      Retorna el primer operando con su exponente ajustado por el
      segundo. De manera equivalente, retorna el primer operando
      multiplicado por "10**other". El segundo operando debe ser un
      número entero.

   shift(other, context=None)

      Retorna el resultado de cambiar los dígitos del primer operando
      en una cantidad especificada por el segundo operando. El segundo
      operando debe ser un número entero en el rango comprendido desde
      -precisión hasta precisión. El valor absoluto del segundo
      operando da el número de lugares a desplazar. Si el segundo
      operando es positivo, el desplazamiento es hacia la izquierda;
      de lo contrario, el desplazamiento es hacia la derecha. Los
      dígitos desplazados en el coeficiente son ceros. El signo y el
      exponente del primer operando no se modifican.

   sqrt(context=None)

      Retorna la raíz cuadrada del argumento con precisión total.

   to_eng_string(context=None)

      Convierte a una cadena de caracteres, usando notación de
      ingeniería si se necesita un exponente.

      La notación de ingeniería tiene como exponente un múltiplo de 3.
      Esto puede dejar hasta 3 dígitos a la izquierda del punto
      decimal y puede requerir la adición de uno o dos ceros finales.

      Por ejemplo, este método convierte "Decimal('123E+1')" en
      "Decimal('1.23E+3')".

   to_integral(rounding=None, context=None)

      Idéntico al método "to_integral_value()". El nombre
      "to_integral" se ha mantenido por compatibilidad con versiones
      anteriores.

   to_integral_exact(rounding=None, context=None)

      Redondea al entero más cercano, generando la señal "Inexact" o
      "Rounded", según corresponda, si se produce un redondeo. El modo
      de redondeo está determinado por el parámetro "rounding" si es
      proporcionado, o por el establecido en el "context"
      proporcionado en caso contrario. Si no se proporciona ninguno de
      estos dos parámetros, se utiliza el modo de redondeo establecido
      en el contexto actual.

   to_integral_value(rounding=None, context=None)

      Redondea al entero más cercano sin generar la señal "Inexact" o
      "Rounded". Si se proporciona, se aplica el método de redondeo
      especificado por *rounding*; en caso contrario, se utiliza el
      método de redondeo del *context* proporcionado o el del contexto
      actual.

   Decimal numbers can be rounded using the "round()" function:

   round(number)

   round(number, ndigits)

      If *ndigits* is not given or "None", returns the nearest "int"
      to *number*, rounding ties to even, and ignoring the rounding
      mode of the "Decimal" context.  Raises "OverflowError" if
      *number* is an infinity or "ValueError" if it is a (quiet or
      signaling) NaN.

      If *ndigits* is an "int", the context's rounding mode is
      respected and a "Decimal" representing *number* rounded to the
      nearest multiple of "Decimal('1E-ndigits')" is returned; in this
      case, "round(number, ndigits)" is equivalent to
      "self.quantize(Decimal('1E-ndigits'))".  Returns
      "Decimal('NaN')" if *number* is a quiet NaN.  Raises
      "InvalidOperation" if *number* is an infinity, a signaling NaN,
      or if the length of the coefficient after the quantize operation
      would be greater than the current context's precision.  In other
      words, for the non-corner cases:

      * if *ndigits* is positive, return *number* rounded to *ndigits*
        decimal places;

      * if *ndigits* is zero, return *number* rounded to the nearest
        integer;

      * if *ndigits* is negative, return *number* rounded to the
        nearest multiple of "10**abs(ndigits)".

      For example:

         >>> from decimal import Decimal, getcontext, ROUND_DOWN
         >>> getcontext().rounding = ROUND_DOWN
         >>> round(Decimal('3.75'))     # context rounding ignored
         4
         >>> round(Decimal('3.5'))      # round-ties-to-even
         4
         >>> round(Decimal('3.75'), 0)  # uses the context rounding
         Decimal('3')
         >>> round(Decimal('3.75'), 1)
         Decimal('3.7')
         >>> round(Decimal('3.75'), -1)
         Decimal('0E+1')

### Operandos lógicos

Los métodos "logical_and()", "logical_invert()", "logical_or()", y
"logical_xor()" esperan que sus argumentos sean *operandos lógicos*.
Un *operando lógico* es una instancia de "Decimal" cuyo exponente y
signo son ambos cero, y cuyos dígitos son todos "0" o "1".

## Objetos context

Los contextos son entornos para operaciones aritméticas. Gobiernan la
precisión, establecen reglas para el redondeo, determinan qué señales
se tratan como excepciones y limitan el rango para los exponentes.

Cada hilo tiene su propio contexto actual, al que se accede o se
reemplaza usando las funciones "getcontext()" y "setcontext()"
respectivamente:

decimal.getcontext()

   Retorna el contexto actual del hilo activo.

decimal.setcontext(c, /)

   Establece *c* como contexto actual para el hilo activo.

También puedes usar la declaración "with" y la función
"localcontext()" para cambiar temporalmente el contexto activo.

decimal.localcontext(ctx=None, **kwargs)

   Retorna un gestor de contexto que establecerá el contexto actual
   para el hilo activo en una copia de *ctx* al ingresar en la
   sentencia with y restaurará el contexto anterior al salir de la
   misma. Si no se especifica ningún contexto, se utiliza una copia
   del contexto actual. El argumento *kwargs* se usa para establecer
   los atributos del nuevo contexto.

   Por ejemplo, el siguiente código establece la precisión decimal
   actual en 42 lugares, realiza un cálculo y luego restaura
   automáticamente el contexto anterior:

      from decimal import localcontext

      with localcontext() as ctx:
          ctx.prec = 42   # Perform a high precision calculation
          s = calculate_something()
      s = +s  # Round the final result back to the default precision

   Usando argumentos de palabra clave, el código sería el siguiente:

      from decimal import localcontext

      with localcontext(prec=42) as ctx:
          s = calculate_something()
      s = +s

   Lanza "TypeError" si *kwargs* proporciona un atributo que "Context"
   no soporta. Lanza también "TypeError" o "ValueError" si *kwargs*
   proporciona un valor no válido para un atributo.

   Distinto en la versión 3.11: "localcontext()" ahora admite la
   configuración de atributos de contexto mediante el uso de
   argumentos de palabra clave.

decimal.IEEEContext(bits)

   Return a context object initialized to the proper values for one of
   the IEEE interchange formats.  The argument must be a multiple of
   32 and less than "IEEE_CONTEXT_MAX_BITS".

   Added in version 3.14.

También se pueden crear nuevos contextos utilizando el constructor de
la clase "Context" que se describe a continuación. Además, el módulo
proporciona tres contextos prediseñados:

decimal.BasicContext

   Este es un contexto estándar definido por la Especificación general
   de la aritmética decimal. La precisión se establece en nueve. El
   redondeo se establece en "ROUND_HALF_UP". Se restablecen todos los
   flags. Todas las trampas están habilitadas (las señales son
   tratadas como excepciones) excepto "Inexact", "Rounded" y
   "Subnormal".

   Debido a que la mayoría de las trampas están habilitadas, este
   contexto es especialmente útil para la depuración.

decimal.ExtendedContext

   Este es un contexto estándar definido por la Especificación general
   de la aritmética decimal. La precisión se establece en nueve. El
   redondeo se establece en "ROUND_HALF_EVEN". Se restablecen todos
   los flags. No se habilitan trampas (para que no se generen
   excepciones durante los cálculos).

   Debido a que las trampas están deshabilitadas, este contexto es
   útil para aplicaciones que prefieren tener un valor "NaN" o
   "Infinity" como resultado en lugar de lanzar excepciones. Esto
   permite que una aplicación complete una ejecución en presencia de
   condiciones que, de otra manera, detendrían el programa.

decimal.DefaultContext

   Este contexto es utilizado por el constructor de la clase "Context"
   como un prototipo para nuevos contextos. Cambiar un campo (como la
   precisión) tiene el efecto de cambiar el valor predeterminado para
   los nuevos contextos creados por el constructor de "Context".

   Este contexto es más útil en entornos con múltiples hilos. Cambiar
   uno de los campos antes de que se inicien los hilos tiene el efecto
   de establecer valores predeterminados en todo el sistema. No se
   recomienda cambiar los campos después de que se hayan iniciado los
   hilos, ya que requeriría el uso de mecanismos de sincronización
   para evitar condiciones de carrera entre los hilos.

   En entornos de un solo hilo, es preferible no utilizar este
   contexto en absoluto. En su lugar, simplemente crea contextos
   explícitamente como se describe a continuación.

   Los valores predeterminados son "Context.prec"="28",
   "Context.rounding"="ROUND_HALF_EVEN", y trampas habilitadas para
   "Overflow", "InvalidOperation", y "DivisionByZero".

Además de los tres contextos proporcionados, se pueden crear nuevos
contextos mediante el constructor de la clase "Context".

class decimal.Context(prec=None, rounding=None, Emin=None, Emax=None, capitals=None, clamp=None, flags=None, traps=None)

   Crea un nuevo contexto. Si no se especifica un campo, o es "None",
   los valores predeterminados se copian de "DefaultContext". Si el
   campo *flags* no está especificado, o es "None", se restablecen
   todas los flags.

   prec

      An integer in the range ["1", "MAX_PREC"] that sets the
      precision for arithmetic operations in the context.

   rounding

      One of the constants listed in the section Rounding Modes.

   traps
   flags

      Lists of any signals to be set. Generally, new contexts should
      only set traps and leave the flags clear.

   Emin
   Emax

      Integers specifying the outer limits allowable for exponents.
      *Emin* must be in the range ["MIN_EMIN", "0"], *Emax* in the
      range ["0", "MAX_EMAX"].

   capitals

      Either "0" or "1" (the default). If set to "1", exponents are
      printed with a capital "E"; otherwise, a lowercase "e" is used:
      "Decimal('6.02e+23')".

   clamp

      Either "0" (the default) or "1".  If set to "1", the exponent
      "e" of a "Decimal" instance representable in this context is
      strictly limited to the range "Emin - prec + 1 <= e <= Emax -
      prec + 1". If *clamp* is "0" then a weaker condition holds: the
      adjusted exponent of the "Decimal" instance is at most "Emax".
      When *clamp* is "1", a large normal number will, where possible,
      have its exponent reduced and a corresponding number of zeros
      added to its coefficient, in order to fit the exponent
      constraints; this preserves the value of the number but loses
      information about significant trailing zeros.  For example:

         >>> Context(prec=6, Emax=999, clamp=1).create_decimal('1.23e999')
         Decimal('1.23000E+999')

      Un valor *clamp* de "1" permite la compatibilidad con los
      formatos de intercambio decimal de ancho fijo especificados en
      IEEE 754.

   La clase "Context" define varios métodos de propósito general, así
   como una gran cantidad de métodos para hacer aritmética
   directamente en un contexto dado. Además, para cada uno de los
   métodos de la clase "Decimal" descritos anteriormente (con la
   excepción de los métodos "adjusted()" y "as_tuple()") hay un método
   correspondiente en la clase "Context". Por ejemplo, para una
   instancia de "Context" "C" y una instancia de "Decimal" "x",
   "C.exp(x)" es equivalente a "x.exp(context=C)". Cada método
   "Context" acepta también un entero de Python (una instancia de
   "int") en cualquier lugar donde se acepte una instancia de Decimal.

   clear_flags()

      Restablece todos los flags a "0".

   clear_traps()

      Restablece todas las trampas a "0".

      Added in version 3.3.

   copy()

      Retorna un duplicado del contexto.

   copy_decimal(num, /)

      Retorna una copia de la instancia de Decimal num.

   create_decimal(num='0', /)

      Crea una nueva instancia de Decimal a partir de *num* pero
      usando *self* como contexto. A diferencia del constructor de
      "Decimal", la precisión del contexto, el método de redondeo, los
      flags y las trampas se aplican a la conversión.

      Esto es útil porque las constantes a menudo se proporcionan con
      una precisión mayor que la que necesita la aplicación. Otro
      beneficio es que el redondeo elimina inmediatamente los efectos
      no deseados de los dígitos más allá de la precisión actual. En
      el siguiente ejemplo, usar entradas no redondeadas significa que
      agregar cero a una suma puede cambiar el resultado:

         >>> getcontext().prec = 3
         >>> Decimal('3.4445') + Decimal('1.0023')
         Decimal('4.45')
         >>> Decimal('3.4445') + Decimal(0) + Decimal('1.0023')
         Decimal('4.44')

      Este método implementa la operación to-number de la
      especificación de IBM. Si el argumento es una cadena de
      caracteres, no se permiten espacios en blanco ni guiones bajos,
      ni al principio ni al final.

   create_decimal_from_float(f, /)

      Crea una nueva instancia de Decimal a partir de un flotante *f*,
      pero redondeando usando *self* como contexto. A diferencia del
      método de clase "Decimal.from_float()", la precisión del
      contexto, el método de redondeo, los flags y las trampas se
      aplican a la conversión.

         >>> context = Context(prec=5, rounding=ROUND_DOWN)
         >>> context.create_decimal_from_float(math.pi)
         Decimal('3.1415')
         >>> context = Context(prec=5, traps=[Inexact])
         >>> context.create_decimal_from_float(math.pi)
         Traceback (most recent call last):
             ...
         decimal.Inexact: None

      Added in version 3.1.

   Etiny()

      Retorna un valor igual a "Emin - prec + 1" que es el valor
      mínimo del exponente para resultados subnormales. Cuando ocurre
      un desbordamiento numérico negativo ("underflow"), el exponente
      se establece en "Etiny".

   Etop()

      Retorna un valor igual a "Emax - prec + 1".

   El enfoque habitual para trabajar con decimales es crear instancias
   de la clase "Decimal" y luego aplicar operaciones aritméticas que
   tienen lugar dentro del contexto actual para el hilo activo. Un
   enfoque alternativo es utilizar métodos de contexto para calcular
   dentro de un contexto específico. Los métodos son similares a los
   de la clase "Decimal" y aquí solo se relatan brevemente.

   abs(x, /)

      Retorna el valor absoluto de *x*.

   add(x, y, /)

      Retorna la suma de *x* e *y*.

   canonical(x, /)

      Retorna el mismo objeto Decimal *x*.

   compare(x, y, /)

      Compara *x* e *y* numéricamente.

   compare_signal(x, y, /)

      Compara los valores de los dos operandos numéricamente.

   compare_total(x, y, /)

      Compara los dos operandos utilizando su representación
      abstracta.

   compare_total_mag(x, y, /)

      Compara los dos operandos utilizando su representación
      abstracta, ignorando el signo.

   copy_abs(x, /)

      Retorna una copia de *x* con el signo establecido en 0.

   copy_negate(x, /)

      Retorna una copia de *x* con el signo invertido.

   copy_sign(x, y, /)

      Copia el signo de *y* en *x*.

   divide(x, y, /)

      Retorna *x* dividido entre *y*.

   divide_int(x, y, /)

      Retorna *x* dividido entre *y*, truncando el resultado a un
      número entero.

   divmod(x, y, /)

      Divide dos números y retorna la parte entera del resultado.

   exp(x, /)

      Retorna "e ** x".

   fma(x, y, z, /)

      Retorna *x* multiplicado por *y*, más *z*.

   is_canonical(x, /)

      Retorna "True" si *x* está en forma canónica, en caso contrario
      retorna "False".

   is_finite(x, /)

      Retorna "True" si *x* es un valor finito, en caso contrario
      retorna "False".

   is_infinite(x, /)

      Retorna "True" si *x* es un valor infinito, en caso contrario
      retorna "False".

   is_nan(x, /)

      Retorna "True" si *x* es un valor qNaN o sNaN , en caso
      contrario retorna "False".

   is_normal(x, /)

      Retorna "True" si *x* es un número normal, en caso contrario
      retorna "False".

   is_qnan(x, /)

      Retorna "True" si *x* es un NaN silencioso, en caso contrario
      retorna "False".

   is_signed(x, /)

      Retorna "True" si *x* es un valor negativo, en caso contrario
      retorna "False".

   is_snan(x, /)

      Retorna "True" si *x* es un NaN señalizador, en caso contrario
      retorna "False".

   is_subnormal(x, /)

      Retorna "True" si *x* es un número subnormal, en caso contrario
      retorna "False".

   is_zero(x, /)

      Retorna "True" si *x* es un cero, en caso contrario retorna
      "False".

   ln(x, /)

      Retorna el logaritmo natural (base e) de *x*.

   log10(x, /)

      Retorna el logaritmo en base 10 de *x*.

   logb(x, /)

      Retorna el exponente de la magnitud del MSD ("dígito más
      significativo") del operando.

   logical_and(x, y, /)

      Aplica la operación lógica *and* entre los dígitos de cada
      operando.

   logical_invert(x, /)

      Invierte todos los dígitos en *x*.

   logical_or(x, y, /)

      Aplica la operación lógica *or* entre los dígitos de cada
      operando.

   logical_xor(x, y, /)

      Aplica la operación lógica *xor* entre los dígitos de cada
      operando.

   max(x, y, /)

      Compara dos valores numéricamente y retorna el mayor de ellos.

   max_mag(x, y, /)

      Compara los valores numéricamente ignorando sus signos.

   min(x, y, /)

      Compara dos valores numéricamente y retorna el menor de ellos.

   min_mag(x, y, /)

      Compara los valores numéricamente ignorando sus signos.

   minus(x, /)

      Se corresponde con el operador unario de resta (prefijo) de
      Python.

   multiply(x, y, /)

      Retorna el producto de *x* por *y*.

   next_minus(x, /)

      Retorna el número más grande representable menor que *x*.

   next_plus(x, /)

      Retorna el número más pequeño representable mayor que *x*.

   next_toward(x, y, /)

      Retorna el número más cercano a *x*, en la dirección de *y*.

   normalize(x, /)

      Reduce *x* a su forma más simple.

   number_class(x, /)

      Retorna una cadena de caracteres indicando la clase de *x*.

   plus(x, /)

      Se corresponde con el operador unario de suma (prefijo) de
      Python. Esta operación aplica la precisión y el redondeo
      establecidos en el contexto, por lo que *no* es una operación de
      identidad.

   power(x, y, modulo=None)

      Retorna "x" elevado a la potencia "y", reconduciendo al módulo
      "modulo" si se proporciona.

      Con dos argumentos, calcula "x**y". Si "x" es negativo, entonces
      "y" debe ser un entero. El resultado será inexacto, a menos que
      "y" sea un entero y el resultado sea finito y pueda expresarse
      exactamente con los dígitos de la 'precisión' establecida. Se
      utiliza el modo de redondeo establecido en el contexto. Los
      resultados siempre se redondean correctamente en la versión de
      Python.

      "Decimal(0) ** Decimal(0)" da como resultado "InvalidOperation",
      y si "InvalidOperation" no es atrapada, entonces da como
      resultado "Decimal('NaN')".

      Distinto en la versión 3.3: El módulo C calcula "power()" en
      términos de las funciones "exp()" y "ln()" redondeadas
      correctamente. El resultado está bien definido pero sólo "casi
      siempre correctamente redondeado".

      Con tres argumentos, calcula "(x**y) % modulo". Para la forma de
      tres argumentos, se mantienen las siguientes restricciones sobre
      los argumentos:

      * los tres argumentos deben ser enteros

      * "y" debe ser un valor no negativo

      * al menos uno, "x" o "y" , no debe ser cero

      * "modulo" no debe ser cero y tener como mínimo los dígitos de
        la 'precisión'

      El valor resultante de "Context.power(x, y, modulo)" es igual al
      valor que se obtendría calculando "(x**y) % modulo" con
      precisión ilimitada, la diferencia es que se calcula de manera
      más eficiente . El exponente del resultado es cero,
      independientemente de los exponentes de "x", "y" y  "modulo". El
      resultado siempre es exacto.

   quantize(x, y, /)

      Retorna un valor igual a *x* (redondeado), pero que tiene el
      exponente de *y*.

   radix()

      Simplemente retorna 10, ya que es Decimal, :)

   remainder(x, y, /)

      Retorna el resto de la división entera.

      El signo del resultado, si no es cero, es el mismo que el del
      dividendo original.

   remainder_near(x, y, /)

      Retorna "x - y * n", donde *n* es el número entero más cercano
      al valor exacto de "x / y" (si el resultado es 0, entonces su
      signo será el signo de *x*).

   rotate(x, y, /)

      Retorna una copia de *x* rotada *y* veces.

   same_quantum(x, y, /)

      Retorna "True" si los dos operandos tienen el mismo exponente.

   scaleb(x, y, /)

      Retorna el primer operando después de agregar el segundo valor a
      su exponente.

   shift(x, y, /)

      Retorna una copia de *x* desplazada *y* veces.

   sqrt(x, /)

      Retorna la raíz cuadrada de un número no negativo para la
      precisión del contexto.

   subtract(x, y, /)

      Retorna la diferencia entre *x* e *y*.

   to_eng_string(x, /)

      Convierte a una cadena de caracteres, usando notación de
      ingeniería si se necesita un exponente.

      La notación de ingeniería tiene como exponente un múltiplo de 3.
      Esto puede dejar hasta 3 dígitos a la izquierda del punto
      decimal y puede requerir la adición de uno o dos ceros finales.

   to_integral_exact(x, /)

      Redondea a un entero.

   to_sci_string(x, /)

      Convierte un número en una cadena de caracteres usando notación
      científica.

## Constantes

Las constantes detalladas en esta sección solo son relevantes para el
módulo de C. Se incluyen también en la versión pura de Python por
compatibilidad.

+-----------------------------------+-----------------------+---------------------------------+
|                                   | 32-bit                | 64-bit                          |
|===================================|=======================|=================================|
## | decimal.MAX_PREC                  | "425000000"           | "999999999999999999"            |

## | decimal.MAX_EMAX                  | "425000000"           | "999999999999999999"            |

## | decimal.MIN_EMIN                  | "-425000000"          | "-999999999999999999"           |

## | decimal.MIN_ETINY                 | "-849999999"          | "-1999999999999999997"          |

## | decimal.IEEE_CONTEXT_MAX_BITS     | "256"                 | "512"                           |

decimal.HAVE_THREADS

   El valor es "True". Está obsoleta, debido ha que Python ahora
   siempre tiene soporte para hilos.

   Obsoleto desde la versión 3.9.

decimal.HAVE_CONTEXTVAR

   El valor predeterminado es "True". Si Python se "configura usando
   --without-decimal-contextvar", la versión de C usa un contexto de
   hilos-locales en lugar de un contexto de corrutinas-locales y el
   valor de la constante es "False". Esto es algo más rápido en
   algunos escenarios de contexto anidado.

   Added in version 3.8.3.

## Modos de redondeo

decimal.ROUND_CEILING

   Redondear hacia "Infinity".

decimal.ROUND_DOWN

   Redondear hacia cero.

decimal.ROUND_FLOOR

   Redondear hacia "-Infinity".

decimal.ROUND_HALF_DOWN

   Redondear al valor contiguo más cercano, con empates hacia cero.

decimal.ROUND_HALF_EVEN

   Redondear al valor contiguo más cercano, con empates al entero par
   contiguo.

decimal.ROUND_HALF_UP

   Redondear al valor contiguo más cercano, con empates alejándose de
   cero.

decimal.ROUND_UP

   Redondear alejándose de cero.

decimal.ROUND_05UP

   Si el último dígito después de redondear hacia cero es 0 ó 5,
   redondear alejándose de cero, en caso contrario, redondear hacia
   cero.

## Señales

Las señales representan condiciones que surgen durante el cálculo.
Cada una se corresponde con un solo flag de contexto y un habilitador
de trampas de contexto.

El flag de contexto se establece siempre que se encuentra la
condición. Después del cálculo, los flags pueden comprobarse con fines
informativos (por ejemplo, para determinar si un cálculo fue exacto).
Después de verificar los flags, asegúrate de borrarlos antes de
comenzar con el siguiente cálculo.

Si el habilitador de trampas del contexto está configurado para la
señal, entonces la condición hace que se lance una excepción de
Python. Por ejemplo, si se establece la trampa "DivisionByZero", se
genera una excepción "DivisionByZero" al encontrar la condición.

class decimal.Clamped

   Cambia un exponente para ajustar las restricciones de
   representación.

   Normalmente, la restricción ocurre cuando un exponente cae fuera de
   los límites "Emin" y "Emax" del contexto. Si es posible, el
   exponente se reduce para ajustar agregando ceros al coeficiente.

class decimal.DecimalException

   Clase base para otras señales. Es una subclase de
   "ArithmeticError".

class decimal.DivisionByZero

   Señala la división de un número no infinito entre cero.

   Puede ocurrir en la división, en la división modular o al elevar un
   número a una potencia negativa. Si esta señal no es atrapada, se
   retorna "Infinity" o "-Infinity", con el signo determinado por las
   entradas del cálculo.

class decimal.Inexact

   Indica que se produjo un redondeo y el resultado no es exacto.

   Señala que se descartaron dígitos distintos de cero durante el
   redondeo. Se retorna el resultado redondeado. El flag o la trampa
   de señal se utiliza para detectar cuando los resultados son
   inexactos.

class decimal.InvalidOperation

   Señala que se realizó una operación no válida.

   Indica que se solicitó una operación que no tiene lógica. Si esta
   señal no está atrapada, se retorna "NaN". Las posibles causas
   incluyen:

      Infinity - Infinity
      0 * Infinity
      Infinity / Infinity
      x % 0
      Infinity % x
      sqrt(-x) and x > 0
      0 ** 0
      x ** (non-integer)
      x ** Infinity

class decimal.Overflow

   Desbordamiento numérico.

   Indica que el exponente es mayor que "Context.Emax" después de que
   se haya producido el redondeo. Si no está atrapada, el resultado
   depende del modo de redondeo, ya sea tirando hacia adentro hasta el
   mayor número finito representable o redondeando hacia afuera a
   "Infinity". En cualquier caso, también se activan las señales
   "Inexact" y "Rounded".

class decimal.Rounded

   Se produjo un redondeo, aunque posiblemente no hubo pérdida de
   información.

   Señal lanzada cada vez que el redondeo descarta dígitos; incluso si
   esos dígitos son cero (como al redondear "5.00" a "5.0"). Si no
   está atrapada, se retorna el resultado sin cambios. Esta señal se
   utiliza para detectar la pérdida de dígitos significativos.

class decimal.Subnormal

   El exponente antes del redondeo era menor que "Emin".

   Ocurre cuando el resultado de una operación es subnormal (el
   exponente es demasiado pequeño). Si no está atrapada, se retorna el
   resultado sin cambios.

class decimal.Underflow

   Desbordamiento numérico negativo con resultado redondeado a cero.

   Ocurre cuando un resultado subnormal se lleva a cero mediante
   redondeo. "Inexact" y "Subnormal" también se señalan.

class decimal.FloatOperation

   Habilita una semántica más estricta para mezclar flotantes y
   objetos Decimal.

   Si la señal no está atrapada (predeterminado), se permite mezclar
   flotantes y objetos Decimal en el constructor de "Decimal", en el
   método "create_decimal()" y en todos los operadores de comparación.
   Tanto la conversión como las comparaciones son exactas. Cualquier
   ocurrencia de una operación mixta se registra silenciosamente
   estableciendo "FloatOperation" a los flags del contexto. Las
   conversiones explícitas usando "from_float()" o
   "create_decimal_from_float()" no establecen el flag.

   En caso contrario (la señal está atrapada), solo las comparaciones
   de igualdad y las conversiones explícitas permanecen silenciadas.
   Todas las demás operaciones mixtas lanzan una excepción
   "FloatOperation".

La siguiente tabla resume la jerarquía de señales:

   exceptions.ArithmeticError(exceptions.Exception)
       DecimalException
           Clamped
           DivisionByZero(DecimalException, exceptions.ZeroDivisionError)
           Inexact
               Overflow(Inexact, Rounded)
               Underflow(Inexact, Rounded, Subnormal)
           InvalidOperation
           Rounded
           Subnormal
           FloatOperation(DecimalException, exceptions.TypeError)

## Floating-point notes

### Mitigación del error de redondeo usando mayor precisión

El uso de la coma flotante decimal elimina el error de representación
decimal (haciendo posible representar "0.1" de forma exacta). Sin
embargo, algunas operaciones aún pueden incurrir en errores de
redondeo cuando los dígitos distintos de cero exceden la precisión
fija.

The effects of round-off error can be amplified by the addition or
subtraction of nearly offsetting quantities resulting in loss of
significance.  Knuth provides two instructive examples where rounded
floating-point arithmetic with insufficient precision causes the
breakdown of the associative and distributive properties of addition:

   # Examples from Seminumerical Algorithms, Section 4.2.2.
   >>> from decimal import Decimal, getcontext
   >>> getcontext().prec = 8

   >>> u, v, w = Decimal(11111113), Decimal(-11111111), Decimal('7.51111111')
   >>> (u + v) + w
   Decimal('9.5111111')
   >>> u + (v + w)
   Decimal('10')

   >>> u, v, w = Decimal(20000), Decimal(-6), Decimal('6.0000003')
   >>> (u*v) + (u*w)
   Decimal('0.01')
   >>> u * (v+w)
   Decimal('0.0060000')

The "decimal" module makes it possible to restore the identities by
expanding the precision sufficiently to avoid loss of significance:

   >>> getcontext().prec = 20
   >>> u, v, w = Decimal(11111113), Decimal(-11111111), Decimal('7.51111111')
   >>> (u + v) + w
   Decimal('9.51111111')
   >>> u + (v + w)
   Decimal('9.51111111')
   >>>
   >>> u, v, w = Decimal(20000), Decimal(-6), Decimal('6.0000003')
   >>> (u*v) + (u*w)
   Decimal('0.0060000')
   >>> u * (v+w)
   Decimal('0.0060000')

### Valores especiales

The number system for the "decimal" module provides special values
including "NaN", "sNaN", "-Infinity", "Infinity", and two zeros, "+0"
and "-0".

Los infinitos se pueden construir directamente con
"Decimal('Infinity')". Además, pueden surgir al dividir entre cero
cuando la señal "DivisionByZero" no es interceptada. Asimismo, cuando
la señal "Overflow" no es interceptada, un infinito puede resultar del
redondeo más allá de los límites del mayor número representable.

Los infinitos tienen signo (afín) y se pueden usar en operaciones
aritméticas donde se tratan como números muy grandes e indeterminados.
Por ejemplo, adicionar una constante a infinito resulta en otro
infinito.

Algunas operaciones son indeterminadas y retornan "NaN", o lanzan una
excepción si la señal "InvalidOperation" es atrapada. Por ejemplo,
"0/0" retorna "NaN" que significa "no es un número". Esta variedad de
"NaN" es silenciosa y, una vez creada, fluirá a través de otros
cálculos dando siempre como resultado otro "NaN". Este comportamiento
puede ser útil para una serie de cálculos a los que ocasionalmente les
faltan entradas, permitiendo que el cálculo continúe mientras se
marcan resultados específicos como no válidos.

Una variante es "sNaN", que emite una señal en lugar de permanecer en
silencio después de cada operación. Este es un valor de retorno útil
cuando un resultado no válido requiere interrumpir un cálculo para un
manejo especial.

El comportamiento de los operadores de comparación de Python puede ser
un poco sorprendente cuando está involucrado un valor "NaN". Una
prueba de igualdad donde uno de los operandos es un "NaN" silencioso o
señalizador siempre retorna "False`" (incluso cuando se hace
"Decimal('NaN')==Decimal('NaN')"), mientras que una prueba de
desigualdad siempre retorna "True". Un intento de comparar dos objetos
Decimal usando cualquiera de los operadores "<", "<=", ">" o ">="
lanzará la señal "InvalidOperation" si alguno de los operandos es
"NaN", y retornará "False" si esta señal no es capturada. Ten en
cuenta que la Especificación General de la Aritmética Decimal no
especifica el comportamiento de las comparaciones directas. Estas
reglas para las comparaciones que involucran a "NaN" se tomaron del
estándar IEEE 854 (consulta la Tabla 3 en la sección 5.7). Utiliza en
su lugar los métodos "compare()" y "compare_signal()" para garantizar
el cumplimiento estricto de los estándares.

Los ceros con signo pueden resultar de cálculos que desbordan la
precisión establecida. Mantienen el signo que habría resultado si el
cálculo se hubiera realizado con mayor precisión. Dado que su magnitud
es cero, los ceros positivos y negativos se tratan como iguales y su
signo es solo informativo.

In addition to the two signed zeros which are distinct yet equal,
there are various representations of zero with differing precisions
yet equivalent in value.  This takes a bit of getting used to.  For an
eye accustomed to normalized floating-point representations, it is not
immediately obvious that the following calculation returns a value
equal to zero:

>>> 1 / Decimal('Infinity')
Decimal('0E-1000026')

## Trabajando con hilos

La función "getcontext()" accede a un objeto "Context" diferente para
cada hilo. Tener contextos de hilo separados significa que los hilos
pueden realizar cambios (como "getcontext().prec=10") sin interferir
con otros hilos.

Asimismo, la función "setcontext()" asigna automáticamente su objetivo
al hilo actual.

If "setcontext()" has not been called before "getcontext()", then
"getcontext()" will automatically create a new context for use in the
current thread.  New context objects have default values set from the
"decimal.DefaultContext" object.

The "sys.flags.thread_inherit_context" flag affects the context for
new threads.  If the flag is false, new threads will start with an
empty context.  In this case, "getcontext()" will create a new context
object when called and use the default values from *DefaultContext*.
If the flag is true, new threads will start with a copy of context
from the caller of "threading.Thread.start()".

To control the defaults so that each thread will use the same values
throughout the application, directly modify the *DefaultContext*
object. This should be done *before* any threads are started so that
there won't be a race condition between threads calling
"getcontext()". For example:

   # Set applicationwide defaults for all threads about to be launched
   DefaultContext.prec = 12
   DefaultContext.rounding = ROUND_DOWN
   DefaultContext.traps = ExtendedContext.traps.copy()
   DefaultContext.traps[InvalidOperation] = 1
   setcontext(DefaultContext)

   # Afterwards, the threads can be started
   t1.start()
   t2.start()
   t3.start()
    . . .

## Casos prácticos

A continuación hay algunos casos prácticos que sirven como funciones
de utilidad y que muestran formas de trabajar con la clase "Decimal":

   def moneyfmt(value, places=2, curr='', sep=',', dp='.',
                pos='', neg='-', trailneg=''):
       """Convert Decimal to a money formatted string.

       places:  required number of places after the decimal point
       curr:    optional currency symbol before the sign (may be blank)
       sep:     optional grouping separator (comma, period, space, or blank)
       dp:      decimal point indicator (comma or period)
                only specify as blank when places is zero
       pos:     optional sign for positive numbers: '+', space or blank
       neg:     optional sign for negative numbers: '-', '(', space or blank
       trailneg:optional trailing minus indicator:  '-', ')', space or blank

       >>> d = Decimal('-1234567.8901')
       >>> moneyfmt(d, curr='$')
       '-$1,234,567.89'
       >>> moneyfmt(d, places=0, sep='.', dp='', neg='', trailneg='-')
       '1.234.568-'
       >>> moneyfmt(d, curr='$', neg='(', trailneg=')')
       '($1,234,567.89)'
       >>> moneyfmt(Decimal(123456789), sep=' ')
       '123 456 789.00'
       >>> moneyfmt(Decimal('-0.02'), neg='<', trailneg='>')
       '<0.02>'

       """
       q = Decimal(10) ** -places      # 2 places --> '0.01'
       sign, digits, exp = value.quantize(q).as_tuple()
       result = []
       digits = list(map(str, digits))
       build, next = result.append, digits.pop
       if sign:
           build(trailneg)
       for i in range(places):
           build(next() if digits else '0')
       if places:
           build(dp)
       if not digits:
           build('0')
       i = 0
       while digits:
           build(next())
           i += 1
           if i == 3 and digits:
               i = 0
               build(sep)
       build(curr)
       build(neg if sign else pos)
       return ''.join(reversed(result))

   def pi():
       """Compute Pi to the current precision.

       >>> print(pi())
       3.141592653589793238462643383

       """
       getcontext().prec += 2  # extra digits for intermediate steps
       three = Decimal(3)      # substitute "three=3.0" for regular floats
       lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
       while s != lasts:
           lasts = s
           n, na = n+na, na+8
           d, da = d+da, da+32
           t = (t * n) / d
           s += t
       getcontext().prec -= 2
       return +s               # unary plus applies the new precision

   def exp(x):
       """Return e raised to the power of x.  Result type matches input type.

       >>> print(exp(Decimal(1)))
       2.718281828459045235360287471
       >>> print(exp(Decimal(2)))
       7.389056098930650227230427461
       >>> print(exp(2.0))
       7.38905609893
       >>> print(exp(2+0j))
       (7.38905609893+0j)

       """
       getcontext().prec += 2
       i, lasts, s, fact, num = 0, 0, 1, 1, 1
       while s != lasts:
           lasts = s
           i += 1
           fact *= i
           num *= x
           s += num / fact
       getcontext().prec -= 2
       return +s

   def cos(x):
       """Return the cosine of x as measured in radians.

       The Taylor series approximation works best for a small value of x.
       For larger values, first compute x = x % (2 * pi).

       >>> print(cos(Decimal('0.5')))
       0.8775825618903727161162815826
       >>> print(cos(0.5))
       0.87758256189
       >>> print(cos(0.5+0j))
       (0.87758256189+0j)

       """
       getcontext().prec += 2
       i, lasts, s, fact, num, sign = 0, 0, 1, 1, 1, 1
       while s != lasts:
           lasts = s
           i += 2
           fact *= i * (i-1)
           num *= x * x
           sign *= -1
           s += num / fact * sign
       getcontext().prec -= 2
       return +s

   def sin(x):
       """Return the sine of x as measured in radians.

       The Taylor series approximation works best for a small value of x.
       For larger values, first compute x = x % (2 * pi).

       >>> print(sin(Decimal('0.5')))
       0.4794255386042030002732879352
       >>> print(sin(0.5))
       0.479425538604
       >>> print(sin(0.5+0j))
       (0.479425538604+0j)

       """
       getcontext().prec += 2
       i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
       while s != lasts:
           lasts = s
           i += 2
           fact *= i * (i-1)
           num *= x * x
           sign *= -1
           s += num / fact * sign
       getcontext().prec -= 2
       return +s

## Preguntas frecuentes sobre decimal

Q: It is cumbersome to type "decimal.Decimal('1234.5')".  Is there a
way to minimize typing when using the interactive interpreter?

A: Some users abbreviate the constructor to just a single letter:

>>> D = decimal.Decimal
>>> D('1.23') + D('3.45')
Decimal('4.68')

Q: In a fixed-point application with two decimal places, some inputs
have many places and need to be rounded.  Others are not supposed to
have excess digits and need to be validated.  What methods should be
used?

A: The "quantize()" method rounds to a fixed number of decimal places.
If the "Inexact" trap is set, it is also useful for validation:

>>> TWOPLACES = Decimal(10) ** -2       # same as Decimal('0.01')

>>> # Round to two places
>>> Decimal('3.214').quantize(TWOPLACES)
Decimal('3.21')

>>> # Validate that a number does not exceed two places
>>> Decimal('3.21').quantize(TWOPLACES, context=Context(traps=[Inexact]))
Decimal('3.21')

>>> Decimal('3.214').quantize(TWOPLACES, context=Context(traps=[Inexact]))
Traceback (most recent call last):
   ...
Inexact: None

Q: Once I have valid two place inputs, how do I maintain that
invariant throughout an application?

A: Some operations like addition, subtraction, and multiplication by
an integer will automatically preserve fixed point.  Others
operations, like division and non-integer multiplication, will change
the number of decimal places and need to be followed-up with a
"quantize()" step:

>>> a = Decimal('102.72')           # Initial fixed-point values
>>> b = Decimal('3.17')
>>> a + b                           # Addition preserves fixed-point
Decimal('105.89')
>>> a - b
Decimal('99.55')
>>> a * 42                          # So does integer multiplication
Decimal('4314.24')
>>> (a * b).quantize(TWOPLACES)     # Must quantize non-integer multiplication
Decimal('325.62')
>>> (b / a).quantize(TWOPLACES)     # And quantize division
Decimal('0.03')

Al desarrollar aplicaciones de coma fija, es conveniente definir
funciones para gestionar el paso "quantize()":

>>> def mul(x, y, fp=TWOPLACES):
...     return (x * y).quantize(fp)
...
>>> def div(x, y, fp=TWOPLACES):
...     return (x / y).quantize(fp)

>>> mul(a, b)                       # Automatically preserve fixed-point
Decimal('325.62')
>>> div(b, a)
Decimal('0.03')

Q: There are many ways to express the same value.  The numbers "200",
"200.000", "2E2", and ".02E+4" all have the same value at various
precisions. Is there a way to transform them to a single recognizable
canonical value?

A: The "normalize()" method maps all equivalent values to a single
representative:

>>> values = map(Decimal, '200 200.000 2E2 .02E+4'.split())
>>> [v.normalize() for v in values]
[Decimal('2E+2'), Decimal('2E+2'), Decimal('2E+2'), Decimal('2E+2')]

Q: When does rounding occur in a computation?

A: It occurs *after* the computation.  The philosophy of the decimal
specification is that numbers are considered exact and are created
independent of the current context.  They can even have greater
precision than current context.  Computations process with those exact
inputs and then rounding (or other context operations) is applied to
the *result* of the computation:

   >>> getcontext().prec = 5
   >>> pi = Decimal('3.1415926535')   # More than 5 digits
   >>> pi                             # All digits are retained
   Decimal('3.1415926535')
   >>> pi + 0                         # Rounded after an addition
   Decimal('3.1416')
   >>> pi - Decimal('0.00005')        # Subtract unrounded numbers, then round
   Decimal('3.1415')
   >>> pi + 0 - Decimal('0.00005').   # Intermediate values are rounded
   Decimal('3.1416')

Q: Some decimal values always print with exponential notation.  Is
there a way to get a non-exponential representation?

A: For some values, exponential notation is the only way to express
the number of significant places in the coefficient.  For example,
expressing "5.0E+3" as "5000" keeps the value constant but cannot show
the original's two-place significance.

Si una aplicación no necesita preocuparse por el seguimiento de
significación, es fácil eliminar el exponente y los ceros finales,
perdiendo significación, pero manteniendo el valor sin cambios:

>>> def remove_exponent(d):
...     return d.quantize(Decimal(1)) if d == d.to_integral() else d.normalize()

>>> remove_exponent(Decimal('5E+3'))
Decimal('5000')

Q: Is there a way to convert a regular float to a "Decimal"?

A: Yes, any binary floating-point number can be exactly expressed as a
Decimal though an exact conversion may take more precision than
intuition would suggest:

   >>> Decimal(math.pi)
   Decimal('3.141592653589793115997963468544185161590576171875')

Q: Within a complex calculation, how can I make sure that I haven't
gotten a spurious result because of insufficient precision or rounding
anomalies.

A: The decimal module makes it easy to test results.  A best practice
is to re-run calculations using greater precision and with various
rounding modes. Widely differing results indicate insufficient
precision, rounding mode issues, ill-conditioned inputs, or a
numerically unstable algorithm.

Q: I noticed that context precision is applied to the results of
operations but not to the inputs.  Is there anything to watch out for
when mixing values of different precisions?

A: Yes.  The principle is that all values are considered to be exact
and so is the arithmetic on those values.  Only the results are
rounded.  The advantage for inputs is that "what you type is what you
get".  A disadvantage is that the results can look odd if you forget
that the inputs haven't been rounded:

   >>> getcontext().prec = 3
   >>> Decimal('3.104') + Decimal('2.104')
   Decimal('5.21')
   >>> Decimal('3.104') + Decimal('0.000') + Decimal('2.104')
   Decimal('5.20')

La solución es aumentar la precisión o forzar el redondeo de las
entradas utilizando la operación unaria más:

   >>> getcontext().prec = 3
   >>> +Decimal('1.23456789')      # unary plus triggers rounding
   Decimal('1.23')

Alternativamente, las entradas se pueden redondear en el momento que
se crean usando el método "Context.create_decimal()":

>>> Context(prec=5, rounding=ROUND_DOWN).create_decimal('1.2345678')
Decimal('1.2345')

Q: Is the CPython implementation fast for large numbers?

A: Yes.  In the CPython and PyPy3 implementations, the C/CFFI versions
of the decimal module integrate the high speed libmpdec library for
arbitrary precision correctly rounded decimal floating-point
arithmetic [1]. "libmpdec" uses Karatsuba multiplication for medium-
sized numbers and the Number Theoretic Transform for very large
numbers.

El contexto debe adaptarse para una aritmética de precisión arbitraria
exacta. "Emin" y "Emax" siempre deben establecerse en sus valores
máximos, "clamp" siempre debe ser 0 (el valor predeterminado).
Establecer "prec" requiere cierto cuidado.

El enfoque más fácil para probar la aritmética bignum es usar también
el valor máximo para "prec" [2]:

   >>> setcontext(Context(prec=MAX_PREC, Emax=MAX_EMAX, Emin=MIN_EMIN))
   >>> x = Decimal(2) ** 256
   >>> x / 128
   Decimal('904625697166532776746648320380374280103671755200316906558262375061821325312')

For inexact results, "MAX_PREC" is far too large on 64-bit platforms
and the available memory will be insufficient:

   >>> Decimal(1) / 3
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   MemoryError

En sistemas con sobreasignación (por ejemplo, Linux), un enfoque más
sofisticado es establecer "prec" a la cantidad de RAM disponible.
Supongamos que tenemos 8GB de RAM y esperamos 10 operandos simultáneos
usando un máximo de 500 MB cada uno:

   >>> import sys
   >>>
   >>> # Maximum number of digits for a single operand using 500MB in 8-byte words
   >>> # with 19 digits per word (4-byte and 9 digits for the 32-bit build):
   >>> maxdigits = 19 * ((500 * 1024**2) // 8)
   >>>
   >>> # Check that this works:
   >>> c = Context(prec=maxdigits, Emax=MAX_EMAX, Emin=MIN_EMIN)
   >>> c.traps[Inexact] = True
   >>> setcontext(c)
   >>>
   >>> # Fill the available precision with nines:
   >>> x = Decimal(0).logical_invert() * 9
   >>> sys.getsizeof(x)
   524288112
   >>> x + 2
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     decimal.Inexact: [<class 'decimal.Inexact'>]

En general (y especialmente en sistemas sin sobreasignación), se
recomienda estimar límites aún más estrictos y establecer la trampa
"Inexact" si se espera que todos los cálculos sean exactos.

[1] Added in version 3.3.

[2] Distinto en la versión 3.9: Este enfoque ahora funciona para todos
    los resultados exactos excepto para las potencias no enteras.
    También retro-portado a 3.7 y 3.8.
