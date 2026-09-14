---
title: '"math" --- Mathematical functions'
source_url: https://docs.python.org/es/3
source_path: library/math.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3200
---

# "math" --- Mathematical functions

======================================================================

This module provides access to common mathematical functions and
constants, including those defined by the C standard.

Estas funciones no pueden ser usadas con números complejos; usa las
funciones con el mismo nombre del módulo "cmath" si requieres soporte
para números complejos. La distinción entre las funciones que admiten
números complejos y las que no se hace debido a que la mayoría de los
usuarios no quieren aprender tantas matemáticas como se requiere para
comprender los números complejos. Recibir una excepción en lugar de un
resultado complejo permite la detección temprana del número complejo
inesperado utilizado como parámetro, de modo que el programador pueda
determinar cómo y porqué se generó en primer lugar.

Este módulo proporciona las funciones descritas a continuación.
Excepto cuando se indique lo contrario explícitamente, todos los
valores retornados son flotantes.

# | **Number-theoretic functions**                                                                                                                                                |

## | "comb(n, k)"                                         | Number of ways to choose *k* items from *n* items without repetition and without order                                 |

## | "factorial(n)"                                       | *n* factorial                                                                                                          |

## | "gcd(*integers)"                                     | Greatest common divisor of the integer arguments                                                                       |

## | "isqrt(n)"                                           | Integer square root of a nonnegative integer *n*                                                                       |

## | "lcm(*integers)"                                     | Least common multiple of the integer arguments                                                                         |

## | "perm(n, k)"                                         | Number of ways to choose *k* items from *n* items without repetition and with order                                    |

## | **Floating point arithmetic**                                                                                                                                                 |

## | "ceil(x)"                                            | Ceiling of *x*, the smallest integer greater than or equal to *x*                                                      |

## | "fabs(x)"                                            | Absolute value of *x*                                                                                                  |

## | "floor(x)"                                           | Floor of *x*, the largest integer less than or equal to *x*                                                            |

## | "fma(x, y, z)"                                       | Fused multiply-add operation: "(x * y) + z"                                                                            |

## | "fmod(x, y)"                                         | Remainder of division "x / y"                                                                                          |

## | "modf(x)"                                            | Fractional and integer parts of *x*                                                                                    |

## | "remainder(x, y)"                                    | Remainder of *x* with respect to *y*                                                                                   |

## | "trunc(x)"                                           | Integer part of *x*                                                                                                    |

## | **Floating point manipulation functions**                                                                                                                                     |

## | "copysign(x, y)"                                     | Magnitude (absolute value) of *x* with the sign of *y*                                                                 |

## | "frexp(x)"                                           | Mantissa and exponent of *x*                                                                                           |

## | "isclose(a, b, rel_tol, abs_tol)"                    | Check if the values *a* and *b* are close to each other                                                                |

## | "isfinite(x)"                                        | Check if *x* is neither an infinity nor a NaN                                                                          |

## | "isinf(x)"                                           | Check if *x* is a positive or negative infinity                                                                        |

## | "isnan(x)"                                           | Check if *x* is a NaN  (not a number)                                                                                  |

## | "ldexp(x, i)"                                        | "x * (2**i)", inverse of function "frexp()"                                                                            |

## | "nextafter(x, y, steps)"                             | Floating-point value *steps* steps after *x* towards *y*                                                               |

## | "ulp(x)"                                             | Value of the least significant bit of *x*                                                                              |

## | **Power, exponential and logarithmic functions**                                                                                                                              |

## | "cbrt(x)"                                            | Cube root of *x*                                                                                                       |

## | "exp(x)"                                             | *e* raised to the power *x*                                                                                            |

## | "exp2(x)"                                            | *2* raised to the power *x*                                                                                            |

## | "expm1(x)"                                           | *e* raised to the power *x*, minus 1                                                                                   |

## | "log(x, base)"                                       | Logarithm of *x* to the given base (*e* by default)                                                                    |

## | "log1p(x)"                                           | Natural logarithm of *1+x* (base *e*)                                                                                  |

## | "log2(x)"                                            | Base-2 logarithm of *x*                                                                                                |

## | "log10(x)"                                           | Base-10 logarithm of *x*                                                                                               |

## | "pow(x, y)"                                          | *x* raised to the power *y*                                                                                            |

