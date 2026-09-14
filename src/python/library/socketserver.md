---
title: '"socketserver" --- A framework for network servers'
source_url: https://docs.python.org/es/3
source_path: library/socketserver.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3850
---

# "socketserver" --- A framework for network servers

**Código fuente:** Lib/socketserver.py

======================================================================

The "socketserver" module simplifies the task of writing network
servers.

Availability: not WASI.

This module does not work or is not available on WebAssembly. See
Plataformas WebAssembly for more information.

Hay cuatro clases básicas de servidores concretos:

class socketserver.TCPServer(server_address, RequestHandlerClass, bind_and_activate=True)

   Esto utiliza el protocolo TCP de Internet, que proporciona flujos
   continuos de datos entre el cliente y el servidor. Si
   *bind_and_activate* es verdadero, el constructor intenta invocar
   automáticamente "server_bind()" y "server_activate()". Los otros
   parámetros se pasan a la clase base "BaseServer".

class socketserver.UDPServer(server_address, RequestHandlerClass, bind_and_activate=True)

   Esto utiliza datagramas, que son paquetes discretos de información
   que pueden llegar fuera de servicio o perderse durante el tránsito.
   Los parámetros son los mismos que para "TCPServer".

class socketserver.UnixStreamServer(server_address, RequestHandlerClass, bind_and_activate=True)
class socketserver.UnixDatagramServer(server_address, RequestHandlerClass, bind_and_activate=True)

   Estas clases que se usan con menos frecuencia son similares a las
   clases TCP y UDP, pero usan sockets de dominio Unix; no están
   disponibles en plataformas que no sean Unix. Los parámetros son los
   mismos que para "TCPServer".

Estas cuatro clases procesan solicitudes *sincrónicamente*; cada
solicitud debe completarse antes de que se pueda iniciar la siguiente.
Esto no es adecuado si cada solicitud tarda mucho en completarse,
porque requiere mucho cálculo o porque retorna muchos datos que el
cliente tarda en procesar. La solución es crear un proceso o hilo
independiente para manejar cada solicitud; las clases mixtas
"ForkingMixIn" y "ThreadingMixIn" pueden usarse para soportar el
comportamiento asincrónico.

La creación de un servidor requiere varios pasos. Primero, debes crear
una clase de controlador de solicitudes subclasificando la clase
"BaseRequestHandler" y anulando su método "handle()"; este método
procesará las solicitudes entrantes. En segundo lugar, debe crear una
instancia de una de las clases de servidor, pasándole la dirección del
servidor y la clase del controlador de solicitudes. Se recomienda
utilizar el servidor en una declaración "with". Luego llame al método
"handle_request()" o "serve_forever()" del objeto de servidor para
procesar una o muchas solicitudes. Finalmente, llame a
"server_close()" para cerrar el socket (a menos que haya usado una
"with" declaración).

Al heredar de "ThreadingMixIn" para el comportamiento de la conexión
con subprocesos, debe declarar explícitamente cómo desea que se
comporten sus subprocesos en un cierre abrupto. La clase
"ThreadingMixIn" define un atributo *daemon_threads*, que indica si el
servidor debe esperar o no la terminación del hilo. Debe establecer la
bandera explícitamente si desea que los subprocesos se comporten de
forma autónoma; el valor predeterminado es "False", lo que significa
que Python no se cerrará hasta que todos los hilos creados por
"ThreadingMixIn" hayan salido.

Las clases de servidor tienen los mismos métodos y atributos externos,
independientemente del protocolo de red que utilicen.

## Notas de creación del servidor

Hay cinco clases en un diagrama de herencia, cuatro de las cuales
representan servidores síncronos de cuatro tipos:

   +------------+
   | BaseServer |
   +------------+
         |
         v
   +-----------+        +------------------+
   | TCPServer |------->| UnixStreamServer |
   +-----------+        +------------------+
         |
         v
   +-----------+        +--------------------+
   | UDPServer |------->| UnixDatagramServer |
   +-----------+        +--------------------+

Tenga en cuenta que "UnixDatagramServer" deriva de "UDPServer", no de
"UnixStreamServer" --- la única diferencia entre un servidor IP y uno
Unix es la familia de direcciones.

