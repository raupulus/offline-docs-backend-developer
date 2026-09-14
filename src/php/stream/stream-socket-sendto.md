---
title: stream_socket_sendto
description: Envía un mensaje al socket, conectado o no
source_url: https://www.php.net/manual/es/function.stream-socket-sendto.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-socket-sendto.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: e50e79746
order: 88180
---

stream_socket_sendto

Envía un mensaje al socket, conectado o no

## Descripción

```php
stream_socket_sendto(resource $socket, string $data, [int $flags], [string $address]): int
```php

`stream_socket_sendto` envía los datos `data` al socket `socket`.

## Parámetros

`socket`  
El socket al cual enviar los datos `data`.

`data`  
Los datos a enviar.

`flags`  
El valor de `flags` puede ser la combinación de las constantes siguientes:

|              |                                              |
|--------------|----------------------------------------------|
| `STREAM_OOB` | Trata los datos en modo OOB (`out-of-band`). |

Valores posibles para `flags`

`address`  
La dirección del socket se especifica cuando el socket es creado, y será utilizada si otra dirección no es especificada en el parámetro `address`.

Cuando es proporcionada, debe estar en formato IP numérico (versión 4 o 6).

## Valores devueltos

Retorna el código de resultado, en forma de integer, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `stream_socket_sendto`

```
<?php
/* Abre un socket en el puerto 1234 de localhost */
$socket = stream_socket_client('tcp://127.0.0.1:1234');

/* Envía datos directamente */
fwrite($socket, "Normal data transmit.");

/* Envía otros datos, en modo out of band. */
stream_socket_sendto($socket, "Mode out of Band.", STREAM_OOB);

/* Fin */
fclose($socket);
?>

    
```php

## Véase también

stream_socket_recvfrom

stream_socket_client

stream_socket_server
