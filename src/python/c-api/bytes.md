---
title: Objetos bytes
source_url: https://docs.python.org/es/3
source_path: c-api/bytes.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 100
---

# Objetos bytes

Estas funciones lanzan "TypeError" cuando se espera un parámetro de
bytes y se llama con un parámetro que no es bytes.

type PyBytesObject

   Este subtipo de "PyObject" representa un objeto bytes de Python.

PyTypeObject PyBytes_Type
    * Part of the Stable ABI.*

   Esta instancia de "PyTypeObject" representa el tipo bytes de
   Python; es el mismo objeto que "bytes" en la capa de Python.

int PyBytes_Check(PyObject *o)

   Retorna verdadero si el objeto *o* es un objeto bytes o una
   instancia de un subtipo del tipo bytes. Esta función siempre
   finaliza con éxito.

int PyBytes_CheckExact(PyObject *o)

   Retorna verdadero si el objeto *o* es un objeto bytes, pero no una
   instancia de un subtipo del tipo bytes. Esta función siempre
   finaliza con éxito.

PyObject *PyBytes_FromString(const char *v)
    *Return value: New reference.** Part of the Stable ABI.** Thread
   safety: Atomic.*

   Retorna un nuevo objeto bytes con una copia de la cadena de
   caracteres *v* como valor en caso de éxito y "NULL" en caso de
   error. El parámetro *v* no debe ser "NULL"; no se comprobará.

PyObject *PyBytes_FromStringAndSize(const char *v, Py_ssize_t len)
    *Return value: New reference.** Part of the Stable ABI.** Thread
   safety: Atomic.*

   Retorna un nuevo objeto bytes con una copia de la cadena de
   caracteres *v* como valor y longitud *len* en caso de éxito y
   "NULL" en caso de error. Si *v* es "NULL", el contenido del objeto
   bytes no se inicializa.

PyObject *PyBytes_FromFormat(const char *format, ...)
    *Return value: New reference.** Part of the Stable ABI.** Thread
   safety: Atomic.*

   Toma una cadena de caracteres *format* del estilo C "printf()" y un
   número variable de argumentos, calcula el tamaño del objeto bytes
   Python resultante y retorna un objeto bytes con los valores
   formateados. Los argumentos variables deben ser tipos C y deben
   corresponder exactamente a los caracteres de formato en la cadena
   de caracteres *format*. Se permiten los siguientes caracteres de
   formato:

   +---------------------+-----------------+----------------------------------+
   | Caracteres de       | Tipo            | Comentario                       |
   | formato             |                 |                                  |
   |=====================|=================|==================================|
   | "%%"                | *n/a*           | El carácter literal %.           |
   +---------------------+-----------------+----------------------------------+
   | "%c"                | int             | Un solo byte, representado como  |
   |                     |                 | un C int.                        |
   +---------------------+-----------------+----------------------------------+
   | "%d"                | int             | Equivalente a "printf("%d")".    |
   |                     |                 | [1]                              |
   +---------------------+-----------------+----------------------------------+
   | "%u"                | unsigned int    | Equivalente a "printf("%u")".    |
   |                     |                 | [1]                              |
   +---------------------+-----------------+----------------------------------+
   | "%ld"               | long            | Equivalente a "printf("%ld")".   |
   |                     |                 | [1]                              |
   +---------------------+-----------------+----------------------------------+
   | "%lu"               | unsigned long   | Equivalente a "printf("%lu")".   |
   |                     |                 | [1]                              |
   +---------------------+-----------------+----------------------------------+
   | "%zd"               | "Py_ssize_t"    | Equivalente a "printf("%zd")".   |
   |                     |                 | [1]                              |
   +---------------------+-----------------+----------------------------------+
   | "%zu"               | size_t          | Equivalente a "printf("%zu")".   |
   |                     |                 | [1]                              |
   +---------------------+-----------------+----------------------------------+
   | "%i"                | int             | Equivalente a "printf("%i")".    |
   |                     |                 | [1]                              |
   +---------------------+-----------------+----------------------------------+
   | "%x"                | int             | Equivalente a "printf("%x")".    |
   |                     |                 | [1]                              |
   +---------------------+-----------------+----------------------------------+
   | "%s"                | const char*     | Un arreglo de caracteres C       |
   |                     |                 | terminados en nulo.              |
   +---------------------+-----------------+----------------------------------+
   | "%p"                | const void*     | La representación hexadecimal de |
   |                     |                 | un puntero en C. Principalmente  |
   |                     |                 | equivalente a "printf("%p")"     |
   |                     |                 | excepto que se garantiza que     |
   |                     |                 | comience con el literal "0x",    |
   |                     |                 | independientemente de lo que     |
   |                     |                 | produzca el "printf" de la       |
   |                     |                 | plataforma.                      |
   +---------------------+-----------------+----------------------------------+

   Un carácter de formato no reconocido hace que todo el resto de la
   cadena de caracteres de formato se copie como está en el objeto de
   resultado y se descartan los argumentos adicionales.

   [1] Para especificadores de enteros *(d, u, ld, lu, zd, zu, i, x)*:
       el indicador de conversión 0 tiene efecto incluso cuando se
       proporciona una precisión.