## | "sqrt(x)"                                            | Square root of *x*                                                                                                     |

## | **Summation and product functions**                                                                                                                                           |

## | "dist(p, q)"                                         | Euclidean distance between two points *p* and *q* given as an iterable of coordinates                                  |

## | "fsum(iterable)"                                     | Sum of values in the input *iterable*                                                                                  |

## | "hypot(*coordinates)"                                | Euclidean norm of an iterable of coordinates                                                                           |

## | "prod(iterable, start)"                              | Product of elements in the input *iterable* with a *start* value                                                       |

## | "sumprod(p, q)"                                      | Sum of products from two iterables *p* and *q*                                                                         |

## | **Angular conversion**                                                                                                                                                        |

## | "degrees(x)"                                         | Convert angle *x* from radians to degrees                                                                              |

## | "radians(x)"                                         | Convert angle *x* from degrees to radians                                                                              |

## | **Trigonometric functions**                                                                                                                                                   |

## | "acos(x)"                                            | Arc cosine of *x*                                                                                                      |

## | "asin(x)"                                            | Arc sine of *x*                                                                                                        |

## | "atan(x)"                                            | Arc tangent of *x*                                                                                                     |

## | "atan2(y, x)"                                        | "atan(y / x)"                                                                                                          |

## | "cos(x)"                                             | Cosine of *x*                                                                                                          |

## | "sin(x)"                                             | Sine of *x*                                                                                                            |

## | "tan(x)"                                             | Tangent of *x*                                                                                                         |

## | **Hyperbolic functions**                                                                                                                                                      |

## | "acosh(x)"                                           | Inverse hyperbolic cosine of *x*                                                                                       |

## | "asinh(x)"                                           | Inverse hyperbolic sine of *x*                                                                                         |

## | "atanh(x)"                                           | Inverse hyperbolic tangent of *x*                                                                                      |

## | "cosh(x)"                                            | Hyperbolic cosine of *x*                                                                                               |

## | "sinh(x)"                                            | Hyperbolic sine of *x*                                                                                                 |

## | "tanh(x)"                                            | Hyperbolic tangent of *x*                                                                                              |

## | **Special functions**                                                                                                                                                         |

## | "erf(x)"                                             | Error function at *x*                                                                                                  |

## | "erfc(x)"                                            | Complementary error function at *x*                                                                                    |

## | "gamma(x)"                                           | Gamma function at *x*                                                                                                  |

## | "lgamma(x)"                                          | Natural logarithm of the absolute value of the Gamma function at *x*                                                   |

## | **Constants**                                                                                                                                                                 |

## | "pi"                                                 | *π* = 3.141592...                                                                                                      |

## | "e"                                                  | *e* = 2.718281...                                                                                                      |

## | "tau"                                                | *τ* = 2*π* = 6.283185...                                                                                               |

## | "inf"                                                | Positive infinity                                                                                                      |

## | "nan"                                                | "Not a number" (NaN)                                                                                                   |

## Number-theoretic functions

math.comb(n, k)

   Retorna el número de formas posibles de elegir *k* elementos de
   *n*, de forma ordenada y sin repetición.

   Se evalúa como "n! / (k! * (n - k)!)" cuando "k <= n" y como cero
   cuando "k > n".

   También llamado coeficiente binomial porque es equivalente al
   coeficiente del k-ésimo término en la expansión polinomial de "(1 +
   x)ⁿ".

   Lanza una excepción "TypeError" si alguno de los argumentos no es
   un entero. Lanza una excepción "ValueError" si alguno de los
   argumentos es negativo.

   Added in version 3.8.

math.factorial(n)

   Return factorial of the nonnegative integer *n*.

   Distinto en la versión 3.10: Floats with integral values (like
   "5.0") are no longer accepted.

math.gcd(*integers)

   Retorna el máximo común divisor de los argumentos enteros. Si
   cualquiera de los argumentos no es cero, entonces el valor
   retornado es el entero positivo más grande que divide a todos los
   argumentos. Si todos los argumentos son cero, entonces el valor
   retornado es "0". "gcd()" sin argumentos retorna "0".

   Added in version 3.5.

   Distinto en la versión 3.9: Agregado soporte para un número
   arbitrario de argumentos. Anteriormente sólo se soportaba dos
   argumentos.

