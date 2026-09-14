---
title: Transportes y protocolos
source_url: https://docs.python.org/es/3
source_path: library/asyncio-protocol.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1680
---

# Transportes y protocolos

-[ Prefacio ]-

Los transportes y protocolos son utilizados por las APIs de **bajo
nivel** de los bucles de eventos, como "loop.create_connection()".
Utilizan un estilo de programación basado en retrollamadas y permiten
implementaciones de alto rendimiento de protocolos de red o IPC (p.
ej. HTTP).

Esencialmente, los transportes y protocolos solo deben usarse en
bibliotecas y frameworks, nunca en aplicaciones asyncio de alto nivel.

Esta página de la documentación cubre tanto Transports como Protocols.

-[ Introducción ]-

En el nivel más alto, el transporte se ocupa de *cómo* se transmiten
los bytes, mientras que el protocolo determina *qué* bytes transmitir
(y hasta cierto punto cuándo).

Una forma diferente de decir lo mismo: Un transporte es una
abstracción para un socket (o un punto final de E/S similar) mientras
que un protocolo es una abstracción para una aplicación, desde el
punto de vista del transporte.

Otro punto de vista más es que las interfaces de transporte y
protocolo definen juntas una interfaz abstracta para usar E/S de red y
E/S entre procesos.

Siempre existe una relación 1:1 entre el transporte y los objetos
protocolo: el protocolo llama a los métodos del transporte para enviar
datos, mientras que el transporte llama a los métodos del protocolo
para enviarle los datos que se han recibido.

La mayoría de los métodos del bucle de eventos orientados a la
conexión (como "loop.create_connection()") aceptan generalmente un
argumento *protocol_factory* que es usado para crear un objeto
*Protocol* para una conexión aceptada, representada por un objeto
*Transport*. Estos métodos suelen retornar una tupla de la forma
"(transporte, protocolo)".

-[ Contenidos ]-

Esta página de la documentación contiene las siguientes secciones:

* La sección Transports documenta las clases asyncio "BaseTransport",
  "ReadTransport", "WriteTransport", "Transport", "DatagramTransport"
  y "SubprocessTransport".

* La sección Protocols documenta las clases asyncio "BaseProtocol",
  "Protocol", "BufferedProtocol", "DatagramProtocol" y
  "SubprocessProtocol".

* La sección Examples muestra cómo trabajar con transportes,
  protocolos y las APIs de bajo nivel del bucle de eventos.

## Transportes

**Código fuente:** Lib/asyncio/transports.py

======================================================================

Los transportes son clases proporcionadas por "asyncio" para abstraer
varios tipos de canales de comunicación.

Los objetos transporte siempre son instanciados por un bucle de
eventos asyncio.

asyncio implementa transportes para TCP, UDP, SSL y pipes de
subprocesos. Los métodos disponibles en un transporte dependen del
tipo de transporte.

Las clases transporte no son seguras en hilos.

### Jerarquía de transportes

class asyncio.BaseTransport

   Clase base para todos los transportes. Contiene métodos que todos
   los transportes asyncio comparten.

class asyncio.WriteTransport(BaseTransport)

   Un transporte base para conexiones de solo escritura.

   Las instancias de la clase *WriteTransport* se retornan desde el
   método del bucle de eventos "loop.connect_write_pipe()" y también
   se utilizan en métodos relacionados con subprocesos como
   "loop.subprocess_exec()".

class asyncio.ReadTransport(BaseTransport)

   Un transporte base para conexiones de solo lectura.

   Las instancias de la clase *ReadTransport* se retornan desde el
   método del bucle de eventos "loop.connect_read_pipe()" y también se
   utilizan en métodos relacionados con subprocesos como
   "loop.subprocess_exec()".

