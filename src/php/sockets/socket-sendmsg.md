---
title: socket_sendmsg
description: Envía un mensaje
source_url: https://www.php.net/manual/es/function.socket-sendmsg.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-sendmsg.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: false
translation_revision: 14dc7c473
order: 75800
---

socket_sendmsg

Envía un mensaje

## Descripción

```php
socket_sendmsg(Socket $socket, array $message, [int $flags]): int
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`socket`  

`message`  

`flags`  

## Valores devueltos

Devuelve el número de bytes enviados, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `socket` ahora es una instancia de `Socket` ; anteriormente, era un `resource`. |

## Véase también

`socket_recvmsg`, `socket_cmsg_space`
