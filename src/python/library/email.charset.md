---
title: '"email.charset": Representing character sets'
source_url: https://docs.python.org/es/3
source_path: library/email.charset.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2380
---

# "email.charset": Representing character sets

**Código fuente:** Lib/email/charset.py

======================================================================

Este módulo es parte de la API de email heredada ("Compat32"). En la
nueva API solo se usa la tabla de alias.

El texto restante de esta sección corresponde a la documentación
original del módulo.

Este módulo proporciona una clase "Charset" para representar conjuntos
de caracteres y conversiones de conjuntos de caracteres en mensajes de
correo electrónico, así como un registro de conjuntos de caracteres y
varios métodos de conveniencia para manipular este registro. Las
instancias de "Charset" se utilizan en varios otros módulos dentro del
paquete "email".

Import this class from the "email.charset" module.

class email.charset.Charset(input_charset=DEFAULT_CHARSET)

   Asigna conjuntos de caracteres a sus propiedades de correo
   electrónico.

   Esta clase proporciona información sobre los requisitos impuestos
   al correo electrónico para un conjunto de caracteres específico.
   También proporciona rutinas de conveniencia para convertir entre
   juegos de caracteres, dada la disponibilidad de los códecs
   aplicables. Dado un conjunto de caracteres, hará todo lo posible
   para proporcionar información sobre cómo utilizar ese conjunto de
   caracteres en un mensaje de correo electrónico de forma compatible
   con RFC.

   Ciertos conjuntos de caracteres deben codificarse con quoted-
   printable o base64 cuando se usan en encabezados o cuerpos de
   correo electrónico. Ciertos conjuntos de caracteres deben
   convertirse directamente y no están permitidos en el correo
   electrónico.

   Opcional *input_charset* es como se describe a continuación;
   siempre se convierte a minúsculas.  Después de que el alias sea
   normalizado también se utiliza como una búsqueda en el registro de
   conjuntos de caracteres para averiguar la codificación del
   encabezado, codificación de cuerpo, y códec de conversión de salida
   que se usarán para el conjunto de caracteres.  Por ejemplo, si
   *input_charset* es "iso-8859-1", los encabezados y cuerpos se
   codificarán mediante quoted-printable y no es necesario ningún
   códec de conversión de salida.  Si *input_charset* es "euc-jp", los
   encabezados se codificarán con base64, los cuerpos no se
   codificarán, pero el texto de salida se convertirá del conjunto de
   caracteres "euc-jp" al conjunto de caracteres "iso-2022-jp".

   Las instancias "Charset" tienen los siguientes atributos de datos:

   input_charset

      El conjunto de caracteres inicial especificado. Los alias
      comunes se convierten a sus nombres de correo electrónico
      *Official* (por ejemplo, "latin_1" se convierte a "iso-8859-1").
      El valor predeterminado es "us-ascii" de 7 bits.

   header_encoding

      Si el conjunto de caracteres debe codificarse antes de que pueda
      usarse en un encabezado de correo electrónico, este atributo se
      establecerá a "charset.QP" (para imprimible con comillas),
      "charset.BASE64" (para codificación base64), o
      "charset.SHORTEST" para la codificación más corta QP o BASE64.
      De lo contrario será "None".

   body_encoding

      Igual que *header_encoding*, pero describe la codificación del
      cuerpo del mensaje de correo, que de hecho puede ser diferente a
      la codificación del encabezado. "charset.SHORTEST" no está
      permitido para *body_encoding*.

   output_charset

      Algunos conjuntos de caracteres deben ser convertidos antes de
      poder ser usados en cabeceras o cuerpos de correos. Si el
      *input_charset* es uno de ellos, este atributo contendrá el
      nombre del conjunto de caracteres al que será convertido. De lo
      contrario, será "None".

   input_codec

      El nombre del códec de Python usado para convertir el
      *input_charset* a Unicode. Si no es necesario un códec de
      conversión, este atributo será "None".

   output_codec

      El nombre del códec de Python usado para convertir Unicode a
      *output_charset*. Si no es necesario un códec de conversión,
      este atributo tendrá el mismo valor que *input_codec*.

   Las instancias "Charset" además tienen los siguientes métodos:

   get_body_encoding()

      Retorna la codificación de transferencia de contenido usada para
      la codificación del cuerpo.

      Esta es la cadena de caracteres "quoted-printable" o "base64"
      dependiendo de la codificación usada, o es una función, en cuyo
      caso se deberá llamar a la función con un solo argumento, el
      objeto Mensaje a ser codificado. La función deberá luego
      establecer el encabezado *Content-Transfer-Encoding*  en lo que
      sea apropiado.

      Retorna la cadena "quoted-printable" si *body_encoding* es "QP",
      retorna la cadena "base64" si *body_encoding* es "BASE64", y
      retorna la cadena "7bit" en caso contrario.

   get_output_charset()

      Return the output character set.

      Este es el atributo *output_charset* si no es "None", en caso
      contrario es *input_charset*.

   header_encode(string)

      Codifica como encabezado la cadena de caracteres *string*.

      El tipo de codificación (base64 o quoted-printable) se basará en
      el atributo *header_encoding*.

   header_encode_lines(string, maxlengths)

      Codifica como encabezado *string* convirtiéndolo primero a
      bytes.

      Es similar a  "header_encode()" excepto que la cadena se ajusta
      a las longitudes máximas indicadas en el argumento *maxlengths*,
      el cual debe ser un iterador: cada elemento retornado por este
      iterador proporcionará la siguiente longitud máxima de línea.

   body_encode(string)

      Codifica como cuerpo la cadena *string*.

      El tipo de codificación  (base64 o quoted-printable) se basará
      en el atributo *body_encoding*.

   La clase "Charset" también proporciona una serie de métodos para
   soportar operaciones estándar y funciones integradas.

   __str__()

      Retorna *input_charset* como una cadena de caracteres convertida
      a minúsculas. "__repr__()" es un alias para "__str__()".

   __eq__(other)

      Este método le permite comparar dos instancias "Charset" por
      igualdad.

   __ne__(other)

      Este método le permite comparar dos instancias "Charset" por
      desigualdad.

