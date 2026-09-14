---
title: Analizando argumentos y construyendo valores
source_url: https://docs.python.org/es/3
source_path: c-api/arg.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 60
---

# Analizando argumentos y construyendo valores

These functions are useful when creating your own extension functions
and methods.  Additional information and examples are available in
Ampliación e incrustación del intérprete de Python.

Las tres primeras de estas funciones descritas, "PyArg_ParseTuple()",
"PyArg_ParseTupleAndKeywords()", y "PyArg_Parse()", todas usan
*cadenas de caracteres de formato* que se utilizan para contarle a la
función sobre los argumentos esperados. Las cadenas de caracteres de
formato utilizan la misma sintaxis para cada una de estas funciones.

## Analizando argumentos

Una cadena de formato consta de cero o más "unidades de formato." Una
unidad de formato describe un objeto Python; por lo general es un solo
carácter o una secuencia de unidades formato entre paréntesis. Con
unas pocas excepciones, una unidad de formato que no es una secuencia
entre paréntesis normalmente corresponde a un único argumento de
dirección de estas funciones. En la siguiente descripción, la forma
citada es la unidad de formato; la entrada en paréntesis (redondos) es
el tipo de objeto Python que coincida con la unidad de formato; y la
entrada entre corchetes [cuadrados] es el tipo de la variable(s) C
cuya dirección debe ser pasada.

### Cadena de caracteres y búferes

Nota:

  En Python 3.12 y versiones anteriores, la macro "PY_SSIZE_T_CLEAN"
  debe estar definida antes de incluir "Python.h" para usar todas las
  variantes "#" de formatos ("s#", "y#", etc.) explicadas a
  continuación. Esto no es necesario en Python 3.13 y versiones
  posteriores.

Estos formatos permiten acceder a un objeto como un bloque contiguo de
memoria. Usted no tiene que proporcionar almacenamiento en bruto para
el Unicode o área de bytes retornada.

A menos que se indique lo contrario, los búferes no son terminados en
NULL (*NUL-terminated*).

Hay tres formas en que las cadenas de caracteres y los búferes pueden
convertirse a C:

* Formats such as "y*" and "s*" fill a "Py_buffer" structure. This
  locks the underlying buffer so that the caller can subsequently use
  the buffer even inside a "Py_BEGIN_ALLOW_THREADS" block without the
  risk of mutable data being resized or destroyed. As a result, **you
  have to call** "PyBuffer_Release()" after you have finished
  processing the data (or in any early abort case).

* Los formatos "es", "es#", "et" y "et#" asignan el búfer de
  resultado. **Debe llamar** "PyMem_Free()" después de haber terminado
  de procesar los datos (o en cualquier caso de aborto temprano).

* Otros formatos toman un "str" o un *objeto de tipo bytes* de solo
  lectura, como "bytes", y proporcionan un puntero "const char *" a su
  búfer. En este caso el búfer es "prestado" (*borrowed*): es
  gestionado por el objeto Python correspondiente y comparte el tiempo
  de vida de este objeto. No tendrá que liberar ninguna memoria usted
  mismo.

  Para asegurar que el búfer subyacente pueda ser prestado de forma
  segura, el campo "PyBufferProcs.bf_releasebuffer" del objeto debe
  ser "NULL". Esto desautoriza objetos mutables comunes como
  "bytearray", pero también algunos objetos de solo lectura como
  "memoryview" de "bytes".

  Además de este requisito de "bf_releasebuffer", no hay verificación
  para comprobar si el objeto de entrada es inmutable (por ejemplo, si
  respetaría una solicitud de un búfer escribible, o si otro hilo
  puede mutar los datos).

"s" ("str") [const char *]
   Convierte un objeto Unicode a un puntero C a una cadena de
   caracteres. Un puntero a una cadena de caracteres existente se
   almacena en la variable puntero del carácter cuya dirección se
   pasa. La cadena de caracteres en C es terminada en NULL. La cadena
   de caracteres de Python no debe contener puntos de código
   incrustado nulos; si lo hace, se lanza una excepción "ValueError".
   Los objetos Unicode se convierten en cadenas de caracteres de C
   utilizando codificación "'utf-8'". Si esta conversión fallase lanza
   un "UnicodeError".

   Nota:

     Este formato no acepta *objetos de tipo bytes*. Si desea aceptar
     los caminos del sistema de archivos y convertirlos en cadenas de
     caracteres C, es preferible utilizar el formato "O&" con
     "PyUnicode_FSConverter()" como convertidor.

   Distinto en la versión 3.5: Anteriormente, "TypeError" se lanzó
   cuando se encontraron puntos de código nulos incrustados en la
   cadena de caracteres de Python.

