---
title: '"wsgiref" --- WSGI Utilities and Reference Implementation'
source_url: https://docs.python.org/es/3
source_path: library/wsgiref.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4550
---

# "wsgiref" --- WSGI Utilities and Reference Implementation

**Código fuente:** Lib/wsgiref

======================================================================

Advertencia:

  "wsgiref" is a reference implementation and is not recommended for
  production. The module only implements basic security checks.

La Interfaz de Pasarela del Servidor Web, o *Web Server Gateway
Interface* en inglés (WSGI), es una interfaz estándar entre el
servidor web y aplicaciones web escritas en Python. Con una interfaz
estándar es más sencillo usar una aplicación que soporte WSGI con
diferentes servidores web.

Sólo los autores de servidores y frameworks web necesitan conocer cada
detalle y caso límite del diseño WSGI. No es necesario conocer cada
detalle de WSGI sólo para instalar o escribir una aplicación web
usando un *framework* existente.

"wsgiref" is a reference implementation of the WSGI specification that
can be used to add WSGI support to a web server or framework.  It
provides utilities for manipulating WSGI environment variables and
response headers, base classes for implementing WSGI servers, a demo
HTTP server that serves WSGI applications, types for static type
checking, and a validation tool that checks WSGI servers and
applications for conformance to the WSGI specification (**PEP 3333**).

Vea wsgi.readthedocs.io para más información sobre WSGI, así como
enlaces a tutoriales y otros recursos.

## "wsgiref.util" -- WSGI environment utilities

Este módulo ofrece una variedad de funciones útiles para trabajar con
entornos WSGI. Un entorno WSGI es un diccionario que contiene
variables de la petición HTTP, descrito en **PEP 3333**. Todas las
funciones que aceptan un parámetro *environ* esperan un diccionario
compatible con WSGI. Por favor, consulte la especificación detallada
en **PEP 3333**, y los alias de tipos que pueden usarse en las
anotaciones de tipo en "WSGIEnvironment".

wsgiref.util.guess_scheme(environ)

   Retorna una deducción del valor para "wsgi.url_scheme" que debería
   ser "http" o "https", buscando la variable de entorno "HTTPS" en el
   diccionario *environ*. El valor de retorno es una cadena.

   Esta función es útil al crear un *gateway* que envuelve CGI o un
   protocolo similar como FastCGI. Habitualmente, los servidores que
   ofrecen estos protocolos incluyen una variable "HTTPS" con el valor
   "1", "yes", o "on" cuando reciben una petición vía SSL. Así, esta
   función retorna "https" si encuentra ese valor, o "http", en caso
   contrario.

wsgiref.util.request_uri(environ, include_query=True)

   Retorna la URI completa de la petición, opcionalmente la cadena de
   consulta, usando el algoritmo encontrado en la sección "URL
   Reconstruction" de **PEP 3333**. Si *include_query* es falso, la
   cadena de consulta no se incluye en la URI resultante.

wsgiref.util.application_uri(environ)

   Similar a "request_uri()" excepto que se ignoran las variables
   "PATH_INFO" y "QUERY_STRING". El resultado es la URI base del
   objeto de aplicación indicado en la petición.

wsgiref.util.shift_path_info(environ)

   Desplaza un solo nombre de "PATH_INFO" a "SCRIPT_NAME" y retorna el
   nombre. Se modifica el diccionario *environ*, por lo que se deberá
   usar una copia si se quiere mantener "PATH_INFO" o "SCRIPT_NAME"
   intactos.

   Si no quedan segmentos en "PATH_INFO", retornará "None".

   Habitualmente, esta rutina se usa para procesar cada porción de la
   ruta del URI de la petición, por ejemplo, para usar la ruta como
   una serie de claves en un diccionario. Esta rutina modifica el
   entorno pasado para permitir invocar otra aplicación WSGI que esté
   localizada en la URI objetivo. Por ejemplo, si hay una aplicación
   WSGI en "/foo", y la ruta es "/foo/bar/baz", y la aplicación WSGI
   en "/foo" llama a "shift_path_info()", recibirá la cadena "bar", y
   se actualizará el entorno para pasarlo a una aplicación WSGI en
   "/foo/bar". Es decir, "SCRIPT_NAME" cambiará de "/foo" a "/foo/bar"
   y "PATH_INFO" cambiará de "/bar/baz" a "/baz".

   Cuando "PATH_INFO" es únicamente "/", esta rutina retornará una
   cadena vacía y añadirá una barra final a "SCRIPT_NAME", incluso
   cuando normalmente los segmentos de ruta vacíos se ignoran y
   "SCRIPT_NAME" no acaba con una barra. Este comportamiento es
   intencional, para asegurar que una aplicación puede diferenciar
   entre URIs que acaban en "/x" de las que acaban en "/x/" cuando
   usan esta rutina para atravesar objetos.

