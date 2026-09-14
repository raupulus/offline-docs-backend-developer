---
title: Objetos de números complejos
source_url: https://docs.python.org/es/3
source_path: c-api/complex.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 160
---

# Objetos de números complejos

Los objetos de números complejos de Python se implementan como dos
tipos distintos cuando se ven desde la API de C: uno es el objeto de
Python expuesto a los programas de Python, y el otro es una estructura
en C que representa el valor de número complejo real. La API
proporciona funciones para trabajar con ambos.

## Números complejos como estructuras C

Tenga en cuenta que las funciones que aceptan estas estructuras como
parámetros y las retornan como resultados lo hacen *por valor* en
lugar de desreferenciarlas a través de punteros. Esto es consistente
en toda la API.

type Py_complex

   La estructura C que corresponde a la porción de valor de un objeto
   de número complejo de Python. La mayoría de las funciones para
   tratar con objetos de números complejos utilizan estructuras de
   este tipo como valores de entrada o salida, según corresponda.

   double real
   double imag

   La estructura se define como:

      typedef struct {
          double real;
          double imag;
      } Py_complex;

Py_complex _Py_c_sum(Py_complex left, Py_complex right)

   Retorna la suma de dos números complejos, utilizando la
   representación C "Py_complex".

Py_complex _Py_c_diff(Py_complex left, Py_complex right)

   Retorna la diferencia entre dos números complejos, usando la
   representación C "Py_complex".

Py_complex _Py_c_neg(Py_complex num)

   Retorna la negación del número complejo *num*, utilizando la
   representación C "Py_complex".

Py_complex _Py_c_prod(Py_complex left, Py_complex right)

   Retorna el producto de dos números complejos, usando la
   representación C "Py_complex".

Py_complex _Py_c_quot(Py_complex dividend, Py_complex divisor)

   Retorna el cociente de dos números complejos, utilizando la
   representación C "Py_complex".

   Si *divisor* es nulo, este método retorna cero y establece "errno"
   en "EDOM".

Py_complex _Py_c_pow(Py_complex num, Py_complex exp)

   Retorna la exponenciación de *num* por *exp*, utilizando la
   representación C "Py_complex".

   Si *num* es nulo y *exp* no es un número real positivo, este método
   retorna cero y establece "errno" a "EDOM".

   Set "errno" to "ERANGE" on overflows.

## Números complejos como objetos de Python

type PyComplexObject

   Este subtipo de "PyObject" representa un objeto de número complejo
   de Python.

PyTypeObject PyComplex_Type
    * Part of the Stable ABI.*

   Esta instancia de "PyTypeObject" representa el tipo de número
   complejo de Python. Es el mismo objeto que "complex" en la capa de
   Python.

int PyComplex_Check(PyObject *p)

   Retorna verdadero si su argumento es un "PyComplexObject" o un
   subtipo de "PyComplexObject". Esta función siempre finaliza con
   éxito.

int PyComplex_CheckExact(PyObject *p)

   Retorna verdadero si su argumento es un "PyComplexObject", pero no
   un subtipo de "PyComplexObject". Esta función siempre finaliza con
   éxito.

PyObject *PyComplex_FromCComplex(Py_complex v)
    *Return value: New reference.*

   Crea un nuevo objeto de número complejo de Python a partir de un
   valor C "Py_complex". Retorna "NULL" con una excepción establecida
   en caso de error.

PyObject *PyComplex_FromDoubles(double real, double imag)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna un nuevo objeto "PyComplexObject" de *real* e *imag*.
   Retorna "NULL" con una excepción establecida en caso de error.

double PyComplex_RealAsDouble(PyObject *op)
    * Part of the Stable ABI.*

   Retorna la parte real de *op* como double en C.

   Si *op* no es un objeto de número complejo de Python pero tiene un
   método "__complex__()", primero se llamará a este método para
   convertir *op* en un objeto de número complejo de Python. Si
   "__complex__()" no está definido, entonces recurre a
   "PyFloat_AsDouble()" y retorna su resultado.

   En caso de falla, este método retorna "-1.0" con una excepción
   establecida, por lo que se debe llamar "PyErr_Occurred()" para
   verificar si hay errores.

   Distinto en la versión 3.13: Use "__complex__()" si está
   disponible.

double PyComplex_ImagAsDouble(PyObject *op)
    * Part of the Stable ABI.*

   Retorna la parte imaginaria de *op* como un double de C.

   Si *op* no es un objeto de número complejo de Python pero tiene un
   método "__complex__()", primero se llamará a este método para
   convertir *op* en un objeto de número complejo de Python. Si
   "__complex__()" no está definido, entonces recurre a
   "PyFloat_AsDouble()" y retorna "0.0" en caso de éxito.

   En caso de falla, este método retorna "-1.0" con una excepción
   establecida, por lo que se debe llamar "PyErr_Occurred()" para
   verificar si hay errores.

   Distinto en la versión 3.13: Use "__complex__()" si está
   disponible.

Py_complex PyComplex_AsCComplex(PyObject *op)

   Retorna el valor "Py_complex" del número complejo *op*.

   Si *op* no es un objeto de número complejo de Python pero tiene un
   método "__complex__()", primero se llamará a este método para
   convertir *op* en un objeto de número complejo de Python. Si
   "__complex__()" no está definido, entonces recurre a "__float__()".
   Si "__float__()" no está definido, entonces recurre a
   "__index__()".

   En caso de falla, este método retorna "Py_complex" con "real"
   establecido en "-1.0" y con una excepción establecida, por lo que
   se debe llamar a "PyErr_Occurred()" para verificar si hay errores.

   Distinto en la versión 3.8: Use "__index__()" si está disponible.