The "email.charset" module also provides the following functions for
adding new entries to the global character set, alias, and codec
registries:

email.charset.add_charset(charset, header_enc=None, body_enc=None, output_charset=None)

   Añade propiedades de carácter al registro global.

   *charset* es el conjunto de caracteres de entrada, y debe ser el
   nombre canónico del conjunto de caracteres.

   Opcional *header_enc* y *body_enc* es "charset.QP" para imprimibles
   entre comillas, "charset.BASE64" para codificación base64,
   "charset.SHORTEST" para la codificación más corta entre imprimible
   entre comillas o base64, o "None" para no codificar. "SHORTEST"
   solo es válido para *header_enc*. El valor predeterminado es "None"
   para no codificar.

   Opcional *output_charset* es es el conjunto de caracteres en el que
   debe estar la salida. Las conversiones proceden del conjunto de
   caracteres de entrada, a Unicode, al conjunto de caracteres de
   salida cuando se llama al método "Charset.convert()". El valor
   predeterminado es la salida en el mismo conjunto de caracteres que
   la entrada.

   Tanto *input_charset* y *output_charset* deben tener entradas de
   códec Unicode en el conjunto de caracteres del módulo para la
   asignación del códec; use "add_codec()" para agregar códecs que el
   módulo no conozca. Consulte la documentación del módulo "codecs"
   para más información.

   El registro global de conjuntos de caracteres se mantiene en el
   módulo global diccionario "CHARSETS".

email.charset.add_alias(alias, canonical)

   Añade un alias al conjunto de caracteres. *alias* es el nombre del
   alias, p. ej. "latin-1". *canonical* es el nombre canónico del
   conjunto de caracteres, p. ej. "iso-8859-1".

   El registro de alias global de conjuntos de caracteres se mantiene
   en el módulo global diccionario "ALIASES".

email.charset.add_codec(charset, codecname)

   Añade un códec que asigna caracteres en el conjunto de caracteres
   dado hacia y desde Unicode.

   *charset* es el nombre canónico de un conjunto de caracteres.
   *codename* es el nombre de un códec de Python, según corresponda
   para el segundo argumento del método "str" de  "encode()".
