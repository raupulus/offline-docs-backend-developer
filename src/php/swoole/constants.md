---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/swoole.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_revision: 6047c10c1
order: 90380
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`SWOOLE_VERSION` (`string`)  
La versión de Swoole.

`SWOOLE_VERSION_ID` (`int`)  
La versión de Swoole.

`SWOOLE_MAJOR_VERSION` (`int`)  
La versión mayor de Swoole.

`SWOOLE_MINOR_VERSION` (`int`)  
La versión menor de Swoole.

`SWOOLE_RELEASE_VERSION` (`int`)  
La versión de lanzamiento de Swoole.

`SWOOLE_EXTRA_VERSION` (`string`)  
La versión extra de Swoole.

`SWOOLE_DEBUG` (`int`)  
El modo de depuración de Swoole.

`SWOOLE_HAVE_COMPRESSION` (`int`)  
Activa el modo de compresión de las respuestas HTTP.

`SWOOLE_HAVE_ZLIB` (`int`)  
Si la herramienta de compresión zlib está disponible.

`SWOOLE_HAVE_BROTLI` (`int`)  
Si la herramienta de compresión brotli está disponible.

`SWOOLE_USE_HTTP2` (`int`)  
El soporte para HTTP2.

`SWOOLE_USE_SHORTNAME` (`int`)  
Activa/desactiva los alias cortos.

`SWOOLE_SOCK_TCP` (`int`)  
El socket TCP ipv4.

`SWOOLE_SOCK_TCP6` (`int`)  
El socket TCP ipv6.

`SWOOLE_SOCK_UDP` (`int`)  
El socket UDP ipv4.

`SWOOLE_SOCK_UDP6` (`int`)  
El socket UDP ipv6.

`SWOOLE_SOCK_UNIX_DGRAM` (`int`)  
El socket UNIX dgram.

`SWOOLE_SOCK_UNIX_STREAM` (`int`)  
El socket UNIX stream.

`SWOOLE_SOCK_SYNC` (`int`)  
El modo cliente síncrono.

`SWOOLE_SOCK_ASYNC` (`int`)  
El modo cliente asíncrono.

`SWOOLE_KEEP` (`int`)  
Swoole\Client soporta la creación de una conexión TCP larga al servidor en PHP-FPM/Apache.

`SWOOLE_SSL` (`int`)  
Activa el cifrado SSL.

`SWOOLE_SSLv3_METHOD` (`int`)  
Método SSLv3.

`SWOOLE_SSLv3_SERVER_METHOD` (`int`)  
El método de servidor SSLv3.

`SWOOLE_SSLv3_CLIENT_METHOD` (`int`)  
El método de cliente SSLv3.

`SWOOLE_TLSv1_METHOD` (`int`)  
El método TLSv1.

`SWOOLE_TLSv1_SERVER_METHOD` (`int`)  
El método de servidor TLSv1.

`SWOOLE_TLSv1_CLIENT_METHOD` (`int`)  
El método de cliente TLSv1.

`SWOOLE_TLSv1_1_METHOD` (`int`)  
El método TLSv1_1.

`SWOOLE_TLSv1_1_SERVER_METHOD` (`int`)  
El método de servidor TLSv1_1.

`SWOOLE_TLSv1_1_CLIENT_METHOD` (`int`)  
El método de cliente TLSv1_1.

`SWOOLE_TLSv1_2_METHOD` (`int`)  
El método TLSv1_2.

`SWOOLE_TLSv1_2_SERVER_METHOD` (`int`)  
El método de servidor TLSv1_2.

`SWOOLE_TLSv1_2_CLIENT_METHOD` (`int`)  
El método de cliente TLSv1_2.

`SWOOLE_DTLS_SERVER_METHOD` (`int`)  
El método de servidor DTLS.

`SWOOLE_DTLS_CLIENT_METHOD` (`int`)  
El método de cliente DTLS.

`SWOOLE_SSLv23_METHOD` (`int`)  
El método SSLv23.

`SWOOLE_SSLv23_SERVER_METHOD` (`int`)  
El método de servidor SSLv23.

`SWOOLE_SSLv23_CLIENT_METHOD` (`int`)  
El método de cliente SSLv23.

`SWOOLE_TLS_METHOD` (`int`)  
El método TLS.

`SWOOLE_TLS_SERVER_METHOD` (`int`)  
El método de servidor TLS.

`SWOOLE_TLS_CLIENT_METHOD` (`int`)  
El método de cliente TLS.

`SWOOLE_SSL_SSLv3` (`int`)  
El protocolo SSLv3.

`SWOOLE_SSL_TLSv1` (`int`)  
El protocolo TLSv1.

`SWOOLE_SSL_TLSv1_1` (`int`)  
El protocolo TLSv1_1.

`SWOOLE_SSL_TLSv1_2` (`int`)  
El protocolo TLSv1_2.

`SWOOLE_SSL_TLSv1_3` (`int`)  
El protocolo TLSv1_3.

`SWOOLE_SSL_DTLS` (`int`)  
El protocolo DTLS.

`SWOOLE_SSL_SSLv2` (`int`)  
El protocolo SSLv2.

`SWOOLE_EVENT_READ` (`int`)  
Si es necesario escuchar los eventos de lectura.

`SWOOLE_EVENT_WRITE` (`int`)  
Si es necesario escuchar los eventos de escritura.

`SWOOLE_STRERROR_SYSTEM` (`int`)  
Convierte el número errno del sistema en mensajes de error.

`SWOOLE_STRERROR_GAI` (`int`)  
Convierte el número errno de la información de dirección en mensajes de error.

