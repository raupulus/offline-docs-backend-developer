---
title: socket_set_option
description: Modifica las opciones de socket
source_url: https://www.php.net/manual/es/function.socket-set-option.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-set-option.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: 890cc22d3
order: 75840
---

socket_set_option

Modifica las opciones de socket

## Descripción

```php
socket_set_option(Socket $socket, int $level, int $option, array $value): bool
```php

`socket_set_option` configura la opción especificada por `option`, al nivel de protocolo `level` al valor apuntado por `value` para el socket especificado por `socket`.

## Parámetros

`socket`  
Una instancia de `Socket` creada por `socket_create` o `socket_accept`.

`level`  
El parámetro `level` especifica la capa del protocolo de la opción. Por ejemplo, para modificar una opción de la capa socket, se utiliza un nivel igual a `SOL_SOCKET`. Otros niveles, como TCP, pueden ser utilizados especificando un número de protocolo para este nivel. Los números de protocolos pueden ser utilizados utilizando la función `getprotobyname`.

`option`  
Las opciones disponibles son las mismas que para la función `socket_get_option`.

`value`  
El valor de la opción.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Ahora lanza una excepción cuando se utiliza `MCAST_LEAVE_GROUP` o `MCAST_LEAVE_SOURCE_GROUP` y el valor no es un objeto o un array válido, y lanza un ValueError cuando se utiliza una opción multicast sobre un socket que no es de la familia `AF_INET` o `AF_INET6`. |
| 8.0.0 | `socket` ahora es una instancia de `Socket` ; anteriormente, era un `resource`. |

## Ejemplos

Ejemplo con `socket_set_option`

```
<?php
$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);

if (!is_resource($socket)) {
    echo 'No es posible crear el socket: '. socket_strerror(socket_last_error()) . PHP_EOL;
}

if (!socket_set_option($socket, SOL_SOCKET, SO_REUSEADDR, 1)) {
    echo 'No es posible definir la opción del socket: '. socket_strerror(socket_last_error()) . PHP_EOL;
}

if (!socket_bind($socket, '127.0.0.1', 1223)) {
    echo 'No es posible vincular el socket: '. socket_strerror(socket_last_error()) . PHP_EOL;
}

$rval = socket_get_option($socket, SOL_SOCKET, SO_REUSEADDR);

if ($rval === false) {
    echo 'No es posible recuperar la opción del socket: '. socket_strerror(socket_last_error()) . PHP_EOL;
} else if ($rval !== 0) {
    echo 'SO_REUSEADDR está definido en el socket!' . PHP_EOL;
}
?>

    
```php

## Véase también

`socket_create`, `socket_bind`, `socket_strerror`, `socket_last_error`, `socket_get_option`