"s*" ("str" o *bytes-like object*) [Py_buffer]
   Este formato acepta objetos Unicode, así como objetos de tipo
   bytes. Llena una estructura  "Py_buffer" proporcionada por la
   persona que llama. En este caso la cadena de caracteres de C
   resultante puede contener bytes NUL embebidos. Los objetos Unicode
   se convierten en cadenas de caracteres C utilizando codificación
   "'utf-8'".

"s#" ("str", *bytes-like object* de sólo lectura) [const char *,
"Py_ssize_t"]
   Like "s*", except that it provides a borrowed buffer. The result is
   stored into two C variables, the first one a pointer to a C string,
   the second one its length. The string may contain embedded null
   bytes. Unicode objects are converted to C strings using "'utf-8'"
   encoding.

"z" ("str" o "None") [const char *]
   Como "s", pero el objeto Python también puede ser "None", en cuyo
   caso el puntero C se establece en "NULL".

"z*" ("str", *bytes-like object* o "None") [Py_buffer]
   Como "s*", pero el objeto Python también puede ser "None", en cuyo
   caso el miembro de "buf" de la estructura "Py_buffer" se establece
   en "NULL".

"z#" ("str", *bytes-like object* de sólo lectura o "None") [const char
*, "Py_ssize_t"]
   Como "s#", pero el objeto Python también puede ser "None", en cuyo
   caso el puntero C se establece en "NULL".

"y" (*bytes-like object* de sólo lectura) [const char *]
   This format converts a bytes-like object to a C pointer to a
   borrowed character string; it does not accept Unicode objects.  The
   bytes buffer must not contain embedded null bytes; if it does, a
   "ValueError" exception is raised.

   Distinto en la versión 3.5: Anteriormente, "TypeError" se lanzó
   cuando bytes nulos incrustados se encontraron en el buffer de
   bytes.

"y*" (*bytes-like object*) [Py_buffer]
   Esta variante de "s*" no acepta objetos Unicode, solamente los
   objetos de tipo bytes. **Esta es la forma recomendada para aceptar
   datos binarios.**

"y#" (*bytes-like object* de sólo lectura) [const char *,
"Py_ssize_t"]
   Esta variante en "s#" no acepta objetos Unicode, solo objetos
   similares a bytes.

"S" ("bytes") [PyBytesObject *]
   Requires that the Python object is a "bytes" object, without
   attempting any conversion.  Raises "TypeError" if the object is not
   a bytes object.  The C variable may also be declared as PyObject*.

"Y" ("bytearray") [PyByteArrayObject *]
   Requires that the Python object is a "bytearray" object, without
   attempting any conversion.  Raises "TypeError" if the object is not
   a "bytearray" object. The C variable may also be declared as
   PyObject*.

"U" ("str") [PyObject *]
   Requires that the Python object is a Unicode object, without
   attempting any conversion.  Raises "TypeError" if the object is not
   a Unicode object.  The C variable may also be declared as
   PyObject*.

"w*" (*bytes-like object* de lectura y escritura) [Py_buffer]
   This format accepts any object which implements the read-write
   buffer interface. It fills a "Py_buffer" structure provided by the
   caller. The buffer may contain embedded null bytes. The caller has
   to call "PyBuffer_Release()" when it is done with the buffer.

"es" ("str") [const char *encoding, char **buffer]
   Esta variante en "s" se usa para codificar Unicode en un búfer de
   caracteres. Solo funciona para datos codificados sin bytes NUL
   integrados.

   This format requires two arguments.  The first is only used as
   input, and must be a const char* which points to the name of an
   encoding as a NUL-terminated string, or "NULL", in which case
   "'utf-8'" encoding is used. An exception is raised if the named
   encoding is not known to Python.  The second argument must be a
   char**; the value of the pointer it references will be set to a
   buffer with the contents of the argument text. The text will be
   encoded in the encoding specified by the first argument.

   "PyArg_ParseTuple()" asignará un búfer del tamaño necesitado,
   copiará los datos codificados en este búfer y ajustará **buffer*
   para referenciar el nuevo almacenamiento asignado. Quien llama es
   responsable para llamar "PyMem_Free()" para liberar el búfer
   asignado después de su uso.