wsgiref.util.setup_testing_defaults(environ)

   Actualiza *environ* con valores por defecto triviales con propósito
   de prueba.

   Esta rutina añade varios parámetros requeridos por WSGI, incluyendo
   "HTTP_POST", "SERVER_NAME", "SERVER_PORT", "REQUEST_METHOD",
   "SCRIPT_NAME", "PATH_INFO", y todas las variables "wsgi.*"
   definidas en **PEP 3333**. Sólo ofrece valores por defecto y no
   reemplaza ningún valor existente en esas variables.

   Esta rutina pretende facilitar la preparación de entornos ficticios
   para pruebas unitarias de servidores y aplicaciones WSGI. NO
   debería usarse en servidores y aplicaciones WSGI reales, ya que los
   valores son ficticios!

   Example usage (see also "demo_app()" for another example):

      from wsgiref.util import setup_testing_defaults
      from wsgiref.simple_server import make_server

      # A relatively simple WSGI application. It's going to print out the
      # environment dictionary after being updated by setup_testing_defaults
      def simple_app(environ, start_response):
          setup_testing_defaults(environ)

          status = '200 OK'
          headers = [('Content-type', 'text/plain; charset=utf-8')]

          start_response(status, headers)

          ret = [("%s: %s\n" % (key, value)).encode("utf-8")
                 for key, value in environ.items()]
          return ret

      with make_server('', 8000, simple_app) as httpd:
          print("Serving on port 8000...")
          httpd.serve_forever()

In addition to the environment functions above, the "wsgiref.util"
module also provides these miscellaneous utilities:

wsgiref.util.is_hop_by_hop(header_name)

   Retorna "True" si 'header_name' es una cabecera "Hop-by-Hop"
   HTTP/1.1, como se define en **RFC 2616**.

class wsgiref.util.FileWrapper(filelike, blksize=8192)

   Una implementación concreta del protocolo
   "wsgiref.types.FileWrapper" usado para convertir objetos de tipo
   archivo en un *iterator*. Los objetos resultantes son *iterable*s.
   A medida que se itera sobre el objeto, el parámetro opcional
   *blksize* se pasará repetidamente al método "read()" del objeto
   archivo para obtener cadenas de bytes para entregar. Cuando
   "read()" retorna una cadena de bytes vacía, la iteración finalizará
   y no se podrá reiniciar.

   Si *filelike* tiene un método "close()", el objeto retornado
   también tendrá un método "close()" que llamará al método "close()"
   del objeto archivo subyacente.

   Ejemplo de uso:

      from io import StringIO
      from wsgiref.util import FileWrapper

      # We're using a StringIO-buffer for as the file-like object
      filelike = StringIO("This is an example file-like object"*10)
      wrapper = FileWrapper(filelike, blksize=5)

      for chunk in wrapper:
          print(chunk)

   Distinto en la versión 3.11: Support for "__getitem__()" method has
   been removed.

## "wsgiref.headers" -- WSGI response header tools

Este módulo ofrece una sola clase, "Headers", para la manipulación de
cabeceras de respuesta WSGI usando un interfaz de mapa.

