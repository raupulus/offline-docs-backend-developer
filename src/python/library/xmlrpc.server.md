---
title: '"xmlrpc.server" --- Basic XML-RPC servers'
source_url: https://docs.python.org/es/3
source_path: library/xmlrpc.server.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4670
---

# "xmlrpc.server" --- Basic XML-RPC servers

**Código fuente:** Lib/xmlrpc/server.py

======================================================================

The "xmlrpc.server" module provides a basic server framework for XML-
RPC servers written in Python.  Servers can either be free standing,
using "SimpleXMLRPCServer", or embedded in a CGI environment, using
"CGIXMLRPCRequestHandler".

Advertencia:

  The "xmlrpc.server" module is not secure against maliciously
  constructed data.  If you need to parse untrusted or unauthenticated
  data, see XML security.

Availability: not WASI.

This module does not work or is not available on WebAssembly. See
Plataformas WebAssembly for more information.

class xmlrpc.server.SimpleXMLRPCServer(addr, requestHandler=SimpleXMLRPCRequestHandler, logRequests=True, allow_none=False, encoding=None, bind_and_activate=True, use_builtin_types=False)

   Crea una nueva instancia de servidor. Esta clase proporciona
   métodos para el registro de funciones que pueden ser llamados por
   el protocolo XML-RPC. El parámetro *requestHandler* debe ser un
   generador para las instancias del controlador de solicitudes; el
   valor predeterminado es "SimpleXMLRPCRequestHandler". Los
   parámetros *addr* y *requestHandler* se pasan al constructor
   "socketserver. TCPServer". Si *logRequests* es verdadero (valor
   predeterminado), se registrarán las solicitudes; establecer este
   parámetro como falso desactivará el registro. Los parámetros
   *allow_none* y *encoding* se pasan a "xmlrpc.client" y controlan
   las respuestas XML-RPC que se devolverán desde el servidor. El
   parámetro *bind_and_activate* controla si "server_bind()" y
   "server_activate()" son llamados inmediatamente por el constructor;
   por defecto es verdadero. Establecerlo como false permite que el
   código manipule la variable de clase *allow_reuse_address* antes de
   enlazar la dirección. El parámetro *use_builtin_types* se pasa a la
   función "loads()" y controla qué tipos se procesan cuando se
   reciben valores de fecha y hora o datos binarios; el valor
   predeterminado es false.

   Distinto en la versión 3.3: Se ha añadido el indicador
   *use_builtin_types*.

class xmlrpc.server.CGIXMLRPCRequestHandler(allow_none=False, encoding=None, use_builtin_types=False)

   Crea una nueva instancia para gestionar solicitudes XML-RPC en un
   entorno CGI.  Los parámetros *allow_none* y *encoding* se pasan a
   "xmlrpc.client" y controlan las respuestas XML-RPC que se
   devolverán desde el servidor. El parámetro *use_builtin_types* se
   pasa a la función "loads()" y controla qué tipos se procesan cuando
   se reciben valores de fecha y hora o datos binarios; el valor
   predeterminado es falso.

   Distinto en la versión 3.3: Se ha añadido el indicador
   *use_builtin_types*.

class xmlrpc.server.SimpleXMLRPCRequestHandler

   Crea una nueva instancia del controlador de solicitudes.  Este
   controlador de solicitudes admite solicitudes "POST" y modifica el
   registro para que se respete el parámetro *logRequests* del
   parámetro constructor "SimpleXMLRPCServer".

## SimpleXMLRPCServer objects

La clase "SimpleXMLRPCServer" se basa en "socketserver.TCPServer" y
proporciona un medio para crear servidores XML-RPC simples e
independientes.

SimpleXMLRPCServer.register_function(function=None, name=None)

   Register a function that can respond to XML-RPC requests.  If
   *name* is given, it will be the method name associated with
   *function*, otherwise "function.__name__" will be used.  *name* is
   a string, and may contain characters not legal in Python
   identifiers, including the period character.

   This method can also be used as a decorator.  When used as a
   decorator, *name* can only be given as a keyword argument to
   register *function* under *name*.  If no *name* is given,
   "function.__name__" will be used.

   Distinto en la versión 3.7: "register_function()" puede ser usado
   como decorador.

