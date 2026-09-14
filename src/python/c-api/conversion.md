---
title: Conversión y formato de cadenas de caracteres
source_url: https://docs.python.org/es/3
source_path: c-api/conversion.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 190
---

# Conversión y formato de cadenas de caracteres

Funciones para conversión de números y salida de cadena de caracteres
formateadas.

int PyOS_snprintf(char *str, size_t size, const char *format, ...)
    * Part of the Stable ABI.*

   Salida de no más de *size* bytes a *str* según la cadena de
   caracteres de formato *format* y los argumentos adicionales.
   Consulte la página de manual de Unix *snprintf(3)*.

int PyOS_vsnprintf(char *str, size_t size, const char *format, va_list va)
    * Part of the Stable ABI.*

   Salida de no más de *size* bytes a *str* según la cadena de
   caracteres de formato *format* y la lista de argumentos variables
   *va*. Página de manual de Unix *vsnprintf(3)*.

"PyOS_snprintf()" y "PyOS_vsnprintf()" envuelven las funciones
estándar de la biblioteca C "snprintf()" y "vsnprintf()". Su propósito
es garantizar un comportamiento consistente en casos de esquina
(*corner cases*), que las funciones del Estándar C no hacen.

Las envolturas aseguran que "str[size-1]" sea siempre "'\0'" al
retornar. Nunca se escriben más de *size* bytes (incluido el "'\0'"
del final) en *str*. Ambas funciones requieren que "str != NULL",
"size > 0", "format != NULL" y "size < INT_MAX". Tenga en cuenta que
esto significa que no hay equivalente a la expresión "n =
snprintf(NULL, 0, ...)" de C99, la cual determinaría el tamaño del
búfer necesario.

El valor de retorno (*rv*) para estas funciones debe interpretarse de
la siguiente manera:

* Cuando "0 <= rv < size", la conversión de salida fue exitosa y los
  caracteres *rv* se escribieron en *str* (excluyendo el byte "'\0'"
  final en "str[rv]").

* Cuando "rv >= size", la conversión de salida se truncó y se habría
  necesitado un búfer con "rv + 1" bytes para tener éxito.
  "str[size-1]" es "'\0'" en este caso.

* When "rv < 0", the output conversion failed and "str[size-1]" is
  "'\0'" in this case too, but the rest of *str* is undefined. The
  exact cause of the error depends on the underlying platform.

Las siguientes funciones proporcionan cadenas de caracteres
independientes de la configuración regional para numerar las
conversiones.

unsigned long PyOS_strtoul(const char *str, char **ptr, int base)
    * Part of the Stable ABI.*

   Convierte la parte inicial de la cadena de caracteres en "str" a un
   valor unsigned long según la "base" dada, que debe estar entre "2"
   y "36" inclusive, o ser el valor especial "0".

   Se ignoran los espacios en blanco y las mayúsculas y minúsculas.
   Si "base" es cero se busca un prefijo "0b", "0o" o "0x" para
   indicar la base.  Si no están, por defecto es "10".  La base debe
   ser 0 o entre 2 y 36 (ambos inclusive).  Si "ptr" no es "NULL",
   contendrá un puntero al final del escaneo.

   Si el valor convertido queda fuera del rango del tipo de retorno
   correspondiente, se produce un error de rango ("errno" se establece
   en "ERANGE") y se devuelve "ULONG_MAX".  Si no se puede realizar la
   conversión, se devuelve "0".

   Vea también el manual Unix de *strtoul(3)*.

   Added in version 3.2.

long PyOS_strtol(const char *str, char **ptr, int base)
    * Part of the Stable ABI.*

   Convierte la parte inicial de la cadena de caracteres en "str" a un
   valor long según la "base" dada, que debe estar entre "2" y "36"
   inclusive, o ser el valor especial "0".

   Igual que "PyOS_strtoul()", pero devuelve un valor long en su lugar
   y "LONG_MAX" en desbordamientos.

   Vea también el manual Unix de *strtol(3)*.

   Added in version 3.2.

double PyOS_string_to_double(const char *s, char **endptr, PyObject *overflow_exception)
    * Part of the Stable ABI.*

   Convierte una cadena de caracteres "s" a un valor double, generando
   una excepción de Python en caso de fallo. El conjunto de cadenas de
   caracteres aceptadas corresponde al conjunto de cadenas aceptadas
   por el constructor de Python "float()", excepto que "s" no debe
   tener espacios en blanco iniciales o finales. La conversión es
   independiente de la configuración regional actual.

   Si "endptr" es "NULL", convierte toda la cadena de caracteres.
   Lanza "ValueError" y retorna "-1.0" si la cadena de caracteres no
   es una representación válida de un número de punto flotante.

   Si *endptr* no es "NULL", convierte la mayor cantidad posible de la
   cadena de caracteres y configura "*endptr" para que apunte al
   primer carácter no convertido. Si ningún segmento inicial de la
   cadena de caracteres es la representación válida de un número de
   punto flotante, configura "*endptr" para que apunte al comienzo de
   la cadena de caracteres, lanza ValueError y retorna "-1.0".

   If "s" represents a value that is too large to store in a float
   (for example, ""1e500"" is such a string on many platforms) then if
   "overflow_exception" is "NULL" return "Py_INFINITY" (with an
   appropriate sign) and don't set any exception.  Otherwise,
   "overflow_exception" must point to a Python exception object; raise
   that exception and return "-1.0".  In both cases, set "*endptr" to
   point to the first character after the converted value.

   Si se produce algún otro error durante la conversión (por ejemplo,
   un error de falta de memoria), establece la excepción Python
   adecuada y retorna "-1.0".

   Added in version 3.1.

