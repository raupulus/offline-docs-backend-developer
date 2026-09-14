---
title: Objetos y códecs unicode
source_url: https://docs.python.org/es/3
source_path: c-api/unicode.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 760
---

# Objetos y códecs unicode

## Objetos unicode

Desde la implementación del **PEP 393** en Python 3.3, los objetos
Unicode utilizan internamente una variedad de representaciones, para
permitir el manejo del rango completo de caracteres Unicode mientras
se mantiene la eficiencia de memoria. Hay casos especiales para
cadenas de caracteres donde todos los puntos de código están por
debajo de 128, 256 o 65536; de lo contrario, los puntos de código
deben estar por debajo de 1114112 (que es el rango completo de
Unicode).

La representación UTF-8 se crea bajo demanda y se almacena en caché en
el objeto Unicode.

Nota:

  La representación "Py_UNICODE" ha sido eliminada desde Python 3.12
  con APIs obsoletas. Consulte **PEP 623** para obtener más
  información.

### Tipo unicode

Estos son los tipos básicos de objetos Unicode utilizados para la
implementación de Unicode en Python:

PyTypeObject PyUnicode_Type
    * Part of the Stable ABI.*

   This instance of "PyTypeObject" represents the Python Unicode type.
   It is exposed to Python code as "str".

PyTypeObject PyUnicodeIter_Type
    * Part of the Stable ABI.*

   This instance of "PyTypeObject" represents the Python Unicode
   iterator type. It is used to iterate over Unicode string objects.

type Py_UCS4
type Py_UCS2
type Py_UCS1
    * Part of the Stable ABI.*

   Estos tipos son definiciones de tipo (*typedefs*) para los tipos
   'enteros sin signo' (*unsigned int*) lo suficientemente anchos como
   para contener caracteres de 32 bits, 16 bits y 8 bits,
   respectivamente. Cuando se trate con caracteres Unicode
   individuales, use "Py_UCS4".

   Added in version 3.3.

type PyASCIIObject
type PyCompactUnicodeObject
type PyUnicodeObject

   Estos subtipos de "PyObject" representan un objeto Python Unicode.
   En casi todos los casos, no deben usarse directamente, ya que todas
   las funciones API que se ocupan de objetos Unicode toman y retornan
   punteros "PyObject".

   Added in version 3.3.

   The structure of a particular object can be determined using the
   following macros. The macros cannot fail; their behavior is
   undefined if their argument is not a Python Unicode object.

   PyUnicode_IS_COMPACT(o)

      True if *o* uses the "PyCompactUnicodeObject" structure.

      Added in version 3.3.

   PyUnicode_IS_COMPACT_ASCII(o)

      True if *o* uses the "PyASCIIObject" structure.

      Added in version 3.3.

Las siguientes API son realmente macros de C y se pueden utilizar para
realizar comprobaciones rápidas y acceder a datos internos de solo
lectura de objetos Unicode:

int PyUnicode_Check(PyObject *obj)

   Retorna verdadero si el objeto *obj* es un objeto Unicode o una
   instancia de un subtipo Unicode. Esta función siempre tiene éxito.

int PyUnicode_CheckExact(PyObject *obj)

   Retorna verdadero si el objeto *obj* es un objeto Unicode, pero no
   una instancia de un subtipo. Esta función siempre tiene éxito.

Py_ssize_t PyUnicode_GET_LENGTH(PyObject *unicode)

   Retorna la longitud de la cadena de caracteres Unicode, en puntos
   de código. *unicode* tiene que ser un objeto Unicode en la
   representación "canónica" (no marcada).

   Added in version 3.3.

Py_UCS1 *PyUnicode_1BYTE_DATA(PyObject *unicode)
Py_UCS2 *PyUnicode_2BYTE_DATA(PyObject *unicode)
Py_UCS4 *PyUnicode_4BYTE_DATA(PyObject *unicode)

   Retorna un puntero a la representación canónica emitida a los tipos
   enteros UCS1, UCS2 o UCS4 para el acceso directo a los caracteres.
   No se realizan verificaciones si la representación canónica tiene
   el tamaño de carácter correcto; use "PyUnicode_KIND()" para
   seleccionar la función correcta.

   Added in version 3.3.

PyUnicode_1BYTE_KIND
PyUnicode_2BYTE_KIND
PyUnicode_4BYTE_KIND

   Retorna los valores de la macro "PyUnicode_KIND()".

   Added in version 3.3.

   Distinto en la versión 3.12: "PyUnicode_WCHAR_KIND" ha sido
   eliminada.

int PyUnicode_KIND(PyObject *unicode)

   Retorna una de las constantes de tipo "PyUnicode" (ver arriba) que
   indican cuántos bytes por carácter utiliza este objeto Unicode para
   almacenar sus datos. *unicode* tiene que ser un objeto Unicode en
   la representación "canónica" (no verificada).

   Added in version 3.3.

void *PyUnicode_DATA(PyObject *unicode)

   Retorna un puntero vacío al búfer Unicode sin formato. *unicode*
   tiene que ser un objeto Unicode en la representación "canónica" (no
   marcada).

   Added in version 3.3.

void PyUnicode_WRITE(int kind, void *data, Py_ssize_t index, Py_UCS4 value)

   Write the code point *value* to the given zero-based *index* in a
   string.

   The *kind* value and *data* pointer must have been obtained from a
   string using "PyUnicode_KIND()" and "PyUnicode_DATA()"
   respectively. You must hold a reference to that string while
   calling "PyUnicode_WRITE()". All requirements of
   "PyUnicode_WriteChar()" also apply.

   The function performs no checks for any of its requirements, and is
   intended for usage in loops.

   Added in version 3.3.

Py_UCS4 PyUnicode_READ(int kind, void *data, Py_ssize_t index)

   Lee un punto de código de una representación canónica *data*
   (obtenido con "PyUnicode_DATA()"). No se realizan verificaciones ni
   llamadas preparadas.

   Added in version 3.3.

Py_UCS4 PyUnicode_READ_CHAR(PyObject *unicode, Py_ssize_t index)

   Lee un carácter de un objeto Unicode *unicode*, que debe estar en
   la representación "canónica". Esto es menos eficiente que
   "PyUnicode_READ()" si realiza varias lecturas consecutivas.

   Added in version 3.3.

Py_UCS4 PyUnicode_MAX_CHAR_VALUE(PyObject *unicode)

   Retorna el punto de código máximo adecuado para crear otra cadena
   basada en *unicode*, que debe estar en la representación
   "canónica". Esto siempre es una aproximación pero más eficiente que
   iterar sobre la cadena.

   Added in version 3.3.

int PyUnicode_IsIdentifier(PyObject *unicode)
    * Part of the Stable ABI.*

   Retorna "1" si la cadena de caracteres es un identificador válido
   de acuerdo con la definición del lenguaje, sección Names
   (identifiers and keywords). Retorna "0" de lo contrario.

   Distinto en la versión 3.9: La función ya no llama a
   "Py_FatalError()" si la cadena de caracteres no está lista.

unsigned int PyUnicode_IS_ASCII(PyObject *unicode)

   Return true if the string only contains ASCII characters.
   Equivalent to "str.isascii()".

   Added in version 3.2.

### Propiedades de caracteres Unicode

Unicode proporciona muchas propiedades de caracteres diferentes. Los
que se necesitan con mayor frecuencia están disponibles a través de
estas macros que se asignan a las funciones de C según la
configuración de Python.

int Py_UNICODE_ISSPACE(Py_UCS4 ch)

   Retorna "1" o "0" dependiendo de si *ch* es un carácter de espacio
   en blanco.

int Py_UNICODE_ISLOWER(Py_UCS4 ch)

   Retorna "1" o "0" dependiendo de si *ch* es un carácter en
   minúscula.

int Py_UNICODE_ISUPPER(Py_UCS4 ch)

   Retorna "1" o "0" dependiendo de si *ch* es un carácter en
   mayúscula.

int Py_UNICODE_ISTITLE(Py_UCS4 ch)

   Retorna "1" o "0" dependiendo de si *ch* es un carácter en caso de
   título (*titlecase*).

int Py_UNICODE_ISLINEBREAK(Py_UCS4 ch)

   Retorna "1" o "0" dependiendo de si *ch* es un carácter de salto de
   línea.

int Py_UNICODE_ISDECIMAL(Py_UCS4 ch)

   Retorna "1" o "0" dependiendo de si *ch* es un carácter decimal o
   no.

int Py_UNICODE_ISDIGIT(Py_UCS4 ch)

   Retorna "1" o "0" dependiendo de si *ch* es un carácter de dígitos.

int Py_UNICODE_ISNUMERIC(Py_UCS4 ch)

   Retorna "1" o "0" dependiendo de si *ch* es un carácter numérico.

int Py_UNICODE_ISALPHA(Py_UCS4 ch)

   Retorna "1" o "0" dependiendo de si *ch* es un carácter alfabético.

int Py_UNICODE_ISALNUM(Py_UCS4 ch)

   Retorna "1" o "0" dependiendo de si *ch* es un carácter
   alfanumérico.

int Py_UNICODE_ISPRINTABLE(Py_UCS4 ch)

   Return "1" or "0" depending on whether *ch* is a printable
   character, in the sense of "str.isprintable()".

Estas API se pueden usar para conversiones caracteres rápidas y
directos:

Py_UCS4 Py_UNICODE_TOLOWER(Py_UCS4 ch)

   Retorna el carácter *ch* convertido a minúsculas.

Py_UCS4 Py_UNICODE_TOUPPER(Py_UCS4 ch)

   Retorna el carácter *ch* convertido a mayúsculas.

Py_UCS4 Py_UNICODE_TOTITLE(Py_UCS4 ch)

   Retorna el carácter *ch* convertido a formato de título
   (*titlecase*).

