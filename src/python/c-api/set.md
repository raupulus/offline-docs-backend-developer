---
title: Objetos conjunto
source_url: https://docs.python.org/es/3
source_path: c-api/set.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 620
---

# Objetos conjunto

Esta sección detalla la API pública de los objetos "set" y
"frozenset".  Cualquier funcionalidad que no esté listada a
continuación se accede mejor utilizando el protocolo abstracto de
objetos (incluyendo "PyObject_CallMethod()",
"PyObject_RichCompareBool()", "PyObject_Hash()", "PyObject_Repr()",
"PyObject_IsTrue()", "PyObject_Print()", y "PyObject_GetIter()") o el
protocolo numérico abstracto (incluyendo "PyNumber_And()",
"PyNumber_Subtract()", "PyNumber_Or()", "PyNumber_Xor()",
"PyNumber_InPlaceAnd()", "PyNumber_InPlaceSubtract()",
"PyNumber_InPlaceOr()", y "PyNumber_InPlaceXor()").

type PySetObject

   Este subtipo de "PyObject" se utiliza para mantener los datos
   internos de los objetos "set" y "frozenset".  Es como un
   "PyDictObject" en el sentido de que tiene un tamaño fijo para los
   conjuntos pequeños (muy parecido al almacenamiento de tuplas) y
   apuntará a un bloque de memoria separado y de tamaño variable para
   los conjuntos de tamaño medio y grande (muy parecido al
   almacenamiento de listas). Ninguno de los campos de esta estructura
   debe considerarse público y todos están sujetos a cambios.  Todo el
   acceso debe hacerse a través de la API documentada en lugar de
   manipular los valores de la estructura.

PyTypeObject PySet_Type
    * Part of the Stable ABI.*

   Esta es una instancia de "PyTypeObject" que representa el tipo
   Python "set".

PyTypeObject PyFrozenSet_Type
    * Part of the Stable ABI.*

   Esta es una instancia de "PyTypeObject" que representa el tipo
   Python "frozenset".

Los siguientes macros de comprobación de tipos funcionan en punteros a
cualquier objeto de Python. Del mismo modo, las funciones del
constructor funcionan con cualquier objeto Python iterable.

int PySet_Check(PyObject *p)

   Retorna verdadero si *p* es un objeto "set" o una instancia de un
   subtipo. Esta función siempre finaliza con éxito.

int PyFrozenSet_Check(PyObject *p)

   Retorna verdadero si *p* es un objeto "frozenset" o una instancia
   de un subtipo. Esta función siempre finaliza con éxito.

int PyAnySet_Check(PyObject *p)

   Retorna verdadero si *p* es un objeto "set", un objeto "frozenset",
   o una instancia de un subtipo. Esta función siempre finaliza con
   éxito.

int PySet_CheckExact(PyObject *p)

   Retorna verdadero si *p* es un objeto "set" pero no una instancia
   de un subtipo. Esta función siempre finaliza con éxito.

   Added in version 3.10.

int PyAnySet_CheckExact(PyObject *p)

   Retorna verdadero si *p* es un objeto "set" o un objeto "frozenset"
   pero no una instancia de un subtipo. Esta función siempre finaliza
   con éxito.

int PyFrozenSet_CheckExact(PyObject *p)

   Retorna verdadero si *p* es un objeto "frozenset" pero no una
   instancia de un subtipo. Esta función siempre finaliza con éxito.

PyObject *PySet_New(PyObject *iterable)
    *Return value: New reference.** Part of the Stable ABI.** Thread
   safety: Safe for concurrent use on the same object.*

   Retorna un nuevo "set" que contiene objetos retornados por
   *iterable*. El *iterable* puede ser "NULL" para crear un nuevo
   conjunto vacío. Retorna el nuevo conjunto en caso de éxito o "NULL"
   en caso de error. Lanza "TypeError" si *iterable* no es realmente
   iterable. El constructor también es útil para copiar un conjunto
   ("c=set(s)").

   Nota:

     The operation is atomic on *free threading* when *iterable* is a
     "set", "frozenset" or "dict".

PyObject *PyFrozenSet_New(PyObject *iterable)
    *Return value: New reference.** Part of the Stable ABI.** Thread
   safety: Safe for concurrent use on the same object.*

   Retorna un nuevo "frozenset" que contiene objetos retornados por
   *iterable*. El *iterable* puede ser "NULL" para crear un nuevo
   frozenset vacío. Retorna el nuevo conjunto en caso de éxito o
   "NULL" en caso de error. Lanza "TypeError" si *iterable* no es
   realmente iterable.

   Nota:

     The operation is atomic on *free threading* when *iterable* is a
     "set", "frozenset" or "dict".

