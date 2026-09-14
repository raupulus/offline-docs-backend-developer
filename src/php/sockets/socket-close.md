---
title: socket_close
description: Cierra una instancia de Socket
source_url: https://www.php.net/manual/es/function.socket-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: 14dc7c473
order: 75600
---

socket_close

Cierra una instancia de

Socket

## Descripción

```php
socket_close(Socket $socket): void
```php

`socket_close` cierra la instancia `Socket` proporcionada por `socket`.

## Parámetros

`socket`  
Una instancia de `Socket` creada por `socket_create` o `socket_accept`.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `socket` ahora es una instancia de `Socket` ; anteriormente, era un `resource`. |

## Véase también

`socket_bind`, `socket_listen`, `socket_create`, `socket_strerror`
