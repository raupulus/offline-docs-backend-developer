---
title: Protocolo de números
source_url: https://docs.python.org/es/3
source_path: c-api/number.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 530
---

# Protocolo de números

int PyNumber_Check(PyObject *o)
    * Part of the Stable ABI.*

   Retorna "1" si el objeto *o* proporciona protocolos numéricos, y
   falso en caso contrario. Esta función siempre finaliza con éxito.

   Distinto en la versión 3.8: Retorna "1" si *o* es un índice entero.

PyObject *PyNumber_Add(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el resultado de agregar *o1* y *o2*, o "NULL" en caso de
   falla. Este es el equivalente de la expresión de Python "o1 + o2".

PyObject *PyNumber_Subtract(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el resultado de restar *o2* de *o1*, o "NULL" en caso de
   falla. Este es el equivalente de la expresión de Python "o1 - o2".

PyObject *PyNumber_Multiply(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el resultado de multiplicar *o1* y *o2*, o "NULL" en caso
   de error. Este es el equivalente de la expresión de Python "o1 *
   o2".

PyObject *PyNumber_MatrixMultiply(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.7.*

   Retorna el resultado de la multiplicación de matrices en *o1* y
   *o2*, o "NULL" en caso de falla. Este es el equivalente de la
   expresión de Python "o1 @ o2".

   Added in version 3.5.

PyObject *PyNumber_FloorDivide(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el cociente de la división entera a la baja entre *o1* y
   *o2*, o "NULL" en caso de error. Este es el equivalente de la
   expresión de Python "o1 // o2".

PyObject *PyNumber_TrueDivide(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna una aproximación razonable para el valor matemático de *o1*
   dividido por *o2* o "NULL" en caso de falla. El valor de retorno es
   "aproximado" porque los números binarios de punto flotante son
   aproximados; No es posible representar todos los números reales en
   base dos. Esta función puede retornar un valor de punto flotante
   cuando se pasan dos enteros. Es equivalente a la expresión de
   Python "o1 / o2".

PyObject *PyNumber_Remainder(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el resto de la división entera a la baja entre *o1* y *o2*,
   o "NULL" en caso de error. Este es el equivalente de la expresión
   de Python "o1 % o2".

PyObject *PyNumber_Divmod(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI.*

   Vea la función incorporada "divmod()". Retorna "NULL" en caso de
   falla. Este es el equivalente de la expresión de Python "divmod
   (o1, o2)".

PyObject *PyNumber_Power(PyObject *o1, PyObject *o2, PyObject *o3)
    *Return value: New reference.** Part of the Stable ABI.*

   Consulte la función incorporada "pow()". Retorna "NULL" en caso de
   falla. Este es el equivalente de la expresión de Python "pow(o1,
   o2, o3)", donde *o3* es opcional. Si se ignora *o3*, pase "Py_None"
   en su lugar (pasar "NULL" por *o3* provocaría un acceso ilegal a la
   memoria).

PyObject *PyNumber_Negative(PyObject *o)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna la negación de *o* en caso de éxito o "NULL" en caso de
   error. Este es el equivalente de la expresión de Python "-o".

PyObject *PyNumber_Positive(PyObject *o)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna *o* en caso de éxito o "NULL" en caso de error. Este es el
   equivalente de la expresión de Python "+o".

PyObject *PyNumber_Absolute(PyObject *o)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el valor absoluto de *o* o "NULL" en caso de error. Este es
   el equivalente de la expresión de Python "abs(o)".

PyObject *PyNumber_Invert(PyObject *o)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna la negación bit a bit de *o* en caso de éxito o "NULL" en
   caso de error. Este es el equivalente de la expresión de Python
   "~o".

PyObject *PyNumber_Lshift(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el resultado del desplazamiento a la izquierda *o1* por
   *o2* en caso de éxito o "NULL" en caso de error. Este es el
   equivalente de la expresión de Python "o1 << o2".

PyObject *PyNumber_Rshift(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el resultado del desplazamiento a la derecha *o1* por *o2*
   en caso de éxito o "NULL" en caso de error. Este es el equivalente
   de la expresión de Python "o1 >> o2".

PyObject *PyNumber_And(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el "bit a bit y" (*bitwise and*) de *o1* y *o2* en caso de
   éxito y "NULL" en caso de error. Este es el equivalente de la
   expresión de Python "o1 & o2".

PyObject *PyNumber_Xor(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el "bit a bit o exclusivo" (*bitwise exclusive or*) de *o1*
   por *o2* en caso de éxito, o "NULL" en caso de error. Este es el
   equivalente de la expresión de Python "o1 ^ o2".

PyObject *PyNumber_Or(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el "bit a bit o" (*bitwise or*) de *o1* y *o2* en caso de
   éxito, o "NULL" en caso de error. Este es el equivalente de la
   expresión de Python "o1 | o2".

PyObject *PyNumber_InPlaceAdd(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el resultado de agregar *o1* y *o2*, o "NULL" en caso de
   falla. La operación se realiza en su lugar (*in-place*) cuando *o1*
   lo admite. Este es el equivalente de la declaración de Python "o1
   += o2".

PyObject *PyNumber_InPlaceSubtract(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el resultado de restar *o2* de *o1*, o "NULL" en caso de
   falla. La operación se realiza en su lugar (*in-place*) cuando *o1*
   lo admite. Este es el equivalente de la declaración de Python "o1
   -= o2".

PyObject *PyNumber_InPlaceMultiply(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el resultado de multiplicar *o1* y *o2*, o "NULL" en caso
   de error. La operación se realiza en su lugar (*in-place*) cuando
   *o1* lo admite. Este es el equivalente de la declaración de Python
   "o1 *= o2".

PyObject *PyNumber_InPlaceMatrixMultiply(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.7.*

   Retorna el resultado de la multiplicación de matrices en *o1* y
   *o2*, o "NULL" en caso de falla. La operación se realiza en su
   lugar (*in-place*) cuando *o1* lo admite. Este es el equivalente de
   la declaración de Python "o1 @= o2".

   Added in version 3.5.

PyObject *PyNumber_InPlaceFloorDivide(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el cociente de la división entera a la baja entre *o1* y
   *o2*, o "NULL" en caso de error. La operación se realiza in situ
   (*in-place*) cuando *o1* lo admite. Es el equivalente de la
   sentencia de Python "o1 //= o2".

PyObject *PyNumber_InPlaceTrueDivide(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna una aproximación razonable para el valor matemático de *o1*
   dividido por *o2* o "NULL" en caso de falla. El valor de retorno es
   "aproximado" porque los números binarios de coma flotante son
   aproximados; No es posible representar todos los números reales en
   base dos. Esta función puede retornar un valor de punto flotante
   cuando se pasan dos enteros. La operación se realiza en su lugar
   (*in-place*) cuando *o1* lo admite.

PyObject *PyNumber_InPlaceRemainder(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el resto de dividir *o1* entre *o2* o "NULL" en caso de
   error. La operación se realiza en su lugar (*in-place*) cuando *o1*
   lo admite. Este es el equivalente de la declaración de Python "o1%=
   o2".

PyObject *PyNumber_InPlacePower(PyObject *o1, PyObject *o2, PyObject *o3)
    *Return value: New reference.** Part of the Stable ABI.*

   Consulte la función incorporada "pow()". Retorna "NULL" en caso de
   falla. La operación se realiza en su lugar (*in-place*) cuando *o1*
   lo admite. Este es el equivalente de la declaración de Python "o1
   **= o2" cuando *o3* es "Py_None", o una variante en su lugar (*in-
   place*) de "pow (o1, o2, o3)" de lo contrario. Si se ignora *o3*,
   pase "Py_None" en su lugar (pasar "NULL" para *o3* provocaría un
   acceso ilegal a la memoria).

PyObject *PyNumber_InPlaceLshift(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el resultado del desplazamiento a la izquierda *o1* por
   *o2* en caso de éxito o "NULL" en caso de error. La operación se
   realiza en su sitio (*in-place*) cuando *o1* lo admite. Este es el
   equivalente de la declaración de Python "o1 <<= o2".

PyObject *PyNumber_InPlaceRshift(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el resultado del desplazamiento a la derecha *o1* por *o2*
   en caso de éxito o "NULL" en caso de error. La operación se realiza
   en su lugar (*in-place*) cuando *o1* lo admite. Este es el
   equivalente de la declaración de Python "o1 >>= o2".

PyObject *PyNumber_InPlaceAnd(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el "bit a bit y" (*bitwise and*) de *o1* y *o2* en caso de
   éxito y "NULL" en caso de error. La operación se realiza en su
   lugar (*in-place*) cuando *o1* lo admite. Este es el equivalente de
   la declaración de Python "o1 &= o2".

PyObject *PyNumber_InPlaceXor(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el "bit a bit o exclusivo" (*bitwise exclusive or*) de *o1*
   por *o2* en caso de éxito, o "NULL" en caso de error. La operación
   se realiza en su lugar (*in-place*) cuando *o1* lo admite. Este es
   el equivalente de la declaración de Python "o1 ^= o2".

PyObject *PyNumber_InPlaceOr(PyObject *o1, PyObject *o2)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el "bit a bit o" (*bitwise or*) de *o1* y *o2* en caso de
   éxito, o "NULL" en caso de error. La operación se realiza en su
   lugar *in-place* cuando *o1* lo admite. Este es el equivalente de
   la declaración de Python "o1 |= o2".

PyObject *PyNumber_Long(PyObject *o)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el *o* convertido a un objeto entero en caso de éxito, o
   "NULL" en caso de error. Este es el equivalente de la expresión de
   Python "int(o)".

PyObject *PyNumber_Float(PyObject *o)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el *o* convertido a un objeto flotante en caso de éxito o
   "NULL" en caso de error. Este es el equivalente de la expresión de
   Python "float(o)".

PyObject *PyNumber_Index(PyObject *o)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el *o* convertido aun entero de Python (*int*) en caso de
   éxito o "NULL" con una excepción "TypeError" lanzada en caso de
   error.

   Distinto en la versión 3.10: El resultado siempre tiene el tipo
   exacto "int". Anteriormente, el resultado podía ser una instancia
   de una subclase de "int".

PyObject *PyNumber_ToBase(PyObject *n, int base)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el entero *n* convertido a base *base* como una cadena de
   caracteres. El argumento *base* debe ser uno de 2, 8, 10 o 16. Para
   la base 2, 8 o 16, la cadena retornada está prefijada con un
   marcador base de "'0b'"', "'0o'" o "'0x'", respectivamente. Si *n*
   no es un entero (*int*) Python, primero se convierte con
   "PyNumber_Index()".

Py_ssize_t PyNumber_AsSsize_t(PyObject *o, PyObject *exc)
    * Part of the Stable ABI.*

   Retorna *o* convertido a un valor "Py_ssize_t" si *o* puede
   interpretarse como un entero. Si la llamada falla, se lanza una
   excepción y se retorna "-1".

   Si *o* puede convertirse a un entero de Python pero el intento de
   convertirlo a un valor "Py_ssize_t" lanzaría un "OverflowError",
   entonces el argumento *exc* es el tipo de excepción que se lanzará
   (normalmente "IndexError" o "OverflowError").  Si *exc* es "NULL",
   la excepción se borra y el valor se recorta a "PY_SSIZE_T_MIN" para
   un entero negativo o a "PY_SSIZE_T_MAX" para un entero positivo.

int PyIndex_Check(PyObject *o)
    * Part of the Stable ABI since version 3.8.*

   Retorna "1" si *o* es un entero índice (tiene la ranura "nb_index"
   de la estructura "tp_as_number" rellenada), y "0" en caso
   contrario. Esta función siempre finaliza con éxito.