Las siguientes funciones y macros están disponibles para instancias de
"set" o "frozenset" o instancias de sus subtipos.

Py_ssize_t PySet_Size(PyObject *anyset)
    * Part of the Stable ABI.** Thread safety: Atomic.*

   Retorna la longitud de un objeto "set" o "frozenset". Equivalente a
   "len(anyset)". Lanza un "SystemError" si *anyset* no es "set",
   "frozenset", o una instancia de un subtipo.

Py_ssize_t PySet_GET_SIZE(PyObject *anyset)
    * Thread safety: Atomic.*

   Forma macro de "PySet_Size()" sin comprobación de errores.

int PySet_Contains(PyObject *anyset, PyObject *key)
    * Part of the Stable ABI.** Thread safety: Safe for concurrent use
   on the same object.*

   Retorna "1" si se encuentra, "0" si no se encuentra y "-1" si se
   encuentra un error. A diferencia del método Python
   "__contains__()", esta función no convierte automáticamente
   conjuntos que no son hashable en frozensets temporales. Lanza un
   "TypeError" si la *key* no es hashable. Lanza "SystemError" si
   *anyset* no es un "set", "frozenset", o una instancia de un
   subtipo.

   Nota:

     The operation is atomic on *free threading* when *key* is "str",
     "int", "float", "bool" or "bytes".

int PySet_Add(PyObject *set, PyObject *key)
    * Part of the Stable ABI.** Thread safety: Safe for concurrent use
   on the same object.*

   Añade *key* a una instancia "set".  También funciona con instancias
   de "frozenset" (al igual que "PyTuple_SetItem()" puede usarse para
   rellenar los valores de nuevos frozensets antes de que sean
   expuestos a otro código).  Retorna "0" en caso de éxito o "-1" en
   caso de fallo. Lanza un error "TypeError" si la *key* no es
   hashable. Lanza un "MemoryError" si no hay espacio para crecer.
   Lanza un "SystemError" si *set* no es una instancia de "set" o su
   subtipo.

   Nota:

     The operation is atomic on *free threading* when *key* is "str",
     "int", "float", "bool" or "bytes".

Las siguientes funciones están disponibles para instancias de "set" o
sus subtipos, pero no para instancias de "frozenset" o sus subtipos.

int PySet_Discard(PyObject *set, PyObject *key)
    * Part of the Stable ABI.** Thread safety: Safe for concurrent use
   on the same object.*

   Return "1" if found and removed, "0" if not found (no action
   taken), and "-1" if an error is encountered.  Does not raise
   "KeyError" for missing keys.  Raise a "TypeError" if the *key* is
   unhashable.  Unlike the Python "discard()" method, this function
   does not automatically convert unhashable sets into temporary
   frozensets. Raise "SystemError" if *set* is not an instance of
   "set" or its subtype.

   Nota:

     The operation is atomic on *free threading* when *key* is "str",
     "int", "float", "bool" or "bytes".

PyObject *PySet_Pop(PyObject *set)
    *Return value: New reference.** Part of the Stable ABI.** Thread
   safety: Atomic.*

   Retorna una nueva referencia a un objeto arbitrario en el *set* y
   elimina el objeto del *set*. Retorna "NULL" en caso de falla. Lanza
   "KeyError" si el conjunto está vacío. Lanza a "SystemError" si
   *set* no es una instancia de "set" o su subtipo.

int PySet_Clear(PyObject *set)
    * Part of the Stable ABI.** Thread safety: Atomic.*

   Vacía todos los elementos de un conjunto existente. Retorna "0" en
   caso de éxito. Retorna "-1" y lanza "SystemError" si *set* no es
   una instancia de "set" o su subtipo.

   Nota:

     In the *free-threaded build*, the set is emptied before its
     entries are cleared, so other threads will observe an empty set
     rather than intermediate states.

## Deprecated API

PySet_MINSIZE

   A constant representing the size of an internal preallocated table
   inside "PySetObject" instances.

   This is documented solely for completeness, as there are no
   guarantees that a given version of CPython uses preallocated tables
   with a fixed size. In code that does not deal with unstable set
   internals, "PySet_MINSIZE" can be replaced with a small constant
   like "8".

   If looking for the size of a set, use "PySet_Size()" instead.

   Soft deprecated since version 3.14.
