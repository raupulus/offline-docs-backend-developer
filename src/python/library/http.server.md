---
title: '"http.server" --- HTTP servers'
source_url: https://docs.python.org/es/3
source_path: library/http.server.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2880
---

# "http.server" --- HTTP servers

**Código fuente:** Lib/http/server.py

======================================================================

Este módulo define clases para implementar servidores HTTP.

Advertencia:

  "http.server" is not recommended for production. It only implements
  basic security checks.

Availability: not WASI.

This module does not work or is not available on WebAssembly. See
Plataformas WebAssembly for more information.

Una clase, "HTTPServer", es una subclase "socketserver.TCPServer".
Crea y escucha en el socket HTTP, enviando las peticiones a un
handler.  El código para crear y ejecutar el servidor se ve así:

   def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
       server_address = ('', 8000)
       httpd = server_class(server_address, handler_class)
       httpd.serve_forever()

class http.server.HTTPServer(server_address, RequestHandlerClass)

   This class builds on the "TCPServer" class by storing the server
   address as instance variables named "server_name" and
   "server_port". The server is accessible by the handler, typically
   through the handler's "server" instance variable.

   server_name

      The HTTP server's fully qualified domain name.

   server_port

      The HTTP server's port number obtained from *server_address*.

class http.server.ThreadingHTTPServer(server_address, RequestHandlerClass)

   Esta clase es idéntica a HTTPServer, pero utiliza subprocesos para
   controlar las solicitudes mediante el uso de "ThreadingMixIn". Esto
   es útil para controlar los sockets de pre-apertura de los
   navegadores web, en los que "HTTPServer" esperaría indefinidamente.

   Added in version 3.7.

class http.server.HTTPSServer(server_address, RequestHandlerClass, bind_and_activate=True, *, certfile, keyfile=None, password=None, alpn_protocols=None)

   Subclass of "HTTPServer" with a wrapped socket using the "ssl"
   module. If the "ssl" module is not available, instantiating a
   "HTTPSServer" object fails with a "RuntimeError".

   The *certfile* argument is the path to the SSL certificate chain
   file, and the *keyfile* is the path to the file containing the
   private key.

   A *password* can be specified for files protected and wrapped with
   PKCS#8, but beware that this could possibly expose hardcoded
   passwords in clear.

   Ver también:

     See "ssl.SSLContext.load_cert_chain()" for additional information
     on the accepted values for *certfile*, *keyfile* and *password*.

   When specified, the *alpn_protocols* argument must be a sequence of
   strings specifying the "Application-Layer Protocol Negotiation"
   (ALPN) protocols supported by the server. ALPN allows the server
   and the client to negotiate the application protocol during the TLS
   handshake.

   By default, it is set to "["http/1.1"]", meaning the server
   supports HTTP/1.1.

   Added in version 3.14.

class http.server.ThreadingHTTPSServer(server_address, RequestHandlerClass, bind_and_activate=True, *, certfile, keyfile=None, password=None, alpn_protocols=None)

   This class is identical to "HTTPSServer" but uses threads to handle
   requests by inheriting from "ThreadingMixIn". This is analogous to
   "ThreadingHTTPServer" only using "HTTPSServer".

   Added in version 3.14.

The "HTTPServer", "ThreadingHTTPServer", "HTTPSServer" and
"ThreadingHTTPSServer" must be given a *RequestHandlerClass* on
instantiation, of which this module provides three different variants:

