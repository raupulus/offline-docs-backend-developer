---
title: Streams
source_url: https://docs.python.org/es/3
source_path: library/asyncio-stream.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1710
---

# Streams

**Código fuente:** Lib/asyncio/streams.py

======================================================================

Los *streams* son async/await primitivos de alto nivel para trabajar
con conexiones de red. Los *streams* permiten enviar y recibir datos
sin utilizar *callbacks* o protocolos y transportes de bajo nivel.

Aquí hay un ejemplo de un cliente eco TCP escrito utilizando *streams*
asyncio:

   import asyncio

   async def tcp_echo_client(message):
       reader, writer = await asyncio.open_connection(
           '127.0.0.1', 8888)

       print(f'Send: {message!r}')
       writer.write(message.encode())
       await writer.drain()

       data = await reader.read(100)
       print(f'Received: {data.decode()!r}')

       print('Close the connection')
       writer.close()
       await writer.wait_closed()

   asyncio.run(tcp_echo_client('Hello World!'))

Consulte también la sección de Examples a continuación.

-[ Funciones *stream* ]-

Las siguientes funciones asyncio de nivel superior se pueden utilizar
para crear y trabajar con *streams*:

async asyncio.open_connection(host=None, port=None, *, limit=None, ssl=None, family=0, proto=0, flags=0, sock=None, local_addr=None, server_hostname=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None, happy_eyeballs_delay=None, interleave=None)

   Establece una conexión de red y retorna un par de objetos "(reader,
   writer)".

   Los objetos *reader* y *writer* retornados son instancias de las
   clases "StreamReader" y "StreamWriter".

   *limit* determina el límite de tamaño del búfer utilizado por la
   instancia de "StreamReader" retornada. De forma predeterminada,
   *limit* está establecido en 64 KiB.

   El resto de los argumentos se pasan directamente a
   "loop.create_connection()".

   Nota:

     El argumento *sock* transfiere la propiedad del socket al
     "StreamWriter" creado. Para cerrar el socket, llame a su método
     "close()".

   Distinto en la versión 3.7: Se agregó el parámetro
   *ssl_handshake_timeout*.

   Distinto en la versión 3.8: Added the *happy_eyeballs_delay* and
   *interleave* parameters.

   Distinto en la versión 3.10: Se eliminó el parámetro *loop*.

   Distinto en la versión 3.11: Added the *ssl_shutdown_timeout*
   parameter.

async asyncio.start_server(client_connected_cb, host=None, port=None, *, limit=None, family=socket.AF_UNSPEC, flags=socket.AI_PASSIVE, sock=None, backlog=100, ssl=None, reuse_address=None, reuse_port=None, keep_alive=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None, start_serving=True)

   Inicia un servidor socket.

   La retrollamada *client_connected_cb* se llama siempre que se
   establece una nueva conexión de cliente. Recibe un par "(reader,
   writer)" como dos argumentos, instancias de las clases
   "StreamReader" y "StreamWriter".

   *client_connected_cb* puede ser una función simple invocable o de
   corrutina; si es una función de corrutina, se programará
   automáticamente como un "Task".

   *limit* determina el límite de tamaño del búfer utilizado por la
   instancia de "StreamReader" retornada. De forma predeterminada,
   *limit* está establecido en 64 KiB.

   El resto de los argumentos se pasan directamente a
   "loop.create_server()".

   Nota:

     El argumento *sock* transfiere la propiedad del socket al
     servidor creado. Para cerrar el socket, llame al método "close()"
     del servidor.

   Distinto en la versión 3.7: Se agregaron los parámetros
   *ssl_handshake_timeout* y *start_serving*.

   Distinto en la versión 3.10: Se eliminó el parámetro *loop*.

   Distinto en la versión 3.11: Added the *ssl_shutdown_timeout*
   parameter.

   Distinto en la versión 3.13: Added the *keep_alive* parameter.

-[ Sockets Unix ]-

