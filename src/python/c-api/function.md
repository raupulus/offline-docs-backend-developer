---
title: Objetos función
source_url: https://docs.python.org/es/3
source_path: c-api/function.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 300
---

# Objetos función

Hay algunas funciones específicas para las funciones de Python.

type PyFunctionObject

   La estructura C utilizada para las funciones.

PyTypeObject PyFunction_Type

   Esta es una instancia de "PyTypeObject" y representa el tipo
   función de Python. Está expuesto a los programadores de Python como
   "types.FunctionType".

int PyFunction_Check(PyObject *o)

   Retorna verdadero si *o* es un objeto función (tiene tipo
   "PyFunction_Type"). El parámetro no debe ser "NULL". Esta función
   siempre finaliza con éxito.

PyObject *PyFunction_New(PyObject *code, PyObject *globals)
    *Return value: New reference.*

   Retorna un nuevo objeto función asociado con el objeto código
   *code*. *globals* debe ser un diccionario con las variables
   globales accesibles para la función.

   El docstring y el nombre de la función se obtienen del objeto
   código. "__module__" se obtiene de *globals*. Los argumentos por
   defecto, anotaciones y clausura se establecen en "NULL".
   "__qualname__" se establece en el mismo valor que el campo
   "co_qualname" del objeto código.

PyObject *PyFunction_NewWithQualName(PyObject *code, PyObject *globals, PyObject *qualname)
    *Return value: New reference.*

   Como "PyFunction_New()", pero también permite configurar el
   atributo "__qualname__" del objeto función. *qualname* debe ser un
   objeto unicode o "NULL"; si es "NULL", el atributo "__qualname__"
   se establece en el mismo valor que el campo "co_qualname" del
   objeto código.

   Added in version 3.3.

PyObject *PyFunction_GetCode(PyObject *op)
    *Return value: Borrowed reference.*

   Retorna el objeto código asociado con el objeto función *op*.

PyObject *PyFunction_GetGlobals(PyObject *op)
    *Return value: Borrowed reference.*

   Retorna el diccionario global asociado con el objeto función *op*.

PyObject *PyFunction_GetModule(PyObject *op)
    *Return value: Borrowed reference.*

   Retorna una *referencia prestada* al atributo "__module__" del
   objeto función *op*. Puede ser *NULL*.

   Esto es normalmente una "cadena de caracteres" que contiene el
   nombre del módulo, pero se puede establecer en cualquier otro
   objeto mediante código Python.

PyObject *PyFunction_GetDefaults(PyObject *op)
    *Return value: Borrowed reference.*

   Retorna los valores predeterminados del argumento del objeto
   función *op*. Esto puede ser una tupla de argumentos o "NULL".

int PyFunction_SetDefaults(PyObject *op, PyObject *defaults)

   Establece los valores predeterminados del argumento para el objeto
   función *op*. *defaults* deben ser "Py_None" o una tupla.

   Lanza "SystemError" y retorna "-1" en caso de error.

void PyFunction_SetVectorcall(PyFunctionObject *func, vectorcallfunc vectorcall)

   Establece el campo vectorcall de un objeto función dado *func*.

   Advertencia: ¡las extensiones que usan esta API deben preservar el
   comportamiento de la función vectorcall inalterada (por defecto)!

   Added in version 3.12.

PyObject *PyFunction_GetKwDefaults(PyObject *op)
    *Return value: Borrowed reference.*

   Return the keyword-only argument default values of the function
   object *op*. This can be a dictionary of arguments or "NULL".

int PyFunction_SetKwDefaults(PyObject *op, PyObject *defaults)

   Set the keyword-only argument default values of the function object
   *op*. *defaults* must be a dictionary of keyword-only arguments or
   "Py_None".

   This function returns "0" on success, and returns "-1" with an
   exception set on failure.

PyObject *PyFunction_GetClosure(PyObject *op)
    *Return value: Borrowed reference.*

   Retorna el cierre asociado con el objeto función *op*. Esto puede
   ser "NULL" o una tupla de objetos celda.

int PyFunction_SetClosure(PyObject *op, PyObject *closure)

   Establece el cierre asociado con el objeto función *op*. *cierre*
   debe ser "Py_None" o una tupla de objetos celda.

   Lanza "SystemError" y retorna "-1" en caso de error.