class http.server.BaseHTTPRequestHandler(request, client_address, server)

   This class is used to handle the HTTP requests that arrive at the
   server.  By itself, it cannot respond to any actual HTTP requests;
   it must be subclassed to handle each request method (for example,
   "'GET'" or "'POST'"). "BaseHTTPRequestHandler" provides a number of
   class and instance variables, and methods for use by subclasses.

   The handler will parse the request and the headers, then call a
   method specific to the request type. The method name is constructed
   from the request. For example, for the request method "SPAM", the
   "do_SPAM()" method will be called with no arguments. All of the
   relevant information is stored in instance variables of the
   handler.  Subclasses should not need to override or extend the
   "__init__()" method.

   "BaseHTTPRequestHandler" tiene las siguientes variables de
   instancia:

   client_address

      Contiene una tupla con el formato "(host, port)" que hace
      referencia a la dirección del cliente.

   server

      Contiene la instancia del servidor.

   close_connection

      Booleano que se debe establecer antes de "handle_one_request()"
      retorna, que indica si se puede esperar otra solicitud o si la
      conexión debe cerrarse.

   requestline

      Contiene la representación de cadena de la línea de solicitud
      HTTP. Se elimina el CRLF de terminación. Este atributo debe
      establecerse mediante "handle_one_request()". Si no se ha
      procesado ninguna línea de solicitud válida, debe establecerse
      en la cadena vacía.

   command

      Contiene el comando (tipo de petición). Por ejemplo, "'GET'".

   path

      Contains the request path. If the query component of the URL is
      present, then "path" includes the query. Using the terminology
      of **RFC 3986**, "path" here includes "hier-part" and the
      "query".

   request_version

      Contiene la versión de la cadena de caracteres para la petición.
      Por ejemplo, "HTTP/1.0'".

   headers

      Holds an instance of the class specified by the "MessageClass"
      class variable. This instance parses and manages the headers in
      the HTTP request. The "parse_headers()" function from
      "http.client" is used to parse the headers and it requires that
      the HTTP request provide a valid **RFC 5322** style header.

   rfile

      Un flujo de entrada "io.BufferedIOBase", listo para leer desde
      el inicio de los datos de entrada opcionales.

   wfile

      Contiene el flujo de salida para escribir una respuesta al
      cliente. Se debe utilizar la adherencia apropiada al protocolo
      HTTP cuando se escribe en este flujo para lograr una
      interoperación exitosa con los clientes HTTP.

      Distinto en la versión 3.6: Este es un flujo de
      "io.BufferedIOBase".

   "BaseHTTPRequestHandler" tiene los siguientes atributos:

   server_version

      Especifica la versión del software del servidor. Es posible que
      desee anular esto. El formato es de múltiples cadenas separadas
      por espacio en blanco, donde cada cadena es de la forma
      nombre[/versión]. Por ejemplo, "BaseHTTP/0.2'".

   sys_version

      Contiene la versión del sistema Python, en una forma utilizable
      por el método "version_string" y la variable de clase
      "server_version". Por ejemplo, "Python/1.4'".

   error_message_format

      Specifies a format string that should be used by "send_error()"
      method for building an error response to the client. The string
      is filled by default with variables from "responses" based on
      the status code passed to "send_error()".

   error_content_type

      Especifica el encabezado *HTTP Content-Type* de las respuestas
      de error enviadas al cliente.  El valor predeterminado es
      "'text/html'".

   protocol_version

      Especifica la versión de HTTP con la cual el servidor es
      conforme. Es enviada como respuesta para informarle al cliente
      sobre las capacidades de comunicación del servidor para
      siguientes peticiones. Si se establece en "'HTTP/1.1'", el
      servidor permitirá conexiones persistentes HTTP; sin embargo, el
      servidor *debe* incluir un encabezado exacto "Content-Length"
      (usando "send_header()") en todas sus respuestas a los clientes.
      Para la compatibilidad con versiones anteriores, el valor
      predeterminado es "'HTTP/1.0'".

   MessageClass

      Especifica una "email.message.Message"-como clase para analizar
      los encabezados HTTP.  Típicamente, esto no es anulado, y por
      defecto es "http.client.HTTPMessage".

   responses

      Este atributo contiene una asignación de enteros de código de
      error a tuplas de dos elementos que contienen un mensaje corto y
      largo. Por ejemplo, "{code (shortmessage, longmessage)}". El
      *shortmessage* se utiliza normalmente como la clave *message* en
      una respuesta de error, y *longmessage* como la clave *explain*.
      Es utilizado por "send_response_only()" y "send_error()"
      métodos.

   Una instancia "BaseHTTPRequestHandler" tiene los siguientes
   métodos:

   handle()

      Calls "handle_one_request()" once (or, if persistent connections
      are enabled, multiple times) to handle incoming HTTP requests.
      You should never need to override it; instead, implement
      appropriate "do_*()" methods.

   handle_one_request()

      This method will parse and dispatch the request to the
      appropriate "do_*()" method.  You should never need to override
      it.

   handle_expect_100()

      When an HTTP/1.1 conformant server receives an "Expect:
      100-continue" request header it responds with a "100 Continue"
      followed by "200 OK" headers. This method can be overridden to
      raise an error if the server does not want the client to
      continue.  For example, the server can choose to send "417
      Expectation Failed" as a response header and "return False".

      Added in version 3.2.

   send_error(code, message=None, explain=None)

      Sends and logs a complete error reply to the client. The numeric
      *code* specifies the HTTP error code, with *message* as an
      optional, short, human readable description of the error.  The
      *explain* argument can be used to provide more detailed
      information about the error; it will be formatted using the
      "error_message_format" attribute and emitted, after a complete
      set of headers, as the response body.  The "responses" attribute
      holds the default values for *message* and *explain* that will
      be used if no value is provided; for unknown codes the default
      value for both is the string "???". The body will be empty if
      the method is HEAD or the response code is one of the following:
      "1*xx*", "204 No Content", "205 Reset Content", "304 Not
      Modified".

      Distinto en la versión 3.4: La respuesta de error incluye un
      encabezado de longitud de contenido. Añadido el argumento
      *explain*.

   send_response(code, message=None)

      Agrega un encabezado de respuesta al búfer de encabezados y
      registra la solicitud aceptada. La línea de respuesta HTTP se
      escribe en el búfer interno, seguido de los encabezados *Server*
      y *Date*. Los valores de estos dos encabezados se recogen de los
      métodos "version_string()" y "date_time_string()",
      respectivamente. Si el servidor no tiene la intención de enviar
      ningún otro encabezado utilizando el método "send_header()",
      entonces "send_response()" debe ir seguido de una llamada
      "end_headers()".

      Distinto en la versión 3.3: Los encabezados se almacenan en un
      búfer interno y "end_headers()" debe llamarse explícitamente.

   send_header(keyword, value)

      Agrega el encabezado HTTP a un búfer interno que se escribirá en
      la secuencia de salida cuando se invoca "end_headers()" o
      "flush_headers()". *keyword* debe especificar la palabra clave
      *header*, con *value* especificando su valor. Tenga en cuenta
      que, después de que se realizan las llamadas *send_header*,
      "end_headers()" DEBE llamarse para completar la operación.

      This method does not reject input containing CRLF sequences.

      Distinto en la versión 3.2: Los encabezados se almacenan en un
      búfer interno.

   send_response_only(code, message=None)

      Sends the response header only, used for the purposes when "100
      Continue" response is sent by the server to the client. The
      headers are not buffered and sent directly the output stream. If
      the *message* is not specified, the HTTP message corresponding
      the response *code*  is sent.

      This method does not reject *message* containing CRLF sequences.

      Added in version 3.2.

   end_headers()

      Adds a blank line (indicating the end of the HTTP headers in the
      response) to the headers buffer and calls "flush_headers()".

      Distinto en la versión 3.2: Los encabezados del buffer se
      escriben en el flujo de salida.

   flush_headers()

      Finalmente envía los encabezados al flujo de salida y limpia el
      buffer interno de los cabezales.

      Added in version 3.3.

   log_request(code='-', size='-')

      Registra una solicitud aceptada (exitosa). El *code* debe
      especificar el código numérico HTTP asociado a la respuesta. Si
      un tamaño de la respuesta está disponible, entonces debe ser
      pasado como el parámetro *size*.

   log_error(...)

      Registra un error cuando una solicitud no puede ser cumplida.
      Por defecto, pasa el mensaje a "log_message()", por lo que toma
      los mismos argumentos (*format* y valores adicionales).

   log_message(format, ...)

      Logs an arbitrary message to "sys.stderr". This is typically
      overridden to create custom error logging mechanisms. The
      *format* argument is a standard printf-style format string,
      where the additional arguments to "log_message()" are applied as
      inputs to the formatting. The client IP address and current date
      and time are prefixed to every message logged.

   version_string()

      Retorna la cadena de versiones del software del servidor. Esta
      es una combinación de los atributos "server_version" y
      "sys_version".

   date_time_string(timestamp=None)

      Retorna la fecha y la hora dadas por *timestamp* (que debe ser
      "None" o en el formato retornado por "time.time`()"), formateado
      para un encabezado de mensaje. Si se omite *timestamp*, utiliza
      la fecha y la hora actuales.

      El resultado se muestra como "Sun, 06 Nov 1994 08:49:37 GMT'".

   log_date_time_string()

      Retorna la fecha y la hora actuales, formateadas para el
      registro.

   address_string()

      Retorna la dirección del cliente.

      Distinto en la versión 3.3: Anteriormente, se realizó una
      búsqueda de nombres. Para evitar retrasos en la resolución del
      nombre, ahora siempre retorna la dirección IP.

