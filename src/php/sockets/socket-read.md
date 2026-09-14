---
title: socket_read
description: Lee datos de un socket
source_url: https://www.php.net/manual/es/function.socket-read.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-read.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: f80105b4f
order: 75740
---

socket_read

Lee datos de un socket

## Descripción

```php
socket_read(Socket $socket, int $length, [int $mode]): string
```php

`socket_read` lee datos desde la instancia de `Socket` `socket`, creada por `socket_create` o `socket_accept`.

## Parámetros

`socket`  
Una instancia de `Socket` creada por `socket_create` o `socket_accept`.

`length`  
Lee un máximo de `length` bytes. De lo contrario, puede utilizarse `\r`, `\n` o `\0` para terminar la lectura (según el valor elegido para `mode`, ver a continuación).

`mode`  
El parámetro opcional `mode` puede tomar uno de los siguientes valores constantes:

- `PHP_BINARY_READ` (Por omisión) - utiliza la función del sistema `recv()`. Capaz de leer datos binarios.

- `PHP_NORMAL_READ` - la lectura se detiene en `\n` y `\r`

## Valores devueltos

`socket_read` devuelve los datos en forma de string en caso de éxito, y `false` en caso contrario (incluyendo si el host remoto ha cerrado la conexión). El código de error generado puede obtenerse llamando a la función `socket_last_error`. Este código de error puede pasarse a la función `socket_strerror` para obtener un mensaje de error legible por humanos.

> [!NOTE]
> `socket_read` devuelve un string de longitud cero (""), cuando ya no hay más datos para leer.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `socket` ahora es una instancia de `Socket` ; anteriormente, era un `resource`. |

## Véase también

`socket_accept`, `socket_bind`, `socket_connect`, `socket_listen`, `socket_last_error`, `socket_strerror`, `socket_write`