`SWOOLE_STRERROR_DNS` (`int`)  
Convierte el número errno de DNS en mensajes de error.

`SWOOLE_STRERROR_SWOOLE` (`int`)  
Convierte el número errno de Swoole en mensajes de error.

`SWOOLE_ERROR_MALLOC_FAIL` (`int`)  
Fallo en la asignación de memoria (MALLOC).

`SWOOLE_ERROR_SYSTEM_CALL_FAIL` (`int`)  
Fallo en la llamada al sistema.

`SWOOLE_ERROR_PHP_FATAL_ERROR` (`int`)  
Error fatal de PHP.

`SWOOLE_ERROR_NAME_TOO_LONG` (`int`)  
Nombre demasiado largo.

`SWOOLE_ERROR_INVALID_PARAMS` (`int`)  
Parámetros no válidos.

`SWOOLE_ERROR_QUEUE_FULL` (`int`)  
La cola está llena.

`SWOOLE_ERROR_OPERATION_NOT_SUPPORT` (`int`)  
Operación no soportada.

`SWOOLE_ERROR_PROTOCOL_ERROR` (`int`)  
Error de protocolo.

`SWOOLE_ERROR_WRONG_OPERATION` (`int`)  
Operación incorrecta.

`SWOOLE_ERROR_PHP_RUNTIME_NOTICE` (`int`)  
Aviso de ejecución de PHP.

`SWOOLE_ERROR_FOR_TEST` (`int`)  
Para pruebas.

`SWOOLE_ERROR_NO_PAYLOAD` (`int`)  
Sin carga útil.

`SWOOLE_ERROR_UNDEFINED_BEHAVIOR` (`int`)  
Comportamiento no definido.

`SWOOLE_ERROR_NOT_THREAD_SAFETY` (`int`)  
No es seguro para los hilos.

`SWOOLE_ERROR_FILE_NOT_EXIST` (`int`)  
El fichero no existe.

`SWOOLE_ERROR_FILE_TOO_LARGE` (`int`)  
Fichero demasiado grande.

`SWOOLE_ERROR_FILE_EMPTY` (`int`)  
Fichero vacío.

`SWOOLE_ERROR_DNSLOOKUP_DUPLICATE_REQUEST` (`int`)  
La solicitud de búsqueda DNS está duplicada.

`SWOOLE_ERROR_DNSLOOKUP_RESOLVE_FAILED` (`int`)  
La resolución DNS ha fallado.

`SWOOLE_ERROR_DNSLOOKUP_RESOLVE_TIMEOUT` (`int`)  
La resolución DNS ha tardado demasiado.

`SWOOLE_ERROR_DNSLOOKUP_UNSUPPORTED` (`int`)  
La resolución DNS no está soportada.

`SWOOLE_ERROR_DNSLOOKUP_NO_SERVER` (`int`)  
La resolución DNS no tiene servidor.

`SWOOLE_ERROR_BAD_IPV6_ADDRESS` (`int`)  
Dirección IPv6 incorrecta.

`SWOOLE_ERROR_UNREGISTERED_SIGNAL` (`int`)  
Señal no registrada.

`SWOOLE_ERROR_BAD_HOST_ADDR` (`int`)  
Dirección de host incorrecta.

`SWOOLE_ERROR_EVENT_SOCKET_REMOVED` (`int`)  
Socket de evento eliminado.

`SWOOLE_ERROR_SESSION_CLOSED_BY_SERVER` (`int`)  
La sesión ha sido cerrada por el servidor.

`SWOOLE_ERROR_SESSION_CLOSED_BY_CLIENT` (`int`)  
La sesión ha sido cerrada por el cliente.

`SWOOLE_ERROR_SESSION_CLOSING` (`int`)  
Cierre de sesión.

`SWOOLE_ERROR_SESSION_CLOSED` (`int`)  
Sesión cerrada.

`SWOOLE_ERROR_SESSION_NOT_EXIST` (`int`)  
La sesión no existe.

`SWOOLE_ERROR_SESSION_INVALID_ID` (`int`)  
La sesión tiene un ID inválido.

`SWOOLE_ERROR_SESSION_DISCARD_TIMEOUT_DATA` (`int`)  
Datos de sesión con tiempo de espera agotado.

`SWOOLE_ERROR_SESSION_DISCARD_DATA` (`int`)  
Datos de sesión descartados.

`SWOOLE_ERROR_OUTPUT_BUFFER_OVERFLOW` (`int`)  
Desbordamiento del búfer de salida.

`SWOOLE_ERROR_OUTPUT_SEND_YIELD` (`int`)  
Rendimiento de envío de salida.

`SWOOLE_ERROR_SSL_NOT_READY` (`int`)  
SSL no está listo.

`SWOOLE_ERROR_SSL_CANNOT_USE_SENFILE` (`int`)  
SSL no puede utilizar sendfile.

`SWOOLE_ERROR_SSL_EMPTY_PEER_CERTIFICATE` (`int`)  
SSL certificado de par vacío.

`SWOOLE_ERROR_SSL_VERIFY_FAILED` (`int`)  
SSL verificación fallida.

`SWOOLE_ERROR_SSL_BAD_CLIENT` (`int`)  
SSL cliente incorrecto.

`SWOOLE_ERROR_SSL_BAD_PROTOCOL` (`int`)  
SSL protocolo incorrecto.

`SWOOLE_ERROR_SSL_RESET` (`int`)  
SSL reiniciado.

`SWOOLE_ERROR_SSL_HANDSHAKE_FAILED` (`int`)  
SSL fallo en el apretón de manos.

