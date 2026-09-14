---
title: '"base64" --- Base16, Base32, Base64, Base85 Data Encodings'
source_url: https://docs.python.org/es/3
source_path: library/base64.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1820
---

# "base64" --- Base16, Base32, Base64, Base85 Data Encodings

**Código fuente:** Lib/base64.py

======================================================================

This module provides functions for encoding binary data to printable
ASCII characters and decoding such encodings back to binary data. This
includes the encodings specified in **RFC 4648** (Base64, Base32 and
Base16), the Base85 encoding specified in PDF 2.0, and non-standard
variants of Base85 used elsewhere.

Hay dos interfaces proporcionadas por este módulo. La interfaz moderna
admite la codificación de *objetos similares a bytes* a ASCII "bytes"
y la decodificación de *objetos similares a bytes* o cadenas que
contienen ASCII a "bytes". Se admiten los dos alfabetos base 64
definidos en **RFC 4648** (normal y seguro para URL y sistema de
archivos).

The legacy interface does not support decoding from strings, but it
does provide functions for encoding and decoding to and from *file
objects*.  It only supports the Base64 standard alphabet, and it adds
newlines every 76 characters as per **RFC 2045**.  Note that if you
are looking for **RFC 2045** support you probably want to be looking
at the "email" package instead.

Distinto en la versión 3.3: Las cadenas de caracteres Unicode de solo
ASCII ahora son aceptadas por las funciones de decodificación de la
interfaz moderna.

Distinto en la versión 3.4: Cualquier *objeto similar a bytes* ahora
son aceptados por todas las funciones de codificación y decodificación
en este módulo. Ascii85/Base85 soporte agregado.

## RFC 4648 Encodings

The **RFC 4648** encodings are suitable for encoding binary data so
that it can be safely sent by email, used as parts of URLs, or
included as part of an HTTP POST request.

base64.b64encode(s, altchars=None)

   Codifica el *objeto similar a bytes* *s* utilizando Base64 y
   retorna los "bytes" codificados.

   Optional *altchars* must be a *bytes-like object* of length 2 which
   specifies an alternative alphabet for the "+" and "/" characters.
   This allows an application to e.g. generate URL or filesystem safe
   Base64 strings.  The default is "None", for which the standard
   Base64 alphabet is used.

   May assert or raise a "ValueError" if the length of *altchars* is
   not 2.  Raises a "TypeError" if *altchars* is not a *bytes-like
   object*.

base64.b64decode(s, altchars=None, validate=False)

   Decodifica el *objeto similar a bytes* codificado en Base64 o
   cadena de caracteres ASCII *s* y retorna los "bytes" decodificados.

   Optional *altchars* must be a *bytes-like object* or ASCII string
   of length 2 which specifies the alternative alphabet used instead
   of the "+" and "/" characters.

   Una excepción "binascii.Error" se lanza si *s* está incorrectamente
   rellenado (*padded*).

   Si *validate* es "False" (el valor predeterminado), los caracteres
   que no están en el alfabeto normal de base 64 ni en el alfabeto
   alternativo se descartan antes de la verificación del relleno. Si
   *validate* es "True", estos caracteres no alfabéticos en la entrada
   dan como resultado "binascii.Error".

   Para más información sobre la verificación estricta de base64,
   véase "binascii.a2b_base64()"

   May assert or raise a "ValueError" if the length of *altchars* is
   not 2.

base64.standard_b64encode(s)

   Codifica el *objeto similar a bytes* *s* usando el alfabeto
   estándar Base64 y retorna los "bytes" codificados.

base64.standard_b64decode(s)

   Decodifica un *bytes-like object* o cadena de caracteres ASCII *s*
   utilizando el alfabeto estándar Base64 y retorna los "bytes"
   decodificados.

base64.urlsafe_b64encode(s)

   Codifica el *objeto similar a bytes* *s* usando el alfabeto seguro
   para URL y sistemas de archivos, que sustituye a "-" en lugar de
   "+" y "_" en lugar de "/" en el alfabeto estándar de Base64, y
   retorna los "bytes" codificados. El resultado aún puede contener
   "=".

base64.urlsafe_b64decode(s)

   Decodifica *objeto similar a bytes* o cadena de caracteres ASCII
   *s* utilizando el alfabeto seguro para URL y sistema de archivos,
   que sustituye "-" en lugar de "+" y "_" en lugar de "/" en el
   alfabeto estándar de Base64, y retorna los "bytes" decodificados.

base64.b32encode(s)

   Codifica el *objeto similar a bytes* *s* utilizando Base32 y
   retorna los "bytes" codificados.