int Py_UNICODE_TODECIMAL(Py_UCS4 ch)

   Retorna el carácter *ch* convertido a un entero positivo decimal.
   Retorna "-1" si esto no es posible. Esta función no lanza
   excepciones.

int Py_UNICODE_TODIGIT(Py_UCS4 ch)

   Retorna el carácter *ch* convertido a un entero de un solo dígito.
   Retorna "-1" si esto no es posible. Esta función no lanza
   excepciones.

double Py_UNICODE_TONUMERIC(Py_UCS4 ch)

   Retorna el carácter *ch* convertido a doble. Retorna "-1.0" si esto
   no es posible. Esta función no lanza excepciones.

Estas API se pueden usar para trabajar con sustitutos:

int Py_UNICODE_IS_SURROGATE(Py_UCS4 ch)

   Comprueba si *ch* es un sustituto ("0xD800 <= ch <= 0xDFFF").

int Py_UNICODE_IS_HIGH_SURROGATE(Py_UCS4 ch)

   Comprueba si *ch* es un sustituto alto ("0xD800 <= ch <= 0xDFFF").

int Py_UNICODE_IS_LOW_SURROGATE(Py_UCS4 ch)

   Comprueba si *ch* es un sustituto bajo ("0xD800 <= ch <= 0xDFFF").

Py_UCS4 Py_UNICODE_HIGH_SURROGATE(Py_UCS4 ch)

   Return the high UTF-16 surrogate ("0xD800" to "0xDBFF") for a
   Unicode code point in the range "[0x10000; 0x10FFFF]".

Py_UCS4 Py_UNICODE_LOW_SURROGATE(Py_UCS4 ch)

   Return the low UTF-16 surrogate ("0xDC00" to "0xDFFF") for a
   Unicode code point in the range "[0x10000; 0x10FFFF]".

Py_UCS4 Py_UNICODE_JOIN_SURROGATES(Py_UCS4 high, Py_UCS4 low)

   Join two surrogate code points and return a single "Py_UCS4" value.
   *high* and *low* are respectively the leading and trailing
   surrogates in a surrogate pair. *high* must be in the range
   "[0xD800; 0xDBFF]" and *low* must be in the range "[0xDC00;
   0xDFFF]".

### Creando y accediendo a cadenas de caracteres Unicode

Para crear objetos Unicode y acceder a sus propiedades de secuencia
básicas, use estas API:

PyObject *PyUnicode_New(Py_ssize_t size, Py_UCS4 maxchar)
    *Return value: New reference.*

   Crea un nuevo objeto Unicode. *maxchar* debe ser el punto de código
   máximo que se colocará en la cadena de caracteres. Como una
   aproximación, se puede redondear al valor más cercano en la
   secuencia 127, 255, 65535, 1114111.

   En caso de error, establecer una excepción y devolver "NULL".

   After creation, the string can be filled by
   "PyUnicode_WriteChar()", "PyUnicode_CopyCharacters()",
   "PyUnicode_Fill()", "PyUnicode_WRITE()" or similar. Since strings
   are supposed to be immutable, take care to not “use” the result
   while it is being modified. In particular, before it's filled with
   its final contents, a string:

   * must not be hashed,

   * must not be "converted to UTF-8", or another non-"canonical"
     representation,

   * must not have its reference count changed,

   * must not be shared with code that might do one of the above.

   This list is not exhaustive. Avoiding these uses is your
   responsibility; Python does not always check these requirements.

   To avoid accidentally exposing a partially-written string object,
   prefer using the "PyUnicodeWriter" API, or one of the
   "PyUnicode_From*" functions below.

   Added in version 3.3.

PyObject *PyUnicode_FromKindAndData(int kind, const void *buffer, Py_ssize_t size)
    *Return value: New reference.*

   Crea un nuevo objeto Unicode con el tipo *kind* dado (los valores
   posibles son "PyUnicode_1BYTE_KIND" etc., según lo retornado por
   "PyUnicode_KIND()"). El *búfer* debe apuntar a un vector (*array*)
   de *tamaño* unidades de 1, 2 o 4 bytes por carácter, según el tipo.

   Si es necesario, la entrada *buffer* se copia y se transforma en la
   representación canónica. Por ejemplo, si el *buffer* es una cadena
   de caracteres UCS4 ("PyUnicode_4BYTE_KIND") y consta solo de puntos
   de código en el rango UCS1, se transformará en UCS1
   ("PyUnicode_1BYTE_KIND").

   Added in version 3.3.

PyObject *PyUnicode_FromStringAndSize(const char *str, Py_ssize_t size)
    *Return value: New reference.** Part of the Stable ABI.*

   Crea un objeto Unicode desde el búfer de caracteres *str*. Los
   bytes se interpretarán como codificados en UTF-8. El búfer se copia
   en el nuevo objeto. El valor de retorno podría ser un objeto
   compartido, es decir, no se permite la modificación de los datos.

   Esta función lanza "SystemError" cuando:

   * *size* < 0,

   * *str* es "NULL" y *size* > 0

   Distinto en la versión 3.12: *str* == "NULL" con *size* > 0 ya no
   está permitido.

PyObject *PyUnicode_FromString(const char *str)
    *Return value: New reference.** Part of the Stable ABI.*

   Crea un objeto Unicode a partir de un búfer *str* de caracteres
   terminado en nulo y codificado en UTF-8.

PyObject *PyUnicode_FromFormat(const char *format, ...)
    *Return value: New reference.** Part of the Stable ABI.*

   Toma una cadena de caracteres *format* con el estilo de "printf()"
   en C y un número variable de argumentos, calcula el tamaño de la
   cadena Python Unicode resultante y retorna una cadena de caracteres
   con los valores formateados. Los argumentos variables deben ser
   tipos de C y deben corresponder exactamente a los caracteres de
   formato en la cadena de caracteres *format* codificada en ASCII.

   Un especificador de conversión contiene dos o más caracteres y
   tiene los siguientes componentes, que deben aparecer en este orden:

   1. El carácter "'%'", que marca el inicio del especificador.

   2. Indicadores de conversión (opcional), que afectan el resultado
      de algunos tipos de conversión.

   3. Ancho de campo mínimo (opcional). Si se especifica como un "'*'"
      (asterisco), el ancho real se proporciona en el siguiente
      argumento, que debe ser de tipo int, y el objeto a convertir
      viene después del ancho de campo mínimo y la precisión opcional.

   4. Precisión (opcional), dada como un "'.'" (punto) seguido de la
      precisión. Si se especifica como "'*'" (un asterisco), la
      precisión real se proporciona en el siguiente argumento, que
      debe ser de tipo int, y el valor a convertir viene después de la
      precisión.

   5. Modificador de longitud (opcional).

   6. Tipo de conversión.

   Los caracteres de los indicadores de conversión son:

   +---------+---------------------------------------------------------------+
   | Indica  | Significado                                                   |
   | dor     |                                                               |
   |=========|===============================================================|
   | "0"     | La conversión se rellenará con ceros para valores numéricos.  |
   +---------+---------------------------------------------------------------+
   | "-"     | El valor convertido se ajusta a la izquierda (anula el        |
   |         | indicador "0" si ambos están dados).                          |
   +---------+---------------------------------------------------------------+

   Los modificadores de longitud para las siguientes conversiones de
   enteros ("d", "i", "o", "u", "x" o "X") especifican el tipo del
   argumento (int por defecto):

   +------------+-------------------------------------------------------+
   | Modificad  | Tipos                                                 |
   | or         |                                                       |
   |============|=======================================================|
   | "l"        | long o unsigned long                                  |
   +------------+-------------------------------------------------------+
   | "ll"       | long long o unsigned long long                        |
   +------------+-------------------------------------------------------+
   | "j"        | "intmax_t" o "uintmax_t"                              |
   +------------+-------------------------------------------------------+
   | "z"        | "size_t" o "ssize_t"                                  |
   +------------+-------------------------------------------------------+
   | "t"        | "ptrdiff_t"                                           |
   +------------+-------------------------------------------------------+

   El modificador de longitud "l" para las siguientes conversiones "s"
   o "V" especifica que el tipo del argumento es const wchar_t*.

   Los especificadores de conversión son:

   +-----------------------------------+-----------------------------------+-----------------------------------+
   | Especificador de conversión       | Tipo                              | Comentario                        |
   |===================================|===================================|===================================|
   | "%"                               | *n/a*                             | El carácter literal "%".          |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "d", "i"                          | Especificado por el modificador   | La representación decimal de un   |
   |                                   | de longitud                       | entero C con signo.               |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "u"                               | Especificado por el modificador   | La representación decimal de un   |
   |                                   | de longitud                       | entero C sin signo.               |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "o"                               | Especificado por el modificador   | La representación octal de un     |
   |                                   | de longitud                       | entero C sin signo.               |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "x"                               | Especificado por el modificador   | La representación hexadecimal de  |
   |                                   | de longitud                       | un entero C sin signo             |
   |                                   |                                   | (minúsculas).                     |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "X"                               | Especificado por el modificador   | La representación hexadecimal de  |
   |                                   | de longitud                       | un entero C sin signo             |
   |                                   |                                   | (mayúsculas).                     |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "c"                               | int                               | Un solo carácter.                 |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "s"                               | const char* o const wchar_t*      | Un arreglo de caracteres de C     |
   |                                   |                                   | terminada en nulo.                |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "p"                               | const void*                       | La representación hexadecimal de  |
   |                                   |                                   | un puntero en C. Principalmente   |
   |                                   |                                   | equivalente a "printf("%p")"      |
   |                                   |                                   | excepto que se garantiza que      |
   |                                   |                                   | comience con el literal "0x",     |
   |                                   |                                   | independientemente de lo que      |
   |                                   |                                   | produzca el "printf" de la        |
   |                                   |                                   | plataforma.                       |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "A"                               | PyObject*                         | El resultado de llamar "ascii()". |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "U"                               | PyObject*                         | Un objeto unicode.                |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "V"                               | PyObject*, const char* o const    | Un objeto Unicode (que puede ser  |
   |                                   | wchar_t*                          | "NULL") y un arreglo de           |
   |                                   |                                   | caracteres C terminado en nulo    |
   |                                   |                                   | como segundo parámetro (que se    |
   |                                   |                                   | utilizará, si el primer parámetro |
   |                                   |                                   | es "NULL").Un objeto Unicode (que |
   |                                   |                                   | puede ser "NULL") y un arreglo de |
   |                                   |                                   | caracteres de C terminada en nulo |
   |                                   |                                   | como segundo parámetro (que se    |
   |                                   |                                   | utilizará, si el primer parámetro |
   |                                   |                                   | es "NULL").                       |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "S"                               | PyObject*                         | El resultado de llamar            |
   |                                   |                                   | "PyObject_Str()".                 |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "R"                               | PyObject*                         | El resultado de llamar            |
   |                                   |                                   | "PyObject_Repr()".                |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "T"                               | PyObject*                         | Obtener el nombre completamente   |
   |                                   |                                   | cualificado de un tipo de objeto; |
   |                                   |                                   | llamar a                          |
   |                                   |                                   | "PyType_GetFullyQualifiedName()". |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "#T"                              | PyObject*                         | Similar al formato "T", pero usa  |
   |                                   |                                   | dos puntos (":") como separador   |
   |                                   |                                   | entre el nombre del módulo y el   |
   |                                   |                                   | nombre cualificado.               |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "N"                               | PyTypeObject*                     | Obtener el nombre completamente   |
   |                                   |                                   | cualificado de un tipo; llamar a  |
   |                                   |                                   | "PyType_GetFullyQualifiedName()". |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "#N"                              | PyTypeObject*                     | Similar al formato "N", pero usa  |
   |                                   |                                   | dos puntos (":") como separador   |
   |                                   |                                   | entre el nombre del módulo y el   |
   |                                   |                                   | nombre cualificado.               |
   +-----------------------------------+-----------------------------------+-----------------------------------+

   Nota:

     La unidad del formateador de ancho es el número de caracteres en
     lugar de bytes. La unidad del formateador de precisión es la
     cantidad de bytes o elementos "wchar_t" (si se usa el modificador
     de longitud "l") para ""%s"" y ""%V"" (si el argumento
     "PyObject*" es "NULL"), y una cantidad de caracteres para ""%A"",
     ""%U"", ""%S"", ""%R"" y ""%V"" (si el argumento "PyObject*" no
     es "NULL").

   Nota:

     A diferencia de "printf()" de C, el indicador "0" tiene efecto
     incluso cuando se proporciona una precisión para conversiones de
     enteros ("d", "i", "u", "o", "x" o "X").

   Distinto en la versión 3.2: Soporte agregado para ""%lld"" y
   ""%llu"".

   Distinto en la versión 3.3: Soporte agregado para ""%li"", ""%lli""
   y ""%zi"".

   Distinto en la versión 3.4: Soporte agregado para formateadores de
   anchura y precisión para ""%s"", ""%A"", ""%U"", ""%V"", ""%S"",
   ""%R"".

   Distinto en la versión 3.12: Soporte para los especificadores de
   conversión "o" y "X". Soporte para los modificadores de longitud
   "j" y "t". Los modificadores de longitud ahora se aplican a todas
   las conversiones de enteros. El modificador de longitud "l" ahora
   se aplica a los especificadores de conversión "s" y "V". Soporte
   para ancho y precisión variables "*". Soporte para el indicador
   "-".Un carácter de formato no reconocido ahora establece un
   "SystemError". En versiones anteriores, hacía que el resto de la
   cadena de formato se copiara tal cual a la cadena resultante, y
   cualquier argumento extra se descartaba.

   Distinto en la versión 3.13: Soporte agregado para los formatos
   "%T", "%#T", "%N" y "%#N".