`SWOOLE_ERROR_PACKAGE_LENGTH_TOO_LARGE` (`int`)  
Longitud de paquete demasiado grande.

`SWOOLE_ERROR_PACKAGE_LENGTH_NOT_FOUND` (`int`)  
Longitud de paquete no encontrada.

`SWOOLE_ERROR_DATA_LENGTH_TOO_LARGE` (`int`)  
Los datos son demasiado largos.

`SWOOLE_ERROR_PACKAGE_MALFORMED_DATA` (`int`)  
Error de datos de paquete mal formado.

`SWOOLE_ERROR_TASK_PACKAGE_TOO_BIG` (`int`)  
Paquete de tarea demasiado grande.

`SWOOLE_ERROR_TASK_DISPATCH_FAIL` (`int`)  
Distribución de tarea fallida.

`SWOOLE_ERROR_TASK_TIMEOUT` (`int`)  
Tiempo de espera de la tarea agotado.

`SWOOLE_ERROR_HTTP2_STREAM_ID_TOO_BIG` (`int`)  
El identificador del flujo HTTP2 es demasiado grande.

`SWOOLE_ERROR_HTTP2_STREAM_NO_HEADER` (`int`)  
El flujo HTTP2 no tiene encabezado.

`SWOOLE_ERROR_HTTP2_STREAM_NOT_FOUND` (`int`)  
El flujo HTTP2 no ha sido encontrado.

`SWOOLE_ERROR_HTTP2_STREAM_IGNORE` (`int`)  
El flujo HTTP2 es ignorado.

`SWOOLE_ERROR_HTTP2_SEND_CONTROL_FRAME_FAILED` (`int`)  
El envío del marco de control Http2 ha fallado.

`SWOOLE_ERROR_AIO_BAD_REQUEST` (`int`)  
Solicitud Aio incorrecta.

`SWOOLE_ERROR_AIO_CANCELED` (`int`)  
Aio cancelada.

`SWOOLE_ERROR_AIO_TIMEOUT` (`int`)  
Tiempo de espera Aio agotado.

`SWOOLE_ERROR_CLIENT_NO_CONNECTION` (`int`)  
El cliente no tiene conexión.

`SWOOLE_ERROR_SOCKET_CLOSED` (`int`)  
El socket ha sido cerrado.

`SWOOLE_ERROR_SOCKET_POLL_TIMEOUT` (`int`)  
Tiempo de espera del socket poll agotado.

`SWOOLE_ERROR_SOCKS5_UNSUPPORT_VERSION` (`int`)  
Versión no soportada de Socks5.

`SWOOLE_ERROR_SOCKS5_UNSUPPORT_METHOD` (`int`)  
Método no soportado de Socks5.

`SWOOLE_ERROR_SOCKS5_AUTH_FAILED` (`int`)  
La autenticación Socks5 ha fallado.

`SWOOLE_ERROR_SOCKS5_SERVER_ERROR` (`int`)  
Error del servidor Socks5.

`SWOOLE_ERROR_SOCKS5_HANDSHAKE_FAILED` (`int`)  
El apretón de manos Socks5 ha fallado.

`SWOOLE_ERROR_HTTP_PROXY_HANDSHAKE_ERROR` (`int`)  
Error de apretón de manos Http proxy.

`SWOOLE_ERROR_HTTP_INVALID_PROTOCOL` (`int`)  
Protocolo Http inválido.

`SWOOLE_ERROR_HTTP_PROXY_HANDSHAKE_FAILED` (`int`)  
Fallo en el apretón de manos Http proxy.

`SWOOLE_ERROR_HTTP_PROXY_BAD_RESPONSE` (`int`)  
Respuesta incorrecta Http proxy.

`SWOOLE_ERROR_HTTP_CONFLICT_HEADER` (`int`)  
Conflicto de encabezado Http.

`SWOOLE_ERROR_HTTP_CONTEXT_UNAVAILABLE` (`int`)  
Contexto Http no disponible.

`SWOOLE_ERROR_HTTP_COOKIE_UNAVAILABLE` (`int`)  
Cookie Http no disponible.

`SWOOLE_ERROR_WEBSOCKET_BAD_CLIENT` (`int`)  
Cliente Websocket incorrecto.

`SWOOLE_ERROR_WEBSOCKET_BAD_OPCODE` (`int`)  
Opcode Websocket incorrecto.

`SWOOLE_ERROR_WEBSOCKET_UNCONNECTED` (`int`)  
Websocket no conectado.

`SWOOLE_ERROR_WEBSOCKET_HANDSHAKE_FAILED` (`int`)  
El apretón de manos de Websocket ha fallado.

`SWOOLE_ERROR_WEBSOCKET_PACK_FAILED` (`int`)  
El empaquetado de Websocket ha fallado.

`SWOOLE_ERROR_WEBSOCKET_UNPACK_FAILED` (`int`)  
El desempaquetado de Websocket ha fallado.

`SWOOLE_ERROR_WEBSOCKET_INCOMPLETE_PACKET` (`int`)  
Paquete Websocket incompleto.

`SWOOLE_ERROR_SERVER_MUST_CREATED_BEFORE_CLIENT` (`int`)  
El servidor debe ser creado antes que el cliente.

`SWOOLE_ERROR_SERVER_TOO_MANY_SOCKET` (`int`)  
El servidor tiene demasiados sockets.

`SWOOLE_ERROR_SERVER_WORKER_TERMINATED` (`int`)  
El servidor de trabajo ha sido terminado.