PyObject *PyBytes_FromFormatV(const char *format, va_list vargs)
    *Return value: New reference.** Part of the Stable ABI.** Thread
   safety: Atomic.*

   Idéntica a "PyBytes_FromFormat()" excepto que toma exactamente dos
   argumentos.

PyObject *PyBytes_FromObject(PyObject *o)
    *Return value: New reference.** Part of the Stable ABI.** Thread
   safety: Safe for concurrent use on the same object.*

   Retorna la representación en bytes del objeto *o* que implementa el
   protocolo de búfer.

   Nota:

     If the object implements the buffer protocol, then the buffer
     must not be mutated while the bytes object is being created.

Py_ssize_t PyBytes_Size(PyObject *o)
    * Part of the Stable ABI.** Thread safety: Atomic.*

   Retorna la longitud de los bytes en el objeto bytes *o*.

Py_ssize_t PyBytes_GET_SIZE(PyObject *o)
    * Thread safety: Atomic.*

   Forma macro de "PyBytes_Size()" pero sin verificación de errores.

char *PyBytes_AsString(PyObject *o)
    * Part of the Stable ABI.** Thread safety: Safe to call from
   multiple threads with external synchronization only.*

   Retorna un puntero al contenido de *o*. El puntero se refiere al
   búfer interno de *o*, que consiste en "len(o) + 1" bytes. El último
   byte en el búfer siempre es nulo, independientemente de si hay
   otros bytes nulos. Los datos no deben modificarse de ninguna
   manera, a menos que el objeto se haya creado usando
   "PyBytes_FromStringAndSize(NULL, size)". No debe ser desasignado.
   Si *o* no es un objeto de bytes en absoluto, "PyBytes_AsString()"
   retorna "NULL" y lanza un "TypeError".

char *PyBytes_AS_STRING(PyObject *string)
    * Thread safety: Safe to call from multiple threads with external
   synchronization only.*

   Forma macro de "PyBytes_AsString()" pero sin verificación de
   errores.

int PyBytes_AsStringAndSize(PyObject *obj, char **buffer, Py_ssize_t *length)
    * Part of the Stable ABI.** Thread safety: Safe to call from
   multiple threads with external synchronization only.*

   Retorna los contenidos terminados en nulo del objeto *obj* a través
   de las variables de salida *buffer* y *length*. Retorna "0" en caso
   de éxito.

   Si *length* es "NULL", el objeto bytes no puede contener bytes
   nulos incrustados; en caso contrario, la función retorna "-1" y se
   lanza un "ValueError".

   El búfer se refiere a un búfer interno de *obj*, que incluye un
   byte nulo adicional al final (no está considerado en *length*). Los
   datos no deben modificarse de ninguna manera, a menos que el objeto
   se haya creado usando "PyBytes_FromStringAndSize(NULL, size)". No
   debe ser desasignado. Si *obj* no es un objeto bytes en absoluto,
   "PyBytes_AsStringAndSize()" retorna "-1" y lanza "TypeError".

   Distinto en la versión 3.5: Anteriormente, "TypeError" se lanzaba
   cuando se encontraban bytes nulos incrustados en el objeto bytes.

