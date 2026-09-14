---
title: socket_bind
description: Asocia un nombre a un socket
source_url: https://www.php.net/manual/es/function.socket-bind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-bind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: 890cc22d3
order: 75580
---

socket_bind

Asocia un nombre a un socket

## Descripción

```php
socket_bind(Socket $socket, string $address, [int $port]): bool
```php

Asocia el nombre proporcionado por `address` a la interfaz de conexión descrita por `socket`. Esto debe realizarse antes de que se establezca una conexión utilizando `socket_connect` o `socket_listen`.

## Parámetros

`socket`  
Una instancia de `Socket` creada por `socket_create`.

`address`  
Si el socket pertenece a la familia `AF_INET`, el parámetro `address` es una IP numérica (i.e. `127.0.0.1`).

Si el socket pertenece a la familia `AF_UNIX`, el parámetro `address` representa la ruta de un socket de dominio Unix (i.e. `/tmp/my.sock`).

`port` (opcional)  
El parámetro `port` solo se utiliza al asociar un socket `AF_INET` y designa el puerto en el que escuchar para una conexión.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

El código de error puede ser recuperado con la función `socket_last_error`. Este código puede ser pasado a la función `socket_strerror` para recuperar el mensaje textual del error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Ahora lanza un ValueError cuando `port` es menor que 0 o mayor que 65535. |
| 8.0.0 | `socket` ahora es una instancia de `Socket` ; anteriormente, era un `resource`. |

## Ejemplos

Uso de `socket_bind` para definir la dirección de origen

```
<?php
// Creación de un nuevo socket
$sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);

// Una lista de direcciones IP, por ejemplo, pertenecen a la computadora
$sourceips['kevin']    = '127.0.0.1';
$sourceips['madcoder'] = '127.0.0.2';

// Asocia la dirección de origen
socket_bind($sock, $sourceips['madcoder']);

// Conexión a la dirección de destino
socket_connect($sock, '127.0.0.1', 80);

// Escritura
$request = 'GET / HTTP/1.1' . "\r\n" .
'Host: example.com' . "\r\n\r\n";
socket_write($sock, $request);

// Cierre
socket_close($sock);

?>
    
```php

## Notas

> [!NOTE]
> Esta función debe ser utilizada en el socket antes de la función `socket_connect`.

## Véase también

`socket_connect`, `socket_listen`, `socket_create`, `socket_last_error`, `socket_strerror`