char *PyOS_double_to_string(double val, char format_code, int precision, int flags, int *ptype)
    * Part of the Stable ABI.*

   Convierte un double *val*  a una cadena de caracteres usando
   *format_code*, *precision* y *flags* suministrados.

   *format_code*  debe ser uno de "'e'", "'E'", "'f'", "'F'", "'g'",
   "'G'" or "'r'".  Para "'r'", la *precision* suministrada debe ser 0
   y se ignora.  El código de formato "'r'" especifica el formato
   estándar "repr()".

   *flags* can be zero or more of the following values or-ed together:

   Py_DTSF_SIGN

      Always precede the returned string with a sign character, even
      if *val* is non-negative.

   Py_DTSF_ADD_DOT_0

      Ensure that the returned string will not look like an integer.

   Py_DTSF_ALT

      Apply "alternate" formatting rules. See the documentation for
      the "PyOS_snprintf()" "'#'" specifier for details.

   Py_DTSF_NO_NEG_0

      Negative zero is converted to positive zero.

      Added in version 3.11.

   If *ptype* is non-"NULL", then the value it points to will be set
   to one of the following constants depending on the type of *val*:

   +----------------------------------------------------+----------------------------------------------------+
   | **ptype*                                           | type of *val*                                      |
   |====================================================|====================================================|
   | Py_DTST_FINITE                                     | finite number                                      |
   +----------------------------------------------------+----------------------------------------------------+
   | Py_DTST_INFINITE                                   | infinite number                                    |
   +----------------------------------------------------+----------------------------------------------------+
   | Py_DTST_NAN                                        | not a number                                       |
   +----------------------------------------------------+----------------------------------------------------+

   El valor de retorno es un puntero a *buffer* con la cadena de
   caracteres convertida o "NULL" si la conversión falla. La persona
   que llama es responsable de liberar la cadena de caracteres
   retornada llamando a "PyMem_Free()".

   Added in version 3.1.

int PyOS_mystricmp(const char *str1, const char *str2)
int PyOS_mystrnicmp(const char *str1, const char *str2, Py_ssize_t size)
    * Part of the Stable ABI.*

   Case insensitive comparison of strings. These functions work almost
   identically to "strcmp()" and "strncmp()" (respectively), except
   that they ignore the case of ASCII characters.

   Return "0" if the strings are equal, a negative value if *str1*
   sorts lexicographically before *str2*, or a positive value if it
   sorts after.

   In the *str1* or *str2* arguments, a NUL byte marks the end of the
   string. For "PyOS_mystrnicmp()", the *size* argument gives the
   maximum size of the string, as if NUL was present at the index
   given by *size*.

   These functions do not use the locale.

int PyOS_stricmp(const char *str1, const char *str2)
int PyOS_strnicmp(const char *str1, const char *str2, Py_ssize_t size)

   Case insensitive comparison of strings.

   On Windows, these are aliases of "stricmp()" and "strnicmp()",
   respectively.

   On other platforms, they are aliases of "PyOS_mystricmp()" and
   "PyOS_mystrnicmp()", respectively.

# Character classification and conversion

The following macros provide locale-independent (unlike the C standard
library "ctype.h") character classification and conversion. The
argument must be a signed or unsigned char.

Py_ISALNUM(c)

   Return true if the character *c* is an alphanumeric character.

Py_ISALPHA(c)

   Return true if the character *c* is an alphabetic character ("a-z"
   and "A-Z").

Py_ISDIGIT(c)

   Return true if the character *c* is a decimal digit ("0-9").

Py_ISLOWER(c)

   Return true if the character *c* is a lowercase ASCII letter
   ("a-z").

Py_ISUPPER(c)

   Return true if the character *c* is an uppercase ASCII letter
   ("A-Z").

Py_ISSPACE(c)

   Return true if the character *c* is a whitespace character (space,
   tab, carriage return, newline, vertical tab, or form feed).

Py_ISXDIGIT(c)

   Return true if the character *c* is a hexadecimal digit ("0-9",
   "a-f", and "A-F").

Py_TOLOWER(c)

   Return the lowercase equivalent of the character *c*.

Py_TOUPPER(c)

   Return the uppercase equivalent of the character *c*.
