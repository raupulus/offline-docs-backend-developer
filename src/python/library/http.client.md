---
title: '"http.client" --- HTTP protocol client'
source_url: https://docs.python.org/es/3
source_path: library/http.client.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2850
---

# "http.client" --- HTTP protocol client

**Código fuente:** Lib/http/client.py

======================================================================

Este módulo define clases que implementan el lado del cliente de los
protocolos HTTP y HTTPS. Normalmente no se usa directamente --- el
módulo "urllib.request" lo usa para gestionar URLs que utilizan HTTP y
HTTPS.

Ver también:

  The Requests package is recommended for a higher-level HTTP client
  interface.

Nota:

  El soporte HTTPS solo está disponible si Python se compiló con
  soporte SSL (a través del módulo "ssl").

Availability: not WASI.

This module does not work or is not available on WebAssembly. See
Plataformas WebAssembly for more information.

El módulo proporciona las siguientes clases:

class http.client.HTTPConnection(host, port=None, [timeout, ]source_address=None, blocksize=8192)

   Una instancia "HTTPConnection" representa una transacción con un
   servidor HTTP. Se debe instanciar pasándole un host y un número de
   puerto opcional. Si no se pasa ningún número de puerto, el puerto
   se extrae de la cadena de host si tiene la forma "host:port"; de lo
   contrario, se utiliza el puerto HTTP predeterminado (80). Si se
   proporciona el parámetro opcional *timeout*, las operaciones de
   bloqueo (como los intentos de conexión) expirarán después de esos
   segundos (si no se proporciona, se usa la configuración de tiempo
   de espera global predeterminada). El parámetro opcional
   *source_address* puede ser una tupla de un (host, puerto) para usar
   como la dirección de origen desde la que se realiza la conexión
   HTTP. El parámetro opcional *blocksize* establece el tamaño del
   búfer en bytes para enviar un cuerpo de mensaje similar a un
   archivo.

   Por ejemplo, las siguientes llamadas crean instancias que se
   conectan al servidor en el mismo host y puerto:

      >>> h1 = http.client.HTTPConnection('www.python.org')
      >>> h2 = http.client.HTTPConnection('www.python.org:80')
      >>> h3 = http.client.HTTPConnection('www.python.org', 80)
      >>> h4 = http.client.HTTPConnection('www.python.org', 80, timeout=10)

   Distinto en la versión 3.2: *source_address* fue adicionado.

   Distinto en la versión 3.4: Se eliminó el argumento *strict*. Las
   "Respuestas Simples" de estilo HTTP 0.9 ya no son compatibles.

   Distinto en la versión 3.7: argumento *blocksize* fue adicionado.

class http.client.HTTPSConnection(host, port=None, *, [timeout, ]source_address=None, context=None, blocksize=8192)

   Una subclase de "HTTPConnection" que usa SSL para la comunicación
   con servidores seguros. El puerto predeterminado es "443". Si se
   especifica *context*, debe ser una instancia de "ssl.SSLContext"
   que describa las diversas opciones de SSL.

   Por favor lea Consideraciones de seguridad para obtener más
   información sobre las mejores prácticas.

   Distinto en la versión 3.2: *source_address*, *context* y
   *check_hostname* fueron adicionados.

   Distinto en la versión 3.2: This class now supports HTTPS virtual
   hosts if possible (that is, if "ssl.HAS_SNI" is true).

   Distinto en la versión 3.4: Se eliminó el argumento *strict*. Las
   "Respuestas Simples" de estilo HTTP 0.9 ya no son compatibles.

   Distinto en la versión 3.4.3: This class now performs all the
   necessary certificate and hostname checks by default. To revert to
   the previous, unverified, behavior
   "ssl._create_unverified_context()" can be passed to the *context*
   parameter.

   Distinto en la versión 3.8: Esta clase ahora habilita TLS 1.3
   "ssl.SSLContext.post_handshake_auth" para el *context*
   predeterminado o cuando *cert_file* se pasa con un *context*
   personalizado.

   Distinto en la versión 3.10: This class now sends an ALPN extension
   with protocol indicator "http/1.1" when no *context* is given.
   Custom *context* should set ALPN protocols with
   "set_alpn_protocols()".

   Distinto en la versión 3.12: The deprecated *key_file*, *cert_file*
   and *check_hostname* parameters have been removed.