"et" ("str", "bytes" o "bytearray") [const char *encoding, char
**buffer]
   Igual que "es", excepto que los objetos de cadena de caracteres de
   bytes se pasan sin recodificarlos. En cambio, la implementación
   supone que el objeto de cadena de caracteres de bytes utiliza la
   codificación que se pasa como parámetro.

"es#" ("str") [const char *encoding, char **buffer, "Py_ssize_t"
*buffer_length]
   Esta variante en "s#" se usa para codificar Unicode en un búfer de
   caracteres. A diferencia del formato "es", esta variante permite
   datos de entrada que contienen caracteres NUL.

   It requires three arguments.  The first is only used as input, and
   must be a const char* which points to the name of an encoding as a
   NUL-terminated string, or "NULL", in which case "'utf-8'" encoding
   is used. An exception is raised if the named encoding is not known
   to Python.  The second argument must be a char**; the value of the
   pointer it references will be set to a buffer with the contents of
   the argument text. The text will be encoded in the encoding
   specified by the first argument. The third argument must be a
   pointer to an integer; the referenced integer will be set to the
   number of bytes in the output buffer.

   Hay dos modos de operación:

   Si **buffer* señala un puntero "NULL", la función asignará un búfer
   del tamaño necesario, copiará los datos codificados en este búfer y
   configurará **buffer* para hacer referencia al almacenamiento
   recién asignado. Quien llama es responsable de llamar a
   "PyMem_Free()" para liberar el búfer asignado después del uso.

   Si **buffer* apunta a un puntero no "NULL" (un búfer ya asignado),
   "PyArg_ParseTuple()" usará esta ubicación como el búfer e
   interpretará el valor inicial de **buffer_length* como el tamaño
   del búfer. Luego copiará los datos codificados en el búfer y los
   terminará en NUL. Si el búfer no es lo suficientemente grande, se
   establecerá a "ValueError".

   En ambos casos, **buffer_length* se establece a la longitud de los
   datos codificados sin el byte NUL final.

"et#" ("str", "bytes" o "bytearray") [const char *encoding, char
**buffer, "Py_ssize_t" *buffer_length]
   Igual que "es#", excepto que los objetos de cadena de caracteres de
   bytes se pasan sin recodificarlos. En cambio, la implementación
   supone que el objeto de cadena de caracteres de bytes utiliza la
   codificación que se pasa como parámetro.

Distinto en la versión 3.12: "u", "u#", "Z" y "Z#" fueron eliminados
porque usaban una representación heredada "Py_UNICODE*".

### Números

These formats allow representing Python numbers or single characters
as C numbers. Formats that require "int", "float" or "complex" can
also use the corresponding special methods "__index__()",
"__float__()" or "__complex__()" to convert the Python object to the
required type.

For signed integer formats, "OverflowError" is raised if the value is
out of range for the C type. For unsigned integer formats, no range
checking is done --- the most significant bits are silently truncated
when the receiving field is too small to receive the value.

"b" ("int") [unsigned char]
   Convert a nonnegative Python integer to an unsigned tiny integer,
   stored in a C unsigned char.

"B" ("int") [unsigned char]
   Convert a Python integer to a tiny integer without overflow
   checking, stored in a C unsigned char.

"h" ("int") [short int]
   Convert a Python integer to a C short int.

"H" ("int") [unsigned short int]
   Convert a Python integer to a C unsigned short int, without
   overflow checking.

"i" ("int") [int]
   Convert a Python integer to a plain C int.

"I" ("int") [unsigned int]
   Convert a Python integer to a C unsigned int, without overflow
   checking.

"l" ("int") [long int]
   Convert a Python integer to a C long int.

"k" ("int") [unsigned long]
   Convert a Python integer to a C unsigned long without overflow
   checking.

   Distinto en la versión 3.14: Use "__index__()" if available.

"L" ("int") [long long]
   Convert a Python integer to a C long long.

"K" ("int") [unsigned long long]
   Convert a Python integer to a C unsigned long long without overflow
   checking.

   Distinto en la versión 3.14: Use "__index__()" if available.

"n" ("int") ["Py_ssize_t"]
   Convierte un entero de Python a un "Py_ssize_t" de C.

"c" ("bytes" o "bytearray" de largo 1) [char]
   Convert a Python byte, represented as a "bytes" or "bytearray"
   object of length 1, to a C char.

   Distinto en la versión 3.3: Permite objetos "bytearray".