PyObject *PyFunction_GetAnnotations(PyObject *op)
    *Return value: Borrowed reference.*

   Retorna las anotaciones del objeto función *op*. Este puede ser un
   diccionario mutable o "NULL".

int PyFunction_SetAnnotations(PyObject *op, PyObject *annotations)

   Establece las anotaciones para el objeto función *op*.
   *annotations* debe ser un diccionario o "Py_None".

   Lanza "SystemError" y retorna "-1" en caso de error.

PyObject *PyFunction_GET_CODE(PyObject *op)
PyObject *PyFunction_GET_GLOBALS(PyObject *op)
PyObject *PyFunction_GET_MODULE(PyObject *op)
PyObject *PyFunction_GET_DEFAULTS(PyObject *op)
PyObject *PyFunction_GET_KW_DEFAULTS(PyObject *op)
PyObject *PyFunction_GET_CLOSURE(PyObject *op)
PyObject *PyFunction_GET_ANNOTATIONS(PyObject *op)
    *Return value: Borrowed reference.*

   These functions are similar to their "PyFunction_Get*"
   counterparts, but do not do type checking. Passing anything other
   than an instance of "PyFunction_Type" is undefined behavior.

int PyFunction_AddWatcher(PyFunction_WatchCallback callback)

   Registra *callback* como un observador de función para el
   intérprete actual. Retorna un ID que puede pasarse a
   "PyFunction_ClearWatcher()". En caso de error (por ejemplo, no hay
   más IDs de observador disponibles), retorna "-1" y establece una
   excepción.

   Added in version 3.12.

int PyFunction_ClearWatcher(int watcher_id)

   Limpia el observador identificado por *watcher_id* previamente
   retornado de "PyFunction_AddWatcher()" para el intérprete actual.
   Retorna "0" en caso de éxito, o "-1" y establece una excepción en
   caso de error (por ejemplo, si el *watcher_id* dado nunca fue
   registrado).

   Added in version 3.12.

type PyFunction_WatchEvent

      Enumeration of possible function watcher events:

      * "PyFunction_EVENT_CREATE"

      * "PyFunction_EVENT_DESTROY"

      * "PyFunction_EVENT_MODIFY_CODE"

      * "PyFunction_EVENT_MODIFY_DEFAULTS"

      * "PyFunction_EVENT_MODIFY_KWDEFAULTS"

   Added in version 3.12.

typedef int (*PyFunction_WatchCallback)(PyFunction_WatchEvent event, PyFunctionObject *func, PyObject *new_value)

   Tipo de una función callback de observador de función.

   Si *event* es "PyFunction_EVENT_CREATE" o
   "PyFunction_EVENT_DESTROY" entonces *new_value* será "NULL". De lo
   contrario, *new_value* mantendrá una *referencia prestada* al nuevo
   valor que está a punto de almacenarse en *func* para el atributo
   que se está modificando.

   El callback puede inspeccionar pero no debe modificar *func*;
   hacerlo podría tener efectos impredecibles, incluyendo recursión
   infinita.

   If *event* is "PyFunction_EVENT_CREATE", then the callback is
   invoked after *func* has been fully initialized. Otherwise, the
   callback is invoked before the modification to *func* takes place,
   so the prior state of *func* can be inspected. The runtime is
   permitted to optimize away the creation of function objects when
   possible. In such cases no event will be emitted. Although this
   creates the possibility of an observable difference of runtime
   behavior depending on optimization decisions, it does not change
   the semantics of the Python code being executed.

   Si *event* es "PyFunction_EVENT_DESTROY", tomar una referencia en
   el callback a la función a punto de ser destruida la resucitará,
   evitando que sea liberada en este momento. Cuando el objeto
   resucitado sea destruido más tarde, cualquier callback observador
   activo en ese momento será llamado de nuevo.

   Si el callback establece una excepción, debe retornar "-1"; esta
   excepción se imprimirá como una excepción no lanzable usando
   "PyErr_WriteUnraisable()". De lo contrario debe retornar "0".

   Puede haber ya una excepción pendiente establecida al entrar al
   callback. En este caso, el callback debe retornar "0" con la misma
   excepción aún establecida. Esto significa que el callback no puede
   llamar a ninguna otra API que pueda establecer una excepción a
   menos que guarde y borre el estado de la excepción primero, y lo
   restaure antes de retornar.

   Added in version 3.12.
