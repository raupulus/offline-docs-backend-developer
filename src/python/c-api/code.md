---
title: Objetos código
source_url: https://docs.python.org/es/3
source_path: c-api/code.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 140
---

# Objetos código

Los objetos código son un detalle de bajo nivel de la implementación
de CPython. Cada uno representa un fragmento de código ejecutable que
aún no se ha vinculado a una función.

type PyCodeObject

   La estructura en C de los objetos utilizados para describir objetos
   código. Los campos de este tipo están sujetos a cambios en
   cualquier momento.

PyTypeObject PyCode_Type

   This is an instance of "PyTypeObject" representing the Python code
   object.

int PyCode_Check(PyObject *co)

   Return true if *co* is a code object. This function always
   succeeds.

Py_ssize_t PyCode_GetNumFree(PyCodeObject *co)

   Return the number of *free (closure) variables* in a code object.

int PyUnstable_Code_GetFirstFree(PyCodeObject *co)

   *This is Unstable API. It may change without warning in minor
   releases.*

   Return the position of the first *free (closure) variable* in a
   code object.

   Distinto en la versión 3.13: Renamed from "PyCode_GetFirstFree" as
   part of Unstable C API. The old name is deprecated, but will remain
   available until the signature changes again.

PyCodeObject *PyUnstable_Code_New(int argcount, int kwonlyargcount, int nlocals, int stacksize, int flags, PyObject *code, PyObject *consts, PyObject *names, PyObject *varnames, PyObject *freevars, PyObject *cellvars, PyObject *filename, PyObject *name, PyObject *qualname, int firstlineno, PyObject *linetable, PyObject *exceptiontable)

   *This is Unstable API. It may change without warning in minor
   releases.*

   Return a new code object.  If you need a dummy code object to
   create a frame, use "PyCode_NewEmpty()" instead.

   Since the definition of the bytecode changes often, calling
   "PyUnstable_Code_New()" directly can bind you to a precise Python
   version.

   The many arguments of this function are inter-dependent in complex
   ways, meaning that subtle changes to values are likely to result in
   incorrect execution or VM crashes. Use this function only with
   extreme care.

   Distinto en la versión 3.11: Added "qualname" and "exceptiontable"
   parameters.

   Distinto en la versión 3.12: Renamed from "PyCode_New" as part of
   Unstable C API. The old name is deprecated, but will remain
   available until the signature changes again.

PyCodeObject *PyUnstable_Code_NewWithPosOnlyArgs(int argcount, int posonlyargcount, int kwonlyargcount, int nlocals, int stacksize, int flags, PyObject *code, PyObject *consts, PyObject *names, PyObject *varnames, PyObject *freevars, PyObject *cellvars, PyObject *filename, PyObject *name, PyObject *qualname, int firstlineno, PyObject *linetable, PyObject *exceptiontable)

   *This is Unstable API. It may change without warning in minor
   releases.*

   Similar to "PyUnstable_Code_New()", but with an extra
   "posonlyargcount" for positional-only arguments. The same caveats
   that apply to "PyUnstable_Code_New" also apply to this function.

   Added in version 3.8: as "PyCode_NewWithPosOnlyArgs"

   Distinto en la versión 3.11: Added "qualname" and  "exceptiontable"
   parameters.

   Distinto en la versión 3.12: Renamed to
   "PyUnstable_Code_NewWithPosOnlyArgs". The old name is deprecated,
   but will remain available until the signature changes again.

PyCodeObject *PyCode_NewEmpty(const char *filename, const char *funcname, int firstlineno)
    *Return value: New reference.*

   Retorna un nuevo objeto de código vacío con el nombre de archivo
   especificado, el nombre de la función y el número de la primera
   línea. Si el objeto código resultante es ejecutado, lanzará una
   "Exception".

int PyCode_Addr2Line(PyCodeObject *co, int byte_offset)

   Retorna el número de línea de la instrucción que se produce en o
   antes de "byte_offset" y finaliza después. Si solo necesita el
   número de línea de un marco, use "PyFrame_GetLineNumber()" en su
   lugar.

   For efficiently iterating over the line numbers in a code object,
   use **the API described in PEP 626**.

int PyCode_Addr2Location(PyObject *co, int byte_offset, int *start_line, int *start_column, int *end_line, int *end_column)

   Establece los punteros "int" pasados en los números de línea y
   columna del código fuente para las instrucciones en "byte_offset".
   Establece el valor en "0" cuando la información no está disponible
   para algún elemento en particular.

   Retorna "1" si la función fue exitosa y "0" de lo contrario.

   Added in version 3.11.

