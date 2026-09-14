---
title: '15. Floating-Point Arithmetic:  Issues and Limitations'
source_url: https://docs.python.org/es/3
source_path: tutorial/floatingpoint.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: tutorial
order: 4920
---

# 15. Floating-Point Arithmetic:  Issues and Limitations

Los números de punto flotante se representan en el hardware de
computadoras como fracciones en base 2 (binarias). Por ejemplo, la
fracción **decimal** "0.625" tiene un valor de 6/10 + 2/100 + 5/1000,
y de la misma manera, la fracción binaria "0.101" tiene un valor de
1/2 + 0/4 + 1/8. Estas dos fracciones tienen valores idénticos; la
única diferencia real radica en que la primera se escribe en notación
fraccional en base 10, y la segunda en base 2.

Desafortunadamente, la mayoría de las fracciones decimales no pueden
representarse exactamente como fracciones binarias.  Como
consecuencia, en general los números de punto flotante decimal que
ingresás en la computadora son sólo aproximados por los números de
punto flotante binario que realmente se guardan en la máquina.

El problema es más fácil de entender primero en base 10.  Considerá la
fracción 1/3.  Podés aproximarla como una fracción de base 10

   0.3

...o, mejor,

   0.33

...o, mejor,

   0.333

...y así.  No importa cuantos dígitos desees escribir, el resultado
nunca será exactamente 1/3, pero será una aproximación cada vez mejor
de 1/3.

De la misma manera, no importa cuantos dígitos en base 2 quieras usar,
el valor decimal 0.1 no puede representarse exactamente como una
fracción en base 2.  En base 2, 1/10 es la siguiente fracción que se
repite infinitamente:

   0.0001100110011001100110011001100110011001100110011...

Frená en cualquier número finito de bits, y tendrás una aproximación.
En la mayoría de las máquinas hoy en día, los float se aproximan
usando una fracción binaria con el numerador usando los primeros 53
bits con el bit más significativos y el denominador como una potencia
de dos.  En el caso de 1/10, la fracción binaria es "3602879701896397
/ 2 ** 55" que está cerca pero no es exactamente el valor verdadero de
1/10.

La mayoría de los usuarios no son conscientes de esta aproximación por
la forma en que se muestran los valores. Python solamente muestra una
aproximación decimal al valor verdadero decimal de la aproximación
binaria almacenada por la máquina. En la mayoría de las máquinas, si
Python fuera a imprimir el verdadero valor decimal de la aproximación
binaria almacenada para 0.1, debería mostrar:

   >>> 0.1
   0.1000000000000000055511151231257827021181583404541015625

Esos son más dígitos que lo que la mayoría de la gente encuentra útil,
por lo que Python mantiene manejable la cantidad de dígitos al mostrar
un valor redondeado en su lugar:

   >>> 1 / 10
   0.1

Sólo recordá que, a pesar de que el valor mostrado resulta ser
exactamente 1/10, el valor almacenado realmente es la fracción binaria
más cercana posible.

Interesantemente, hay varios números decimales que comparten la misma
fracción binaria más aproximada. Por ejemplo, los números "0.1",
"0.10000000000000001" y
"0.1000000000000000055511151231257827021181583404541015625" son todos
aproximados por "3602879701896397 / 2 ** 55".  Ya que todos estos
valores decimales comparten la misma aproximación, se podría mostrar
cualquiera de ellos para preservar el invariante "eval(repr(x)) == x".

Históricamente, el prompt de Python y la función integrada "repr()"
eligieron el valor con los 17 dígitos, "0.10000000000000001".  Desde
Python 3.1, en la mayoría de los sistemas Python ahora es capaz de
elegir la forma más corta de ellos y mostrar "0.1".

Note that this is in the very nature of binary floating point: this is
not a bug in Python, and it is not a bug in your code either.  You'll
see the same kind of thing in all languages that support your
hardware's floating-point arithmetic (although some languages may not
*display* the difference by default, or in all output modes).

Para una salida más elegante, quizás quieras usar el formateo de
cadenas de texto para generar un número limitado de dígitos
significativos:

   >>> format(math.pi, '.12g')  # give 12 significant digits
   '3.14159265359'

   >>> format(math.pi, '.2f')   # give 2 digits after the point
   '3.14'

   >>> repr(math.pi)
   '3.141592653589793'

Es importante darse cuenta que esto es, realmente, una ilusión: estás
simplemente redondeando al *mostrar* el valor verdadero de la máquina.

