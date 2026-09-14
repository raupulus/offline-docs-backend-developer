---
title: '"http" --- HTTP modules'
source_url: https://docs.python.org/es/3
source_path: library/http.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2890
---

# "http" --- HTTP modules

**Código fuente:** Lib/http/__init__.py

======================================================================

"http" is a package that collects several modules for working with the
HyperText Transfer Protocol:

* "http.client" es un cliente del protocolo HTTP de bajo nivel; para
  la apertura de URL de alto nivel use "urllib.request"

* "http.server" contiene clases de servidor HTTP básicas basadas en
  "socketserver"

* "http.cookies" tiene utilidades para implementar la gestión de
  estados mediante cookies

* "http.cookiejar" provee persistencia de cookies

The "http" module also defines the following enums that help you work
with http related code:

class http.HTTPStatus

   Added in version 3.5.

   Una subclase de "enum.IntEnum" que define un conjunto de códigos de
   estado HTTP, frases de motivo y descripciones largas escritas en
   inglés.

   Uso:

      >>> from http import HTTPStatus
      >>> HTTPStatus.OK
      HTTPStatus.OK
      >>> HTTPStatus.OK == 200
      True
      >>> HTTPStatus.OK.value
      200
      >>> HTTPStatus.OK.phrase
      'OK'
      >>> HTTPStatus.OK.description
      'Request fulfilled, document follows'
      >>> list(HTTPStatus)
      [HTTPStatus.CONTINUE, HTTPStatus.SWITCHING_PROTOCOLS, ...]

## Códigos de estado HTTP

Los códigos de estado registrados por IANA disponibles en
"http.HTTPStatus" son:

+---------+-------------------------------------+---------------------------------------------------------------------------------+
| Código  | Nombre de la enumeración            | Detalle                                                                         |
|=========|=====================================|=================================================================================|
## | "100"   | "CONTINUE"                          | HTTP Semantics **RFC 9110**, Section 15.2.1                                     |

## | "101"   | "SWITCHING_PROTOCOLS"               | HTTP Semantics **RFC 9110**, Section 15.2.2                                     |

## | "102"   | "PROCESSING"                        | WebDAV **RFC 2518**, Sección 10.1                                               |

## | "103"   | "EARLY_HINTS"                       | Un código de estado HTTP para indicar pistas **RFC 8297**                       |

## | "200"   | "OK"                                | HTTP Semantics **RFC 9110**, Section 15.3.1                                     |

## | "201"   | "CREATED"                           | HTTP Semantics **RFC 9110**, Section 15.3.2                                     |

## | "202"   | "ACCEPTED"                          | HTTP Semantics **RFC 9110**, Section 15.3.3                                     |

## | "203"   | "NON_AUTHORITATIVE_INFORMATION"     | HTTP Semantics **RFC 9110**, Section 15.3.4                                     |

## | "204"   | "NO_CONTENT"                        | HTTP Semantics **RFC 9110**, Section 15.3.5                                     |

## | "205"   | "RESET_CONTENT"                     | HTTP Semantics **RFC 9110**, Section 15.3.6                                     |

## | "206"   | "PARTIAL_CONTENT"                   | HTTP Semantics **RFC 9110**, Section 15.3.7                                     |

## | "207"   | "MULTI_STATUS"                      | WebDAV **RFC 4918**, Sección 11.1                                               |

## | "208"   | "ALREADY_REPORTED"                  | Extensiones de enlace a WebDAV **RFC 5842**, Sección 7.1 (Experimental)         |

## | "226"   | "IM_USED"                           | Codificación delta en HTTP **RFC 3229**, Sección 10.4.1                         |

## | "300"   | "MULTIPLE_CHOICES"                  | HTTP Semantics **RFC 9110**, Section 15.4.1                                     |

## | "301"   | "MOVED_PERMANENTLY"                 | HTTP Semantics **RFC 9110**, Section 15.4.2                                     |

## | "302"   | "FOUND"                             | HTTP Semantics **RFC 9110**, Section 15.4.3                                     |

## | "303"   | "SEE_OTHER"                         | HTTP Semantics **RFC 9110**, Section 15.4.4                                     |

## | "304"   | "NOT_MODIFIED"                      | HTTP Semantics **RFC 9110**, Section 15.4.5                                     |

## | "305"   | "USE_PROXY"                         | HTTP Semantics **RFC 9110**, Section 15.4.6                                     |

## | "307"   | "TEMPORARY_REDIRECT"                | HTTP Semantics **RFC 9110**, Section 15.4.8                                     |

## | "308"   | "PERMANENT_REDIRECT"                | HTTP Semantics **RFC 9110**, Section 15.4.9                                     |

## | "400"   | "BAD_REQUEST"                       | HTTP Semantics **RFC 9110**, Section 15.5.1                                     |

## | "401"   | "UNAUTHORIZED"                      | HTTP Semantics **RFC 9110**, Section 15.5.2                                     |