class http.server.SimpleHTTPRequestHandler(request, client_address, server, directory=None)

   Esta clase sirve archivos del directorio *directory* e inferior, o
   del directorio actual si no se proporciona *directory*, mapeando
   directamente la estructura del directorio a las solicitudes HTTP.

   Distinto en la versión 3.7: Added the *directory* parameter.

   Distinto en la versión 3.9: El parámetro *directory* acepta un
   *path-like object*.

   La carga de trabajo, como el análisis de la solicitud, lo hace la
   clase base "BaseHTTPRequestHandler".  Esta clase implementa las
   funciones "do_GET()" y "do_HEAD()".

   Los siguientes se definen como atributos de clase de
   "SimpleHTTPRequestHandler":

   server_version

      Esto sería ""SimpleHTTP/" + __version__", donde "__version__" se
      define a nivel de módulo.

   index_pages

      Specifies the filenames that are treated as directory index
      pages.

      Defaults to "("index.html", "index.htm")".

      Added in version 3.12.

   extensions_map

      Un diccionario que asigna sufijos a tipos MIME contiene
      sobreescrituras personalizadas para las asignaciones
      predeterminadas del sistema. El mapeo se usa sin distinción
      entre mayúsculas y minúsculas, por lo que solo debe contener
      claves en minúsculas.

      Distinto en la versión 3.9: Este diccionario ya no contiene las
      asignaciones predeterminadas del sistema, sino que solo contiene
      anulaciones.

   Una instancia "SimpleHTTPRequestHandler" tiene los siguientes
   métodos:

   do_HEAD()

      Este método sirve para el tipo de petición: "'HEAD'" envía los
      encabezados que enviaría para la petición equivalente "GET". Ver
      el método "do_GET()" para una explicación más completa de los
      posibles encabezados.

   do_GET()

      La solicitud se asigna a un archivo local interpretando la
      solicitud como una ruta relativa al directorio de trabajo
      actual.

      If the request was mapped to a directory, the directory is
      checked for an index page as specified by "index_pages". If
      found, the file's contents are returned; otherwise a directory
      listing is generated by calling the "list_directory()" method.
      This method uses "os.listdir()" to scan the directory, and
      returns a "404" error response if the "listdir()" fails.

      If the request was mapped to a file, it is opened. Any "OSError"
      exception in opening the requested file is mapped to a "404",
      "'File not found'" error. If there was an "'If-Modified-Since'"
      header in the request, and the file was not modified after this
      time, a "304", "'Not Modified'" response is sent. Otherwise, the
      content type is guessed by calling the "guess_type()" method,
      which in turn uses the *extensions_map* variable, and the file
      contents are returned.

      Un encabezado de "'Content-type:'" con el tipo de contenido
      adivinado, seguido de un encabezado de "'Content-Length:'" con
      el tamaño del archivo y un encabezado de "'Last-Modified:'" con
      el tiempo de modificación del archivo.

      Then follows a blank line signifying the end of the headers, and
      then the contents of the file are output.

      Por ejemplo, ver la implementación de la función "test" en
      Lib/http/server.py.

      Distinto en la versión 3.7: Soporta la cabecera "'If-Modified-
      Since'".

   list_directory(path)

      Helper to list the contents of *path* when no index page is
      present.

      This returns either a *file-like object* (which must be closed
      by the caller) or "None" to indicate an error, in which case the
      caller has nothing further to do. In either case, the headers
      are sent.

   guess_type(path)

      Guess the type of the file at the given *path*.

      This returns a string of the form "type/subtype", usable for a
      MIME Content-type header.

      The default implementation looks the file's extension up in
      "extensions_map", falling back to "mimetypes.guess_file_type()"
      and then to "'application/octet-stream'".

      Distinto en la versión 3.13: Add "mimetypes.guess_file_type()"
      as a fallback.