class http.client.HTTPResponse(sock, debuglevel=0, method=None, url=None)

   Clase cuyas instancias se retornan tras una conexión exitosa. No
   son instancias realizadas directamente por el usuario.

   Distinto en la versión 3.4: Se eliminó el argumento *strict*. Las
   "Respuestas Simples" del estilo HTTP 0.9 ya no están soportadas.

Este módulo proporciona la siguiente función:

http.client.parse_headers(fp)

   Parse the headers from a file pointer *fp* representing a HTTP
   request/response. The file has to be a "BufferedIOBase" reader
   (i.e. not text) and must provide a valid **RFC 5322** style header.

   Esta función retorna una instancia de "http.client.HTTPMessage" que
   contiene los campos de encabezado, pero no un *payload* (lo mismo
   que "HTTPResponse.msg" y
   "http.server.BaseHTTPRequestHandler.headers" ) Después de regresar,
   el puntero de archivo *fp* está listo para leer el cuerpo HTTP.

   Nota:

     "parse_headers()" no analiza la línea de inicio de un mensaje
     HTTP; solo analiza las líneas "Name: value". El archivo tiene que
     estar listo para leer estas líneas de campo, por lo que la
     primera línea ya debe consumirse antes de llamar a la función.

Las siguientes excepciones son lanzadas según corresponda:

exception http.client.HTTPException

   La clase base de las otras excepciones en este módulo. Es una
   subclase de "Exception".

exception http.client.NotConnected

   Una subclase de "HTTPException".

exception http.client.InvalidURL

   Una subclase de "HTTPException", es lanzada si se proporciona un
   puerto y no es numérico o está vacío.

exception http.client.UnknownProtocol

   Una subclase de "HTTPException".

exception http.client.UnknownTransferEncoding

   Una subclase de "HTTPException".

exception http.client.UnimplementedFileMode

   Una subclase de "HTTPException".

exception http.client.IncompleteRead

   Una subclase de "HTTPException".

exception http.client.ImproperConnectionState

   Una subclase de "HTTPException".

exception http.client.CannotSendRequest

   Una subclase de "ImproperConnectionState".

exception http.client.CannotSendHeader

   Una subclase de "ImproperConnectionState".

exception http.client.ResponseNotReady

   Una subclase de "ImproperConnectionState".

exception http.client.BadStatusLine

   Una subclase de "HTTPException". Es lanzada si un servidor responde
   con un código de estado HTTP que no entendemos.

exception http.client.LineTooLong

   Una subclase de "HTTPException". Es lanzada si se recibe una línea
   excesivamente larga en el protocolo HTTP del servidor.

exception http.client.RemoteDisconnected

   Una subclase de "ConnectionResetError" y "BadStatusLine". Lanzada
   por "HTTPConnection.getresponse()" cuando el intento de leer la
   respuesta no produce datos leídos de la conexión, indica que el
   extremo remoto ha cerrado la conexión.

   Added in version 3.5: Previamente, "BadStatusLine""('')" fue
   lanzada.

Las constantes definidas en este módulo son:

http.client.HTTP_PORT

   El puerto predeterminado para el protocolo HTTP (siempre "80").

http.client.HTTPS_PORT

   El puerto predeterminado para el protocolo HTTPS (siempre "443").

http.client.responses

   Este diccionario asigna los códigos de estado HTTP 1.1 a los
   nombres W3C.

   Ejemplo: "http.client.responses[http.client.NOT_FOUND]" es "'Not
   Found'".

Consulte Códigos de estado HTTP para obtener una lista de los códigos
de estado HTTP que están disponibles en este módulo como constantes.

