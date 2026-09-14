---
title: '"urllib.error" --- Exception classes raised by urllib.request'
source_url: https://docs.python.org/es/3
source_path: library/urllib.error.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4400
---

# "urllib.error" --- Exception classes raised by urllib.request

**Código fuente:** Lib/urllib/error.py

======================================================================

The "urllib.error" module defines the exception classes for exceptions
raised by "urllib.request".  The base exception class is "URLError".

The following exceptions are raised by "urllib.error" as appropriate:

exception urllib.error.URLError

   Los gestores lanzan esta excepción (o excepciones derivadas) cuando
   encuentran un problema. Es una subclase de "OSError".

   reason

      El motivo de este error. Puede ser una cadena de mensaje u otra
      instancia de una excepción.

   Distinto en la versión 3.3: "URLError" used to be a subtype of
   "IOError", which is now an alias of "OSError".

exception urllib.error.HTTPError(url, code, msg, hdrs, fp)

   A pesar de ser una excepción (una subclase de "URLError"), un
   "HTTPError" también puede funcionar como un valor de retorno no
   excepcional de tipo archivo (lo mismo que retorna "urlopen()").
   Esto es útil para gestionar errores HTTP exóticos, como peticiones
   de autentificación.

   url

      Contiene la URL de la solicitud. Un alias para el atributo
      *filename*.

   code

      Un código de estado HTTP como los definidos en **RFC 2616**.
      Este valor numérico se corresponde con un valor de un
      diccionario de códigos como el que hay en
      "http.server.BaseHTTPRequestHandler.responses".

   reason

      Normalmente esto es una cadena de caracteres que explica el
      motivo de este error. Un alias para el atributo *msg*.

   headers

      Las cabeceras de la respuesta HTTP de la petición HTTP que causó
      el "HTTPError". Un alias para el atributo *hdrs*.

      Added in version 3.4.

   fp

      Un objeto similar a un archivo donde se puede leer el cuerpo del
      error HTTP.

exception urllib.error.ContentTooShortError(msg, content)

   Esta excepción se lanza cuando la función "urlretrieve()" detecta
   que la cantidad de datos descargados es menor que la esperada (dada
   por la cabecera *Content-Length*).

   content

      Los datos descargados (y supuestamente truncados).
