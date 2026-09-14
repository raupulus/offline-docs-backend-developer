---
title: Objetos de método de instancia
source_url: https://docs.python.org/es/3
source_path: c-api/method.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 490
---

# Objetos de método de instancia

An instance method is a wrapper for a "PyCFunction" and the new way to
bind a "PyCFunction" to a class object. It replaces the former call
"PyMethod_New(func, NULL, class)".

PyTypeObject PyInstanceMethod_Type

   Esta instancia de "PyTypeObject" representa el tipo de método de
   instancia de Python. No está expuesto a los programas de Python.

int PyInstanceMethod_Check(PyObject *o)

   Retorna verdadero si *o* es un objeto de método de instancia (tiene
   tipo "PyInstanceMethod_Type"). El parámetro no debe ser "NULL".
   Esta función siempre finaliza con éxito.

PyObject *PyInstanceMethod_New(PyObject *func)
    *Return value: New reference.*

   Return a new instance method object, with *func* being any callable
   object. *func* is the function that will be called when the
   instance method is called.

PyObject *PyInstanceMethod_Function(PyObject *im)
    *Return value: Borrowed reference.*

   Retorna el objeto de función asociado con el método de instancia
   *im*.

PyObject *PyInstanceMethod_GET_FUNCTION(PyObject *im)
    *Return value: Borrowed reference.*

   Versión macro de "PyInstanceMethod_Function()" que evita la
   comprobación de errores.

# Objetos método

Los métodos son objetos de función enlazados. Los métodos siempre
están vinculados a una instancia de una clase definida por el usuario.
Los métodos no vinculados (métodos vinculados a un objeto de clase) ya
no están disponibles.

PyTypeObject PyMethod_Type

   Esta instancia de "PyTypeObject" representa el tipo de método
   Python. Esto está expuesto a los programas de Python como
   "types.MethodType".

int PyMethod_Check(PyObject *o)

   Retorna verdadero si *o* es un objeto de método (tiene tipo
   "PyMethod_Type"). El parámetro no debe ser "NULL". Esta función
   siempre finaliza con éxito.

PyObject *PyMethod_New(PyObject *func, PyObject *self)
    *Return value: New reference.*

   Retorna un nuevo objeto de método, con *func* como cualquier objeto
   invocable y *self* la instancia en la que se debe vincular el
   método. *func* es la función que se llamará cuando se llame al
   método. *self* no debe ser "NULL".

PyObject *PyMethod_Function(PyObject *meth)
    *Return value: Borrowed reference.*

   Retorna el objeto de función asociado con el método *meth*.

PyObject *PyMethod_GET_FUNCTION(PyObject *meth)
    *Return value: Borrowed reference.*

   Versión macro de "PyMethod_Function()" que evita la comprobación de
   errores.

PyObject *PyMethod_Self(PyObject *meth)
    *Return value: Borrowed reference.*

   Retorna la instancia asociada con el método *meth*.

PyObject *PyMethod_GET_SELF(PyObject *meth)
    *Return value: Borrowed reference.*

   Versión macro de "PyMethod_Self()" que evita la comprobación de
   errores.
