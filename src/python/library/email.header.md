---
title: '"email.header": Internationalized headers'
source_url: https://docs.python.org/es/3
source_path: library/email.header.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2450
---

# "email.header": Internationalized headers

**Código fuente:** Lib/email/header.py

======================================================================

Este módulo es parte de la API de email heredada ("Compat32"). En la
API actual, la codificación y decodificación de las cabeceras se
gestiona de forma transparente por la API de tipo diccionario de la
clase "EmailMessage". Además de los usos del código heredado, este
módulo puede ser útil en aplicaciones que necesiten controlar
completamente el conjunto de caracteres usado cuando se codifican las
cabeceras.

El resto del texto de esta sección es la documentación original del
módulo.

**RFC 2822** es el estándar base que describe el formato de los
mensajes de correo electrónico. Deriva del estándar anterior **RFC
822**, cuyo uso se generalizó durante una época en la que la mayoría
del correo electrónico se componía únicamente de caracteres ASCII.
**RFC 2822** es una especificación que se escribió asumiendo que el
correo electrónico contiene solo caracteres ASCII 7-bit.

Of course, as email has been deployed worldwide, it has become
internationalized, such that language specific character sets can now
be used in email messages.  The base standard still requires email
messages to be transferred using only 7-bit ASCII characters, so a
slew of RFCs have been written describing how to encode email
containing non-ASCII characters into **RFC 2822**-compliant format.
These RFCs include **RFC 2045**, **RFC 2046**, **RFC 2047**, and **RFC
2231**. The "email" package supports these standards in its
"email.header" and "email.charset" modules.

If you want to include non-ASCII characters in your email headers, say
in the *Subject* or *To* fields, you should use the "Header" class and
assign the field in the "Message" object to an instance of "Header"
instead of using a string for the header value.  Import the "Header"
class from the "email.header" module. For example:

   >>> from email.message import Message
   >>> from email.header import Header
   >>> msg = Message()
   >>> h = Header('p\xf6stal', 'iso-8859-1')
   >>> msg['Subject'] = h
   >>> msg.as_string()
   'Subject: =?iso-8859-1?q?p=F6stal?=\n\n'

¿Has visto cómo hemos hecho que el campo *Subject* contuviera un
caracter no ASCII? Lo hemos hecho creando una instancia de "Header" y
pasándole el conjunto de caracteres en los que estaba codificado la
cadena de bytes. Cuando la instancia de "Message" subsecuente se ha
aplanado, el campo *Subject* se ha codificado en **RFC 2047**
adecuadamente. Los lectores de correo que soportan MIME deberían
mostrar esta cabecera usando el caracter ISO-8859-1 incrustado.

Aquí está la descripción de la clase "Header":

