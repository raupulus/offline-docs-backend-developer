---
title: Objetos *DateTime*
source_url: https://docs.python.org/es/3
source_path: c-api/datetime.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 220
---

# Objetos *DateTime*

Various date and time objects are supplied by the "datetime" module.
Before using any of these functions, the header file "datetime.h" must
be included in your source (note that this is not included by
"Python.h"), and the macro "PyDateTime_IMPORT" must be invoked,
usually as part of the module initialisation function.  The macro puts
a pointer to a C structure into a static variable, "PyDateTimeAPI",
that is used by the following macros.

PyDateTime_IMPORT()

   Import the datetime C API.

   On success, populate the "PyDateTimeAPI" pointer. On failure, set
   "PyDateTimeAPI" to "NULL" and set an exception. The caller must
   check if an error occurred via "PyErr_Occurred()":

      PyDateTime_IMPORT;
      if (PyErr_Occurred()) { /* cleanup */ }

   Advertencia:

     This is not compatible with subinterpreters.

type PyDateTime_CAPI

   Structure containing the fields for the datetime C API.

   The fields of this structure are private and subject to change.

   Do not use this directly; prefer "PyDateTime_*" APIs instead.

PyDateTime_CAPI *PyDateTimeAPI

   Dynamically allocated object containing the datetime C API.

   This variable is only available once "PyDateTime_IMPORT" succeeds.

type PyDateTime_Date

   Este subtipo de "PyObject" representa un *date object* de Python.

type PyDateTime_DateTime

   Este subtipo de "PyObject" representa un *datetime object* de
   Python.

type PyDateTime_Time

   Este subtipo de "PyObject" representa un *time object* de Python.

type PyDateTime_Delta

   Este subtipo de "PyObject" representa la diferencia entre dos
   valores *datetime*.

PyTypeObject PyDateTime_DateType

   Esta instancia de "PyTypeObject" representa el *date type* de
   Python; es el mismo objeto que "datetime.date" en la capa de
   Python.

PyTypeObject PyDateTime_DateTimeType

   Esta instancia de "PyTypeObject" representa el *datetime type* de
   Python; es el mismo objeto que "datetime.datetime" en la capa de
   Python.

PyTypeObject PyDateTime_TimeType

   Esta instancia de "PyObject" representa el *time type* de Python;
   es el mismo objeto que "datetime.time" en la capa de Python.

PyTypeObject PyDateTime_DeltaType

   This instance of "PyTypeObject" represents the Python type for the
   difference between two datetime values; it is the same object as
   "datetime.timedelta" in the Python layer.

PyTypeObject PyDateTime_TZInfoType

   Esta instancia de "PyTypeObject" representa el tipo de Python de
   *time zone info*; es el mismo objeto que "datetime.tzinfo" de la
   capa de Python.

Macro para acceder al singleton UTC:

PyObject *PyDateTime_TimeZone_UTC

   Retorna la zona horaria singleton que representa UTC, el mismo
   objeto que "datetime.timezone.utc".

   Added in version 3.7.

Macros de verificación de tipo:

int PyDate_Check(PyObject *ob)

   Retorna verdadero si *ob* es de tipo "PyDateTime_DateType" o un
   subtipo de "PyDateTime_DateType". *ob* no debe ser "NULL". Esta
   función siempre finaliza con éxito.

int PyDate_CheckExact(PyObject *ob)

   Retorna verdadero si *ob* es de tipo "PyDateTime_DateType". *ob* no
   debe ser "NULL". Esta función siempre finaliza con éxito.

int PyDateTime_Check(PyObject *ob)

   Retorna verdadero si *ob* es de tipo "PyDateTime_DateTimeType" o un
   subtipo de "PyDateTime_DateTimeType". *ob* no debe ser "NULL". Esta
   función siempre finaliza con éxito.

int PyDateTime_CheckExact(PyObject *ob)

   Retorna verdadero si *ob* es de tipo "PyDateTime_DateTimeType".
   *ob* no debe ser "NULL". Esta función siempre finaliza con éxito.