class asyncio.Transport(WriteTransport, ReadTransport)

   Interfaz que representa un transporte bidireccional, como una
   conexión TCP.

   El usuario no crea una instancia de transporte directamente; en su
   lugar se llama a una función de utilidad, pasándole una fábrica de
   protocolos junto a otra información necesaria para crear el
   transporte y el protocolo.

   Las instancias de la clase *Transport* son retornadas o utilizadas
   por métodos del bucle de eventos como "loop.create_connection()",
   "loop.create_unix_connection()", "loop.create_server()",
   "loop.sendfile()", etc.

class asyncio.DatagramTransport(BaseTransport)

   Un transporte para conexiones de datagramas (UDP).

   Las instancias de la clase *DatagramTransport* se retornan desde el
   método "loop.create_datagram_endpoint()" del bucle de eventos.

class asyncio.SubprocessTransport(BaseTransport)

   Una abstracción para representar una conexión entre un proceso
   padre y su proceso OS hijo.

   Las instancias de la clase *SubprocessTransport* se retornan desde
   los métodos del bucle de eventos "loop.subprocess_shell()" y
   "loop.subprocess_exec()".

### Transporte base

BaseTransport.close()

   Cierra el transporte.

   Si el transporte tiene un búfer para datos de salida, los datos
   almacenados en el búfer se eliminarán de forma asincrónica. No se
   recibirán más datos. Después de que se vacíen todos los datos
   almacenados en el búfer, el método "protocol.connection_lost()" del
   protocolo se llamará con "None" como argumento. El transporte no
   debería ser usado luego de haber sido cerrado.

BaseTransport.is_closing()

   Retorna "True" si el transporte se está cerrando o está ya cerrado.

BaseTransport.get_extra_info(name, default=None)

   Retorna información sobre el transporte o los recursos subyacentes
   que utiliza.

   *name* es una cadena de caracteres que representa la información
   específica del transporte que se va a obtener.

   *default* es el valor que se retornará si la información no está
   disponible o si el transporte no admite la consulta con la
   implementación del bucle de eventos de terceros dada o en la
   plataforma actual.

   Por ejemplo, el siguiente código intenta obtener el objeto socket
   subyacente del transporte:

      sock = transport.get_extra_info('socket')
      if sock is not None:
          print(sock.getsockopt(...))

   Categorías de información que se pueden consultar sobre algunos
   transportes:

   * socket:

     * "'peername'": la dirección remota a la que está conectado el
       socket, resultado de "socket.socket.getpeername()" ("None" en
       caso de error)

     * "'socket'": instancia de "socket.socket"

     * "'sockname'": la dirección propia del socket, resultado de
       "socket.socket.getsockname()"

   * socket SSL:

     * "'compression'": el algoritmo de compresión que se está usando
       como una cadena de caracteres o "None" si la conexión no está
       comprimida; resultado de "ssl.SSLSocket.compression()"

     * "'cipher'": una tupla de tres valores que contiene el nombre
       del cifrado que se está utilizando, la versión del protocolo
       SSL que define su uso y la cantidad de bits de la clave secreta
       que se utilizan; resultado de "ssl.SSLSocket.cipher()"

     * "'peercert'": certificado de pares; resultado de
       "ssl.SSLSocket.getpeercert()"

     * "'sslcontext'": instancia de "ssl.SSLContext"

     * "'ssl_object'": instancia de "ssl.SSLObject" o "ssl.SSLSocket"

   * pipe:

     * "'pipe'": objeto pipe

   * subproceso:

     * "'subprocess'": instancia de "subprocess.Popen"

BaseTransport.set_protocol(protocol)

   Establece un nuevo protocolo.

   El cambio de protocolo solo debe realizarse cuando esté documentado
   que ambos protocolos admiten el cambio.

BaseTransport.get_protocol()

   Retorna el protocolo actual.

### Transportes de solo lectura

ReadTransport.is_reading()

   Retorna "True" si el transporte está recibiendo nuevos datos.

   Added in version 3.7.

