---
title: Objetos generadores
source_url: https://docs.python.org/es/3
source_path: c-api/gen.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 320
---

# Objetos generadores

Los objetos generadores son lo que Python usa para implementar
iteradores generadores. Normalmente se crean iterando sobre una
función que produce valores, en lugar de llamar explícitamente
"PyGen_New()" o "PyGen_NewWithQualName()".

type PyGenObject

   La estructura en C utilizada para los objetos generadores.

PyTypeObject PyGen_Type

   El objeto tipo correspondiente a los objetos generadores.

int PyGen_Check(PyObject *ob)

   Retorna verdadero si *ob* es un objeto generador; *ob* no debe ser
   "NULL". Esta función siempre finaliza con éxito.

int PyGen_CheckExact(PyObject *ob)

   Retorna verdadero si el tipo de *ob* es "PyGen_Type"; *ob* no debe
   ser "NULL". Esta función siempre finaliza con éxito.

PyObject *PyGen_New(PyFrameObject *frame)
    *Return value: New reference.*

   Create and return a new generator object based on the *frame*
   object. A reference to *frame* is "*stolen*" by this function (even
   on error). The argument must not be "NULL".

PyObject *PyGen_NewWithQualName(PyFrameObject *frame, PyObject *name, PyObject *qualname)
    *Return value: New reference.*

   Create and return a new generator object based on the *frame*
   object, with "__name__" and "__qualname__" set to *name* and
   *qualname*. A reference to *frame* is "*stolen*" by this function
   (even on error).  The *frame* argument must not be "NULL".

PyCodeObject *PyGen_GetCode(PyGenObject *gen)

   Return a new *strong reference* to the code object wrapped by
   *gen*. This function always succeeds.

## Asynchronous Generator Objects

Ver también: **PEP 525**

PyTypeObject PyAsyncGen_Type

   The type object corresponding to asynchronous generator objects.
   This is available as "types.AsyncGeneratorType" in the Python
   layer.

   Added in version 3.6.

PyObject *PyAsyncGen_New(PyFrameObject *frame, PyObject *name, PyObject *qualname)

   Create a new asynchronous generator wrapping *frame*, with
   "__name__" and "__qualname__" set to *name* and *qualname*. *frame*
   is "*stolen*" by this function (even on error) and must not be
   "NULL".

   On success, this function returns a *strong reference* to the new
   asynchronous generator. On failure, this function returns "NULL"
   with an exception set.

   Added in version 3.6.

int PyAsyncGen_CheckExact(PyObject *op)

   Return true if *op* is an asynchronous generator object, false
   otherwise. This function always succeeds.

   Added in version 3.6.

## Deprecated API

PyAsyncGenASend_CheckExact(op)

   This is an API that was included in Python's C API by mistake.

   It is solely here for completeness; do not use this API.

   Soft deprecated since version 3.14.
