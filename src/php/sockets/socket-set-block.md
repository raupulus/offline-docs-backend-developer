---
title: socket_set_block
description: Establece el socket en modo bloqueante
source_url: https://www.php.net/manual/es/function.socket-set-block.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-set-block.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: 14dc7c473
order: 75820
---

socket_set_block

Establece el socket en modo bloqueante

## Descripción

```php
socket_set_block(Socket $socket): bool
```php

`socket_set_block` elimina la opción `O_NONBLOCK` del socket especificado por `socket`.

Cuando se realiza una operación (por ejemplo, recepción, envío, conexión, aceptación, etc.) sobre un socket no bloqueante, el script no se pone en pausa hasta que recibe una señal. En su lugar, si la operación debe resultar en un bloqueo, la función llamada fallará.

## Parámetros

`socket`  
Una instancia de `Socket` creada por `socket_create` o `socket_accept`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `socket` ahora es una instancia de `Socket` ; anteriormente, era un `resource`. |

## Ejemplos

Ejemplo con `socket_set_block`

```
<?php
$socket = socket_create_listen(1223);
socket_set_block($socket);

socket_accept($socket);
?>

    
```php

Este ejemplo crea un socket que escucha todas las interfaces del puerto 1223 y establece el socket en modo `O_BLOCK`. `socket_accept` esperará hasta que haya una conexión para aceptar.

## Véase también

`socket_set_nonblock`, `socket_set_option`
