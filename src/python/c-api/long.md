---
title: Objetos enteros
source_url: https://docs.python.org/es/3
source_path: c-api/long.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 440
---

# Objetos enteros

Todos los enteros se implementan como objetos enteros "largos"
(*long*) de tamaño arbitrario.

En caso de error, la mayoría de las API "PyLong_As*" retornan "(tipo
de retorno) -1" que no se puede distinguir de un número. Use
"PyErr_Occurred()" para desambiguar.

type PyLongObject
    * Part of the Limited API (as an opaque struct).*

   Este subtipo de "PyObject" representa un objeto entero de Python.

PyTypeObject PyLong_Type
    * Part of the Stable ABI.*

   Esta instancia de "PyTypeObject" representa el tipo entero de
   Python. Este es el mismo objeto que "int" en la capa de Python.

int PyLong_Check(PyObject *p)

   Retorna verdadero si su argumento es un "PyLongObject" o un subtipo
   de "PyLongObject". Esta función siempre finaliza con éxito.

int PyLong_CheckExact(PyObject *p)

   Retorna verdadero si su argumento es un "PyLongObject", pero no un
   subtipo de "PyLongObject". Esta función siempre finaliza con éxito.

PyObject *PyLong_FromLong(long v)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna un objeto "PyLongObject" nuevo desde *v*, o "NULL" en caso
   de error.

   **Detalles de implementación de CPython:** CPython keeps an array
   of integer objects for all integers between "-5" and "256".  When
   you create an int in that range you actually just get back a
   reference to the existing object.

PyObject *PyLong_FromUnsignedLong(unsigned long v)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna un objeto "PyLongObject" nuevo desde un C unsigned long, o
   "NULL" en caso de error.

PyObject *PyLong_FromSsize_t(Py_ssize_t v)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna un objeto "PyLongObject" nuevo desde un C "Py_ssize_t", o
   "NULL" en caso de error.

PyObject *PyLong_FromSize_t(size_t v)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna un objeto "PyLongObject" nuevo desde un C "size_t", o
   "NULL" en caso de error.

PyObject *PyLong_FromLongLong(long long v)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna un objeto "PyLongObject" nuevo desde un C long long, o
   "NULL" en caso de error.

PyObject *PyLong_FromUnsignedLongLong(unsigned long long v)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna un objeto "PyLongObject" nuevo desde un C unsigned long
   long, o "NULL" en caso de error.

PyObject *PyLong_FromInt32(int32_t value)
PyObject *PyLong_FromInt64(int64_t value)
    * Part of the Stable ABI since version 3.14.*

   Return a new "PyLongObject" object from a signed C int32_t or
   int64_t, or "NULL" with an exception set on failure.

   Added in version 3.14.

PyObject *PyLong_FromUInt32(uint32_t value)
PyObject *PyLong_FromUInt64(uint64_t value)
    * Part of the Stable ABI since version 3.14.*

   Return a new "PyLongObject" object from an unsigned C uint32_t or
   uint64_t, or "NULL" with an exception set on failure.

   Added in version 3.14.

PyObject *PyLong_FromDouble(double v)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna un nuevo objeto "PyLongObject" de la parte entera de *v*, o
   "NULL" en caso de error.

PyObject *PyLong_FromString(const char *str, char **pend, int base)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna un nuevo "PyLongObject" basado en el valor de cadena de
   caracteres en *str*, que se interpreta de acuerdo con la raíz en
   *base*, o "NULL" en caso de error. Si *pend* no es "NULL", **pend*
   apuntará al final de *str* en caso de éxito o al primer carácter
   que no se pudo procesar en caso de error. Si *base* es "0", *str*
   se interpreta utilizando la definición Literales enteros; en este
   caso, los ceros a la izquierda en un número decimal distinto de
   cero lanzan un "ValueError". Si *base* no es "0", debe estar entre
   "2" y "36", inclusive. Se ignoran los espacios iniciales y finales
   y los guiones bajos individuales después de un especificador base y
   entre dígitos. Si no hay dígitos o *str* no termina en NULL después
   de los dígitos y los espacios finales, se lanzará "ValueError".

   Ver también:

     "PyLong_AsNativeBytes()" and "PyLong_FromNativeBytes()" functions
     can be used to convert a "PyLongObject" to/from an array of bytes
     in base "256".