SimpleXMLRPCServer.register_instance(instance, allow_dotted_names=False)

   Registre un objeto que se usa para exponer nombre de métodos que no
   se han registrado usando "register_function()". Si *instance*
   contiene un método "_dispatch()", este será llamado con el nombre
   del método solicitado y los parámetros de la solicitud. Su API es
   "def _dispatch(self, method, params)" (tenga en cuenta que *params*
   no representa una lista de argumentos variables). Si se invoca a
   una función subyacente para realizar su tarea, esa función es
   llamada como "func(*params)", expandiendo la lista de parámetros.
   El valor de retorno de "_dispatch()" se retorna al cliente como
   resultado. Si *instance* no tiene un método "_dispatch()", se busca
   un atributo que coincida con el nombre del método solicitado.

   Si el argumento opcional *allow_dotted_names* es verdadero y la
   instancia no tiene un método "_dispatch()", entonces si el nombre
   solicitado contiene puntos, cada componente del nombre del método
   se busca individualmente, con el efecto con el efecto que produce
   una búsqueda jerárquica simple. El valor encontrado en esta
   búsqueda es entonces llamado con los parámetros de la solicitud y
   el valor de retorno se devuelve al cliente.

   Advertencia:

     Habilitando la opción *allow_dotted_names* permite a los intrusos
     acceder a las variables globales de su módulo y puede permitir
     que los intrusos ejecuten código arbitrario en su máquina.
     Utilice esta opción únicamente en una red cerrada y segura.

SimpleXMLRPCServer.register_introspection_functions()

   Registre las funciones de introspección XML-RPC
   "system.listMethods", "system.methodHelp" y
   "system.methodSignature".

SimpleXMLRPCServer.register_multicall_functions()

   Registre la función de llamada múltiple XML-RPC system.multicall.

SimpleXMLRPCRequestHandler.rpc_paths

   Un valor de atributo que debe ser una tupla que enumere porciones
   de rota válidas de la URL para recibir solicitudes XML-RPC. Las
   solicitudes publicadas en otras rutas darán como resultado un error
   HTTP 404 "no existe tal página". Si esta tupla está vacía, todas
   las rutas se considerarán válidas. El valor predeterminado es
   "('/', '/RPC2')".

### SimpleXMLRPCServer example

Código del servidor:

   from xmlrpc.server import SimpleXMLRPCServer
   from xmlrpc.server import SimpleXMLRPCRequestHandler

   # Restrict to a particular path.
   class RequestHandler(SimpleXMLRPCRequestHandler):
       rpc_paths = ('/RPC2',)

   # Create server
   with SimpleXMLRPCServer(('localhost', 8000),
                           requestHandler=RequestHandler) as server:
       server.register_introspection_functions()

       # Register pow() function; this will use the value of
       # pow.__name__ as the name, which is just 'pow'.
       server.register_function(pow)

       # Register a function under a different name
       def adder_function(x, y):
           return x + y
       server.register_function(adder_function, 'add')

       # Register an instance; all the methods of the instance are
       # published as XML-RPC methods (in this case, just 'mul').
       class MyFuncs:
           def mul(self, x, y):
               return x * y

       server.register_instance(MyFuncs())

       # Run the server's main loop
       server.serve_forever()

El siguiente código de cliente llamará a los métodos disponibles por
el servidor anterior:

   import xmlrpc.client

   s = xmlrpc.client.ServerProxy('http://localhost:8000')
   print(s.pow(2,3))  # Returns 2**3 = 8
   print(s.add(2,3))  # Returns 5
   print(s.mul(5,2))  # Returns 5*2 = 10

   # Print list of available methods
   print(s.system.listMethods())

