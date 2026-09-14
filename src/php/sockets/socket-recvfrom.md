---
title: socket_recvfrom
description: Recibe datos de un socket, conectado o no
source_url: https://www.php.net/manual/es/function.socket-recvfrom.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-recvfrom.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: de9c65c91
order: 75760
---

socket_recvfrom

Recibe datos de un socket, conectado o no

## Descripción

```php
socket_recvfrom(Socket $socket, string $data, int $length, int $flags, string $address, [int $port]): int
```php

La función `socket_recvfrom` recibe `length` bytes de datos del buffer `data` desde `address` en el puerto `port` (si el socket no es del tipo `AF_UNIX`), utilizando `socket`. `socket_recvfrom` puede ser utilizado para recuperar los datos desde sockets conectadas o no. Asimismo, uno o varios flags pueden ser especificados para modificar este comportamiento.

Los parámetros `address` y `port` deben ser pasados por referencia. Si el socket no está conectado, `address` contendrá la dirección internet del host remoto o la ruta del socket Unix. Si el socket está conectado, `address` valdrá `null`. Asimismo, el parámetro `port` contendrá el puerto del host remoto en el caso de un socket `AF_INET` o `AF_INET6`.

> [!NOTE]
> Esta función es segura para sistemas binarios.

## Parámetros

`socket`  
El parámetro `socket` debe ser una instancia de `Socket` creada por `socket_create`.

`data`  
Los datos recuperados serán colocados en la variable especificada por este parámetro.

`length`  
Hasta `length` bytes deben ser recuperados del host remoto.

`flags`  
El valor de este parámetro puede ser una combinación de los flags siguientes, unidos por un OR binario (`|`).

| Flag | Descripción |
|----|----|
| `MSG_OOB` | Procesamiento fuera de la banda de datos. |
| `MSG_PEEK` | Recibe los datos desde el inicio de la cola de recepción sin eliminarlos de esta cola. |
| `MSG_WAITALL` | Bloquea hasta que al menos `length` bytes hayan sido recibidos. Sin embargo, si se recibe una señal o el host remoto se desconecta, la función podrá retornar menos datos. |
| `MSG_DONTWAIT` | Cuando este flag está definido, la función retorna datos incluso si debería permanecer bloqueada. |

Valores posibles para `flags`

`address`  
Si el socket es del tipo `AF_UNIX`, `address` será la ruta hacia este fichero. De lo contrario, para los sockets no-conectados, `address` es la dirección IP del host remoto, o `null` si el socket está conectado.

`port`  
Este argumento solo se aplica a los sockets `AF_INET` y `AF_INET6`, y especifica el puerto remoto desde el cual los datos son recibidos. Si el socket está conectado, `port` valdrá `null`.

## Valores devueltos

`socket_recvfrom` retorna el número de bytes recibidos, o `false` si ocurre un error. El código de error actual puede ser obtenido llamando a la función `socket_last_error`. Este código de error puede ser pasado a la función `socket_strerror` para obtener una explicación textual del error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `socket` ahora es una instancia de `Socket` ; anteriormente, era un `resource`. |

## Ejemplos

Ejemplo con `socket_recvfrom`

```
<?php

$socket = socket_create(AF_INET, SOCK_DGRAM, SOL_UDP);
socket_bind($socket, '127.0.0.1', 1223);

$from = '';
$port = 0;
socket_recvfrom($socket, $buf, 12, 0, $from, $port);

echo "Recepción de $buf desde la dirección remota $from y del puerto remoto $port" . PHP_EOL;
?>

    
```php

Este ejemplo inicializa un socket UDP en el puerto 1223 de la dirección 127.0.0.1 y muestra al menos 12 caracteres recibidos desde el host remoto.

## Véase también

`socket_recv`, `socket_send`, `socket_sendto`, `socket_create`