class socketserver.ForkingMixIn
class socketserver.ThreadingMixIn

   Se pueden crear versiones de Forking y threading de cada tipo de
   servidor utilizando estas clases mixtas. Por ejemplo,
   "ThreadingUDPServer" se crea de la siguiente manera:

      class ThreadingUDPServer(ThreadingMixIn, UDPServer):
          pass

   La clase de mezcla es lo primero, ya que anula un método definido
   en "UDPServer". La configuración de los distintos atributos también
   cambia el comportamiento del mecanismo del servidor subyacente.

   "ForkingMixIn" y las clases de Forking mencionadas a continuación
   solo están disponibles en plataformas POSIX que admiten
   "os.fork()".

   block_on_close

      "ForkingMixIn.server_close" waits until all child processes
      complete, except if "block_on_close" attribute is "False".

      "ThreadingMixIn.server_close" waits until all non-daemon threads
      complete, except if "block_on_close" attribute is "False".

   max_children

      Specify how many child processes will exist to handle requests
      at a time for "ForkingMixIn".  If the limit is reached, new
      requests will wait until one child process has finished.

   daemon_threads

      For "ThreadingMixIn" use daemonic threads by setting
      "ThreadingMixIn.daemon_threads" to "True" to not wait until
      threads complete.

   Distinto en la versión 3.7: "ForkingMixIn.server_close" and
   "ThreadingMixIn.server_close" now waits until all child processes
   and non-daemonic threads complete. Add a new
   "ForkingMixIn.block_on_close" class attribute to opt-in for the
   pre-3.7 behaviour.

class socketserver.ForkingTCPServer
class socketserver.ForkingUDPServer
class socketserver.ThreadingTCPServer
class socketserver.ThreadingUDPServer
class socketserver.ForkingUnixStreamServer
class socketserver.ForkingUnixDatagramServer
class socketserver.ThreadingUnixStreamServer
class socketserver.ThreadingUnixDatagramServer

   Estas clases están predefinidas utilizando las clases mixtas.

Added in version 3.12: Las clases "ForkingUnixStreamServer" y
"ForkingUnixDatagramServer" fueron agregadas.

Para implementar un servicio, debes derivar una clase de
"BaseRequestHandler" y redefinir su método "handle()". Luego, puede
ejecutar varias versiones del servicio combinando una de las clases de
servidor con su clase de controlador de solicitudes. La clase del
controlador de solicitudes debe ser diferente para los servicios de
datagramas o flujos. Esto se puede ocultar usando las subclases del
controlador "StreamRequestHandler" o "DatagramRequestHandler".

Por supuesto, ¡todavía tienes que usar la cabeza! Por ejemplo, no
tiene sentido usar un servidor de bifurcación si el servicio contiene
un estado en la memoria que puede ser modificado por diferentes
solicitudes, ya que las modificaciones en el proceso hijo nunca
alcanzarían el estado inicial que se mantiene en el proceso padre y se
pasa a cada hijo. En este caso, puede usar un servidor de subprocesos,
pero probablemente tendrá que usar bloqueos para proteger la
integridad de los datos compartidos.

Por otro lado, si está creando un servidor HTTP donde todos los datos
se almacenan externamente (por ejemplo, en el sistema de archivos),
una clase síncrona esencialmente hará que el servicio sea "sordo"
mientras se maneja una solicitud, que puede ser durante mucho tiempo
si un cliente tarda en recibir todos los datos que ha solicitado. Aquí
es apropiado un servidor de enhebrado o bifurcación.

En algunos casos, puede ser apropiado procesar parte de una solicitud
de forma síncrona, pero para finalizar el procesamiento en un hijo
bifurcado según los datos de la solicitud. Esto se puede implementar
usando un servidor sincrónico y haciendo un fork explicito en la clase
del controlador de solicitudes el método "handle()".

Otro enfoque para gestionar múltiples solicitudes simultáneas en un
entorno que no admite subprocesos ni "fork()" (o donde estos son
demasiado costosos o inadecuados para el servicio) es mantener una
tabla explícita de solicitudes parcialmente terminadas y utilizar
"selectors" para decidir en qué solicitud trabajar a continuación (o
si manejar una nueva solicitud entrante). Esto es particularmente
importante para los servicios de transmisión en los que cada cliente
puede potencialmente estar conectado durante mucho tiempo (si no se
pueden utilizar subprocesos o subprocesos).

## Objetos de servidor