The "SimpleHTTPRequestHandler" class can be used to create a very
basic webserver serving files relative to the current directory as
follows:

   import http.server
   import socketserver

   PORT = 8000

   Handler = http.server.SimpleHTTPRequestHandler

   with socketserver.TCPServer(("", PORT), Handler) as httpd:
       print("serving at port", PORT)
       httpd.serve_forever()

"SimpleHTTPRequestHandler" can also be subclassed to enhance behavior,
such as using different index file names by overriding the class
attribute "index_pages".

class http.server.CGIHTTPRequestHandler(request, client_address, server)

   Esta clase se utiliza para servir tanto a los archivos como a la
   salida de los scripts CGI del directorio actual y del siguiente.
   Note que el mapeo de la estructura jerárquica de HTTP a la
   estructura del directorio local es exactamente como en
   "SimpleHTTPRequestHandler".

   Nota:

     Los scripts CGI ejecutados por la clase "CGIHTTPRequestHandler"
     no pueden ejecutar redirecciones (código HTTP 302), porque el
     código 200 (la salida del script sigue) se envía antes de la
     ejecución del script CGI.  Esto adelanta el código de estado.

   La clase, sin embargo, ejecutará el script CGI, en lugar de
   servirlo como un archivo, si adivina que es un script CGI.  Sólo se
   usan CGI basados en directorios --- la otra configuración común del
   servidor es tratar las extensiones especiales como denotando los
   scripts CGI.

   The "do_GET()" and "do_HEAD()" functions are modified to run CGI
   scripts and serve the output, instead of serving files, if the
   request leads to somewhere below the "cgi_directories" path.

   La "CGIHTTPRequestHandler" define el siguiente miembro de datos:

   cgi_directories

      Esto por defecto es "['/cgi-bin', '/htbin']" y describe los
      directorios a tratar como si contuvieran scripts CGI.

   La "CGIHTTPRequestHandler" define el siguiente método:

   do_POST()

      Este método sirve para el tipo de petición "'POST'", sólo
      permitido para scripts CGI.  El error 501, "Can only POST to CGI
      scripts", se produce cuando se intenta enviar a una url no CGI.

   Tenga en cuenta que los scripts CGI se ejecutarán con UID de
   usuario *nobody*, por razones de seguridad.  Los problemas con el
   script CGI serán traducidos al error 403.

   Deprecated since version 3.13, will be removed in version 3.15:
   "CGIHTTPRequestHandler" is being removed in 3.15.  CGI has not been
   considered a good way to do things for well over a decade. This
   code has been unmaintained for a while now and sees very little
   practical use. Retaining it could lead to further security
   considerations.