PyObject *PyCode_GetCode(PyCodeObject *co)

   Equivalente al código Python "getattr(co, 'co_code')". Retorna una
   referencia fuerte a un "PyBytesObject" representando el bytecode en
   un objecto código. En caso de error se retorna "NULL" y se lanza
   una excepción.

   Este "PyBytesObject" puede ser creado a pedido del intérprete y no
   necesariamente representa el bytecode que es realmente ejecutado
   por CPython. Los casos de uso principales para esta función son
   depuradores y perfiladores.

   Added in version 3.11.

PyObject *PyCode_GetVarnames(PyCodeObject *co)

   Equivalente al código Python "getattr(co, 'co_varnames')". Retorna
   una nueva referencia a un "PyTupleObject" que contiene los nombres
   de las variables locales. En caso de error, retorna "NULL" y lanza
   una excepción.

   Added in version 3.11.

PyObject *PyCode_GetCellvars(PyCodeObject *co)

   Equivalente al código Python "getattr(co, 'co_cellvars')". Retorna
   una nueva referencia a un "PyTupleObject" que contiene los nombres
   de las variables locales referenciadas por funciones anidadas. En
   caso de error, retorna "NULL" y lanza una excepción.

   Added in version 3.11.

PyObject *PyCode_GetFreevars(PyCodeObject *co)

   Equivalent to the Python code "getattr(co, 'co_freevars')". Returns
   a new reference to a "PyTupleObject" containing the names of the
   *free (closure) variables*. On error, "NULL" is returned and an
   exception is raised.

   Added in version 3.11.

int PyCode_AddWatcher(PyCode_WatchCallback callback)

   Register *callback* as a code object watcher for the current
   interpreter. Return an ID which may be passed to
   "PyCode_ClearWatcher()". In case of error (e.g. no more watcher IDs
   available), return "-1" and set an exception.

   Added in version 3.12.

int PyCode_ClearWatcher(int watcher_id)

   Clear watcher identified by *watcher_id* previously returned from
   "PyCode_AddWatcher()" for the current interpreter. Return "0" on
   success, or "-1" and set an exception on error (e.g. if the given
   *watcher_id* was never registered.)

   Added in version 3.12.

type PyCodeEvent

   Enumeration of possible code object watcher events: -
   "PY_CODE_EVENT_CREATE" - "PY_CODE_EVENT_DESTROY"

   Added in version 3.12.

typedef int (*PyCode_WatchCallback)(PyCodeEvent event, PyCodeObject *co)

   Type of a code object watcher callback function.

   If *event* is "PY_CODE_EVENT_CREATE", then the callback is invoked
   after *co* has been fully initialized. Otherwise, the callback is
   invoked before the destruction of *co* takes place, so the prior
   state of *co* can be inspected.

   If *event* is "PY_CODE_EVENT_DESTROY", taking a reference in the
   callback to the about-to-be-destroyed code object will resurrect it
   and prevent it from being freed at this time. When the resurrected
   object is destroyed later, any watcher callbacks active at that
   time will be called again.

   Users of this API should not rely on internal runtime
   implementation details. Such details may include, but are not
   limited to, the exact order and timing of creation and destruction
   of code objects. While changes in these details may result in
   differences observable by watchers (including whether a callback is
   invoked or not), it does not change the semantics of the Python
   code being executed.

   If the callback sets an exception, it must return "-1"; this
   exception will be printed as an unraisable exception using
   "PyErr_WriteUnraisable()". Otherwise it should return "0".

   There may already be a pending exception set on entry to the
   callback. In this case, the callback should return "0" with the
   same exception still set. This means the callback may not call any
   other API that can set an exception unless it saves and clears the
   exception state first, and restores it before returning.

   Added in version 3.12.

PyObject *PyCode_Optimize(PyObject *code, PyObject *consts, PyObject *names, PyObject *lnotab_obj)

   This is a function that does nothing.

   Prior to Python 3.10, this function would perform basic
   optimizations to a code object.

   Distinto en la versión 3.10: This function now does nothing.

   Soft deprecated since version 3.13.

# Code Object Flags

Code objects contain a bit-field of flags, which can be retrieved as
the "co_flags" Python attribute (for example using
"PyObject_GetAttrString()"), and set using a *flags* argument to
"PyUnstable_Code_New()" and similar functions.