## | "402"   | "PAYMENT_REQUIRED"                  | HTTP Semantics **RFC 9110**, Section 15.5.3                                     |

## | "403"   | "FORBIDDEN"                         | HTTP Semantics **RFC 9110**, Section 15.5.4                                     |

## | "404"   | "NOT_FOUND"                         | HTTP Semantics **RFC 9110**, Section 15.5.5                                     |

## | "405"   | "METHOD_NOT_ALLOWED"                | HTTP Semantics **RFC 9110**, Section 15.5.6                                     |

## | "406"   | "NOT_ACCEPTABLE"                    | HTTP Semantics **RFC 9110**, Section 15.5.7                                     |

## | "407"   | "PROXY_AUTHENTICATION_REQUIRED"     | HTTP Semantics **RFC 9110**, Section 15.5.8                                     |

## | "408"   | "REQUEST_TIMEOUT"                   | HTTP Semantics **RFC 9110**, Section 15.5.9                                     |

## | "409"   | "CONFLICT"                          | HTTP Semantics **RFC 9110**, Section 15.5.10                                    |

## | "410"   | "GONE"                              | HTTP Semantics **RFC 9110**, Section 15.5.11                                    |

## | "411"   | "LENGTH_REQUIRED"                   | HTTP Semantics **RFC 9110**, Section 15.5.12                                    |

## | "412"   | "PRECONDITION_FAILED"               | HTTP Semantics **RFC 9110**, Section 15.5.13                                    |

## | "413"   | "CONTENT_TOO_LARGE"                 | HTTP Semantics **RFC 9110**, Section 15.5.14                                    |

## | "414"   | "URI_TOO_LONG"                      | HTTP Semantics **RFC 9110**, Section 15.5.15                                    |

## | "415"   | "UNSUPPORTED_MEDIA_TYPE"            | HTTP Semantics **RFC 9110**, Section 15.5.16                                    |

## | "416"   | "RANGE_NOT_SATISFIABLE"             | HTTP Semantics **RFC 9110**, Section 15.5.17                                    |

## | "417"   | "EXPECTATION_FAILED"                | HTTP Semantics **RFC 9110**, Section 15.5.18                                    |

## | "418"   | "IM_A_TEAPOT"                       | HTCPCP/1.0 **RFC 2324**, Sección 2.3.2                                          |

## | "421"   | "MISDIRECTED_REQUEST"               | HTTP Semantics **RFC 9110**, Section 15.5.20                                    |

## | "422"   | "UNPROCESSABLE_CONTENT"             | HTTP Semantics **RFC 9110**, Section 15.5.21                                    |

## | "423"   | "LOCKED"                            | WebDAV **RFC 4918**, Sección 11.3                                               |

## | "424"   | "FAILED_DEPENDENCY"                 | WebDAV **RFC 4918**, Sección 11.4                                               |

## | "425"   | "TOO_EARLY"                         | Uso de datos iniciales en HTTP **RFC 8470**                                     |

## | "426"   | "UPGRADE_REQUIRED"                  | HTTP Semantics **RFC 9110**, Section 15.5.22                                    |

## | "428"   | "PRECONDITION_REQUIRED"             | Códigos de estados HTTP adicionales **RFC 6585**                                |

## | "429"   | "TOO_MANY_REQUESTS"                 | Códigos de estados HTTP adicionales **RFC 6585**                                |

## | "431"   | "REQUEST_HEADER_FIELDS_TOO_LARGE"   | Códigos de estados HTTP adicionales **RFC 6585**                                |

## | "451"   | "UNAVAILABLE_FOR_LEGAL_REASONS"     | Un código de estado HTTP para reportar obstáculos legales **RFC 7725**          |

## | "500"   | "INTERNAL_SERVER_ERROR"             | HTTP Semantics **RFC 9110**, Section 15.6.1                                     |

## | "501"   | "NOT_IMPLEMENTED"                   | HTTP Semantics **RFC 9110**, Section 15.6.2                                     |

## | "502"   | "BAD_GATEWAY"                       | HTTP Semantics **RFC 9110**, Section 15.6.3                                     |

## | "503"   | "SERVICE_UNAVAILABLE"               | HTTP Semantics **RFC 9110**, Section 15.6.4                                     |

## | "504"   | "GATEWAY_TIMEOUT"                   | HTTP Semantics **RFC 9110**, Section 15.6.5                                     |

## | "505"   | "HTTP_VERSION_NOT_SUPPORTED"        | HTTP Semantics **RFC 9110**, Section 15.6.6                                     |

| "506"   | "VARIANT_ALSO_NEGOTIATES"           | Negociación transparente de contenido en HTTP **RFC 2295**, Sección 8.1         |
## |         |                                     | (Experimental)                                                                  |

## | "507"   | "INSUFFICIENT_STORAGE"              | WebDAV **RFC 4918**, Sección 11.5                                               |

