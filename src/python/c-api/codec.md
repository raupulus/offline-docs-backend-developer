---
title: Registro de códec y funciones de soporte
source_url: https://docs.python.org/es/3
source_path: c-api/codec.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 150
---

# Registro de códec y funciones de soporte

int PyCodec_Register(PyObject *search_function)
    * Part of the Stable ABI.*

   Registra una nueva función de búsqueda de códec.

   As a side effect, this tries to load the "encodings" package, if
   not yet done, to make sure that it is always first in the list of
   search functions.

int PyCodec_Unregister(PyObject *search_function)
    * Part of the Stable ABI since version 3.10.*

   Anula el registro de una función de búsqueda de códecs y borra el
   caché del registro. Si la función de búsqueda no está registrada,
   no hace nada. Retorna 0 en caso de éxito. Lanza una excepción y
   devuelva -1 en caso de error.

   Added in version 3.10.

int PyCodec_KnownEncoding(const char *encoding)
    * Part of the Stable ABI.*

   Retorna "1" o "0" dependiendo de si hay un códec registrado para el
   *encoding* dado. Esta función siempre finaliza con éxito.

PyObject *PyCodec_Encode(PyObject *object, const char *encoding, const char *errors)
    *Return value: New reference.** Part of the Stable ABI.*

   API de codificación genérica basada en códec.

   *object* se pasa a través de la función de codificador encontrada
   por el *encoding* dado usando el método de manejo de errores
   definido por *errors*. *errors* pueden ser "NULL" para usar el
   método predeterminado definido para el códec. Lanza un
   "LookupError" si no se puede encontrar el codificador.

PyObject *PyCodec_Decode(PyObject *object, const char *encoding, const char *errors)
    *Return value: New reference.** Part of the Stable ABI.*

   API de decodificación basada en códec genérico.

   *object* is passed through the decoder function found for the given
   *encoding* using the error handling method defined by *errors*.
   *errors* may be "NULL" to use the default method defined for the
   codec.  Raises a "LookupError" if no decoder can be found.

## API de búsqueda de códec

En las siguientes funciones, la cadena de caracteres *encoding* se
busca convertida a todos los caracteres en minúscula, lo que hace que
las codificaciones se busquen a través de este mecanismo sin
distinción entre mayúsculas y minúsculas. Si no se encuentra ningún
códec, se establece un "KeyError" y se retorna "NULL".

PyObject *PyCodec_Encoder(const char *encoding)
    *Return value: New reference.** Part of the Stable ABI.*

   Obtiene una función de codificador para el *encoding* dado.

PyObject *PyCodec_Decoder(const char *encoding)
    *Return value: New reference.** Part of the Stable ABI.*

   Obtiene una función de decodificador para el *encoding* dado.

PyObject *PyCodec_IncrementalEncoder(const char *encoding, const char *errors)
    *Return value: New reference.** Part of the Stable ABI.*

   Obtiene un objeto "IncrementalEncoder" para el *encoding* dada.

PyObject *PyCodec_IncrementalDecoder(const char *encoding, const char *errors)
    *Return value: New reference.** Part of the Stable ABI.*

   Obtiene un objeto "IncrementalDecoder" para el *encoding* dado.

PyObject *PyCodec_StreamReader(const char *encoding, PyObject *stream, const char *errors)
    *Return value: New reference.** Part of the Stable ABI.*

   Obtiene una función de fábrica "StreamReader" para el *encoding*
   dado.

PyObject *PyCodec_StreamWriter(const char *encoding, PyObject *stream, const char *errors)
    *Return value: New reference.** Part of the Stable ABI.*

   Obtiene una función de fábrica "StreamWriter" por el *encoding*
   dado.

## API de registro para controladores de errores de codificación Unicode

int PyCodec_RegisterError(const char *name, PyObject *error)
    * Part of the Stable ABI.*

   Registra la función de devolución de llamada de manejo de errores
   *error* bajo el nombre *name* dado. Esta función de devolución de
   llamada será llamada por un códec cuando encuentre caracteres no
   codificables / bytes no codificables y *name* se especifica como
   parámetro de error en la llamada a la función de codificación /
   decodificación.

   La devolución de llamada obtiene un único argumento, una instancia
   de "UnicodeEncodeError", "UnicodeDecodeError" o
   "UnicodeTranslateError" que contiene información sobre la secuencia
   problemática de caracteres o bytes y su desplazamiento en la cadena
   original (consulte Objetos unicode de excepción para funciones para
   extraer esta información). La devolución de llamada debe lanzar la
   excepción dada o retornar una tupla de dos elementos que contiene
   el reemplazo de la secuencia problemática, y un número entero que
   proporciona el desplazamiento en la cadena original en la que se
   debe reanudar la codificación / decodificación.

   Retorna "0" en caso de éxito, "-1" en caso de error.

PyObject *PyCodec_LookupError(const char *name)
    *Return value: New reference.** Part of the Stable ABI.*

   Busca la función de devolución de llamada de manejo de errores
   registrada con *name*. Como caso especial se puede pasar "NULL", en
   cuyo caso se retornará la devolución de llamada de manejo de
   errores para "estricto".

PyObject *PyCodec_StrictErrors(PyObject *exc)
    *Return value: Always NULL.** Part of the Stable ABI.*

   Lanza *exc* como una excepción.

PyObject *PyCodec_IgnoreErrors(PyObject *exc)
    *Return value: New reference.** Part of the Stable ABI.*

   Ignora el error Unicode, omitiendo la entrada defectuosa.

PyObject *PyCodec_ReplaceErrors(PyObject *exc)
    *Return value: New reference.** Part of the Stable ABI.*

   Reemplaza el error de codificación Unicode con "?" o "U+FFFD".

PyObject *PyCodec_XMLCharRefReplaceErrors(PyObject *exc)
    *Return value: New reference.** Part of the Stable ABI.*

   Reemplaza el error de codificación Unicode con referencias de
   caracteres XML.

PyObject *PyCodec_BackslashReplaceErrors(PyObject *exc)
    *Return value: New reference.** Part of the Stable ABI.*

   Reemplaza el error de codificación Unicode con escapes de barra
   invertida ("\x", "\u" y "\U").

PyObject *PyCodec_NameReplaceErrors(PyObject *exc)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.7.*

   Reemplaza el error de codificación Unicode con escapes "\N{...}".

   Added in version 3.5.

## Codec utility variables

const char *Py_hexdigits

   A string constant containing the lowercase hexadecimal digits:
   ""0123456789abcdef"".

   Added in version 3.3.