void PyBytes_Concat(PyObject **bytes, PyObject *newpart)
    * Part of the Stable ABI.** Thread safety: Safe for concurrent use
   on the same object.*

   Create a new bytes object in **bytes* containing the contents of
   *newpart* appended to *bytes*; the caller will own the new
   reference. The reference to the old value of *bytes* will be
   "*stolen*". If the new object cannot be created, the old reference
   to *bytes* will still be "stolen", the value of **bytes* will be
   set to "NULL", and the appropriate exception will be set.

   Nota:

     If *newpart* implements the buffer protocol, then the buffer must
     not be mutated while the new bytes object is being created.

void PyBytes_ConcatAndDel(PyObject **bytes, PyObject *newpart)
    * Part of the Stable ABI.** Thread safety: Safe for concurrent use
   on the same object.*

   Crea un nuevo objeto de bytes en **bytes* que contenga el contenido
   de *newpart* agregado a *bytes*. Esta versión libera la *strong
   reference* a *newpart* (es decir, disminuye su recuento de
   referencias).

   Nota:

     If *newpart* implements the buffer protocol, then the buffer must
     not be mutated while the new bytes object is being created.

PyObject *PyBytes_Join(PyObject *sep, PyObject *iterable)
    * Thread safety: Safe for concurrent use on the same object.*

   Similar to "sep.join(iterable)" in Python.

   *sep* must be Python "bytes" object. (Note that "PyUnicode_Join()"
   accepts "NULL" separator and treats it as a space, whereas
   "PyBytes_Join()" doesn't accept "NULL" separator.)

   *iterable* must be an iterable object yielding objects that
   implement the buffer protocol.

   On success, return a new "bytes" object. On error, set an exception
   and return "NULL".

   Added in version 3.14.

   Nota:

     If *iterable* objects implement the buffer protocol, then the
     buffers must not be mutated while the new bytes object is being
     created.

int _PyBytes_Resize(PyObject **bytes, Py_ssize_t newsize)
    * Thread safety: Safe to call without external synchronization on
   distinct objects.*

   Redimensiona un objeto bytes. *newsize* será la nueva longitud del
   objeto bytes. Se puede considerar como crear un nuevo objeto bytes
   y destruir el anterior, solo que de forma más eficiente. Pasa la
   dirección de un objeto bytes existente como lvalue (se puede
   escribir en él) y el nuevo tamaño deseado. En caso de éxito,
   **bytes* contiene el objeto bytes redimensionado y se retorna "0";
   la dirección en **bytes* puede diferir de su valor de entrada. Si
   la reasignación falla, el objeto bytes original en **bytes* se
   desasigna, **bytes* se establece en "NULL", se establece
   "MemoryError" y se retorna "-1".

PyObject *PyBytes_Repr(PyObject *bytes, int smartquotes)
    * Part of the Stable ABI.** Thread safety: Atomic.*

   Get the string representation of *bytes*. This function is
   currently used to implement "bytes.__repr__()" in Python.

   This function does not do type checking; it is undefined behavior
   to pass *bytes* as a non-bytes object or "NULL".

   If *smartquotes* is true, the representation will use a double-
   quoted string instead of single-quoted string when single-quotes
   are present in *bytes*. For example, the byte string "'Python'"
   would be represented as "b"'Python'"" when *smartquotes* is true,
   or "b'\'Python\''" when it is false.

   On success, this function returns a *strong reference* to a "str"
   object containing the representation. On failure, this returns
   "NULL" with an exception set.

PyObject *PyBytes_DecodeEscape(const char *s, Py_ssize_t len, const char *errors, Py_ssize_t unicode, const char *recode_encoding)
    * Part of the Stable ABI.** Thread safety: Atomic.*

   Unescape a backslash-escaped string *s*. *s* must not be "NULL".
   *len* must be the size of *s*.

   *errors* must be one of ""strict"", ""replace"", or ""ignore"". If
   *errors* is "NULL", then ""strict"" is used by default.

   On success, this function returns a *strong reference* to a Python
   "bytes" object containing the unescaped string. On failure, this
   function returns "NULL" with an exception set.

   Distinto en la versión 3.9: *unicode* and *recode_encoding* are now
   unused.