class socketserver.BaseServer(server_address, RequestHandlerClass)

   Esta es la superclase de todos los objetos de servidor en el
   módulo. Define la interfaz, que se indica a continuación, pero no
   implementa la mayoría de los métodos, que se realiza en subclases.
   Los dos parámetros se almacenan en los atributos respectivos
   "server_address" y "RequestHandlerClass".

   fileno()

      Retorna un descriptor de archivo entero para el socket en el que
      escucha el servidor. Esta función se pasa comúnmente a
      "selectors", para permitir monitorear múltiples servidores en el
      mismo proceso.

   handle_request()

      Procese una sola solicitud. Esta función llama a los siguientes
      métodos en orden: "get_request()", "verify_request()", y
      "process_request()". Si el método proporcionado por el usuario
      "handle()" de la clase del controlador lanza una excepción, se
      llamará al método "handle_error()" del servidor. Si no se recibe
      ninguna solicitud en "timeout" segundos, se llamará a
      "handle_timeout()" y "handle_request()" regresará.

   serve_forever(poll_interval=0.5)

      Manejar solicitudes hasta una solicitud explícita "shutdown()".
      Sondeo de apagado cada *poll_interval* segundos. Ignora el
      atributo "timeout". También llama "service_actions()", que puede
      ser utilizado por una subclase o mixin para proporcionar
      acciones específicas para un servicio dado. Por ejemplo, la
      clase "ForkingMixIn" usa "service_actions()" para limpiar
      procesos secundarios zombies.

      Distinto en la versión 3.3: Se agregó la llamada
      "service_actions" al método "serve_forever".

   service_actions()

      Esto se llama en el ciclo "serve_forever()". Este método puede
      ser reemplazado por subclases o clases mixtas para realizar
      acciones específicas para un servicio dado, como acciones de
      limpieza.

      Added in version 3.3.

   shutdown()

      Dile al bucle "serve_forever()" que se detenga y espere hasta
      que lo haga. "shutdown()" debe llamarse mientras
      "serve_forever()" se está ejecutando en un hilo diferente, de lo
      contrario, se bloqueará.

   server_close()

      Limpiar el servidor. Puede ser sobrescrito.

   address_family

      The family of protocols to which the server's socket belongs.
      Common examples are "socket.AF_INET", "socket.AF_INET6", and
      "socket.AF_UNIX".  Subclass the TCP or UDP server classes in
      this module with class attribute "address_family = AF_INET6" set
      if you want IPv6 server classes.

   RequestHandlerClass

      La clase de controlador de solicitudes proporcionada por el
      usuario; se crea una instancia de esta clase para cada
      solicitud.

   server_address

      La dirección en la que escucha el servidor. El formato de las
      direcciones varía según la familia de protocolos; consulte la
      documentación del módulo "socket" para obtener más detalles.
      Para los protocolos de Internet, esta es una tupla que contiene
      una cadena que da la dirección y un número de puerto entero:
      "('127.0.0.1', 80)", por ejemplo.

   socket

      El objeto de socket en el que el servidor escuchará las
      solicitudes entrantes.

   Las clases de servidor admiten las siguientes variables de clase:

   allow_reuse_address

      Si el servidor permitirá la reutilización de una dirección. Este
      valor predeterminado es "False", y se puede establecer en
      subclases para cambiar la política.

   request_queue_size

      El tamaño de la cola de solicitudes. Si toma mucho tiempo
      procesar una sola solicitud, cualquier solicitud que llegue
      mientras el servidor está ocupado se coloca en una cola, hasta
      "request_queue_size". Una vez que la cola está llena, más
      solicitudes de clientes obtendrán un error de "Conexión
      denegada". El valor predeterminado suele ser 5, pero las
      subclases pueden anularlo.

   socket_type

      El tipo de socket utilizado por el servidor;
      "socket.SOCK_STREAM" y "socket.SOCK_DGRAM" son dos valores
      comunes.

   timeout

      Duración del tiempo de espera, medida en segundos, o "None" si
      no se desea un tiempo de espera. Si "handle_request()" no recibe
      solicitudes entrantes dentro del período de tiempo de espera, se
      llama al método "handle_timeout()".

   Hay varios métodos de servidor que pueden ser anulados por
   subclases de clases de servidor base como "TCPServer"; estos
   métodos no son útiles para los usuarios externos del objeto de
   servidor.

   finish_request(request, client_address)

      En realidad, procesa la solicitud creando instancias
      "RequestHandlerClass" y llamando a su método "handle()".

   get_request()

      Debe aceptar una solicitud del socket y retornar una tupla de 2
      que contenga el objeto de socket *nuevo* que se utilizará para
      comunicarse con el cliente y la dirección del cliente.

   handle_error(request, client_address)

      Esta función se llama si el método "handle()" de una instancia
      "RequestHandlerClass" lanza una excepción. La acción
      predeterminada es imprimir el rastreo al error estándar y
      continuar manejando más solicitudes.

      Distinto en la versión 3.6: Ahora solo se solicitan excepciones
      derivadas de la clase "Exception".

   handle_timeout()

      Esta función se llama cuando el atributo "timeout" se ha
      establecido en un valor distinto de "None" y el tiempo de espera
      ha pasado sin que se reciban solicitudes. La acción
      predeterminada para los servidores de forking es recopilar el
      estado de cualquier proceso hijo que haya salido, mientras que
      en los servidores de threading este método no hace nada.

   process_request(request, client_address)

      Llama a "finish_request()" para crear una instancia de
      "RequestHandlerClass". Si lo desea, esta función puede crear un
      nuevo proceso o hilo para manejar la solicitud; las clases
      "ForkingMixIn" y "ThreadingMixIn" hacen esto.

   server_activate()

      Lo llama el constructor del servidor para activar el servidor.
      El comportamiento predeterminado para un servidor TCP
      simplemente invoca "listen()" en el socket del servidor. Puede
      anularse.

   server_bind()

      Lo llama el constructor del servidor para vincular el socket a
      la dirección deseada. Puede anularse.

   verify_request(request, client_address)

      Debe retornar un valor booleano; si el valor es "True", la
      solicitud se procesará, y si es "False", la solicitud será
      denegada. Esta función se puede anular para implementar
      controles de acceso para un servidor. La implementación
      predeterminada siempre retorna "True".

   Distinto en la versión 3.6: Se agregó soporte para el protocolo
   *context manager*. Salir del administrador de contexto es
   equivalente a llamar a "server_close()".

