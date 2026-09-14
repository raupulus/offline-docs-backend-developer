---
title: '"email.errors": Exception and Defect classes'
source_url: https://docs.python.org/es/3
source_path: library/email.errors.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2420
---

# "email.errors": Exception and Defect classes

**Código fuente:** Lib/email/errors.py

======================================================================

The following exception classes are defined in the "email.errors"
module:

exception email.errors.MessageError

   Esta es la clase base para todas las excepciones que el paquete
   "email"  puede lanzar. Se deriva de la clase estándar "Exception"
   y no define métodos adicionales.

exception email.errors.MessageParseError

   Esta es la clase base para las excepciones generadas por la clase
   "Parser". Se deriva de "MessageError". Esta clase también es
   utilizada internamente por el analizador sintáctico utilizado por
   "headerregistry".

exception email.errors.HeaderParseError

   Lanzada en algunas condiciones de error al analizar los encabezados
   **RFC 5322** de un mensaje, esta clase se deriva de
   "MessageParseError". El método "set_boundary()" lanzará este error
   si el tipo de contenido es desconocido cuando se llama al método.
   "Header" puede lanzar este error para ciertos errores de
   decodificación de base64, y cuando se intenta crear un encabezado
   que parece contener un encabezado incrustado (es decir, hay lo que
   se supone que es un línea de continuación que no tiene espacios en
   blanco iniciales y parece un encabezado).

exception email.errors.BoundaryError

   Deprecada y no utilizada actualmente.

exception email.errors.MultipartConversionError

   Raised if the "attach()" method is called on an instance of a class
   derived from "MIMENonMultipart" (e.g. "MIMEImage").
   "MultipartConversionError" multiply inherits from "MessageError"
   and the built-in "TypeError".

exception email.errors.HeaderWriteError

   Raised when an error occurs when the "generator" outputs headers.

exception email.errors.MessageDefect

   This is the base class for all defects found when parsing email
   messages. It is derived from "ValueError".

exception email.errors.HeaderDefect

   This is the base class for all defects found when parsing email
   headers. It is derived from "MessageDefect".

Aquí está la lista de defectos que "FeedParser" puede encontrar
mientras analiza mensajes. Tenga en cuenta que los defectos se agregan
al mensaje donde se encontró el problema, por ejemplo, si un mensaje
anidado dentro de un *multipart/alternative* tenía un encabezado mal
formado, ese objeto de mensaje anidado tendría un defecto, pero el
contenido los mensajes no lo harían.

Todas las clases de defectos se derivan de
"email.errors.MessageDefect".

exception email.errors.NoBoundaryInMultipartDefect

   A message claimed to be a multipart, but had no *boundary*
   parameter.

exception email.errors.StartBoundaryNotFoundDefect

   The start boundary claimed in the *Content-Type* header was never
   found.

exception email.errors.CloseBoundaryNotFoundDefect

   A start boundary was found, but no corresponding close boundary was
   ever found.

   Added in version 3.3.

exception email.errors.FirstHeaderLineIsContinuationDefect

   The message had a continuation line as its first header line.

exception email.errors.MisplacedEnvelopeHeaderDefect

   A "Unix From" header was found in the middle of a header block.

exception email.errors.MissingHeaderBodySeparatorDefect

   A line was found while parsing headers that had no leading white
   space but contained no ':'.  Parsing continues assuming that the
   line represents the first line of the body.

   Added in version 3.3.

exception email.errors.MalformedHeaderDefect

   A header was found that was missing a colon, or was otherwise
   malformed.

   Obsoleto desde la versión 3.3: Este defecto no se ha utilizado por
   varias versiones de Python.

exception email.errors.MultipartInvariantViolationDefect

   A message claimed to be a *multipart*, but no subparts were found.
   Note that when a message has this defect, its "is_multipart()"
   method may return "False" even though its content type claims to be
   *multipart*.

exception email.errors.InvalidBase64PaddingDefect

   When decoding a block of base64 encoded bytes, the padding was not
   correct. Enough padding is added to perform the decode, but the
   resulting decoded bytes may be invalid.

exception email.errors.InvalidBase64CharactersDefect

   When decoding a block of base64 encoded bytes, characters outside
   the base64 alphabet were encountered.  The characters are ignored,
   but the resulting decoded bytes may be invalid.

exception email.errors.InvalidBase64LengthDefect

   When decoding a block of base64 encoded bytes, the number of non-
   padding base64 characters was invalid (1 more than a multiple of
   4).  The encoded block was kept as-is.

exception email.errors.InvalidDateDefect

   When decoding an invalid or unparsable date field.  The original
   value is kept as-is.