PyObject *PyLong_FromUnicodeObject(PyObject *u, int base)
    *Return value: New reference.*

   Convierte una secuencia de dígitos Unicode en la cadena de
   caracteres *u* en un valor entero de Python.

   Added in version 3.3.

PyObject *PyLong_FromVoidPtr(void *p)
    *Return value: New reference.** Part of the Stable ABI.*

   Crea un entero de Python desde el puntero *p*. El valor del puntero
   se puede recuperar del valor resultante usando
   "PyLong_AsVoidPtr()".

PyObject *PyLong_FromNativeBytes(const void *buffer, size_t n_bytes, int flags)
    * Part of the Stable ABI since version 3.14.*

   Crea un entero de Python desde el valor contenido en los primeros
   *n_bytes* de *buffer*, interpretado como un número con signo del
   complemento a dos.

   *flags* son los mismos que para "PyLong_AsNativeBytes()". Al pasar
   "-1" seleccionará el endian nativo con el que CPython fue compilado
   y asumirá que el bit más significativo es un bit de signo. Al pasar
   "Py_ASNATIVEBYTES_UNSIGNED_BUFFER" producirá el mismo resultado que
   llamar a "PyLong_FromUnsignedNativeBytes()". Otros indicadores se
   ignoran.

   Added in version 3.13.

PyObject *PyLong_FromUnsignedNativeBytes(const void *buffer, size_t n_bytes, int flags)
    * Part of the Stable ABI since version 3.14.*

   Crea un entero de Python desde el valor contenido en los primeros
   *n_bytes* de *buffer*, interpretado como un número sin signo.

   *flags* son los mismos que para "PyLong_AsNativeBytes()". Al pasar
   "-1" seleccionará el endian nativo con el que CPython fue compilado
   y asumirá que el bit más significativo no es un bit con signo. Los
   indicadores que no sean endian se ignoran.

   Added in version 3.13.

PyLong_FromPid(pid)

   Macro for creating a Python integer from a process identifier.

   This can be defined as an alias to "PyLong_FromLong()" or
   "PyLong_FromLongLong()", depending on the size of the system's PID
   type.

   Added in version 3.2.

long PyLong_AsLong(PyObject *obj)
    * Part of the Stable ABI.*

   Retorna una representación C long de *obj*. Si *obj* no es una
   instancia de "PyLongObject", primero llama a su método
   "__index__()" (si está presente) para convertirlo en un
   "PyLongObject".

   Lanza "OverflowError" si el valor de *obj* está fuera de rango para
   un long.

   Retorna "-1" en caso de error. Use "PyErr_Occurred()" para
   desambiguar.

   Distinto en la versión 3.8: Use "__index__()" si está disponible.

   Distinto en la versión 3.10: Esta función no usará más "__int__()".

   long PyLong_AS_LONG(PyObject *obj)

      Exactly equivalent to the preferred "PyLong_AsLong". In
      particular, it can fail with "OverflowError" or another
      exception.

      Soft deprecated since version 3.14.

int PyLong_AsInt(PyObject *obj)
    * Part of the Stable ABI since version 3.13.*

   Similar a "PyLong_AsLong()", pero almacena el resultado en un C int
   en lugar de un C long.

   Added in version 3.13.

