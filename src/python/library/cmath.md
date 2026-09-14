---
title: '"cmath" --- Mathematical functions for complex numbers'
source_url: https://docs.python.org/es/3
source_path: library/cmath.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1930
---

# "cmath" --- Mathematical functions for complex numbers

======================================================================

This module provides access to mathematical functions for complex
numbers.  The functions in this module accept integers, floating-point
numbers or complex numbers as arguments. They will also accept any
Python object that has either a "__complex__()" or a "__float__()"
method: these methods are used to convert the object to a complex or
floating-point number, respectively, and the function is then applied
to the result of the conversion.

Nota:

  For functions involving branch cuts, we have the problem of deciding
  how to define those functions on the cut itself. Following Kahan's
  "Branch cuts for complex elementary functions" paper, as well as
  Annex G of C99 and later C standards, we use the sign of zero to
  distinguish one side of the branch cut from the other: for a branch
  cut along (a portion of) the real axis we look at the sign of the
  imaginary part, while for a branch cut along the imaginary axis we
  look at the sign of the real part.For example, the "cmath.sqrt()"
  function has a branch cut along the negative real axis. An argument
  of "-2-0j" is treated as though it lies *below* the branch cut, and
  so gives a result on the negative imaginary axis:

     >>> cmath.sqrt(-2-0j)
     -1.4142135623730951j

  But an argument of "-2+0j" is treated as though it lies above the
  branch cut:

     >>> cmath.sqrt(-2+0j)
     1.4142135623730951j

# | **Conversions to and from polar coordinates**                                                                             |

## | "phase(z)"                                           | Return the phase of *z*                                            |

## | "polar(z)"                                           | Return the representation of *z* in polar coordinates              |

## | "rect(r, phi)"                                       | Return the complex number *z* with polar coordinates *r* and *phi* |

## | **Power and logarithmic functions**                                                                                       |

## | "exp(z)"                                             | Return *e* raised to the power *z*                                 |

## | "log(z[, base])"                                     | Return the logarithm of *z* to the given *base* (*e* by default)   |

## | "log10(z)"                                           | Return the base-10 logarithm of *z*                                |

## | "sqrt(z)"                                            | Return the square root of *z*                                      |

## | **Trigonometric functions**                                                                                               |

## | "acos(z)"                                            | Return the arc cosine of *z*                                       |

## | "asin(z)"                                            | Return the arc sine of *z*                                         |

## | "atan(z)"                                            | Return the arc tangent of *z*                                      |

## | "cos(z)"                                             | Return the cosine of *z*                                           |

## | "sin(z)"                                             | Return the sine of *z*                                             |

## | "tan(z)"                                             | Return the tangent of *z*                                          |

## | **Hyperbolic functions**                                                                                                  |

## | "acosh(z)"                                           | Return the inverse hyperbolic cosine of *z*                        |

## | "asinh(z)"                                           | Return the inverse hyperbolic sine of *z*                          |

## | "atanh(z)"                                           | Return the inverse hyperbolic tangent of *z*                       |

## | "cosh(z)"                                            | Return the hyperbolic cosine of *z*                                |

## | "sinh(z)"                                            | Return the hyperbolic sine of *z*                                  |

## | "tanh(z)"                                            | Return the hyperbolic tangent of *z*                               |

## | **Classification functions**                                                                                              |

## | "isfinite(z)"                                        | Check if all components of *z* are finite                          |

## | "isinf(z)"                                           | Check if any component of *z* is infinite                          |

## | "isnan(z)"                                           | Check if any component of *z* is a NaN                             |

## | "isclose(a, b, *, rel_tol, abs_tol)"                 | Check if the values *a* and *b* are close to each other            |

## | **Constants**                                                                                                             |

## | "pi"                                                 | *π* = 3.141592...                                                  |

## | "e"                                                  | *e* = 2.718281...                                                  |

## | "tau"                                                | *τ* = 2*π* = 6.283185...                                           |

## | "inf"                                                | Positive infinity                                                  |

## | "infj"                                               | Pure imaginary infinity                                            |

## | "nan"                                                | "Not a number" (NaN)                                               |

## | "nanj"                                               | Pure imaginary NaN                                                 |

## Conversión a y desde coordenadas polares

A Python complex number "z" is stored internally using *rectangular*
or *Cartesian* coordinates.  It is completely determined by its *real
part* "z.real" and its *imaginary part* "z.imag".

*Las coordenadas polares* dan una alternativa a la representación de
números complejos. En las coordenadas polares, un número complejo *z*
se define por los módulos *r* y el ángulo de fase *phi*. El módulo *r*
es la distancia desde *z* hasta el origen, mientras que la fase *phi*
es el ángulo que va en contra de las agujas del reloj, medido en
radianes, desde el eje positivo de las X hasta el segmento de linea
que une el origen con *z*.

Las siguientes funciones pueden ser usadas para convertir desde
coordenadas rectangulares nativas hasta coordenadas polares y
viceversa.

cmath.phase(z)

   Return the phase of *z* (also known as the *argument* of *z*), as a
   float. "phase(z)" is equivalent to "math.atan2(z.imag, z.real)".
   The result lies in the range [-*π*, *π*], and the branch cut for
   this operation lies along the negative real axis.  The sign of the
   result is the same as the sign of "z.imag", even when "z.imag" is
   zero:

      >>> phase(-1+0j)
      3.141592653589793
      >>> phase(-1-0j)
      -3.141592653589793

Nota:

  The modulus (absolute value) of a complex number *z* can be computed
  using the built-in "abs()" function.  There is no separate "cmath"
  module function for this operation.

