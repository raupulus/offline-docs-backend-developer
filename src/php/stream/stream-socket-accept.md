---
title: stream_socket_accept
description: Acepta una conexión en un socket creado por stream_socket_server
source_url: https://www.php.net/manual/es/function.stream-socket-accept.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-socket-accept.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: c3067ab0a
order: 88120
---

stream_socket_accept

Acepta una conexión en un socket creado por

stream_socket_server

## Descripción

```php
stream_socket_accept(resource $socket, [float $timeout], [string $peer_name]): resource
```php

Acepta una conexión en un socket creado previamente con `stream_socket_server`.

## Parámetros

`socket`  
El socket servidor desde el cual aceptar una conexión.

`timeout`  
Reemplaza el tiempo de espera predeterminado del socket. Este tiempo debe ser proporcionado en segundos. Por omisión, se utiliza [default_socket_timeout](#ini.default-socket-timeout).

`peer_name`  
El nombre (dirección) del cliente conectado, si se proporciona y si está disponible para el transporte seleccionado.

> [!NOTE]
> Asimismo puede ser determinado más tarde, utilizando la función `stream_socket_get_name`.

## Valores devueltos

Devuelve un flujo hacia la conexión socket aceptada o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                  |
|---------|------------------------------|
| 8.0.0   | `timeout` ahora es nullable. |

## Notas

> [!WARNING]
> Esta función no debe ser utilizada con sockets servidor UDP. En su lugar, utilice las funciones `stream_socket_recvfrom` y `stream_socket_sendto`.

## Véase también

`stream_socket_server`, `stream_socket_get_name`, `stream_set_blocking`, `stream_set_timeout`, `fgets`, `fgetss`, `fwrite`, `fclose`, `feof`, [???](#ref.curl)