long PyLong_AsLongAndOverflow(PyObject *obj, int *overflow)
    * Part of the Stable ABI.*

   Retorna una representación C long de *obj*. Si *obj* no es una
   instancia de "PyLongObject", primero llama a su método
   "__index__()" (si está presente) para convertirlo en un
   "PyLongObject".

   Si el valor de *obj* es mayor que "LONG_MAX" o menor que
   "LONG_MIN", establece **overflow* en "1" o "-1", respectivamente, y
   retorna "-1"; de lo contrario, establece **overflow* en "0". Si se
   produce alguna otra excepción, configura **overflow* en "0" y
   retorna "-1" como de costumbre.

   Retorna "-1" en caso de error. Use "PyErr_Occurred()" para
   desambiguar.

   Distinto en la versión 3.8: Use "__index__()" si está disponible.

   Distinto en la versión 3.10: Esta función no usará más "__int__()".

long long PyLong_AsLongLong(PyObject *obj)
    * Part of the Stable ABI.*

   Retorna una representación C long long de *obj*. Si *obj* no es una
   instancia de "PyLongObject", primero llame a su método
   "__index__()" (si está presente) para convertirlo en un
   "PyLongObject".

   Lanza "OverflowError" si el valor de *obj* está fuera de rango para
   un long long.

   Retorna "-1" en caso de error. Use "PyErr_Occurred()" para
   desambiguar.

   Distinto en la versión 3.8: Use "__index__()" si está disponible.

   Distinto en la versión 3.10: Esta función no usará más "__int__()".

long long PyLong_AsLongLongAndOverflow(PyObject *obj, int *overflow)
    * Part of the Stable ABI.*

   Retorna una representación C long long de *obj*. Si *obj* no es una
   instancia de "PyLongObject", primero llame a su método
   "__index__()" (si está presente) para convertirlo en un
   "PyLongObject".

   Si el valor de *obj* es mayor que "LLONG_MAX" o menor que
   "LLONG_MIN", establece **overflow* en "1" o "-1", respectivamente,
   y retorna "-1"; de lo contrario, establece **overflow* en "0". Si
   se produce alguna otra excepción, configura **overflow* en "0" y
   retorna "-1" como de costumbre.

   Retorna "-1" en caso de error. Use "PyErr_Occurred()" para
   desambiguar.

   Added in version 3.2.

   Distinto en la versión 3.8: Use "__index__()" si está disponible.

   Distinto en la versión 3.10: Esta función no usará más "__int__()".

Py_ssize_t PyLong_AsSsize_t(PyObject *pylong)
    * Part of the Stable ABI.*

   Retorna una representación de C "Py_ssize_t" de *pylong*. *pylong*
   debe ser una instancia de "PyLongObject".

   Lanza "OverflowError" si el valor de *pylong* está fuera de rango
   para un "Py_ssize_t".

   Retorna "-1" en caso de error. Use "PyErr_Occurred()" para
   desambiguar.

unsigned long PyLong_AsUnsignedLong(PyObject *pylong)
    * Part of the Stable ABI.*

   Retorna una representación de C unsigned long de *pylong*. *pylong*
   debe ser una instancia de "PyLongObject".

   Lanza "OverflowError" si el valor de *pylong* está fuera de rango
   para un unsigned long.

   Retorna "(unsigned long)-1" en caso de error. Use
   "PyErr_Occurred()" para desambiguar.

size_t PyLong_AsSize_t(PyObject *pylong)
    * Part of the Stable ABI.*

   Retorna una representación de C "size_t" de *pylong*. *pylong* debe
   ser una instancia de "PyLongObject".

   Lanza "OverflowError" si el valor de *pylong* está fuera de rango
   para un "size_t".

   Retorna "(size_t) -1" en caso de error. Use "PyErr_Occurred()" para
   desambiguar.

unsigned long long PyLong_AsUnsignedLongLong(PyObject *pylong)
    * Part of the Stable ABI.*

   Retorna una representación de C unsigned long long de *pylong*.
   *pylong* debe ser una instancia de "PyLongObject".

   Lanza "OverflowError" si el valor de *pylong* está fuera de rango
   para un unsigned long long.

   Retorna "(unsigned long long) -1" en caso de error. Use
   "PyErr_Occurred()" para desambiguar.

   Distinto en la versión 3.1: Ahora un *pylong* negativo lanza un
   "OverflowError", no "TypeError".