`SWOOLE_ERROR_SERVER_INVALID_LISTEN_PORT` (`int`)  
Puerto de escucha del servidor inválido.

`SWOOLE_ERROR_SERVER_TOO_MANY_LISTEN_PORT` (`int`)  
El servidor tiene demasiados puertos de escucha.

`SWOOLE_ERROR_SERVER_PIPE_BUFFER_FULL` (`int`)  
El búfer de tubería del servidor está lleno.

`SWOOLE_ERROR_SERVER_NO_IDLE_WORKER` (`int`)  
El servidor no tiene trabajadores inactivos.

`SWOOLE_ERROR_SERVER_ONLY_START_ONE` (`int`)  
El servidor solo puede iniciarse una vez.

`SWOOLE_ERROR_SERVER_SEND_IN_MASTER` (`int`)  
Servidor enviado en el maestro.

`SWOOLE_ERROR_SERVER_INVALID_REQUEST` (`int`)  
Solicitud inválida del servidor.

`SWOOLE_ERROR_SERVER_CONNECT_FAIL` (`int`)  
Fallo en la conexión del servidor.

`SWOOLE_ERROR_SERVER_INVALID_COMMAND` (`int`)  
Comando inválido del servidor.

`SWOOLE_ERROR_SERVER_IS_NOT_REGULAR_FILE` (`int`)  
El servidor no es un archivo regular.

`SWOOLE_ERROR_SERVER_SEND_TO_WOKER_TIMEOUT` (`int`)  
Tiempo de espera agotado al enviar del servidor al trabajador.

`SWOOLE_ERROR_SERVER_INVALID_CALLBACK` (`int`)  
Función de devolución de llamada inválida del servidor.

`SWOOLE_ERROR_SERVER_UNRELATED_THREAD` (`int`)  
El servidor no está vinculado a un hilo.

`SWOOLE_ERROR_SERVER_WORKER_EXIT_TIMEOUT` (`int`)  
Tiempo de espera de salida del servidor de trabajo.

`SWOOLE_ERROR_SERVER_WORKER_ABNORMAL_PIPE_DATA` (`int`)  
Datos de pipe anormales del servidor de trabajo.

`SWOOLE_ERROR_SERVER_WORKER_UNPROCESSED_DATA` (`int`)  
Datos no procesados del servidor de trabajo.

`SWOOLE_ERROR_CO_OUT_OF_COROUTINE` (`int`)  
Corrutina fuera de corrutina.

`SWOOLE_ERROR_CO_HAS_BEEN_BOUND` (`int`)  
La corrutina ha sido vinculada.

`SWOOLE_ERROR_CO_HAS_BEEN_DISCARDED` (`int`)  
La corrutina ha sido descartada.

`SWOOLE_ERROR_CO_MUTEX_DOUBLE_UNLOCK` (`int`)  
El mutex de corrutina ha sido desbloqueado dos veces.

`SWOOLE_ERROR_CO_BLOCK_OBJECT_LOCKED` (`int`)  
El bloque de objeto de corrutina está bloqueado.

`SWOOLE_ERROR_CO_BLOCK_OBJECT_WAITING` (`int`)  
El bloque de objeto de corrutina está en espera.

`SWOOLE_ERROR_CO_YIELD_FAILED` (`int`)  
El rendimiento de la corrutina ha fallado.

`SWOOLE_ERROR_CO_GETCONTEXT_FAILED` (`int`)  
Getcontext de la corrutina ha fallado.

`SWOOLE_ERROR_CO_SWAPCONTEXT_FAILED` (`int`)  
Swapcontext de la corrutina ha fallado.

`SWOOLE_ERROR_CO_MAKECONTEXT_FAILED` (`int`)  
Makecontext de la corrutina ha fallado.

`SWOOLE_ERROR_CO_IOCPINIT_FAILED` (`int`)  
Iocpinit de la corrutina ha fallado.

`SWOOLE_ERROR_CO_PROTECT_STACK_FAILED` (`int`)  
Protect stack de la corrutina ha fallado.

`SWOOLE_ERROR_CO_STD_THREAD_LINK_ERROR` (`int`)  
Error de enlace de hilo std de corrutina.

`SWOOLE_ERROR_CO_DISABLED_MULTI_THREAD` (`int`)  
Desactiva el multi-hilo de corrutina.

`SWOOLE_ERROR_CO_CANNOT_CANCEL` (`int`)  
La corrutina no puede ser cancelada.

`SWOOLE_ERROR_CO_NOT_EXISTS` (`int`)  
La corrutina no existe.

`SWOOLE_ERROR_CO_CANCELED` (`int`)  
La coroutine ha sido cancelada.

`SWOOLE_ERROR_CO_TIMEDOUT` (`int`)  
La coroutine ha expirado.

`SWOOLE_ERROR_CO_SOCKET_CLOSE_WAIT` (`int`)  
Espera de cierre de socket de coroutine.

`SWOOLE_TRACE_SERVER` (`int`)  
Flag de registro del servidor.

`SWOOLE_TRACE_CLIENT` (`int`)  
Flag de registro del cliente.

`SWOOLE_TRACE_BUFFER` (`int`)  
Flag de registro del búfer.

`SWOOLE_TRACE_CONN` (`int`)  
Flag de registro de la conexión.

`SWOOLE_TRACE_EVENT` (`int`)  
Flag de registro de eventos.

`SWOOLE_TRACE_WORKER` (`int`)  
Flag de registro del trabajador.

`SWOOLE_TRACE_MEMORY` (`int`)  
Flag de registro de la memoria.

`SWOOLE_TRACE_REACTOR` (`int`)  
Flag de registro del reactor.