PyObject *PyUnicode_FromFormatV(const char *format, va_list vargs)
    *Return value: New reference.** Part of the Stable ABI.*

   Idéntico a "PyUnicode_FromFormat()" excepto que toma exactamente
   dos argumentos.

PyObject *PyUnicode_FromObject(PyObject *obj)
    *Return value: New reference.** Part of the Stable ABI.*

   Copia una instancia de un subtipo Unicode a un nuevo objeto Unicode
   verdadero si es necesario. Si *obj* ya es un verdadero objeto
   Unicode (no un subtipo), retorna una nueva *referencia fuerte* al
   objeto.

   Los objetos que no sean Unicode o sus subtipos causarán un
   "TypeError".

PyObject *PyUnicode_FromOrdinal(int ordinal)
    *Return value: New reference.** Part of the Stable ABI.*

   Create a Unicode Object from the given Unicode code point
   *ordinal*.

   The ordinal must be in "range(0x110000)". A "ValueError" is raised
   in the case it is not.

PyObject *PyUnicode_FromEncodedObject(PyObject *obj, const char *encoding, const char *errors)
    *Return value: New reference.** Part of the Stable ABI.*

   Decodifica un objeto codificado *obj* en un objeto Unicode.

   "bytes", "bytearray" y otros *los objetos similares a bytes* se
   decodifican de acuerdo con el *encoding* dado y utilizan el manejo
   de errores definido por *errors*. Ambos pueden ser "NULL" para que
   la interfaz use los valores predeterminados (ver Códecs
   incorporados para más detalles).

   Todos los demás objetos, incluidos los objetos Unicode, hacen que
   se establezca un "TypeError".

   La API retorna "NULL" si hubo un error. La entidad que hace la
   llamadas es la responsable de desreferenciar los objetos
   retornados.

void PyUnicode_Append(PyObject **p_left, PyObject *right)
    * Part of the Stable ABI.*

   Append the string *right* to the end of *p_left*. *p_left* must
   point to a *strong reference* to a Unicode object;
   "PyUnicode_Append()" releases ("*steals*") this reference.

   On error, set **p_left* to "NULL" and set an exception.

   On success, set **p_left* to a new strong reference to the result.

void PyUnicode_AppendAndDel(PyObject **p_left, PyObject *right)
    * Part of the Stable ABI.*

   The function is similar to "PyUnicode_Append()", with the only
   difference being that it decrements the reference count of *right*
   by one.

PyObject *PyUnicode_BuildEncodingMap(PyObject *string)
    *Return value: New reference.** Part of the Stable ABI.*

   Return a mapping suitable for decoding a custom single-byte
   encoding. Given a Unicode string *string* of up to 256 characters
   representing an encoding table, returns either a compact internal
   mapping object or a dictionary mapping character ordinals to byte
   values. Raises a "TypeError" and return "NULL" on invalid input.

   Added in version 3.2.

const char *PyUnicode_GetDefaultEncoding(void)
    * Part of the Stable ABI.*

   Return the name of the default string encoding, ""utf-8"". See
   "sys.getdefaultencoding()".

   The returned string does not need to be freed, and is valid until
   interpreter shutdown.

Py_ssize_t PyUnicode_GetLength(PyObject *unicode)
    * Part of the Stable ABI since version 3.7.*

   Retorna la longitud del objeto Unicode, en puntos de código.

   En caso de error, establece una excepción y retorna "-1".

   Added in version 3.3.

Py_ssize_t PyUnicode_CopyCharacters(PyObject *to, Py_ssize_t to_start, PyObject *from, Py_ssize_t from_start, Py_ssize_t how_many)

   Copia caracteres de un objeto Unicode en otro. Esta función realiza
   la conversión de caracteres cuando es necesario y recurre a
   "memcpy()" si es posible. Retorna "-1" y establece una excepción en
   caso de error; de lo contrario, retorna el número de caracteres
   copiados.

   The string must not have been “used” yet. See "PyUnicode_New()" for
   details.

   Added in version 3.3.

int PyUnicode_Resize(PyObject **unicode, Py_ssize_t length);
    * Part of the Stable ABI.*

   Resize a Unicode object **unicode* to the new *length* in code
   points.

   Try to resize the string in place (which is usually faster than
   allocating a new string and copying characters), or create a new
   string.

   **unicode* is modified to point to the new (resized) object and "0"
   is returned on success. Otherwise, "-1" is returned and an
   exception is set, and **unicode* is left untouched.

   The function doesn't check string content, the result may not be a
   string in canonical representation.

Py_ssize_t PyUnicode_Fill(PyObject *unicode, Py_ssize_t start, Py_ssize_t length, Py_UCS4 fill_char)

   Rellena una cadena con un carácter: escriba *fill_char* en
   "unicode[inicio:inicio+longitud]".

   Falla si *fill_char* es más grande que el carácter máximo de la
   cadena, o si la cadena tiene más de 1 referencia.

   The string must not have been “used” yet. See "PyUnicode_New()" for
   details.

   Return the number of written characters, or return "-1" and raise
   an exception on error.

   Added in version 3.3.

int PyUnicode_WriteChar(PyObject *unicode, Py_ssize_t index, Py_UCS4 character)
    * Part of the Stable ABI since version 3.7.*

   Write a *character* to the string *unicode* at the zero-based
   *index*. Return "0" on success, "-1" on error with an exception
   set.

   This function checks that *unicode* is a Unicode object, that the
   index is not out of bounds, and that the object's reference count
   is one. See "PyUnicode_WRITE()" for a version that skips these
   checks, making them your responsibility.

   The string must not have been “used” yet. See "PyUnicode_New()" for
   details.

   Added in version 3.3.

Py_UCS4 PyUnicode_ReadChar(PyObject *unicode, Py_ssize_t index)
    * Part of the Stable ABI since version 3.7.*

   Lee un carácter de una cadena. Esta función verifica que *unicode*
   es un objeto Unicode y que el índice no está fuera de límites, en
   contraste con la macro "PyUnicode_READ_CHAR()", que no realiza
   ninguna comprobación de errores.

   Retorna el carácter en caso de éxito, "-1" en caso de error con una
   excepción establecida.

   Added in version 3.3.

