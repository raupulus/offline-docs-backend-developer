---
title: Soporte de empaquetado (*marshalling*) de datos
source_url: https://docs.python.org/es/3
source_path: c-api/marshal.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 460
---

# Soporte de empaquetado (*marshalling*) de datos

Estas rutinas permiten que el código C funcione con objetos
serializados utilizando el mismo formato de datos que el módulo
"marshal". Hay funciones para escribir datos en el formato de
serialización y funciones adicionales que se pueden usar para volver a
leer los datos. Los archivos utilizados para almacenar datos ordenados
deben abrirse en modo binario.

Los valores numéricos se almacenan con el byte menos significativo
primero.

The module supports several versions of the data format; see the
"Python module documentation" for details.

Py_MARSHAL_VERSION

   The current format version. See "marshal.version".

void PyMarshal_WriteLongToFile(long value, FILE *file, int version)

   Empaqueta (*marshal*) un entero *value* long a un archivo *file*.
   Esto solo escribirá los 32 bits menos significativos de *value*;
   sin importar el tamaño del tipo long nativo. *version* indica el
   formato del archivo.

   Esta función puede fallar, en cuyo caso establece el indicador de
   error. Utiliza "PyErr_Occurred()" para comprobarlo.

void PyMarshal_WriteObjectToFile(PyObject *value, FILE *file, int version)

   Empaqueta (*marshal*) un objeto Python, *value*, a un archivo
   *file*. *version* indica el formato del archivo.

   Esta función puede fallar, en cuyo caso establece el indicador de
   error. Utiliza "PyErr_Occurred()" para comprobarlo.

PyObject *PyMarshal_WriteObjectToString(PyObject *value, int version)
    *Return value: New reference.*

   Retorna un objeto de bytes que contiene la representación
   empaquetada (*marshalled*) de *value*. *version* indica el formato
   del archivo.

Las siguientes funciones permiten volver a leer los valores
empaquetados (*marshalled*).

long PyMarshal_ReadLongFromFile(FILE *file)

   Retorna un entero long de C desde el flujo de datos FILE* abierto
   para lectura. Solo se puede leer un valor de 32 bits con esta
   función, independientemente del tamaño nativo del tipo long.

   En caso de error, establece la excepción apropiada ("EOFError") y
   retorna "-1".

int PyMarshal_ReadShortFromFile(FILE *file)

   Retorna un entero short de C desde el flujo de datos FILE* abierto
   para lectura. Solo se puede leer un valor de 16 bits con esta
   función, independientemente del tamaño nativo del tipo short.

   En caso de error, establece la excepción apropiada ("EOFError") y
   retorna "-1".

PyObject *PyMarshal_ReadObjectFromFile(FILE *file)
    *Return value: New reference.*

   Retorna un objeto Python del flujo de datos FILE* abierto para
   lectura.

   En caso de error, establece la excepción apropiada ("EOFError",
   "ValueError" o "TypeError") y retorna "NULL".

PyObject *PyMarshal_ReadLastObjectFromFile(FILE *file)
    *Return value: New reference.*

   Return a Python object from the data stream in a FILE* opened for
   reading.  Unlike "PyMarshal_ReadObjectFromFile()", this function
   assumes that no further objects will be read from the file,
   allowing it to aggressively load file data into memory so that the
   de-serialization can operate from data in memory rather than
   reading a byte at a time from the file.  Only use this variant if
   you are certain that you won't be reading anything else from the
   file.

   En caso de error, establece la excepción apropiada ("EOFError",
   "ValueError" o "TypeError") y retorna "NULL".

PyObject *PyMarshal_ReadObjectFromString(const char *data, Py_ssize_t len)
    *Return value: New reference.*

   Retorna un objeto Python del flujo de datos en un búfer de bytes
   que contiene *len* bytes a los que apunta *data*.

   En caso de error, establece la excepción apropiada ("EOFError",
   "ValueError" o "TypeError") y retorna "NULL".