math.isqrt(n)

   Retorna la raíz cuadrada del número entero no negativo *n*. Es el
   resultado de aplicar la función suelo al valor exacto de la raíz
   cuadrada de *n*, o de forma equivalente, el mayor entero *a* tal
   que *a*² ≤ *n*.

   Para algunas aplicaciones, puede ser más conveniente tener el menor
   número entero *a* tal que *n* ≤ *a*², en otras palabras, el
   resultado de aplicar la función techo a la raíz cuadrada exacta de
   *n*. Para *n* positivo, esto se puede calcular usando "a = 1 +
   isqrt(n - 1)".

   Added in version 3.8.

math.lcm(*integers)

   Retorna el mínimo común múltiplo de los argumentos enteros. Si
   todos los argumentos no son cero, entonces el valor retornado es el
   entero positivo más pequeño que es un múltiplo de todos los
   argumentos. Si cualquiera de los argumentos es cero, entonces el
   valor retornado es "0". "lcm()" sin argumentos retorna "1".

   Added in version 3.9.

math.perm(n, k=None)

   Retorna el número de formas posibles de elegir *k* elementos de *n*
   elementos, sin repetición y en orden.

   Se evalúa como "n! / (n - k)!" cuando "k <= n" y como cero cuando
   "k > n".

   If *k* is not specified or is "None", then *k* defaults to *n* and
   the function returns "n!".

   Lanza una excepción "TypeError" si alguno de los argumentos no es
   un entero. Lanza una excepción "ValueError" si alguno de los
   argumentos es negativo.

   Added in version 3.8.

## Floating point arithmetic

math.ceil(x)

   Retorna el "techo" de *x*, el número entero más pequeño que es
   mayor o igual que *x*. Si *x* no es un flotante, delega en
   "x.__ceil__", que debería retornar un valor "Integral".

math.fabs(x)

   Retorna el valor absoluto de *x*.

math.floor(x)

   Retorna el "suelo" de *x*, el primer número entero menor o igual
   que *x*. Si *x* no es un flotante, delega en "x.__floor__", que
   debería retornar un valor "Integral".

math.fma(x, y, z)

   Fused multiply-add operation. Return "(x * y) + z", computed as
   though with infinite precision and range followed by a single round
   to the "float" format. This operation often provides better
   accuracy than the direct expression "(x * y) + z".

   This function follows the specification of the fusedMultiplyAdd
   operation described in the IEEE 754 standard. The standard leaves
   one case implementation-defined, namely the result of "fma(0, inf,
   nan)" and "fma(inf, 0, nan)". In these cases, "math.fma" returns a
   NaN, and does not raise any exception.

   Added in version 3.13.

math.fmod(x, y)

   Return the floating-point remainder of "x / y", as defined by the
   platform C library function "fmod(x, y)". Note that the Python
   expression "x % y" may not return the same result.  The intent of
   the C standard is that "fmod(x, y)" be exactly (mathematically; to
   infinite precision) equal to "x - n*y" for some integer *n* such
   that the result has the same sign as *x* and magnitude less than
   "abs(y)".  Python's "x % y" returns a result with the sign of *y*
   instead, and may not be exactly computable for float arguments. For
   example, "fmod(-1e-100, 1e100)" is "-1e-100", but the result of
   Python's "-1e-100 % 1e100" is "1e100-1e-100", which cannot be
   represented exactly as a float, and rounds to the surprising
   "1e100".  For this reason, function "fmod()" is generally preferred
   when working with floats, while Python's "x % y" is preferred when
   working with integers.

math.modf(x)

   Retorna la parte fraccionaria y entera de *x*. Ambos resultados son
   flotantes y tienen el mismo signo que *x* .

   Note that "modf()" has a different call/return pattern than its C
   equivalents: it takes a single argument and return a pair of
   values, rather than returning its second return value through an
   'output parameter' (there is no such thing in Python).