unsigned long PyLong_AsUnsignedLongMask(PyObject *obj)
    * Part of the Stable ABI.*

   Retorna una representación C unsigned long de *obj*. Si *obj* no es
   una instancia de "PyLongObject", primero llame a su método
   "__index__()" (si está presente) para convertirlo en un
   "PyLongObject".

   Si el valor de *obj* está fuera del rango para unsigned long,
   retorna la reducción de ese valor módulo "ULONG_MAX + 1".

   Retorna "(unsigned long)-1" en caso de error. Use
   "PyErr_Occurred()" para desambiguar.

   Distinto en la versión 3.8: Use "__index__()" si está disponible.

   Distinto en la versión 3.10: Esta función no usará más "__int__()".

unsigned long long PyLong_AsUnsignedLongLongMask(PyObject *obj)
    * Part of the Stable ABI.*

   Retorna una representación C unsigned long long de *obj*. Si *obj*
   no es una instancia de "PyLongObject", primero llame a su método
   "__index__()" (si está presente) para convertirlo en un
   "PyLongObject".

   Si el valor de *obj* está fuera del rango para unsigned long long,
   retorna la reducción de ese valor módulo "ULLONG_MAX + 1".

   Retorna "(unsigned long long) -1" por error. Use "PyErr_Occurred()"
   para desambiguar.

   Distinto en la versión 3.8: Use "__index__()" si está disponible.

   Distinto en la versión 3.10: Esta función no usará más "__int__()".

int PyLong_AsInt32(PyObject *obj, int32_t *value)
int PyLong_AsInt64(PyObject *obj, int64_t *value)
    * Part of the Stable ABI since version 3.14.*

   Set **value* to a signed C int32_t or int64_t representation of
   *obj*.

   If *obj* is not an instance of "PyLongObject", first call its
   "__index__()" method (if present) to convert it to a
   "PyLongObject".

   If the *obj* value is out of range, raise an "OverflowError".

   Set **value* and return "0" on success. Set an exception and return
   "-1" on error.

   *value* must not be "NULL".

   Added in version 3.14.

int PyLong_AsUInt32(PyObject *obj, uint32_t *value)
int PyLong_AsUInt64(PyObject *obj, uint64_t *value)
    * Part of the Stable ABI since version 3.14.*

   Set **value* to an unsigned C uint32_t or uint64_t representation
   of *obj*.

   If *obj* is not an instance of "PyLongObject", first call its
   "__index__()" method (if present) to convert it to a
   "PyLongObject".

   * If *obj* is negative, raise a "ValueError".

   * If the *obj* value is out of range, raise an "OverflowError".

   Set **value* and return "0" on success. Set an exception and return
   "-1" on error.

   *value* must not be "NULL".

   Added in version 3.14.

double PyLong_AsDouble(PyObject *pylong)
    * Part of the Stable ABI.*

   Retorna una representación de C double de *pylong*. *pylong* debe
   ser una instancia de "PyLongObject".

   Lanza "OverflowError" si el valor de *pylong* está fuera de rango
   para un double.

   Retorna "-1.0" en caso de error. Use "PyErr_Occurred()" para
   desambiguar.

void *PyLong_AsVoidPtr(PyObject *pylong)
    * Part of the Stable ABI.*

   Convierte un entero Python *pylong* en un puntero C void. Si
   *pylong* no se puede convertir, se lanzará un "OverflowError". Esto
   solo se garantiza para producir un puntero utilizable void para
   valores creados con "PyLong_FromVoidPtr()".

   Retorna "NULL" en caso de error. Use "PyErr_Occurred()" para
   desambiguar.