class wsgiref.headers.Headers([headers])

   Crea un objeto con interfaz de mapa envolviendo *headers*, que debe
   ser una lista de tuplas nombre/valor de las cabeceras, como se
   describe en **PEP 3333**. El valor por defecto de *headers* es una
   lista vacía.

   "Headers" objects support typical mapping operations including
   "__getitem__()", "get()", "__setitem__()", "setdefault()",
   "__delitem__()" and "__contains__()".  For each of these methods,
   the key is the header name (treated case-insensitively), and the
   value is the first value associated with that header name.  Setting
   a header deletes any existing values for that header, then adds a
   new value at the end of the wrapped header list.  Headers' existing
   order is generally maintained, with new headers added to the end of
   the wrapped list.

   A diferencia de un diccionario, los objetos "Headers" no lanzan un
   error cuando se intenta obtener o eliminar una clave que no está en
   la lista de cabeceras subyacente. Al intentar obtener una clave
   inexistente simplemente se retornará "None", mientras que el
   intento de eliminación de una cabecera inexistente simplemente no
   tendrá ningún efecto.

   Los objetos "Headers" también soportan los métodos "keys()",
   "values()", y "items()". Las listas retornadas por "keys()" y
   "items()" pueden incluir la misma clave más de una vez si se trata
   de una cabecera de valor múltiple. La "len()" de un objeto
   "Headers" es la misma que la longitud de sus "items()", que es la
   misma que la longitud de la lista de cabeceras envuelta. De hecho,
   el método "items()" simplemente retorna una copia de la lista de
   cabeceras.

   La llamada "bytes()" sobre un objeto "Headers" retorna una cadena
   de bytes formateada y lista para su transmisión como cabeceras de
   respuesta HTTP. Cada cabecera se ubica en una línea con su valor
   separado por dos puntos y un espacio. Cada línea finaliza con un
   retorno de carro y un salto de línea, y la cadena de bytes finaliza
   con una línea en blanco.

   Además de la interfaz de mapa y las funcionalidades de formateado,
   los objetos "Headers" también ofrecen los siguientes métodos para
   consultar y añadir cabeceras con múltiples valores, y para añadir
   cabeceras con parámetros MIME:

   get_all(name)

      Retorna una lista de todos los valores para la cabecera
      indicada.

      La lista retornada tendrá los valores ordenados según la lista
      de cabeceras original o según se hayan añadido a esta instancia,
      y podrá contener duplicados. Cualquier campo eliminado y añadido
      de nuevo estará al final de la lista. Si no existen campos con
      el nombre indicado, retornará una lista vacía.

   add_header(name, value, **_params)

      Añade una cabecera, posiblemente de valor múltiple, con los
      parámetros MIME opcionales especificados vía argumentos por
      palabra clave.

      *name* es el nombre de la cabecera a añadir. Se pueden usar
      argumentos por palabra clave para establecer parámetros MIME
      para la cabecera. Cada parámetro debe ser una cadena o "None".
      Todos los guiones bajos en los nombres de parámetros se
      convierten en guiones, dado que los guiones son inválidos en
      identificadores Python y muchos parámetros MIME incluyen
      guiones. Si el valor del parámetro es una cadena, se añade a los
      parámetros del valor de la cabecera con la forma "nombre=valor".
      Si es "None", sólo se añade el nombre del parámetro, para
      reflejar parámetros MIME sin valor. Ejemplo de uso:

         h.add_header('content-disposition', 'attachment', filename='bud.gif')

      El código anterior añadirá una cabecera como la siguiente:

         Content-Disposition: attachment; filename="bud.gif"

   Distinto en la versión 3.5: El parámetro *headers* es opcional.

## "wsgiref.simple_server" -- a simple WSGI HTTP server

Este módulo implementa un servidor HTTP simple, basado en
"http.server", que sirve aplicaciones WSGI. Cada instancia del
servidor sirve una aplicación WSGI simple en una máquina y puerto
dados. Si se quiere servir múltiples aplicaciones en una misma máquina
y puerto, se deberá crear una aplicación WSGI que analiza "PATH_INFO"
para seleccionar qué aplicación invocar para cada petición. Por
ejemplo, usando la función "shift_path_info()" de "wsgiref.util".

wsgiref.simple_server.make_server(host, port, app, server_class=WSGIServer, handler_class=WSGIRequestHandler)

   Crea un nuevo servidor WSGI que sirve en *host* y *port*, aceptando
   conexiones para *app*. El valor de retorno es una instancia de
   *server_class* y procesará peticiones usando *handler_class*. *app*
   debe ser un objeto aplicación WSGI, como se define en **PEP 3333**.

   Ejemplo de uso:

      from wsgiref.simple_server import make_server, demo_app

      with make_server('', 8000, demo_app) as httpd:
          print("Serving HTTP on port 8000...")

          # Respond to requests until process is killed
          httpd.serve_forever()

          # Alternative: serve one request, then exit
          httpd.handle_request()

wsgiref.simple_server.demo_app(environ, start_response)

   This function is a small but complete WSGI application that returns
   a text page containing the message "Hello world!" and a list of the
   key/value pairs provided in the *environ* parameter.  It's useful
   for verifying that a WSGI server (such as "wsgiref.simple_server")
   is able to run a simple WSGI application correctly.

   The *start_response* callable should follow the "StartResponse"
   protocol.