"C" ("str" de largo 1) [int]
   Convert a Python character, represented as a "str" object of length
   1, to a C int.

"f" ("float") [float]
   Convert a Python floating-point number to a C float.

"d" ("float") [double]
   Convert a Python floating-point number to a C double.

"D" ("complex") [Py_complex]
   Convierte un número complejo de Python en una estructura
   "Py_complex" de C.

### Otros objetos

"O" (object) [PyObject *]
   Store a Python object (without any conversion) in a C object
   pointer.  The C program thus receives the actual object that was
   passed.  A new *strong reference* to the object is not created
   (i.e. its reference count is not increased). The pointer stored is
   not "NULL".

"O!" (object) [*typeobject*, PyObject *]
   Store a Python object in a C object pointer.  This is similar to
   "O", but takes two C arguments: the first is the address of a
   Python type object, the second is the address of the C variable (of
   type PyObject*) into which the object pointer is stored.  If the
   Python object does not have the required type, "TypeError" is
   raised.

"O&" (object) [*converter*, *address*]
   Convert a Python object to a C variable through a *converter*
   function.  This takes two arguments: the first is a function, the
   second is the address of a C variable (of arbitrary type),
   converted to void*.  The *converter* function in turn is called as
   follows:

      status = converter(object, address);

   where *object* is the Python object to be converted and *address*
   is the void* argument that was passed to the "PyArg_Parse*"
   function. The returned *status* should be "1" for a successful
   conversion and "0" if the conversion has failed.  When the
   conversion fails, the *converter* function should raise an
   exception and leave the content of *address* unmodified.

   If the *converter* returns "Py_CLEANUP_SUPPORTED", it may get
   called a second time if the argument parsing eventually fails,
   giving the converter a chance to release any memory that it had
   already allocated. In this second call, the *object* parameter will
   be "NULL"; *address* will have the same value as in the original
   call.

   Examples of converters: "PyUnicode_FSConverter()" and
   "PyUnicode_FSDecoder()".

   Distinto en la versión 3.1: "Py_CLEANUP_SUPPORTED" was added.

"p" ("bool") [int]
   Prueba el valor pasado por verdad (un booleano predicado **p**) y
   convierte el resultado a su valor entero C verdadero/falso entero
   equivalente. Establece int en "1" si la expresión era verdadera y
   "0" si era falsa. Esto acepta cualquier valor válido de Python.
   Consulte Evaluar como valor verdadero/falso para obtener más
   información sobre cómo Python prueba los valores por verdad.

   Added in version 3.3.

"(items)" (sequence) [*matching-items*]
   The object must be a Python sequence (except "str", "bytes" or
   "bytearray") whose length is the number of format units in *items*.
   The C arguments must correspond to the individual format units in
   *items*.  Format units for sequences may be nested.

   If *items* contains format units which store a borrowed buffer
   ("s", "s#", "z", "z#", "y", or "y#") or a *borrowed reference*
   ("S", "Y", "U", "O", or "O!"), the object must be a Python tuple.
   The *converter* for the "O&" format unit in *items* must not store
   a borrowed buffer or a borrowed reference.

   Distinto en la versión 3.14: "str" and "bytearray" objects no
   longer accepted as a sequence.

   Obsoleto desde la versión 3.14: Non-tuple sequences are deprecated
   if *items* contains format units which store a borrowed buffer or a
   borrowed reference.

Algunos otros caracteres tienen un significado en una cadena de
formato. Esto puede no ocurrir dentro de paréntesis anidados. Son:

"|"
   Indica que los argumentos restantes en la lista de argumentos de
   Python son opcionales. Las variables C correspondientes a
   argumentos opcionales deben inicializarse a su valor predeterminado
   --- cuando no se especifica un argumento opcional,
   "PyArg_ParseTuple()" no toca el contenido de las variables C
   correspondientes.

"$"
   "PyArg_ParseTupleAndKeywords()" solamente: indica que los
   argumentos restantes en la lista de argumentos de Python son solo
   palabras clave. Actualmente, todos los argumentos de solo palabras
   clave también deben ser argumentos opcionales, por lo que "|"
   siempre debe especificarse antes de "$" en la cadena de formato.

   Added in version 3.3.