PyObject *PyUnicode_Substring(PyObject *unicode, Py_ssize_t start, Py_ssize_t end)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.7.*

   Retorna una subcadena de *unicode*, desde el índice de caracteres
   *start* (incluido) hasta el índice de caracteres *end* (excluido).
   Los índices negativos no son compatibles. En caso de error,
   establece una excepción y retorna "NULL".

   Added in version 3.3.

Py_UCS4 *PyUnicode_AsUCS4(PyObject *unicode, Py_UCS4 *buffer, Py_ssize_t buflen, int copy_null)
    * Part of the Stable ABI since version 3.7.*

   Copia la cadena *unicode* en un búfer UCS4, incluyendo un carácter
   nulo, si *copy_null* está configurado. Retorna "NULL" y establece
   una excepción en caso de error (en particular, un "SystemError" si
   *buflen* es menor que la longitud de *unicode*). Se retorna
   *buffer* en caso de éxito.

   Added in version 3.3.

Py_UCS4 *PyUnicode_AsUCS4Copy(PyObject *unicode)
    * Part of the Stable ABI since version 3.7.*

   Copia la cadena *unicode* en un nuevo búfer UCS4 que se asigna
   usando "PyMem_Malloc()". Si esto falla, retorna "NULL" con un
   "MemoryError" establecido. El búfer retornado siempre tiene un
   punto de código nulo adicional agregado.

   Added in version 3.3.

### Codificación regional

La codificación local actual se puede utilizar para decodificar texto
del sistema operativo.

PyObject *PyUnicode_DecodeLocaleAndSize(const char *str, Py_ssize_t length, const char *errors)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.7.*

   Decodifica una cadena de caracteres UTF-8 en Android y VxWorks, o
   de la codificación de configuración regional actual en otras
   plataformas. Los manejadores de errores admitidos son ""estricto""
   y ""subrogateescape"" (**PEP 383**). El decodificador usa el
   controlador de errores ""estricto"" si *errors* es "NULL". *str*
   debe terminar con un carácter nulo pero no puede contener
   caracteres nulos incrustados.

   Use "PyUnicode_DecodeFSDefaultAndSize()" para decodificar una
   cadena desde el *codificador de sistema de archivos y gestor de
   errores*.

   Esta función ignora el modo Python UTF-8.

   Ver también: La función "Py_DecodeLocale()".

   Added in version 3.3.

   Distinto en la versión 3.7: La función ahora también usa la
   codificación de configuración regional actual para el controlador
   de errores "subrogateescape", excepto en Android. Anteriormente,
   "Py_DecodeLocale()" se usaba para el "subrogateescape", y la
   codificación local actual se usaba para "estricto".

PyObject *PyUnicode_DecodeLocale(const char *str, const char *errors)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.7.*

   Similar a "PyUnicode_DecodeLocaleAndSize()", pero calcula la
   longitud de la cadena usando "strlen()".

   Added in version 3.3.

PyObject *PyUnicode_EncodeLocale(PyObject *unicode, const char *errors)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.7.*

   Codifica un objeto Unicode UTF-8 en Android y VxWorks, o en la
   codificación local actual en otras plataformas. Los manejadores de
   errores admitidos son ""estricto"" y ""subrogateescape"" (**PEP
   383**). El codificador utiliza el controlador de errores
   ""estricto"" si *errors* es "NULL". Retorna un objeto "bytes".
   *unicode* no puede contener caracteres nulos incrustados.

   Use "PyUnicode_EncodeFSDefault()" para codificar una cadena al
   *codificador de sistema de archivos y gestor de errores*.

   Esta función ignora el modo Python UTF-8.

   Ver también: La función "Py_EncodeLocale()".

   Added in version 3.3.

   Distinto en la versión 3.7: La función ahora también usa la
   codificación de configuración regional actual para el controlador
   de errores "subrogateescape", excepto en Android. Anteriormente,
   "Py_EncodeLocale()" se usaba para el "subrogateescape", y la
   codificación local actual se usaba para "estricto".

### Codificación del sistema de archivos

Funciones que codifican y decodifican desde el *codificador de sistema
de archivos y gestor de errores* (**PEP 383** y **PEP 529**).

To encode file names to "bytes" during argument parsing, the ""O&""
converter should be used, passing "PyUnicode_FSConverter()" as the
conversion function:

int PyUnicode_FSConverter(PyObject *obj, void *result)
    * Part of the Stable ABI.*

   PyArg_Parse* converter: encode "str" objects -- obtained directly
   or through the "os.PathLike" interface -- to "bytes" using
   "PyUnicode_EncodeFSDefault()"; "bytes" objects are output as-is.
   *result* must be an address of a C variable of type PyObject* (or
   PyBytesObject*). On success, set the variable to a new *strong
   reference* to a bytes object which must be released when it is no
   longer used and return a non-zero value ("Py_CLEANUP_SUPPORTED").
   Embedded null bytes are not allowed in the result. On failure,
   return "0" with an exception set.

   If *obj* is "NULL", the function releases a strong reference stored
   in the variable referred by *result* and returns "1".

   Added in version 3.1.

   Distinto en la versión 3.6: Acepta un objeto similar a una ruta
   (*path-like object*).

To decode file names to "str" during argument parsing, the ""O&""
converter should be used, passing "PyUnicode_FSDecoder()" as the
conversion function:

int PyUnicode_FSDecoder(PyObject *obj, void *result)
    * Part of the Stable ABI.*

   PyArg_Parse* converter: decode "bytes" objects -- obtained either
   directly or indirectly through the "os.PathLike" interface -- to
   "str" using "PyUnicode_DecodeFSDefaultAndSize()"; "str" objects are
   output as-is. *result* must be an address of a C variable of type
   PyObject* (or PyUnicodeObject*). On success, set the variable to a
   new *strong reference* to a Unicode object which must be released
   when it is no longer used and return a non-zero value
   ("Py_CLEANUP_SUPPORTED"). Embedded null characters are not allowed
   in the result. On failure, return "0" with an exception set.

   If *obj* is "NULL", release the strong reference to the object
   referred to by *result* and return "1".

   Added in version 3.2.

   Distinto en la versión 3.6: Acepta un objeto similar a una ruta
   (*path-like object*).

PyObject *PyUnicode_DecodeFSDefaultAndSize(const char *str, Py_ssize_t size)
    *Return value: New reference.** Part of the Stable ABI.*

   Decodifica una cadena desde el *codificador de sistema de archivos
   y gestor de errores*.

   Si necesita decodificar una cadena desde la codificación de
   configuración regional actual, use
   "PyUnicode_DecodeLocaleAndSize()".

   Ver también: La función "Py_DecodeLocale()".

   Distinto en la versión 3.6: Ahora se usa el *manejador de errores
   del sistema de archivos*.

PyObject *PyUnicode_DecodeFSDefault(const char *str)
    *Return value: New reference.** Part of the Stable ABI.*

   Decodifica una cadena terminada en nulo desde el *codificador de
   sistema de archivos y gestor de errores*.

   Si se conoce la longitud de la cadena, utilice
   "PyUnicode_DecodeFSDefaultAndSize()".

   Distinto en la versión 3.6: Ahora se usa el *manejador de errores
   del sistema de archivos*.

PyObject *PyUnicode_EncodeFSDefault(PyObject *unicode)
    *Return value: New reference.** Part of the Stable ABI.*

   Codifica un objeto Unicode al *codificador de sistema de archivos y
   gestor de errores*, y retorna "bytes". Tenga en cuenta que el
   objeto resultante "bytes" puede contener bytes nulos.

   Si necesitas codificar una cadena en la codificación de la
   configuración regional actual, utiliza "PyUnicode_EncodeLocale()".

   Ver también: La función "Py_EncodeLocale()".

   Added in version 3.2.

   Distinto en la versión 3.6: Ahora se usa el *manejador de errores
   del sistema de archivos*.

### soporte wchar_t

soporte "wchar_t" para plataformas que lo soportan:

PyObject *PyUnicode_FromWideChar(const wchar_t *wstr, Py_ssize_t size)
    *Return value: New reference.** Part of the Stable ABI.*

   Crea un objeto Unicode a partir del búfer "wchar_t" *wstr* del
   tamaño *size* dado. Pasar "-1" como *size* indica que la función
   debe calcular la longitud, usando "wcslen()". Retorna "NULL" en
   caso de falla.

Py_ssize_t PyUnicode_AsWideChar(PyObject *unicode, wchar_t *wstr, Py_ssize_t size)
    * Part of the Stable ABI.*

   Copiar el contenido del objeto Unicode en el búfer "wchar_t"
   *wstr*. Como máximo se copian *size* caracteres "wchar_t"
   (excluyendo un posible carácter de terminación nulo al final).
   Devolver el número de caracteres "wchar_t" copiados o "-1" en caso
   de error.

   Cuando *wstr* es "NULL", retornar en su lugar el *size* que sería
   necesario para almacenar todo *unicode*, incluyendo un nulo de
   terminación.

   Tenga en cuenta que la cadena wchar_t* resultante puede o no
   terminar en nulo. Es responsabilidad del llamador asegurarse de que
   la cadena wchar_t* termine en nulo en caso de que la aplicación lo
   requiera. Además, tenga en cuenta que la cadena wchar_t* podría
   contener caracteres nulos, lo que provocaría que la cadena se
   truncara cuando se utiliza con la mayoría de las funciones de C.