ReadTransport.pause_reading()

   Pausa el extremo receptor del transporte. No se pasarán datos al
   método "protocol.data_received()" del protocolo hasta que se llame
   a "resume_reading()".

   Distinto en la versión 3.7: El método es idempotente, es decir, se
   puede llamar cuando el transporte ya está en pausa o cerrado.

ReadTransport.resume_reading()

   Reanuda el extremo receptor. El método "protocol.data_received()"
   del protocolo se llamará una vez más si hay algunos datos
   disponibles para su lectura.

   Distinto en la versión 3.7: El método es idempotente, es decir, se
   puede llamar cuando el transporte está leyendo.

### Transportes de solo escritura

WriteTransport.abort()

   Cierra el transporte inmediatamente, sin esperar a que finalicen
   las operaciones pendientes. Se perderán los datos almacenados en el
   búfer. No se recibirán más datos. El método
   "protocol.connection_lost()" del protocolo será llamado
   eventualmente con "None" como argumento.

WriteTransport.can_write_eof()

   Retorna "True" si el transporte admite "write_eof()", en caso
   contrario "False".

WriteTransport.get_write_buffer_size()

   Retorna el tamaño actual del búfer de salida utilizado por el
   transporte.

WriteTransport.get_write_buffer_limits()

   Obtiene los límites superior e inferior para el control del flujo
   de escritura. Retorna una tupla "(low, high)" donde *low*
   ('inferior') y *high* ('superior') son un número de bytes positivo.

   Usa "set_write_buffer_limits()" para establecer los límites.

   Added in version 3.4.2.

WriteTransport.set_write_buffer_limits(high=None, low=None)

   Establece los límites *high* ('superior') y *low* ('inferior') para
   el control del flujo de escritura.

   Estos dos valores (medidos en número de bytes) controlan cuándo se
   llaman los métodos "protocol.pause_writing()" y
   "protocol.resume_writing()" del protocolo . Si se especifica, el
   límite inferior debe ser menor o igual que el límite superior. Ni
   *high* ni *low* pueden ser negativos.

   "pause_writing()" se llama cuando el tamaño del búfer es mayor o
   igual que el valor *high* ('superior'). Si se ha pausado la
   escritura, se llama a "resume_writing()" cuando el tamaño del búfer
   es menor o igual que el valor *low* ('inferior').

   Los valores por defecto son específicos de la implementación. Si
   solo se proporciona el límite superior, el inferior toma de forma
   predeterminada un valor específico, dependiente de la
   implementación, menor o igual que el límite superior. Establecer
   *high* ('superior') en cero fuerza *low* ('inferior') a cero
   también y hace que "pause_writing()" sea llamado siempre que el
   búfer no esté vacío. Establecer *low* ('inferior') en cero hace que
   "resume_writing()" sea llamado únicamente cuando el búfer esté
   vacío. El uso de cero para cualquiera de los límites es
   generalmente subóptimo, ya que reduce las oportunidades para
   realizar E/S y cálculos simultáneamente.

   Usa "get_write_buffer_limits()" para obtener los límites.

WriteTransport.write(data)

   Escribe los bytes de *data* en el transporte.

   Este método no bloquea; almacena los datos en el búfer y organiza
   que se envíen de forma asincrónica.

WriteTransport.writelines(list_of_data)

   Escribe una lista (o cualquier iterable) de bytes de datos en el
   transporte. Esto es funcionalmente equivalente a llamar a "write()"
   en cada elemento generado por el iterable, pero puede ser
   implementado de manera más eficiente.

WriteTransport.write_eof()

   Cierra el extremo de escritura del transporte después de vaciar
   todos los datos almacenados en el búfer. Aún es posible recibir
   datos.

   Este método puede lanzar una excepción "NotImplementedError" si el
   transporte (p. ej. SSL) no soporta conexiones semicerradas (*half-
   closed*).

### Transportes de datagramas