":"
   La lista de unidades de formato termina aquí; la cadena después de
   los dos puntos se usa como el nombre de la función en los mensajes
   de error (el "valor asociado" de la excepción que
   "PyArg_ParseTuple()" lanza).

";"
   La lista de unidades de formato termina aquí; la cadena después del
   punto y coma se usa como mensaje de error *en lugar de* del mensaje
   de error predeterminado. ":" y ";" se excluyen mutuamente.

Note that any Python object references which are provided to the
caller are *borrowed* references; do not release them (i.e. do not
decrement their reference count)!

Los argumentos adicionales pasados a estas funciones deben ser
direcciones de variables cuyo tipo está determinado por la cadena de
formato; Estos se utilizan para almacenar valores de la tupla de
entrada. Hay algunos casos, como se describe en la lista de unidades
de formato anterior, donde estos parámetros se utilizan como valores
de entrada; deben coincidir con lo especificado para la unidad de
formato correspondiente en ese caso.

For the conversion to succeed, the *arg* object must match the format
and the format must be exhausted.  On success, the "PyArg_Parse*"
functions return true, otherwise they return false and raise an
appropriate exception. When the "PyArg_Parse*" functions fail due to
conversion failure in one of the format units, the variables at the
addresses corresponding to that and the following format units are
left untouched.

### Funciones API

int PyArg_ParseTuple(PyObject *args, const char *format, ...)
    * Part of the Stable ABI.*

   Analiza los parámetros de una función que solo toma parámetros
   posicionales en variables locales. Retorna verdadero en el éxito;
   en caso de fallo, retorna falso y lanza la excepción apropiada.

int PyArg_VaParse(PyObject *args, const char *format, va_list vargs)
    * Part of the Stable ABI.*

   Idéntico a "PyArg_ParseTuple()", excepto que acepta una *va_list*
   en lugar de un número variable de argumentos .

int PyArg_ParseTupleAndKeywords(PyObject *args, PyObject *kw, const char *format, char *const *keywords, ...)
    * Part of the Stable ABI.*

   Parse the parameters of a function that takes both positional and
   keyword parameters into local variables. The *keywords* argument is
   a "NULL"-terminated array of keyword parameter names specified as
   null-terminated ASCII or UTF-8 encoded C strings. Empty names
   denote positional-only parameters. Returns true on success; on
   failure, it returns false and raises the appropriate exception.

   Nota:

     The *keywords* parameter declaration is char *const* in C and
     const char *const* in C++. This can be overridden with the
     "PY_CXX_CONST" macro.

   Distinto en la versión 3.6: Soporte agregado para sólo parámetros
   posicionales.

   Distinto en la versión 3.13: The *keywords* parameter has now type
   char *const* in C and const char *const* in C++, instead of char**.
   Added support for non-ASCII keyword parameter names.

int PyArg_VaParseTupleAndKeywords(PyObject *args, PyObject *kw, const char *format, char *const *keywords, va_list vargs)
    * Part of the Stable ABI.*

   Idéntico a "PyArg_ParseTupleAndKeywords()", excepto que acepta una
   *va_list* en lugar de un número variable de argumentos.

int PyArg_ValidateKeywordArguments(PyObject*)
    * Part of the Stable ABI.*

   Asegúrese de que las claves en el diccionario de argumentos de
   palabras clave son cadenas. Esto solo es necesario si
   "PyArg_ParseTupleAndKeywords()" no se utiliza, ya que este último
   ya hace esta comprobación.

   Added in version 3.2.

int PyArg_Parse(PyObject *args, const char *format, ...)
    * Part of the Stable ABI.*

   Parse the parameter of a function that takes a single positional
   parameter into a local variable.  Returns true on success; on
   failure, it returns false and raises the appropriate exception.

   Example:

      // Function using METH_O calling convention
      static PyObject*
      my_function(PyObject *module, PyObject *arg)
      {
          int value;
          if (!PyArg_Parse(arg, "i:my_function", &value)) {
              return NULL;
          }
          // ... use value ...
      }