wchar_t *PyUnicode_AsWideCharString(PyObject *unicode, Py_ssize_t *size)
    * Part of the Stable ABI since version 3.7.*

   Convierte el objeto Unicode en una cadena de caracteres ancha. La
   cadena de salida siempre termina con un carácter nulo. Si *size* no
   es "NULL", escribe el número de caracteres anchos (excluyendo el
   carácter de terminación nulo final) en **size*. Tenga en cuenta que
   la cadena resultante "wchar_t" podría contener caracteres nulos, lo
   que provocaría que la cadena se truncara cuando se usara con la
   mayoría de las funciones de C. Si *size* es "NULL" y la cadena
   wchar_t* contiene caracteres nulos un "ValueError" aparece.

   Retorna un búfer asignado por "PyMem_New" (utilice "PyMem_Free()"
   para liberarlo) en caso de éxito. En caso de error, retorna "NULL"
   y **size* no está definido. Lanza un "MemoryError" si falla la
   asignación de memoria.

   Added in version 3.2.

   Distinto en la versión 3.7: Lanza un "ValueError" si *size* es
   "NULL" y la cadena wchar_t* contiene caracteres nulos.

## Códecs incorporados

Python proporciona un conjunto de códecs integrados que están escritos
en C para mayor velocidad. Todos estos códecs se pueden usar
directamente a través de las siguientes funciones.

Muchas de las siguientes API toman dos argumentos de *encoding* y
*errors*, y tienen la misma semántica que las del constructor de
objetos de cadena incorporado "str()".

Establecer la codificación en "NULL" hace que se use la codificación
predeterminada, que es UTF-8. Las llamadas al sistema de archivos
deben usar "PyUnicode_FSConverter()" para codificar nombres de
archivos. Esto utiliza el *codificador de sistema de archivos y gestor
de errores* internamente.

El manejo de errores se establece mediante *errors* que también pueden
establecerse en "NULL", lo que significa usar el manejo predeterminado
definido para el códec. El manejo de errores predeterminado para todos
los códecs integrados es "estricto" (se lanza "ValueError").

Todos los códecs usan una interfaz similar. Solo las desviaciones de
los siguientes genéricos se documentan por simplicidad.

### Códecs genéricos

The following macro is provided:

Py_UNICODE_REPLACEMENT_CHARACTER

   The Unicode code point "U+FFFD" (replacement character).

   This Unicode character is used as the replacement character during
   decoding if the *errors* argument is set to "replace".

Estas son las APIs de códecs genéricos:

PyObject *PyUnicode_Decode(const char *str, Py_ssize_t size, const char *encoding, const char *errors)
    *Return value: New reference.** Part of the Stable ABI.*

   Crea un objeto Unicode decodificando *size* bytes de la cadena
   codificada *str*. *encoding* y *errors* tienen el mismo significado
   que los parámetros del mismo nombre en la función incorporada
   "str()". El códec que se utilizará se busca utilizando el registro
   de códec Python. Retorna "NULL" si el códec provocó una excepción.

PyObject *PyUnicode_AsEncodedString(PyObject *unicode, const char *encoding, const char *errors)
    *Return value: New reference.** Part of the Stable ABI.*

   Codifica un objeto Unicode y retorna el resultado como un objeto de
   bytes de Python. *encoding* y *errors* tienen el mismo significado
   que los parámetros del mismo nombre en el método Unicode
   "encode()". El códec que se utilizará se busca utilizando el
   registro de códec Python. Retorna "NULL" si el códec provocó una
   excepción.

### Códecs UTF-8

Estas son las APIs del códec UTF-8:

PyObject *PyUnicode_DecodeUTF8(const char *str, Py_ssize_t size, const char *errors)
    *Return value: New reference.** Part of the Stable ABI.*

   Crea un objeto Unicode decodificando *size* bytes de la cadena
   codificada UTF-8 *str*. Retorna "NULL" si el códec provocó una
   excepción.

PyObject *PyUnicode_DecodeUTF8Stateful(const char *str, Py_ssize_t size, const char *errors, Py_ssize_t *consumed)
    *Return value: New reference.** Part of the Stable ABI.*

   Si *consumed* es "NULL", se comporta como "PyUnicode_DecodeUTF8()".
   Si *consumed* no es "NULL", las secuencias de bytes UTF-8
   incompletas no se tratarán como un error. Esos bytes no serán
   decodificados y la cantidad de bytes que han sido decodificados se
   almacenará en *consumed*.

PyObject *PyUnicode_AsUTF8String(PyObject *unicode)
    *Return value: New reference.** Part of the Stable ABI.*

   Codifica un objeto Unicode usando UTF-8 y retorna el resultado como
   un objeto de bytes de Python. El manejo de errores es "estricto".
   Retorna "NULL" si el códec provocó una excepción.

   La función falla si la cadena contiene puntos de código sustitutos
   ("U+D800" - "U+DFFF").

const char *PyUnicode_AsUTF8AndSize(PyObject *unicode, Py_ssize_t *size)
    * Part of the Stable ABI since version 3.10.*

   Retorna un puntero a la codificación UTF-8 del objeto Unicode y
   almacena el tamaño de la representación codificada (en bytes) en
   *size*. El argumento *size* puede ser "NULL"; en este caso no se
   almacenará el tamaño. El búfer retornado siempre tiene un byte nulo
   adicional agregado (no incluido en *size*), independientemente de
   si hay otros puntos de código nulo.

   En caso de error, establecer una excepción, establecer *size* en
   "-1" (si no es NULL) y devolver "NULL".

   La función falla si la cadena contiene puntos de código sustitutos
   ("U+D800" - "U+DFFF").

   Esto almacena en caché la representación UTF-8 de la cadena en el
   objeto Unicode, y las llamadas posteriores retornarán un puntero al
   mismo búfer. El llamador no es responsable de desasignar el búfer.
   El búfer se desasigna y los punteros al mismo se invalidan cuando
   el objeto Unicode es recolectado por el recolector de basura.

   Added in version 3.3.

   Distinto en la versión 3.7: The return type is now "const char *"
   rather than "char *".

   Distinto en la versión 3.10: Esta función es parte de la API
   limitada.

const char *PyUnicode_AsUTF8(PyObject *unicode)

   Como "PyUnicode_AsUTF8AndSize()", pero no almacena el tamaño.

   Advertencia:

     This function does not have any special behavior for null
     characters embedded within *unicode*. As a result, strings
     containing null characters will remain in the returned string,
     which some C functions might interpret as the end of the string,
     leading to truncation. If truncation is an issue, it is
     recommended to use "PyUnicode_AsUTF8AndSize()" instead.

   Added in version 3.3.

   Distinto en la versión 3.7: The return type is now "const char *"
   rather than "char *".

### Códecs UTF-32

Estas son las APIs de códecs para UTF-32:

PyObject *PyUnicode_DecodeUTF32(const char *str, Py_ssize_t size, const char *errors, int *byteorder)
    *Return value: New reference.** Part of the Stable ABI.*

   Decodifica *size* bytes de una cadena de búfer codificada UTF-32 y
   retorna el objeto Unicode correspondiente. *errors* (si no es
   "NULL") define el manejo de errores. Su valor predeterminado es
   "estricto".

   Si *byteorder* no es "NULL", el decodificador comienza a
   decodificar utilizando el orden de bytes dado:

      *byteorder == -1: little endian
      *byteorder == 0:  native order
      *byteorder == 1:  big endian

   Si "*byteorder" es cero, y los primeros cuatro bytes de los datos
   de entrada son una marca de orden de bytes (BOM), el decodificador
   cambia a este orden de bytes y la BOM no se copia en la cadena de
   caracteres Unicode resultante. Si "*byteorder" es "-1" o "1",
   cualquier marca de orden de bytes se copia en la salida.

   Una vez completado, **byteorder* se establece en el orden de bytes
   actual al final de los datos de entrada.

   Si *byteorder* es "NULL", el códec se inicia en modo de orden
   nativo.

   Retorna "NULL" si el códec provocó una excepción.

PyObject *PyUnicode_DecodeUTF32Stateful(const char *str, Py_ssize_t size, const char *errors, int *byteorder, Py_ssize_t *consumed)
    *Return value: New reference.** Part of the Stable ABI.*

   Si *consumed* es "NULL", se comporta como
   "PyUnicode_DecodeUTF32()". Si *consumed* no es "NULL",
   "PyUnicode_DecodeUTF32Stateful()" no tratará las secuencias de
   bytes UTF-32 incompletas finales (como un número de bytes no
   divisible por cuatro) como un error. Esos bytes no serán
   decodificados y la cantidad de bytes que han sido decodificados se
   almacenará en *consumed*.

PyObject *PyUnicode_AsUTF32String(PyObject *unicode)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna una cadena de bytes de Python usando la codificación UTF-32
   en orden de bytes nativo. La cadena siempre comienza con una marca
   BOM. El manejo de errores es "estricto". Retorna "NULL" si el códec
   provocó una excepción.

### Códecs UTF-16

Estas son las APIs de códecs para UTF-16:

PyObject *PyUnicode_DecodeUTF16(const char *str, Py_ssize_t size, const char *errors, int *byteorder)
    *Return value: New reference.** Part of the Stable ABI.*

   Decodifica *size* bytes de una cadena de caracteres de búfer
   codificada UTF-16 y retorna el objeto Unicode correspondiente.
   *errors* (si no es "NULL") define el manejo de errores. Su valor
   predeterminado es "estricto".

   Si *byteorder* no es "NULL", el decodificador comienza a
   decodificar utilizando el orden de bytes dado:

      *byteorder == -1: little endian
      *byteorder == 0:  native order
      *byteorder == 1:  big endian

   Si "*byteorder" es cero, y los primeros dos bytes de los datos de
   entrada son una marca de orden de bytes (BOM), el decodificador
   cambia a este orden de bytes y la BOM no se copia en la cadena de
   caracteres Unicode resultante. Si "*byteorder" es "-1" o "1",
   cualquier marca de orden de bytes se copia en la salida (donde dará
   como resultado un "\ufeff" o un carácter "\ufffe").

   Una vez completado, **byteorder* se establece en el orden de bytes
   actual al final de los datos de entrada.

   Si *byteorder* es "NULL", el códec se inicia en modo de orden
   nativo.

   Retorna "NULL" si el códec provocó una excepción.