DatagramTransport.sendto(data, addr=None)

   Envía los bytes *data* al par remoto proporcionado por *addr* (una
   dirección de destino dependiente del transporte). Si *addr* es
   "None", los datos se envían a la dirección de destino proporcionada
   en la creación del transporte.

   Este método no bloquea; almacena los datos en el búfer y organiza
   que se envíen de forma asincrónica.

   Distinto en la versión 3.13: This method can be called with an
   empty bytes object to send a zero-length datagram. The buffer size
   calculation used for flow control is also updated to account for
   the datagram header.

DatagramTransport.abort()

   Cierra el transporte inmediatamente, sin esperar a que finalicen
   las operaciones pendientes. Se perderán los datos almacenados en el
   búfer. No se recibirán más datos. El método
   "protocol.connection_lost()" del protocolo será llamado
   eventualmente con "None" como argumento.

### Transportes de subprocesos

SubprocessTransport.get_pid()

   Retorna la id del subproceso como un número entero.

SubprocessTransport.get_pipe_transport(fd)

   Retorna el transporte para la pipe de comunicación correspondiente
   al descriptor de archivo entero *fd*:

   * "0": writable streaming transport of the standard input
     (*stdin*), or "None" if the subprocess was not created with
     "stdin=PIPE"

   * "1": readable streaming transport of the standard output
     (*stdout*), or "None" if the subprocess was not created with
     "stdout=PIPE"

   * "2": readable streaming transport of the standard error
     (*stderr*), or "None" if the subprocess was not created with
     "stderr=PIPE"

   * otro *fd*: "None"

SubprocessTransport.get_returncode()

   Retorna el código de retorno del subproceso como un entero o "None"
   si no ha retornado aún, lo que es similar al atributo
   "subprocess.Popen.returncode".

SubprocessTransport.kill()

   Mata al subproceso.

   En los sistemas POSIX, la función envía SIGKILL al subproceso. En
   Windows, este método es un alias para "terminate()".

   Ver también "subprocess.Popen.kill()".

SubprocessTransport.send_signal(signal)

   Envía el número de *señal* al subproceso, como en
   "subprocess.Popen.send_signal()".

SubprocessTransport.terminate()

   Detiene el subproceso.

   On POSIX systems, this method sends "SIGTERM" to the subprocess. On
   Windows, the Windows API function "TerminateProcess()" is called to
   stop the subprocess.

   Ver también "subprocess.Popen.terminate()".

SubprocessTransport.close()

   Mata al subproceso llamando al método "kill()".

   Si el subproceso aún no ha retornado, cierra los transportes de las
   pipes *stdin*, *stdout* y *stderr*.

## Protocolos

**Código fuente:** Lib/asyncio/protocols.py

======================================================================

asyncio proporciona un conjunto de clases base abstractas que pueden
usarse para implementar protocolos de red. Estas clases están
destinadas a ser utilizadas junto con los transportes.

Las subclases de las clases abstractas de protocolos base pueden
implementar algunos o todos los métodos. Todos estos métodos son
retrollamadas: son llamados por los transportes en ciertos eventos,
por ejemplo, cuando se reciben algunos datos. Un método del protocolo
base debe ser llamado por el transporte correspondiente.

### Protocolos base

class asyncio.BaseProtocol

   Protocolo base con métodos que comparten todos los demás
   protocolos.

class asyncio.Protocol(BaseProtocol)

   La clase base para implementar protocolos de *streaming* (TCP,
   sockets Unix, etc).

class asyncio.BufferedProtocol(BaseProtocol)

   Una clase base para implementar protocolos de *streaming* con
   control manual del búfer de recepción.

class asyncio.DatagramProtocol(BaseProtocol)

   La clase base para implementar protocolos de datagramas (UDP).

class asyncio.SubprocessProtocol(BaseProtocol)

   La clase base para implementar protocolos que se comunican con
   procesos secundarios (pipes unidireccionales).

### Protocolo base

Todos los protocolos asyncio pueden implementar las retrollamadas del
protocolo base.

-[ Retrollamadas de conexión ]-

