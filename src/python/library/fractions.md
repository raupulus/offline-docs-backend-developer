---
title: '"fractions" --- Rational numbers'
source_url: https://docs.python.org/es/3
source_path: library/fractions.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2650
---

# "fractions" --- Rational numbers

**Source code:** Lib/fractions.py

======================================================================

The "fractions" module provides support for rational number
arithmetic.

A Fraction instance can be constructed from a pair of rational
numbers, from a single number, or from a string.

class fractions.Fraction(numerator=0, denominator=1)
class fractions.Fraction(number)
class fractions.Fraction(string)

   The first version requires that *numerator* and *denominator* are
   instances of "numbers.Rational" and returns a new "Fraction"
   instance with a value equal to "numerator/denominator". If
   *denominator* is zero, it raises a "ZeroDivisionError".

   The second version requires that *number* is an instance of
   "numbers.Rational" or has the "as_integer_ratio()" method (this
   includes "float" and "decimal.Decimal"). It returns a "Fraction"
   instance with exactly the same value. Assumed, that the
   "as_integer_ratio()" method returns a pair of coprime integers and
   last one is positive. Note that due to the usual issues with binary
   point (see Floating-Point Arithmetic:  Issues and Limitations), the
   argument to "Fraction(1.1)" is not exactly equal to 11/10, and so
   "Fraction(1.1)" does *not* return "Fraction(11, 10)" as one might
   expect. (But see the documentation for the "limit_denominator()"
   method below.)

   The last version of the constructor expects a string. The usual
   form for this instance is:

      [sign] numerator ['/' denominator]

   donde el "sign" opcional puede ser '+' o '-' y "numerator" y
   "denominator" (si están presentes) son cadenas de caracteres de
   dígitos decimales (guiones bajos se pueden usar para delimitar
   dígitos como con las integrales literales en el código). Además,
   cualquier cadena de caracteres que represente un valor finito y sea
   aceptado por el constructor de "float" también es aceptado por el
   constructor de "Fraction". En cualquier caso, la cadena de
   caracteres de entrada también puede tener espacios en blanco
   iniciales y / o finales. Aquí hay unos ejemplos:

      >>> from fractions import Fraction
      >>> Fraction(16, -10)
      Fraction(-8, 5)
      >>> Fraction(123)
      Fraction(123, 1)
      >>> Fraction()
      Fraction(0, 1)
      >>> Fraction('3/7')
      Fraction(3, 7)
      >>> Fraction(' -3/7 ')
      Fraction(-3, 7)
      >>> Fraction('1.414213 \t\n')
      Fraction(1414213, 1000000)
      >>> Fraction('-.125')
      Fraction(-1, 8)
      >>> Fraction('7e-6')
      Fraction(7, 1000000)
      >>> Fraction(2.25)
      Fraction(9, 4)
      >>> Fraction(1.1)
      Fraction(2476979795053773, 2251799813685248)
      >>> from decimal import Decimal
      >>> Fraction(Decimal('1.1'))
      Fraction(11, 10)

   La clase "Fraction" hereda de la clase base abstracta
   "numbers.Rational", e implementa todos los métodos y operaciones de
   esa clase. Las instancias "Fraction" son *hashable*, y deben ser
   tratadas como inmutables. Adicionalmente "Fraction" tiene los
   siguientes propiedades y métodos:

   Distinto en la versión 3.2: El constructor de "Fraction" ahora
   acepta instancias de "float" y "decimal".

   Distinto en la versión 3.9: The "math.gcd()" function is now used
   to normalize the *numerator* and *denominator*. "math.gcd()" always
   returns an "int" type. Previously, the GCD type depended on
   *numerator* and *denominator*.

   Distinto en la versión 3.11: Ahora se permiten guiones bajos al
   crear una instancia de "Fraction" a partir de una cadena de
   caracteres, siguiendo las reglas de **PEP 515**.

   Distinto en la versión 3.11: "Fraction" ahora implementa "__int__"
   para satisfacer las comprobaciones de instancia de
   "typing.SupportsInt".

   Distinto en la versión 3.12: Se permite espacio alrededor de la
   barra para entrada de cadena de caracteres: "Fraction('2 / 3')".

   Distinto en la versión 3.12: "Fraction" instancias ahora apoya
   formato de estilo flotante, con tipos de presentación ""e"", ""E"",
   ""f"", ""F"", ""g"", ""G"" and ""%""".

   Distinto en la versión 3.13: Formatting of "Fraction" instances
   without a presentation type now supports fill, alignment, sign
   handling, minimum width and grouping.

   Distinto en la versión 3.14: The "Fraction" constructor now accepts
   any objects with the "as_integer_ratio()" method.

   numerator

      Numerador de la fracción irreducible.

   denominator

      Denominator of the Fraction in lowest terms. Guaranteed to be
      positive.

   as_integer_ratio()

      Retorna una tupla de dos números enteros, cuyo relación es igual
      a la fracción original.La relación está en términos más bajos y
      tiene un denominador positivo.

      Added in version 3.8.

   is_integer()

      Retorna "True" si la fracción es un número entero.

      Added in version 3.12.

   classmethod from_float(f)

      Constructor alternativo que solo acepta instancias de "float" o
      "numbers.Integral". Ten cuidado que "Fraction.from_float(0.3)"
      no es lo mismo  que "Fraction(3, 10)".

      Nota:

        Desde Python 3.2 en adelante, puedes construir una instancia
        "Fraction" directamente desde "float".

   classmethod from_decimal(dec)

      Constructor alternativo que solo acepta instancias de
      "decimal.Decimal" o "numbers.Integral".

      Nota:

        Desde Python 3.2 en adelante, puedes construir una instancia
        "Fraction" directamente desde una instancia "decimal.Decimal".

   classmethod from_number(number)

      Alternative constructor which only accepts instances of
      "numbers.Integral", "numbers.Rational", "float" or
      "decimal.Decimal", and objects with the "as_integer_ratio()"
      method, but not strings.

      Added in version 3.14.

   limit_denominator(max_denominator=1000000)

      Busca y retorna la instancia de "Fraction" mas cercana a "self"
      que tenga como denominador *max_denominator*. Este método es
      útil para encontrar aproximaciones racionales a un número en
      punto flotante determinado:

      >>> from fractions import Fraction
      >>> Fraction('3.1415926535897932').limit_denominator(1000)
      Fraction(355, 113)

      o para recuperar un numero racional que esta representado como
      flotante:

      >>> from math import pi, cos
      >>> Fraction(cos(pi/3))
      Fraction(4503599627370497, 9007199254740992)
      >>> Fraction(cos(pi/3)).limit_denominator()
      Fraction(1, 2)
      >>> Fraction(1.1).limit_denominator()
      Fraction(11, 10)

   __floor__()

      Retorna el máximo "int" "<= self". Este método puede accederse
      también a través de la función "math.floor()":

      >>> from math import floor
      >>> floor(Fraction(355, 113))
      3

   __ceil__()

      Retorna el mínimo "int" ">= self". Este método puede accederse
      también a través de la función "math.ceil()".

   __round__()
   __round__(ndigits)

      La primera versión retorna el valor "int" mas cercano a "self"
      redondeando mitades al valor par. La segunda versión redondea
      "self" al múltiplo mas cercano de "Fraction(1, 10**ndigits)"
      (lógicamente, si "ndigits" es negativo), nuevamente redondeando
      mitades al valor par. Este método también puede accederse a
      través de la función "round()".

   __format__(format_spec, /)

      Provides support for formatting of "Fraction" instances via the
      "str.format()" method, the "format()" built-in function, or
      Formatted string literals.

      If the "format_spec" format specification string does not end
      with one of the presentation types "'e'", "'E'", "'f'", "'F'",
      "'g'", "'G'" or "'%'" then formatting follows the general rules
      for fill, alignment, sign handling, minimum width, and grouping
      as described in the format specification mini-language. The
      "alternate form" flag "'#'" is supported: if present, it forces
      the output string to always include an explicit denominator,
      even when the value being formatted is an exact integer. The
      zero-fill flag "'0'" is not supported.

      If the "format_spec" format specification string ends with one
      of the presentation types "'e'", "'E'", "'f'", "'F'", "'g'",
      "'G'" or "'%'" then formatting follows the rules outlined for
      the "float" type in the Format specification mini-language
      section.

      Aquí hay unos ejemplos:

         >>> from fractions import Fraction
         >>> format(Fraction(103993, 33102), '_')
         '103_993/33_102'
         >>> format(Fraction(1, 7), '.^+10')
         '...+1/7...'
         >>> format(Fraction(3, 1), '')
         '3'
         >>> format(Fraction(3, 1), '#')
         '3/1'
         >>> format(Fraction(1, 7), '.40g')
         '0.1428571428571428571428571428571428571429'
         >>> format(Fraction('1234567.855'), '_.2f')
         '1_234_567.86'
         >>> f"{Fraction(355, 113):*>20.6e}"
         '********3.141593e+00'
         >>> old_price, new_price = 499, 672
         >>> "{:.2%} price increase".format(Fraction(new_price, old_price) - 1)
         '34.67% price increase'

Ver también:

  Módulo "numbers"
     Las clases base abstractas que representan la jerarquía de
     números.