## Objetos de "HTTPConnection"

Las instancias "HTTPConnection" tienen los siguientes métodos:

HTTPConnection.request(method, url, body=None, headers={}, *, encode_chunked=False)

   This will send a request to the server using the HTTP request
   method *method* and the request URI *url*. The provided *url* must
   be an absolute path to conform with **RFC 2616 §5.1.2** (unless
   connecting to an HTTP proxy server or using the "OPTIONS" or
   "CONNECT" methods).

   Si se especifica *body*, los datos especificados se envían una vez
   finalizados los encabezados. Puede ser "str", un objeto *bytes-like
   object*, un objeto *file object* abierto, o un iterable de "bytes".
   Si *body* es una cadena, se codifica como ISO-8859-1, el valor
   predeterminado para HTTP. Si es un objeto de tipo bytes, los bytes
   se envían tal cual. Si es un objeto *file object*, se envía el
   contenido del archivo; Este objeto de archivo debe soportar al
   menos el método "read()". Si el objeto de archivo es una instancia
   de "io.TextIOBase", los datos retornados por el método "read()" se
   codificarán como ISO-8859-1, de lo contrario, los datos retornados
   por "read()" se envía como está. Si *body* es un iterable, los
   elementos del iterable se envían tal cual hasta que se agota el
   iterable.

   The *headers* argument should be a mapping of extra HTTP headers to
   send with the request. A **Host header** must be provided to
   conform with **RFC 2616 §5.1.2** (unless connecting to an HTTP
   proxy server or using the "OPTIONS" or "CONNECT" methods).

   Si *headers* no contiene "Content-Length" ni Transfer-Encoding,
   pero hay un cuerpo de solicitud, uno de esos campos de encabezado
   se agregará automáticamente. Si *body* es "None", el encabezado
   "Content-Length" se establece en "0" para los métodos que esperan
   un cuerpo ("PUT", "POST" y "PATCH") . Si *body* es una cadena de
   caracteres o un objeto similar a bytes que no es también un *file*,
   el encabezado "Content-Length" se establece en su longitud.
   Cualquier otro tipo de *body* (archivos e iterables en general) se
   codificará en fragmentos, y el encabezado "Transfer-Encoding" se
   establecerá automáticamente en lugar de "Content-Length".

   El argumento *encode_chunked* solo es relevante si "Transfer-
   Encoding" se especifica en *headers*. Si *encode_chunked* es
   "False", el objeto "HTTPConnection" supone que toda la codificación
   es manejada por el código de llamada. Si es "True", el cuerpo
   estará codificado en fragmentos.

   For example, to perform a "GET" request to
   "https://docs.python.org/3/":

      >>> import http.client
      >>> host = "docs.python.org"
      >>> conn = http.client.HTTPSConnection(host)
      >>> conn.request("GET", "/3/", headers={"Host": host})
      >>> response = conn.getresponse()
      >>> print(response.status, response.reason)
      200 OK

   Nota:

     La codificación de transferencia fragmentada se ha agregado al
     protocolo HTTP versión 1.1. A menos que se sepa que el servidor
     HTTP maneja HTTP 1.1, el llamador debe especificar la longitud
     del contenido o debe pasar un "str" o un objeto similar a bytes
     que no sea también un archivo como la representación del cuerpo.

   Nota:

     Note that you must have read the whole response or call "close()"
     if "getresponse()" raised an non-"ConnectionError" exception
     before you can send a new request to the server.

   Distinto en la versión 3.2: *body* ahora puede ser un iterable.

   Distinto en la versión 3.6: Si ni "Content-Length" ni "Transfer-
   Encoding" están configurados en *headers*, el archivo y los objetos
   iterables *body* ahora están codificados en fragmentos. Se agregó
   el argumento *encode_chunked*. No se intenta determinar la longitud
   del contenido para los objetos de archivo.