"register_function()" también se puede utilizar como decorador. El
ejemplo de servidor anterior puede registrar funciones a modo de
decorador:

   from xmlrpc.server import SimpleXMLRPCServer
   from xmlrpc.server import SimpleXMLRPCRequestHandler

   class RequestHandler(SimpleXMLRPCRequestHandler):
       rpc_paths = ('/RPC2',)

   with SimpleXMLRPCServer(('localhost', 8000),
                           requestHandler=RequestHandler) as server:
       server.register_introspection_functions()

       # Register pow() function; this will use the value of
       # pow.__name__ as the name, which is just 'pow'.
       server.register_function(pow)

       # Register a function under a different name, using
       # register_function as a decorator. *name* can only be given
       # as a keyword argument.
       @server.register_function(name='add')
       def adder_function(x, y):
           return x + y

       # Register a function under function.__name__.
       @server.register_function
       def mul(x, y):
           return x * y

       server.serve_forever()

El siguiente ejemplo incluido en el módulo "Lib/xmlrpc/server.py"
muestra un servidor que permite nombres con puntos y registra una
función de llamada múltiple.

Advertencia:

  Enabling the *allow_dotted_names* option allows intruders to access
  your module's global variables and may allow intruders to execute
  arbitrary code on your machine.  Only use this example within a
  secure, closed network.

   import datetime as dt

   class ExampleService:
       def getData(self):
           return '42'

       class currentTime:
           @staticmethod
           def getCurrentTime():
               return dt.datetime.now()

   with SimpleXMLRPCServer(("localhost", 8000)) as server:
       server.register_function(pow)
       server.register_function(lambda x,y: x+y, 'add')
       server.register_instance(ExampleService(), allow_dotted_names=True)
       server.register_multicall_functions()
       print('Serving XML-RPC on localhost port 8000')
       try:
           server.serve_forever()
       except KeyboardInterrupt:
           print("\nKeyboard interrupt received, exiting.")
           sys.exit(0)

Esta demostración de ExampleService se puede invocar desde la línea de
comando:

   python -m xmlrpc.server

El cliente que interactúa con el servidor anterior está incluido en
*Lib/xmlrpc/client.py*:

   server = ServerProxy("http://localhost:8000")

   try:
       print(server.currentTime.getCurrentTime())
   except Error as v:
       print("ERROR", v)

   multi = MultiCall(server)
   multi.getData()
   multi.pow(2,9)
   multi.add(1,2)
   try:
       for response in multi():
           print(response)
   except Error as v:
       print("ERROR", v)

Este cliente que interactúa con el servidor XMLRPC de demostración se
puede invocar como:

   python -m xmlrpc.client

## CGIXMLRPCRequestHandler

La clase "CGIXMLRPCRequestHandler" se puede usar para manejar
solicitudes XML-RPC enviadas a scripts Python CGI.

CGIXMLRPCRequestHandler.register_function(function=None, name=None)

   Register a function that can respond to XML-RPC requests.  If
   *name* is given, it will be the method name associated with
   *function*, otherwise "function.__name__" will be used.  *name* is
   a string, and may contain characters not legal in Python
   identifiers, including the period character.

   This method can also be used as a decorator.  When used as a
   decorator, *name* can only be given as a keyword argument to
   register *function* under *name*.  If no *name* is given,
   "function.__name__" will be used.

   Distinto en la versión 3.7: "register_function()" puede ser usado
   como decorador.

CGIXMLRPCRequestHandler.register_instance(instance)

   Registra un objeto que se usa para exponer nombres de métodos que
   no se han registrado usando "register_function()". Si la instancia
   contiene un método "_dispatch()", se llama con el nombre del método
   solicitado y los parámetros de la solicitud; el valor de retorno se
   devuelve al cliente como resultado. Si la instancia no tiene un
   método "_dispatch()", se busca un atributo que coincida con el
   nombre del método solicitado; si el nombre del método contiene
   puntos, cada componente del nombre del método se busca
   individualmente, con el efecto con el efecto que produce una
   búsqueda jerárquica simple. El valor encontrado en esta búsqueda es
   entonces llamado con los parámetros de la solicitud y el valor de
   retorno se devuelve al cliente.

CGIXMLRPCRequestHandler.register_introspection_functions()

   Registra las funciones de introspección "system.listMethods",
   "system.methodHelp" y "system.methodSignature".

CGIXMLRPCRequestHandler.register_multicall_functions()

   Registra la función de llamada múltiple XML-RPC "system.multicall".