math.remainder(x, y)

   Retorna el resto o residuo según la norma IEEE 754 de *x* con
   respecto a *y*. Para un valor *x* finito y un valor *y* finito
   distinto de cero, es la diferencia "x - n * y", donde "n" es el
   número entero más cercano al valor exacto del cociente "x / y". Si
   "x / y" está exactamente en mitad de dos enteros consecutivos, el
   entero *par* más cercano se utiliza para "n". Por lo tanto, el
   residuo "r = remainder(x, y)" siempre satisface "abs(r) <= 0.5 *
   abs(y)".

   Los casos especiales siguen el estándar IEEE 754: en particular,
   "remainder(x, math.inf)" es *x* para todo *x* finito, y
   "remainder(x, 0)" junto a "remainder(math.inf, x)" lanzan una
   excepción "ValueError" para todo *x* que no sea NaN. Si el
   resultado de la operación residuo es cero, este cero tendrá el
   mismo signo que *x*.

   On platforms using IEEE 754 binary floating point, the result of
   this operation is always exactly representable: no rounding error
   is introduced.

   Added in version 3.7.

math.trunc(x)

   Retorna *x* con la parte fraccionaria eliminada, dejando la parte
   entera.Esto redondea hacia 0: "trunc()" es equivalente a "floor()"
   para *x* positivo y equivalente a  "ceil()"  para *x* negativo. Si
   *x* no es un flotante, delega a "x.__trunc__", que debería retornar
   un valor "Integral".

Para las funciones "ceil()", "floor()" y "modf()", ten en cuenta que
*todos* los números de coma flotante de magnitud suficientemente
grande son enteros exactos. Los flotantes de Python normalmente no
tienen más de 53 bits de precisión (lo mismo que el tipo double de C
en la plataforma), en cuyo caso cualquier flotante *x* con "abs(x) >=
2**52" no necesariamente tiene bits fraccionarios.

## Floating point manipulation functions

math.copysign(x, y)

   Retorna un flotante con la magnitud (valor absoluto) de *x* pero el
   signo de *y*. En plataformas que admiten ceros con signo,
   "copysign(1.0, -0.0)" retorna *-1.0*.

math.frexp(x)

   Return the mantissa and exponent of *x* as the pair "(m, e)". If
   *x* is a finite nonzero number, then *m* is a float with "0.5 <=
   abs(m) < 1.0" and an integer *e* is such that "x == m * 2**e"
   exactly.  Else, return "(x, 0)". This is used to "pick apart" the
   internal representation of a float in a portable way.

   Note that "frexp()" has a different call/return pattern than its C
   equivalents: it takes a single argument and return a pair of
   values, rather than returning its second return value through an
   'output parameter' (there is no such thing in Python).

math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)

   Retorna "True" si los valores *a* y *b* están cerca el uno del otro
   y "False" en caso contrario.

   Whether or not two values are considered close is determined
   according to given absolute and relative tolerances.  If no errors
   occur, the result will be: "abs(a-b) <= max(rel_tol * max(abs(a),
   abs(b)), abs_tol)".

   *rel_tol* is the relative tolerance -- it is the maximum allowed
   difference between *a* and *b*, relative to the larger absolute
   value of *a* or *b*. For example, to set a tolerance of 5%, pass
   "rel_tol=0.05".  The default tolerance is "1e-09", which assures
   that the two values are the same within about 9 decimal digits.
   *rel_tol* must be nonnegative and less than "1.0".

   *abs_tol* is the absolute tolerance; it defaults to "0.0" and it
   must be nonnegative.  When comparing "x" to "0.0", "isclose(x, 0)"
   is computed as "abs(x) <= rel_tol  * abs(x)", which is "False" for
   any nonzero "x" and *rel_tol* less than "1.0".  So add an
   appropriate positive *abs_tol* argument to the call.

   Los valores especiales de IEEE 754 "NaN", "inf" e "-inf" se
   manejarán de acuerdo con las reglas del IEEE. Concretamente, "NaN"
   no se considera cercano a ningún otro valor, incluido "NaN". Por su
   parte, "inf" e "-inf" solo se consideran cercanos a sí mismos.

   Added in version 3.5.

   Ver también:

     **PEP 485** -- Una función para comprobar la igualdad aproximada

math.isfinite(x)

   Retorna "True" si *x* no es infinito ni NaN, o "False" en caso
   contrario. (Ten en cuenta que "0.0" *es* considerado finito.)

   Added in version 3.2.

math.isinf(x)

   Retorna "True" si *x* es infinito positivo o negativo, o "False" en
   caso contrario.

