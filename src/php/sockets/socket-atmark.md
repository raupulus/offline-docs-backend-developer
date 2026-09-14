---
title: socket_atmark
description: Determina si el socket está en la marca fuera de banda
source_url: https://www.php.net/manual/es/function.socket-atmark.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-atmark.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: 2c357a0dd
order: 75570
---

socket_atmark

Determina si el socket está en la marca fuera de banda

## Descripción

```php
socket_atmark(Socket $socket): bool
```php

Determina si `socket` está en la marca fuera de banda.

## Parámetros

`socket`  
Una instancia de `Socket` creada con `socket_create`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Uso de `socket_atmark` para comprobar si el socket está listo para leer datos fuera de banda.

```
<?php
$socketServer = socket_create( AF_INET, SOCK_STREAM, SOL_TCP );
socket_set_option( $socketServer, SOL_SOCKET, SO_REUSEADDR, 1 );
socket_bind( $socketServer, '127.0.0.1' );
socket_listen( $socketServer );

$socketClient = socket_create( AF_INET, SOCK_STREAM, SOL_TCP );
socket_getsockname( $socketServer, $stAddr, $uPort );
socket_connect( $socketClient, $stAddr, $uPort );

$socket = socket_accept( $socketServer );
socket_shutdown( $socket, 1 );

$st = 'Estos son datos normales.';
socket_send( $socketClient, $st, strlen( $st ), 0 );
$st = '!'; # TCP solo permite un byte de datos urgentes.
socket_send( $socketClient, $st, strlen( $st ), MSG_OOB );
$st = 'No tan urgente.';
socket_send( $socketClient, $st, strlen( $st ), 0 );
socket_shutdown( $socketClient );

do {
    if ( socket_atmark( $socket ) ) {
        $rc = socket_recv( $socket, $st, 65536, MSG_OOB );
        echo "Datos urgentes recibidos: ({$rc}) {$st}\n";
    } else {
        $rc = socket_recv( $socket, $st, 1024, 0 );
        echo "Datos normales recibidos: ({$rc}) {$st}\n";
    }
} while ( $rc > 0 );
socket_close( $socketServer );
socket_close( $socketClient );
socket_close( $socket );
?>

    
```php

El ejemplo anterior mostrará:

    Datos normales recibidos: (25) Estos son datos normales.
    Datos urgentes recibidos: (1) !
    Datos normales recibidos: (15) No tan urgente.
    Datos normales recibidos: (0)

## Véase también

`socket_connect`, `socket_create`
