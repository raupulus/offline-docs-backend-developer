---
title: '"email.iterators": Iterators'
source_url: https://docs.python.org/es/3
source_path: library/email.iterators.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2470
---

# "email.iterators": Iterators

**Código fuente:** Lib/email/iterators.py

======================================================================

Iterating over a message object tree is fairly easy with the
"Message.walk" method.  The "email.iterators" module provides some
useful higher level iterations over message object trees.

email.iterators.body_line_iterator(msg, decode=False)

   Itera sobre todas las cargas útiles de todas las subpartes de
   *msg*, retornando las cargas útiles en cadenas de caracteres línea
   por línea. Descarta todas las cabeceras de las subpartes, y
   descarta cualquier subparte con una carga útil que no sea una
   cadena de caracteres de Python. Esto de alguna forma es equivalente
   a leer la representación en texto plano del mensaje desde un
   fichero usando "readline()", descartando todas las cabeceras
   intermedias.

   El argumento opcional *decode* se pasa a través de
   "Message.get_payload".

email.iterators.typed_subpart_iterator(msg, maintype='text', subtype=None)

   Itera sobre todas las subpartes de *msg*, retornando solo las
   subpartes que coincidan el tipo MIME especificado por *maintype* y
   *subtype*.

   Note que *subtype* es opcional; si se omite, entonces se comprobará
   si el tipo MIME de las subpartes coincide con el tipo principal
   solamente. *maintype* es opcional también; su valor por defecto es
   *text*.

   Por tanto, por defecto "typed_subpart_iterator()" retorna cada
   parte que tenga un tipo MIME *text/**.

La siguiente función se ha añadido como una útil herramienta de
depuración. *No* debe ser considerada parte de la interfaz pública
soportada para este paquete.

email.iterators._structure(msg, fp=None, level=0, include_default=False)

   Imprime una representación con sangrías de los tipos del contenido
   de la estructura de objetos mensaje. Por ejemplo:

      >>> msg = email.message_from_file(somefile)
      >>> _structure(msg)
      multipart/mixed
          text/plain
          text/plain
          multipart/digest
              message/rfc822
                  text/plain
              message/rfc822
                  text/plain
              message/rfc822
                  text/plain
              message/rfc822
                  text/plain
              message/rfc822
                  text/plain
          text/plain

   El argumento opcional *fp* es un objeto similar a un fichero en el
   que imprimir la salida. Debe ser adecuado para la función de Python
   "print()". Se usa *level* internamente. *include_default*, si tiene
   su valor a verdadero, imprime el tipo por defecto también.
