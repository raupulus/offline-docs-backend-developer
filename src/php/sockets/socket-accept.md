---
title: socket_accept
description: Acepta una conexión en un socket
source_url: https://www.php.net/manual/es/function.socket-accept.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-accept.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: 14dc7c473
order: 75520
---

socket_accept

Acepta una conexión en un socket

## Descripción

```php
socket_accept(Socket $socket): Socket
```php

Una vez que el socket `socket` ha sido creado con la función `socket_create`, vinculado a un nombre con la función `socket_bind`, y puesto en espera de conexión con la función `socket_listen`, `socket_accept` acepta las conexiones en este socket. Una vez que se establece una conexión, se devuelve una nueva instancia de `Socket`. Esta puede ser utilizada para las comunicaciones. Si hay varias conexiones en espera, se utilizará la primera. Si no hay conexiones en espera, `socket_accept` se bloqueará hasta que se presente una conexión. Si `socket` ha sido configurado como no bloqueante, gracias a `socket_set_blocking` o `socket_set_nonblock`, se devolverá `false`.

La instancia de `Socket` devuelta por `socket_accept` no debe ser utilizada para aceptar nuevas conexiones. El socket original `socket`, que está en espera, permanece abierto y puede ser reutilizado.

## Parámetros

`socket`  
Una instancia de `Socket` creada por `socket_create`.

## Valores devueltos

Devuelve una nueva instancia de `Socket` en caso de éxito o `false` en caso de error. El código de error generado puede ser obtenido llamando a la función `socket_last_error`. Este código de error puede ser pasado a la función `socket_strerror` para obtener un mensaje de error legible por humanos.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `Socket` ; anteriormente, se devolvía un `resource`. |

## Véase también

`socket_connect`, `socket_listen`, `socket_create`, `socket_bind`, `socket_strerror`
