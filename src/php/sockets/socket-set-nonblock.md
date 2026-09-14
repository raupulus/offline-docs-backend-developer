---
title: socket_set_nonblock
description: Selecciona el modo no bloqueante de un puntero de fichero
source_url: https://www.php.net/manual/es/function.socket-set-nonblock.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-set-nonblock.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: e50e79746
order: 75830
---

socket_set_nonblock

Selecciona el modo no bloqueante de un puntero de fichero

## Descripción

```php
socket_set_nonblock(Socket $socket): bool
```php

La función `socket_set_nonblock` configura la opción `O_NONBLOCK` para el socket especificado por el argumento `socket`.

Cuando una operación (por ejemplo, recepción, envío, conexión, aceptación, etc.) se realiza sobre un socket no bloqueante, el script no se pone en pausa mientras recibe una señal. En su lugar, si la operación debe resultar en un bloqueo, la función llamada fallará.

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

Ejemplo con `socket_set_nonblock`

```
<?php
$socket = socket_create_listen(1223);
socket_set_nonblock($socket);

socket_accept($socket);
?>

    
```php

Este ejemplo crea un socket escuchando todas las interfaces en el puerto 1223 y define el socket en modo `O_NONBLOCK`. `socket_accept` fallará inmediatamente si hay una conexión pendiente exactamente en ese momento.

## Véase también

`socket_set_block`, `socket_set_option`, `stream_set_blocking`
