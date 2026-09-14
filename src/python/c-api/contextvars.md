---
title: Objetos de variables de contexto
source_url: https://docs.python.org/es/3
source_path: c-api/contextvars.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 180
---

# Objetos de variables de contexto

Added in version 3.7.

Distinto en la versión 3.7.1:

Nota:

  En Python 3.7.1, las firmas de todas las variables de contexto C
  APIs fueron **cambiadas** para usar punteros "PyObject" en lugar de
  "PyContext", "PyContextVar", y "PyContextToken", por ejemplo:

     // en 3.7.0:
     PyContext *PyContext_New(void);

     // en 3.7.1+:
     PyObject *PyContext_New(void);

  Ver bpo-34762 para más detalles.

Esta sección detalla la API pública de C para el módulo "contextvars".

type PyContext

   La estructura C utilizada para representar un objeto
   "contextvars.Context".

type PyContextVar

   La estructura C utilizada para representar un objeto
   "contextvars.ContextVar".

type PyContextToken

   La estructura C solía representar un objeto "contextvars.Token".

PyTypeObject PyContext_Type

   El objeto de tipo que representa el tipo *context*.

PyTypeObject PyContextVar_Type

   El objeto tipo que representa el tipo *variable de contexto*.

PyTypeObject PyContextToken_Type

   El tipo objeto que representa el tipo *token de variable de
   contexto*.

Macros de verificación de tipo:

int PyContext_CheckExact(PyObject *o)

   Retorna verdadero si *o* es de tipo "PyContext_Type". *o* no debe
   ser "NULL". Esta función siempre finaliza con éxito.

int PyContextVar_CheckExact(PyObject *o)

   Retorna verdadero si *o* es de tipo "PyContextVar_Type". *o* no
   debe ser "NULL". Esta función siempre finaliza con éxito.

int PyContextToken_CheckExact(PyObject *o)

   Retorna verdadero si *o* es de tipo "PyContextToken_Type". *o* no
   debe ser "NULL". Esta función siempre finaliza con éxito.

Funciones de gestión de objetos de contexto:

PyObject *PyContext_New(void)
    *Return value: New reference.*

   Crea un nuevo objeto de contexto vacío. Retorna "NULL" si se ha
   producido un error.

PyObject *PyContext_Copy(PyObject *ctx)
    *Return value: New reference.*

   Crea una copia superficial del objeto de contexto *ctx* pasado.
   Retorna "NULL" si se ha producido un error.

PyObject *PyContext_CopyCurrent(void)
    *Return value: New reference.*

   Crea una copia superficial del contexto actual del hilo. Retorna
   "NULL" si se ha producido un error.

int PyContext_Enter(PyObject *ctx)

   Establece *ctx* como el contexto actual para el hilo actual.
   Retorna "0" en caso de éxito y "-1" en caso de error.

int PyContext_Exit(PyObject *ctx)

   Desactiva el contexto *ctx* y restaura el contexto anterior como el
   contexto actual para el hilo actual. Retorna "0" en caso de éxito y
   "-1" en caso de error.

int PyContext_AddWatcher(PyContext_WatchCallback callback)

   Register *callback* as a context object watcher for the current
   interpreter. Return an ID which may be passed to
   "PyContext_ClearWatcher()". In case of error (e.g. no more watcher
   IDs available), return "-1" and set an exception.

   Added in version 3.14.

int PyContext_ClearWatcher(int watcher_id)

   Clear watcher identified by *watcher_id* previously returned from
   "PyContext_AddWatcher()" for the current interpreter. Return "0" on
   success, or "-1" and set an exception on error (e.g. if the given
   *watcher_id* was never registered.)

   Added in version 3.14.

type PyContextEvent

   Enumeration of possible context object watcher events:

   * "Py_CONTEXT_SWITCHED": The *current context* has switched to a
     different context.  The object passed to the watch callback is
     the now-current "contextvars.Context" object, or None if no
     context is current.

   Added in version 3.14.

typedef int (*PyContext_WatchCallback)(PyContextEvent event, PyObject *obj)

   Context object watcher callback function.  The object passed to the
   callback is event-specific; see "PyContextEvent" for details.

   If the callback returns with an exception set, it must return "-1";
   this exception will be printed as an unraisable exception using
   "PyErr_FormatUnraisable()". Otherwise it should return "0".

   There may already be a pending exception set on entry to the
   callback. In this case, the callback should return "0" with the
   same exception still set. This means the callback may not call any
   other API that can set an exception unless it saves and clears the
   exception state first, and restores it before returning.

   Added in version 3.14.

Funciones variables de contexto:

PyObject *PyContextVar_New(const char *name, PyObject *def)
    *Return value: New reference.*

   Crea un nuevo objeto "ContextVar". El parámetro *name* se usa para
   propósitos de introspección y depuración. El parámetro *def*
   especifica el valor predeterminado para la variable de contexto, o
   "NULL" para no especificar un valor predeterminado. Si se ha
   producido un error, esta función retorna "NULL".

int PyContextVar_Get(PyObject *var, PyObject *default_value, PyObject **value)

   Obtiene el valor de una variable de contexto. Retorna "-1" si se
   produjo un error durante la búsqueda y "0" si no se produjo ningún
   error, se haya encontrado o no un valor.

   Si se encontró la variable de contexto, *value* será un puntero a
   ella. Si la variable de contexto *not* se encontró, *value*
   apuntará a:

   * *default_value*, si no es "NULL";

   * el valor predeterminado de *var*, si no es "NULL";

   * "NULL"

   A excepción de "NULL", la función retorna una nueva referencia.

PyObject *PyContextVar_Set(PyObject *var, PyObject *value)
    *Return value: New reference.*

   Establece el valor de *var* en *value* en el contexto actual.
   Retorna un nuevo objeto token para este cambio, o "NULL" si se ha
   producido un error.

int PyContextVar_Reset(PyObject *var, PyObject *token)

   Restablece el estado de la variable de contexto *var* a la que
   estaba antes "PyContextVar_Set()" que retornó el *token* fue
   llamado. Esta función retorna "0" en caso de éxito y "-1" en caso
   de error.
