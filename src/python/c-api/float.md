---
title: Floating-Point Objects
source_url: https://docs.python.org/es/3
source_path: c-api/float.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 280
---

# Floating-Point Objects

type PyFloatObject

   This subtype of "PyObject" represents a Python floating-point
   object.

PyTypeObject PyFloat_Type
    * Part of the Stable ABI.*

   This instance of "PyTypeObject" represents the Python floating-
   point type.  This is the same object as "float" in the Python
   layer.

int PyFloat_Check(PyObject *p)

   Retorna verdadero si su argumento es un "PyFloatObject" o un
   subtipo de "PyFloatObject". Esta función siempre finaliza con
   éxito.

int PyFloat_CheckExact(PyObject *p)

   Retorna verdadero si su argumento es un "PyFloatObject", pero no un
   subtipo de "PyFloatObject". Esta función siempre finaliza con
   éxito.

PyObject *PyFloat_FromString(PyObject *str)
    *Return value: New reference.** Part of the Stable ABI.*

   Crea un objeto "PyFloatObject" basado en la cadena de caracteres en
   *str*, o "NULL" en caso de error.

PyObject *PyFloat_FromDouble(double v)
    *Return value: New reference.** Part of the Stable ABI.*

   Crea un objeto "PyFloatObject" a partir de *v*, o "NULL" en caso de
   error.

double PyFloat_AsDouble(PyObject *pyfloat)
    * Part of the Stable ABI.*

   Return a C double representation of the contents of *pyfloat*.  If
   *pyfloat* is not a Python floating-point object but has a
   "__float__()" method, this method will first be called to convert
   *pyfloat* into a float. If "__float__()" is not defined then it
   falls back to "__index__()". This method returns "-1.0" upon
   failure, so one should call "PyErr_Occurred()" to check for errors.

   Distinto en la versión 3.8: Utilice "__index__()" si está
   disponible.

double PyFloat_AS_DOUBLE(PyObject *pyfloat)

   Retorna una representación C double de los contenidos de *pyfloat*,
   pero sin verificación de errores.

PyObject *PyFloat_GetInfo(void)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna una instancia de *structseq* que contiene información sobre
   la precisión, los valores mínimos y máximos de un flotante. Es un
   contenedor reducido alrededor del archivo de encabezado "float.h".

double PyFloat_GetMax()
    * Part of the Stable ABI.*

   Retorna el máximo flotante finito representable *DBL_MAX* como C
   double.

double PyFloat_GetMin()
    * Part of the Stable ABI.*

   Retorna el flotante positivo normalizado mínimo *DBL_MIN* como C
   double.

Py_INFINITY

   This macro expands to a constant expression of type double, that
   represents the positive infinity.

   On most platforms, this is equivalent to the "INFINITY" macro from
   the C11 standard "<math.h>" header.

Py_NAN

   This macro expands to a constant expression of type double, that
   represents a quiet not-a-number (qNaN) value.

   On most platforms, this is equivalent to the "NAN" macro from the
   C11 standard "<math.h>" header.

Py_HUGE_VAL

   Equivalent to "INFINITY".

   Obsoleto desde la versión 3.14: The macro is *soft deprecated*.

Py_MATH_E

   The definition (accurate for a double type) of the "math.e"
   constant.

Py_MATH_El

   High precision (long double) definition of "e" constant.

Py_MATH_PI

   The definition (accurate for a double type) of the "math.pi"
   constant.

Py_MATH_PIl

   High precision (long double) definition of "pi" constant.

Py_MATH_TAU

   The definition (accurate for a double type) of the "math.tau"
   constant.

   Added in version 3.6.

Py_RETURN_NAN

   Return "math.nan" from a function.

   On most platforms, this is equivalent to "return
   PyFloat_FromDouble(NAN)".

Py_RETURN_INF(sign)

   Return "math.inf" or "-math.inf" from a function, depending on the
   sign of *sign*.

   On most platforms, this is equivalent to the following:

      return PyFloat_FromDouble(copysign(INFINITY, sign));

Py_IS_FINITE(X)

   Return "1" if the given floating-point number *X* is finite, that
   is, it is normal, subnormal or zero, but not infinite or NaN.
   Return "0" otherwise.

   Obsoleto desde la versión 3.14: The macro is *soft deprecated*.
   Use "isfinite" instead.