`SWOOLE_TRACE_PHP` (`int`)  
Flag de registro PHP.

`SWOOLE_TRACE_HTTP` (`int`)  
Flag de registro HTTP.

`SWOOLE_TRACE_HTTP2` (`int`)  
Flag de registro HTTP2.

`SWOOLE_TRACE_EOF_PROTOCOL` (`int`)  
Flag de registro del protocolo eof.

`SWOOLE_TRACE_LENGTH_PROTOCOL` (`int`)  
Flag de registro del protocolo de longitud.

`SWOOLE_TRACE_CLOSE` (`int`)  
Flag de registro de cierre.

`SWOOLE_TRACE_WEBSOCKET` (`int`)  
Flag de registro Websocket.

`SWOOLE_TRACE_REDIS_CLIENT` (`int`)  
Flag de registro del cliente Redis.

`SWOOLE_TRACE_MYSQL_CLIENT` (`int`)  
Flag de registro del cliente MySQL.

`SWOOLE_TRACE_HTTP_CLIENT` (`int`)  
Flag de registro del cliente HTTP.

`SWOOLE_TRACE_AIO` (`int`)  
Flag de registro AIO.

`SWOOLE_TRACE_SSL` (`int`)  
Flag de registro SSL.

`SWOOLE_TRACE_NORMAL` (`int`)  
Flag de registro normal.

`SWOOLE_TRACE_CHANNEL` (`int`)  
Flag de registro de canal.

`SWOOLE_TRACE_TIMER` (`int`)  
Flag de registro del temporizador.

`SWOOLE_TRACE_SOCKET` (`int`)  
Flag de registro de socket.

`SWOOLE_TRACE_COROUTINE` (`int`)  
Flag de registro de coroutine.

`SWOOLE_TRACE_CONTEXT` (`int`)  
Flag de registro de contexto.

`SWOOLE_TRACE_CO_HTTP_SERVER` (`int`)  
Flag de registro del servidor http de coroutine.

`SWOOLE_TRACE_TABLE` (`int`)  
Flag de registro de la tabla.

`SWOOLE_TRACE_CO_CURL` (`int`)  
Flag de registro de la coroutine curl.

`SWOOLE_TRACE_CARES` (`int`)  
Flag de registro de Cares.

`SWOOLE_TRACE_ZLIB` (`int`)  
Flag de registro zlib.

`SWOOLE_TRACE_CO_PGSQL` (`int`)  
Flag de registro de la coroutine pgsql.

`SWOOLE_TRACE_CO_ODBC` (`int`)  
Flag de registro de la coroutine odbc.

`SWOOLE_TRACE_CO_ORACLE` (`int`)  
Flag de registro de la coroutine oracle.

`SWOOLE_TRACE_CO_SQLITE` (`int`)  
Flag de registro de la coroutine sqlite.

`SWOOLE_TRACE_ALL` (`int`)  
Flag de registro de todos los niveles.

`SWOOLE_LOG_DEBUG` (`int`)  
Flag de registro de depuración.

`SWOOLE_LOG_TRACE` (`int`)  
Flag de registro de trace.

`SWOOLE_LOG_INFO` (`int`)  
Flag de registro de información.

`SWOOLE_LOG_NOTICE` (`int`)  
Flag de registro de notificación.

`SWOOLE_LOG_WARNING` (`int`)  
Flag de registro de advertencia.

`SWOOLE_LOG_ERROR` (`int`)  
Bandera de registro de errores.

`SWOOLE_LOG_NONE` (`int`)  
Equivale a desactivar las informaciones de registro, las informaciones de registro no serán lanzadas.

`SWOOLE_LOG_ROTATION_SINGLE` (`int`)  
Desactiva la rotación de los registros.

`SWOOLE_LOG_ROTATION_MONTHLY` (`int`)  
Gira los registros mensualmente.

`SWOOLE_LOG_ROTATION_DAILY` (`int`)  
Gira los registros diariamente.

`SWOOLE_LOG_ROTATION_HOURLY` (`int`)  
Gira los registros cada hora.

`SWOOLE_LOG_ROTATION_EVERY_MINUTE` (`int`)  
Gira los registros cada minuto.

`SWOOLE_IPC_NONE` (`int`)  
No utilizar mecanismo de comunicación interproceso (IPC).

`SWOOLE_IPC_UNIXSOCK` (`int`)  
Para la comunicación entre procesos (IPC), el uso de sockets Unix (UnixSocket) en modo corrutina es altamente recomendado.

`SWOOLE_IPC_SOCKET` (`int`)  
Para la comunicación entre procesos (IPC), el método listen debe ser llamado para especificar la dirección y el puerto a monitorear.

`SWOOLE_IOV_MAX` (`int`)  
El límite MAX de iov.

`SWOOLE_IOURING_DEFAULT` (`int`)  
En modo interrupt-driven, las I/O son enviadas a través de la llamada al sistema io_uring_enter, y la finalización es determinada verificando directamente el estado de la cola de finalización.

`SWOOLE_IOURING_SQPOLL` (`int`)  
En modo de interrogación del núcleo, el núcleo crea hilos dedicados para enviar y recolectar las solicitudes I/O, eliminando casi los cambios de contexto entre el usuario y el núcleo.

`SWOOLE_BASE` (`int`)  
Modo básico.

`SWOOLE_PROCESS` (`int`)  
Modo multi-processus.

`SWOOLE_THREAD` (`int`)  
Modo multi-thread.

`SWOOLE_IPC_UNSOCK` (`int`)  
El proceso de tarea comunica con el proceso de trabajo utilizando un socket Unix.