## Command-line interface

"http.server" can also be invoked directly using the "-m" switch of
the interpreter.  The following example illustrates how to serve files
relative to the current directory:

   python -m http.server [OPTIONS] [port]

The following options are accepted:

port

   The server listens to port 8000 by default. The default can be
   overridden by passing the desired port number as an argument:

      python -m http.server 9000

-b, --bind <address>

   Specifies a specific address to which it should bind. Both IPv4 and
   IPv6 addresses are supported. By default, the server binds itself
   to all interfaces. For example, the following command causes the
   server to bind to localhost only:

      python -m http.server --bind 127.0.0.1

   Added in version 3.4.

   Distinto en la versión 3.8: Support IPv6 in the "--bind" option.

-d, --directory <dir>

   Specifies a directory to which it should serve the files. By
   default, the server uses the current directory. For example, the
   following command uses a specific directory:

      python -m http.server --directory /tmp/

   Added in version 3.7.

-p, --protocol <version>

   Specifies the HTTP version to which the server is conformant. By
   default, the server is conformant to HTTP/1.0. For example, the
   following command runs an HTTP/1.1 conformant server:

      python -m http.server --protocol HTTP/1.1

   Added in version 3.11.

--cgi

   "CGIHTTPRequestHandler" puede ser activado en la línea de comandos
   pasando la opción "--cgi":

      python -m http.server --cgi

   Deprecated since version 3.13, will be removed in version 3.15:
   "http.server" command line "--cgi" support is being removed because
   "CGIHTTPRequestHandler" is being removed.

Advertencia:

  "CGIHTTPRequestHandler" and the "--cgi" command-line option are not
  intended for use by untrusted clients and may be vulnerable to
  exploitation. Always use within a secure environment.

--tls-cert

   Specifies a TLS certificate chain for HTTPS connections:

      python -m http.server --tls-cert fullchain.pem

   Added in version 3.14.

--tls-key

   Specifies a private key file for HTTPS connections.

   This option requires "--tls-cert" to be specified.

   Added in version 3.14.

--tls-password-file

   Specifies the password file for password-protected private keys:

      python -m http.server \
             --tls-cert cert.pem \
             --tls-key key.pem \
             --tls-password-file password.txt

   This option requires "--tls-cert" to be specified.

   Added in version 3.14.

## Security considerations

"SimpleHTTPRequestHandler" will follow symbolic links when handling
requests which makes it possible for files outside of the specified
directory to be served.

Methods "BaseHTTPRequestHandler.send_header()" and
"BaseHTTPRequestHandler.send_response_only()" assume sanitized input
and do not perform input validation such as checking for the presence
of CRLF sequences. Untrusted input may result in HTTP header injection
attacks.

Earlier versions of Python did not scrub control characters from the
log messages emitted to stderr from "python -m http.server" or the
default "BaseHTTPRequestHandler" ".log_message" implementation. This
could allow remote clients connecting to your server to send nefarious
control codes to your terminal.

Distinto en la versión 3.12: Control characters are scrubbed in stderr
logs.