Py_IS_INFINITY(X)

   Return "1" if the given floating-point number *X* is positive or
   negative infinity.  Return "0" otherwise.

   Obsoleto desde la versión 3.14: The macro is *soft deprecated*.
   Use "isinf" instead.

Py_IS_NAN(X)

   Return "1" if the given floating-point number *X* is a not-a-number
   (NaN) value.  Return "0" otherwise.

   Obsoleto desde la versión 3.14: The macro is *soft deprecated*.
   Use "isnan" instead.

## Funciones de empaquetado y desempaquetado

Las funciones de empaquetar y desempaquetar proporcionan una manera
eficiente e independiente de la plataforma para almacenar valores de
coma flotante como cadenas de bytes. Las rutinas Pack producen una
cadena de bytes a partir de un C double, y las rutinas Desempaquetar
producen un C double a partir de dicha cadena de bytes. El sufijo (2,
4 u 8) especifica el número de bytes en la cadena de bytes.

En plataformas que parecen usar formatos IEEE 754, estas funciones
actúan copiando los bits. En otras plataformas, el formato 2-byte es
idéntico al formato de media precision IEEE 754 binary16, el formato
de 4-byte (32 bits) es idéntico al formato de precisión simple binario
IEEE 754 binary32, y el formato de 8-byte al formato de doble
precisión binario IEEE 754 binary64, aunque el empaquetado de INFs y
NaNs (si existen en la plataforma) no se maneja correctamente,
mientras que intentar desempaquetar una cadena de bytes que contenga
un IEEE INF o NaN generará una excepción.

Note that NaN type may not be preserved on IEEE platforms (signaling
NaNs become quiet NaNs), for example on x86 systems in 32-bit mode.

En plataformas que no son IEEE con más precisión, o mayor rango
dinámico, que el IEEE 754 admite, no se pueden empaquetar todos los
valores; en plataformas que no son IEEE con menos precisión o con un
rango dinámico más pequeño, no se pueden desempaquetar todos los
valores. Lo que sucede en tales casos es en parte accidental
(desafortunadamente).

Added in version 3.11.

### Funciones de Empaquetado

The pack routines write 2, 4 or 8 bytes, starting at *p*. *le* is an
int argument, non-zero if you want the bytes string in little-endian
format (exponent last, at "p+1", "p+3", or "p+6" and "p+7"), zero if
you want big-endian format (exponent first, at *p*). The
"PY_BIG_ENDIAN" constant can be used to use the native endian: it is
equal to "1" on big endian processor, or "0" on little endian
processor.

Valor retornado: "0" si todo está bien, "-1" si hay error (y se
establece una excepción, probablemente "OverflowError").

Hay dos problemas en plataformas que no son IEEE:

* Lo que esto hace es indefinido si *x* es un NaN o infinito.

* "-0.0" and "+0.0" produce la misma cadena de bytes.

int PyFloat_Pack2(double x, char *p, int le)

   Empaquete un C doble como el formato de media precisión IEEE 754
   binary16.

int PyFloat_Pack4(double x, char *p, int le)

   Empaque un C doble como el formato de precisión simple IEEE 754
   binary32.

int PyFloat_Pack8(double x, char *p, int le)

   Empaque un C doble como el formato de doble precisión IEEE 754
   binary64.

### Funciones de Desempaquetado

Las rutinas de desempaquetado leen 2, 4 u 8 bytes, comenzando en *p*.
*le* es un argumento int , distinto de cero si la cadena bytes está en
formato little-endian (exponente al final, en "p+1", "p+3" o "p+6" y
"p+7"), cero si está en formato big-endian (exponente primero, en
*p*). La constante "PY_BIG_ENDIAN" se puede usar para utilizar el
endian nativo: es igual a "1" en un procesador big endian, o "0" en un
procesador little-endian.

Valor retornado: Doble desempaquetado. Si hay error, "-1.0" y
"PyErr_Occurred()" es verdadero (y se establece una excepción,
probablemente "OverflowError").

Hay que tener en cuenta que en una plataforma que no sea IEEE, esto se
negará a desempaquetar una cadena de bytes que representa un NaN o
infinito.

double PyFloat_Unpack2(const char *p, int le)

   Descomprima el formato de media precisión IEEE 754 binary16 como un
   doble C.

double PyFloat_Unpack4(const char *p, int le)

   Descomprima el formato de precisión simple IEEE 754 binary32 como
   un doble C.

double PyFloat_Unpack8(const char *p, int le)

   Descomprima el formato de doble precisión IEEE 754 binary64 como un
   doble C.