CGIXMLRPCRequestHandler.handle_request(request_text=None)

   Maneja una solicitud XML-RPC. Si se proporciona *request_text*,
   deberían ser los datos POST proporcionados por el servidor HTTP, de
   lo contrario se utilizará el contenido de stdin.

Ejemplo:

   class MyFuncs:
       def mul(self, x, y):
           return x * y

   handler = CGIXMLRPCRequestHandler()
   handler.register_function(pow)
   handler.register_function(lambda x,y: x+y, 'add')
   handler.register_introspection_functions()
   handler.register_instance(MyFuncs())
   handler.handle_request()

## Documentando el servidor XMLRPC

Estas clases amplían las clases anteriores para proporcionar
documentación HTML en respuesta a solicitudes HTTP GET. Los servidores
pueden ser independientes, usando "DocXMLRPCServer", o integrados en
un entorno CGI, usando "DocCGIXMLRPCRequestHandler".

class xmlrpc.server.DocXMLRPCServer(addr, requestHandler=DocXMLRPCRequestHandler, logRequests=True, allow_none=False, encoding=None, bind_and_activate=True, use_builtin_types=True)

   Crea una nueva instancia de servidor. Todos los parámetros tienen
   el mismo significado que para "SimpleXMLRPCServer";
   *requestHandler* tiene como valor predeterminado
   "DocXMLRPCRequestHandler".

   Distinto en la versión 3.3: Se ha añadido el indicador
   *use_builtin_types*.

class xmlrpc.server.DocCGIXMLRPCRequestHandler

   Crea una nueva instancia para manejar solicitudes XML-RPC en un
   entorno CGI.

class xmlrpc.server.DocXMLRPCRequestHandler

   Crea una nueva instancia de controlador de solicitudes. Este
   controlador de solicitudes admite solicitudes XML-RPC POST,
   solicitudes GET de documentación y modifica el registro para que se
   respete el parámetro *logRequests* del parámetro constructor
   "DocXMLRPCServer".

## DocXMLRPCServer objects

La clase "DocXMLRPCServer" se deriva de "SimpleXMLRPCServer" y
proporciona un medio para crear servidores XML-RPC autónomos y
autodocumentados. Las solicitudes HTTP POST se manejan como llamadas
al método XML-RPC. Las solicitudes HTTP GET se manejan generando
documentación HTML al estilo pydoc. Esto permite que un servidor
proporcione su propia documentación basada en web.

DocXMLRPCServer.set_server_title(server_title)

   Establezca el título utilizado en la documentación HTML generada.
   Este título se utilizará dentro del elemento HTML "title".

DocXMLRPCServer.set_server_name(server_name)

   Establezca el nombre utilizado en la documentación HTML generada.
   Este nombre aparecerá en la parte superior de la documentación
   generada dentro de un elemento "h1".

DocXMLRPCServer.set_server_documentation(server_documentation)

   Establezca la descripción utilizada en la documentación HTML
   generada. Esta descripción aparecerá como un párrafo, debajo del
   nombre del servidor, en la documentación.

## DocCGIXMLRPCRequestHandler

La clase "DocCGIXMLRPCRequestHandler" se deriva de
"CGIXMLRPCRequestHandler" y proporciona un medio para crear scripts
CGI XML-RPC autodocumentados. Las solicitudes HTTP POST se manejan
como llamadas al método XML-RPC. Las solicitudes HTTP GET se manejan
generando documentación HTML al estilo pydoc. Esto permite que un
servidor proporcione su propia documentación basada en web.

DocCGIXMLRPCRequestHandler.set_server_title(server_title)

   Establezca el título utilizado en la documentación HTML generada.
   Este título se utilizará dentro del elemento HTML "title".

DocCGIXMLRPCRequestHandler.set_server_name(server_name)

   Establezca el nombre utilizado en la documentación HTML generada.
   Este nombre aparecerá en la parte superior de la documentación
   generada dentro de un elemento "h1".

DocCGIXMLRPCRequestHandler.set_server_documentation(server_documentation)

   Establezca la descripción utilizada en la documentación HTML
   generada. Esta descripción aparecerá como un párrafo, debajo del
   nombre del servidor, en la documentación.