base64.b32decode(s, casefold=False, map01=None)

   Decodifica el *objeto similar a bytes* codificado en Base32 o
   cadena de caracteres ASCII *s* y retorna los "bytes" decodificados.

   El opcional *casefold* es un flag que especifica si un alfabeto en
   minúscula es aceptable como entrada. Por motivos de seguridad, el
   valor predeterminado es "Falso".

   **RFC 4648** permite la asignación opcional del dígito 0 (cero) a
   la letra O (oh), y la asignación opcional del dígito 1 (uno) a la
   letra I (ojo) o la letra L (el) . El argumento opcional *map01*
   cuando no es "None", especifica la letra a la cual el dígito 1
   debería mapearse(cuando *map01* no es "None", el dígito 0 siempre
   se asigna a la letra O). Por motivos de seguridad, el valor
   predeterminado es "None", por lo que 0 y 1 no están permitidos en
   la entrada.

   Una "binascii.Error" se lanza si *s* está incorrectamente rellenado
   (*padded*) o si hay caracteres no alfabéticos presentes en la
   entrada.

base64.b32hexencode(s)

   Similar a "b32encode()" pero usa el Alfabeto Hexagonal Extendido,
   como se define en **RFC 4648**.

   Added in version 3.10.

base64.b32hexdecode(s, casefold=False)

   Similar a "b32decode()" pero usa el Alfabeto Hexagonal Extendido,
   como se define en **RFC 4648**.

   Esta versión no permite el dígito 0 (cero) a la letra O (oh) y el
   dígito 1 (uno) a las asignaciones de la letra I (ojo) o la letra L
   (el), todos estos caracteres están incluidos en el Alfabeto
   Hexagonal Extendido y no son intercambiables.

   Added in version 3.10.

base64.b16encode(s)

   Codifica el *objeto similar a bytes* *s* utilizando Base16 y
   retorna los "bytes" codificados.

base64.b16decode(s, casefold=False)

   Decodifica el *objeto similar a bytes* codificado en Base16 o
   cadena de caracteres ASCII *s* y retorna los "bytes" decodificados.

   El opcional *casefold* es un flag que especifica si un alfabeto en
   minúscula es aceptable como entrada. Por motivos de seguridad, el
   valor predeterminado es "Falso".

   Una "binascii.Error" se lanza si *s* está incorrectamente rellenado
   (*padded*) o si hay caracteres no alfabéticos presentes en la
   entrada.

## Base85 Encodings

Base85 encoding is a family of algorithms which represent four bytes
using five ASCII characters.  Originally implemented in the Unix
"btoa(1)" utility, a version of it was later adopted by Adobe in the
PostScript language and is standardized in PDF 2.0 (ISO 32000-2). This
version, in both its "btoa" and PDF variants, is implemented by
"a85encode()".

A separate version, using a different output character set, was
defined as an April Fool's joke in **RFC 1924** but is now used by Git
and other software.  This version is implemented by "b85encode()".

Finally, a third version, using yet another output character set
designed for safe inclusion in programming language strings, is
defined by ZeroMQ and implemented here by "z85encode()".

The functions present in this module differ in how they handle the
following:

* Whether to include and expect enclosing "<~" and "~>" markers.

* Whether to fold the input into multiple lines.

* The set of ASCII characters used for encoding.

* Compact encodings of sequences of spaces and null bytes.

* The encoding of zero-padding bytes applied to the input.

Refer to the documentation of the individual functions for more
information.

base64.a85encode(b, *, foldspaces=False, wrapcol=0, pad=False, adobe=False)

   Codifica el *objeto similar a bytes* *b* utilizando Ascii85 y
   retorna los "bytes" codificados.

   *foldspaces* is an optional flag that uses the special short
   sequence 'y' instead of 4 consecutive spaces (ASCII 0x20) as
   supported by 'btoa'. This feature is not supported by the standard
   encoding used in PDF.

   *wrapcol* controls whether the output should have newline ("b'\n'")
   characters added to it. If this is non-zero, each output line will
   be at most this many characters long, excluding the trailing
   newline.

   *pad* controls whether zero-padding applied to the end of the input
   is fully retained in the output encoding, as done by "btoa",
   producing an exact multiple of 5 bytes of output. This is not part
   of the standard encoding used in PDF, as it does not preserve the
   length of the data.

   *adobe* controls whether the encoded byte sequence is framed with
   "<~" and "~>", as in a PostScript base-85 string literal.  Note
   that while ASCII85Decode streams in PDF documents *must* be
   terminated with "~>", they *must not* use a leading "<~".

   Added in version 3.4.

