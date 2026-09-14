---
title: Objetos diccionario
source_url: https://docs.python.org/es/3
source_path: c-api/dict.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 240
---

# Objetos diccionario

type PyDictObject

   Este subtipo de "PyObject" representa un objeto diccionario de
   Python.

PyTypeObject PyDict_Type
    * Part of the Stable ABI.*

   Esta instancia de "PyTypeObject" representa el tipo diccionario de
   Python. Este es el mismo objeto que "dict" en la capa de Python.

int PyDict_Check(PyObject *p)
    * Thread safety: Atomic.*

   Retorna verdadero si *p* es un objeto "dict" o una instancia de un
   subtipo del tipo "dict". Esta función siempre finaliza con éxito.

int PyDict_CheckExact(PyObject *p)
    * Thread safety: Atomic.*

   Retorna verdadero si *p* es un objeto "dict", pero no una instancia
   de un subtipo del tipo "dict". Esta función siempre finaliza con
   éxito.

PyObject *PyDict_New()
    *Return value: New reference.** Part of the Stable ABI.** Thread
   safety: Atomic.*

   Retorna un nuevo diccionario vacío, o "NULL" en caso de falla.

PyObject *PyDictProxy_New(PyObject *mapping)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna un objeto a "types.MappingProxyType" para una asignación
   que imponga un comportamiento de solo lectura. Esto normalmente se
   usa para crear una vista para evitar la modificación del
   diccionario para los tipos de clase no dinámicos.

PyTypeObject PyDictProxy_Type
    * Part of the Stable ABI.*

   The type object for mapping proxy objects created by
   "PyDictProxy_New()" and for the read-only "__dict__" attribute of
   many built-in types. A "PyDictProxy_Type" instance provides a
   dynamic, read-only view of an underlying dictionary: changes to the
   underlying dictionary are reflected in the proxy, but the proxy
   itself does not support mutation operations. This corresponds to
   "types.MappingProxyType" in Python.

void PyDict_Clear(PyObject *p)
    * Part of the Stable ABI.** Thread safety: Atomic.*

   Vacía un diccionario existente de todos los pares clave-valor
   (*key-value*).

int PyDict_Contains(PyObject *p, PyObject *key)
    * Part of the Stable ABI.** Thread safety: Safe for concurrent use
   on the same object.*

   Determine if dictionary *p* contains *key*.  If an item in *p*
   matches *key*, return "1", otherwise return "0".  On error, return
   "-1". This is equivalent to the Python expression "key in p".

   Nota:

     The operation is atomic on *free threading* when *key* is "str",
     "int", "float", "bool" or "bytes".

int PyDict_ContainsString(PyObject *p, const char *key)
    * Thread safety: Atomic.*

   This is the same as "PyDict_Contains()", but *key* is specified as
   a const char* UTF-8 encoded bytes string, rather than a PyObject*.

   Added in version 3.13.

PyObject *PyDict_Copy(PyObject *p)
    *Return value: New reference.** Part of the Stable ABI.** Thread
   safety: Atomic.*

   Retorna un nuevo diccionario que contiene los mismos pares clave-
   valor (*key-value*) que *p*.

int PyDict_SetItem(PyObject *p, PyObject *key, PyObject *val)
    * Part of the Stable ABI.** Thread safety: Safe for concurrent use
   on the same object.*

   Insert *val* into the dictionary *p* with a key of *key*.  *key*
   must be *hashable*; if it isn't, "TypeError" will be raised. Return
   "0" on success or "-1" on failure. This function *does not*
   "*steal*" a reference to *val*.

   Nota:

     The operation is atomic on *free threading* when *key* is "str",
     "int", "float", "bool" or "bytes".

int PyDict_SetItemString(PyObject *p, const char *key, PyObject *val)
    * Part of the Stable ABI.** Thread safety: Atomic.*

   This is the same as "PyDict_SetItem()", but *key* is specified as a
   const char* UTF-8 encoded bytes string, rather than a PyObject*.

int PyDict_DelItem(PyObject *p, PyObject *key)
    * Part of the Stable ABI.** Thread safety: Safe for concurrent use
   on the same object.*

   Remove the entry in dictionary *p* with key *key*. *key* must be
   *hashable*; if it isn't, "TypeError" is raised. If *key* is not in
   the dictionary, "KeyError" is raised. Return "0" on success or "-1"
   on failure.

   Nota:

     The operation is atomic on *free threading* when *key* is "str",
     "int", "float", "bool" or "bytes".