Las retrollamadas de conexión son llamadas exactamente una vez por
conexión establecida en todos los protocolos. Todas las demás
retrollamadas del protocolo solo pueden ser llamadas entre estos dos
métodos.

BaseProtocol.connection_made(transport)

   Se llama cuando se establece una conexión.

   El argumento *transport* es el transporte que representa la
   conexión. El protocolo se encarga de almacenar la referencia a su
   propio transporte.

BaseProtocol.connection_lost(exc)

   Se llama cuando la conexión se pierde o se cierra.

   El argumento es un objeto excepción o "None". Esto último significa
   que se recibió un EOF regular o que la conexión fue cancelada o
   cerrada por este lado de la conexión.

-[ Retrollamadas de control de flujo ]-

Los transportes pueden llamar a las retrollamadas de control de flujo
para pausar o reanudar la escritura llevada a cabo por el protocolo.

Consulta la documentación del método "set_write_buffer_limits()" para
obtener más detalles.

BaseProtocol.pause_writing()

   Se llama cuando el búfer del transporte supera el límite superior.

BaseProtocol.resume_writing()

   Se llama cuando el búfer del transporte se vacía por debajo del
   límite inferior.

Si el tamaño del búfer es igual al límite superior, "pause_writing()"
no será llamado: el tamaño del búfer debe superarse estrictamente.

Por el contrario, se llama a "resume_writing()" cuando el tamaño del
búfer es igual o menor que el límite inferior. Estas condiciones
finales son importantes para garantizar que todo salga como se espera
cuando cualquiera de los dos límites sea cero.

### Protocolos de *streaming*

Los métodos de eventos, como "loop.create_server()",
"loop.create_unix_server()", "loop.create_connection()",
"loop.create_unix_connection()", "loop.connect_accepted_socket()",
"loop.connect_read_pipe()", y "loop.connect_write_pipe()" aceptan
fábricas que retornan protocolos de *streaming*.

Protocol.data_received(data)

   Se llama cuando se reciben algunos datos. *data* es un objeto bytes
   no vacío que contiene los datos entrantes.

   Que los datos se almacenen en un búfer, que se fragmenten o se
   vuelvan a ensamblar depende del transporte. En general, no debe
   confiar en semánticas específicas y, en cambio, hacer que su
   análisis sea genérico y flexible. Sin embargo, los datos siempre se
   reciben en el orden correcto.

   El método se puede llamar un número arbitrario de veces mientras
   una conexión esté abierta.

   Sin embargo, "protocol.eof_received()" se llama como máximo una
   vez. Luego de llamar a "eof_received()", ya no se llama más a
   "data_received()".

Protocol.eof_received()

   Se llama cuando el otro extremo indica que no enviará más datos
   (por ejemplo, llamando a "transport.write_eof()" si el otro extremo
   también usa asyncio).

   Este método puede retornar un valor falso (incluido "None"), en
   cuyo caso el transporte se cerrará solo. Por el contrario, si este
   método retorna un valor verdadero, el protocolo utilizado determina
   si se debe cerrar el transporte. Dado que la implementación por
   defecto retorna "None", en éste caso, se cierra implícitamente la
   conexión.

   Algunos transportes, incluido SSL, no admiten conexiones
   semicerradas (*half-closed*), en cuyo caso retornar verdadero desde
   este método resultará en el cierre de la conexión.

Máquina de estado:

   start -> connection_made
       [-> data_received]*
       [-> eof_received]?
   -> connection_lost -> end

### Protocolos de *streaming* mediante búfer

Added in version 3.7.

Los protocolos que hacen uso de un búfer se pueden utilizar con
cualquier método del bucle de eventos que admita Streaming Protocols.

Las implementaciones de "BufferedProtocol" permiten la asignación
manual explícita y el control del búfer de recepción. Los bucles de
eventos pueden utilizar el búfer proporcionado por el protocolo para
evitar copias de datos innecesarias. Esto puede resultar en una mejora
notable del rendimiento de los protocolos que reciben grandes
cantidades de datos. Las implementaciones de protocolos sofisticados
pueden reducir significativamente la cantidad de asignaciones de
búfer.

