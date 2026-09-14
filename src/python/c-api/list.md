---
title: Objetos lista
source_url: https://docs.python.org/es/3
source_path: c-api/list.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 430
---

# Objetos lista

type PyListObject

   Este subtipo de "PyObject" representa un objeto lista de Python.

PyTypeObject PyList_Type
    * Part of the Stable ABI.*

   Esta instancia de "PyTypeObject" representa el tipo lista de
   Python. Este es el mismo objeto que "list" en la capa de Python.

int PyList_Check(PyObject *p)
    * Thread safety: Atomic.*

   Retorna verdadero si *p* es un objeto lista o una instancia de un
   subtipo del tipo lista. Esta función siempre finaliza con éxito.

int PyList_CheckExact(PyObject *p)
    * Thread safety: Atomic.*

   Retorna verdadero si *p* es un objeto lista, pero no una instancia
   de un subtipo del tipo lista. Esta función siempre finaliza con
   éxito.

PyObject *PyList_New(Py_ssize_t len)
    *Return value: New reference.** Part of the Stable ABI.** Thread
   safety: Atomic.*

   Retorna una nueva lista de longitud *len* en caso de éxito o "NULL"
   en caso de error.

   Nota:

     Si *len* es mayor que cero, los elementos del objeto de la lista
     retornada se establecen en "NULL". Por lo tanto, no puede
     utilizar funciones API abstractas como "PySequence_SetItem()" o
     exponer el objeto al código Python antes de configurar todos los
     elementos en un objeto real con "PyList_SetItem()" o
     "PyList_SET_ITEM()". Las siguientes APIs son APIs seguras antes
     de que la lista esté completamente inicializada:
     "PyList_SetItem()" y "PyList_SET_ITEM()".

Py_ssize_t PyList_Size(PyObject *list)
    * Part of the Stable ABI.** Thread safety: Atomic.*

   Retorna la longitud del objeto lista en *list*; esto es equivalente
   a "len(list)" en un objeto lista.

Py_ssize_t PyList_GET_SIZE(PyObject *list)
    * Thread safety: Atomic.*

   Similar a "PyList_Size()", pero sin comprobación de errores.

PyObject *PyList_GetItemRef(PyObject *list, Py_ssize_t index)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.13.** Thread safety: Atomic.*

   Retorna el objeto en la posición *index* en la lista a la que
   apunta *list*. La posición no debe ser negativa; La indexación
   desde el final de la lista no es compatible. Si *index* está fuera
   de los límites (*<0 o >= len(list)*), retorna "NULL" y establece
   una excepción "IndexError".

   Added in version 3.13.

PyObject *PyList_GetItem(PyObject *list, Py_ssize_t index)
    *Return value: Borrowed reference.** Part of the Stable ABI.**
   Thread safety: Safe to call from multiple threads with external
   synchronization only.*

   Como "PyList_GetItemRef()", pero retorna una *referencia prestada*
   en lugar de una *referencia fuerte*.

   Nota:

     In the *free-threaded build*, the returned *borrowed reference*
     may become invalid if another thread modifies the list
     concurrently. Prefer "PyList_GetItemRef()", which returns a
     *strong reference*.

PyObject *PyList_GET_ITEM(PyObject *list, Py_ssize_t i)
    *Return value: Borrowed reference.** Thread safety: Safe to call
   from multiple threads with external synchronization only.*

   Similar a "PyList_GetItem()", pero sin comprobación de errores.

   Nota:

     In the *free-threaded build*, the returned *borrowed reference*
     may become invalid if another thread modifies the list
     concurrently. Prefer "PyList_GetItemRef()", which returns a
     *strong reference*.

int PyList_SetItem(PyObject *list, Py_ssize_t index, PyObject *item)
    * Part of the Stable ABI.** Thread safety: Atomic.*

   Establece el elemento en el índice *index* en la lista a *item*.
   Retorna "0" en caso de éxito. Si *index* está fuera de límites,
   retorna "-1" y establece una excepción "IndexError".

   Nota:

     This function "*steals*" a reference to *item*, even on error. On
     success, it discards a reference to an item already in the list
     at the affected position (unless it was "NULL").

void PyList_SET_ITEM(PyObject *list, Py_ssize_t i, PyObject *o)
    * Thread safety: Safe to call from multiple threads with external
   synchronization only.*

   Forma macro de "PyList_SetItem()" sin comprobación de errores. Esto
   normalmente solo se usa para completar nuevas listas donde no hay
   contenido anterior.

   La verificación de límites se realiza como una aserción si Python
   se compila en modo de depuración o "con aserciones".

   Nota:

     This macro "*steals*" a reference to *item*, and, unlike
     "PyList_SetItem()", does *not* discard a reference to any item
     that is being replaced; any reference in *list* at position *i*
     will be leaked.

   Nota:

     In the *free-threaded build*, this macro has no internal
     synchronization. It is normally only used to fill in new lists
     where no other thread has a reference to the list. If the list
     may be shared, use "PyList_SetItem()" instead, which uses a *per-
     object lock*.

