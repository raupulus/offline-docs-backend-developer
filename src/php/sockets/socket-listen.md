---
title: socket_listen
description: Espera una conexión en un socket
source_url: https://www.php.net/manual/es/function.socket-listen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-listen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: 14dc7c473
order: 75730
---

socket_listen

Espera una conexión en un socket

## Descripción

```php
socket_listen(Socket $socket, [int $backlog]): bool
```php

Una vez que el socket `socket` ha sido creado con la función `socket_create` y vinculado a un nombre con la función `socket_bind`, puede ponerse en espera de la conexión entrante.

`socket_listen` solo funciona con sockets de tipo `SOCK_STREAM` y `SOCK_SEQPACKET`.

## Parámetros

`socket`  
Una instancia de `Socket` creada por `socket_create` o `socket_addrinfo_bind`.

`backlog`  
Un número máximo de `backlog` conexiones serán puestas en espera de procesamiento. Si una solicitud de conexión llega y la cola está llena, el cliente recibirá un error indicando `ECONNREFUSED`, o, si el protocolo de soporte acepta retransmisiones, la solicitud será ignorada para que los intentos posteriores finalmente tengan éxito.

> [!NOTE]
> El número máximo pasado en el parámetro `backlog` depende principalmente de la plataforma de soporte. En Linux, se trunca automáticamente a `SOMAXCONN`. En Windows, si la constante `SOMAXCONN` es pasada, el servicio responsable de los sockets elegirá un valor máximo *razonable*. No hay método para adivinar el valor realmente elegido.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. El código de error generado puede obtenerse llamando a la función `socket_last_error`. Este código de error puede pasarse a la función `socket_strerror` para obtener un mensaje de error legible por humanos.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `socket` ahora es una instancia de `Socket` ; anteriormente, era un `resource`. |

## Véase también

`socket_accept`, `socket_bind`, `socket_connect`, `socket_create`, `socket_strerror`, `socket_addrinfo_bind`
