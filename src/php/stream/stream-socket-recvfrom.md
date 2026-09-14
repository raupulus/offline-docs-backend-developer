---
title: stream_socket_recvfrom
description: Lee datos desde un socket, conectado o no
source_url: https://www.php.net/manual/es/function.stream-socket-recvfrom.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-socket-recvfrom.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: e50e79746
order: 88170
---

stream_socket_recvfrom

Lee datos desde un socket, conectado o no

## Descripción

```php
stream_socket_recvfrom(resource $socket, int $length, [int $flags], [string $address]): string
```php

`stream_socket_recvfrom` acepta datos desde un socket remoto, hasta un total de `length` bytes.

## Parámetros

`socket`  
El socket remoto.

`length`  
El número de bytes a recibir de `socket`.

`flags`  
El valor de `flags` puede ser la combinación de las constantes siguientes:

|  |  |
|----|----|
| `STREAM_OOB` | Procesa los datos en modo OOB (`out-of-band`). |
| `STREAM_PEEK` | Lee datos desde el socket, pero no utiliza el buffer. Las próximas llamadas a `fread` o `stream_socket_recvfrom` leerán los mismos datos. |

Valores posibles para `flags`

`address`  
Si el argumento `address` es proporcionado, recibirá la dirección del socket remoto.

## Valores devueltos

Devuelve los datos leídos, como `string`, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `stream_socket_recvfrom`

```
<?php
/* Abre un socket en el puerto 1234 de localhost */
$server = stream_socket_server('tcp://127.0.0.1:1234');

/* Acepta una conexión */
$socket = stream_socket_accept($server);

/* Lee un paquete (1500 es el tamaño clásico MTU) de datos OOB */
echo "Recibido Out-Of-Band: '" . stream_socket_recvfrom($socket, 1500, STREAM_OOB) . "'\n";

/* Lee los datos normales in-band, pero no modifica nada */
echo "Datos: '" . stream_socket_recvfrom($socket, 1500, STREAM_PEEK) . "'\n";

/* Vuelve a leer el mismo paquete, pero vacía el buffer. */
echo "Datos: '" . stream_socket_recvfrom($socket, 1500) . "'\n";

/* Finalización */
fclose($socket);
fclose($server);
?>

    
```php

## Notas

> [!NOTE]
> Si el mensaje recibido es más grande que `length`, los datos adicionales pueden ser destruidos, dependiendo del tipo de socket utilizado (por ejemplo UDP).

> [!NOTE]
> La llamada a `stream_socket_recvfrom` en flujos basados en socket, después de la llamada a funciones de flujo basadas en buffer (como `fread` o `stream_get_line`) lee directamente los datos desde el socket y evita el uso del buffer con el flujo.

## Véase también

stream_socket_sendto

stream_socket_client

stream_socket_server
