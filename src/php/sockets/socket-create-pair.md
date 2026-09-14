---
title: socket_create_pair
description: Crea un par de sockets idénticos y los almacena en un array
source_url: https://www.php.net/manual/es/function.socket-create-pair.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-create-pair.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: 14dc7c473
order: 75640
---

socket_create_pair

Crea un par de sockets idénticos y los almacena en un array

## Descripción

```php
socket_create_pair(int $domain, int $type, int $protocol, array $pair): bool
```php

`socket_create_pair` crea un par de sockets idénticos y los almacena en `pair`. Esta función se utiliza comúnmente en IPC (`InterProcess Communication`).

## Parámetros

`domain`  
El argumento `domain` especifica la familia del protocolo a utilizar por el socket. Ver la documentación sobre la función `socket_create` para una lista completa.

`type`  
El argumento `type` especifica el tipo de comunicación a utilizar por el socket. Ver la documentación sobre la función `socket_create` para una lista completa.

`protocol`  
El argumento `protocol` define un protocolo específico en el dominio especificado `domain` para ser utilizado durante una comunicación en un socket devuelto. El valor apropiado puede ser encontrado por su nombre utilizando la función `getprotobyname`. Si el protocolo deseado es TCP o UDP, las constantes correspondientes `SOL_TCP` y `SOL_UDP` pueden ser utilizadas.

Ver la documentación sobre la función `socket_create` para una lista completa de los protocolos soportados.

`pair`  
Una referencia a un array en el cual las dos instancias de `Socket` serán insertadas.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `pair` es una referencia a un array de instancias de `Socket`; anteriormente, era una referencia a un array de `resource`s. |

## Ejemplos

Ejemplo con `socket_create_pair`

```
<?php
$sockets = array();

/* En Windows, debemos utilizar AF_INET */
$domain = (strtoupper(substr(PHP_OS, 0, 3)) == 'WIN' ? AF_INET : AF_UNIX);

/* Creación del par de sockets */
if (socket_create_pair($domain, SOCK_STREAM, 0, $sockets) === false) {
    echo "socket_create_pair ha fallado. Razón: ".socket_strerror(socket_last_error());
}
/* Envío y recepción de datos */
if (socket_write($sockets[0], "ABCdef123\n", strlen("ABCdef123\n")) === false) {
    echo "socket_write() ha fallado. Razón: ".socket_strerror(socket_last_error($sockets[0]));
}
if (($data = socket_read($sockets[1], strlen("ABCdef123\n"), PHP_BINARY_READ)) === false) {
    echo "socket_read() ha fallado. Razón: ".socket_strerror(socket_last_error($sockets[1]));
}
var_dump($data);

/* Cierre de los sockets */
socket_close($sockets[0]);
socket_close($sockets[1]);
?>

    
```php

Ejemplo IPC con `socket_create_pair`

```
<?php
$ary = array();
$strone = 'Mensaje desde el padre.';
$strtwo = 'Mensaje desde el hijo.';
if (socket_create_pair(AF_UNIX, SOCK_STREAM, 0, $ary) === false) {
    echo "socket_create_pair() ha fallado. Razón: ".socket_strerror(socket_last_error());
}
$pid = pcntl_fork();
if ($pid == -1) {
    echo 'No es posible duplicar el proceso.';
} elseif ($pid) {
    /* padre */
    socket_close($ary[0]);
    if (socket_write($ary[1], $strone, strlen($strone)) === false) {
        echo "socket_write() ha fallado. Razón: ".socket_strerror(socket_last_error($ary[1]));
    }
    if (socket_read($ary[1], strlen($strtwo), PHP_BINARY_READ) == $strtwo) {
        echo "Recepción de $strtwo\n";
    }
    socket_close($ary[1]);
} else {
    /* hijo */
    socket_close($ary[1]);
    if (socket_write($ary[0], $strtwo, strlen($strtwo)) === false) {
        echo "socket_write() ha fallado. Razón: ".socket_strerror(socket_last_error($ary[0]));
    }
    if (socket_read($ary[0], strlen($strone), PHP_BINARY_READ) == $strone) {
        echo "Recepción de $strone\n";
    }
    socket_close($ary[0]);
}
?>

    
```php

## Véase también

`socket_create`, `socket_create_listen`, `socket_bind`, `socket_listen`, `socket_last_error`, `socket_strerror`