Las siguientes retrollamadas son llamadas en instancias
"BufferedProtocol":

BufferedProtocol.get_buffer(sizehint)

   Se llama para asignar un nuevo búfer de recepción.

   *sizehint* es el tamaño mínimo recomendado para el búfer retornado.
   Es aceptable retornar búferes más pequeños o más grandes de lo que
   sugiere *sizehint*. Cuando se establece en -1, el tamaño del búfer
   puede ser arbitrario. Es un error retornar un búfer con tamaño
   cero.

   "get_buffer()" debe retornar un objeto que implemente el protocolo
   de búfer.

BufferedProtocol.buffer_updated(nbytes)

   Se llama cuando el búfer se ha actualizado con los datos recibidos.

   *nbytes* es el número total de bytes que se escribieron en el
   búfer.

BufferedProtocol.eof_received()

   Consulte la documentación del método "protocol.eof_received()".

"get_buffer()" se puede llamar un número arbitrario de veces durante
una conexión. Sin embargo, "protocol.eof_received ()" se llama como
máximo una vez y, si se llama, "get_buffer()" y "buffer_updated()" no
serán llamados después de eso.

Máquina de estado:

   start -> connection_made
       [-> get_buffer
           [-> buffer_updated]?
       ]*
       [-> eof_received]?
   -> connection_lost -> end

### Protocolos de datagramas

Las instancias del protocolo de datagramas deben ser construidas por
fábricas de protocolos pasadas al método
"loop.create_datagram_endpoint()".

DatagramProtocol.datagram_received(data, addr)

   Se llama cuando se recibe un datagrama. *data* es un objeto bytes
   que contiene los datos entrantes. *addr* es la dirección del par
   que envía los datos; el formato exacto depende del transporte.

DatagramProtocol.error_received(exc)

   Se llama cuando una operación de envío o recepción anterior genera
   una "OSError". *exc* es la instancia "OSError".

   Este método se llama en condiciones excepcionales, cuando el
   transporte (por ejemplo, UDP) detecta que un datagrama no se pudo
   entregar a su destinatario. Sin embargo, en la mayoría de casos,
   los datagramas que no se puedan entregar se eliminarán
   silenciosamente.

Nota:

  En los sistemas BSD (macOS, FreeBSD, etc.) el control de flujo no es
  compatible con los protocolos de datagramas, esto se debe a que no
  hay una forma confiable de detectar fallos de envío causados por
  escribir demasiados paquetes.El socket siempre aparece como
  disponible ('ready') y se eliminan los paquetes sobrantes. Un error
  "OSError" con "errno" establecido en "errno.ENOBUFS" puede o no ser
  generado; si se genera, se informará a
  "DatagramProtocol.error_received()" pero en caso contrario se
  ignorará.

### Protocolos de subprocesos

Las instancias de protocolo de subproceso deben ser construidas por
fábricas de protocolos pasadas a los métodos "loop.subprocess_exec()"
y "loop.subprocess_shell()".

SubprocessProtocol.pipe_data_received(fd, data)

   Se llama cuando el proceso hijo escribe datos en su pipe stdout o
   stderr.

   *fd* es el descriptor de archivo entero de la pipe.

   *data* es un objeto bytes no vacío que contiene los datos
   recibidos.

SubprocessProtocol.pipe_connection_lost(fd, exc)

   Se llama cuando se cierra una de las pipes que se comunican con el
   proceso hijo.

   *fd* es el descriptor de archivo entero que se cerró.

SubprocessProtocol.process_exited()

   Se llama cuando el proceso hijo ha finalizado.

   It can be called before "pipe_data_received()" and
   "pipe_connection_lost()" methods.

## Ejemplos

### Servidor de eco TCP