HTTPConnection.getresponse()

   Debe llamarse después de enviar una solicitud para obtener la
   respuesta del servidor. Retorna una instancia de "HTTPResponse".

   Distinto en la versión 3.5: Si una "ConnectionError" o una subclase
   fue lanzada, el objeto "HTTPConnection" estará listo para volver a
   conectarse cuando se envíe una nueva solicitud.Note that this does
   not apply to "OSError"s raised by the underlying socket. Instead
   the caller is responsible to call "close()" on the existing
   connection.

HTTPConnection.set_debuglevel(level)

   Establecer el nivel de depuración. El nivel de depuración
   predeterminado es "0", lo que significa que no se imprime ninguna
   salida de depuración. Cualquier valor mayor que "0" hará que todos
   los resultados de depuración definidos actualmente se impriman en
   *stdout*. El "debuglevel" se pasa a cualquier objeto nuevo
   "HTTPResponse" que se cree.

   Added in version 3.1.

HTTPConnection.set_tunnel(host, port=None, headers=None)

   Configure el host y el puerto para el túnel de conexión HTTP. Esto
   permite ejecutar la conexión a través de un servidor proxy.

   The *host* and *port* arguments specify the endpoint of the
   tunneled connection (i.e. the address included in the CONNECT
   request, *not* the address of the proxy server).

   The *headers* argument should be a mapping of extra HTTP headers to
   send with the CONNECT request.

   As HTTP/1.1 is used for HTTP CONNECT tunnelling request, as per the
   RFC, a HTTP "Host:" header must be provided, matching the
   authority-form of the request target provided as the destination
   for the CONNECT request. If a HTTP "Host:" header is not provided
   via the headers argument, one is generated and transmitted
   automatically.

   Por ejemplo, para hacer un túnel a través de un servidor proxy
   HTTPS que se ejecuta localmente en el puerto 8080, pasaríamos la
   dirección del proxy al constructor "HTTPSConnection", y la
   dirección del host al que finalmente queremos llegar al método
   "set_tunnel()":

      >>> import http.client
      >>> conn = http.client.HTTPSConnection("localhost", 8080)
      >>> conn.set_tunnel("www.python.org")
      >>> conn.request("HEAD","/index.html")

   Added in version 3.2.

   Distinto en la versión 3.12: HTTP CONNECT tunnelling requests use
   protocol HTTP/1.1, upgraded from protocol HTTP/1.0. "Host:" HTTP
   headers are mandatory for HTTP/1.1, so one will be automatically
   generated and transmitted if not provided in the headers argument.

HTTPConnection.get_proxy_response_headers()

   Returns a dictionary with the headers of the response received from
   the proxy server to the CONNECT request.

   If the CONNECT request was not sent, the method returns "None".

   Added in version 3.12.

HTTPConnection.connect()

   Se conecta al servidor especificado cuando el objeto fue creado.
   Por defecto, esto se llama automáticamente cuando se realiza una
   solicitud si el cliente aún no tiene una conexión.

   Lanza un evento de auditoría "http.client.connect" con los
   argumentos "self", "host", "port".

HTTPConnection.close()

   Cierre la conexión al servidor.

HTTPConnection.blocksize

   Tamaño del búfer en bytes para enviar un archivo como cuerpo del
   mensaje.

   Added in version 3.7.

As an alternative to using the "request()" method described above, you
can also send your request step by step, by using the four functions
below.

HTTPConnection.putrequest(method, url, skip_host=False, skip_accept_encoding=False)

   Esta debería ser la primera llamada después de que se haya
   realizado la conexión al servidor. Envía una línea al servidor que
   consta de la cadena de caracteres *method*, la cadena de caracteres
   *url* y la versión HTTP ("HTTP/1.1"). Para deshabilitar el envío
   automático de encabezados "Host:" o "Accept-Encoding:" (por
   ejemplo, para aceptar codificaciones de contenido adicionales),
   especifique *skip_host* o *skip_accept_encoding* con valores no
   Falsos.