int PyList_Insert(PyObject *list, Py_ssize_t index, PyObject *item)
    * Part of the Stable ABI.** Thread safety: Safe for concurrent use
   on the same object.*

   Inserta el elemento *item* en la lista *list* delante del índice
   *index*. Retorna "0" si tiene éxito; retorna "-1" y establece una
   excepción si no tiene éxito. Análogo a "list.insert(index, item)".

int PyList_Append(PyObject *list, PyObject *item)
    * Part of the Stable ABI.** Thread safety: Atomic.*

   Agrega el objeto *item* al final de la lista *list*. Retorna "0" si
   tiene éxito; retorna "-1" y establece una excepción si no tiene
   éxito. Análogo a "list.append(item)".

PyObject *PyList_GetSlice(PyObject *list, Py_ssize_t low, Py_ssize_t high)
    *Return value: New reference.** Part of the Stable ABI.** Thread
   safety: Atomic.*

   Retorna una lista de los objetos en *list* que contiene los objetos
   *between*, *low* y *high*. Retorna "NULL" y establece una excepción
   si no tiene éxito. Análogo a "list[low:high]". La indexación desde
   el final de la lista no es compatible.

int PyList_SetSlice(PyObject *list, Py_ssize_t low, Py_ssize_t high, PyObject *itemlist)
    * Part of the Stable ABI.** Thread safety: Safe for concurrent use
   on the same object.*

   Establece el segmento de *list* entre *low* y *high* para el
   contenido de *itemlist*. Análogo a "list[low:high] = itemlist". La
   lista *itemlist* puede ser "NULL", lo que indica la asignación de
   una lista vacía (eliminación de segmentos). Retorna "0" en caso de
   éxito, "-1" en caso de error. La indexación desde el final de la
   lista no es compatible.

   Nota:

     In the *free-threaded build*, when *itemlist* is a "list", both
     *list* and *itemlist* are locked for the duration of the
     operation. For other iterables (or "NULL"), only *list* is
     locked.

int PyList_Extend(PyObject *list, PyObject *iterable)
    * Thread safety: Safe for concurrent use on the same object.*

   Extiende *list* con los contenidos de *iterable*. Esto es lo mismo
   que "PyList_SetSlice(list, PY_SSIZE_T_MAX, PY_SSIZE_T_MAX,
   iterable)" y análogo a "list.extend(iterable)" o "list +=
   iterable".

   Lanza una excepción y retorna "-1" si *list* no es un objeto
   "list". Retorna 0 en caso de éxito.

   Added in version 3.13.

   Nota:

     In the *free-threaded build*, when *iterable* is a "list", "set",
     "dict", or dict view, both *list* and *iterable* (or its
     underlying dict) are locked for the duration of the operation.
     For other iterables, only *list* is locked; *iterable* may be
     concurrently modified by another thread.

int PyList_Clear(PyObject *list)
    * Thread safety: Atomic.*

   Elimina todos los elementos de *list*. Esto es lo mismo que
   "PyList_SetSlice(list, 0, PY_SSIZE_T_MAX, NULL)" y análogo a
   "list.clear()" o "del list[:]".

   Lanza una excepción y retorna "-1" si *list* no es un objeto
   "list". Retorna 0 en caso de éxito.

   Added in version 3.13.

int PyList_Sort(PyObject *list)
    * Part of the Stable ABI.** Thread safety: Safe for concurrent use
   on the same object.*

   Ordena los elementos de *list* en su lugar. Retorna "0" en caso de
   éxito, "-1" en caso de error. Esto es equivalente a "list.sort()".

   Nota:

     In the *free-threaded build*, element comparison via "__lt__()"
     can execute arbitrary Python code, during which the *per-object
     lock* may be temporarily released. For built-in types ("str",
     "int", "float"), the lock is not released during comparison.

int PyList_Reverse(PyObject *list)
    * Part of the Stable ABI.** Thread safety: Safe for concurrent use
   on the same object.*

   Invierte los elementos de la lista *list* en su lugar. Retorna "0"
   en caso de éxito, "-1" en caso de error. Este es el equivalente de
   "list.reverse()".

PyObject *PyList_AsTuple(PyObject *list)
    *Return value: New reference.** Part of the Stable ABI.** Thread
   safety: Atomic.*

   Retorna un nuevo objeto tupla que contiene el contenido de *list*;
   equivalente a "tuple(list)".