Crear un servidor de eco TCP usando el método "loop.create_server()",
enviar de vuelta los datos recibidos y cerrar la conexión:

   import asyncio

   class EchoServerProtocol(asyncio.Protocol):
       def connection_made(self, transport):
           peername = transport.get_extra_info('peername')
           print('Connection from {}'.format(peername))
           self.transport = transport

       def data_received(self, data):
           message = data.decode()
           print('Data received: {!r}'.format(message))

           print('Send: {!r}'.format(message))
           self.transport.write(data)

           print('Close the client socket')
           self.transport.close()

   async def main():
       # Get a reference to the event loop as we plan to use
       # low-level APIs.
       loop = asyncio.get_running_loop()

       server = await loop.create_server(
           EchoServerProtocol,
           '127.0.0.1', 8888)

       async with server:
           await server.serve_forever()

   asyncio.run(main())

Ver también:

  El ejemplo Servidor de eco TCP usando streams usa la función de alto
  nivel "asyncio.start_server()".

### Cliente de eco TCP

Un cliente de eco TCP usando el método "loop.create_connection()",
envía datos y espera hasta que la conexión se cierre:

   import asyncio

   class EchoClientProtocol(asyncio.Protocol):
       def __init__(self, message, on_con_lost):
           self.message = message
           self.on_con_lost = on_con_lost

       def connection_made(self, transport):
           transport.write(self.message.encode())
           print('Data sent: {!r}'.format(self.message))

       def data_received(self, data):
           print('Data received: {!r}'.format(data.decode()))

       def connection_lost(self, exc):
           print('The server closed the connection')
           self.on_con_lost.set_result(True)

   async def main():
       # Get a reference to the event loop as we plan to use
       # low-level APIs.
       loop = asyncio.get_running_loop()

       on_con_lost = loop.create_future()
       message = 'Hello World!'

       transport, protocol = await loop.create_connection(
           lambda: EchoClientProtocol(message, on_con_lost),
           '127.0.0.1', 8888)

       # Wait until the protocol signals that the connection
       # is lost and close the transport.
       try:
           await on_con_lost
       finally:
           transport.close()

   asyncio.run(main())

Ver también:

  El ejemplo Cliente de eco TCP usando streams usa la función de alto
  nivel "asyncio.open_connection()".

### Servidor de eco UDP

Un servidor de eco UDP, usando el método
"loop.create_datagram_endpoint()", envía de vuelta los datos
recibidos:

   import asyncio

   class EchoServerProtocol:
       def connection_made(self, transport):
           self.transport = transport

       def datagram_received(self, data, addr):
           message = data.decode()
           print('Received %r from %s' % (message, addr))
           print('Send %r to %s' % (message, addr))
           self.transport.sendto(data, addr)

   async def main():
       print("Starting UDP server")

       # Get a reference to the event loop as we plan to use
       # low-level APIs.
       loop = asyncio.get_running_loop()

       # One protocol instance will be created to serve all
       # client requests.
       transport, protocol = await loop.create_datagram_endpoint(
           EchoServerProtocol,
           local_addr=('127.0.0.1', 9999))

       try:
           await asyncio.sleep(3600)  # Serve for 1 hour.
       finally:
           transport.close()

   asyncio.run(main())

### Cliente de eco UDP

Un cliente de eco UDP, usando el método
"loop.create_datagram_endpoint()", envía datos y cierra el transporte
cuando recibe la respuesta:

   import asyncio

   class EchoClientProtocol:
       def __init__(self, message, on_con_lost):
           self.message = message
           self.on_con_lost = on_con_lost
           self.transport = None

       def connection_made(self, transport):
           self.transport = transport
           print('Send:', self.message)
           self.transport.sendto(self.message.encode())

       def datagram_received(self, data, addr):
           print("Received:", data.decode())

           print("Close the socket")
           self.transport.close()

       def error_received(self, exc):
           print('Error received:', exc)

       def connection_lost(self, exc):
           print("Connection closed")
           self.on_con_lost.set_result(True)

   async def main():
       # Get a reference to the event loop as we plan to use
       # low-level APIs.
       loop = asyncio.get_running_loop()

       on_con_lost = loop.create_future()
       message = "Hello World!"

       transport, protocol = await loop.create_datagram_endpoint(
           lambda: EchoClientProtocol(message, on_con_lost),
           remote_addr=('127.0.0.1', 9999))

       try:
           await on_con_lost
       finally:
           transport.close()

   asyncio.run(main())

