---
title: Objetos de referencia débil
source_url: https://docs.python.org/es/3
source_path: c-api/weakref.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 790
---

# Objetos de referencia débil

Python soporta *referencias débiles* como objetos de primera clase.
Hay dos tipos de objetos específicos que implementan directamente
referencias débiles. El primero es un objeto con referencia simple, y
el segundo actúa como un proxy del objeto original tanto como pueda.

int PyWeakref_Check(PyObject *ob)

   Retorna un valor distinto de cero si *ob* es una referencia o un
   objeto proxy. Esta función siempre finaliza con éxito.

int PyWeakref_CheckRef(PyObject *ob)

   Return non-zero if *ob* is a reference object or a subclass of the
   reference type.  This function always succeeds.

int PyWeakref_CheckRefExact(PyObject *ob)

   Return non-zero if *ob* is a reference object, but not a subclass
   of the reference type.  This function always succeeds.

int PyWeakref_CheckProxy(PyObject *ob)

   Retorna un valor distinto de cero si *ob* es un objeto proxy. Esta
   función siempre finaliza con éxito.

PyObject *PyWeakref_NewRef(PyObject *ob, PyObject *callback)
    *Return value: New reference.** Part of the Stable ABI.*

   Return a weak reference object for the object *ob*.  This will
   always return a new reference, but is not guaranteed to create a
   new object; an existing reference object may be returned.  The
   second parameter, *callback*, can be a callable object that
   receives notification when *ob* is garbage collected; it should
   accept a single parameter, which will be the weak reference object
   itself. *callback* may also be "None" or "NULL".  If *ob* is not a
   weakly referenceable object, this will raise "TypeError" and return
   "NULL".

   Ver también:

     "PyType_SUPPORTS_WEAKREFS()" for checking if *ob* is weakly
     referenceable.

PyObject *PyWeakref_NewProxy(PyObject *ob, PyObject *callback)
    *Return value: New reference.** Part of the Stable ABI.*

   Return a weak reference proxy object for the object *ob*.  This
   will always return a new reference, but is not guaranteed to create
   a new object; an existing proxy object may be returned.  The second
   parameter, *callback*, can be a callable object that receives
   notification when *ob* is garbage collected; it should accept a
   single parameter, which will be the weak reference object itself.
   *callback* may also be "None" or "NULL".  If *ob* weakly
   referenceable object, this will raise "TypeError" and return
   "NULL".

   Ver también:

     "PyType_SUPPORTS_WEAKREFS()" for checking if *ob* is weakly
     referenceable.

int PyWeakref_GetRef(PyObject *ref, PyObject **pobj)
    * Part of the Stable ABI since version 3.13.*

   Obtiene un *strong reference* al objeto referenciado desde una
   referencia débil, *ref*, en **pobj*.

   * En caso de éxito, asigna **pobj* en un nuevo *strong reference*
     al objeto referenciado y retorna 1.

   * Si la referencia está inactiva, asigna **pobj* a "NULL" y retorna
     0.

   * En caso de error, lanza una excepción y devuelve -1.

   Added in version 3.13.

PyObject *PyWeakref_GetObject(PyObject *ref)
    *Return value: Borrowed reference.** Part of the Stable ABI.*

   Retorna un *borrowed reference* del objeto referenciado desde una
   referencia débil, *ref*. Si el referente ya no está activo, retorna
   "Py_None".

   Nota:

     Esta función retorna una referencia *borrowed reference* al
     objeto referenciado. Esto significa que siempre debe llamar a
     "Py_INCREF()" sobre el objeto excepto cuando no pueda ser
     destruido antes del último uso de la referencia prestada.

   Deprecated since version 3.13, will be removed in version 3.15:
   Utiliza "PyWeakref_GetRef()" en su lugar.

PyObject *PyWeakref_GET_OBJECT(PyObject *ref)
    *Return value: Borrowed reference.*

   Similar a "PyWeakref_GetObject()", pero no realiza ninguna
   comprobación de errores.

   Deprecated since version 3.13, will be removed in version 3.15:
   Utiliza "PyWeakref_GetRef()" en su lugar.

int PyWeakref_IsDead(PyObject *ref)

   Test if the weak reference *ref* is dead. Returns 1 if the
   reference is dead, 0 if it is alive, and -1 with an error set if
   *ref* is not a weak reference object.

   Added in version 3.14.

void PyObject_ClearWeakRefs(PyObject *object)
    * Part of the Stable ABI.*

   Esta función es invocada por el gestor "tp_dealloc" para limpiar
   referencias débiles.

   Esto recorre las referencias débiles de *object* e invoca
   retrollamadas para aquellas referencias que tengan una. Retorna
   cuando se han intentado todas las retrollamadas.

void PyUnstable_Object_ClearWeakRefsNoCallbacks(PyObject *object)

   *This is Unstable API. It may change without warning in minor
   releases.*

   Borra las referencias débiles para *object* sin llamar a las
   retrollamadas.

   Esta función es invocada por el gestor "tp_dealloc" para tipos con
   finalizadores (i.e., "__del__()"). El gestor de esos objetos
   primero llama a "PyObject_ClearWeakRefs()" para borrar las
   referencias débiles y llamar a sus callbacks, luego al finalizador,
   y finalmente a esta función para borrar cualquier referencia débil
   que pueda haber sido creada por el finalizador.

   En la mayoría de los casos, es más apropiado utilizar
   "PyObject_ClearWeakRefs()" para borrar las referencias débiles en
   lugar de esta función.

   Added in version 3.13.