`SWOOLE_IPC_MSGQUEUE` (`int`)  
El proceso de tarea comunica con el proceso de trabajo utilizando una cola de mensajes Sysv.

`SWOOLE_IPC_PREEMPTIVE` (`int`)  
El proceso de tarea comunica con el proceso de trabajo utilizando un modo preemptivo sobre una cola de mensajes sysvmsg.

`SWOOLE_SERVER_COMMAND_MASTER` (`int`)  
El proceso maestro acepta las solicitudes.

`SWOOLE_SERVER_COMMAND_MANAGER` (`int`)  
El proceso de gestión acepta las solicitudes.

`SWOOLE_SERVER_COMMAND_REACTOR_THREAD` (`int`)  
El hilo Reactor acepta las solicitudes.

`SWOOLE_SERVER_COMMAND_EVENT_WORKER` (`int`)  
El proceso de trabajador de eventos acepta las solicitudes.

`SWOOLE_SERVER_COMMAND_TASK_WORKER` (`int`)  
El proceso de trabajador de tareas acepta las solicitudes.

`SWOOLE_DISPATCH_ROUND` (`int`)  
Modo round robin, cada proceso Worker será asignado secuencialmente para cada conexión recibida.

`SWOOLE_DISPATCH_FDMOD` (`int`)  
Asigna el Worker en función del descriptor de archivo de la conexión. Esto garantiza que los datos de la misma conexión serán tratados por el mismo Worker únicamente.

`SWOOLE_DISPATCH_IDLE_WORKER` (`int`)  
El proceso principal elegirá la entrega en función del estado de carga de trabajo del Worker, entregando únicamente a los Workers inactivos.

`SWOOLE_DISPATCH_IPMOD` (`int`)  
Asignación basada en la IP del cliente utilizando un hachado módulo, asignando a un proceso Worker específico. Esto asegura que los datos de la misma conexión de IP fuente serán siempre asignados al mismo proceso Worker. Algoritmo: inet_addr_mod(ClientIP, worker_num).

`SWOOLE_DISPATCH_UIDMOD` (`int`)  
Requiere la asignación de un uid único llamando a Server-\>bind() en el código del usuario. Luego, el sistema subyacente asigna a diferentes procesos Worker en función del valor del UID. Algoritmo: UID % worker_num. Para usar strings como UID, puede utilizarse crc32(UID_STRING).

`SWOOLE_DISPATCH_USERFUNC` (`int`)  
Define una función de retorno dispatch_func, donde el valor de retorno determina qué proceso maneja la solicitud.

`SWOOLE_DISPATCH_CO_CONN_LB` (`int`)  
Determina qué proceso maneja la solicitud en función del número de conexiones.

`SWOOLE_DISPATCH_CO_REQ_LB` (`int`)  
Determina qué proceso maneja la solicitud en función del número de solicitudes.

`SWOOLE_DISPATCH_CONCURRENT_LB` (`int`)  
Determina qué proceso maneja la solicitud en función del número de conexiones y solicitudes.

`SWOOLE_WORKER_BUSY` (`int`)  
El proceso está ocupado.

`SWOOLE_WORKER_IDLE` (`int`)  
El proceso está inactivo.

`SWOOLE_WORKER_EXIT` (`int`)  
El proceso ha finalizado.

`SWOOLE_MUTEX` (`int`)  
Bloqueo Mutex.

`SWOOLE_RWLOCK` (`int`)  
Bloqueo RW.

`SWOOLE_SPINLOCK` (`int`)  
Bloqueo de espera activa (spinlock).

`SWOOLE_CORO_MAX_NUM_LIMIT` (`int`)  
El número máximo de corrutinas creadas (PHP_INT_MAX).

`SWOOLE_CORO_INIT` (`int`)  
Inicialización de corrutina.

`SWOOLE_CORO_WAITING` (`int`)  
Rendimiento de la corrutina.

`SWOOLE_CORO_RUNNING` (`int`)  
Completación de la corrutina.

`SWOOLE_CORO_END` (`int`)  
Corrutina completada.

`SWOOLE_EXIT_IN_COROUTINE` (`int`)  
Ejecuta la función exit() en la corrutina.

`SWOOLE_EXIT_IN_SERVER` (`int`)  
Ejecuta la función exit() en el servidor.

`SWOOLE_HTTP2_TYPE_DATA` (`int`)  
Trama de datos HTTP2.

`SWOOLE_HTTP2_TYPE_HEADERS` (`int`)  
Trama de encabezados HTTP2.

`SWOOLE_HTTP2_TYPE_PRIORITY` (`int`)  
Trama de prioridad HTTP2.

`SWOOLE_HTTP2_TYPE_RST_STREAM` (`int`)  
Trama de rst de flujo HTTP2.

`SWOOLE_HTTP2_TYPE_SETTINGS` (`int`)  
Trama de parámetros HTTP2.

`SWOOLE_HTTP2_TYPE_PUSH_PROMISE` (`int`)  
Trama de promesa de empuje HTTP2.

`SWOOLE_HTTP2_TYPE_PING` (`int`)  
Trama de ping HTTP2.

`SWOOLE_HTTP2_TYPE_GOAWAY` (`int`)  
Trama de goaway HTTP2.

`SWOOLE_HTTP2_TYPE_WINDOW_UPDATE` (`int`)  
Trama de actualización de ventana HTTP2.

`SWOOLE_HTTP2_TYPE_CONTINUATION` (`int`)  
Trama de continuación HTTP2.

