---
title: Allocating objects on the heap
source_url: https://docs.python.org/es/3
source_path: c-api/allocation.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 40
---

# Allocating objects on the heap

PyObject *_PyObject_New(PyTypeObject *type)
    *Return value: New reference.*

PyVarObject *_PyObject_NewVar(PyTypeObject *type, Py_ssize_t size)
    *Return value: New reference.*

PyObject *PyObject_Init(PyObject *op, PyTypeObject *type)
    *Return value: Borrowed reference.** Part of the Stable ABI.*

   Initialize a newly allocated object *op* with its type and initial
   reference.  Returns the initialized object.  Other fields of the
   object are not initialized.  Despite its name, this function is
   unrelated to the object's "__init__()" method ("tp_init" slot).
   Specifically, this function does **not** call the object's
   "__init__()" method.

   In general, consider this function to be a low-level routine. Use
   "tp_alloc" where possible. For implementing "tp_alloc" for your
   type, prefer "PyType_GenericAlloc()" or "PyObject_New()".

   Nota:

     This function only initializes the object's memory corresponding
     to the initial "PyObject" structure.  It does not zero the rest.

PyVarObject *PyObject_InitVar(PyVarObject *op, PyTypeObject *type, Py_ssize_t size)
    *Return value: Borrowed reference.** Part of the Stable ABI.*

   Esto hace todo lo que "PyObject_Init()" hace, y también inicializa
   la información de longitud para un objeto de tamaño variable.

   Nota:

     This function only initializes some of the object's memory.  It
     does not zero the rest.

PyObject_New(TYPE, typeobj)

   Allocates a new Python object using the C structure type *TYPE* and
   the Python type object *typeobj* ("PyTypeObject*") by calling
   "PyObject_Malloc()" to allocate memory and initializing it like
   "PyObject_Init()".  The caller will own the only reference to the
   object (i.e. its reference count will be one).

   Avoid calling this directly to allocate memory for an object; call
   the type's "tp_alloc" slot instead.

   When populating a type's "tp_alloc" slot, "PyType_GenericAlloc()"
   is preferred over a custom function that simply calls this macro.

   This macro does not call "tp_alloc", "tp_new" ("__new__()"), or
   "tp_init" ("__init__()").

   This cannot be used for objects with "Py_TPFLAGS_HAVE_GC" set in
   "tp_flags"; use "PyObject_GC_New" instead.

   Memory allocated by this macro must be freed with "PyObject_Free()"
   (usually called via the object's "tp_free" slot).

   Nota:

     The returned memory is not guaranteed to have been completely
     zeroed before it was initialized.

   Nota:

     This macro does not construct a fully initialized object of the
     given type; it merely allocates memory and prepares it for
     further initialization by "tp_init".  To construct a fully
     initialized object, call *typeobj* instead.  For example:

        PyObject *foo = PyObject_CallNoArgs((PyObject *)&PyFoo_Type);

   Ver también:

     * "PyObject_Free()"

     * "PyObject_GC_New"

     * "PyType_GenericAlloc()"

     * "tp_alloc"

PyObject_NewVar(TYPE, typeobj, size)

   Like "PyObject_New" except:

   * It allocates enough memory for the *TYPE* structure plus *size*
     ("Py_ssize_t") fields of the size given by the "tp_itemsize"
     field of *typeobj*.

   * The memory is initialized like "PyObject_InitVar()".

   This is useful for implementing objects like tuples, which are able
   to determine their size at construction time.  Embedding the array
   of fields into the same allocation decreases the number of
   allocations, improving the memory management efficiency.

   Avoid calling this directly to allocate memory for an object; call
   the type's "tp_alloc" slot instead.

   When populating a type's "tp_alloc" slot, "PyType_GenericAlloc()"
   is preferred over a custom function that simply calls this macro.

   This cannot be used for objects with "Py_TPFLAGS_HAVE_GC" set in
   "tp_flags"; use "PyObject_GC_NewVar" instead.

   Memory allocated by this function must be freed with
   "PyObject_Free()" (usually called via the object's "tp_free" slot).

   Nota:

     The returned memory is not guaranteed to have been completely
     zeroed before it was initialized.

   Nota:

     This macro does not construct a fully initialized object of the
     given type; it merely allocates memory and prepares it for
     further initialization by "tp_init".  To construct a fully
     initialized object, call *typeobj* instead.  For example:

        PyObject *list_instance = PyObject_CallNoArgs((PyObject *)&PyList_Type);

   Ver también:

     * "PyObject_Free()"

     * "PyObject_GC_NewVar"

     * "PyType_GenericAlloc()"

     * "tp_alloc"

PyObject _Py_NoneStruct

   Objeto que es visible en Python como "None". Esto solo se debe
   acceder utilizando el macro "Py_None", que se evalúa como un
   puntero a este objeto.

Ver también:

  Objetos módulo
     Para asignar y crear módulos de extensión.

## Soft-deprecated aliases

Soft deprecated since version 3.10.

These are aliases to existing functions and macros. They exist solely
for backwards compatibility.

+----------------------------------------------------+----------------------------------------------------+
| Soft-deprecated alias                              | Function                                           |
|====================================================|====================================================|
## | PyObject_NEW(type, typeobj)                        | "PyObject_New"                                     |

## | PyObject_NEW_VAR(type, typeobj, n)                 | "PyObject_NewVar"                                  |

## | PyObject_INIT(op, typeobj)                         | "PyObject_Init()"                                  |

## | PyObject_INIT_VAR(op, typeobj, n)                  | "PyObject_InitVar()"                               |

## | PyObject_MALLOC(n)                                 | "PyObject_Malloc()"                                |

## | PyObject_REALLOC(p, n)                             | "PyObject_Realloc()"                               |

## | PyObject_FREE(p)                                   | "PyObject_Free()"                                  |

## | PyObject_DEL(p)                                    | "PyObject_Free()"                                  |

## | PyObject_Del(p)                                    | "PyObject_Free()"                                  |