Una ilusión puede generar otra. Por ejemplo, ya que 0.1 no es
exactamente 1/10, sumar tres veces 0.1 podría también no generar
exactamente 0.3:

   >>> 0.1 + 0.1 + 0.1 == 0.3
   False

También, ya que 0.1 no puede acercarse más al valor exacto de 1/10 y
0.3 no puede acercarse más al valor exacto de 3/10, redondear primero
con la función "round()" no puede ayudar:

   >>> round(0.1, 1) + round(0.1, 1) + round(0.1, 1) == round(0.3, 1)
   False

Aunque los números no pueden acercarse más a sus valores exactos
previstos, la función "math.isclose()" puede ser útil para comparar
valores inexactos:

   >>> math.isclose(0.1 + 0.1 + 0.1, 0.3)
   True

Alternatively, the "round()" function can be used to compare rough
approximations:

   >>> round(math.pi, ndigits=2) == round(22 / 7, ndigits=2)
   True

Binary floating-point arithmetic holds many surprises like this.  The
problem with "0.1" is explained in precise detail below, in the
"Representation Error" section.  See Examples of Floating Point
Problems for a pleasant summary of how binary floating point works and
the kinds of problems commonly encountered in practice.  Also see The
Perils of Floating Point for a more complete account of other common
surprises.

As that says near the end, "there are no easy answers."  Still, don't
be unduly wary of floating point!  The errors in Python float
operations are inherited from the floating-point hardware, and on most
machines are on the order of no more than 1 part in 2**53 per
operation.  That's more than adequate for most tasks, but you do need
to keep in mind that it's not decimal arithmetic and that every float
operation can suffer a new rounding error.

A pesar de que existen casos patológicos, para la mayoría de usos
casuales de la aritmética de punto flotante al final verás el
resultado que esperás si simplemente redondeás lo que mostrás de tus
resultados finales al número de dígitos decimales que esperás.
"str()" es normalmente suficiente, y para un control más fino mirá los
parámetros del método de formateo "str.format()" en Custom string
formatting.

Para los casos de uso que necesitan una representación decimal exacta,
probá el módulo "decimal", que implementa aritmética decimal útil para
aplicaciones de contabilidad y de alta precisión.

El módulo "fractions" soporta otra forma de aritmética exacta, ya que
implementa aritmética basada en números racionales (por lo que números
como 1/3 pueden ser representados exactamente).

Si eres un usuario intensivo de operaciones de punto flotante,
deberías echar un vistazo al paquete NumPy y a muchos otros paquetes
para operaciones matemáticas y estadísticas proporcionados por el
proyecto SciPy. Ver <https://scipy.org>.

Python provee herramientas que pueden ayudar en esas raras ocasiones
cuando realmente *querés* saber el valor exacto de un punto flotante.
El método "float.as_integer_ratio()" expresa el valor del punto
flotante como una fracción:

   >>> x = 3.14159
   >>> x.as_integer_ratio()
   (3537115888337719, 1125899906842624)

Ya que la fracción es exacta, se puede usar para recrear sin pérdidas
el valor original:

   >>> x == 3537115888337719 / 1125899906842624
   True

El método "float.hex()" expresa un punto flotante en hexadecimal (base
16), nuevamente retornando el valor exacto almacenado por tu
computadora:

   >>> x.hex()
   '0x1.921f9f01b866ep+1'

Esta representación hexadecimal precisa se puede usar para reconstruir
el valor exacto del punto flotante:

   >>> x == float.fromhex('0x1.921f9f01b866ep+1')
   True

Ya que la representación es exacta, es útil para portar valores a
través de diferentes versiones de Python de manera confiable
(independencia de plataformas) e intercambiar datos con otros
lenguajes que soportan el mismo formato (como Java y C99).

Otra herramienta útil es la función "sum()" que ayuda a mitigar la
pérdida de precisión durante la suma. Utiliza precisión extendida para
pasos de redondeo intermedios a medida que se agregan valores a un
total en ejecución. Esto puede marcar la diferencia en la precisión
general para que los errores no se acumulen hasta el punto en que
afecten el total final:

   >>> 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 == 1.0
   False
   >>> sum([0.1] * 10) == 1.0
   True

