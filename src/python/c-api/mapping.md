---
title: Protocolo de mapeo
source_url: https://docs.python.org/es/3
source_path: c-api/mapping.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 450
---

# Protocolo de mapeo

Consulte también "PyObject_GetItem()", "PyObject_SetItem()" y
"PyObject_DelItem()".

int PyMapping_Check(PyObject *o)
    * Part of the Stable ABI.*

   Return "1" if the object provides the mapping protocol or supports
   slicing, and "0" otherwise.  Note that it returns "1" for Python
   classes with a "__getitem__()" method, since in general it is
   impossible to determine what type of keys the class supports. This
   function always succeeds.

Py_ssize_t PyMapping_Size(PyObject *o)
Py_ssize_t PyMapping_Length(PyObject *o)
    * Part of the Stable ABI.*

   Retorna el número de claves en el objeto *o* en caso de éxito, y
   "-1" en caso de error. Esto es equivalente a la expresión de Python
   "len(o)".

PyObject *PyMapping_GetItemString(PyObject *o, const char *key)
    *Return value: New reference.** Part of the Stable ABI.*

   This is the same as "PyObject_GetItem()", but *key* is specified as
   a const char* UTF-8 encoded bytes string, rather than a PyObject*.

int PyMapping_GetOptionalItem(PyObject *obj, PyObject *key, PyObject **result)
    * Part of the Stable ABI since version 3.13.*

   Variant of "PyObject_GetItem()" which doesn't raise "KeyError" if
   the key is not found.

   If the key is found, return "1" and set **result* to a new *strong
   reference* to the corresponding value. If the key is not found,
   return "0" and set **result* to "NULL"; the "KeyError" is silenced.
   If an error other than "KeyError" is raised, return "-1" and set
   **result* to "NULL".

   Added in version 3.13.

int PyMapping_GetOptionalItemString(PyObject *obj, const char *key, PyObject **result)
    * Part of the Stable ABI since version 3.13.*

   This is the same as "PyMapping_GetOptionalItem()", but *key* is
   specified as a const char* UTF-8 encoded bytes string, rather than
   a PyObject*.

   Added in version 3.13.

int PyMapping_SetItemString(PyObject *o, const char *key, PyObject *v)
    * Part of the Stable ABI.*

   This is the same as "PyObject_SetItem()", but *key* is specified as
   a const char* UTF-8 encoded bytes string, rather than a PyObject*.

int PyMapping_DelItem(PyObject *o, PyObject *key)

   This is an alias of "PyObject_DelItem()".

int PyMapping_DelItemString(PyObject *o, const char *key)

   This is the same as "PyObject_DelItem()", but *key* is specified as
   a const char* UTF-8 encoded bytes string, rather than a PyObject*.

int PyMapping_HasKeyWithError(PyObject *o, PyObject *key)
    * Part of the Stable ABI since version 3.13.*

   Return "1" if the mapping object has the key *key* and "0"
   otherwise. This is equivalent to the Python expression "key in o".
   On failure, return "-1".

   Added in version 3.13.

int PyMapping_HasKeyStringWithError(PyObject *o, const char *key)
    * Part of the Stable ABI since version 3.13.*

   This is the same as "PyMapping_HasKeyWithError()", but *key* is
   specified as a const char* UTF-8 encoded bytes string, rather than
   a PyObject*.

   Added in version 3.13.

int PyMapping_HasKey(PyObject *o, PyObject *key)
    * Part of the Stable ABI.*

   Retorna "1" si el objeto de mapeo tiene la clave *key* y "0" de lo
   contrario. Esto es equivalente a la expresión de Python "key in o".
   Esta función siempre finaliza con éxito.

   Nota:

     Exceptions which occur when this calls the "__getitem__()" method
     are silently ignored. For proper error handling, use
     "PyMapping_HasKeyWithError()", "PyMapping_GetOptionalItem()" or
     "PyObject_GetItem()" instead.

int PyMapping_HasKeyString(PyObject *o, const char *key)
    * Part of the Stable ABI.*

   This is the same as "PyMapping_HasKey()", but *key* is specified as
   a const char* UTF-8 encoded bytes string, rather than a PyObject*.

   Nota:

     Exceptions that occur when this calls the "__getitem__()" method
     or while creating the temporary "str" object are silently
     ignored. For proper error handling, use
     "PyMapping_HasKeyStringWithError()",
     "PyMapping_GetOptionalItemString()" or
     "PyMapping_GetItemString()" instead.

PyObject *PyMapping_Keys(PyObject *o)
    *Return value: New reference.** Part of the Stable ABI.*

   En caso de éxito, retorna una lista de las claves en el objeto *o*.
   En caso de fallo, retorna "NULL".

   Distinto en la versión 3.7: Anteriormente, la función retornaba una
   lista o una tupla.

PyObject *PyMapping_Values(PyObject *o)
    *Return value: New reference.** Part of the Stable ABI.*

   En caso de éxito, retorna una lista de los valores en el objeto
   *o*. En caso de fallo, retorna "NULL".

   Distinto en la versión 3.7: Anteriormente, la función retornaba una
   lista o una tupla.

PyObject *PyMapping_Items(PyObject *o)
    *Return value: New reference.** Part of the Stable ABI.*

   En caso de éxito, retorna una lista de los elementos en el objeto
   *o*, donde cada elemento es una tupla que contiene un par clave-
   valor (*key-value*). En caso de fallo, retorna "NULL".

   Distinto en la versión 3.7: Anteriormente, la función retornaba una
   lista o una tupla.