int PyDict_DelItemString(PyObject *p, const char *key)
    * Part of the Stable ABI.** Thread safety: Atomic.*

   This is the same as "PyDict_DelItem()", but *key* is specified as a
   const char* UTF-8 encoded bytes string, rather than a PyObject*.

int PyDict_GetItemRef(PyObject *p, PyObject *key, PyObject **result)
    * Part of the Stable ABI since version 3.13.** Thread safety: Safe
   for concurrent use on the same object.*

   Return a new *strong reference* to the object from dictionary *p*
   which has a key *key*:

   * If the key is present, set **result* to a new *strong reference*
     to the value and return "1".

   * If the key is missing, set **result* to "NULL" and return "0".

   * On error, raise an exception, set **result* to "NULL" and return
     "-1".

   Nota:

     The operation is atomic on *free threading* when *key* is "str",
     "int", "float", "bool" or "bytes".

   Added in version 3.13.

   See also the "PyObject_GetItem()" function.

PyObject *PyDict_GetItem(PyObject *p, PyObject *key)
    *Return value: Borrowed reference.** Part of the Stable ABI.**
   Thread safety: Safe to call from multiple threads with external
   synchronization only.*

   Return a *borrowed reference* to the object from dictionary *p*
   which has a key *key*.  Return "NULL" if the key *key* is missing
   *without* setting an exception.

   Nota:

     Exceptions that occur while this calls "__hash__()" and
     "__eq__()" methods are silently ignored. Prefer the
     "PyDict_GetItemWithError()" function instead.

   Nota:

     In the *free-threaded build*, the returned *borrowed reference*
     may become invalid if another thread modifies the dictionary
     concurrently. Prefer "PyDict_GetItemRef()", which returns a
     *strong reference*.

   Distinto en la versión 3.10: Calling this API without an *attached
   thread state* had been allowed for historical reason. It is no
   longer allowed.

PyObject *PyDict_GetItemWithError(PyObject *p, PyObject *key)
    *Return value: Borrowed reference.** Part of the Stable ABI.**
   Thread safety: Safe to call from multiple threads with external
   synchronization only.*

   Variante de "PyDict_GetItem()" que no suprime las excepciones.
   Retorna "NULL" **con** una excepción establecida si se produjo una
   excepción. Retorna "NULL" **sin** una excepción establecida si la
   clave no estaba presente.

   Nota:

     In the *free-threaded build*, the returned *borrowed reference*
     may become invalid if another thread modifies the dictionary
     concurrently. Prefer "PyDict_GetItemRef()", which returns a
     *strong reference*.

PyObject *PyDict_GetItemString(PyObject *p, const char *key)
    *Return value: Borrowed reference.** Part of the Stable ABI.**
   Thread safety: Safe to call from multiple threads with external
   synchronization only.*

   This is the same as "PyDict_GetItem()", but *key* is specified as a
   const char* UTF-8 encoded bytes string, rather than a PyObject*.

   Nota:

     Exceptions that occur while this calls "__hash__()" and
     "__eq__()" methods or while creating the temporary "str" object
     are silently ignored. Prefer using the
     "PyDict_GetItemWithError()" function with your own
     "PyUnicode_FromString()" *key* instead.

   Nota:

     In the *free-threaded build*, the returned *borrowed reference*
     may become invalid if another thread modifies the dictionary
     concurrently. Prefer "PyDict_GetItemStringRef()", which returns a
     *strong reference*.

int PyDict_GetItemStringRef(PyObject *p, const char *key, PyObject **result)
    * Part of the Stable ABI since version 3.13.** Thread safety:
   Atomic.*

   Similar to "PyDict_GetItemRef()", but *key* is specified as a const
   char* UTF-8 encoded bytes string, rather than a PyObject*.

   Added in version 3.13.

