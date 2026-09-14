---
title: Objetos de arreglos de bytes (*bytearrays*)
source_url: https://docs.python.org/es/3
source_path: c-api/bytearray.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 90
---

# Objetos de arreglos de bytes (*bytearrays*)

type PyByteArrayObject

   Este subtipo de "PyObject" representa un objeto arreglo de bytes de
   Python.

PyTypeObject PyByteArray_Type
    * Part of the Stable ABI.*

   Esta instancia de "PyTypeObject" representa el tipo arreglo de
   bytes de Python; es el mismo objeto que "bytearray" en la capa de
   Python.

## Macros de verificación de tipos

int PyByteArray_Check(PyObject *o)

   Retorna verdadero si el objeto *o* es un objeto de arreglo de bytes
   o una instancia de un subtipo del tipo arreglo de bytes. Esta
   función siempre finaliza con éxito.

int PyByteArray_CheckExact(PyObject *o)

   Retorna verdadero si el objeto *o* es un objeto de arreglo de
   bytes, pero no una instancia de un subtipo del tipo arreglo de
   bytes. Esta función siempre finaliza con éxito.

## Funciones API directas

PyObject *PyByteArray_FromObject(PyObject *o)
    *Return value: New reference.** Part of the Stable ABI.** Thread
   safety: Safe for concurrent use on the same object.*

   Retorna un nuevo objeto de arreglo de bytes de cualquier objeto,
   *o*, que implementa el buffer protocol.

   Al fallar, retorna "NULL" con una excepción asignada.

   Nota:

     If the object implements the buffer protocol, then the buffer
     must not be mutated while the bytearray object is being created.

PyObject *PyByteArray_FromStringAndSize(const char *string, Py_ssize_t len)
    *Return value: New reference.** Part of the Stable ABI.** Thread
   safety: Atomic.*

   Crea un nuevo objeto de arreglo de bytes a partir de *string* y su
   longitud, *len*.

   Al fallar, retorna "NULL" con una excepción asignada.

PyObject *PyByteArray_Concat(PyObject *a, PyObject *b)
    *Return value: New reference.** Part of the Stable ABI.** Thread
   safety: Safe for concurrent use on the same object.*

   Une los arreglos de bytes (*bytearrays*) *a* y *b* y retorna un
   nuevo arreglo de bytes (*bytearray*) con el resultado.

   Al fallar, retorna "NULL" con una excepción asignada.

   Nota:

     If the object implements the buffer protocol, then the buffer
     must not be mutated while the bytearray object is being created.

Py_ssize_t PyByteArray_Size(PyObject *bytearray)
    * Part of the Stable ABI.** Thread safety: Atomic.*

   Retorna el tamaño de *bytearray* después de buscar un puntero
   "NULL".

char *PyByteArray_AsString(PyObject *bytearray)
    * Part of the Stable ABI.** Thread safety: Safe to call from
   multiple threads with external synchronization only.*

   Retorna el contenido de *bytearray* como un arreglo de caracteres
   después de verificar un puntero "NULL". El arreglo retornado
   siempre tiene un byte nulo adicional agregado.

   Nota:

     It is not thread-safe to mutate the bytearray object while using
     the returned char array.

int PyByteArray_Resize(PyObject *bytearray, Py_ssize_t len)
    * Part of the Stable ABI.*

   Resize the internal buffer of *bytearray* to *len*. Failure is a
   "-1" return with an exception set.

   Distinto en la versión 3.14: A negative *len* will now result in an
   exception being set and -1 returned.

## Macros

Estos macros intercambian seguridad por velocidad y no comprueban
punteros.

char *PyByteArray_AS_STRING(PyObject *bytearray)
    * Thread safety: Safe to call from multiple threads with external
   synchronization only.*

   Similar a "PyByteArray_AsString()", pero sin comprobación de
   errores.

   Nota:

     It is not thread-safe to mutate the bytearray object while using
     the returned char array.

Py_ssize_t PyByteArray_GET_SIZE(PyObject *bytearray)
    * Thread safety: Atomic.*

   Similar a "PyByteArray_Size()", pero sin comprobación de errores.
