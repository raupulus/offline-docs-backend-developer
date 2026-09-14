---
title: Objetos iteradores
source_url: https://docs.python.org/es/3
source_path: c-api/iterator.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 410
---

# Objetos iteradores

Python proporciona dos objetos iteradores de propósito general. El
primero, un iterador de secuencia, funciona con una secuencia
arbitraria que admite el método "__getitem__()". El segundo funciona
con un objeto invocable y un valor centinela, llamando al invocable
para cada elemento en la secuencia y finalizando la iteración cuando
se retorna el valor centinela.

PyTypeObject PySeqIter_Type
    * Part of the Stable ABI.*

   Objeto tipo para objetos iteradores retornados por
   "PySeqIter_New()" y la forma de un argumento de la función
   incorporada "iter()" para los tipos de secuencia incorporados.

int PySeqIter_Check(PyObject *op)

   Retorna verdadero si el tipo de *op* es "PySeqIter_Type". Esta
   función siempre finaliza con éxito.

PyObject *PySeqIter_New(PyObject *seq)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna un iterador que funciona con un objeto de secuencia
   general, *seq*. La iteración termina cuando la secuencia lanza
   "IndexError" para la operación de suscripción.

PyTypeObject PyCallIter_Type
    * Part of the Stable ABI.*

   Objeto tipo para los objetos iteradores retornados por
   "PyCallIter_New()" y la forma de dos argumentos de la función
   incorporada "iter()".

int PyCallIter_Check(PyObject *op)

   Retorna verdadero si el tipo de *op* es "PyCallIter_Type". Esta
   función siempre finaliza con éxito.

PyObject *PyCallIter_New(PyObject *callable, PyObject *sentinel)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna un nuevo iterador. El primer parámetro, *callable*, puede
   ser cualquier objeto invocable de Python que se pueda invocar sin
   parámetros; cada llamada debe retornar el siguiente elemento en la
   iteración. Cuando *callable* retorna un valor igual a *sentinel*,
   la iteración finalizará.

## Range Objects

PyTypeObject PyRange_Type
    * Part of the Stable ABI.*

   The type object for "range" objects.

int PyRange_Check(PyObject *o)

   Return true if the object *o* is an instance of a "range" object.
   This function always succeeds.

## Builtin Iterator Types

These are built-in iteration types that are included in Python's C
API, but provide no additional functions. They are here for
completeness.

+----------------------------------------------------+----------------------------------------------------+
| C type                                             | Python type                                        |
|====================================================|====================================================|
| PyTypeObject PyEnum_Type  * Part of the Stable     | "enumerate"                                        |
## | ABI.*                                              |                                                    |

| PyTypeObject PyFilter_Type  * Part of the Stable   | "filter"                                           |
## | ABI.*                                              |                                                    |

| PyTypeObject PyMap_Type  * Part of the Stable      | "map"                                              |
## | ABI.*                                              |                                                    |

| PyTypeObject PyReversed_Type  * Part of the Stable | "reversed"                                         |
## | ABI.*                                              |                                                    |

| PyTypeObject PyZip_Type  * Part of the Stable      | "zip"                                              |
## | ABI.*                                              |                                                    |

## Other Iterator Objects

PyTypeObject PyByteArrayIter_Type
    * Part of the Stable ABI.*

PyTypeObject PyBytesIter_Type
    * Part of the Stable ABI.*

PyTypeObject PyListIter_Type
    * Part of the Stable ABI.*

PyTypeObject PyListRevIter_Type
    * Part of the Stable ABI.*

PyTypeObject PySetIter_Type
    * Part of the Stable ABI.*

PyTypeObject PyTupleIter_Type
    * Part of the Stable ABI.*

PyTypeObject PyRangeIter_Type
    * Part of the Stable ABI.*

PyTypeObject PyLongRangeIter_Type
    * Part of the Stable ABI.*

PyTypeObject PyDictIterKey_Type
    * Part of the Stable ABI.*

PyTypeObject PyDictRevIterKey_Type
    * Part of the Stable ABI since version 3.8.*

PyTypeObject PyDictIterValue_Type
    * Part of the Stable ABI.*

PyTypeObject PyDictRevIterValue_Type
    * Part of the Stable ABI since version 3.8.*

PyTypeObject PyDictIterItem_Type
    * Part of the Stable ABI.*

PyTypeObject PyDictRevIterItem_Type
    * Part of the Stable ABI since version 3.8.*

PyTypeObject PyODictIter_Type

   Type objects for iterators of various built-in objects.

   Do not create instances of these directly; prefer calling
   "PyObject_GetIter()" instead.

   Note that there is no guarantee that a given built-in type uses a
   given iterator type. For example, iterating over "range" will use
   one of two iterator types depending on the size of the range. Other
   types may start using a similar scheme in the future, without
   warning.
