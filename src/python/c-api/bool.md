---
title: Objetos booleanos
source_url: https://docs.python.org/es/3
source_path: c-api/bool.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 70
---

# Objetos booleanos

Los booleanos en Python se implementan como una subclase de enteros.
Solo hay dos booleanos "Py_False" y "Py_True". Como tal, las funciones
normales de creación y eliminación no se aplican a los booleanos. Sin
embargo, los siguientes macros están disponibles.

PyTypeObject PyBool_Type
    * Part of the Stable ABI.*

   Esta instancia de "PyTypeObject" representa el tipo booleano de
   Python; es el mismo objeto que "bool" en la capa de Python.

int PyBool_Check(PyObject *o)

   Retorna verdadero si *o* es de tipo "PyBool_Type". Esta función
   siempre finaliza con éxito.

PyObject *Py_False

   The Python "False" object.  This object has no methods and is
   *immortal*.

   Distinto en la versión 3.12: "Py_False" is *immortal*.

PyObject *Py_True

   The Python "True" object.  This object has no methods and is
   *immortal*.

   Distinto en la versión 3.12: "Py_True" is *immortal*.

Py_RETURN_FALSE

   Retorna "Py_False" desde una función.

Py_RETURN_TRUE

   Retorna "Py_True" desde una función..

PyObject *PyBool_FromLong(long v)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna "Py_True" o "Py_False", dependiendo del valor verdadero de
   *v*.