`SWOOLE_HTTP2_ERROR_NO_ERROR` (`int`)  
Ningún error HTTP2.

`SWOOLE_HTTP2_ERROR_PROTOCOL_ERROR` (`int`)  
Error de protocolo HTTP2.

`SWOOLE_HTTP2_ERROR_INTERNAL_ERROR` (`int`)  
Error interno HTTP2.

`SWOOLE_HTTP2_ERROR_FLOW_CONTROL_ERROR` (`int`)  
Error de control de flujo HTTP2.

`SWOOLE_HTTP2_ERROR_SETTINGS_TIMEOUT` (`int`)  
Error de tiempo de espera de los parámetros HTTP2.

`SWOOLE_HTTP2_ERROR_STREAM_CLOSED` (`int`)  
Error de flujo HTTP2 cerrado.

`SWOOLE_HTTP2_ERROR_FRAME_SIZE_ERROR` (`int`)  
Error de tamaño de trama HTTP2.

`SWOOLE_HTTP2_ERROR_REFUSED_STREAM` (`int`)  
Error de flujo rechazado HTTP2.

`SWOOLE_HTTP2_ERROR_CANCEL` (`int`)  
Error de cancelación HTTP2.

`SWOOLE_HTTP2_ERROR_COMPRESSION_ERROR` (`int`)  
Error de compresión HTTP2.

`SWOOLE_HTTP2_ERROR_CONNECT_ERROR` (`int`)  
Error de conexión HTTP2.

`SWOOLE_HTTP2_ERROR_ENHANCE_YOUR_CALM` (`int`)  
Error enhance your calm HTTP2.

`SWOOLE_HTTP2_ERROR_INADEQUATE_SECURITY` (`int`)  
Error de seguridad inadecuada HTTP2.

`SWOOLE_HTTP2_ERROR_HTTP_1_1_REQUIRED` (`int`)  
Error HTTP2 requiere http1.1.

`SWOOLE_HTTP_CLIENT_ESTATUS_CONNECT_FAILED` (`int`)  
Expiración de la conexión, el servidor no escucha en el puerto o hay una falla en la red, se puede leer \$errCode para obtener el código de error de red específico.

`SWOOLE_HTTP_CLIENT_ESTATUS_REQUEST_TIMEOUT` (`int`)  
Expiración de la petición, el servidor no ha devuelto una respuesta en el tiempo especificado.

`SWOOLE_HTTP_CLIENT_ESTATUS_SERVER_RESET` (`int`)  
Después de que la petición del cliente sea enviada, el servidor ha forzado la desconexión de la conexión.

`SWOOLE_HTTP_CLIENT_ESTATUS_SEND_FAILED` (`int`)  
Fallo al enviar al cliente (esta constante está disponible en Swoole versión \>= v4.5.9, anteriormente, se utilizaba el código de estado).

`SWOOLE_MSGQUEUE_ORIENT` (`int`)  
Swoole\Process::pop() va a devolver un dato específico en la cola con el tipo de mensaje como id del proceso + 1, Swoole\Process::pusl() va a añadir el tipo de mensaje id del proceso + 1 al dato.

`SWOOLE_MSGQUEUE_BALANCE` (`int`)  
Swoole\Process::pop() devuelve el primer mensaje en la cola, Swoole\Process::push() no añade un tipo específico al mensaje.

`SWOOLE_HOOK_TCP` (`int`)  
Flujo basado en corrutina de tipo TCP Socket, incluyendo los tipos más comunes como Redis, PDO, Mysqli.

`SWOOLE_HOOK_UDP` (`int`)  
Flujo basado en corrutina de tipo UDP Socket.

`SWOOLE_HOOK_UNIX` (`int`)  
Flujo basado en corrutina de tipo Unix Socket.

`SWOOLE_HOOK_UDG` (`int`)  
Flujo basado en corrutina de tipo UDG Stream Socket.

`SWOOLE_HOOK_SSL` (`int`)  
Flujo basado en corrutina de tipo SSL Stream Socket.

`SWOOLE_HOOK_TLS` (`int`)  
Flujo basado en corrutina de tipo TLS Stream Socket.

`SWOOLE_HOOK_STREAM_FUNCTION` (`int`)  
Flujo basado en corrutina para las funciones stream\_\*.

`SWOOLE_HOOK_FILE` (`int`)  
Fichero basado en corrutina para las funciones de ficheros.

`SWOOLE_HOOK_STDIO` (`int`)  
Operaciones STDIO basadas en corrutina.

`SWOOLE_HOOK_SLEEP` (`int`)  
Operaciones de sueño basadas en corrutina, incluyendo sleep, usleep, time_nanosleep, time_sleep_until.

`SWOOLE_HOOK_PROC` (`int`)  
Funciones proc\* basadas en corrutina, incluyendo: proc_open, proc_close, proc_get_status, proc_terminate.

`SWOOLE_HOOK_CURL` (`int`)  
Extensión curl basada en corrutina.

`SWOOLE_HOOK_NATIVE_CURL` (`int`)  
Extensión curl nativa basada en corrutina.

`SWOOLE_HOOK_BLOCKING_FUNCTION` (`int`)  
Función no bloqueante basada en corrutina, incluyendo: gethostbyname, exec, shell_exec.

`SWOOLE_HOOK_SOCKETS` (`int`)  
Extensión sockets basada en corrutina.

`SWOOLE_HOOK_PDO_PGSQL` (`int`)  
Extensión pdo_pgsql basada en corrutina.

`SWOOLE_HOOK_PDO_ODBC` (`int`)  
Extensión pdo_odbc basada en corrutina.

