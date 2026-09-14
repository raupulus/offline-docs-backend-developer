---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/stream.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: false
translation_revision: 4de6272a1
order: 87730
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`STREAM_CLIENT_ASYNC_CONNECT` (`int`)  
Abre el socket cliente de manera asíncrona. Esta opción debe utilizarse con el flag `STREAM_CLIENT_CONNECT`.

`STREAM_CLIENT_CONNECT` (`int`)  
Abre la conexión del socket cliente. Los sockets cliente deben incluir siempre este flag.

`STREAM_CLIENT_PERSISTENT` (`int`)  
El socket cliente debe permanecer persistente entre las cargas de página.

<!-- -->

`STREAM_SERVER_BIND` (`int`)  
Indica que un flujo debe enlazarse al objetivo especificado. Los sockets servidor deben incluir siempre este flag.

`STREAM_SERVER_LISTEN` (`int`)  
Indica que un flujo enlazado con el flag `STREAM_SERVER_BIND` debe comenzar a escuchar el socket. Los transportes orientados a conexión (como TCP) deben utilizar este flag, de lo contrario el socket servidor no se activará. Utilizar este flag para transportes sin conexión (como UDP) es un error.

<!-- -->

`STREAM_SHUT_RD` (`int`)  
Desactivar las recepciones adicionales.

`STREAM_SHUT_WR` (`int`)  
Desactivar las transmisiones adicionales.

`STREAM_SHUT_RDWR` (`int`)  
Desactivar las recepciones y transmisiones adicionales.

<!-- -->

`STREAM_OOB` (`int`)  
Procesa los datos OOB (`fuera de banda`).

`STREAM_PEEK` (`int`)  
Recupera los datos del socket, pero sin consumir el búfer.

Las llamadas siguientes a `fread` o `stream_socket_recvfrom` verán los mismos datos.

> [!NOTE]
> No es un flag válido para `stream_socket_sendto`.

<!-- -->

`STREAM_FILTER_READ` (`int`)  
Indica que el filtro especificado debe aplicarse únicamente durante la *lectura*.

`STREAM_FILTER_WRITE` (`int`)  
Indica que el filtro especificado debe aplicarse únicamente durante la *escritura*.

`STREAM_FILTER_ALL` (`int`)  
Equivalente a `STREAM_FILTER_READ | STREAM_FILTER_WRITE`.

<!-- -->

`STREAM_CRYPTO_METHOD_ANY_CLIENT` (`int`)  
Cualquier versión de TLS o SSL en un flujo cliente.

`STREAM_CRYPTO_METHOD_SSLv2_CLIENT` (`int`)  
SSL 2 en un flujo cliente.

`STREAM_CRYPTO_METHOD_SSLv3_CLIENT` (`int`)  
SSL 3 en un flujo cliente.

`STREAM_CRYPTO_METHOD_SSLv23_CLIENT` (`int`)  
TLS 1.0, 1.1 o 1.2 en un flujo cliente.

`STREAM_CRYPTO_METHOD_TLS_CLIENT` (`int`)  
Cualquier versión de TLS en un flujo cliente.

`STREAM_CRYPTO_METHOD_TLSv1_0_CLIENT` (`int`)  
TLS 1.0 en un flujo cliente.

`STREAM_CRYPTO_METHOD_TLSv1_1_CLIENT` (`int`)  
TLS 1.1 en un flujo cliente.

`STREAM_CRYPTO_METHOD_TLSv1_2_CLIENT` (`int`)  
TLS 1.2 en un flujo cliente.

`STREAM_CRYPTO_METHOD_TLSv1_3_CLIENT` (`int`)  
TLS 1.3 en un flujo cliente.

`STREAM_CRYPTO_METHOD_ANY_SERVER` (`int`)  
Cualquier versión de TLS o SSL en un flujo servidor.

`STREAM_CRYPTO_METHOD_SSLv2_SERVER` (`int`)  
SSL 2 en un flujo servidor.

`STREAM_CRYPTO_METHOD_SSLv3_SERVER` (`int`)  
SSL 3 en un flujo servidor.

`STREAM_CRYPTO_METHOD_SSLv23_SERVER` (`int`)  
TLS 1.0, 1.1 o 1.2 en un flujo servidor.

`STREAM_CRYPTO_METHOD_TLS_SERVER` (`int`)  
Cualquier versión de TLS en un flujo servidor.

`STREAM_CRYPTO_METHOD_TLSv1_0_SERVER` (`int`)  
TLS 1.0 en un flujo servidor.

`STREAM_CRYPTO_METHOD_TLSv1_1_SERVER` (`int`)  
TLS 1.1 en un flujo servidor.

