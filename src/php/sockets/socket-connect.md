---
title: socket_connect
description: Crea una conexión en un socket
source_url: https://www.php.net/manual/es/function.socket-connect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-connect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: e58f2f647
order: 75620
---

socket_connect

Crea una conexión en un socket

## Descripción

```php
socket_connect(Socket $socket, string $address, [int $port]): bool
```php

Crea una nueva conexión utilizando la instancia `Socket` `socket`, que debe ser una instancia de `Socket` creada por `socket_create`.

## Parámetros

`socket`  
Una instancia de `Socket` creada con `socket_create`.

`address`  
El argumento `address` es una dirección IPv4 válida (por ejemplo, `127.0.0.1`) si `socket` es `AF_INET`, o una dirección IPv6 válida (por ejemplo, `::1`) si el soporte IPv6 está activo y el argumento `socket` es `AF_INET6`, o una ruta hacia un socket de dominio Unix, si la familia de sockets es `AF_UNIX`.

`port`  
El argumento `port` solo se utiliza y es obligatorio al conectarse a un socket `AF_INET` o `AF_INET6`, e indica el puerto del host remoto al que debe realizarse la conexión.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. El código de error generado puede obtenerse llamando a la función `socket_last_error`. Este código de error puede pasarse a la función `socket_strerror` para obtener un mensaje de error legible por humanos.

> [!NOTE]
> Si el socket es no bloqueante, entonces esta función devuelve `false` con el siguiente error: `Operation now in progress`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `socket` ahora es una instancia de `Socket` ; anteriormente, era un `resource`. |
| 8.0.0 | `port` ahora es nullable. |

## Véase también

`socket_bind`, `socket_listen`, `socket_create`, `socket_last_error`, `socket_strerror`