math.isnan(x)

   Retorna "True" si *x* es NaN (not a number, en español: no es un
   número), o "False" en caso contrario.

math.ldexp(x, i)

   Retorna "x * (2**i)". Esta es esencialmente la función inversa de
   "frexp()".

math.nextafter(x, y, steps=1)

   Retorna el valor en coma flotante *steps* pasos después *x* hacia
   *y*.

   Si *x* es igual a *y*, retorna *y*, a menos que *steps* sea cero.

   Ejemplos:

   * "math.nextafter(x, math.inf)" va hacia el infinito positivo.

   * "math.nextafter(x, -math.inf)" va hacia el infinito negativo.

   * "math.nextafter(x, 0.0)" va hacia cero.

   * "math.nextafter(x, math.copysign(math.inf, x))" se aleja de cero.

   Ver también "math.ulp()".

   Added in version 3.9.

   Distinto en la versión 3.12: Añadido el argumento *steps*.

math.ulp(x)

   Retorna el valor del bit menos significativo del flotante *x*:

   * Si *x* es un NaN (*not a number*), retorna *x*.

   * Si *x* es negativo, retorna "ulp(-x)".

   * Si *x* es un infinito positivo, retorna *x*.

   * Si *x* es igual a cero, retorna el flotante representable
     *desnormalizado* positivo más pequeño (menor que el flotante
     *normalizado* positivo mínimo, "sys.float_info.min").

   * Si *x* es igual al flotante representable positivo más pequeño,
     retorna el bit menos significativo de *x*, de tal manera que el
     primer flotante menor que *x* es "x - ulp(x)".

   * De lo contrario (*x* es un número finito positivo), retorna el
     valor del bit menos significativo de *x* , de tal forma que el
     primer flotante mayor a *x* es "x + ulp(x)".

   ULP significa *Unit in the Last Place* (unidad en el último lugar).

   Ver también "math.nextafter()" y "sys.float_info.epsilon".

   Added in version 3.9.

## Power, exponential and logarithmic functions

math.cbrt(x)

   Retorna la raíz cúbica de *x*.

   Added in version 3.11.

math.exp(x)

   Retorna *e* elevado a la *x* potencia, dónde *e* = 2.718281... es
   la base de los logaritmos naturales. Esto generalmente es más
   preciso que "math.e ** x" o "pow(math.e, x)".

math.exp2(x)

   Retorna *2* elevado a la potencia *x*.

   Added in version 3.11.

math.expm1(x)

   Retorna *e* elevado a la *x* potencia, menos 1. Aquí *e* es la base
   de los logaritmos naturales. Para flotantes *x* pequeños, la resta
   en "exp(x) - 1" puede resultar en una pérdida significativa de
   precisión; la función "expm1()" proporciona una forma de calcular
   este valor con una precisión total:

   >>> from math import exp, expm1
   >>> exp(1e-5) - 1  # gives result accurate to 11 places
   1.0000050000069649e-05
   >>> expm1(1e-5)    # result accurate to full precision
   1.0000050000166668e-05

   Added in version 3.2.

math.log(x[, base])

   Con un argumento, retorna el logaritmo natural de *x* (en base
   *e*).

   Con dos argumentos, retorna el logaritmo de *x* en la *base* dada,
   calculado como "log(x)/log(base)".

math.log1p(x)

   Retorna el logaritmo natural de *1+x* (base *e*). El resultado se
   calcula de forma precisa para *x* cercano a cero.

math.log2(x)

   Retorna el logaritmo en base 2 de *x*. Esto suele ser más preciso
   que "log(x, 2)".

   Added in version 3.3.

   Ver también:

     "int.bit_length()" retorna el número de bits necesarios para
     representar un entero en binario, excluyendo el signo y los ceros
     iniciales.

math.log10(x)

   Retorna el logaritmo en base 10 de *x*. Esto suele ser más preciso
   que "log(x, 10)".