class email.header.Header(s=None, charset=None, maxlinelen=None, header_name=None, continuation_ws=' ', errors='strict')

   Crea una cabecera conforme a las especificaciones MIME que contiene
   cadenas de caracteres en diferentes conjuntos de caracteres.

   El argumento opcional *s* es el valor inicial de la cabecera. Si es
   "None" (el valor por defecto), el valor inicial de la cabecera
   quedará sin asignar. Puedes añadirlo luego a la cabecera con
   llamadas al método "append()". *s* debe ser una instancia de
   "bytes" o "str", pero lee la documentación de "append()" para
   conocer los detalles semánticos.

   El argumento opcional *charset* sirve para dos propósitos: tiene el
   mismo significado que el argumento *charset* en el método
   "append()". También asigna el conjunto de caracteres por defecto
   para todas las llamadas subsecuentes a "append()" que omitan el
   argumento *charset*. Si no se proporciona *charset* en el
   constructor (por defecto), el conjunto de caracteres "us-ascii" se
   usa tanto para el conjunto de caracteres inicial de *s* como por
   defecto para las llamadas subsecuentes a "append()".

   The maximum line length can be specified explicitly via
   *maxlinelen*.  For splitting the first line to a shorter value (to
   account for the field header which isn't included in *s*, e.g.
   *Subject*) pass in the name of the field in *header_name*.  The
   default *maxlinelen* is 78, and the default value for *header_name*
   is "None", meaning it is not taken into account for the first line
   of a long, split header.

   El argumento opcional *continuation_ws* debe ser conforme a las
   normas de espacios en blanco plegables de la **RFC 2822**, y
   normalmente es o un espacio o un caracter tabulador. Este caracter
   se antepondrá delante de las líneas continuadas. El valor por
   defecto de *continuation_ws* es un solo espacio.

   El argumento opcional *errors* se pasa directamente a través del
   método "append()".

   append(s, charset=None, errors='strict')

      Añade la cadena de caracteres *s* a la cabecera MIME.

      El argumento opcional *charset*, si se proporciona, debe ser una
      instancia de "Charset" (ver "email.charset") o el nombre de un
      conjunto de datos, que deberá ser convertido a una instancia de
      "Charset". Un valor de "None" (el valor por defecto) significa
      que se usará el *charset* dado en el constructor.

      *s* puede ser una instancia de "bytes" o de "str". Si es una
      instancia de "bytes", entonces *charset* es la codificación de
      esa cadena de bytes, y se lanzará un "UnicodeError" si la cadena
      de caracteres no puede decodificarse con ese conjunto de
      caracteres.

      Si *s* es una instancia de "str", entonces *charset* es una
      sugerencia que especifica el conjunto de caracteres usando en la
      cadena de caracteres.

      En cualquier caso, cuando se produce una cabecera conforme a la
      **RFC 2822** usando las reglas de la **RFC 2047**, la cadena de
      caracteres se codificará usando el códec de salida del conjunto
      de caracteres. Si la cadena de caracteres no puede codificarse
      usando el códec de salida, se lanzará un UnicodeError.

      El argumento opcional *errors* se pasa como el argumento de
      errores para la llamada de decodificación si *s* es una cadena
      de bits.

   encode(splitchars=';, \t', maxlinelen=None, linesep='\n')

      Codifica un mensaje de la cabecera en un formato conforme a RFC,
      posiblemente envolviendo las líneas largas y encapsulando las
      partes no ASCII en base64 o en codificaciones imprimibles
      entrecomilladas.

      El argumento opcional *splitchars* es una cadena de caracteres
      que contiene caracteres a los que el algoritmo de separación
      debería asignar espacio extra durante la encapsulación de la
      cabecera normal. Esto da un basto soporte a los saltos
      sintácticos de alto nivel de la **RFC 2822**: los puntos de
      separación precedidos por un caracter separador tienen
      preferencia durante la separación de la línea, con preferencia
      de caracteres en el orden en el que aparecen en la cadena de
      caracteres. El espacio y el tabulador pueden incluirse en la
      cadena de caracteres para indicar si se debería dar preferencia
      a uno sobre el otro como punto de separación cuando no aparezcan
      otros caracteres separadores en la línea que se está dividiendo.
      Los caracteres separadores no afectan a las líneas codificadas
      de la **RFC 2047**.

      *maxlinelen*, si se proporciona, sobrescribe el valor de
      longitud de línea máxima para la instancia.

      *linesep* especifica los caracteres usados para separar las
      líneas de la cabecera plegada. Su valor por defecto es el valor
      más útil para el código de una aplicación Python ("\n"), pero se
      puede especificar "\r\n" para producir cabeceras con separadores
      de línea conforme a RFCs.

      Distinto en la versión 3.2: Argumento *linesep* añadido.

   La clase "Header" también proporciona una serie de métodos para
   soportar operaciones estándar y funciones incorporadas.

   __str__()

      Retorna una aproximación de "Header" como una cadena de
      caracteres, usando una longitud de línea ilimitada. Todas las
      piezas se convierten a unicode utilizando la codificación
      especificada y unidas adecuadamente. Todas las piezas con un
      conjunto de caracteres "'unknown-8bit'" se decodifican como
      ASCII usando el gestor de errores de "'replace'".

      Distinto en la versión 3.2: Añadida gestión del conjunto de
      caracteres "'unknown-8bit'".

   __eq__(other)

      Este método permite comparar si dos instancias de "Header" son
      iguales.

   __ne__(other)

      Este método permite comparar si dos instancias de "Header" no
      son iguales.

The "email.header" module also provides the following convenient
functions.

email.header.decode_header(header)

   Decodifica el valor de un mensaje de la cabecera sin convertir el
   conjunto de caracteres. El valor de la cabecera está en *header*.

   For historical reasons, this function may return either:

   1. A list of pairs containing each of the decoded parts of the
      header, "(decoded_bytes, charset)", where *decoded_bytes* is
      always an instance of "bytes", and *charset* is either:

         * A lower case string containing the name of the character
           set specified.

         * "None" for non-encoded parts of the header.

   2. A list of length 1 containing a pair "(string, None)", where
      *string* is always an instance of "str".

   An "email.errors.HeaderParseError" may be raised when certain
   decoding errors occur (e.g. a base64 decoding exception).

   Here are examples:

   >>> from email.header import decode_header
   >>> decode_header('=?iso-8859-1?q?p=F6stal?=')
   [(b'p\xf6stal', 'iso-8859-1')]
   >>> decode_header('unencoded_string')
   [('unencoded_string', None)]
   >>> decode_header('bar =?utf-8?B?ZsOzbw==?=')
   [(b'bar ', None), (b'f\xc3\xb3o', 'utf-8')]

   Nota:

     This function exists for backwards compatibility only. For new
     code, we recommend using "email.headerregistry.HeaderRegistry".

email.header.make_header(decoded_seq, maxlinelen=None, header_name=None, continuation_ws=' ')

   Crea una instancia de "Header" a partir de una secuencia de duplas
   como las retornadas por "decode_header()".

   "decode_header()" toma el valor de una cadena de caracteres de la
   cabecera y retorna una secuencia de duplas con el formato
   "(decoded_string, charset)", donde *charset* es el nombre del
   conjunto de caracteres.

   Esta función toma una de esas secuencias de duplas y retorna una
   instancia de "Header". Los argumentos opcionales *maxlinelen*,
   *header_name* y *continuation_ws* son como los del constructor
   "Header".

   Nota:

     This function exists for backwards compatibility only, and is not
     recommended for use in new code.