PyObject *PyDict_SetDefault(PyObject *p, PyObject *key, PyObject *defaultobj)
    *Return value: Borrowed reference.** Thread safety: Safe to call
   from multiple threads with external synchronization only.*

   Esto es lo mismo al nivel de Python "dict.setdefault()". Si está
   presente, retorna el valor correspondiente a *key* del diccionario
   *p*. Si la clave no está en el "dict", se inserta con el valor
   *defaultobj* y se retorna *defaultobj*. Esta función evalúa la
   función *hash* de *key* solo una vez, en lugar de evaluarla
   independientemente para la búsqueda y la inserción.

   Added in version 3.4.

   Nota:

     In the *free-threaded build*, the returned *borrowed reference*
     may become invalid if another thread modifies the dictionary
     concurrently. Prefer "PyDict_SetDefaultRef()", which returns a
     *strong reference*.

int PyDict_SetDefaultRef(PyObject *p, PyObject *key, PyObject *default_value, PyObject **result)
    * Thread safety: Safe for concurrent use on the same object.*

   Inserts *default_value* into the dictionary *p* with a key of *key*
   if the key is not already present in the dictionary. If *result* is
   not "NULL", then **result* is set to a *strong reference* to either
   *default_value*, if the key was not present, or the existing value,
   if *key* was already present in the dictionary. Returns "1" if the
   key was present and *default_value* was not inserted, or "0" if the
   key was not present and *default_value* was inserted. On failure,
   returns "-1", sets an exception, and sets "*result" to "NULL".

   For clarity: if you have a strong reference to *default_value*
   before calling this function, then after it returns, you hold a
   strong reference to both *default_value* and **result* (if it's not
   "NULL"). These may refer to the same object: in that case you hold
   two separate references to it.

   Nota:

     The operation is atomic on *free threading* when *key* is "str",
     "int", "float", "bool" or "bytes".

   Added in version 3.13.

int PyDict_Pop(PyObject *p, PyObject *key, PyObject **result)
    * Thread safety: Safe for concurrent use on the same object.*

   Remove *key* from dictionary *p* and optionally return the removed
   value. Do not raise "KeyError" if the key is missing.

   * If the key is present, set **result* to a new reference to the
     removed value if *result* is not "NULL", and return "1".

   * If the key is missing, set **result* to "NULL" if *result* is not
     "NULL", and return "0".

   * On error, raise an exception and return "-1".

   Similar to "dict.pop()", but without the default value and not
   raising "KeyError" if the key is missing.

   Nota:

     The operation is atomic on *free threading* when *key* is "str",
     "int", "float", "bool" or "bytes".

   Added in version 3.13.

int PyDict_PopString(PyObject *p, const char *key, PyObject **result)
    * Thread safety: Atomic.*

   Similar to "PyDict_Pop()", but *key* is specified as a const char*
   UTF-8 encoded bytes string, rather than a PyObject*.

   Added in version 3.13.

PyObject *PyDict_Items(PyObject *p)
    *Return value: New reference.** Part of the Stable ABI.** Thread
   safety: Atomic.*

   Retorna un "PyListObject" que contiene todos los elementos del
   diccionario.

PyObject *PyDict_Keys(PyObject *p)
    *Return value: New reference.** Part of the Stable ABI.** Thread
   safety: Atomic.*

   Retorna un "PyListObject" que contiene todas las claves del
   diccionario.

PyObject *PyDict_Values(PyObject *p)
    *Return value: New reference.** Part of the Stable ABI.** Thread
   safety: Atomic.*

   Retorna un "PyListObject" que contiene todos los valores del
   diccionario *p*.

Py_ssize_t PyDict_Size(PyObject *p)
    * Part of the Stable ABI.** Thread safety: Atomic.*

   Retorna el número de elementos en el diccionario. Esto es
   equivalente a "len(p)" en un diccionario.

Py_ssize_t PyDict_GET_SIZE(PyObject *p)
    * Thread safety: Atomic.*

   Similar to "PyDict_Size()", but without error checking.

