---
title: Objetos corrutina
source_url: https://docs.python.org/es/3
source_path: c-api/coro.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 200
---

# Objetos corrutina

Added in version 3.5.

Los objetos de corrutina son las funciones declaradas con un retorno
de palabra clave "async".

type PyCoroObject

   La estructura en C utilizada para objeto corrutina.

PyTypeObject PyCoro_Type

   El tipo de objeto correspondiente a los objetos corrutina.

int PyCoro_CheckExact(PyObject *ob)

   Retorna verdadero si el tipo de *ob* es "PyCoro_Type"; *ob* no debe
   ser "NULL". Esta función siempre finaliza con éxito.

PyObject *PyCoro_New(PyFrameObject *frame, PyObject *name, PyObject *qualname)
    *Return value: New reference.*

   Crea y retorna un nuevo objeto corrutina basado en el objeto
   *frame*, con "__name__" y "__qualname__" establecido en *name* y
   *qualname*. Una referencia a *frame* es robada por esta función. El
   argumento *frame* no debe ser "NULL".