int PyTime_Check(PyObject *ob)

   Retorna verdadero si *ob* es de tipo "PyDateTime_TimeType" o un
   subtipo de "PyDateTime_TimeType". *ob* no debe ser "NULL". Esta
   función siempre finaliza con éxito.

int PyTime_CheckExact(PyObject *ob)

   Retorna verdadero si *ob* es de tipo "PyDateTime_TimeType". *ob* no
   debe ser "NULL". Esta función siempre finaliza con éxito.

int PyDelta_Check(PyObject *ob)

   Retorna verdadero si *ob* es de tipo "PyDateTime_DeltaType" o un
   subtipo de "PyDateTime_DeltaType". *ob* no debe ser "NULL". Esta
   función siempre finaliza con éxito.

int PyDelta_CheckExact(PyObject *ob)

   Retorna verdadero si *ob* es de tipo "PyDateTime_DeltaType". *ob*
   no debe ser "NULL". Esta función siempre finaliza con éxito.

int PyTZInfo_Check(PyObject *ob)

   Retorna verdadero si *ob* es de tipo "PyDateTime_TZInfoType" o un
   subtipo de "PyDateTime_TZInfoType".  *ob* no debe ser "NULL". Esta
   función siempre finaliza con éxito.

int PyTZInfo_CheckExact(PyObject *ob)

   Retorna verdadero si *ob* es de tipo "PyDateTime_TZInfoType". *ob*
   no debe ser "NULL". Esta función siempre finaliza con éxito.

Macros para crear objetos:

PyObject *PyDate_FromDate(int year, int month, int day)
    *Return value: New reference.*

   Retorna un objeto "datetime.date" con el año, mes y día
   especificados.

PyObject *PyDateTime_FromDateAndTime(int year, int month, int day, int hour, int minute, int second, int usecond)
    *Return value: New reference.*

   Retorna un objeto "datetime.datetime" con el año, mes, día, hora,
   minuto, segundo y micro segundo especificados.

PyObject *PyDateTime_FromDateAndTimeAndFold(int year, int month, int day, int hour, int minute, int second, int usecond, int fold)
    *Return value: New reference.*

   Retorna un objeto "datetime.datetime" con el año, mes, día, hora,
   minuto, segundo, micro segundo y doblez especificados.

   Added in version 3.6.

PyObject *PyTime_FromTime(int hour, int minute, int second, int usecond)
    *Return value: New reference.*

   Retorna un objeto "datetime.time" con la hora, minuto, segundo y
   micro segundo especificados.

PyObject *PyTime_FromTimeAndFold(int hour, int minute, int second, int usecond, int fold)
    *Return value: New reference.*

   Retorna un objeto "datetime.time" con la hora, minuto, segundo,
   micro segundo y doblez especificados.

   Added in version 3.6.

PyObject *PyDelta_FromDSU(int days, int seconds, int useconds)
    *Return value: New reference.*

   Retorna un objeto "datetime.timedelta" que representa el número
   dado de días, segundos y micro segundos. La normalización se
   realiza de modo que el número resultante de micro segundos y
   segundos se encuentre en los rangos documentados para los objetos
   "datetime.timedelta".

PyObject *PyTimeZone_FromOffset(PyObject *offset)
    *Return value: New reference.*

   Retorna un objeto "datetime.timezone" con un desplazamiento fijo
   sin nombre representado por el argumento *offset*.

   Added in version 3.7.

PyObject *PyTimeZone_FromOffsetAndName(PyObject *offset, PyObject *name)
    *Return value: New reference.*

   Retorna un objeto "datetime.timezone" con un desplazamiento fijo
   representado por el argumento *offset* y con tzname *name*.

   Added in version 3.7.

Macros para extraer campos de objetos de fecha. El argumento debe ser
una instancia de "PyDateTime_Date", incluidas las subclases (como
"PyDateTime_DateTime"). El argumento no debe ser "NULL", y el tipo no
se comprueba.

int PyDateTime_GET_YEAR(PyDateTime_Date *o)

   Regrese el año, como un int positivo.

int PyDateTime_GET_MONTH(PyDateTime_Date *o)

   Regresa el mes, como int del 1 al 12.