int PyDict_Next(PyObject *p, Py_ssize_t *ppos, PyObject **pkey, PyObject **pvalue)
    * Part of the Stable ABI.** Thread safety: Safe to call from
   multiple threads with external synchronization only.*

   Iterate over all key-value pairs in the dictionary *p*.  The
   "Py_ssize_t" referred to by *ppos* must be initialized to "0" prior
   to the first call to this function to start the iteration; the
   function returns true for each pair in the dictionary, and false
   once all pairs have been reported.  The parameters *pkey* and
   *pvalue* should either point to PyObject* variables that will be
   filled in with each key and value, respectively, or may be "NULL".
   Any references returned through them are borrowed.  *ppos* should
   not be altered during iteration. Its value represents offsets
   within the internal dictionary structure, and since the structure
   is sparse, the offsets are not consecutive.

   Por ejemplo:

      PyObject *key, *value;
      Py_ssize_t pos = 0;

      while (PyDict_Next(self->dict, &pos, &key, &value)) {
          /* do something interesting with the values... */
          ...
      }

   El diccionario *p* no debe mutarse durante la iteración. Es seguro
   modificar los valores de las claves a medida que recorre el
   diccionario, pero solo mientras el conjunto de claves no cambie.
   Por ejemplo:

      PyObject *key, *value;
      Py_ssize_t pos = 0;

      while (PyDict_Next(self->dict, &pos, &key, &value)) {
          long i = PyLong_AsLong(value);
          if (i == -1 && PyErr_Occurred()) {
              return -1;
          }
          PyObject *o = PyLong_FromLong(i + 1);
          if (o == NULL)
              return -1;
          if (PyDict_SetItem(self->dict, key, o) < 0) {
              Py_DECREF(o);
              return -1;
          }
          Py_DECREF(o);
      }

   The function is not thread-safe in the *free-threaded* build
   without external synchronization.  You can use
   "Py_BEGIN_CRITICAL_SECTION" to lock the dictionary while iterating
   over it:

      Py_BEGIN_CRITICAL_SECTION(self->dict);
      while (PyDict_Next(self->dict, &pos, &key, &value)) {
          ...
      }
      Py_END_CRITICAL_SECTION();

   Nota:

     On the free-threaded build, this function can be used safely
     inside a critical section. However, the references returned for
     *pkey* and *pvalue* are *borrowed* and are only valid while the
     critical section is held. If you need to use these objects
     outside the critical section or when the critical section can be
     suspended, create a *strong reference* (for example, using
     "Py_NewRef()").

int PyDict_Merge(PyObject *a, PyObject *b, int override)
    * Part of the Stable ABI.** Thread safety: Safe for concurrent use
   on the same object.*

   Itera sobre el objeto de mapeo *b* agregando pares clave-valor al
   diccionario *a*. *b* puede ser un diccionario o cualquier objeto
   que soporte "PyMapping_Keys()" y "PyObject_GetItem()". Si
   *override* es verdadero, los pares existentes en *a* se
   reemplazarán si se encuentra una clave coincidente en *b*, de lo
   contrario, los pares solo se agregarán si no hay una clave
   coincidente en *a*. Retorna "0" en caso de éxito o "-1" si se lanza
   una excepción.

   Nota:

     In the *free-threaded build*, when *b* is a "dict" (with the
     standard iterator), both *a* and *b* are locked for the duration
     of the operation. When *b* is a non-dict mapping, only *a* is
     locked; *b* may be concurrently modified by another thread.

int PyDict_Update(PyObject *a, PyObject *b)
    * Part of the Stable ABI.** Thread safety: Safe for concurrent use
   on the same object.*

   Esto es lo mismo que "PyDict_Merge(a, b, 1)" en C, y es similar a
   "a.update(b)" en Python excepto que "PyDict_Update()" no vuelve a
   la iteración sobre una secuencia de pares de valores clave si el
   segundo argumento no tiene el atributo "claves". Retorna "0" en
   caso de éxito o "-1" si se produjo una excepción.

   Nota:

     In the *free-threaded build*, when *b* is a "dict" (with the
     standard iterator), both *a* and *b* are locked for the duration
     of the operation. When *b* is a non-dict mapping, only *a* is
     locked; *b* may be concurrently modified by another thread.

