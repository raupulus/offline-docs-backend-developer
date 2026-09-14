---
title: socket_getpeername
description: Interroga el otro extremo de la comunicación
source_url: https://www.php.net/manual/es/function.socket-getpeername.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-getpeername.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: 5eaa3458d
order: 75690
---

socket_getpeername

Interroga el otro extremo de la comunicación

## Descripción

```php
socket_getpeername(Socket $socket, string $address, [int $port]): bool
```php

Interroga el otro extremo de la comunicación.

## Parámetros

`socket`  
Una instancia de `Socket` creada por `socket_create` o `socket_accept`.

`address`  
Si el socket `socket` es de tipo `AF_INET` o `AF_INET6`, `socket_getpeername` devolverá *la dirección IP* del host, en notación numérica (por ejemplo, `127.0.0.1` o `fe80::1`) en el parámetro `address`, y si el parámetro opcional `port` está presente, también devolverá el puerto de la comunicación establecida.

Si el socket `socket` es de tipo `AF_UNIX`, `socket_getpeername` devolverá la ruta en el sistema de archivos (por ejemplo, `/var/run/daemon.sock`) en el parámetro `address`.

`port`  
Si se proporciona, este debe ser el puerto asociado a la dirección del parámetro `address`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. `socket_getpeername` también puede devolver `false` si el tipo del socket no es ni `AF_INET`, `AF_INET6` ni `AF_UNIX`, en cuyo caso el último código de error del socket *no* se modifica.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `socket` ahora es una instancia de `Socket` ; anteriormente, era un `resource`. |

## Notas

> [!NOTE]
> `socket_getsockname` no debe usarse con los sockets `AF_UNIX` creados con `socket_accept`. Solo los sockets creados con `socket_connect` o un socket servidor primario tras una llamada a `socket_bind` devolverán valores lógicos.

> [!NOTE]
> Para que la función `socket_getpeername` devuelva un valor coherente, el socket sobre el que se llama a la función debe ser evidentemente uno para el que el concepto de "peer" tiene sentido.

## Véase también

`socket_getsockname`, `socket_last_error`, `socket_strerror`
