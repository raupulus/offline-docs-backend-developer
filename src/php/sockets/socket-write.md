---
title: socket_write
description: Escribe en un socket
source_url: https://www.php.net/manual/es/function.socket-write.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-write.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: 2ca105847
order: 75880
---

socket_write

Escribe en un socket

## Descripción

```php
socket_write(Socket $socket, string $data, [int $length]): int
```php

`socket_write` escribe en el socket `socket` los datos del buffer `data`.

## Parámetros

`socket`  

`data`  
El buffer a escribir.

`length`  
El parámetro opcional `length` puede especificar explícitamente el tamaño de los datos que deben ser escritos. Si esta longitud es mayor que el tamaño de `data`, será reducida automáticamente al tamaño de `data` mismo.

## Valores devueltos

`socket_write` devuelve el número de bytes que han podido ser escritos en el socket o `false` si ocurre un error. El código de error generado puede ser obtenido llamando a la función `socket_last_error`. Este código de error puede ser pasado a la función `socket_strerror` para obtener un mensaje de error, legible para humanos.

> [!NOTE]
> Es perfectamente válido que `socket_write` devuelva cero, lo que significa que ningún byte ha sido escrito. Asegúrese de utilizar el operador `===` para comparar el retorno de la función con `false`, y detectar un caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `socket` ahora es una instancia de `Socket` ; anteriormente, era un `resource`. |
| 8.0.0 | `length` ahora es nullable. |

## Notas

> [!NOTE]
> `socket_write` no escribe necesariamente todos los bytes de `data` proporcionados. Es válido que, siguiendo ciertas configuraciones de buffer de red, solo una cierta cantidad de datos, incluso un byte, sea escrito, incluso si `data` es más grande. Un ciclo debe ser utilizado para asegurarse de que el resto de `data` sea transmitido.

## Véase también

`socket_accept`, `socket_bind`, `socket_connect`, `socket_listen`, `socket_read`, `socket_strerror`