## Solicitar objetos de controlador

class socketserver.BaseRequestHandler

   Esta es la superclase de todos los objetos de manejo de
   solicitudes. Define la interfaz, que se muestra a continuación. Una
   subclase de controlador de solicitudes concreta debe definir un
   nuevo método "handle()" y puede anular cualquiera de los otros
   métodos. Se crea una nueva instancia de la subclase para cada
   solicitud.

   setup()

      Se llama antes del método "handle()" para realizar las acciones
      de inicialización necesarias. La implementación predeterminada
      no hace nada.

   handle()

      This function must do all the work required to service a
      request.  The default implementation does nothing.  Several
      instance attributes are available to it; the request is
      available as "request"; the client address as "client_address";
      and the server instance as "server", in case it needs access to
      per-server information.

      The type of "request" is different for datagram or stream
      services.  For stream services, "request" is a socket object;
      for datagram services, "request" is a pair of string and socket.

   finish()

      Se llama después del método "handle()" para realizar las
      acciones de limpieza necesarias. La implementación
      predeterminada no hace nada. Si "setup()" lanza una excepción,
      no se llamará a esta función.

   request

      The *new* "socket.socket" object to be used to communicate with
      the client.

   client_address

      Client address returned by "BaseServer.get_request()".

   server

      "BaseServer" object used for handling the request.

class socketserver.StreamRequestHandler
class socketserver.DatagramRequestHandler

   These "BaseRequestHandler" subclasses override the "setup()" and
   "finish()" methods, and provide "rfile" and "wfile" attributes.

   rfile

      A file object from which receives the request is read. Support
      the "io.BufferedIOBase" readable interface.

   wfile

      A file object to which the reply is written. Support the
      "io.BufferedIOBase" writable interface

   Distinto en la versión 3.6: "wfile" also supports the
   "io.BufferedIOBase" writable interface.

## Ejemplos

### "socketserver.TCPServer" Ejemplo

Este es el lado del servidor:

   import socketserver

   class MyTCPHandler(socketserver.BaseRequestHandler):
       """
       The request handler class for our server.

       It is instantiated once per connection to the server, and must
       override the handle() method to implement communication to the
       client.
       """

       def handle(self):
           # self.request is the TCP socket connected to the client
           pieces = [b'']
           total = 0
           while b'\n' not in pieces[-1] and total < 10_000:
               pieces.append(self.request.recv(2000))
               total += len(pieces[-1])
           self.data = b''.join(pieces)
           print(f"Received from {self.client_address[0]}:")
           print(self.data.decode("utf-8"))
           # just send back the same data, but upper-cased
           self.request.sendall(self.data.upper())
           # after we return, the socket will be closed.

   if __name__ == "__main__":
       HOST, PORT = "localhost", 9999

       # Create the server, binding to localhost on port 9999
       with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
           # Activate the server; this will keep running until you
           # interrupt the program with Ctrl-C
           server.serve_forever()

Una clase de controlador de solicitudes alternativa que hace uso de
secuencias (objetos similares a archivos que simplifican la
comunicación al proporcionar la interfaz de archivo estándar):

   class MyTCPHandler(socketserver.StreamRequestHandler):

       def handle(self):
           # self.rfile is a file-like object created by the handler.
           # We can now use e.g. readline() instead of raw recv() calls.
           # We limit ourselves to 10000 bytes to avoid abuse by the sender.
           self.data = self.rfile.readline(10000).rstrip()
           print(f"{self.client_address[0]} wrote:")
           print(self.data.decode("utf-8"))
           # Likewise, self.wfile is a file-like object used to write back
           # to the client
           self.wfile.write(self.data.upper())

