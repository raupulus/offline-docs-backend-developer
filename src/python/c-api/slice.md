---
title: Objetos rebanada (*slice*)
source_url: https://docs.python.org/es/3
source_path: c-api/slice.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 630
---

# Objetos rebanada (*slice*)

PyTypeObject PySlice_Type
    * Part of the Stable ABI.*

   El objeto tipo para objetos rebanadas. Esto es lo mismo que "slice"
   en la capa de Python.

int PySlice_Check(PyObject *ob)

   Retorna verdadero si *ob* es un objeto rebanada; *ob* no debe ser
   "NULL". Esta función siempre funciona correctamente.

PyObject *PySlice_New(PyObject *start, PyObject *stop, PyObject *step)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna un nuevo objeto rebanada con los valores dados. Los
   parámetros *start*, *stop* y *step* se utilizan como los valores de
   los atributos del objeto rebanada de los mismos nombres. Cualquiera
   de los valores puede ser "NULL", en cuyo caso se usará "None" para
   el atributo correspondiente.

   Retorna "NULL" con una excepción establecida si no se ha podido
   asignar el nuevo objeto.

int PySlice_GetIndices(PyObject *slice, Py_ssize_t length, Py_ssize_t *start, Py_ssize_t *stop, Py_ssize_t *step)
    * Part of the Stable ABI.*

   Recupera los índices *start*, *stop* y *step* del objeto rebanada
   *slice*, suponiendo una secuencia de longitud *length*. Trata los
   índices mayores que *length* como errores.

   Retorna "0" en caso de éxito y "-1" en caso de error sin una
   excepción establecida (a menos que uno de los índices no sea "None"
   y no se haya convertido a un entero, en cuyo caso "- 1" se retorna
   con una excepción establecida).

   Probablemente no quiera usar esta función.

   Distinto en la versión 3.2: El tipo de parámetro para el parámetro
   *slice* era "PySliceObject*" antes.

int PySlice_GetIndicesEx(PyObject *slice, Py_ssize_t length, Py_ssize_t *start, Py_ssize_t *stop, Py_ssize_t *step, Py_ssize_t *slicelength)
    * Part of the Stable ABI.*

   Reemplazo utilizable para "PySlice_GetIndices()". Recupera los
   índices de *start*, *stop*, y *step* del objeto rebanada *slice*
   asumiendo una secuencia de longitud *length*, y almacena la
   longitud de la rebanada en *slicelength*. Los índices fuera de los
   límites se recortan de manera coherente con el manejo de sectores
   normales.

   Retorna "0" en caso de éxito y "-1" en caso de error con una
   excepción establecida.

   Nota:

     Esta función se considera no segura para secuencias
     redimensionables. Su invocación debe ser reemplazada por una
     combinación de "PySlice_Unpack()" y "PySlice_AdjustIndices()"
     donde:

        if (PySlice_GetIndicesEx(slice, length, &start, &stop, &step, &slicelength) < 0) {
            // retorna un error
        }

     es reemplazado por:

        if (PySlice_Unpack(slice, &start, &stop, &step) < 0) {
            // retorna un error
        }
        slicelength = PySlice_AdjustIndices(length, &start, &stop, step);

   Distinto en la versión 3.2: El tipo de parámetro para el parámetro
   *slice* era "PySliceObject*" antes.

   Distinto en la versión 3.6.1: Si "Py_LIMITED_API" no se establece o
   se establece el valor entre "0x03050400" y "0x03060000" (sin
   incluir) o "0x03060100" o un superior "PySlice_GetIndicesEx()" se
   implementa como un macro usando " PySlice_Unpack()" y
   "PySlice_AdjustIndices()". Los argumentos *start*, *stop* y *step*
   se evalúan más de una vez.

   Obsoleto desde la versión 3.6.1: Si "Py_LIMITED_API" se establece
   en un valor menor que "0x03050400" o entre "0x03060000" y
   "0x03060100" (sin incluir) "PySlice_GetIndicesEx()" es una función
   obsoleta.

int PySlice_Unpack(PyObject *slice, Py_ssize_t *start, Py_ssize_t *stop, Py_ssize_t *step)
    * Part of the Stable ABI since version 3.7.*

   Extrae los miembros de datos *start*, *stop*, y *step* de un objeto
   rebanada como enteros en C. Reduce silenciosamente los valores
   mayores que "PY_SSIZE_T_MAX" a "PY_SSIZE_T_MAX", aumenta
   silenciosamente los valores *start* y *stop* inferiores a
   "PY_SSIZE_T_MIN" a "PY_SSIZE_T_MIN", y silenciosamente aumenta los
   valores de *step* a menos de "-PY_SSE" a "-PY_SSIZE_T_MAX".

   Retorna "-1" con una excepción establecida en caso de error, "0" en
   caso de éxito.

   Added in version 3.6.1.

Py_ssize_t PySlice_AdjustIndices(Py_ssize_t length, Py_ssize_t *start, Py_ssize_t *stop, Py_ssize_t step)
    * Part of the Stable ABI since version 3.7.*

   Ajusta los índices de corte de inicio/fin asumiendo una secuencia
   de la longitud especificada. Los índices fuera de los límites se
   recortan de manera coherente con el manejo de sectores normales.

   Retorna la longitud de la rebanada. Siempre exitoso. No llama al
   código de Python.

   Added in version 3.6.1.

## Objeto elipsis

PyTypeObject PyEllipsis_Type
    * Part of the Stable ABI.*

   The type of Python "Ellipsis" object.  Same as "types.EllipsisType"
   in the Python layer.

PyObject *Py_Ellipsis

   El objeto "Ellipsis" de Python.  Este objeto no tiene métodos.  Al
   igual que "Py_None", es un objeto singleton *immortal*.

   Distinto en la versión 3.12: "Py_Ellipsis" es inmortal.
