---
title: Índice de API de bajo nivel
source_url: https://docs.python.org/es/3
source_path: library/asyncio-llapi-index.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1650
---

# Índice de API de bajo nivel

Esta página enumera todas las APIs de asyncio de bajo nivel.

## Obtención del bucle de eventos

+----------------------------------------------------+----------------------------------------------------+
| "asyncio.get_running_loop()"                       | La función **preferida** para obtener el bucle de  |
## |                                                    | eventos en ejecución.                              |

| "asyncio.get_event_loop()"                         | Obtiene una instancia del bucle de eventos (en     |
## |                                                    | ejecución o actual mediante la política actual).   |

| "asyncio.set_event_loop()"                         | Establece el bucle de eventos como actual a través |
## |                                                    | de la política del bucle.                          |

## | "asyncio.new_event_loop()"                         | Crea un nuevo bucle de eventos.                    |

-[ Ejemplos ]-

* Usando asyncio.get_running_loop().

## Métodos del bucle de eventos

Consulte también la sección de documentación principal sobre Event
loop methods.

-[ Ciclo de vida ]-

+----------------------------------------------------+----------------------------------------------------+
| "loop.run_until_complete()"                        | Ejecuta un Future/Tarea/aguardable (*awaitable*)   |
## |                                                    | hasta que se complete.                             |

## | "loop.run_forever()"                               | Ejecuta el bucle de eventos para siempre.          |

## | "loop.stop()"                                      | Detiene el bucle de eventos.                       |

## | "loop.close()"                                     | Cierra el bucle de eventos.                        |

| "loop.is_running()"                                | Retorna "True" si el bucle de eventos se está      |
## |                                                    | ejecutando.                                        |

| "loop.is_closed()"                                 | Retorna "True" si el bucle de eventos está         |
## |                                                    | cerrado.                                           |

## | "await" "loop.shutdown_asyncgens()"                | Cierra generadores asincrónicos.                   |

-[ Depuración ]-

# | "loop.set_debug()"                                 | Habilita o deshabilita el modo de depuración.      |

## | "loop.get_debug()"                                 | Obtiene el modo de depuración actual.              |

-[ Programación de devoluciones de llamada ]-

# | "loop.call_soon()"                                 | Invoca una devolución de llamada *soon*.           |

| "loop.call_soon_threadsafe()"                      | Una variante segura para subprocesos de            |
## |                                                    | "loop.call_soon()".                                |

| "loop.call_later()"                                | Invoca una devolución de llamada *después* del     |
## |                                                    | tiempo especificado.                               |

| "loop.call_at()"                                   | Invoca una devolución de llamada *en* el tiempo    |
## |                                                    | especificado.                                      |

-[ Thread/Interpreter/Process Pool ]-

+----------------------------------------------------+----------------------------------------------------+
| "await" "loop.run_in_executor()"                   | Ejecuta una función de bloqueo vinculada a la CPU  |
|                                                    | o de otro tipo en un ejecutor                      |
## |                                                    | "concurrent.futures".                              |

| "loop.set_default_executor()"                      | Establece el ejecutor predeterminado para          |
## |                                                    | "loop.run_in_executor()".                          |

-[ Tareas y Futures ]-

# | "loop.create_future()"                             | Crea un objeto "Future".                           |

## | "loop.create_task()"                               | Programa una corrutina como "Task".                |

| "loop.set_task_factory()"                          | Establece una fábrica utilizada por                |
## |                                                    | "loop.create_task()" para crear "Tareas".          |

| "loop.get_task_factory()"                          | Obtiene la fábrica "loop.create_task()" que se usa |
## |                                                    | para crear "Tareas".                               |

-[ DNS ]-

# | "await" "loop.getaddrinfo()"                       | Versión asincrónica de "socket.getaddrinfo()".     |

## | "await" "loop.getnameinfo()"                       | Versión asincrónica de "socket.getnameinfo()".     |

-[ Redes e IPC ]-

# | "await" "loop.create_connection()"                 | Abre una conexión TCP.                             |

## | "await" "loop.create_server()"                     | Crea un servidor TCP.                              |

## | "await" "loop.create_unix_connection()"            | Abre una conexión de socket Unix.                  |

## | "await" "loop.create_unix_server()"                | Crea un servidor socket de Unix.                   |

| "await" "loop.connect_accepted_socket()"           | Envuelve un "socket" en un par "(transport,        |
## |                                                    | protocol)".                                        |

## | "await" "loop.create_datagram_endpoint()"          | Abre una conexión de datagramas (UDP).             |

## | "await" "loop.sendfile()"                          | Envía un archivo a través del transporte.          |

## | "await" "loop.start_tls()"                         | Actualiza una conexión existente a TLS.            |

| "await" "loop.connect_read_pipe()"                 | Envuelve el fin de lectura de *pipe* en un par     |
## |                                                    | "(transport, protocol)".                           |

| "await" "loop.connect_write_pipe()"                | Envuelve el fin de escritura de *pipe* en un par   |
## |                                                    | "(transport, protocol)".                           |

-[ Sockets ]-

# | "await" "loop.sock_recv()"                         | Recibe datos de "socket".                          |

## | "await" "loop.sock_recv_into()"                    | Recibe datos de "socket" en un buffer.             |

## | "await" "loop.sock_recvfrom()"                     | Recibe un datagrama desde "socket".                |

## | "await" "loop.sock_recvfrom_into()"                | Recibe un datagrama desde "socket" en un buffer.   |

## | "await" "loop.sock_sendall()"                      | Envía datos a "socket".                            |

| "await" "loop.sock_sendto()"                       | Envía un datagrama a través de "socket" a la       |
## |                                                    | dirección indicada.                                |

## | "await" "loop.sock_connect()"                      | Conecta con "socket".                              |

## | "await" "loop.sock_accept()"                       | Acepta una conexión "socket".                      |

## | "await" "loop.sock_sendfile()"                     | Envía un archivo a través de "socket".             |

| "loop.add_reader()"                                | Comienza a monitorear un descriptor de archivo     |
## |                                                    | para ver la disponibilidad de lectura.             |

| "loop.remove_reader()"                             | Detiene el monitoreo del descriptor de archivo     |
## |                                                    | para ver la disponibilidad de lectura.             |

| "loop.add_writer()"                                | Comienza a monitorear un descriptor de archivo     |
## |                                                    | para ver la disponibilidad de escritura.           |

| "loop.remove_writer()"                             | Detiene el monitoreo del descriptor de archivo     |
## |                                                    | para ver la disponibilidad de escritura.           |

-[ Señales Unix ]-

# | "loop.add_signal_handler()"                        | Añade un gestor para "signal".                     |

## | "loop.remove_signal_handler()"                     | Elimina un gestor para "signal".                   |

-[ Subprocesos ]-

# | "loop.subprocess_exec()"                           | Genera un subproceso.                              |

## | "loop.subprocess_shell()"                          | Genera un subproceso desde un comando de shell.    |

-[ Gestor de errores ]-

# | "loop.call_exception_handler()"                    | Invoca al gestor de excepciones.                   |

## | "loop.set_exception_handler()"                     | Establece un nuevo gestor de excepciones.          |

## | "loop.get_exception_handler()"                     | Obtiene el gestor de excepciones actual.           |

| "loop.default_exception_handler()"                 | La implementación predetermina del gestor de       |
## |                                                    | excepciones.                                       |

-[ Ejemplos ]-

* Usando asyncio.new_event_loop() y loop.run_forever().

* Usando loop.call_later().

* Usando "loop.create_connection()" para implementar un cliente de
  eco.

* Usando "loop.create_connection()" para conectar a un socket.

* Usando add_reader() para mirar un FD y leer eventos.

* Usando loop.add_signal_handler().

* Usando loop.subprocess_exec().

## Transportes

Todos los transportes implementan los siguientes métodos:

# | "transport.close()"                                | Cierra el transporte.                              |

| "transport.is_closing()"                           | Retorna "True" si el transporte está cerrado o se  |
## |                                                    | está cerrando.                                     |

## | "transport.get_extra_info()"                       | Solicita información sobre el transporte.          |

## | "transport.set_protocol()"                         | Establece un nuevo protocolo.                      |

## | "transport.get_protocol()"                         | Retorna el protocolo actual.                       |

Transportes que pueden recibir datos (conexiones TCP y Unix, *pipes*,
etc). Retornan de métodos como "loop.create_connection()",
"loop.create_unix_connection()", "loop.connect_read()", etc:

-[ Leer transportes ]-

# | "transport.is_reading()"                           | Retorna "True" si el transporte está recibiendo.   |

## | "transport.pause_reading()"                        | Pausa la recepción.                                |

## | "transport.resume_reading()"                       | Reanuda la recepción.                              |

Transportes que pueden enviar datos (conexiones TCP y Unix, *pipes*,
etc). Retornan de métodos como "loop.create_connection()",
"loop.create_unix_connection()", "loop.connect_write_pipe()", etc:

-[ Escribir transportes ]-

# | "transport.write()"                                | Escribe datos en el transporte.                    |

## | "transport.writelines()"                           | Escribe búferes en el transporte.                  |

| "transport.can_write_eof()"                        | Retorna "True" si el transporte admite el envío de |
## |                                                    | EOF.                                               |

| "transport.write_eof()"                            | Cierra y envía EOF después de vaciar los datos     |
## |                                                    | almacenados en búfer.                              |

## | "transport.abort()"                                | Cierra el transporte inmediatamente.               |

## | "transport.get_write_buffer_size()"                | Retorna el tamaño actual del búfer de salida.      |

| "transport.get_write_buffer_limits()"              | Retorna los límites superior e inferior para       |
## |                                                    | controlar el flujo de escritura.                   |

| "transport.set_write_buffer_limits()"              | Establece nuevos límites superior e inferior para  |
## |                                                    | el control del flujo de escritura.                 |

Transportes retornados por "loop.create_datagram_endpoint()":

-[ Transportes de datagramas ]-

# | "transport.sendto()"                               | Envía datos al par remoto.                         |

## | "transport.abort()"                                | Cierra el transporte inmediatamente.               |

Abstracción de transporte de bajo nivel sobre subprocesos. Retornado
por "loop.subprocess_exec()" y "loop.subprocess_shell()":

-[ Transportes de subprocesos ]-

# | "transport.get_pid()"                              | Retorna el id de proceso del subproceso.           |

| "transport.get_pipe_transport()"                   | Retorna el transporte para la *pipe* de            |
|                                                    | comunicación solicitada (*stdin*, *stdout* o       |
## |                                                    | *stderr*).                                         |

## | "transport.get_returncode()"                       | Retorna el código de retorno del subproceso.       |

## | "transport.kill()"                                 | Mata el subproceso.                                |

## | "transport.send_signal()"                          | Envía una señal al subproceso.                     |

## | "transport.terminate()"                            | Detiene el subproceso.                             |

## | "transport.close()"                                | Mata el subproceso y cierra todas las *pipes*.     |

## Protocolos

Las clases de protocolo pueden implementar los siguientes **métodos de
devolución de llamada**:

# | "callback" "connection_made()"                     | Se llama cuando se establece una conexión.         |

## | "callback" "connection_lost()"                     | Se llama cuando la conexión se pierde o cierra.    |

| "callback" "pause_writing()"                       | Se llama cuando el búfer del transporte excede el  |
## |                                                    | límite superior.                                   |

| "callback" "resume_writing()"                      | Se llama cuando el búfer del transporte se vacía   |
## |                                                    | por debajo del límite inferior.                    |

-[ Protocolos de streaming (TCP, Unix Sockets, Pipes) ]-

# | "callback" "data_received()"                       | Se llama cuando se reciben algunos datos.          |

## | "callback" "eof_received()"                        | Se llama cuando se recibe un EOF.                  |

-[ Protocolos de streaming en búfer ]-

# | "callback" "get_buffer()"                          | Se llama para asignar un nuevo búfer de recepción. |

| "callback" "buffer_updated()"                      | Se llama cuando el búfer se actualizó con los      |
## |                                                    | datos recibidos.                                   |

## | "callback" "eof_received()"                        | Se llama cuando se recibe un EOF.                  |

-[ Protocolos de datagramas ]-

# | "callback" "datagram_received()"                   | Se llama cuando se recibe un datagrama.            |

| "callback" "error_received()"                      | Se llama cuando una operación de envío o recepción |
## |                                                    | anterior genera un "OSError".                      |

-[ Protocolos de subprocesos ]-

+----------------------------------------------------+----------------------------------------------------+
| "callback" "pipe_data_received()"                  | Se llama cuando el proceso hijo escribe datos en   |
## |                                                    | su *pipe* *stdout* o *stderr*.                     |

| "callback" "pipe_connection_lost()"                | Se llama cuando se cierra un *pipe* que se         |
## |                                                    | comunica con el proceso hijo.                      |

| "callback" "process_exited()"                      | Called when the child process has exited. It can   |
|                                                    | be called before "pipe_data_received()" and        |
## |                                                    | "pipe_connection_lost()" methods.                  |

## Políticas de bucle de eventos

Las políticas son un mecanismo de bajo nivel para alterar el
comportamiento de funciones como "asyncio.get_event_loop()". Vea
también la sección principal políticas para más detalles.

-[ Acceso a políticas ]-

# | "asyncio.get_event_loop_policy()"                  | Retorna la política actual en todo el proceso.     |

## | "asyncio.set_event_loop_policy()"                  | Establece una nueva política para todo el proceso. |

## | "AbstractEventLoopPolicy"                          | Clase base para objetos de política.               |