async asyncio.open_unix_connection(path=None, *, limit=None, ssl=None, sock=None, server_hostname=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None)

   Establece una conexión de socket Unix y retorna un par de "(reader,
   writer)".

   Similar a "open_connection()" pero opera en sockets Unix.

   Consulte también la documentación de
   "loop.create_unix_connection()".

   Nota:

     El argumento *sock* transfiere la propiedad del socket al
     "StreamWriter" creado. Para cerrar el socket, llame a su método
     "close()".

   Availability: Unix.

   Distinto en la versión 3.7: Se agregó el parámetro
   *ssl_handshake_timeout*. El parámetro *path* ahora puede ser un
   *path-like object*

   Distinto en la versión 3.10: Se eliminó el parámetro *loop*.

   Distinto en la versión 3.11: Added the *ssl_shutdown_timeout*
   parameter.

async asyncio.start_unix_server(client_connected_cb, path=None, *, limit=None, sock=None, backlog=100, ssl=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None, start_serving=True, cleanup_socket=True)

   Inicia un servidor socket Unix.

   Similar a "start_server()" pero funciona con sockets Unix.

   If *cleanup_socket* is true then the Unix socket will automatically
   be removed from the filesystem when the server is closed, unless
   the socket has been replaced after the server has been created.

   Consulte también la documentación de "loop.create_unix_server()".

   Nota:

     El argumento *sock* transfiere la propiedad del socket al
     servidor creado. Para cerrar el socket, llame al método "close()"
     del servidor.

   Availability: Unix.

   Distinto en la versión 3.7: Se agregaron los parámetros
   *ssl_handshake_timeout* y *start_serving*. El parámetro *path*
   ahora puede ser un *path-like object*.

   Distinto en la versión 3.10: Se eliminó el parámetro *loop*.

   Distinto en la versión 3.11: Added the *ssl_shutdown_timeout*
   parameter.

   Distinto en la versión 3.13: Added the *cleanup_socket* parameter.

## StreamReader

class asyncio.StreamReader

   Represents a reader object that provides APIs to read data from the
   IO stream. As an *asynchronous iterable*, the object supports the
   "async for" statement.

   No se recomienda crear instancias de objetos *StreamReader*
   directamente; utilice "open_connection()" y "start_server()" en su
   lugar.

   feed_eof()

      Acknowledge the EOF.

   async read(n=-1)

      Read up to *n* bytes from the stream.

      If *n* is not provided or set to "-1", read until EOF, then
      return all read "bytes". If EOF was received and the internal
      buffer is empty, return an empty "bytes" object.

      If *n* is "0", return an empty "bytes" object immediately.

      If *n* is positive, return at most *n* available "bytes" as soon
      as at least 1 byte is available in the internal buffer. If EOF
      is received before any byte is read, return an empty "bytes"
      object.

   async readline()

      Lea una línea, donde "línea" es una secuencia de bytes que
      termina en "\n".

      Si se recibe EOF (final del archivo) y no se encontró "\n", el
      método retorna datos leídos parcialmente.

      Si se recibe EOF (final de archivo) y el búfer interno está
      vacío, retorna un objeto "bytes" vacío.

   async readexactly(n)

      Lee exactamente *n* bytes.

      Genera un "IncompleteReadError" si se alcanza EOF (final del
      archivo) antes de que se pueda leer *n*. Utilice el atributo
      "IncompleteReadError.partial" para obtener los datos leídos
      parcialmente.

   async readuntil(separator=b'\n')

      Lee datos de la secuencia hasta que se encuentre el separador
      (*separator*).

      En caso de éxito, los datos y el separador se eliminarán del
      búfer interno (consumido). Los datos retornados incluirán el
      separador al final.

      Si la cantidad de datos leídos excede el límite de flujo
      configurado, se genera una excepción "LimitOverrunError" y los
      datos se dejan en el búfer interno y se pueden leer nuevamente.

      Si se alcanza EOF (final del archivo) antes de que se encuentre
      el separador completo, se genera una excepción
      "IncompleteReadError" y se restablece el búfer interno. El
      atributo "IncompleteReadError.partial" puede contener una parte
      del separador.

      The *separator* may also be a tuple of separators. In this case
      the return value will be the shortest possible that has any
      separator as the suffix. For the purposes of
      "LimitOverrunError", the shortest possible separator is
      considered to be the one that matched.

      Added in version 3.5.2.

      Distinto en la versión 3.13: The *separator* parameter may now
      be a "tuple" of separators.

   at_eof()

      Retorna "True" si el buffer está vacío y "feed_eof()" fue
      llamado.