PyObject *PyUnicode_DecodeUTF16Stateful(const char *str, Py_ssize_t size, const char *errors, int *byteorder, Py_ssize_t *consumed)
    *Return value: New reference.** Part of the Stable ABI.*

   Si *consumed* es "NULL", se comporta como
   "PyUnicode_DecodeUTF16()". Si *consumed* no es "NULL",
   "PyUnicode_DecodeUTF16Stateful()" no tratará las secuencias de
   bytes UTF-16 incompletas finales (como un número impar de bytes o
   un par sustituto dividido) como un error. Esos bytes no serán
   decodificados y la cantidad de bytes que han sido decodificados se
   almacenará en *consumed*.

PyObject *PyUnicode_AsUTF16String(PyObject *unicode)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna una cadena de bytes de Python usando la codificación UTF-16
   en orden de bytes nativo. La cadena siempre comienza con una marca
   BOM. El manejo de errores es "estricto". Retorna "NULL" si el códec
   provocó una excepción.

### Códecs UTF-7

Estas son las APIs del códec UTF-7:

PyObject *PyUnicode_DecodeUTF7(const char *str, Py_ssize_t size, const char *errors)
    *Return value: New reference.** Part of the Stable ABI.*

   Crea un objeto Unicode decodificando *size* bytes de la cadena de
   caracteres codificada UTF-7 *str*. Retorna "NULL" si el códec
   provocó una excepción.

PyObject *PyUnicode_DecodeUTF7Stateful(const char *str, Py_ssize_t size, const char *errors, Py_ssize_t *consumed)
    *Return value: New reference.** Part of the Stable ABI.*

   Si *consumed* es "NULL", se comporta como "PyUnicode_DecodeUTF7()".
   Si *consumed* no es "NULL", las secciones UTF-7 base-64 incompletas
   no se tratarán como un error. Esos bytes no serán decodificados y
   la cantidad de bytes que han sido decodificados se almacenará en
   *consumed*.

### Códecs Unicode escapado

Estas son las APIs de códecs para Unicode escapado:

PyObject *PyUnicode_DecodeUnicodeEscape(const char *str, Py_ssize_t size, const char *errors)
    *Return value: New reference.** Part of the Stable ABI.*

   Crea un objeto Unicode decodificando *size* bytes de la cadena
   codificada Unicode escapada (*Unicode-Escape*) *str*. Retorna
   "NULL" si el códec provocó una excepción.

PyObject *PyUnicode_AsUnicodeEscapeString(PyObject *unicode)
    *Return value: New reference.** Part of the Stable ABI.*

   Codifica un objeto Unicode usando Unicode escapado (*Unicode-
   Escape*) y retorna el resultado como un objeto de bytes. El manejo
   de errores es "estricto". Retorna "NULL" si el códec provocó una
   excepción.

### Códecs para Unicode escapado en bruto

Estas son las API del códec Unicode escapado en bruto (*Raw Unicode
Escape*):

PyObject *PyUnicode_DecodeRawUnicodeEscape(const char *str, Py_ssize_t size, const char *errors)
    *Return value: New reference.** Part of the Stable ABI.*

   Crea un objeto Unicode decodificando *size* bytes de la cadena de
   caracteres codificada Unicode escapada en bruto (*Raw-Unicode-
   Escape*) *str*. Retorna "NULL" si el códec provocó una excepción.

PyObject *PyUnicode_AsRawUnicodeEscapeString(PyObject *unicode)
    *Return value: New reference.** Part of the Stable ABI.*

   Codifica un objeto Unicode usando Unicode escapado en bruto (*Raw-
   Unicode-Escape*) y retorna el resultado como un objeto de bytes. El
   manejo de errores es "estricto". Retorna "NULL" si el códec provocó
   una excepción.

### Códecs Latin-1

Estas son las API del códec Latin-1: Latin-1 corresponde a los
primeros 256 ordinales Unicode y solo estos son aceptados por los
códecs durante la codificación.

PyObject *PyUnicode_DecodeLatin1(const char *str, Py_ssize_t size, const char *errors)
    *Return value: New reference.** Part of the Stable ABI.*

   Crea un objeto Unicode decodificando *size* bytes de la cadena de
   caracteres codificada en latin-1 *str*. Retorna "NULL" si el códec
   provocó una excepción.

PyObject *PyUnicode_AsLatin1String(PyObject *unicode)
    *Return value: New reference.** Part of the Stable ABI.*

   Codifica un objeto Unicode usando Latin-1 y retorna el resultado
   como un objeto de bytes Python. El manejo de errores es "estricto".
   Retorna "NULL" si el códec provocó una excepción.

### Códecs ASCII

Estas son las API del códec ASCII. Solo se aceptan datos ASCII de 7
bits. Todos los demás códigos generan errores.

PyObject *PyUnicode_DecodeASCII(const char *str, Py_ssize_t size, const char *errors)
    *Return value: New reference.** Part of the Stable ABI.*

   Crea un objeto Unicode decodificando *size* bytes de la cadena de
   caracteres codificada ASCII *str*. Retorna "NULL" si el códec
   provocó una excepción.

PyObject *PyUnicode_AsASCIIString(PyObject *unicode)
    *Return value: New reference.** Part of the Stable ABI.*

   Codifica un objeto Unicode usando ASCII y retorna el resultado como
   un objeto de bytes de Python. El manejo de errores es "estricto".
   Retorna "NULL" si el códec provocó una excepción.

### Códecs de mapa de caracteres

Este códec es especial en el sentido de que puede usarse para
implementar muchos códecs diferentes (y de hecho así se hizo para
obtener la mayoría de los códecs estándar incluidos en el paquete
"encodings"). El códec utiliza mapeos para codificar y decodificar
caracteres. Los objetos de mapeo proporcionados deben admitir la
interfaz de mapeo "__getitem__()"; los diccionarios y las secuencias
funcionan bien.

Estos son las API de códec de mapeo:

PyObject *PyUnicode_DecodeCharmap(const char *str, Py_ssize_t length, PyObject *mapping, const char *errors)
    *Return value: New reference.** Part of the Stable ABI.*

   Crea un objeto Unicode decodificando *size* bytes de la cadena de
   caracteres codificada *str* usando el objeto *mapping* dado.
   Retorna "NULL" si el códec provocó una excepción.

   Si *mapping* es "NULL", se aplicará la decodificación Latin-1. De
   lo contrario, *mapping* debe asignar bytes ordinales (enteros en el
   rango de 0 a 255) a cadenas de caracteres Unicode, enteros (que
   luego se interpretan como ordinales Unicode) o "None". Los bytes de
   datos sin asignar - los que causan un "LookupError", así como los
   que se asignan a "None", "0xFFFE" o "'\ ufffe'", se tratan como
   asignaciones indefinidas y causan un error.

PyObject *PyUnicode_AsCharmapString(PyObject *unicode, PyObject *mapping)
    *Return value: New reference.** Part of the Stable ABI.*

   Codifica un objeto Unicode usando el objeto *mapping* dado y
   retorna el resultado como un objeto de bytes. El manejo de errores
   es "estricto". Retorna "NULL" si el códec provocó una excepción.

   El objeto *mapping* debe asignar enteros ordinales Unicode a
   objetos de bytes, enteros en el rango de 0 a 255 o "None". Los
   ordinales de caracteres no asignados (los que causan un
   "LookupError"), así como los asignados a "Ninguno", se tratan como
   "mapeo indefinido" y causan un error.

La siguiente API de códec es especial en que asigna Unicode a Unicode.

PyObject *PyUnicode_Translate(PyObject *unicode, PyObject *table, const char *errors)
    *Return value: New reference.** Part of the Stable ABI.*

   Traduce una cadena de caracteres aplicando una tabla de mapeo y
   retornando  el objeto Unicode resultante. Retorna "NULL" cuando el
   códec provocó una excepción.

   La tabla de mapeo debe mapear enteros ordinales Unicode a enteros
   ordinales Unicode o "None" (causando la eliminación del carácter).

   Las tablas de mapeo solo necesitan proporcionar la interfaz
   "__getitem__()"; los diccionarios y las secuencias funcionan bien.
   Los ordinales de caracteres no asignados (los que causan un
   "LookupError") se dejan intactos y se copian tal cual.

   *errors* tiene el significado habitual para los códecs. Puede ser
   "NULL", lo que indica que debe usar el manejo de errores
   predeterminado.

### Códecs MBCS para Windows

Estas son las API de códec MBCS. Actualmente solo están disponibles en
Windows y utilizan los convertidores Win32 MBCS para implementar las
conversiones. Tenga en cuenta que MBCS (o DBCS) es una clase de
codificaciones, no solo una. La codificación de destino está definida
por la configuración del usuario en la máquina que ejecuta el códec.

PyObject *PyUnicode_DecodeMBCS(const char *str, Py_ssize_t size, const char *errors)
    *Return value: New reference.** Part of the Stable ABI on Windows
   since version 3.7.*

   Crea un objeto Unicode decodificando *size* bytes de la cadena de
   caracteres codificada con MBCS *str*. Retorna "NULL" si el códec
   provocó una excepción.

PyObject *PyUnicode_DecodeMBCSStateful(const char *str, Py_ssize_t size, const char *errors, Py_ssize_t *consumed)
    *Return value: New reference.** Part of the Stable ABI on Windows
   since version 3.7.*

   Si *consumed* es "NULL", se comporta como "PyUnicode_DecodeMBCS()".
   Si *consumed* no es "NULL", "PyUnicode_DecodeMBCSStateful()" no
   decodificará el byte inicial y el número de bytes que se han
   decodificado se almacenará en *consumed*.

