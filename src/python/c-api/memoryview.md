---
title: Objetos de vista de memoria (*MemoryView*)
source_url: https://docs.python.org/es/3
source_path: c-api/memoryview.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 480
---

# Objetos de vista de memoria (*MemoryView*)

Un objeto "memoryview" expone la interfaz de búfer a nivel de C como
un objeto Python que luego puede pasarse como cualquier otro objeto.

PyTypeObject PyMemoryView_Type
    * Part of the Stable ABI.*

   This instance of "PyTypeObject" represents the Python memoryview
   type. This is the same object as "memoryview" in the Python layer.

PyObject *PyMemoryView_FromObject(PyObject *obj)
    *Return value: New reference.** Part of the Stable ABI.*

   Crea un objeto de vista de memoria *memoryview* a partir de un
   objeto que proporciona la interfaz del búfer. Si *obj* admite
   exportaciones de búfer de escritura, el objeto de vista de memoria
   será de lectura/escritura, de lo contrario puede ser de solo
   lectura o de lectura/escritura a discreción del exportador.

PyBUF_READ
    * Part of the Stable ABI since version 3.11.*

   Indicador para solicitar un búfer de solo lectura.

PyBUF_WRITE
    * Part of the Stable ABI since version 3.11.*

   Indicador para solicitar un búfer escribible.

PyObject *PyMemoryView_FromMemory(char *mem, Py_ssize_t size, int flags)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.7.*

   Crea un objeto de vista de memoria usando *mem* como el búfer
   subyacente. *flags* pueden ser uno de "PyBUF_READ" o "PyBUF_WRITE".

   Added in version 3.3.

PyObject *PyMemoryView_FromBuffer(const Py_buffer *view)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.11.*

   Crea un objeto de vista de memoria que ajuste la estructura de
   búfer dada *view*. Para memorias intermedias de bytes simples,
   "PyMemoryView_FromMemory()" es la función preferida.

PyObject *PyMemoryView_GetContiguous(PyObject *obj, int buffertype, char order)
    *Return value: New reference.** Part of the Stable ABI.*

   Crea un objeto de vista de memoria *memoryview* para un fragmento
   de memoria contiguo (*contiguous*, en *order* 'C' o 'F' de Fortran)
   desde un objeto que define la interfaz del búfer. Si la memoria es
   contigua, el objeto de vista de memoria apunta a la memoria
   original. De lo contrario, se realiza una copia y la vista de
   memoria apunta a un nuevo objeto de bytes.

   *buffertype* puede ser uno de "PyBUF_READ" o "PyBUF_WRITE".

int PyMemoryView_Check(PyObject *obj)

   Retorna verdadero si el objeto *obj* es un objeto de vista de
   memoria. Actualmente no está permitido crear subclases de
   "memoryview". Esta función siempre finaliza con éxito.

Py_buffer *PyMemoryView_GET_BUFFER(PyObject *mview)

   Retorna un puntero a la copia privada de la vista de memoria del
   búfer del exportador. *mview* **debe** ser una instancia de
   *memoryview*; este macro no verifica su tipo, debe hacerlo usted
   mismo o correrá el riesgo de fallas.

PyObject *PyMemoryView_GET_BASE(PyObject *mview)

   Retorna un puntero al objeto de exportación en el que se basa la
   vista de memoria o "NULL" si la vista de memoria ha sido creada por
   una de las funciones "PyMemoryView_FromMemory()" o
   "PyMemoryView_FromBuffer()". *mview* **debe** ser una instancia de
   *memoryview*.