int PyDict_MergeFromSeq2(PyObject *a, PyObject *seq2, int override)
    * Part of the Stable ABI.** Thread safety: Safe for concurrent use
   on the same object.*

   Actualiza o combina en el diccionario *a*, desde los pares clave-
   valor en *seq2*. *seq2* debe ser un objeto iterable que produzca
   objetos iterables de longitud 2, vistos como pares clave-valor. En
   el caso de claves duplicadas, el último gana si *override* es
   verdadero, de lo contrario, el primero gana. Retorna "0" en caso de
   éxito o "-1" si se produjo una excepción. El equivalente en Python
   (excepto el valor de retorno)

      def PyDict_MergeFromSeq2(a, seq2, override):
          for key, value in seq2:
              if override or key not in a:
                  a[key] = value

   Nota:

     In the *free-threaded* build, only *a* is locked. The iteration
     over *seq2* is not synchronized; *seq2* may be concurrently
     modified by another thread.

int PyDict_AddWatcher(PyDict_WatchCallback callback)
    * Thread safety: Safe to call from multiple threads with external
   synchronization only.*

   Register *callback* as a dictionary watcher. Return a non-negative
   integer id which must be passed to future calls to
   "PyDict_Watch()". In case of error (e.g. no more watcher IDs
   available), return "-1" and set an exception.

   Nota:

     This function is not internally synchronized. In the *free-
     threaded* build, callers should ensure no concurrent calls to
     "PyDict_AddWatcher()" or "PyDict_ClearWatcher()" are in progress.

   Added in version 3.12.

int PyDict_ClearWatcher(int watcher_id)
    * Thread safety: Safe to call from multiple threads with external
   synchronization only.*

   Clear watcher identified by *watcher_id* previously returned from
   "PyDict_AddWatcher()". Return "0" on success, "-1" on error (e.g.
   if the given *watcher_id* was never registered.)

   Nota:

     This function is not internally synchronized. In the *free-
     threaded* build, callers should ensure no concurrent calls to
     "PyDict_AddWatcher()" or "PyDict_ClearWatcher()" are in progress.

   Added in version 3.12.

int PyDict_Watch(int watcher_id, PyObject *dict)
    * Thread safety: Safe to call without external synchronization on
   distinct objects.*

   Mark dictionary *dict* as watched. The callback granted
   *watcher_id* by "PyDict_AddWatcher()" will be called when *dict* is
   modified or deallocated. Return "0" on success or "-1" on error.

   Added in version 3.12.

int PyDict_Unwatch(int watcher_id, PyObject *dict)
    * Thread safety: Safe to call without external synchronization on
   distinct objects.*

   Mark dictionary *dict* as no longer watched. The callback granted
   *watcher_id* by "PyDict_AddWatcher()" will no longer be called when
   *dict* is modified or deallocated. The dict must previously have
   been watched by this watcher. Return "0" on success or "-1" on
   error.

   Added in version 3.12.

type PyDict_WatchEvent

   Enumeration of possible dictionary watcher events:
   "PyDict_EVENT_ADDED", "PyDict_EVENT_MODIFIED",
   "PyDict_EVENT_DELETED", "PyDict_EVENT_CLONED",
   "PyDict_EVENT_CLEARED", or "PyDict_EVENT_DEALLOCATED".

   Added in version 3.12.

typedef int (*PyDict_WatchCallback)(PyDict_WatchEvent event, PyObject *dict, PyObject *key, PyObject *new_value)

   Type of a dict watcher callback function.

   If *event* is "PyDict_EVENT_CLEARED" or "PyDict_EVENT_DEALLOCATED",
   both *key* and *new_value* will be "NULL". If *event* is
   "PyDict_EVENT_ADDED" or "PyDict_EVENT_MODIFIED", *new_value* will
   be the new value for *key*. If *event* is "PyDict_EVENT_DELETED",
   *key* is being deleted from the dictionary and *new_value* will be
   "NULL".

   "PyDict_EVENT_CLONED" occurs when *dict* was previously empty and
   another dict is merged into it. To maintain efficiency of this
   operation, per-key "PyDict_EVENT_ADDED" events are not issued in
   this case; instead a single "PyDict_EVENT_CLONED" is issued, and
   *key* will be the source dictionary.

   The callback may inspect but must not modify *dict*; doing so could
   have unpredictable effects, including infinite recursion. Do not
   trigger Python code execution in the callback, as it could modify
   the dict as a side effect.

   If *event* is "PyDict_EVENT_DEALLOCATED", taking a new reference in
   the callback to the about-to-be-destroyed dictionary will resurrect
   it and prevent it from being freed at this time. When the
   resurrected object is destroyed later, any watcher callbacks active
   at that time will be called again.

   Callbacks occur before the notified modification to *dict* takes
   place, so the prior state of *dict* can be inspected.

   If the callback sets an exception, it must return "-1"; this
   exception will be printed as an unraisable exception using
   "PyErr_WriteUnraisable()". Otherwise it should return "0".

   There may already be a pending exception set on entry to the
   callback. In this case, the callback should return "0" with the
   same exception still set. This means the callback may not call any
   other API that can set an exception unless it saves and clears the
   exception state first, and restores it before returning.

   Added in version 3.12.