The "math.fsum()" goes further and tracks all of the "lost digits" as
values are added onto a running total so that the result has only a
single rounding.  This is slower than "sum()" but will be more
accurate in uncommon cases where large magnitude inputs mostly cancel
each other out leaving a final sum near zero:

   >>> arr = [-0.10430216751806065, -266310978.67179024, 143401161448607.16,
   ...        -143401161400469.7, 266262841.31058735, -0.003244936839808227]
   >>> float(sum(map(Fraction, arr)))   # Exact summation with single rounding
   8.042173697819788e-13
   >>> math.fsum(arr)                   # Single rounding
   8.042173697819788e-13
   >>> sum(arr)                         # Multiple roundings in extended precision
   8.042178034628478e-13
   >>> total = 0.0
   >>> for x in arr:
   ...     total += x                   # Multiple roundings in standard precision
   ...
   >>> total                            # Straight addition has no correct digits!
   -0.0051575902860057365

## 15.1. Error de Representación

Esta sección explica el ejemplo "0.1" en detalle, y muestra como en la
mayoría de los casos vos mismo podés realizar un análisis exacto como
este. Se asume un conocimiento básico de la representación de punto
flotante binario.

*Error de representación* se refiere al hecho de que algunas (la
mayoría) de las fracciones decimales no pueden representarse
exactamente como fracciones binarias (en base 2).  Esta es la razón
principal de por qué Python (o Perl, C, C++, Java, Fortran, y tantos
otros) frecuentemente no mostrarán el número decimal exacto que
esperás.

¿Por qué sucede esto? 1/10 no es exactamente representable como una
fracción binaria. Desde al menos el año 2000, casi todas las máquinas
utilizan la aritmética de punto flotante binaria IEEE 754, y casi
todas las plataformas asignan los números de punto flotante de Python
a valores binarios de 64 bits de precisión "doble" de IEEE 754. Los
valores binarios de IEEE 754 de 64 bits contienen 53 bits de
precisión, por lo que en la entrada, la computadora se esfuerza por
convertir 0.1 en la fracción más cercana de la forma *J*/2***N* donde
*J* es un número entero que contiene exactamente 53 bits.
Reescribiendo

   1 / 10 ~= J / (2**N)

...como

   J ~= 2**N / 10

...y recordando que *J* tiene exactamente 53 bits (es ">= 2**52" pero
"< 2**53"), el mejor valor para *N* es 56:

   >>> 2**52 <=  2**56 // 10  < 2**53
   True

O sea, 56 es el único valor para *N* que deja *J* con exactamente 53
bits. El mejor valor posible para *J* es entonces el cociente
redondeado:

   >>> q, r = divmod(2**56, 10)
   >>> r
   6

Ya que el resto es más que la mitad de 10, la mejor aproximación se
obtiene redondeándolo:

   >>> q+1
   7205759403792794

Por lo tanto la mejor aproximación a 1/10 en doble precisión IEEE 754
es:

   7205759403792794 / 2 ** 56

El dividir tanto el numerador como el denominador reduce la fracción
a:

   3602879701896397 / 2 ** 55

Notá que como lo redondeamos, esto es un poquito más grande que 1/10;
si no lo hubiéramos redondeado, el cociente hubiese sido un poquito
menor que 1/10.  ¡Pero no hay caso en que sea *exactamente* 1/10!

Entonces la computadora nunca "ve" 1/10: lo que ve es la fracción
exacta de arriba, la mejor aproximación al flotante doble IEEE 754 que
puede obtener:

   >>> 0.1 * 2 ** 55
   3602879701896397.0

Si multiplicamos esa fracción por 10**55, podemos ver el valor hasta
los 55 dígitos decimales:

   >>> 3602879701896397 * 10 ** 55 // 2 ** 55
   1000000000000000055511151231257827021181583404541015625

lo que significa que el valor exacto almacenado en la computadora es
igual al valor decimal
0.1000000000000000055511151231257827021181583404541015625. En lugar de
mostrar el valor decimal completo, muchos lenguajes (incluyendo
versiones anteriores de Python), redondean el resultado a 17 dígitos
significativos:

   >>> format(0.1, '.17f')
   '0.10000000000000001'

Los módulos "fractions" y "decimal" hacen fácil estos cálculos:

   >>> from decimal import Decimal
   >>> from fractions import Fraction

   >>> Fraction.from_float(0.1)
   Fraction(3602879701896397, 36028797018963968)

   >>> (0.1).as_integer_ratio()
   (3602879701896397, 36028797018963968)

   >>> Decimal.from_float(0.1)
   Decimal('0.1000000000000000055511151231257827021181583404541015625')

   >>> format(Decimal.from_float(0.1), '.17')
   '0.10000000000000001'