class wsgiref.simple_server.WSGIServer(server_address, RequestHandlerClass)

   Crea una instancia de "WSGIServer". *server_address* debe ser una
   tupla "(máquina,puerto)" y *RequestHandlerClass* debe ser la
   subclase de "http.server.BaseHTTPRequestHandler" que se usará para
   procesar peticiones.

   Normalmente, no es necesario invocar este constructor, ya que la
   función "make_server()" puede gestionar todos los detalles.

   "WSGIServer" es una subclase de "http.server.HTTPServer", por lo
   que todos sus métodos, como "serve_forever()" y "handle_request()",
   están disponibles. "WSGIServer" también ofrece los siguientes
   métodos específicos de WSGI:

   set_app(application)

      Establece el invocable *application* como la aplicación WSGI que
      recibirá las peticiones.

   get_app()

      Retorna la aplicación invocable actualmente establecida.

   Habitualmente, sin embargo, no es necesario usar estos métodos
   adicionales, ya que "set_app()" se llama desde "make_server()" y
   "get_app()" existe sobretodo para el beneficio de instancias del
   gestor de peticiones.

class wsgiref.simple_server.WSGIRequestHandler(request, client_address, server)

   Crea un gestor HTTP para la *request* indicada (es decir un
   socket), *client_address (una tupla ``(máquina,puerto)``), y
   *server* (una instancia "WSGIServer").

   No es necesario crear instancias de esta clase directamente. Se
   crean automáticamente bajo demanda por objetos "WSGIServer". Sin
   embargo, se pueden crear subclases de esta clase y proveerlas como
   *handler_class* a la función "make_server()". Algunos métodos
   posiblemente relevantes para sobreescribir en estas subclases:

   get_environ()

      Retorna un diccionario "WSGIEnvironment" para una petición. La
      implementación por defecto copia el contenido del diccionario
      atributo "base_environ" del objeto "WSGIserver" y añade varias
      cabeceras derivadas de la petición HTTP. Cada llamada a este
      método debe retornar un nuevo diccionario con todas las
      variables de entorno CGI relevantes especificadas en **PEP
      3333**.

   get_stderr()

      Retorna el objeto que debe usarse como el flujo de
      "wsgi.errors". La implementación por defecto retorna simplemente
      "sys.stderr".

   handle()

      Procesa la petición HTTP. La implementación por defecto crea una
      instancia gestora usando una clase "wsgiref.handlers" para
      implementar la interfaz de aplicación WSGI real.

## "wsgiref.validate" --- WSGI conformance checker

When creating new WSGI application objects, frameworks, servers, or
middleware, it can be useful to validate the new code's conformance
using "wsgiref.validate".  This module provides a function that
creates WSGI application objects that validate communications between
a WSGI server or gateway and a WSGI application object, to check both
sides for protocol conformance.

Hay que observar que esta utilidad no garantiza compatibilidad
completa con **PEP 3333**. La ausencia de errores usando este módulo
no implica que no existan errores. Sin embargo, si este módulo produce
errores, implica que o el servidor o la aplicación no son 100%
compatibles.

Este módulo se basa en el módulo "paste.lint" de la librería *Python
Paste* de *Ian Bicking*.

wsgiref.validate.validator(application)

   Envuelve *application* y retorna un nuevo objeto de aplicación
   WSGI. La aplicación retornada reenviará todas las peticiones a la
   *application* original y comprobará que tanto la *application* como
   el servidor que la llama son compatibles con la especificación WSGI
   y con **RFC 2616**.

   Cualquier incompatibilidad detectada provocará el lanzamiento de un
   "AssertionError". Nótese que, sin embargo, cómo se gestionan estos
   errores depende del servidor. Por ejemplo, "wsgiref.simple_server"
   y otros servidores basados en "wsgiref.handlers", que no
   sobreescriben los métodos de gestión de errores para hacer otras
   cosas, simplemente escribirán un mensaje de que el error ha
   ocurrido y volcarán la traza de error en "sys.stderr" o algún otro
   flujo de errores.

   Este *wrapper* puede también generar salidas usando el módulo
   "warnings" para señalar comportamientos que son cuestionables pero
   que no están realmente prohibidos por **PEP 3333**. A no ser que se
   suprima esta salida usando opciones de línea de comandos de Python
   o la API de "warnings", cualquier aviso se escribirá en
   "sys.stderr", en lugar de en "wsgi.errors", aunque sean el mismo
   objeto.

   Ejemplo de uso:

      from wsgiref.validate import validator
      from wsgiref.simple_server import make_server

      # Our callable object which is intentionally not compliant to the
      # standard, so the validator is going to break
      def simple_app(environ, start_response):
          status = '200 OK'  # HTTP Status
          headers = [('Content-type', 'text/plain')]  # HTTP Headers
          start_response(status, headers)

          # This is going to break because we need to return a list, and
          # the validator is going to inform us
          return b"Hello World"

      # This is the application wrapped in a validator
      validator_app = validator(simple_app)

      with make_server('', 8000, validator_app) as httpd:
          print("Listening on port 8000....")
          httpd.serve_forever()