## StreamWriter

class asyncio.StreamWriter

   Representa un objeto de escritura que proporciona APIs para
   escribir datos en el flujo de E/S.

   No se recomienda crear instancias de objetos *StreamWriter*
   directamente; use "open_connection()" y "start_server()" en su
   lugar.

   write(data)

      El método intenta escribir los datos (*data*) en el socket
      subyacente inmediatamente. Si eso falla, los datos se ponen en
      cola en un búfer de escritura interno hasta que se puedan
      enviar.

      The *data* buffer should be a bytes, bytearray, or C-contiguous
      one-dimensional memoryview object.

      El método debe usarse junto con el método "drain()":

         stream.write(data)
         await stream.drain()

   writelines(data)

      El método escribe una lista (o cualquier iterable) de bytes en
      el socket subyacente inmediatamente. Si eso falla, los datos se
      ponen en cola en un búfer de escritura interno hasta que se
      puedan enviar.

      El método debe usarse junto con el método "drain()":

         stream.writelines(lines)
         await stream.drain()

   close()

      El método cierra la secuencia y el socket subyacente.

      The method should be used, though not mandatory, along with the
      "wait_closed()" method:

         stream.close()
         await stream.wait_closed()

   can_write_eof()

      Retorna "True" si el transporte subyacente admite el método
      "write_eof()", "False" en caso contrario.

   write_eof()

      Cierra la escritura de la secuencia después de que se vacíen los
      datos de escritura almacenados en búfer.

   transport

      Retorna el transporte asyncio subyacente.

   get_extra_info(name, default=None)

      Accede a información de transporte opcional; consulte
      "BaseTransport.get_extra_info()" para obtener más detalles.

   async drain()

      Espera hasta que sea apropiado reanudar la escritura en la
      transmisión. Ejemplo:

         writer.write(data)
         await writer.drain()

      Este es un método de control de flujo que interactúa con el
      búfer de escritura de E/S subyacente. Cuando el tamaño del búfer
      alcanza la marca de agua alta, *drain()* bloquea hasta que el
      tamaño del búfer se agota hasta la marca de agua baja y se pueda
      reanudar la escritura. Cuando no hay nada que esperar, "drain()"
      regresa inmediatamente.

   async start_tls(sslcontext, *, server_hostname=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None)

      Actualiza una conexión existente basada en flujo a TLS.

      Parámetros:

      * *sslcontext*: una instancia configurada de "SSLContext".

      * *server_hostname*: establece o sustituye el nombre de host con
        el que se comparará el certificado del servidor de destino.

      * *ssl_handshake_timeout* es el tiempo en segundos que se espera
        a que se complete el protocolo TLS antes de abortar la
        conexión.  "60.0" segundos si "None" (por defecto).

      * *ssl_shutdown_timeout* is the time in seconds to wait for the
        SSL shutdown to complete before aborting the connection.
        "30.0" seconds if "None" (default).

      Added in version 3.11.

      Distinto en la versión 3.12: Added the *ssl_shutdown_timeout*
      parameter.

   is_closing()

      Retorna "True" si la secuencia está cerrada o en proceso de
      cerrarse.

      Added in version 3.7.

   async wait_closed()

      Espera hasta que se cierre la secuencia.

      Should be called after "close()" to wait until the underlying
      connection is closed, ensuring that all data has been flushed
      before e.g. exiting the program.

      Added in version 3.7.