cmath.polar(z)

   Return the representation of *z* in polar coordinates.  Returns a
   pair "(r, phi)" where *r* is the modulus of *z* and *phi* is the
   phase of *z*.  "polar(z)" is equivalent to "(abs(z), phase(z))".

cmath.rect(r, phi)

   Return the complex number *z* with polar coordinates *r* and *phi*.
   Equivalent to "complex(r * math.cos(phi), r * math.sin(phi))".

## Funciones logarítmicas y de potencias

cmath.exp(z)

   Return *e* raised to the power *z*, where *e* is the base of
   natural logarithms.

cmath.log(z[, base])

   Return the logarithm of *z* to the given *base*. If the *base* is
   not specified, returns the natural logarithm of *z*. There is one
   branch cut, from 0 along the negative real axis to -∞.

cmath.log10(z)

   Return the base-10 logarithm of *z*. This has the same branch cut
   as "log()".

cmath.sqrt(z)

   Return the square root of *z*. This has the same branch cut as
   "log()".

## Funciones trigonométricas

cmath.acos(z)

   Return the arc cosine of *z*. There are two branch cuts: One
   extends right from 1 along the real axis to ∞. The other extends
   left from -1 along the real axis to -∞.

cmath.asin(z)

   Return the arc sine of *z*. This has the same branch cuts as
   "acos()".

cmath.atan(z)

   Return the arc tangent of *z*. There are two branch cuts: One
   extends from "1j" along the imaginary axis to "∞j". The other
   extends from "-1j" along the imaginary axis to "-∞j".

cmath.cos(z)

   Return the cosine of *z*.

cmath.sin(z)

   Return the sine of *z*.

cmath.tan(z)

   Return the tangent of *z*.

## Funciones hiperbólicas

cmath.acosh(z)

   Return the inverse hyperbolic cosine of *z*. There is one branch
   cut, extending left from 1 along the real axis to -∞.

cmath.asinh(z)

   Return the inverse hyperbolic sine of *z*. There are two branch
   cuts: One extends from "1j" along the imaginary axis to "∞j".  The
   other extends from "-1j" along the imaginary axis to "-∞j".

cmath.atanh(z)

   Return the inverse hyperbolic tangent of *z*. There are two branch
   cuts: One extends from "1" along the real axis to "∞". The other
   extends from "-1" along the real axis to "-∞".

cmath.cosh(z)

   Return the hyperbolic cosine of *z*.

cmath.sinh(z)

   Return the hyperbolic sine of *z*.

cmath.tanh(z)

   Return the hyperbolic tangent of *z*.

## Funciones de clasificación

cmath.isfinite(z)

   Return "True" if both the real and imaginary parts of *z* are
   finite, and "False" otherwise.

   Added in version 3.2.

cmath.isinf(z)

   Return "True" if either the real or the imaginary part of *z* is an
   infinity, and "False" otherwise.

cmath.isnan(z)

   Return "True" if either the real or the imaginary part of *z* is a
   NaN, and "False" otherwise.

cmath.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)

   Retorna "True" si los valores *a* y *b* son cercanos el uno al otro
   y "Falso" de otro modo.

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
   any "x" and rel_tol less than "1.0".  So add an appropriate
   positive abs_tol argument to the call.

   Los valores especiales IEEE 754 de "NaN", "inf" y "-inf" serán
   manejados de acuerdo al estándar de IEEE. Especialmente, "NaN" no
   se considera cercano a ningún otro valor, incluido "NaN". "inf" y
   "-inf" solo son considerados cercanos a sí mismos.

   Added in version 3.5.

   Ver también:

     **PEP 485** -- Una función para probar igualdad aproximada.

## Constantes

cmath.pi

   La constante matemática *π*, como número de coma flotante.

cmath.e

   La constante matemática *e*, como número de coma flotante.

cmath.tau

   La constante matemática *τ*, como número de coma flotante.

   Added in version 3.6.

cmath.inf

   Números de coma flotante de +infinito. Equivalente a
   "float('inf')".

   Added in version 3.6.

cmath.infj

   Números complejos con la parte real cero y números positivos
   infinitos como la parte imaginaria. Equivalente a "complex(0.0,
   float('inf'))".

   Added in version 3.6.

cmath.nan

   A floating-point "not a number" (NaN) value.  Equivalent to
   "float('nan')". See also "math.nan".

   Added in version 3.6.

cmath.nanj

   Números complejos con parte real cero y como parte imaginaria NaN.
   Equivalente a "complex(0.0, float('nan'))".

   Added in version 3.6.

Note that the selection of functions is similar, but not identical, to
that in module "math".  The reason for having two modules is that some
users aren't interested in complex numbers, and perhaps don't even
know what they are.  They would rather have "math.sqrt(-1)" raise an
exception than return a complex number. Also note that the functions
defined in "cmath" always return a complex number, even if the answer
can be expressed as a real number (in which case the complex number
has an imaginary part of zero).

Un apunte en los tramos: Se tratan de curvas en las cuales las
funciones fallan a ser continua. Son un complemento necesario de
muchas funciones complejas. Se asume que si se necesitan cálculos con
funciones complejas, usted entenderá sobre tramos. Consulte casi
cualquier(no muy elemental) libro sobre variables complejas para saber
más. Para más información en la correcta elección de los tramos para
propósitos numéricos, se recomienda la siguiente bibliografía:

Ver también:

  *Kahan, W:  Branch cuts for complex elementary functions; o, Much
  ado about nothing's sign bit.  En Iserles, A., and Powell, M.
  (eds.), The state of the art in numerical analysis. Clarendon Press
  (1987) pp165--211*.