HTTPConnection.putheader(header, argument[, ...])

   Envía un encabezado de estilo **RFC 822**al servidor. Este envía
   una línea al servidor que consta del encabezado, dos puntos y un
   espacio, y el primer argumento. Si se dan más argumentos, se envían
   líneas de continuación, cada una de las cuales consta de tabulación
   y un argumento.

HTTPConnection.endheaders(message_body=None, *, encode_chunked=False)

   Envía una línea en blanco al servidor, señalando el final de los
   encabezados. El argumento opcional *message_body* se puede usar
   para pasar un cuerpo de mensaje asociado a la solicitud.

   Si *encode_chunked* es "True", el resultado de cada iteración de
   *message_body* se codificará en fragmentos como se especifica en
   **RFC 7230**, Sección 3.3.1. La forma en que se codifican los datos
   depende del tipo de *message_body*. Si *message_body* implementa
   buffer interface la codificación dará como resultado un solo
   fragmento. Si *message_body* es una "collections.abc.Iterable",
   cada iteración de *message_body* dará como resultado un fragmento.
   Si *message_body* es un objeto *file object*, cada llamada a
   ".read()" dará como resultado un fragmento. El método señala
   automáticamente el final de los datos codificados en fragmentos
   inmediatamente después de *message_body*.

   Nota:

     Debido a la especificación de codificación fragmentada,
     fragmentos vacíos producidos por un cuerpo iterador será ignorado
     por el codificador de fragmentos. Esto es para evitar la
     terminación prematura de la lectura de la solicitud por parte del
     servidor de destino debido a una codificación con formato
     incorrecto.

   Distinto en la versión 3.6: Added chunked encoding support and the
   *encode_chunked* parameter.

HTTPConnection.send(data)

   Envía datos al servidor. Esto debe usarse directamente solo después
   de que se haya llamado al método "endheaders()" y antes de que se
   llame al método "getresponse()".

   Lanza un evento de auditoría "http.client.send" con los argumentos
   "self", "data".

## Objetos de "HTTPResponse"

Una instancia de "HTTPResponse" envuelve la respuesta HTTP del
servidor. Proporciona acceso a los encabezados de la solicitud y al
cuerpo de la entidad. La respuesta es un objeto iterable y puede
usarse en una declaración "with".

Distinto en la versión 3.5: La interfaz "io.BufferedIOBase" ahora está
implementada y todas sus operaciones de lectura están soportadas.

HTTPResponse.read([amt])

   Lee y retorna el cuerpo de respuesta, o hasta los siguientes bytes
   *amt*.

HTTPResponse.readinto(b)

   Lee hasta los siguientes bytes "len(b)" del cuerpo de respuesta en
   el búfer *b*. Retorna el número de bytes leídos.

   Added in version 3.3.

HTTPResponse.getheader(name, default=None)

   Retorna el valor del encabezado *name*, o *default* si no hay un
   encabezado que coincida con *name*. Si hay más de un encabezado con
   el nombre *name*, retorne todos los valores unidos por ', '. Si
   'default' es cualquier iterable que no sea una sola cadena de
   caracteres sus elementos se retornan, de manera similar, unidos por
   comas.

HTTPResponse.getheaders()

   Retorna una lista de tuplas (encabezado, valor).

HTTPResponse.fileno()

   Retorna el "fileno" del socket implícito.

HTTPResponse.msg

   Una instancia "http.client.HTTPMessage" que contiene los
   encabezados de respuesta. "http.client.HTTPMessage" es una subclase
   de "email.message.Message".

HTTPResponse.version

   Versión del protocolo HTTP utilizada por el servidor. 10 para
   HTTP/1.0, 11 para HTTP/1.1.

HTTPResponse.url

   URL del recurso recuperado, comúnmente utilizado para determinar si
   se siguió una redirección.

HTTPResponse.headers

   Cabeceras de la respuesta en forma de una instancia
   "email.message.EmailMessage".

HTTPResponse.status

   Código del estado retornado por el servidor.

