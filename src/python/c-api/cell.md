---
title: Objetos celda
source_url: https://docs.python.org/es/3
source_path: c-api/cell.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 130
---

# Objetos celda

"Cell" objects are used to implement variables referenced by multiple
scopes. For each such variable, a cell object is created to store the
value; the local variables of each stack frame that references the
value contain a reference to the cells from outer scopes which also
use that variable.  When the value is accessed, the value contained in
the cell is used instead of the cell object itself.  This de-
referencing of the cell object requires support from the generated
byte-code; these are not automatically de-referenced when accessed.
Cell objects are not likely to be useful elsewhere.

type PyCellObject

   La estructura C utilizada para objetos celda.

PyTypeObject PyCell_Type

   El objeto tipo correspondiente a los objetos celda.

int PyCell_Check(PyObject *ob)

   Retorna verdadero si *ob* es un objeto de celda; *ob* no debe ser
   "NULL". Esta función siempre finaliza con éxito.

PyObject *PyCell_New(PyObject *ob)
    *Return value: New reference.*

   Crea y retorna un nuevo objeto de celda que contiene el valor *ob*.
   El parámetro puede ser "NULL".

PyObject *PyCell_Get(PyObject *cell)
    *Return value: New reference.*

   Return the contents of the cell *cell*, which can be "NULL". If
   *cell* is not a cell object, returns "NULL" with an exception set.

PyObject *PyCell_GET(PyObject *cell)
    *Return value: Borrowed reference.*

   Retorna el contenido de la celda *cell*, pero sin verificar que
   *cell* no sea "NULL" y que sea un objeto de celda.

int PyCell_Set(PyObject *cell, PyObject *value)

   Set the contents of the cell object *cell* to *value*.  This
   releases the reference to any current content of the cell. *value*
   may be "NULL".  *cell* must be non-"NULL".

   On success, return "0". If *cell* is not a cell object, set an
   exception and return "-1".

void PyCell_SET(PyObject *cell, PyObject *value)

   Establece el valor del objeto de celda *cell* en el valor *value*.
   No se ajustan los recuentos de referencia y no se realizan
   verificaciones de seguridad; *cell* no debe ser "NULL" y debe ser
   un objeto de celda.
