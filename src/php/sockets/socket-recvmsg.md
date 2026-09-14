---
title: socket_recvmsg
description: Lee un mensaje
source_url: https://www.php.net/manual/es/function.socket-recvmsg.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-recvmsg.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: false
translation_revision: 14dc7c473
order: 75770
---

socket_recvmsg

Lee un mensaje

## Descripción

```php
socket_recvmsg(Socket $socket, array $message, [int $flags]): int
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`socket`  

`message`  

`flags`  

## Valores devueltos

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `socket` ahora es una instancia de `Socket` ; anteriormente, era un `resource`. |

## Véase también

`socket_sendmsg`, `socket_cmsg_space`
