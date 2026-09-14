---
title: '"numbers" --- Numeric abstract base classes'
source_url: https://docs.python.org/es/3
source_path: library/numbers.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3340
---

# "numbers" --- Numeric abstract base classes

**Código fuente:** Lib/numbers.py

======================================================================

The "numbers" module (**PEP 3141**) defines a hierarchy of numeric
*abstract base classes* which progressively define more operations.
None of the types defined in this module are intended to be
instantiated.

class numbers.Number

   La raíz de la jerarquía numérica. Si desea validar si un argumento
   *x* es un número, sin importar su tipo, use "isinstance(x,
   Number)".

## La torre numérica

class numbers.Complex

   Las subclases de este tipo describen números complejos e incluyen
   las operaciones que funcionan en el tipo "complex" integrado. Estos
   son: conversiones a "complex" y "bool", "real", "imag", "+", "-",
   "*", "/", "**", "abs()", "conjugate()", "==" y "!=". Todos excepto
   "-" y "!=" son abstractos.

   real

      Abstracto. Recupera el componente real de este número.

   imag

      Abstracto. Recupera el componente imaginario de este número.

   abstractmethod conjugate()

      Abstracto. Retorna el complejo conjugado. Por ejemplo,
      "(1+3j).conjugate() == (1-3j)".

class numbers.Real

   To "Complex", "Real" adds the operations that work on real numbers.

   En resumen, estos son: conversiones a "float", "math.trunc()",
   "round()", "math.floor()", "math.ceil()", "divmod()", "//", "%",
   "<", "<=", ">", y ">=".

   *Real* también proporciona valores predeterminados para
   "complex()", "real", "imag", y "conjugate()".

class numbers.Rational

   Subtipos "Real" y agrega propiedades de "numerator" y
   "denominator". También proporciona un valor predeterminado para
   "float()".

   Los valores del "numerator" y del "denominator" deben ser
   instancias de "Integral" y deben estar en términos mínimos con
   "denominator" positivo.

   numerator

      Abstract.  The numerator of this rational number.

   denominator

      Abstract.  The denominator of this rational number.

class numbers.Integral

   Subtipos "Rational" y agrega una conversión a "int". Proporciona
   valores predeterminados para "float()", "numerator" y
   "denominator". Agrega métodos abstractos para "pow()" con
   operaciones de módulo y cadena de bits: "<<", ">>", "&", "^", "|",
   "~".

## Notes for type implementers

Implementers should be careful to make equal numbers equal and hash
them to the same values. This may be subtle if there are two different
extensions of the real numbers. See also Calculo del hash de tipos
numéricos.

### Agregar más *ABCs* numéricos

Por supuesto, hay más *ABCs* posibles para los números, y esto sería
una jerarquía deficiente si se excluye la posibilidad de añadirlos.
Puede usar "MyFoo" entre "Complex" y "Real" así:

   class MyFoo(Complex): ...
   MyFoo.register(Real)

### Implementar operaciones aritméticas

We want to implement the arithmetic operations so that mixed-mode
operations either call an implementation whose author knew about the
types of both arguments, or convert both to the nearest built in type
and do the operation there. For subtypes of "Integral", this means
that "__add__()" and "__radd__()" should be defined as:

   class MyIntegral(Integral):

       def __add__(self, other):
           if isinstance(other, MyIntegral):
               return do_my_adding_stuff(self, other)
           elif isinstance(other, OtherTypeIKnowAbout):
               return do_my_other_adding_stuff(self, other)
           else:
               return NotImplemented

       def __radd__(self, other):
           if isinstance(other, MyIntegral):
               return do_my_adding_stuff(other, self)
           elif isinstance(other, OtherTypeIKnowAbout):
               return do_my_other_adding_stuff(other, self)
           elif isinstance(other, Integral):
               return int(other) + int(self)
           elif isinstance(other, Real):
               return float(other) + float(self)
           elif isinstance(other, Complex):
               return complex(other) + complex(self)
           else:
               return NotImplemented

Hay 5 casos diferentes para una operación de tipo mixto en subclases
de "Complex". Se explicará  todo el código anterior que no se refiere
a "MyIntegral" y "OtherTypeIKnowAbout" como "repetitivo". "a" será una
instancia de "A", que es un subtipo de "Complex" ("a: A <: Complex"),
y "b : B <: Complex". Consideraré "a + b":

1. If "A" defines an "__add__()" which accepts "b", all is well.

2. If "A" falls back to the boilerplate code, and it were to return a
   value from "__add__()", we'd miss the possibility that "B" defines
   a more intelligent "__radd__()", so the boilerplate should return
   "NotImplemented" from "__add__()". (Or "A" may not implement
   "__add__()" at all.)

3. Then "B"'s "__radd__()" gets a chance. If it accepts "a", all is
   well.

4. Si se vuelve a caer en el código repetitivo, no hay más posibles
   métodos para probar, por lo que acá debería vivir la implementación
   predeterminada.

5. Si "B <: A", Python probara "B.__radd__" antes que "A.__add__".
   Esto está bien, porque se implementó con conocimiento de "A", por
   lo que puede manejar instancias antes de delegar un "Complex".

If "A <: Complex" and "B <: Real" without sharing any other knowledge,
then the appropriate shared operation is the one involving the built
in "complex", and both "__radd__()" s land there, so "a+b == b+a".

Dado que la mayoría de las operaciones en un tipo determinado serán
muy similares, puede ser útil definir una función auxiliar que genere
las instancias *forward* y *reverse* de cualquier operador dado. Por
ejemplo, "fractions.Fraction" así:

   def _operator_fallbacks(monomorphic_operator, fallback_operator):
       def forward(a, b):
           if isinstance(b, (int, Fraction)):
               return monomorphic_operator(a, b)
           elif isinstance(b, float):
               return fallback_operator(float(a), b)
           elif isinstance(b, complex):
               return fallback_operator(complex(a), b)
           else:
               return NotImplemented
       forward.__name__ = '__' + fallback_operator.__name__ + '__'
       forward.__doc__ = monomorphic_operator.__doc__

       def reverse(b, a):
           if isinstance(a, Rational):
               # Includes ints.
               return monomorphic_operator(a, b)
           elif isinstance(a, Real):
               return fallback_operator(float(a), float(b))
           elif isinstance(a, Complex):
               return fallback_operator(complex(a), complex(b))
           else:
               return NotImplemented
       reverse.__name__ = '__r' + fallback_operator.__name__ + '__'
       reverse.__doc__ = monomorphic_operator.__doc__

       return forward, reverse

   def _add(a, b):
       """a + b"""
       return Fraction(a.numerator * b.denominator +
                       b.numerator * a.denominator,
                       a.denominator * b.denominator)

   __add__, __radd__ = _operator_fallbacks(_add, operator.add)

   # ...