`STREAM_CRYPTO_METHOD_TLSv1_2_SERVER` (`int`)  
TLS 1.2 en un flujo servidor.

`STREAM_CRYPTO_METHOD_TLSv1_3_SERVER` (`int`)  
TLS 1.3 en un flujo servidor.

`STREAM_CRYPTO_PROTO_SSLv3` (`int`)  
Alias de `STREAM_CRYPTO_METHOD_SSLv3_SERVER`.

`STREAM_CRYPTO_PROTO_TLSv1_0` (`int`)  
Alias de `STREAM_CRYPTO_METHOD_TLSv1_0_SERVER`.

`STREAM_CRYPTO_PROTO_TLSv1_1` (`int`)  
Alias de `STREAM_CRYPTO_METHOD_TLSv1_1_SERVER`.

`STREAM_CRYPTO_PROTO_TLSv1_2` (`int`)  
Alias de `STREAM_CRYPTO_METHOD_TLSv1_2_SERVER`.

`STREAM_CRYPTO_PROTO_TLSv1_3` (`int`)  
Alias de `STREAM_CRYPTO_METHOD_TLSv1_3_SERVER`.

<!-- -->

`STREAM_MUST_SEEK` (`int`)  
Asegura que el flujo sea accesible en lectura/escritura. Esto puede provocar la creación de una copia del flujo.

`STREAM_IGNORE_URL` (`int`)  
No utilizar los wrappers de complementos.

## Constantes utilizadas con `stream_socket_pair`

> [!NOTE]
> No todas las constantes están necesariamente disponibles en un sistema dado.

`STREAM_PF_INET` (`int`)  
Protocolo de Internet Versión 4 (IPv4).

`STREAM_PF_INET6` (`int`)  
Protocolo de Internet Versión 6 (IPv6).

`STREAM_PF_UNIX` (`int`)  
Protocolos internos del sistema Unix.

<!-- -->

`STREAM_SOCK_DGRAM` (`int`)  
Proporciona datagramas, que son mensajes sin conexión. Por ejemplo: UDP.

`STREAM_SOCK_RAW` (`int`)  
Proporciona un socket crudo, dando acceso a los protocolos e interfaces de red internas. Generalmente, este tipo de socket está reservado para el usuario root.

`STREAM_SOCK_RDM` (`int`)  
Proporciona un socket RDM (mensajes entregados de manera confiable).

`STREAM_SOCK_SEQPACKET` (`int`)  
Proporciona un socket de flujo de paquetes secuenciados.

`STREAM_SOCK_STREAM` (`int`)  
Proporciona flujos bidireccionales secuenciados con un mecanismo de transmisión para los datos fuera de banda. Por ejemplo: TCP.

<!-- -->

`STREAM_IPPROTO_ICMP` (`int`)  
Proporciona un socket ICMP.

`STREAM_IPPROTO_IP` (`int`)  
Proporciona un socket IP.

`STREAM_IPPROTO_RAW` (`int`)  
Proporciona un socket RAW.

`STREAM_IPPROTO_TCP` (`int`)  
Proporciona un socket TCP.

`STREAM_IPPROTO_UDP` (`int`)  
Proporciona un socket UDP.

## Constantes utilizadas con `stream_notification_callback`

`STREAM_NOTIFY_RESOLVE` (`int`)  
Una dirección remota requerida para este flujo ha sido resuelta, o la resolución ha fallado.

Consulte `severity` para saber qué ha ocurrido.

> [!WARNING]
> El soporte para este código de notificación aún no está implementado.

`STREAM_NOTIFY_CONNECT` (`int`)  
Se ha establecido una conexión con un recurso externo.

`STREAM_NOTIFY_AUTH_REQUIRED` (`int`)  
Se requiere autorización adicional para acceder al recurso especificado.

Normalmente emitido con un nivel `severity` de `STREAM_NOTIFY_SEVERITY_ERR`.

`STREAM_NOTIFY_MIME_TYPE_IS` (`int`)  
Se ha identificado el `tipo MIME` del recurso.

Consulte `message` para una descripción del tipo descubierto.

`STREAM_NOTIFY_FILE_SIZE_IS` (`int`)  
Se ha descubierto el `tamaño` del recurso.

`STREAM_NOTIFY_REDIRECTED` (`int`)  
El recurso externo ha redirigido el flujo a otra ubicación.

Consulte `message`.

`STREAM_NOTIFY_PROGRESS` (`int`)  
Indica el progreso actual de la transferencia de flujo en `bytes_transferred` y eventualmente `bytes_max` también.