base64.a85decode(b, *, foldspaces=False, adobe=False, ignorechars=b' \t\n\r\x0b')

   Decodifica el *objeto similar a bytes* codificado en Ascii85 o
   cadena de caracteres ASCII *b* y retorna los "bytes" decodificados.

   *foldspaces* is a flag that specifies whether the 'y' short
   sequence should be accepted as shorthand for 4 consecutive spaces
   (ASCII 0x20). This feature is not supported by the standard Ascii85
   encoding used in PDF and PostScript.

   *adobe* controls whether the "<~" and "~>" markers are present.
   While the leading "<~" is not required, the input must end with
   "~>", or a "ValueError" is raised.

   *ignorechars* should be a byte string containing characters to
   ignore from the input. This should only contain whitespace
   characters, and by default contains all whitespace characters in
   ASCII.

   Added in version 3.4.

base64.b85encode(b, pad=False)

   Codifica el *objeto similar a bytes* *b* utilizando base85 (como se
   usa en por ejemplo, diferencias binarias de estilo git) y retorna
   los "bytes" codificados.

   The input is padded with "b'\0'" so its length is a multiple of 4
   bytes before encoding.  If *pad* is true, all the resulting
   characters are retained in the output, which will always be a
   multiple of 5 bytes, and thus the length of the data may not be
   preserved on decoding.

   Added in version 3.4.

base64.b85decode(b)

   Decode the base85-encoded *bytes-like object* or ASCII string *b*
   and return the decoded "bytes".

   Added in version 3.4.

base64.z85encode(s)

   Encode the *bytes-like object* *s* using Z85 (as used in ZeroMQ)
   and return the encoded "bytes".

   The ZeroMQ specification requires the length of Z85-encoded data to
   be a multiple of 5 bytes. To produce compliant data frames, you
   must pad the input data to this function to a multiple of 4 bytes.

   Added in version 3.13.

base64.z85decode(s)

   Decode the Z85-encoded *bytes-like object* or ASCII string *s* and
   return the decoded "bytes".

   Added in version 3.13.

## Legacy Interface

base64.decode(input, output)

   Decodifica el contenido del archivo binario *input* y escribe los
   datos binarios resultantes en el archivo *output*. *input* y
   *output* deben ser *objetos archivo*. *input* se leerá hasta que
   "input.readline()" retorne un objeto de bytes vacío.

base64.decodebytes(s)

   Decodifica el *objeto similar a bytes* *s*, que debe contener una o
   más líneas de datos codificados en base64, y retornará los "bytes"
   decodificados.

   Added in version 3.1.

base64.encode(input, output)

   Codifica el contenido del archivo binario *input* y escribe los
   datos codificados en base64 resultantes en el archivo *output*.
   *input* y *output* deben ser *objetos archivos*. *input* se leerá
   hasta que "input.read()" retorna un objeto de bytes vacío.
   "encode()" inserta un carácter de nueva línea ("b'\n'") después de
   cada 76 bytes de la salida, además de garantizar que la salida
   siempre termine con una nueva línea, según **RFC 2045** (MIME).

base64.encodebytes(s)

   Codifica el *objeto similar a bytes* *s*, que puede contener datos
   binarios arbitrarios, y retorna "bytes" que contienen los datos
   codificados en base64, con líneas nuevas ("b'\n'") insertado
   después de cada 76 bytes de salida, y asegurando que haya una nueva
   línea final, según **RFC 2045** (MIME).

   Added in version 3.1.

Un ejemplo de uso del módulo:

>>> import base64
>>> encoded = base64.b64encode(b'data to be encoded')
>>> encoded
b'ZGF0YSB0byBiZSBlbmNvZGVk'
>>> data = base64.b64decode(encoded)
>>> data
b'data to be encoded'

## Consideraciones de Seguridad

Se agregó una nueva sección de consideraciones de seguridad a **RFC
4648** (sección 12); se recomienda revisar la sección de seguridad
para cualquier código implementado en producción.

Ver también:

  Módulo "binascii"
     Módulo de soporte que contiene conversiones de ASCII a binario y
     binario a ASCII.

  **RFC 1521** - MIME (Extensiones multipropósito de correo de
  Internet) Parte uno: Mecanismos para especificar y describir el
  formato de los cuerpos de mensajes de Internet
     La Sección 5.2, "Codificación de transferencia de contenido
     Base64", proporciona la definición de la codificación base64.

  ISO 32000-2 Portable document format - Part 2: PDF 2.0
     Section 7.4.3, "ASCII85Decode Filter," provides the definition of
     the Ascii85 encoding used in PDF and PostScript, including the
     output character set and the details of data length preservation
     using zero-padding and partial output groups.

  ZeroMQ RFC 32/Z85
     The "Formal Specification" section provides the character set
     used in Z85.
