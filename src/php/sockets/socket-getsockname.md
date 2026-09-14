---
title: socket_getsockname
description: Interroga el socket local
source_url: https://www.php.net/manual/es/function.socket-getsockname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-getsockname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: 890cc22d3
order: 75700
---

socket_getsockname

Interroga el socket local

## Descripción

```php
socket_getsockname(Socket $socket, string $address, [int $port]): bool
```php

> [!NOTE]
> `socket_getsockname` no debe ser utilizada con los sockets `AF_UNIX` creados con `socket_connect`. Solo los sockets tras una llamada a `socket_bind` devolverán valores lógicos.

## Parámetros

`socket`  
Una instancia de `Socket` creada por `socket_create` o `socket_accept`.

`address`  
Si el socket `socket` es de tipo `AF_INET`, o `AF_INET6`, `socket_getsockname` devolverá *la dirección IP* local, en notación numérica (e.g. `127.0.0.1` o `fe80::1`) en el parámetro `address`, y si el parámetro opcional `port` está presente, también devolverá el puerto de la comunicación establecida.

Si el socket `socket` es de tipo `AF_UNIX`, `socket_getsockname` devolverá la ruta en el sistema de archivos (e.g. `/var/run/daemon.sock`) en el parámetro `address`.

`port`  
Si se proporciona, este deberá ser el puerto asociado a la dirección.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. `socket_getsockname` también puede devolver `false` si el tipo del socket no es ni `AF_INET`, ni `AF_INET6`, ni `AF_UNIX`, en cuyo caso el último código de error socket no es *modificado*.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Ahora recupera el índice de la interfaz y su representación en cadena cuando se usa sobre un socket de la familia `AF_PACKET`. |
| 8.0.0 | `socket` ahora es una instancia de `Socket` ; anteriormente, era un `resource`. |

## Véase también

`socket_getpeername`, `socket_last_error`, `socket_strerror`