### Conectando sockets existentes

Espera hasta que un socket reciba datos usando el método
"loop.create_connection()" mediante un protocolo:

   import asyncio
   import socket

   class MyProtocol(asyncio.Protocol):

       def __init__(self, on_con_lost):
           self.transport = None
           self.on_con_lost = on_con_lost

       def connection_made(self, transport):
           self.transport = transport

       def data_received(self, data):
           print("Received:", data.decode())

           # We are done: close the transport;
           # connection_lost() will be called automatically.
           self.transport.close()

       def connection_lost(self, exc):
           # The socket has been closed
           self.on_con_lost.set_result(True)

   async def main():
       # Get a reference to the event loop as we plan to use
       # low-level APIs.
       loop = asyncio.get_running_loop()
       on_con_lost = loop.create_future()

       # Create a pair of connected sockets
       rsock, wsock = socket.socketpair()

       # Register the socket to wait for data.
       transport, protocol = await loop.create_connection(
           lambda: MyProtocol(on_con_lost), sock=rsock)

       # Simulate the reception of data from the network.
       loop.call_soon(wsock.send, 'abc'.encode())

       try:
           await protocol.on_con_lost
       finally:
           transport.close()
           wsock.close()

   asyncio.run(main())

Ver también:

  El ejemplo monitorizar eventos de lectura en un descriptor de
  archivo utiliza el método de bajo nivel "loop.add_reader()" para
  registrar un descriptor de archivo.

  El ejemplo registrar un socket abierto a la espera de datos usando
  streams usa *streams* de alto nivel creados por la función
  "open_connection()" en una corrutina.

### *loop.subprocess_exec()* y *SubprocessProtocol*

Un ejemplo de un protocolo de subproceso que se utiliza para obtener
la salida de un subproceso y esperar su terminación.

El subproceso es creado por el método "loop.subprocess_exec()"

   import asyncio
   import sys

   class DateProtocol(asyncio.SubprocessProtocol):
       def __init__(self, exit_future):
           self.exit_future = exit_future
           self.output = bytearray()
           self.pipe_closed = False
           self.exited = False

       def pipe_connection_lost(self, fd, exc):
           self.pipe_closed = True
           self.check_for_exit()

       def pipe_data_received(self, fd, data):
           self.output.extend(data)

       def process_exited(self):
           self.exited = True
           # process_exited() method can be called before
           # pipe_connection_lost() method: wait until both methods are
           # called.
           self.check_for_exit()

       def check_for_exit(self):
           if self.pipe_closed and self.exited:
               self.exit_future.set_result(True)

   async def get_date():
       # Get a reference to the event loop as we plan to use
       # low-level APIs.
       loop = asyncio.get_running_loop()

       code = 'import datetime as dt; print(dt.datetime.now())'
       exit_future = asyncio.Future(loop=loop)

       # Create the subprocess controlled by DateProtocol;
       # redirect the standard output into a pipe.
       transport, protocol = await loop.subprocess_exec(
           lambda: DateProtocol(exit_future),
           sys.executable, '-c', code,
           stdin=None, stderr=None)

       # Wait for the subprocess exit using the process_exited()
       # method of the protocol.
       await exit_future

       # Close the stdout pipe.
       transport.close()

       # Read the output which was collected by the
       # pipe_data_received() method of the protocol.
       data = bytes(protocol.output)
       return data.decode('ascii').rstrip()

   date = asyncio.run(get_date())
   print(f"Current date: {date}")

Consulte también el mismo ejemplo escrito utilizando la API de alto
nivel.