HTTPResponse.reason

   Una frase de la razón es retornada por el servidor.

HTTPResponse.debuglevel

   Un depurador. Si "debuglevel" es mayor que cero, los mensajes se
   imprimirán en "stdout" a medida que se lee y analiza la respuesta.

HTTPResponse.closed

   Es "True" si la transmisión está cerrada.

HTTPResponse.geturl()

   Obsoleto desde la versión 3.9: Deprecada a favor de "url".

HTTPResponse.info()

   Obsoleto desde la versión 3.9: Deprecada a favor de "headers".

HTTPResponse.getcode()

   Obsoleto desde la versión 3.9: Deprecada a favor de "status".

## Ejemplos

Aquí hay una sesión de ejemplo que usa el método "GET" *method*:

   >>> import http.client
   >>> conn = http.client.HTTPSConnection("www.python.org")
   >>> conn.request("GET", "/")
   >>> r1 = conn.getresponse()
   >>> print(r1.status, r1.reason)
   200 OK
   >>> data1 = r1.read()  # This will return entire content.
   >>> # The following example demonstrates reading data in chunks.
   >>> conn.request("GET", "/")
   >>> r1 = conn.getresponse()
   >>> while chunk := r1.read(200):
   ...     print(repr(chunk))
   b'<!doctype html>\n<!--[if"...
   ...
   >>> # Example of an invalid request
   >>> conn = http.client.HTTPSConnection("docs.python.org")
   >>> conn.request("GET", "/parrot.spam")
   >>> r2 = conn.getresponse()
   >>> print(r2.status, r2.reason)
   404 Not Found
   >>> data2 = r2.read()
   >>> conn.close()

Aquí hay una sesión de ejemplo que usa el método "HEAD". Tenga en
cuenta que el método "HEAD" nunca retorna ningún dato.

   >>> import http.client
   >>> conn = http.client.HTTPSConnection("www.python.org")
   >>> conn.request("HEAD", "/")
   >>> res = conn.getresponse()
   >>> print(res.status, res.reason)
   200 OK
   >>> data = res.read()
   >>> print(len(data))
   0
   >>> data == b''
   True

Aquí hay una sesión de ejemplo que usa el método "POST":

   >>> import http.client, urllib.parse
   >>> params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
   >>> headers = {"Content-type": "application/x-www-form-urlencoded",
   ...            "Accept": "text/plain"}
   >>> conn = http.client.HTTPConnection("bugs.python.org")
   >>> conn.request("POST", "", params, headers)
   >>> response = conn.getresponse()
   >>> print(response.status, response.reason)
   302 Found
   >>> data = response.read()
   >>> data
   b'Redirecting to <a href="https://bugs.python.org/issue12524">https://bugs.python.org/issue12524</a>'
   >>> conn.close()

Las solicitudes HTTP "PUT" del lado del cliente son muy similares a
las solicitudes "POST". La diferencia radica solo en el lado del
servidor donde los servidores HTTP permitirán que se creen recursos a
través de la solicitud "PUT". Cabe señalar que los métodos HTTP
personalizados también se manejan en "urllib.request.Request"
configurando el atributo de método apropiado. Aquí hay una sesión de
ejemplo que muestra cómo enviar una solicitud "PUT":

   >>> # This creates an HTTP request
   >>> # with the content of BODY as the enclosed representation
   >>> # for the resource http://localhost:8080/file
   ...
   >>> import http.client
   >>> BODY = "***filecontents***"
   >>> conn = http.client.HTTPConnection("localhost", 8080)
   >>> conn.request("PUT", "/file", BODY)
   >>> response = conn.getresponse()
   >>> print(response.status, response.reason)
   200, OK

## Objetos de "HTTPMessage"

class http.client.HTTPMessage(email.message.Message)

Una instancia de "http.client.HTTPMessage" contiene los encabezados de
una respuesta HTTP. Se implementa utilizando la clase
"email.message.Message".