## Dictionary View Objects

int PyDictViewSet_Check(PyObject *op)

   Return true if *op* is a view of a set inside a dictionary. This is
   currently equivalent to PyDictKeys_Check(op) ||
   PyDictItems_Check(op). This function always succeeds.

PyTypeObject PyDictKeys_Type
    * Part of the Stable ABI.*

   Type object for a view of dictionary keys. In Python, this is the
   type of the object returned by "dict.keys()".

int PyDictKeys_Check(PyObject *op)

   Return true if *op* is an instance of a dictionary keys view. This
   function always succeeds.

PyTypeObject PyDictValues_Type
    * Part of the Stable ABI.*

   Type object for a view of dictionary values. In Python, this is the
   type of the object returned by "dict.values()".

int PyDictValues_Check(PyObject *op)

   Return true if *op* is an instance of a dictionary values view.
   This function always succeeds.

PyTypeObject PyDictItems_Type
    * Part of the Stable ABI.*

   Type object for a view of dictionary items. In Python, this is the
   type of the object returned by "dict.items()".

int PyDictItems_Check(PyObject *op)

   Return true if *op* is an instance of a dictionary items view. This
   function always succeeds.

## Ordered Dictionaries

Python's C API provides interface for "collections.OrderedDict" from
C. Since Python 3.7, dictionaries are ordered by default, so there is
usually little need for these functions; prefer "PyDict*" where
possible.

PyTypeObject PyODict_Type

   Type object for ordered dictionaries. This is the same object as
   "collections.OrderedDict" in the Python layer.

int PyODict_Check(PyObject *od)

   Return true if *od* is an ordered dictionary object or an instance
   of a subtype of the "OrderedDict" type.  This function always
   succeeds.

int PyODict_CheckExact(PyObject *od)

   Return true if *od* is an ordered dictionary object, but not an
   instance of a subtype of the "OrderedDict" type. This function
   always succeeds.

PyTypeObject PyODictKeys_Type

   Analogous to "PyDictKeys_Type" for ordered dictionaries.

PyTypeObject PyODictValues_Type

   Analogous to "PyDictValues_Type" for ordered dictionaries.

PyTypeObject PyODictItems_Type

   Analogous to "PyDictItems_Type" for ordered dictionaries.

PyObject *PyODict_New(void)

   Return a new empty ordered dictionary, or "NULL" on failure.

   This is analogous to "PyDict_New()".

int PyODict_SetItem(PyObject *od, PyObject *key, PyObject *value)

   Insert *value* into the ordered dictionary *od* with a key of
   *key*. Return "0" on success or "-1" with an exception set on
   failure.

   This is analogous to "PyDict_SetItem()".

int PyODict_DelItem(PyObject *od, PyObject *key)

   Remove the entry in the ordered dictionary *od* with key *key*.
   Return "0" on success or "-1" with an exception set on failure.

   This is analogous to "PyDict_DelItem()".

These are *soft deprecated* aliases to "PyDict" APIs:

+----------------------------------------------------+----------------------------------------------------+
| "PyODict"                                          | "PyDict"                                           |
|====================================================|====================================================|
## | PyODict_GetItem(od, key)                           | "PyDict_GetItem()"                                 |

## | PyODict_GetItemWithError(od, key)                  | "PyDict_GetItemWithError()"                        |

## | PyODict_GetItemString(od, key)                     | "PyDict_GetItemString()"                           |

## | PyODict_Contains(od, key)                          | "PyDict_Contains()"                                |

## | PyODict_Size(od)                                   | "PyDict_Size()"                                    |

## | PyODict_SIZE(od)                                   | "PyDict_GET_SIZE()"                                |