Flags whose names start with "CO_FUTURE_" correspond to features
normally selectable by future statements. These flags can be used in
"PyCompilerFlags.cf_flags". Note that many "CO_FUTURE_" flags are
mandatory in current versions of Python, and setting them has no
effect.

The following flags are available. For their meaning, see the linked
documentation of their Python equivalents.

+----------------------------------------------------+----------------------------------------------------+
| Flag                                               | Meaning                                            |
|====================================================|====================================================|
## | CO_OPTIMIZED                                       | "inspect.CO_OPTIMIZED"                             |

## | CO_NEWLOCALS                                       | "inspect.CO_NEWLOCALS"                             |

## | CO_VARARGS                                         | "inspect.CO_VARARGS"                               |

## | CO_VARKEYWORDS                                     | "inspect.CO_VARKEYWORDS"                           |

## | CO_NESTED                                          | "inspect.CO_NESTED"                                |

## | CO_GENERATOR                                       | "inspect.CO_GENERATOR"                             |

## | CO_COROUTINE                                       | "inspect.CO_COROUTINE"                             |

## | CO_ITERABLE_COROUTINE                              | "inspect.CO_ITERABLE_COROUTINE"                    |

## | CO_ASYNC_GENERATOR                                 | "inspect.CO_ASYNC_GENERATOR"                       |

## | CO_HAS_DOCSTRING                                   | "inspect.CO_HAS_DOCSTRING"                         |

## | CO_METHOD                                          | "inspect.CO_METHOD"                                |

## | CO_FUTURE_DIVISION                                 | no effect ("__future__.division")                  |

## | CO_FUTURE_ABSOLUTE_IMPORT                          | no effect ("__future__.absolute_import")           |

## | CO_FUTURE_WITH_STATEMENT                           | no effect ("__future__.with_statement")            |

## | CO_FUTURE_PRINT_FUNCTION                           | no effect ("__future__.print_function")            |

## | CO_FUTURE_UNICODE_LITERALS                         | no effect ("__future__.unicode_literals")          |

## | CO_FUTURE_GENERATOR_STOP                           | no effect ("__future__.generator_stop")            |

## | CO_FUTURE_ANNOTATIONS                              | "__future__.annotations"                           |

# Extra information

To support low-level extensions to frame evaluation, such as external
just-in-time compilers, it is possible to attach arbitrary extra data
to code objects.

These functions are part of the unstable C API tier: this
functionality is a CPython implementation detail, and the API may
change without deprecation warnings.

Py_ssize_t PyUnstable_Eval_RequestCodeExtraIndex(freefunc free)

   *This is Unstable API. It may change without warning in minor
   releases.*

   Return a new opaque index value used to adding data to code
   objects.

   You generally call this function once (per interpreter) and use the
   result with "PyCode_GetExtra" and "PyCode_SetExtra" to manipulate
   data on individual code objects.

   If *free* is not "NULL": when a code object is deallocated, *free*
   will be called on non-"NULL" data stored under the new index. Use
   "Py_DecRef()" when storing "PyObject".

   Added in version 3.6: as "_PyEval_RequestCodeExtraIndex"

   Distinto en la versión 3.12: Renamed to
   "PyUnstable_Eval_RequestCodeExtraIndex". The old private name is
   deprecated, but will be available until the API changes.

int PyUnstable_Code_GetExtra(PyObject *code, Py_ssize_t index, void **extra)

   *This is Unstable API. It may change without warning in minor
   releases.*

   Set *extra* to the extra data stored under the given index. Return
   0 on success. Set an exception and return -1 on failure.

   If no data was set under the index, set *extra* to "NULL" and
   return 0 without setting an exception.

   Added in version 3.6: as "_PyCode_GetExtra"

   Distinto en la versión 3.12: Renamed to "PyUnstable_Code_GetExtra".
   The old private name is deprecated, but will be available until the
   API changes.

int PyUnstable_Code_SetExtra(PyObject *code, Py_ssize_t index, void *extra)

   *This is Unstable API. It may change without warning in minor
   releases.*

   Set the extra data stored under the given index to *extra*. Return
   0 on success. Set an exception and return -1 on failure.

   Added in version 3.6: as "_PyCode_SetExtra"

   Distinto en la versión 3.12: Renamed to "PyUnstable_Code_SetExtra".
   The old private name is deprecated, but will be available until the
   API changes.
