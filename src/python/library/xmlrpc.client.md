---
title: '"xmlrpc.client" --- XML-RPC client access'
source_url: https://docs.python.org/es/3
source_path: library/xmlrpc.client.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4660
---

# "xmlrpc.client" --- XML-RPC client access

**Source code:** Lib/xmlrpc/client.py

======================================================================

XML-RPC es un método de llamada a procedimiento remoto que utiliza XML
pasado a través de HTTP(S) como transporte. Con él, un cliente puede
llamar a métodos con parámetros en un servidor remoto (el servidor es
nombrado por un URI) y recuperar datos estructurados. Este módulo
admite la escritura de código de cliente XML-RPC; maneja todos los
detalles de la traducción entre objetos de Python conformes y XML en
el cable.

Advertencia:

  The "xmlrpc.client" module is not secure against maliciously
  constructed data.  If you need to parse untrusted or unauthenticated
  data, see XML security.

Distinto en la versión 3.5: For HTTPS URIs, "xmlrpc.client" now
performs all the necessary certificate and hostname checks by default.

Availability: not WASI.

This module does not work or is not available on WebAssembly. See
Plataformas WebAssembly for more information.

class xmlrpc.client.ServerProxy(uri, transport=None, encoding=None, verbose=False, allow_none=False, use_datetime=False, use_builtin_types=False, *, headers=(), context=None)

   Una "ServerProxy" instancia un objeto que gestiona la comunicación
   con un servidor XML-RPC remoto. El primer argumento requerido es un
   URI (*Uniform Resource Indicator*) y normalmente será la URL del
   servidor. El segundo argumento opcional es una instancia de fábrica
   de transporte; de forma predeterminada, es una instancia interna
   "SafeTransport" para https: URL y una instancia interna HTTP
   "Transport" en caso contrario. El tercer argumento opcional es una
   codificación, por defecto UTF-8. El cuarto argumento opcional es un
   indicador de depuración.

   The following parameters govern the use of the returned proxy
   instance. If *allow_none* is true,  the Python constant "None" will
   be translated into XML; the default behaviour is for "None" to
   raise a "TypeError". This is a commonly used extension to the XML-
   RPC specification, but isn't supported by all clients and servers;
   see http://ontosys.com/xml-rpc/extensions.php for a description.
   The *use_builtin_types* flag can be used to cause date/time values
   to be presented as "datetime.datetime" objects and binary data to
   be presented as "bytes" objects; this flag is false by default.
   "datetime.datetime", "bytes" and "bytearray" objects may be passed
   to calls. The *headers* parameter is an optional sequence of HTTP
   headers to send with each request, expressed as a sequence of
   2-tuples representing the header name and value. (e.g. "[('Header-
   Name', 'value')]"). If an HTTPS URL is provided, *context* may be
   "ssl.SSLContext" and configures the SSL settings of the underlying
   HTTPS connection. The obsolete *use_datetime* flag is similar to
   *use_builtin_types* but it applies only to date/time values.

   Distinto en la versión 3.3: La opción *use_builtin_types* fue
   añadida.

   Distinto en la versión 3.8: El parámetro *headers* fue añadida.

   Both the HTTP and HTTPS transports support the URL syntax extension
   for HTTP Basic Authentication: "http://user:pass@host:port/path".
   The  "user:pass" portion will be base64-encoded as an HTTP
   'Authorization' header, and sent to the remote server as part of
   the connection process when invoking an XML-RPC method.  You only
   need to use this if the remote server requires a Basic
   Authentication user and password.

   La instancia retornada es un objeto proxy con métodos que se pueden
   utilizar para invocar las correspondientes llamadas RPC en el
   servidor remoto. Si el servidor remoto admite la API de
   introspección, el proxy también se puede utilizar para consultar al
   servidor remoto los métodos que admite (descubrimiento de
   servicios) y recuperar otros metadatos asociados al servidor.

   Los tipos que son conformes (por ejemplo, que se pueden clasificar
   a través de XML) incluyen lo siguiente (y, excepto donde se
   indique, no se clasifican como el mismo tipo de Python):

   +------------------------+---------------------------------------------------------+
   | Tipo XML-RPC           | Tipo de Python                                          |
   |========================|=========================================================|
   | "boolean"              | "bool"                                                  |
   +------------------------+---------------------------------------------------------+
   | "int", "i1", "i2",     | "int" en el rango de -2147483648 a 2147483647. Los      |
   | "i4", "i8" or          | valores obtienen la etiqueta "<int>" .                  |
   | "biginteger"           |                                                         |
   +------------------------+---------------------------------------------------------+
   | "double" o "float"     | "float".  Los valores obtienen la etiqueta "<double>".  |
   +------------------------+---------------------------------------------------------+
   | "string"               | "str"                                                   |
   +------------------------+---------------------------------------------------------+
   | "array"                | "list" o "tuple" que contiene elementos determinados.   |
   |                        | Las matrices se retornan como "lists".                  |
   +------------------------+---------------------------------------------------------+
   | "struct"               | "dict". Las claves deben ser cadenas de caracteres, los |
   |                        | valores pueden ser de cualquier tipo determinado.       |
   |                        | Pueden pasarse objetos de clases definidas por el       |
   |                        | usuario; sólo se transmite su atributo "__dict__" .     |
   +------------------------+---------------------------------------------------------+
   | "dateTime.iso8601"     | "DateTime" o "datetime.datetime". El tipo retornado     |
   |                        | depende de los valores de los indicadores               |
   |                        | *use_builtin_types* y *use_datetime* .                  |
   +------------------------+---------------------------------------------------------+
   | "base64"               | "Binary", "bytes" o "bytearray". El tipo retornado      |
   |                        | depende del valor de la marca *use_builtin_types*.      |
   +------------------------+---------------------------------------------------------+
   | "nil"                  | La constante "None". Solo se permite pasar si           |
   |                        | *allow_none* es verdadero.                              |
   +------------------------+---------------------------------------------------------+
   | "bigdecimal"           | "decimal.Decimal". Retornado solo el tipo.              |
   +------------------------+---------------------------------------------------------+

   Este es el conjunto completo de tipos de datos admitidos por XML-
   RPC. Las llamadas a métodos también pueden generar una instancia
   especial "Fault", que se usa para señalar errores del servidor XML-
   RPC, o "ProtocolError" que se usa para señalar un error en la capa
   de transporte HTTP/HTTPS. Ambos "Fault" y "ProtocolError" derivan
   de una clase base llamada "Error". Tenga en cuenta que el módulo de
   cliente xmlrpc actualmente no clasifica instancias de subclases de
   tipos integrados.

   Al pasar cadenas de caracteres, los caracteres especiales de XML
   como "<", ">" y "&" se escaparán automáticamente. Sin embargo, es
   responsabilidad de la persona que llama asegurarse de que la cadena
   de caracteres esté libre de caracteres que no están permitidos en
   XML, como los caracteres de control con valores ASCII entre 0 y 31
   (excepto, por supuesto, tabulación, nueva línea y retorno de
   carro); no hacer esto resultará en una solicitud XML-RPC que no es
   XML bien formado. Si tiene que pasar bytes arbitrarios a través de
   XML-RPC, use las clases "bytes" o "bytearray" o la clase
   contenedora "Binary" descrita a continuación.

   "Server" se conserva como un alias para "ServerProxy" para
   compatibilidad con versiones anteriores. El nuevo código debe usar
   "ServerProxy".

   Distinto en la versión 3.5: Se agregó el argumento *context*.

   Distinto en la versión 3.6: Se agregó soporte para etiquetas de
   tipo con prefijos (por ejemplo. "ex:nil"). Se agregó soporte para
   desagrupar los tipos adicionales utilizados por la implementación
   Apache XML-RPC para números: "i1", "i2", "i8", "biginteger",
   "float" y "bigdecimal". Consulte
   http://ws.apache.org/xmlrpc/types.html para obtener una
   descripción.

Ver también:

  XML-RPC HOWTO
     Una buena descripción del funcionamiento de XML-RPC y del
     software cliente en varios idiomas. Contiene prácticamente todo
     lo que un desarrollador de cliente XML-RPC necesita saber.

  XML-RPC Introspection
     Describe la extensión del protocolo XML-RPC para la
     introspección.

  XML-RPC Specification
     La especificación oficial.

## Objetos *ServerProxy*

La instancia de "ServerProxy" tiene un método correspondiente a cada
llamada de procedimiento remoto aceptada por el servidor XML-RPC.
Llamar al método realiza un RPC, enviado por nombre y firma de
argumento (por ejemplo, el mismo nombre de método puede sobrecargarse
con múltiples firmas de argumento). El RPC finaliza retornando un
valor, que puede ser datos retornados en un tipo conforme o un objeto
"Fault" o "ProtocolError" que indica un error.

Los servidores que admiten la API de introspección XML admiten algunos
métodos comunes agrupados bajo el atributo reservado "system":

ServerProxy.system.listMethods()

   Este método retorna una lista de cadenas, una para cada método (que
   no es del sistema) admitido por el servidor XML-RPC.

ServerProxy.system.methodSignature(name)

   Este método toma un parámetro, el nombre de un método implementado
   por el servidor XML-RPC. Retorna una matriz de posibles firmas para
   este método. Una firma es una variedad de tipos. El primero de
   estos tipos es el tipo de retorno del método, el resto son
   parámetros.

   Debido a que se permiten múltiples firmas (es decir, sobrecarga),
   este método retorna una lista de firmas en lugar de un singleton.

   Las propias firmas están restringidas a los parámetros de nivel
   superior esperados por un método. Por ejemplo, si un método espera
   una matriz de estructuras como parámetro y retorna una cadena de
   caracteres, su firma es simplemente "cadena, matriz". Si espera
   tres enteros y retorna una cadena, su firma es "string, int, int,
   int".

   Si no se define una firma para el método, se retorna un valor que
   no es una matriz. En Python, esto significa que el tipo de valor
   retornado será diferente a una lista.

ServerProxy.system.methodHelp(name)

   Este método toma un parámetro, el nombre de un método implementado
   por el servidor XML-RPC. Retorna una cadena de caracteres de
   documentación que describe el uso de ese método. Si no hay tal
   cadena de caracteres disponible, se retorna una cadena de
   caracteres vacía. La cadena de caracteres de documentación puede
   contener marcado HTML.

Distinto en la versión 3.5: Las instancias de "ServerProxy" admiten el
protocolo *context manager* para cerrar el transporte subyacente.

A continuación se muestra un ejemplo práctico. El código del servidor:

   from xmlrpc.server import SimpleXMLRPCServer

   def is_even(n):
       return n % 2 == 0

   server = SimpleXMLRPCServer(("localhost", 8000))
   print("Listening on port 8000...")
   server.register_function(is_even, "is_even")
   server.serve_forever()

El código de cliente para el servidor anterior:

   import xmlrpc.client

   with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
       print("3 is even: %s" % str(proxy.is_even(3)))
       print("100 is even: %s" % str(proxy.is_even(100)))

## Objetos *DateTime*

class xmlrpc.client.DateTime

   Esta clase puede inicializarse con segundos desde la época, una
   tupla de tiempo, una cadena de fecha/hora ISO 8601 o una instancia
   "datetime.datetime". Tiene los siguientes métodos, soportados
   principalmente para uso interno por el código de
   clasificación/eliminación de clasificación:

   decode(string)

      Acepta una cadena de caracteres como el nuevo valor de tiempo de
      la instancia.

   encode(out)

      Escribe la codificación XML-RPC de este elemento "DateTime" en
      el objeto de flujo *out*.

   It also supports certain of Python's built-in operators through
   "rich comparison" and "__repr__()" methods.

A continuación se muestra un ejemplo práctico. El código del servidor:

   import datetime as dt
   from xmlrpc.server import SimpleXMLRPCServer
   import xmlrpc.client

   def today():
       today = dt.datetime.today()
       return xmlrpc.client.DateTime(today)

   server = SimpleXMLRPCServer(("localhost", 8000))
   print("Listening on port 8000...")
   server.register_function(today, "today")
   server.serve_forever()

El código de cliente para el servidor anterior:

   import xmlrpc.client
   import datetime as dt

   proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

   today = proxy.today()
   # convert the ISO 8601 string to a datetime object
   converted = dt.datetime.strptime(today.value, "%Y%m%dT%H:%M:%S")
   print(f"Today: {converted.strftime('%d.%m.%Y, %H:%M')}")

## Objetos binarios

class xmlrpc.client.Binary

   Esta clase puede inicializarse a partir de datos de bytes (que
   pueden incluir NUL). El acceso principal al contenido de un objeto
   "Binary" lo proporciona un atributo:

   data

      Los datos binarios encapsulados por la instancia "Binary". Los
      datos se proporcionan como un objeto "bytes".

   Los objetos "Binary" tienen los siguientes métodos, soportados
   principalmente para uso interno por el código de
   clasificación/desagrupación:

   decode(bytes)

      Acepta un objeto base64 "bytes" y se descodifica como los nuevos
      datos de la instancia.

   encode(out)

      Escribe la codificación XML-RPC base 64 de este elemento binario
      en el objeto de flujo *out*.

      Los datos codificados tendrán líneas nuevas cada 76 caracteres
      según RFC 2045 sección 6.8 **RFC 2045 Section 6.8**, que era la
      especificación estándar de facto base64 cuando se escribió la
      especificación XML-RPC.

   It also supports certain of Python's built-in operators through
   "__eq__()" and "__ne__()" methods.

Ejemplo de uso de los objetos binarios. Vamos a transferir una imagen
sobre XMLRPC:

   from xmlrpc.server import SimpleXMLRPCServer
   import xmlrpc.client

   def python_logo():
       with open("python_logo.jpg", "rb") as handle:
           return xmlrpc.client.Binary(handle.read())

   server = SimpleXMLRPCServer(("localhost", 8000))
   print("Listening on port 8000...")
   server.register_function(python_logo, 'python_logo')

   server.serve_forever()

El cliente obtiene la imagen y la guarda en un archivo:

   import xmlrpc.client

   proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
   with open("fetched_python_logo.jpg", "wb") as handle:
       handle.write(proxy.python_logo().data)

## Objetos Faults

class xmlrpc.client.Fault

   Un objeto "Fault" encapsula el contenido de una etiqueta de error
   XML-RPC. Los objetos de error tienen los siguientes atributos:

   faultCode

      Un entero que indica el tipo de falla.

   faultString

      Una cadena de caracteres que contiene un mensaje de diagnóstico
      asociado con el fallo.

En el siguiente ejemplo vamos a causar intencionalmente un "Fault" al
retornar un objeto de tipo complejo. El código del servidor:

   from xmlrpc.server import SimpleXMLRPCServer

   # A marshalling error is going to occur because we're returning a
   # complex number
   def add(x, y):
       return x+y+0j

   server = SimpleXMLRPCServer(("localhost", 8000))
   print("Listening on port 8000...")
   server.register_function(add, 'add')

   server.serve_forever()

El código de cliente para el servidor anterior:

   import xmlrpc.client

   proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
   try:
       proxy.add(2, 5)
   except xmlrpc.client.Fault as err:
       print("A fault occurred")
       print("Fault code: %d" % err.faultCode)
       print("Fault string: %s" % err.faultString)

## Objetos ProtocolError

class xmlrpc.client.ProtocolError

   El objeto "ProtocolError" describe un error de protocolo en la capa
   de transporte subyacente (como un error 404 'no encontrado' si el
   servidor nombrado por el URI no existe). Tiene los siguientes
   atributos:

   url

      El URI o URL que provocó el error.

   errcode

      El código de error.

   errmsg

      El mensaje de error o la cadena de caracteres de diagnóstico.

   headers

      Un diccionario que contiene los encabezados de la solicitud
      HTTP/HTTPS que desencadenó el error.

En el siguiente ejemplo, vamos a causar intencionalmente un
"ProtocolError" proporcionando un URI inválido:

   import xmlrpc.client

   # create a ServerProxy with a URI that doesn't respond to XMLRPC requests
   proxy = xmlrpc.client.ServerProxy("http://google.com/")

   try:
       proxy.some_method()
   except xmlrpc.client.ProtocolError as err:
       print("A protocol error occurred")
       print("URL: %s" % err.url)
       print("HTTP/HTTPS headers: %s" % err.headers)
       print("Error code: %d" % err.errcode)
       print("Error message: %s" % err.errmsg)

## Objetos MultiCall

El objeto "MultiCall" proporciona una forma de encapsular múltiples
llamadas a un servidor remoto en una sola solicitud [1].

class xmlrpc.client.MultiCall(server)

   Crea un objeto usado para llamadas al método boxcar. *server* es el
   objetivo final de la llamada. Se pueden realizar llamadas al objeto
   de resultado, pero retornarán inmediatamente "None" y solo
   almacenarán el nombre y los parámetros de la llamada en el objeto
   "MultiCall". Llamar al objeto en sí hace que todas las llamadas
   almacenadas se transmitan como una única solicitud de
   "system.multicall". El resultado de esta llamada es un *generator*;
   iterar sobre este generador produce los resultados individuales.

A continuación se muestra un ejemplo de uso de esta clase. El código
del servidor:

   from xmlrpc.server import SimpleXMLRPCServer

   def add(x, y):
       return x + y

   def subtract(x, y):
       return x - y

   def multiply(x, y):
       return x * y

   def divide(x, y):
       return x // y

   # A simple server with simple arithmetic functions
   server = SimpleXMLRPCServer(("localhost", 8000))
   print("Listening on port 8000...")
   server.register_multicall_functions()
   server.register_function(add, 'add')
   server.register_function(subtract, 'subtract')
   server.register_function(multiply, 'multiply')
   server.register_function(divide, 'divide')
   server.serve_forever()

El código de cliente para el servidor anterior:

   import xmlrpc.client

   proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
   multicall = xmlrpc.client.MultiCall(proxy)
   multicall.add(7, 3)
   multicall.subtract(7, 3)
   multicall.multiply(7, 3)
   multicall.divide(7, 3)
   result = multicall()

   print("7+3=%d, 7-3=%d, 7*3=%d, 7//3=%d" % tuple(result))

## Funciones de Conveniencia

xmlrpc.client.dumps(params, methodname=None, methodresponse=None, encoding=None, allow_none=False)

   Convert *params* into an XML-RPC request, or into a response if
   *methodresponse* is true. *params* can be either a tuple of
   arguments or an instance of the "Fault" exception class.  If
   *methodresponse* is true, only a single value can be returned,
   meaning that *params* must be of length 1. *encoding*, if supplied,
   is the encoding to use in the generated XML; the default is UTF-8.
   Python's "None" value cannot be used in standard XML-RPC; to allow
   using it via an extension,  provide a true value for *allow_none*.

xmlrpc.client.loads(data, use_datetime=False, use_builtin_types=False)

   Convierte una solicitud o respuesta XML-RPC en objetos Python, un
   "(params, methodname)".  *params* es una tupla de argumento;
   *methodname* es una cadena de caracteres, o "None" si no hay ningún
   nombre de método presente en el paquete. Si el paquete XML-RPC
   representa una condición de falla, esta función lanzará una
   excepción "Fault". La opción *use_builtin_types* puede usarse para
   hacer que los valores de fecha/hora se presenten como objetos de
   "datetime.datetime" y datos binarios que se presenten como objetos
   de "bytes"; esta opción es falsa por defecto.

   La opción obsoleta *use_datetime* es similar a *use_builtin_types*
   pero esto aplica solo a valores fecha/hora.

   Distinto en la versión 3.3: La opción *use_builtin_types* fue
   añadida.

## Ejemplo de uso de cliente

   # simple test program (from the XML-RPC specification)
   from xmlrpc.client import ServerProxy, Error

   # server = ServerProxy("http://localhost:8000") # local server
   with ServerProxy("http://betty.userland.com") as proxy:

       print(proxy)

       try:
           print(proxy.examples.getStateName(41))
       except Error as v:
           print("ERROR", v)

Para acceder a un servidor XML-RPC a través de un proxy HTTP, debe
definir un transporte personalizado. El siguiente ejemplo muestra
cómo:

   import http.client
   import xmlrpc.client

   class ProxiedTransport(xmlrpc.client.Transport):

       def set_proxy(self, host, port=None, headers=None):
           self.proxy = host, port
           self.proxy_headers = headers

       def make_connection(self, host):
           connection = http.client.HTTPConnection(*self.proxy)
           connection.set_tunnel(host, headers=self.proxy_headers)
           self._connection = host, connection
           return connection

   transport = ProxiedTransport()
   transport.set_proxy('proxy-server', 8080)
   server = xmlrpc.client.ServerProxy('http://betty.userland.com', transport=transport)
   print(server.examples.getStateName(41))

## Ejemplo de uso de cliente y servidor

Vea SimpleXMLRPCServer example.

-[ Notas al pie ]-

[1] Este enfoque se presentó por primera vez en una discusión en
    xmlrpc.com.