PyObject *PyUnicode_DecodeCodePageStateful(int code_page, const char *str, Py_ssize_t size, const char *errors, Py_ssize_t *consumed)
    *Return value: New reference.** Part of the Stable ABI on Windows
   since version 3.7.*

   Similar to "PyUnicode_DecodeMBCSStateful()", except uses the code
   page specified by *code_page*.

PyObject *PyUnicode_AsMBCSString(PyObject *unicode)
    *Return value: New reference.** Part of the Stable ABI on Windows
   since version 3.7.*

   Codifica un objeto Unicode usando MBCS y retorna el resultado como
   un objeto de bytes de Python. El manejo de errores es "estricto".
   Retorna "NULL" si el códec provocó una excepción.

PyObject *PyUnicode_EncodeCodePage(int code_page, PyObject *unicode, const char *errors)
    *Return value: New reference.** Part of the Stable ABI on Windows
   since version 3.7.*

   Codifica el objeto Unicode utilizando la página de códigos
   especificada y retorna un objeto de bytes de Python. Retorna "NULL"
   si el códec provocó una excepción. Use la página de códigos
   "CP_ACP" para obtener el codificador MBCS.

   Added in version 3.3.

## Métodos y funciones de ranura (*Slot*)

Las siguientes API son capaces de manejar objetos Unicode y cadenas de
caracteres en la entrada (nos referimos a ellos como cadenas de
caracteres en las descripciones) y retorna objetos Unicode o enteros
según corresponda.

Todos retornan "NULL" o "-1" si ocurre una excepción.

PyObject *PyUnicode_Concat(PyObject *left, PyObject *right)
    *Return value: New reference.** Part of the Stable ABI.*

   Une dos cadenas de caracteres que dan una nueva cadena de
   caracteres Unicode.

PyObject *PyUnicode_Split(PyObject *unicode, PyObject *sep, Py_ssize_t maxsplit)
    *Return value: New reference.** Part of the Stable ABI.*

   Divide una cadena de caracteres dando una lista de cadenas de
   caracteres Unicode. Si *sep* es "NULL", la división se realizará en
   todas las subcadenas de espacios en blanco. De lo contrario, las
   divisiones ocurren en el separador dado. A lo sumo se realizarán
   *maxsplit* divisiones. Si es negativo, no se establece ningún
   límite. Los separadores no están incluidos en la lista resultante.

   On error, return "NULL" with an exception set.

   Equivalent to "str.split()".

PyObject *PyUnicode_RSplit(PyObject *unicode, PyObject *sep, Py_ssize_t maxsplit)
    *Return value: New reference.** Part of the Stable ABI.*

   Similar to "PyUnicode_Split()", but splitting will be done
   beginning at the end of the string.

   On error, return "NULL" with an exception set.

   Equivalent to "str.rsplit()".

PyObject *PyUnicode_Splitlines(PyObject *unicode, int keepends)
    *Return value: New reference.** Part of the Stable ABI.*

   Divide una cadena de caracteres Unicode en los saltos de línea,
   retornando una lista de cadenas de caracteres Unicode. CRLF se
   considera un salto de línea. Si *keepends* es "0", los caracteres
   de salto de línea no se incluyen en las cadenas de caracteres
   resultantes.

PyObject *PyUnicode_Partition(PyObject *unicode, PyObject *sep)
    *Return value: New reference.** Part of the Stable ABI.*

   Split a Unicode string at the first occurrence of *sep*, and return
   a 3-tuple containing the part before the separator, the separator
   itself, and the part after the separator. If the separator is not
   found, return a 3-tuple containing the string itself, followed by
   two empty strings.

   *sep* must not be empty.

   On error, return "NULL" with an exception set.

   Equivalent to "str.partition()".

PyObject *PyUnicode_RPartition(PyObject *unicode, PyObject *sep)
    *Return value: New reference.** Part of the Stable ABI.*

   Similar to "PyUnicode_Partition()", but split a Unicode string at
   the last occurrence of *sep*. If the separator is not found, return
   a 3-tuple containing two empty strings, followed by the string
   itself.

   *sep* must not be empty.

   On error, return "NULL" with an exception set.

   Equivalent to "str.rpartition()".

PyObject *PyUnicode_Join(PyObject *separator, PyObject *seq)
    *Return value: New reference.** Part of the Stable ABI.*

   Une una secuencia de cadenas de caracteres usando el *separator*
   dado y retorna la cadena de caracteres Unicode resultante.

Py_ssize_t PyUnicode_Tailmatch(PyObject *unicode, PyObject *substr, Py_ssize_t start, Py_ssize_t end, int direction)
    * Part of the Stable ABI.*

   Retorna "1" si *substr* coincide con "unicode[start:end]" en el
   final de cola dado (*direction* == "-1" significa hacer una
   coincidencia de prefijo, *direction* == "1" una coincidencia de
   sufijo), "0" de lo contrario. Retorna "-1" si ocurrió un error.

Py_ssize_t PyUnicode_Find(PyObject *unicode, PyObject *substr, Py_ssize_t start, Py_ssize_t end, int direction)
    * Part of the Stable ABI.*

   Retorna la primera posición de *substr* en "unicode[start:end]"
   usando la *direction* dada (*direction* == "1" significa hacer una
   búsqueda hacia adelante, *direction* == "-1" una búsqueda hacia
   atrás). El valor de retorno es el índice de la primera
   coincidencia; un valor de "-1" indica que no se encontró ninguna
   coincidencia, y "-2" indica que se produjo un error y se ha
   establecido una excepción.

Py_ssize_t PyUnicode_FindChar(PyObject *unicode, Py_UCS4 ch, Py_ssize_t start, Py_ssize_t end, int direction)
    * Part of the Stable ABI since version 3.7.*

   Retorna la primera posición del carácter *ch* en
   "unicode[start:end]" usando la *direction* dada (*direction* == "1"
   significa hacer una búsqueda hacia adelante, *direction* == "-1"
   una búsqueda hacia atrás). El valor de retorno es el índice de la
   primera coincidencia; un valor de "-1" indica que no se encontró
   ninguna coincidencia, y "-2" indica que se produjo un error y se ha
   establecido una excepción.

   Added in version 3.3.

   Distinto en la versión 3.7: *start* y *end* ahora están ajustados
   para comportarse como "unicode[start:end]".

Py_ssize_t PyUnicode_Count(PyObject *unicode, PyObject *substr, Py_ssize_t start, Py_ssize_t end)
    * Part of the Stable ABI.*

   Retorna el número de ocurrencias no superpuestas de *substr* en
   "unicode[start:end]". Retorna "-1" si ocurrió un error.

PyObject *PyUnicode_Replace(PyObject *unicode, PyObject *substr, PyObject *replstr, Py_ssize_t maxcount)
    *Return value: New reference.** Part of the Stable ABI.*

   Reemplaza como máximo *maxcount* ocurrencias de *substr* en
   *unicode* con *replstr* y retorna el objeto Unicode resultante.
   *maxcount* == "-1" significa reemplazar todas las ocurrencias.

int PyUnicode_Compare(PyObject *left, PyObject *right)
    * Part of the Stable ABI.*

   Compara dos cadenas de caracteres y retorna "-1", "0", "1" para
   menor que, igual y mayor que, respectivamente.

   Esta función retorna "-1" en caso de falla, por lo que se debe
   llamar a "PyErr_Occurred()" para verificar si hay errores.

   Ver también: The "PyUnicode_Equal()" function.

int PyUnicode_Equal(PyObject *a, PyObject *b)
    * Part of the Stable ABI since version 3.14.*

   Test if two strings are equal:

   * Return "1" if *a* is equal to *b*.

   * Return "0" if *a* is not equal to *b*.

   * Set a "TypeError" exception and return "-1" if *a* or *b* is not
     a "str" object.

   The function always succeeds if *a* and *b* are "str" objects.

   The function works for "str" subclasses, but does not honor custom
   "__eq__()" method.

   Ver también: The "PyUnicode_Compare()" function.

   Added in version 3.14.

int PyUnicode_EqualToUTF8AndSize(PyObject *unicode, const char *string, Py_ssize_t size)
    * Part of the Stable ABI since version 3.13.*

   Compara un objeto Unicode con un búfer de caracteres que se
   interpreta como codificado en UTF-8 o ASCII y retorna verdadero
   ("1") si son iguales, o falso ("0") en caso contrario. Si el objeto
   Unicode contiene puntos de código subrogados ("U+D800" - "U+DFFF")
   o la cadena C no es UTF-8 válida, se retorna falso ("0").

   Esta función no lanza excepciones.

   Added in version 3.13.

int PyUnicode_EqualToUTF8(PyObject *unicode, const char *string)
    * Part of the Stable ABI since version 3.13.*

   Similar a "PyUnicode_EqualToUTF8AndSize()", pero calcula la
   longitud de *string* usando "strlen()". Si el objeto Unicode
   contiene caracteres nulos, se retorna falso ("0").

   Added in version 3.13.

int PyUnicode_CompareWithASCIIString(PyObject *unicode, const char *string)
    * Part of the Stable ABI.*

   Compara un objeto Unicode, *unicode*, con *string* y retorna "-1",
   "0", "1" para menor que, igual y mayor que, respectivamente. Es
   mejor pasar solo cadenas de caracteres codificadas en ASCII, pero
   la función interpreta la cadena de entrada como ISO-8859-1 si
   contiene caracteres no ASCII.

   Esta función no lanza excepciones.