int PyDateTime_GET_DAY(PyDateTime_Date *o)

   Retorna el día, como int del 1 al 31.

Macros para extraer campos de objetos de fecha y hora. El argumento
debe ser una instancia de "PyDateTime_DateTime", incluidas las
subclases. El argumento no debe ser "NULL" y el tipo no es comprobado:

int PyDateTime_DATE_GET_HOUR(PyDateTime_DateTime *o)

   Retorna la hora, como un int de 0 hasta 23.

int PyDateTime_DATE_GET_MINUTE(PyDateTime_DateTime *o)

   Retorna el minuto, como un int de 0 hasta 59.

int PyDateTime_DATE_GET_SECOND(PyDateTime_DateTime *o)

   Retorna el segundo, como un int de 0 hasta 59.

int PyDateTime_DATE_GET_MICROSECOND(PyDateTime_DateTime *o)

   Retorna el micro segundo, como un int de 0 hasta 999999.

int PyDateTime_DATE_GET_FOLD(PyDateTime_DateTime *o)

   Retorna el *fold*, como int de 0 a 1.

   Added in version 3.6.

PyObject *PyDateTime_DATE_GET_TZINFO(PyDateTime_DateTime *o)

   Retorna el tzinfo (que puede ser "None").

   Added in version 3.10.

Macros para extraer campos de objetos de tiempo. El argumento debe ser
una instancia de "PyDateTime_Time", incluidas las subclases. El
argumento no debe ser "NULL" y el tipo no es comprobado:

int PyDateTime_TIME_GET_HOUR(PyDateTime_Time *o)

   Retorna la hora, como un int de 0 hasta 23.

int PyDateTime_TIME_GET_MINUTE(PyDateTime_Time *o)

   Retorna el minuto, como un int de 0 hasta 59.

int PyDateTime_TIME_GET_SECOND(PyDateTime_Time *o)

   Retorna el segundo, como un int de 0 hasta 59.

int PyDateTime_TIME_GET_MICROSECOND(PyDateTime_Time *o)

   Retorna el micro segundo, como un int de 0 hasta 999999.

int PyDateTime_TIME_GET_FOLD(PyDateTime_Time *o)

   Retorna el *fold*, como int de 0 a 1.

   Added in version 3.6.

PyObject *PyDateTime_TIME_GET_TZINFO(PyDateTime_Time *o)

   Retorna el tzinfo (que puede ser "None").

   Added in version 3.10.

Macros para extraer campos de objetos delta de tiempo. El argumento
debe ser una instancia de "PyDateTime_Delta", incluidas las subclases.
El argumento no debe ser "NULL" y el tipo no es comprobado:

int PyDateTime_DELTA_GET_DAYS(PyDateTime_Delta *o)

   Retorna el número de días, como un int desde -999999999 a
   999999999.

   Added in version 3.3.

int PyDateTime_DELTA_GET_SECONDS(PyDateTime_Delta *o)

   Retorna el número de segundos, como un int de 0 a 86399.

   Added in version 3.3.

int PyDateTime_DELTA_GET_MICROSECONDS(PyDateTime_Delta *o)

   Retorna el número de micro segundos, como un int de 0 a 999999.

   Added in version 3.3.

Macros para la conveniencia de módulos que implementan la API DB:

PyObject *PyDateTime_FromTimestamp(PyObject *args)
    *Return value: New reference.*

   Crea y retorna un nuevo objeto "datetime.datetime" dado una tupla
   de argumentos adecuada para pasar a
   "datetime.datetime.fromtimestamp()".

PyObject *PyDate_FromTimestamp(PyObject *args)
    *Return value: New reference.*

   Crea y retorna un nuevo objeto "datetime.date" dado una tupla de
   argumentos adecuada para pasar a "datetime.date.fromtimestamp()".

# Internal data

The following symbols are exposed by the C API but should be
considered internal-only.

PyDateTime_CAPSULE_NAME

   Name of the datetime capsule to pass to "PyCapsule_Import()".

   Internal usage only. Use "PyDateTime_IMPORT" instead.