Py_ssize_t PyLong_AsNativeBytes(PyObject *pylong, void *buffer, Py_ssize_t n_bytes, int flags)
    * Part of the Stable ABI since version 3.14.*

   Copia el valor entero de Python *pylong* a un *buffer* nativo de
   tamaño *n_bytes*. Los *flags* pueden establecerse en "-1" para un
   comportamiento similar a una conversión de C, o en los valores
   documentados a continuación para controlar el comportamiento.

   Retorna "-1" con una excepción lanzada en caso de error. Esto puede
   ocurrir si *pylong* no se puede interpretar como un entero, o si
   *pylong* era negativo y se configuró el indicador
   "Py_ASNATIVEBYTES_REJECT_NEGATIVE".

   Otherwise, returns the number of bytes required to store the value.
   If this is equal to or less than *n_bytes*, the entire value was
   copied. All *n_bytes* of the buffer are written: remaining bytes
   filled by copies of the sign bit.

   If the returned value is greater than *n_bytes*, the value was
   truncated: as many of the lowest bits of the value as could fit are
   written, and the higher bits are ignored. This matches the typical
   behavior of a C-style downcast.

   Nota:

     El desbordamiento no se considera un error. Si el valor que se
     retorna es mayor que *n_bytes*, se descartan los bits más
     significativos.

   "0" nunca será retornado.

   Los valores siempre se copian como complemento a dos.

   Ejemplo de uso:

      int32_t value;
      Py_ssize_t bytes = PyLong_AsNativeBytes(pylong, &value, sizeof(value), -1);
      if (bytes < 0) {
          // Error. Se estableció una excepción de Python con el motivo.
          return NULL;
      }
      else if (bytes <= (Py_ssize_t)sizeof(value)) {
          // ¡Éxito!
      }
      else {
          // Se produjo un desbordamiento, pero 'value' contiene
          // los bits más bajos truncados de pylong.
      }

   Al pasar cero a *n_bytes* retornará el tamaño de un búfer lo
   suficientemente grande como para contener el valor. Este tamaño
   puede ser mayor de lo técnicamente necesario, pero no excesivamente
   grande. Si *n_bytes=0*, *buffer* puede ser "NULL".

   Nota:

     Al pasar *n_bytes=0* a esta función no es una forma precisa de
     determinar la longitud en bits del valor.

   Para obtener el valor completo de Python de un tamaño desconocido,
   la función se puede llamar dos veces: primero para determinar el
   tamaño del búfer y luego para llenarlo:

      // Pide cuánto espacio necesitamos.
      Py_ssize_t expected = PyLong_AsNativeBytes(pylong, NULL, 0, -1);
      if (expected < 0) {
          // Error. Se estableció una excepción de Python con el motivo.
          return NULL;
      }
      assert(expected != 0);  // Imposible según la definición de la API.
      uint8_t *bignum = malloc(expected);
      if (!bignum) {
          PyErr_SetString(PyExc_MemoryError, "bignum malloc failed.");
          return NULL;
      }
      // Obtiene el valor completo de forma segura.
      Py_ssize_t bytes = PyLong_AsNativeBytes(pylong, bignum, expected, -1);
      if (bytes < 0) {  // Se configuró una excepción.
          free(bignum);
          return NULL;
      }
      else if (bytes > expected) {  // Esto no debería ser posible.
          PyErr_SetString(PyExc_RuntimeError,
              "Unexpected bignum truncation after a size check.");
          free(bignum);
          return NULL;
      }
      // El éxito esperado dada la comprobación previa.
      // ... use bignum ...
      free(bignum);

   *flags* is either "-1" ("Py_ASNATIVEBYTES_DEFAULTS") to select
   defaults that behave most like a C cast, or a combination of the
   other flags in the table below. Note that "-1" cannot be combined
   with other flags.

   Actualmente, "-1" corresponde a "Py_ASNATIVEBYTES_NATIVE_ENDIAN |
   Py_ASNATIVEBYTES_UNSIGNED_BUFFER".

   +-----------------------------------------------+--------+
   | Indicador                                     | Valor  |
   |===============================================|========|
   | Py_ASNATIVEBYTES_DEFAULTS  * Part of the      | "-1"   |
   | Stable ABI since version 3.14.*               |        |
   +-----------------------------------------------+--------+
   | Py_ASNATIVEBYTES_BIG_ENDIAN  * Part of the    | "0"    |
   | Stable ABI since version 3.14.*               |        |
   +-----------------------------------------------+--------+
   | Py_ASNATIVEBYTES_LITTLE_ENDIAN  * Part of the | "1"    |
   | Stable ABI since version 3.14.*               |        |
   +-----------------------------------------------+--------+
   | Py_ASNATIVEBYTES_NATIVE_ENDIAN  * Part of the | "3"    |
   | Stable ABI since version 3.14.*               |        |
   +-----------------------------------------------+--------+
   | Py_ASNATIVEBYTES_UNSIGNED_BUFFER  * Part of   | "4"    |
   | the Stable ABI since version 3.14.*           |        |
   +-----------------------------------------------+--------+
   | Py_ASNATIVEBYTES_REJECT_NEGATIVE  * Part of   | "8"    |
   | the Stable ABI since version 3.14.*           |        |
   +-----------------------------------------------+--------+
   | Py_ASNATIVEBYTES_ALLOW_INDEX  * Part of the   | "16"   |
   | Stable ABI since version 3.14.*               |        |
   +-----------------------------------------------+--------+

   Especificar "Py_ASNATIVEBYTES_NATIVE_ENDIAN" redefinirá cualquier
   otro indicador endian. Pasar "2" está reservado.

   Por defecto, se solicitará búfer suficiente para incluir un bit de
   signo. Por ejemplo, al convertir 128 con *n_bytes=1*, la función
   retornará 2 (o más) para almacenar un bit de signo cero.

   Si se especifica "Py_ASNATIVEBYTES_UNSIGNED_BUFFER", se omitirá el
   bit de signo cero en los cálculos de tamaño. Esto permite, por
   ejemplo, que quepa 128 en un búfer de un solo byte. Si el búfer de
   destino se trata posteriormente como con signo, un valor de entrada
   positivo puede volverse negativo. Tenga en cuenta que este
   indicador no afecta el manejo de valores negativos: para ellos,
   siempre se solicita espacio para un bit de signo.

   Especificar "Py_ASNATIVEBYTES_REJECT_NEGATIVE", se establece una
   excepción si *pylong* es negativo. Sin este indicador, se copiarán
   los valores negativos siempre que haya suficiente espacio para al
   menos un bit de signo, independientemente de si se especificó
   "Py_ASNATIVEBYTES_UNSIGNED_BUFFER".

   Si se especifica "Py_ASNATIVEBYTES_ALLOW_INDEX" y se pasa un valor
   distinto de un entero, se llamará primero a su método
   "__index__()". Esto puede resultar la ejecución de código Python y
   la ejecución de otros subprocesos, lo que podría causar cambios en
   otros objetos o valores en uso. Cuando *flags* es "-1", esta opción
   no se establece y los valores distintos de un entero lanzarán
   "TypeError".

   Nota:

     Con los *flags* predeterminados ("-1" o *UNSIGNED_BUFFER* sin
     *REJECT_NEGATIVE*), varios enteros de Python pueden asignarse a
     un único valor sin desbordamiento. Por ejemplo, tanto "255" como
     "-1" se ajustan a un búfer de un solo byte y configuran todos sus
     bits. Esto coincide con el comportamiento típico de conversión de
     C.

   Added in version 3.13.