## "wsgiref.handlers" -- server/gateway base classes

Este módulo ofrece clases gestoras base para implementar servidores y
*gateways* WSGI. Estas clases base gestionan la mayoría del trabajo de
comunicarse con una aplicación WSGI, siempre que se les dé un entorno
CGI, junto con una entrada, una salida, y un flujo de errores.

class wsgiref.handlers.CGIHandler

   Invocación basada en CGI vía "sys.stdin", "sys.stdout",
   "sys.stderr" y "os.environ". Esto es útil cuando se quiere ejecutar
   una aplicación WSGI como un script CGI. Simplemente es necesario
   invocar "CGIHandler().run(app)", donde "app" es el objeto de
   aplicación WSGI que se quiere invocar.

   Esta clase es una subclase de "BaseCGIHandler" que establece
   "wsgi.run_once" a cierto, "wsgi.multithread" a falso, y
   "wsgi.multiprocess" a cierto, y siempre usa "sys" y "os" para
   obtener los flujos y entorno CGI necesarios.

class wsgiref.handlers.IISCGIHandler

   Una alternativa especializada a "CGIHandler", para usar al
   desplegar en servidores web Microsoft IIS, sin establecer la opción
   de configuración "allowPathInfo" (IIS>=7) o la meta-base
   "allowPathInfoForScriptMappings" (IIS<7).

   Por defecto, IIS entrega "PATH_INFO" que duplica "SCRIPT_NAME" al
   principio, causando problemas con aplicaciones WSGI que implementan
   enrutamiento. Este gestor elimina las partes duplicadas de la ruta.

   IIS se puede configurar para pasar el "PATH_INFO" correcto, pero
   esto causa otro error donde "PATH_TRANSLATED" es incorrecto.
   Afortunadamente, esta variable rara vez se usa y no está
   garantizada por WSGI. Sin embargo, en IIS<7, la configuración solo
   se puede realizar en un nivel de vhost, lo que afecta a todas las
   demás asignaciones de scripts, muchas de las cuales se rompen
   cuando se exponen al error "PATH_TRANSLATED". Por esta razón, IIS<7
   casi nunca se implementa con la solución (incluso IIS7 rara vez lo
   usa porque todavía no tiene una interfaz de usuario).

   No hay forma de que el código CGI detecte cuándo la opción está
   activada, por lo que se ofrece una clase gestora separada. Se usa
   de la misma forma que "CGIHandler", p.e. llamando a
   "IISCGIHandler().run(app)", donde "app" es el objeto aplicación
   WSGI que se desea invocar.

   Added in version 3.2.

class wsgiref.handlers.BaseCGIHandler(stdin, stdout, stderr, environ, multithread=True, multiprocess=False)

   Similar a "CGIHandler", pero en lugar de usar los módulos "sys" y
   "os", el entorno CGI y los flujos de E/S se especifican
   explícitamente. Los valores *multithread* y *multiprocess* se pasan
   a las aplicaciones ejecutadas por la instancia de gestión como
   "wsgi.multithread" y "wsgi.multiprocess".

   Esta clase es una subclase de "SimpleHandler" para usarse con
   servidores HTTP que no reciben peticiones directas de Internet,
   *HTTP origin servers*. Al escribir una implementación de un
   protocolo de pasarela, como CGI, FastCGI, SCGI, etcétera, que use
   una cabecera "Status:" para enviar un estado HTTP, probablemente
   sea adecuado heredar de esta clase, en lugar de "SimpleHandler".

