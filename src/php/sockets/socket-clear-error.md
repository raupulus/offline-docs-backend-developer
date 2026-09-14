---
title: socket_clear_error
description: Elimina todos los errores generados previamente por un socket
source_url: https://www.php.net/manual/es/function.socket-clear-error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-clear-error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: 14dc7c473
order: 75590
---

socket_clear_error

Elimina todos los errores generados previamente por un socket

## Descripción

```php
socket_clear_error([Socket $socket]): void
```php

Elimina todos los códigos de error que han sido registrados para el socket `socket`, o bien para el socket general.

`socket_clear_error` permite restablecer a cero los códigos de error de un socket o del socket global. Esto puede ser útil para detectar la aparición de un error durante una parte de la aplicación.

## Parámetros

`socket`  
Una instancia de `Socket` creada por `socket_create`.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `socket` ahora es una instancia de `Socket` ; anteriormente, era un `resource`. |
| 8.0.0 | `socket` ahora es nullable. |

## Véase también

`socket_last_error`, `socket_strerror`