`SWOOLE_HOOK_PDO_ORACLE` (`int`)  
Extensión pdo_oracle basada en corrutina.

`SWOOLE_HOOK_PDO_SQLITE` (`int`)  
Extensión pdo_sqlite basada en corrutina.

`SWOOLE_HOOK_ALL` (`int`)  
Todos los bloques de funciones y extensiones basadas en corrutina.

`SOCKET_ECANCELED` (`int`)  
Error de socket ecanceled.

`TCP_INFO` (`int`)  
TCP_INFO.

`SWOOLE_TIMER_MIN_MS` (`int`)  
El mínimo del intervalo de temporizador soportado (en milisegundos).

`SWOOLE_TIMER_MIN_SEC` (`double`)  
El mínimo del intervalo de temporizador admitido (en segundos).

`SWOOLE_TIMER_MAX_MS` (`int`)  
El máximo del intervalo de temporizador admitido (en milisegundos).

`SWOOLE_TIMER_MAX_SEC` (`int`)  
El máximo del intervalo de temporizador admitido (en segundos).

`SWOOLE_WEBSOCKET_STATUS_CONNECTION` (`int`)  
WebSocket se encuentra en fase de conexión.

`SWOOLE_WEBSOCKET_STATUS_HANDSHAKE` (`int`)  
El WebSocket se encuentra en fase de apretón de manos.

`SWOOLE_WEBSOCKET_STATUS_ACTIVE` (`int`)  
Conexión WebSocket activa.

`SWOOLE_WEBSOCKET_STATUS_CLOSING` (`int`)  
La conexión WebSocket está cerrada.

`SWOOLE_WEBSOCKET_OPCODE_CONTINUATION` (`int`)  
Trama de continuación WebSocket.

`SWOOLE_WEBSOCKET_OPCODE_TEXT` (`int`)  
Trama de texto WebSocket.

`SWOOLE_WEBSOCKET_OPCODE_BINARY` (`int`)  
Trama binaria WebSocket.

`SWOOLE_WEBSOCKET_OPCODE_CLOSE` (`int`)  
Trama de cierre WebSocket.

`SWOOLE_WEBSOCKET_OPCODE_PING` (`int`)  
Trama de ping WebSocket.

`SWOOLE_WEBSOCKET_OPCODE_PONG` (`int`)  
Trama de pong WebSocket.

`SWOOLE_WEBSOCKET_FLAG_FIN` (`int`)  
Flag FIN WebSocket.

`SWOOLE_WEBSOCKET_FLAG_RSV1` (`int`)  
Flag RSV1 WebSocket.

`SWOOLE_WEBSOCKET_FLAG_RSV2` (`int`)  
Flag RSV2 WebSocket.

`SWOOLE_WEBSOCKET_FLAG_RSV3` (`int`)  
Flag RSV3 WebSocket.

`SWOOLE_WEBSOCKET_FLAG_MASK` (`int`)  
Flag MASK WebSocket.

`SWOOLE_WEBSOCKET_FLAG_COMPRESS` (`int`)  
Flag COMPRESS WebSocket.

`SWOOLE_WEBSOCKET_CLOSE_NORMAL` (`int`)  
Cierre normal (la conexión ha finalizado con éxito).

`SWOOLE_WEBSOCKET_CLOSE_GOING_AWAY` (`int`)  
El punto final se ha ido (por ejemplo, pestaña del navegador cerrada).

`SWOOLE_WEBSOCKET_CLOSE_PROTOCOL_ERROR` (`int`)  
Error de protocolo (trama de datos malformada).

`SWOOLE_WEBSOCKET_CLOSE_DATA_ERROR` (`int`)  
Recepción de datos no soportada (por ejemplo, binaria cuando se espera texto).

`SWOOLE_WEBSOCKET_CLOSE_STATUS_ERROR` (`int`)  
No se ha proporcionado código de estado (enviado como un espacio reservado).

`SWOOLE_WEBSOCKET_CLOSE_ABNORMAL` (`int`)  
Cierre anormal (ninguna trama de cierre recibida, por ejemplo, reinicialización TCP).

`SWOOLE_WEBSOCKET_CLOSE_MESSAGE_ERROR` (`int`)  
Datos inválidos (por ejemplo, texto no-UTF-8 en una trama de texto).

`SWOOLE_WEBSOCKET_CLOSE_POLICY_ERROR` (`int`)  
Violación de la política (por ejemplo, acción no autorizada).

`SWOOLE_WEBSOCKET_CLOSE_MESSAGE_TOO_BIG` (`int`)  
Mensaje demasiado grande (supera el tamaño máximo del servidor).

`SWOOLE_WEBSOCKET_CLOSE_EXTENSION_MISSING` (`int`)  
El cliente no ha negociado las extensiones requeridas.

`SWOOLE_WEBSOCKET_CLOSE_SERVER_ERROR` (`int`)  
El servidor ha encontrado un error.

`SWOOLE_WEBSOCKET_CLOSE_CLOSE_SERVICE_RESTART` (`int`)  
El servicio se reinicia (condición temporal).

`SWOOLE_WEBSOCKET_CLOSE_TRY_AGAIN_LATER` (`int`)  
El servidor está temporalmente sobrecargado (el cliente debería reintentar).

`SWOOLE_WEBSOCKET_CLOSE_BAD_GATEWAY` (`int`)  
Respuesta inválida del servidor en amont.

`SWOOLE_WEBSOCKET_CLOSE_TLS` (`int`)  
El apretón de manos TLS ha fallado (utilizado cuando HTTPS falla).