PyLong_AsPid(pid)

   Macro for converting a Python integer into a process identifier.

   This can be defined as an alias to "PyLong_AsLong()",
   "PyLong_FromLongLong()", or "PyLong_AsInt()", depending on the size
   of the system's PID type.

   Added in version 3.2.

int PyLong_GetSign(PyObject *obj, int *sign)

   Get the sign of the integer object *obj*.

   On success, set **sign* to the integer sign  (0, -1 or +1 for zero,
   negative or positive integer, respectively) and return 0.

   On failure, return -1 with an exception set.  This function always
   succeeds if *obj* is a "PyLongObject" or its subtype.

   Added in version 3.14.

int PyLong_IsPositive(PyObject *obj)

   Check if the integer object *obj* is positive ("obj > 0").

   If *obj* is an instance of "PyLongObject" or its subtype, return
   "1" when it's positive and "0" otherwise.  Else set an exception
   and return "-1".

   Added in version 3.14.

int PyLong_IsNegative(PyObject *obj)

   Check if the integer object *obj* is negative ("obj < 0").

   If *obj* is an instance of "PyLongObject" or its subtype, return
   "1" when it's negative and "0" otherwise.  Else set an exception
   and return "-1".

   Added in version 3.14.

int PyLong_IsZero(PyObject *obj)

   Check if the integer object *obj* is zero.

   If *obj* is an instance of "PyLongObject" or its subtype, return
   "1" when it's zero and "0" otherwise.  Else set an exception and
   return "-1".

   Added in version 3.14.