int PyArg_UnpackTuple(PyObject *args, const char *name, Py_ssize_t min, Py_ssize_t max, ...)
    * Part of the Stable ABI.*

   A simpler form of parameter retrieval which does not use a format
   string to specify the types of the arguments.  Functions which use
   this method to retrieve their parameters should be declared as
   "METH_VARARGS" in function or method tables.  The tuple containing
   the actual parameters should be passed as *args*; it must actually
   be a tuple.  The length of the tuple must be at least *min* and no
   more than *max*; *min* and *max* may be equal.  Additional
   arguments must be passed to the function, each of which should be a
   pointer to a PyObject* variable; these will be filled in with the
   values from *args*; they will contain *borrowed references*. The
   variables which correspond to optional parameters not given by
   *args* will not be filled in; these should be initialized by the
   caller. This function returns true on success and false if *args*
   is not a tuple or contains the wrong number of elements; an
   exception will be set if there was a failure.

   This is an example of the use of this function, taken from the
   sources for the "_weakref" helper module for weak references:

      static PyObject *
      weakref_ref(PyObject *self, PyObject *args)
      {
          PyObject *object;
          PyObject *callback = NULL;
          PyObject *result = NULL;

          if (PyArg_UnpackTuple(args, "ref", 1, 2, &object, &callback)) {
              result = PyWeakref_NewRef(object, callback);
          }
          return result;
      }

   La llamada a "PyArg_UnpackTuple()" en este ejemplo es completamente
   equivalente a esta llamada a "PyArg_ParseTuple()":

      PyArg_ParseTuple(args, "O|O:ref", &object, &callback)

PY_CXX_CONST

   The value to be inserted, if any, before char *const* in the
   *keywords* parameter declaration of "PyArg_ParseTupleAndKeywords()"
   and "PyArg_VaParseTupleAndKeywords()". Default empty for C and
   "const" for C++ (const char *const*). To override, define it to the
   desired value before including "Python.h".

   Added in version 3.13.

## Construyendo valores