## | "508"   | "LOOP_DETECTED"                     | Extensiones de unión WebDAV **RFC 5842**, Sección 7.2 (Experimental)            |

## | "510"   | "NOT_EXTENDED"                      | Un framework de extensión HTTP **RFC 2774**, Sección 7 (Experimental)           |

## | "511"   | "NETWORK_AUTHENTICATION_REQUIRED"   | Códigos de estados HTTP adicionales **RFC 6585**, Sección 6                     |

Con el fin de preservar la compatibilidad con versiones anteriores,
los valores de la enumeración están también presentes en el módulo
"http.client" en forma de constantes. El nombre de la enumeración es
el mismo que el nombre de la constante (ej. "http.HTTPStatus.OK" se
encuentra también disponible como "http.client.OK").

Distinto en la versión 3.7: Se agregó el código de estado "421
MISDIRECTED_REQUEST".

Added in version 3.8: Se agregó el código de estado "451
UNAVAILABLE_FOR_LEGAL_REASONS".

Added in version 3.9: Agregados códigos de estado "103 EARLY_HINTS",
"418 IM_A_TEAPOT" y "425 TOO_EARLY".

Distinto en la versión 3.13: Implemented RFC9110 naming for status
constants. Old constant names are preserved for backwards
compatibility: "413 REQUEST_ENTITY_TOO_LARGE", "414
REQUEST_URI_TOO_LONG", "416 REQUESTED_RANGE_NOT_SATISFIABLE" and "422
UNPROCESSABLE_ENTITY".

## Categoría de estado HTTP

Added in version 3.12.

Los valores enum tienen varias propiedades para indicar la categoría
de estado HTTP:

+----------------------+--------------------------+----------------------------------------+
| Propiedad            | Indica que               | Detalle                                |
|======================|==========================|========================================|
| "is_informational"   | "100 <= status <= 199"   | HTTP Semantics **RFC 9110**, Section   |
## |                      |                          | 15                                     |

| "is_success"         | "200 <= status <= 299"   | HTTP Semantics **RFC 9110**, Section   |
## |                      |                          | 15                                     |

| "is_redirection"     | "300 <= status <= 399"   | HTTP Semantics **RFC 9110**, Section   |
## |                      |                          | 15                                     |

| "is_client_error"    | "400 <= status <= 499"   | HTTP Semantics **RFC 9110**, Section   |
## |                      |                          | 15                                     |

| "is_server_error"    | "500 <= status <= 599"   | HTTP Semantics **RFC 9110**, Section   |
## |                      |                          | 15                                     |

   Uso:

      >>> from http import HTTPStatus
      >>> HTTPStatus.OK.is_success
      True
      >>> HTTPStatus.OK.is_client_error
      False

class http.HTTPMethod

   Added in version 3.11.

   Una subclase de "enum.StrEnum" que define un conjunto de métodos
   HTTP y sus descripciones escritas en inglés.

   Uso:

      >>> from http import HTTPMethod
      >>>
      >>> HTTPMethod.GET
      <HTTPMethod.GET>
      >>> HTTPMethod.GET == 'GET'
      True
      >>> HTTPMethod.GET.value
      'GET'
      >>> HTTPMethod.GET.description
      'Retrieve the target.'
      >>> list(HTTPMethod)
      [<HTTPMethod.CONNECT>,
       <HTTPMethod.DELETE>,
       <HTTPMethod.GET>,
       <HTTPMethod.HEAD>,
       <HTTPMethod.OPTIONS>,
       <HTTPMethod.PATCH>,
       <HTTPMethod.POST>,
       <HTTPMethod.PUT>,
       <HTTPMethod.TRACE>]

## Métodos HTTP

Los  métodos registrados por IANA disponibles en "http.HTTPMethod"
son:

+-------------+-------------------------------------+--------------------------------------------------------------------+
| Método      | Nombre de la enumeración            | Detalle                                                            |
|=============|=====================================|====================================================================|
## | "GET"       | "GET"                               | HTTP Semantics **RFC 9110**, Section 9.3.1                         |

## | "HEAD"      | "HEAD"                              | HTTP Semantics **RFC 9110**, Section 9.3.2                         |

## | "POST"      | "POST"                              | HTTP Semantics **RFC 9110**, Section 9.3.3                         |

## | "PUT"       | "PUT"                               | HTTP Semantics **RFC 9110**, Section 9.3.4                         |

## | "DELETE"    | "DELETE"                            | HTTP Semantics **RFC 9110**, Section 9.3.5                         |

## | "CONNECT"   | "CONNECT"                           | HTTP Semantics **RFC 9110**, Section 9.3.6                         |

## | "OPTIONS"   | "OPTIONS"                           | HTTP Semantics **RFC 9110**, Section 9.3.7                         |

## | "TRACE"     | "TRACE"                             | HTTP Semantics **RFC 9110**, Section 9.3.8                         |

## | "PATCH"     | "PATCH"                             | HTTP/1.1 **RFC 5789**                                              |