PyObject *PyLong_GetInfo(void)
    * Part of the Stable ABI.*

   En caso de éxito, retorna una *named tuple* de solo lectura, que
   contiene información sobre la representación interna de enteros en
   Python. Consulte "sys.int_info" para obtener una descripción de
   cada campo.

   En caso de error, retorna "NULL" con una excepción configurada.

   Added in version 3.1.

int PyUnstable_Long_IsCompact(const PyLongObject *op)

   *This is Unstable API. It may change without warning in minor
   releases.*

   Retorna 1 si *op* es compacto, 0 en caso contrario.

   Esta función permite que el código de rendimiento crítico
   implemente una “ruta rápida” para enteros pequeños. Para valores
   compactos, utilice "PyUnstable_Long_CompactValue()"; para otros,
   utilice una función "PyLong_As*" o "PyLong_AsNativeBytes()".

   Se espera que la aceleración sea insignificante para la mayoría de
   los usuarios.

   Exactamente qué valores se consideran compactos es un detalle de
   implementación y está sujeto a cambios.

   Added in version 3.12.

Py_ssize_t PyUnstable_Long_CompactValue(const PyLongObject *op)

   *This is Unstable API. It may change without warning in minor
   releases.*

   Si *op* es compacto, se determina por
   "PyUnstable_Long_IsCompact()", retorna su valor.

   De lo contrario, el valor que retorna está indefinido.

   Added in version 3.12.

## Export API

Added in version 3.14.

struct PyLongLayout

   Layout of an array of "digits" ("limbs" in the GMP terminology),
   used to represent absolute value for arbitrary precision integers.

   Use "PyLong_GetNativeLayout()" to get the native layout of Python
   "int" objects, used internally for integers with "big enough"
   absolute value.

   See also "sys.int_info" which exposes similar information in
   Python.

   uint8_t bits_per_digit

      Bits per digit. For example, a 15 bit digit means that bits 0-14
      contain meaningful information.

   uint8_t digit_size

      Digit size in bytes. For example, a 15 bit digit will require at
      least 2 bytes.

   int8_t digits_order

      Digits order:

      * "1" for most significant digit first

      * "-1" for least significant digit first

   int8_t digit_endianness

      Digit endianness:

      * "1" for most significant byte first (big endian)

      * "-1" for least significant byte first (little endian)

const PyLongLayout *PyLong_GetNativeLayout(void)

   Get the native layout of Python "int" objects.

   See the "PyLongLayout" structure.

   The function must not be called before Python initialization nor
   after Python finalization. The returned layout is valid until
   Python is finalized. The layout is the same for all Python sub-
   interpreters in a process, and so it can be cached.