The difference is that the "readline()" call in the second handler
will call "recv()" multiple times until it encounters a newline
character, while the first handler had to use a "recv()" loop to
accumulate data until a newline itself.  If it had just used a single
"recv()" without the loop it would just have returned what has been
received so far from the client. TCP is stream based: data arrives in
the order it was sent, but there is no correlation between client
"send()" or "sendall()" calls and the number of "recv()" calls on the
server required to receive it.

Este es el lado del cliente:

   import socket
   import sys

   HOST, PORT = "localhost", 9999
   data = " ".join(sys.argv[1:])

   # Create a socket (SOCK_STREAM means a TCP socket)
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
       # Connect to server and send data
       sock.connect((HOST, PORT))
       sock.sendall(bytes(data, "utf-8"))
       sock.sendall(b"\n")

       # Receive data from the server and shut down
       received = str(sock.recv(1024), "utf-8")

   print("Sent:    ", data)
   print("Received:", received)

La salida del ejemplo debería verse así:

Servidor:

   $ python TCPServer.py
   127.0.0.1 wrote:
   b'hello world with TCP'
   127.0.0.1 wrote:
   b'python is nice'

Cliente:

   $ python TCPClient.py hello world with TCP
   Sent:     hello world with TCP
   Received: HELLO WORLD WITH TCP
   $ python TCPClient.py python is nice
   Sent:     python is nice
   Received: PYTHON IS NICE

### "socketserver.UDPServer" Ejemplo

Este es el lado del servidor:

   import socketserver

   class MyUDPHandler(socketserver.BaseRequestHandler):
       """
       This class works similar to the TCP handler class, except that
       self.request consists of a pair of data and client socket, and since
       there is no connection the client address must be given explicitly
       when sending data back via sendto().
       """

       def handle(self):
           data = self.request[0].strip()
           socket = self.request[1]
           print(f"{self.client_address[0]} wrote:")
           print(data)
           socket.sendto(data.upper(), self.client_address)

   if __name__ == "__main__":
       HOST, PORT = "localhost", 9999
       with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
           server.serve_forever()

Este es el lado del cliente:

   import socket
   import sys

   HOST, PORT = "localhost", 9999
   data = " ".join(sys.argv[1:])

   # SOCK_DGRAM is the socket type to use for UDP sockets
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

   # As you can see, there is no connect() call; UDP has no connections.
   # Instead, data is directly sent to the recipient via sendto().
   sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
   received = str(sock.recv(1024), "utf-8")

   print("Sent:    ", data)
   print("Received:", received)

La salida del ejemplo debería verse exactamente como en el ejemplo del
servidor TCP.

### Mixins asincrónicos

Para construir controladores asincrónicos, use las clases
"ThreadingMixIn" y "ForkingMixIn".

Un ejemplo para la clase "ThreadingMixIn" class

   import socket
   import threading
   import socketserver

   class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

       def handle(self):
           data = str(self.request.recv(1024), 'ascii')
           cur_thread = threading.current_thread()
           response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
           self.request.sendall(response)

   class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
       pass

   def client(ip, port, message):
       with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
           sock.connect((ip, port))
           sock.sendall(bytes(message, 'ascii'))
           response = str(sock.recv(1024), 'ascii')
           print("Received: {}".format(response))

   if __name__ == "__main__":
       # Port 0 means to select an arbitrary unused port
       HOST, PORT = "localhost", 0

       server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
       with server:
           ip, port = server.server_address

           # Start a thread with the server -- that thread will then start one
           # more thread for each request
           server_thread = threading.Thread(target=server.serve_forever)
           # Exit the server thread when the main thread terminates
           server_thread.daemon = True
           server_thread.start()
           print("Server loop running in thread:", server_thread.name)

           client(ip, port, "Hello World 1")
           client(ip, port, "Hello World 2")
           client(ip, port, "Hello World 3")

           server.shutdown()

La salida del ejemplo debería verse así:

   $ python ThreadedTCPServer.py
   Server loop running in thread: Thread-1
   Received: Thread-2: Hello World 1
   Received: Thread-3: Hello World 2
   Received: Thread-4: Hello World 3

La clase "ForkingMixIn" se usa de la misma manera, excepto que el
servidor generará un nuevo proceso para cada solicitud. Disponible
solo en plataformas POSIX que admitan "fork()".