math.pow(x, y)

   Return *x* raised to the power *y*.  Exceptional cases follow the
   IEEE 754 standard as far as possible.  In particular, "pow(1.0, x)"
   and "pow(x, 0.0)" always return "1.0", even when *x* is a zero or a
   NaN.  If both *x* and *y* are finite, *x* is negative, and *y* is
   not an integer then "pow(x, y)" is undefined, and raises
   "ValueError".

   A diferencia del operador incorporado "**", "math.pow()" convierte
   ambos argumentos al tipo "float". Utiliza "**" o la función
   incorporada "pow()" para calcular potencias enteras exactas.

   Distinto en la versión 3.11: Los casos especiales "pow(0.0, -inf)"
   y "pow(-0.0, -inf)" se cambiaron para devolver  "inf" en lugar de
   generar "ValueError", por consistencia con IEEE 754.

math.sqrt(x)

   Retorna la raíz cuadrada de *x*.

## Summation and product functions

math.dist(p, q)

   Retorna la distancia euclidiana entre dos puntos *p* y *q*, cada
   uno de ellos dado como una secuencia (o iterable) de coordenadas.
   Los dos puntos deben tener la misma dimensión.

   Aproximadamente equivalente a:

      sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))

   Added in version 3.8.

math.fsum(iterable)

   Return an accurate floating-point sum of values in the iterable.
   Avoids loss of precision by tracking multiple intermediate partial
   sums.

   La precisión del algoritmo depende de las garantías aritméticas de
   IEEE-754 y del caso típico en el que se usa el "medio redondo a
   par" (half-even) como método de redondeo. En algunas compilaciones
   que no son de Windows, la biblioteca de C subyacente utiliza la
   adición de precisión extendida y, ocasionalmente, puede realizar un
   doble redondeo en una suma intermedia, haciendo que el bit menos
   significativo tome el valor incorrecto.

   For further discussion and two alternative approaches, see the ASPN
   cookbook recipes for accurate floating-point summation.

math.hypot(*coordinates)

   Retorna la norma euclidiana, "sqrt(sum(x**2 for x in
   coordinates))". Esta es la longitud del vector que va desde el
   origen hasta el punto dado por las coordenadas.

   Para un punto bidimensional "(x, y)", esto equivale a calcular la
   hipotenusa de un triángulo rectángulo usando el teorema de
   Pitágoras, "sqrt(x*x + y*y)".

   Distinto en la versión 3.8: Agregado soporte para puntos
   n-dimensionales. Anteriormente, solo se admitía el caso
   bidimensional.

   Distinto en la versión 3.10: Se mejoró la precisión del algoritmo
   para que el error máximo sea inferior a 1 ulp (unidad en último
   lugar). Más típicamente, el resultado casi siempre se redondea
   correctamente dentro de 1/2 ulp.

math.prod(iterable, *, start=1)

   Calcula el producto de todos los elementos en la entrada
   *iterable*. El valor *start* predeterminado para el producto es
   "1".

   Cuando el iterable está vacío, retorna el valor inicial. Esta
   función está diseñada específicamente para su uso con valores
   numéricos y puede rechazar tipos no numéricos.

   Added in version 3.8.

math.sumprod(p, q)

   Retorna la suma de productos de valores de dos iterables *p* y *q*.

   Lanza "ValueError" si las entradas no tienen la misma longitud.

   Aproximadamente equivalente a:

      sum(map(operator.mul, p, q, strict=True))

   Para entradas flotantes y mixtas int/float, los productos
   intermedios y las sumas se calculan con precisión ampliada.

   Added in version 3.12.

## Conversión angular

math.degrees(x)

   Convierte el ángulo *x* de radianes a grados.

math.radians(x)

   Convierte el ángulo *x* de grados a radianes.

## Funciones trigonométricas

math.acos(x)

   Retorna el arcocoseno de *x*, en radianes. El resultado está entre
   "0" y "pi".

math.asin(x)

   Retorna el arcoseno de *x*, en radianes. El resultado está entre
   "-pi/2" y "pi/2".

math.atan(x)

   Retorna la arcotangente de *x*, en radianes. El resultado está
   entre "-pi/2" y "pi/2".

math.atan2(y, x)

   Retorna "atan(y / x)", en radianes. El resultado está entre "-pi" y
   "pi". El vector del plano que va del origen al punto "(x, y)",
   forma este ángulo con el eje X positivo. La ventaja de "atan2()" es
   que el signo de ambas entradas es conocido, por lo que se puede
   calcular el cuadrante correcto para el ángulo. Por ejemplo,
   "atan(1)" y "atan2(1, 1)" son ambas "pi/4", pero "atan2(-1, -1)" es
   "-3*pi/4".