`STREAM_NOTIFY_COMPLETED` (`int`)  
No hay datos adicionales disponibles en el flujo. (Implementado por primera vez a partir de PHP 8.3.0.)

`STREAM_NOTIFY_FAILURE` (`int`)  
Ha ocurrido un error genérico en el flujo.

Consulte `message` y `message_code` para más detalles.

`STREAM_NOTIFY_AUTH_RESULT` (`int`)  
La autorización ha sido completada (con o sin éxito).

<!-- -->

`STREAM_NOTIFY_SEVERITY_INFO` (`int`)  
Notificación normal, sin relación con un error.

`STREAM_NOTIFY_SEVERITY_WARN` (`int`)  
Condición de error no crítica. El procesamiento puede continuar.

`STREAM_NOTIFY_SEVERITY_ERR` (`int`)  
Ha ocurrido un error crítico. El procesamiento no puede continuar.

## Constantes relacionadas con `streamWrapper`

`STREAM_IS_URL` (`int`)  
Indica que el protocolo de la interfaz de flujo es un protocolo URL.

<!-- -->

`STREAM_CAST_FOR_SELECT` (`int`)  
Indica que streamWrapper::stream_cast ha sido llamado por streamWrapper::stream_select.

`STREAM_CAST_AS_STREAM` (`int`)  
Indica que streamWrapper::stream_cast ha sido llamado por un método distinto de streamWrapper::stream_select.

<!-- -->

`STREAM_META_TOUCH` (`int`)  
Indica una llamada a `touch`.

`STREAM_META_OWNER` (`int`)  
Indica una llamada a `chown`.

`STREAM_META_OWNER_NAME` (`int`)  
Indica una llamada a `chown`.

`STREAM_META_GROUP` (`int`)  
Indica una llamada a `chgrp`.

`STREAM_META_GROUP_NAME` (`int`)  
Indica una llamada a `chgrp`.

`STREAM_META_ACCESS` (`int`)  
Indica una llamada a `chmod`.

<!-- -->

`STREAM_MKDIR_RECURSIVE` (`int`)  
Flag recursivo para los parámetros de opciones de `mkdir` y `rmdir`.

<!-- -->

`STREAM_USE_PATH` (`int`)  
Flag que indica que las rutas relativas deben utilizar la ruta de inclusión para localizar el recurso.

`STREAM_REPORT_ERRORS` (`int`)  
Flag que indica que la interfaz de flujo debe reportar errores. Si el flag no está definido, no se debe reportar ningún error.

Los errores generalmente se reportan mediante el uso de la función `trigger_error`.

<!-- -->

`STREAM_OPTION_BLOCKING` (`int`)  
Establece el modo de bloqueo/no bloqueo en un flujo.

`STREAM_OPTION_READ_BUFFER` (`int`)  
Establece el búfer de lectura en un flujo.

`STREAM_BUFFER_NONE` (`int`)  
Sin búfer.

`STREAM_BUFFER_LINE` (`int`)  
Búfer por línea.

`STREAM_BUFFER_FULL` (`int`)  
Búfer completo.

`STREAM_OPTION_READ_TIMEOUT` (`int`)  
Establece el tiempo de espera de lectura en un flujo.

`STREAM_OPTION_WRITE_BUFFER` (`int`)  
Establece el búfer de escritura en un flujo.

Ver `STREAM_OPTION_READ_BUFFER` para las opciones de búfer válidas.

<!-- -->

`STREAM_URL_STAT_LINK` (`int`)  
Solo se debe devolver información sobre el enlace en sí, y no sobre el recurso apuntado por el enlace.

`STREAM_URL_STAT_QUIET` (`int`)  
La interfaz de flujo no debe generar errores.

## Constantes relacionadas con `php_user_filter`

`PSFS_PASS_ON` (`int`)  
Valor de retorno que indica que el filtro de usuario ha devuelto cubos en `out`.

`PSFS_FEED_ME` (`int`)  
Valor de retorno que indica que el filtro de usuario no ha devuelto cubos en `out`. (es decir, no hay datos disponibles).

`PSFS_ERR_FATAL` (`int`)  
Valor de retorno que indica que el filtro de usuario ha encontrado un error irrecuperable. (es decir, datos no válidos recibidos).

<!-- -->

`PSFS_FLAG_NORMAL` (`int`)  
Lectura/escritura normal.

`PSFS_FLAG_FLUSH_INC` (`int`)  
Un vaciado incremental.

`PSFS_FLAG_FLUSH_CLOSE` (`int`)  
Vaciado final antes del cierre.
