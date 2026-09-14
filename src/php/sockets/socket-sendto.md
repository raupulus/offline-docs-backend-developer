---
title: socket_sendto
description: Envía un mensaje a un socket, ya esté conectado o no
source_url: https://www.php.net/manual/es/function.socket-sendto.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-sendto.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: 890cc22d3
order: 75810
---

socket_sendto

Envía un mensaje a un socket, ya esté conectado o no

## Descripción

```php
socket_sendto(Socket $socket, string $data, int $length, int $flags, string $address, [int $port]): int
```php

`socket_sendto` envía `length` octetos del buffer `data` a través del socket `socket`, hacia el puerto `port`, a la dirección `address`.

## Parámetros

`socket`  
Una instancia de `Socket` creada por `socket_create`.

`data`  
Los datos a enviar serán tomados del buffer `data`.

`length`  
`length` octetos de `data` deben ser enviados.

`flags`  
Puede ser una combinación de los siguientes flags, unidos por un OR a nivel de bits (`|`).

|  |  |
|----|----|
| `MSG_OOB` | Trata los datos OOB (out-of-band). |
| `MSG_EOR` | Indica un marcador de registro. Los datos enviados completan el registro. |
| `MSG_EOF` | Termina el envío a través del socket e incluye una notificación apropiada al final de los datos enviados. Los datos enviados completan la transacción. |
| `MSG_DONTROUTE` | Ignora el enrutamiento, usa una interfaz directa. |

Valores posibles para `flags`

`address`  
La dirección IP del host remoto.

`port`  
`port` es el número de puerto al cual los datos deben ser enviados.

## Valores devueltos

`socket_sendto` devuelve el número de octetos enviados al host remoto o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Ahora lanza un ValueError cuando `port` es menor que 0 o mayor que 65535. |
| 8.0.0 | `socket` ahora es una instancia de `Socket` ; anteriormente, era un `resource`. |
| 8.0.0 | `port` ahora es nullable. |

## Ejemplos

Ejemplo con `socket_sendto`

```
<?php
$sock = socket_create(AF_INET, SOCK_DGRAM, SOL_UDP);

$msg = "Ping !";
$len = strlen($msg);

socket_sendto($sock, $msg, $len, 0, '127.0.0.1', 1223);
socket_close($sock);
?>

    
```php

## Véase también

`socket_send`