struct PyLongExport

   Export of a Python "int" object.

   There are two cases:

   * If "digits" is "NULL", only use the "value" member.

   * If "digits" is not "NULL", use "negative", "ndigits" and "digits"
     members.

   int64_t value

      The native integer value of the exported "int" object. Only
      valid if "digits" is "NULL".

   uint8_t negative

      "1" if the number is negative, "0" otherwise. Only valid if
      "digits" is not "NULL".

   Py_ssize_t ndigits

      Number of digits in "digits" array. Only valid if "digits" is
      not "NULL".

   const void *digits

      Read-only array of unsigned digits. Can be "NULL".

int PyLong_Export(PyObject *obj, PyLongExport *export_long)

   Export a Python "int" object.

   *export_long* must point to a "PyLongExport" structure allocated by
   the caller. It must not be "NULL".

   On success, fill in **export_long* and return "0". On error, set an
   exception and return "-1".

   "PyLong_FreeExport()" must be called when the export is no longer
   needed.

      **Detalles de implementación de CPython:** This function always
      succeeds if *obj* is a Python "int" object or a subclass.

void PyLong_FreeExport(PyLongExport *export_long)

   Release the export *export_long* created by "PyLong_Export()".

   **Detalles de implementación de CPython:** Calling
   "PyLong_FreeExport()" is optional if *export_long->digits* is
   "NULL".

## PyLongWriter API

The "PyLongWriter" API can be used to import an integer.

Added in version 3.14.

struct PyLongWriter

   A Python "int" writer instance.

   The instance must be destroyed by "PyLongWriter_Finish()" or
   "PyLongWriter_Discard()".

PyLongWriter *PyLongWriter_Create(int negative, Py_ssize_t ndigits, void **digits)

   Create a "PyLongWriter".

   On success, allocate **digits* and return a writer. On error, set
   an exception and return "NULL".

   *negative* is "1" if the number is negative, or "0" otherwise.

   *ndigits* is the number of digits in the *digits* array. It must be
   greater than 0.

   *digits* must not be NULL.

   After a successful call to this function, the caller should fill in
   the array of digits *digits* and then call "PyLongWriter_Finish()"
   to get a Python "int". The layout of *digits* is described by
   "PyLong_GetNativeLayout()".

   Digits must be in the range ["0"; "(1 << bits_per_digit) - 1"]
   (where the "bits_per_digit" is the number of bits per digit). Any
   unused most significant digits must be set to "0".

   Alternately, call "PyLongWriter_Discard()" to destroy the writer
   instance without creating an "int" object.

PyObject *PyLongWriter_Finish(PyLongWriter *writer)
    *Return value: New reference.*

   Finish a "PyLongWriter" created by "PyLongWriter_Create()".

   On success, return a Python "int" object. On error, set an
   exception and return "NULL".

   The function takes care of normalizing the digits and converts the
   object to a compact integer if needed.

   The writer instance and the *digits* array are invalid after the
   call.

void PyLongWriter_Discard(PyLongWriter *writer)

   Discard a "PyLongWriter" created by "PyLongWriter_Create()".

   If *writer* is "NULL", no operation is performed.

   The writer instance and the *digits* array are invalid after the
   call.

## Deprecated API

These macros are *soft deprecated*. They describe parameters of the
internal representation of "PyLongObject" instances.

Use "PyLong_GetNativeLayout()" instead, along with "PyLong_Export()"
to read integer data or "PyLongWriter" to write it. These currently
use the same layout, but are designed to continue working correctly
even if CPython's internal integer representation changes.

PyLong_SHIFT

   This is equivalent to "bits_per_digit" in the output of
   "PyLong_GetNativeLayout()".

PyLong_BASE

   This is currently equivalent to 1 << PyLong_SHIFT.

PyLong_MASK

   This is currently equivalent to (1 << PyLong_SHIFT) - 1