## Ejemplos

### Cliente eco TCP usando *streams*

Cliente eco TCP usando la función "asyncio.open_connection()":

   import asyncio

   async def tcp_echo_client(message):
       reader, writer = await asyncio.open_connection(
           '127.0.0.1', 8888)

       print(f'Send: {message!r}')
       writer.write(message.encode())
       await writer.drain()

       data = await reader.read(100)
       print(f'Received: {data.decode()!r}')

       print('Close the connection')
       writer.close()
       await writer.wait_closed()

   asyncio.run(tcp_echo_client('Hello World!'))

Ver también:

  El ejemplo del protocolo de cliente eco TCP utiliza el método
  "loop.create_connection()" de bajo nivel.

### Servidor eco TCP usando *streams*

Servidor eco TCP usando la función "asyncio.start_server()":

   import asyncio

   async def handle_echo(reader, writer):
       data = await reader.read(100)
       message = data.decode()
       addr = writer.get_extra_info('peername')

       print(f"Received {message!r} from {addr!r}")

       print(f"Send: {message!r}")
       writer.write(data)
       await writer.drain()

       print("Close the connection")
       writer.close()
       await writer.wait_closed()

   async def main():
       server = await asyncio.start_server(
           handle_echo, '127.0.0.1', 8888)

       addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
       print(f'Serving on {addrs}')

       async with server:
           await server.serve_forever()

   asyncio.run(main())

Ver también:

  El ejemplo del protocolo de servidor eco TCP utiliza el método
  "loop.create_server()".

### Obtener encabezados HTTP

Ejemplo simple de consulta de encabezados HTTP de la URL pasada en la
línea de comando:

   import asyncio
   import urllib.parse
   import sys

   async def print_http_headers(url):
       url = urllib.parse.urlsplit(url)
       if url.scheme == 'https':
           reader, writer = await asyncio.open_connection(
               url.hostname, 443, ssl=True)
       else:
           reader, writer = await asyncio.open_connection(
               url.hostname, 80)

       query = (
           f"HEAD {url.path or '/'} HTTP/1.0\r\n"
           f"Host: {url.hostname}\r\n"
           f"\r\n"
       )

       writer.write(query.encode('latin-1'))
       while True:
           line = await reader.readline()
           if not line:
               break

           line = line.decode('latin1').rstrip()
           if line:
               print(f'HTTP header> {line}')

       # Ignore the body, close the socket
       writer.close()
       await writer.wait_closed()

   url = sys.argv[1]
   asyncio.run(print_http_headers(url))

Uso:

   python example.py http://example.com/path/page.html

o con HTTPS:

   python example.py https://example.com/path/page.html

### Registrar un socket abierto para esperar datos usando *streams*

Corutina esperando hasta que un socket reciba datos usando la función
"open_connection()" function:

   import asyncio
   import socket

   async def wait_for_data():
       # Get a reference to the current event loop because
       # we want to access low-level APIs.
       loop = asyncio.get_running_loop()

       # Create a pair of connected sockets.
       rsock, wsock = socket.socketpair()

       # Register the open socket to wait for data.
       reader, writer = await asyncio.open_connection(sock=rsock)

       # Simulate the reception of data from the network
       loop.call_soon(wsock.send, 'abc'.encode())

       # Wait for data
       data = await reader.read(100)

       # Got data, we are done: close the socket
       print("Received:", data.decode())
       writer.close()
       await writer.wait_closed()

       # Close the second socket
       wsock.close()

   asyncio.run(wait_for_data())

Ver también:

  El ejemplo de registro de un socket abierto para esperar datos
  usando un protocolo utiliza un protocolo de bajo nivel y el método
  "loop.create_connection()".

  El ejemplo de observar un descriptor de archivo para leer eventos
  utiliza el método "loop.add_reader()" de bajo nivel para ver un
  descriptor de archivo.