PyObject *Py_BuildValue(const char *format, ...)
    *Return value: New reference.** Part of the Stable ABI.*

   Create a new value based on a format string similar to those
   accepted by the "PyArg_Parse*" family of functions and a sequence
   of values.  Returns the value or "NULL" in the case of an error; an
   exception will be raised if "NULL" is returned.

   "Py_BuildValue()" no siempre genera una tupla. Construye una tupla
   solo si su cadena de formato contiene dos o más unidades de
   formato. Si la cadena de formato está vacía, retorna "None"; si
   contiene exactamente una unidad de formato, retorna el objeto que
   describa esa unidad de formato. Para forzarlo a retornar una tupla
   de tamaño 0 o uno, paréntesis la cadena de formato.

   Cuando los búfer de memoria se pasan como parámetros para
   suministrar datos para construir objetos, como para los formatos
   "s" y "s#", los datos requeridos se copian. Las memorias
   intermedias proporcionadas por quien llama nunca son referenciadas
   por los objetos creados por "Py_BuildValue()". En otras palabras,
   si su código invoca "malloc()" y pasa la memoria asignada a
   "Py_BuildValue()", su código es responsable de llamar a "free()"
   para esa memoria una vez retorna "Py_BuildValue()".

   En la siguiente descripción, la cadena de caracteres entre
   comillas, *así*, es la unidad de formato; la entrada entre
   paréntesis (redondos) es el tipo de objeto Python que retornará la
   unidad de formato; y la entrada entre corchetes [cuadrados] es el
   tipo de los valores C que se pasarán.

   Los caracteres espacio, tabulación, dos puntos y coma se ignoran en
   las cadenas de formato (pero no dentro de las unidades de formato
   como "s#"). Esto se puede usar para hacer que las cadenas de
   formato largo sean un poco más legibles.

   "s" ("str" o "None") [const char *]
      Convierte una cadena de caracteres C terminada en nulo en un
      objeto Python "str" usando la codificación "'utf-8'". Si el
      puntero de la cadena de caracteres C es "NULL", se usa "None".

   "s#" ("str" o "None") [const char *, "Py_ssize_t"]
      Convierte una cadena de caracteres de C y su longitud en un
      objeto Python "str" utilizando la codificación "'utf-8'". Si el
      puntero de la cadena de caracteres de C es "NULL", la longitud
      se ignora y se retorna "None".

   "y" ("bytes") [const char *]
      Esto convierte una cadena de caracteres de C en un objeto Python
      "bytes". Si el puntero de la cadena de caracteres de C es
      "NULL", se retorna "None".

   "y#" ("bytes") [const char *, "Py_ssize_t"]
      Esto convierte una cadena de caracteres de C y sus longitudes en
      un objeto Python. Si el puntero de la cadena de caracteres de C
      es "NULL", se retorna "None".

   "z" ("str" o "None") [const char *]
      Igual que "s".

   "z#" ("str" o "None") [const char *, "Py_ssize_t"]
      Igual que "s#".

   "u" ("str") [const wchar_t *]
      Convert a null-terminated "wchar_t" buffer of Unicode (UTF-16 or
      UCS-4) data to a Python Unicode object.  If the Unicode buffer
      pointer is "NULL", "None" is returned.

   "u#" ("str") [const wchar_t *, "Py_ssize_t"]
      Convierte un búfer de datos Unicode (UTF-16 o UCS-4) y su
      longitud en un objeto Python Unicode. Si el puntero del búfer
      Unicode es "NULL", la longitud se ignora y se retorna "None".

   "U" ("str" o "None") [const char *]
      Igual que "s".

   "z#" ("str" o "None") [const char *, "Py_ssize_t"]
      Igual que "s#".

   "i" ("int") [int]
      Convert a plain C int to a Python integer object.

   "b" ("int") [char]
      Convert a plain C char to a Python integer object.

   "h" ("int") [short int]
      Convert a plain C short int to a Python integer object.

   "l" ("int") [long int]
      Convert a C long int to a Python integer object.

   "B" ("int") [unsigned char]
      Convert a C unsigned char to a Python integer object.

   "H" ("int") [unsigned short int]
      Convert a C unsigned short int to a Python integer object.

   "I" ("int") [unsigned int]
      Convert a C unsigned int to a Python integer object.

   "k" ("int") [unsigned long]
      Convert a C unsigned long to a Python integer object.

   "L" ("int") [long long]
      Convert a C long long to a Python integer object.

   "K" ("int") [unsigned long long]
      Convert a C unsigned long long to a Python integer object.

   "n" ("int") ["Py_ssize_t"]
      Convierte un "Py_ssize_t" de C a un entero de Python.

   "p" ("bool") [int]
      Convert a C int to a Python "bool" object.

      Be aware that this format requires an "int" argument. Unlike
      most other contexts in C, variadic arguments are not coerced to
      a suitable type automatically. You can convert another type (for
      example, a pointer or a float) to a suitable "int" value using
      "(x) ? 1 : 0" or "!!x".

      Added in version 3.14.

   "c" ("bytes" de largo 1) [char]
      Convert a C int representing a byte to a Python "bytes" object
      of length 1.

   "C" ("str" de largo 1) [int]
      Convert a C int representing a character to Python "str" object
      of length 1.

   "d" ("float") [double]
      Convert a C double to a Python floating-point number.

   "f" ("float") [float]
      Convert a C float to a Python floating-point number.

   "D" ("complex") [Py_complex *]
      Convierte una estructura "Py_complex" de C en un número complejo
      de Python.

   "O" (object) [PyObject *]
      Pass a Python object untouched but create a new *strong
      reference* to it (i.e. its reference count is incremented by
      one). If the object passed in is a "NULL" pointer, it is assumed
      that this was caused because the call producing the argument
      found an error and set an exception. Therefore,
      "Py_BuildValue()" will return "NULL" but won't raise an
      exception.  If no exception has been raised yet, "SystemError"
      is set.

   "S" (object) [PyObject *]
      Igual que "O".

   "N" (object) [PyObject *]
      Same as "O", except it doesn't create a new *strong reference*.
      Useful when the object is created by a call to an object
      constructor in the argument list.

   "O&" (object) [*converter*, *anything*]
      Convert *anything* to a Python object through a *converter*
      function.  The function is called with *anything* (which should
      be compatible with void*) as its argument and should return a
      "new" Python object, or "NULL" if an error occurred.

   "(items)" ("tuple") [*matching-items*]
      Convierta una secuencia de valores C en una tupla de Python con
      el mismo número de elementos.

   "[items]" ("list") [*matching-items*]
      Convierte una secuencia de valores C en una lista de Python con
      el mismo número de elementos.

   "{items}" ("dict") [*matching-items*]
      Convierte una secuencia de valores C en un diccionario Python.
      Cada par de valores C consecutivos agrega un elemento al
      diccionario, que sirve como clave y valor, respectivamente.

   Si hay un error en la cadena de formato, se establece la excepción
   "SystemError" y se retorna "NULL".

PyObject *Py_VaBuildValue(const char *format, va_list vargs)
    *Return value: New reference.** Part of the Stable ABI.*

   Idéntico a "Py_BuildValue()", excepto que acepta una *va_list* en
   lugar de un número variable de argumentos.