math.cos(x)

   Retorna el coseno de *x* radianes.

math.sin(x)

   Retorna el seno de *x* radianes.

math.tan(x)

   Retorna la tangente de *x* radianes.

## Funciones hiperbólicas

Las funciones hiperbólicas son análogas a las funciones
trigonométricas que están basadas en hipérbolas en lugar de círculos.

math.acosh(x)

   Retorna el coseno hiperbólico inverso de *x*.

math.asinh(x)

   Retorna el seno hiperbólico inverso de *x*.

math.atanh(x)

   Retorna la tangente hiperbólica inversa de *x*.

math.cosh(x)

   Retorna el coseno hiperbólico de *x*.

math.sinh(x)

   Retorna el seno hiperbólico de *x*.

math.tanh(x)

   Retorna la tangente hiperbólica de *x*.

## Funciones especiales

math.erf(x)

   Retorna la función error en *x*.

   The "erf()" function can be used to compute traditional statistical
   functions such as the cumulative standard normal distribution:

      def phi(x):
          'Cumulative distribution function for the standard normal distribution'
          return (1.0 + erf(x / sqrt(2.0))) / 2.0

   Added in version 3.2.

math.erfc(x)

   Retorna la función error complementaria en *x*. La función error
   complementaria se define como "1.0 - erf(x)". Se usa para valores
   grandes de *x* donde una resta de 1 causaría una pérdida de
   presición.

   Added in version 3.2.

math.gamma(x)

   Retorna la función gamma en *x*.

   Added in version 3.2.

math.lgamma(x)

   Retorna el logaritmo natural del valor absoluto de la función gamma
   en *x*.

   Added in version 3.2.

## Constantes

math.pi

   La constante matemática *π* = 3.141592..., hasta la precisión
   disponible.

math.e

   La constante matemática *e* = 2.718281..., hasta la precisión
   disponible.

math.tau

   The mathematical constant *τ* = 6.283185..., to available
   precision. Tau is a circle constant equal to 2*π*, the ratio of a
   circle's circumference to its radius. To learn more about Tau,
   check out Vi Hart's video Pi is (still) Wrong, and start
   celebrating Tau day by eating twice as much pie!

   Added in version 3.6.

math.inf

   Un valor infinito positivo en punto flotante. (Para un valor
   infinito negativo, usa "-math.inf".) Equivalente a la salida de
   "float('inf')".

   Added in version 3.5.

math.nan

   Un valor de coma flotante "no es un número" (NaN). Equivalente a la
   salida de "float('nan')". Debido a los requisitos del estándar
   IEEE-754, "math.nan" y "float('nan')" no se consideran iguales a
   ningún otro valor numérico, incluidos ellos mismos. Para verificar
   si un número es NaN, use la función "isnan()" para probar NaN en
   lugar de "is" o "==". Ejemplo:

   >>> import math
   >>> math.nan == math.nan
   False
   >>> float('nan') == float('nan')
   False
   >>> math.isnan(math.nan)
   True
   >>> math.isnan(float('nan'))
   True

   Added in version 3.5.

   Distinto en la versión 3.11: Ahora está siempre disponible.

**Detalles de implementación de CPython:** The "math" module consists
mostly of thin wrappers around the platform C math library functions.
Behavior in exceptional cases follows Annex F of the C99 standard
where appropriate.  The current implementation will raise "ValueError"
for invalid operations like "sqrt(-1.0)" or "log(0.0)" (where C99
Annex F recommends signaling invalid operation or divide-by-zero), and
"OverflowError" for results that overflow (for example,
"exp(1000.0)").  A NaN will not be returned from any of the functions
above unless one or more of the input arguments was a NaN; in that
case, most functions will return a NaN, but (again following C99 Annex
F) there are some exceptions to this rule, for example
"pow(float('nan'), 0.0)" or "hypot(float('nan'), float('inf'))".

Ten en cuenta que Python no hace ningún esfuerzo por distinguir los
NaN de señalización de los NaN silenciosos, y el comportamiento de
señalización de los NaN permanece sin especificar. El comportamiento
estándar es tratar a todos los NaN como silenciosos.

Ver también:

  Módulo "cmath"
     Versiones de muchas de estas funciones para números complejos.