class wsgiref.handlers.SimpleHandler(stdin, stdout, stderr, environ, multithread=True, multiprocess=False)

   Similar a "BaseCGIHandler" pero diseñada para usarse con servidores
   que reciban peticiones directamente de Internet, o *HTTP origin
   servers*. Al escribir una implementación de un servidor HTTP,
   probablemente prefiera heredar de esta clase en lugar de
   "BaseCGIHandler".

   This class is a subclass of "BaseHandler".  It overrides the
   "__init__()", "get_stdin()", "get_stderr()", "add_cgi_vars()",
   "_write()", and "_flush()" methods to support explicitly setting
   the environment and streams via the constructor.  The supplied
   environment and streams are stored in the "stdin", "stdout",
   "stderr", and "environ" attributes.

   El método "write()" de *stdout* podría escribir cada fragmento de
   información completamente, como "io.BufferedIOBase".

class wsgiref.handlers.BaseHandler

   Esta es una clase base abstracta para ejecutar aplicaciones WSGI.
   Cada instancia gestionará una sola petición HTTP, aunque en
   principio se podría crear una subclase reutilizable para múltiples
   peticiones.

   Las instancias de "BaseHandler" tiene un sólo método para uso
   externo:

   run(app)

      Ejecuta la aplicación WSGI *app* indicada.

   Todos los otros métodos de "BaseHandler" se invocan por este método
   en el proceso de ejecutar la aplicación, es decir, existen
   principalmente para permitir personalizar el proceso.

   Los métodos siguientes DEBEN sobrescribirse en una subclase:

   _write(data)

      Enviar los bytes *data* para la transmisión al cliente. Es
      correcto que este método realmente transmita la información. La
      clase "BaseHandler" simplemente separa las operaciones de
      escritura y liberación para una mayor eficiencia cuando el
      sistema subyacente realmente hace esa distinción.

   _flush()

      Forzar la transmisión de los datos en el búfer al cliente. Es
      correcto si este método no es operativo, p.e., si "_write()"
      realmente envía los datos.

   get_stdin()

      Retorna un objeto compatible con "InputStream", apropiado para
      usar como "wsgi.input" de la petición en proceso actualmente.

   get_stderr()

      Retorna un objeto compatible con "ErrorStream", apropiado para
      usar como "wsgi.errors" de la petición en proceso actualmente.

   add_cgi_vars()

      Inserta las variables CGI para la petición actual en el atributo
      "environ".

   A continuación se describen algunos métodos y atributos más que
   podría ser interesante sobrescribir. Esta lista es sólo un sumario,
   sin embargo, y no incluye cada método que puede ser sobrescrito.
   Conviene consultar las docstrings y el código fuente para obtener
   información adicional antes de intentar crear una subclase de
   "BaseHandler" personalizada.

   Atributos y métodos para personalizar el entorno WSGI:

   wsgi_multithread

      El valor a usar en la variable de entorno "wsgi.multithread".
      Por defecto es cierto en "BaseHandler", pero puede tener un
      valor por defecto distinto (o establecerse en el constructor) en
      otras subclases.

   wsgi_multiprocess

      El valor a usar en la variable de entorno "wsgi.multiprocess".
      Por defecto es cierto en "BaseHandler", pero puede tener un
      valor por defecto distinto (o establecerse en el constructor) en
      otras subclases.

   wsgi_run_once

      El valor a usar en la variable de entorno "wsgi.run_once". Por
      defecto es falso en "BaseHandler", pero en "CGIHandler" es
      cierto por defecto.

   os_environ

      The default environment variables to be included in every
      request's WSGI environment.  By default, this is a copy of
      "os.environ" at the time that "wsgiref.handlers" was imported,
      but subclasses can either create their own at the class or
      instance level.  Note that the dictionary should be considered
      read-only, since the default value is shared between multiple
      classes and instances.

   server_software

      Si el atributo "origin_server" tiene valor, éste se usa para
      establecer el valor por defecto de la variable de entorno WSGI
      "SERVER_SOFTWARE" y un cabecera "Server:" por defecto en las
      respuestas HTTP. Las clases gestoras que no son *HTTP origin
      servers*, como "BaseCGIHandler" y "CGIHandler", ignoran este
      atributo.

      Distinto en la versión 3.3: El término "Python" se reemplaza con
      el término específico correspondiente a la implementación del
      intérprete, como "CPython", "Jython", etc.

   get_scheme()

      Retorna el esquema usado en la URL para la petición actual. La
      implementación por defecto utiliza la función "guess_scheme()"
      de "wsgiref.util" para adivinar si el esquema debería ser "http"
      o "https", basándose en las variables de "environ" de la
      petición actual.

   setup_environ()

      Establece el atributo "environ" a un entorno WSGI completo. La
      implementación por defecto utiliza todos los métodos y atributos
      anteriormente mencionados, más los métodos "get_stdin()",
      "get_stderr()" y "add_cgi_vars()", y el atributo
      "wsgi_file_wrapper". También incluye una clave "SERVER_SOFTWARE"
      si no existe, siempre y cuando el atributo "origin_server" tiene
      un valor válido y el atributo "server_software" está
      establecido.

   Métodos y atributos para personalizar el manejo de excepciones:

   log_exception(exc_info)

      Envía la tupla *exc_info* al registro del servidor. *exc_info*
      es un tupla "(type, value, traceback)". La implementación por
      defecto simplemente escribe el seguimiento de la pila en el
      flujo "wsgi.errors" de la petición y lo vacía. Las subclases
      pueden sobrescribir éste método para cambiar el formato o
      redirigir la salida, enviar mensajes de correo con el
      seguimiento de pila a un administrador o cualquier otra acción
      que se considere adecuada.

   traceback_limit

      El máximo número de marcos a incluir en la salida de
      seguimientos de pilas por el método por defecto
      "log_exception()". Si vale "None", se incluyen todos los marcos.

   error_output(environ, start_response)

      Este método es una aplicación WSGI para generar una página de
      error para el usuario. Sólo se invoca si un error ocurre antes
      de enviar las cabeceras al cliente.

      This method can access the current error using
      "sys.exception()", and should pass that information to
      *start_response* when calling it (as described in the "Error
      Handling" section of **PEP 3333**). In particular, the
      *start_response* callable should follow the "StartResponse"
      protocol.

      La implementación por defecto sólo utiliza los atributos
      "error_status", "error_headers" y "error_body" para generar una
      página de salida. Las subclases pueden sobrescribir éste para
      producir una salida de error dinámica mejor.

      Hay que tener en cuenta, sin embargo, que no se recomienda,
      desde una perspectiva de seguridad, mostrar información de
      diagnóstico a cualquier usuario antiguo. Idealmente, se debería
      hacer algo especial para activar la salida de información de
      diagnóstico, motivo por el que la implementación por defecto no
      incluye ninguna.

   error_status

      El estado HTTP utilizado para las respuestas de error. Se
      debería utilizar una de las cadenas de estado definidas en **PEP
      3333**. Por defecto es un código 500 y un mensaje.

   error_headers

      Las cabeceras HTTP utilizadas por las respuestas de error.
      Debería tratarse de una lista de cabeceras de respuesta WSGI
      (tuplas "(name, value)"), tal y como se describe en **PEP
      3333**. La lista por defecto simplemente establece el tipo de
      contenido a "text/plain".

   error_body

      El cuerpo de la respuesta de error. Debería ser una cadena de
      bytes con el cuerpo de la respuesta HTTP. Por defecto contiene
      el texto plano *A server error occurred. Please contact the
      administrator.*

   Métodos y atributos para la funcionalidad "Optional Platform-
   Specific File Handling" de **PEP 3333**:

   wsgi_file_wrapper

      Una fábrica "wsgi.file_wrapper" compatible con
      "wsgiref.types.FileWrapper", o "None". El valor por defecto de
      este atributo es la clase "wsgiref.util.FileWrapper".

   sendfile()

      Sobrescribir para implementar la transmisión de ficheros
      específica para la plataforma. Este método se llama sólo si el
      valor de retorno de la aplicación es una instancia de la clase
      especificada por el atributo "wsgi_file_wrapper". Debería
      retornar un valor cierto si fue capaz de transmitir
      correctamente el fichero, de modo que el código por defecto de
      transmisión no será ejecutado. La implementación por defecto de
      este método simplemente retorna un valor falso.

   Métodos y atributos varios:

   origin_server

      Este atributo debería establecerse a cierto si los métodos
      "_write()" y "_flush()" están siendo usados para comunicar
      directamente al cliente, en lugar de usar un protocolo de
      pasarela CGI que requiere el estado HTTP en una cabecera
      "Status:" especial.

      El valor por defecto de este atributo es cierto en
      "BaseHandler", pero en "BaseCGIHandler" y "CGIHandler" es falso.

   http_version

      Si "origin_server" es cierto, este atributo de tipo cadena se
      usa para establecer la versión HTTP de la respuesta enviada al
      cliente. Por defecto es ""1.0"".

wsgiref.handlers.read_environ()

   Transcodifica las variables CGI de "os.environ" a cadenas "bytes in
   unicode" definidas en **PEP 3333**, retornando un nuevo
   diccionario. Esta función se usa en "CGIHandler" y "IISCGIHandler"
   en lugar de usar directamente "os.environ", lo que no es
   necesariamente compatible con EWGI en todas las plataformas y
   servidores web usando Python 3 -- específicamente, aquellas en las
   que el entorno actual del sistema operativo es Unicode, p.e.
   Windows, o en las que el entorno está en bytes, pero la
   codificación del sistema usada por Python para descodificar lo es
   cualquier otro que ISO-8859-1, por ejemplo, sistemas UNIX que usen
   UTF-8.

   Cuando se está implementando un gestor basado en CGI propio,
   probablemente se requiera usar esta rutina en lugar de sólo copiar
   directamente los valores de "os.environ".

   Added in version 3.2.

## "wsgiref.types" -- WSGI types for static type checking

Este módulo provee varios tipos para validadores estáticos de tipos,
como se describe en **PEP 3333**.

Added in version 3.11.

class wsgiref.types.StartResponse

   A "typing.Protocol" describing **start_response()** callables
   (**PEP 3333**).

wsgiref.types.WSGIEnvironment

   Un alias de tipo que describe un diccionario de entorno WSGI.

wsgiref.types.WSGIApplication

   Un alias de tipo que describe una aplicación WSGI invocable.

class wsgiref.types.InputStream

   A "typing.Protocol" describing a **WSGI Input Stream**.

class wsgiref.types.ErrorStream

   A "typing.Protocol" describing a **WSGI Error Stream**.

class wsgiref.types.FileWrapper

   A "typing.Protocol" describing a **file wrapper**. See
   "wsgiref.util.FileWrapper" for a concrete implementation of this
   protocol.

## Ejemplos

This is a working "Hello World" WSGI application, where the
*start_response* callable should follow the "StartResponse" protocol:

   """
   Every WSGI application must have an application object - a callable
   object that accepts two arguments. For that purpose, we're going to
   use a function (note that you're not limited to a function, you can
   use a class for example). The first argument passed to the function
   is a dictionary containing CGI-style environment variables and the
   second variable is the callable object.
   """
   from wsgiref.simple_server import make_server

   def hello_world_app(environ, start_response):
       status = "200 OK"  # HTTP Status
       headers = [("Content-type", "text/plain; charset=utf-8")]  # HTTP Headers
       start_response(status, headers)

       # The returned object is going to be printed
       return [b"Hello World"]

   with make_server("", 8000, hello_world_app) as httpd:
       print("Serving on port 8000...")

       # Serve until process is killed
       httpd.serve_forever()

Ejemplo de una aplicación WSGI que sirve el directorio actual, acepta
un directorio opcional y un número de puerto (default: 8000) en la
línea de comandos:

   """
   Small wsgiref based web server. Takes a path to serve from and an
   optional port number (defaults to 8000), then tries to serve files.
   MIME types are guessed from the file names, 404 errors are raised
   if the file is not found.
   """
   import mimetypes
   import os
   import sys
   from wsgiref import simple_server, util

   def app(environ, respond):
       # Get the file name and MIME type
       fn = os.path.join(path, environ["PATH_INFO"][1:])
       if "." not in fn.split(os.path.sep)[-1]:
           fn = os.path.join(fn, "index.html")
       mime_type = mimetypes.guess_file_type(fn)[0]

       # Return 200 OK if file exists, otherwise 404 Not Found
       if os.path.exists(fn):
           respond("200 OK", [("Content-Type", mime_type)])
           return util.FileWrapper(open(fn, "rb"))
       else:
           respond("404 Not Found", [("Content-Type", "text/plain")])
           return [b"not found"]

   if __name__ == "__main__":
       # Get the path and port from command-line arguments
       path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
       port = int(sys.argv[2]) if len(sys.argv) > 2 else 8000

       # Make and start the server until control-c
       httpd = simple_server.make_server("", port, app)
       print(f"Serving {path} on port {port}, control-C to stop")
       try:
           httpd.serve_forever()
       except KeyboardInterrupt:
           print("Shutting down.")
           httpd.server_close()