PyObject *PyUnicode_RichCompare(PyObject *left, PyObject *right, int op)
    *Return value: New reference.** Part of the Stable ABI.*

   Comparación enriquecida de dos cadenas de caracteres Unicode y
   retorna uno de los siguientes:

   * "NULL" en caso de que se produzca una excepción

   * "Py_True" o "Py_False" para comparaciones exitosas

   * "Py_NotImplemented" en caso que se desconozca la combinación de
     tipos

   Los posibles valores para *op* son "Py_GT", "Py_GE", "Py_EQ",
   "Py_NE", "Py_LT", y "Py_LE".

PyObject *PyUnicode_Format(PyObject *format, PyObject *args)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna un nuevo objeto de cadena de caracteres desde *format* y
   *args*; esto es análogo al "format % args".

int PyUnicode_Contains(PyObject *unicode, PyObject *substr)
    * Part of the Stable ABI.*

   Comprueba si *substr* está contenido en *unicode* y retorna
   verdadero o falso en consecuencia.

   *substr* tiene que convertirse a una cadena Unicode de un solo
   elemento. Se retorna "-1" si hubo un error.

void PyUnicode_InternInPlace(PyObject **p_unicode)
    * Part of the Stable ABI.*

   Interna el argumento *p_unicode en su lugar. El argumento debe ser
   la dirección de una variable de puntero que apunta a un objeto de
   cadena Unicode de Python. Si existe una cadena internada que es
   igual a *p_unicode, la establece en *p_unicode (liberando la
   referencia al objeto de cadena anterior y creando una nueva
   *referencia fuerte* al objeto de cadena internada), de lo
   contrario, deja *p_unicode tal cual y lo interna.

   (Aclaración: aunque se habla mucho de referencias, piense en esta
   función como de referencia neutral. Debe poseer el objeto que pasa;
   después de la llamada, ya no posee la referencia pasada, pero ahora
   posee el resultado).

   Esta función nunca lanza una excepción. En caso de error, deja su
   argumento inalterado sin internarlo.

   Las instancias de subclases de "str" pueden no ser internadas, es
   decir, PyUnicode_CheckExact(*p_unicode) debe ser verdadero. Si no
   lo es, entonces, como con cualquier otro error, el argumento se
   deja sin cambios.

   Tenga en cuenta que las cadenas internadas no son “inmortales”.
   Debe mantener una referencia al resultado para beneficiarse de la
   internación.

PyObject *PyUnicode_InternFromString(const char *str)
    *Return value: New reference.** Part of the Stable ABI.*

   Una combinación de "PyUnicode_FromString()" y
   "PyUnicode_InternInPlace()", destinada a cadenas asignadas
   estáticamente.

   Retorna una nueva referencia ("owned") a un nuevo objeto de cadena
   Unicode que ha sido internado, o a un objeto de cadena previamente
   internado con el mismo valor.

   Python puede conservar una referencia al resultado o hacerlo
   *immortal*, evitando que sea recolectado por el recolector de
   basura de forma inmediata. Para internar un número no acotado de
   cadenas diferentes, como las que provienen de la entrada del
   usuario, se recomienda llamar directamente a
   "PyUnicode_FromString()" y "PyUnicode_InternInPlace()".

unsigned int PyUnicode_CHECK_INTERNED(PyObject *str)

   Return a non-zero value if *str* is interned, zero if not. The
   *str* argument must be a string; this is not checked. This function
   always succeeds.

   **Detalles de implementación de CPython:** A non-zero return value
   may carry additional information about *how* the string is
   interned. The meaning of such non-zero values, as well as each
   specific string's intern-related details, may change between
   CPython versions.

## PyUnicodeWriter

The "PyUnicodeWriter" API can be used to create a Python "str" object.

Added in version 3.14.

type PyUnicodeWriter

   A Unicode writer instance.

   The instance must be destroyed by "PyUnicodeWriter_Finish()" on
   success, or "PyUnicodeWriter_Discard()" on error.

PyUnicodeWriter *PyUnicodeWriter_Create(Py_ssize_t length)

   Create a Unicode writer instance.

   *length* must be greater than or equal to "0".

   If *length* is greater than "0", preallocate an internal buffer of
   *length* characters.

   Set an exception and return "NULL" on error.

PyObject *PyUnicodeWriter_Finish(PyUnicodeWriter *writer)

   Return the final Python "str" object and destroy the writer
   instance.

   Set an exception and return "NULL" on error.

   The writer instance is invalid after this call.

void PyUnicodeWriter_Discard(PyUnicodeWriter *writer)

   Discard the internal Unicode buffer and destroy the writer
   instance.

   If *writer* is "NULL", no operation is performed.

   The writer instance is invalid after this call.

int PyUnicodeWriter_WriteChar(PyUnicodeWriter *writer, Py_UCS4 ch)

   Write the single Unicode character *ch* into *writer*.

   On success, return "0". On error, set an exception, leave the
   writer unchanged, and return "-1".

int PyUnicodeWriter_WriteUTF8(PyUnicodeWriter *writer, const char *str, Py_ssize_t size)

   Decode the string *str* from UTF-8 in strict mode and write the
   output into *writer*.

   *size* is the string length in bytes. If *size* is equal to "-1",
   call "strlen(str)" to get the string length.

   On success, return "0". On error, set an exception, leave the
   writer unchanged, and return "-1".

   See also "PyUnicodeWriter_DecodeUTF8Stateful()".

int PyUnicodeWriter_WriteASCII(PyUnicodeWriter *writer, const char *str, Py_ssize_t size)

   Write the ASCII string *str* into *writer*.

   *size* is the string length in bytes. If *size* is equal to "-1",
   call "strlen(str)" to get the string length.

   *str* must only contain ASCII characters. The behavior is undefined
   if *str* contains non-ASCII characters.

   On success, return "0". On error, set an exception, leave the
   writer unchanged, and return "-1".

int PyUnicodeWriter_WriteWideChar(PyUnicodeWriter *writer, const wchar_t *str, Py_ssize_t size)

   Write the wide string *str* into *writer*.

   *size* is a number of wide characters. If *size* is equal to "-1",
   call "wcslen(str)" to get the string length.

   On success, return "0". On error, set an exception, leave the
   writer unchanged, and return "-1".

int PyUnicodeWriter_WriteUCS4(PyUnicodeWriter *writer, Py_UCS4 *str, Py_ssize_t size)

   Writer the UCS4 string *str* into *writer*.

   *size* is a number of UCS4 characters.

   On success, return "0". On error, set an exception, leave the
   writer unchanged, and return "-1".

int PyUnicodeWriter_WriteStr(PyUnicodeWriter *writer, PyObject *obj)

   Call "PyObject_Str()" on *obj* and write the output into *writer*.

   On success, return "0". On error, set an exception, leave the
   writer unchanged, and return "-1".

   To write a "str" subclass which overrides the "__str__()" method,
   "PyUnicode_FromObject()" can be used to get the original string.

int PyUnicodeWriter_WriteRepr(PyUnicodeWriter *writer, PyObject *obj)

   Call "PyObject_Repr()" on *obj* and write the output into *writer*.

   If *obj* is "NULL", write the string ""<NULL>"" into *writer*.

   On success, return "0". On error, set an exception, leave the
   writer unchanged, and return "-1".

   Distinto en la versión 3.14.4: Added support for "NULL".

int PyUnicodeWriter_WriteSubstring(PyUnicodeWriter *writer, PyObject *str, Py_ssize_t start, Py_ssize_t end)

   Write the substring "str[start:end]" into *writer*.

   *str* must be Python "str" object. *start* must be greater than or
   equal to 0, and less than or equal to *end*. *end* must be less
   than or equal to *str* length.

   On success, return "0". On error, set an exception, leave the
   writer unchanged, and return "-1".

int PyUnicodeWriter_Format(PyUnicodeWriter *writer, const char *format, ...)

   Similar to "PyUnicode_FromFormat()", but write the output directly
   into *writer*.

   On success, return "0". On error, set an exception, leave the
   writer unchanged, and return "-1".

int PyUnicodeWriter_DecodeUTF8Stateful(PyUnicodeWriter *writer, const char *string, Py_ssize_t length, const char *errors, Py_ssize_t *consumed)

   Decode the string *str* from UTF-8 with *errors* error handler and
   write the output into *writer*.

   *size* is the string length in bytes. If *size* is equal to "-1",
   call "strlen(str)" to get the string length.

   *errors* is an error handler name, such as ""replace"". If *errors*
   is "NULL", use the strict error handler.

   If *consumed* is not "NULL", set **consumed* to the number of
   decoded bytes on success. If *consumed* is "NULL", treat trailing
   incomplete UTF-8 byte sequences as an error.

   On success, return "0". On error, set an exception, leave the
   writer unchanged, and return "-1".

   See also "PyUnicodeWriter_WriteUTF8()".

## Deprecated API

The following API is deprecated.

type Py_UNICODE

   This is a typedef of "wchar_t", which is a 16-bit type or 32-bit
   type depending on the platform. Please use "wchar_t" directly
   instead.

   Distinto en la versión 3.3: En versiones anteriores, este era un
   tipo de 16 bits o de 32 bits, dependiendo de si seleccionó una
   versión Unicode "estrecha" o "amplia" de Python en el momento de la
   compilación.

   Deprecated since version 3.13, will be removed in version 3.15.

int PyUnicode_READY(PyObject *unicode)

   Do nothing and return "0". This API is kept only for backward
   compatibility, but there are no plans to remove it.

   Added in version 3.3.

   Obsoleto desde la versión 3.10: This API does nothing since Python
   3.12. Previously, this needed to be called for each string created
   using the old API ("PyUnicode_FromUnicode()" or similar).

unsigned int PyUnicode_IS_READY(PyObject *unicode)

   Do nothing and return "1". This API is kept only for backward
   compatibility, but there are no plans to remove it.

   Added in version 3.3.

   Obsoleto desde la versión 3.14: This API does nothing since Python
   3.12. Previously, this could be called to check if
   "PyUnicode_READY()" is necessary.
