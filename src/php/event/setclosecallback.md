---
title: EventHttpConnection::setCloseCallback
description: Define una función de retrollamada al cerrar la conexión
source_url: https://www.php.net/manual/es/eventhttpconnection.setclosecallback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventhttpconnection/setclosecallback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 22583751f
order: 20010
---

EventHttpConnection::setCloseCallback

Define una función de retrollamada al cerrar la conexión

## Descripción

```php
public EventHttpConnection::setCloseCallback(callable $callback, [mixed $data]): void
```php

Define una función de retrollamada al cerrar la conexión.

## Parámetros

`callback`  
Función de retrollamada a llamar al cerrar la conexión. Debe corresponder al siguiente prototipo:

```php
callback([EventHttpConnection $conn], [mixed $arg]): void
```

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con EventHttpConnection::setCloseCallback

```php
<?php
/*
 * Configuración de la retrollamada de cierre de conexión
 *
 * El script maneja las conexiones cerradas utilizando la API HTTP.
 *
 * Uso:
 * 1) Iniciar el servidor:
 * $ php examples/http_closecb.php 4242
 *
 * 2) Iniciar un cliente en otra terminal. La sesión de tipo telnet
 * debe verse como sigue:
 *
 * $ nc -t 127.0.0.1 4242
 * GET / HTTP/1.0
 * Connection: close
 *
 * El servidor debe mostrar algo similar a lo siguiente:
 *
 * HTTP/1.0 200 OK
 * Content-Type: multipart/x-mixed-replace;boundary=boundarydonotcross
 * Connection: close
 *
 * <html>
 *
 * 3) Terminar la conexión del cliente abruptamente,
 * es decir, matar el proceso o simplemente presionar Ctrl-C.
 *
 * 4) Verificar si el servidor llamó a _close_callback.
 * El script debe mostrar la cadena "_close_callback" en la salida estándar.
 *
 * 5) Verificar si el proceso del servidor no tiene conexiones huérfanas,
 * por ejemplo, con la utilidad `lsof`.
 */

function _close_callback($conn)
{
    echo __FUNCTION__, PHP_EOL;
}

function _http_default($req, $dummy)
{
    $conn = $req->getConnection();
    $conn->setCloseCallback('_close_callback', NULL);

    /*
    Al habilitar Event::READ se protege al servidor contra conexiones no cerradas.
    Esta es una peculiaridad de Libevent. La biblioteca deshabilita los eventos Event::READ
    en esta conexión, y el servidor no es notificado sobre las conexiones terminadas.

    Por lo tanto, cada vez que el cliente termina la conexión abruptamente, obtenemos una conexión huérfana. Por ejemplo, lo siguiente es parte del comando `lsof -p $PID | grep TCP`
    después de que el cliente ha terminado la conexión:

    57-php     15057 ruslan  6u  unix 0xffff8802fb59c780   0t0  125187 socket
    58:php     15057 ruslan  7u  IPv4             125189   0t0     TCP *:4242 (LISTEN)
    59:php     15057 ruslan  8u  IPv4             124342   0t0     TCP localhost:4242->localhost:37375 (CLOSE_WAIT)

    donde $PID es el ID del proceso.

    El siguiente bloque de código corrige este tipo de conexiones huérfanas.
     */
    $bev = $req->getBufferEvent();
    $bev->enable(Event::READ);

    // Debemos liberarlo explícitamente. Ver EventHttpRequest::getConnection

    $bev->free(); // Debemos liberarlo explícitamente

    $req->addHeader(
        'Content-Type',
        'multipart/x-mixed-replace;boundary=boundarydonotcross',
        EventHttpRequest::OUTPUT_HEADER
    );

    $buf = new EventBuffer();
    $buf->add('<html>');

    $req->sendReply(200, "OK");
    $req->sendReplyChunk($buf);
}

$port = 4242;
if ($argc > 1) {
    $port = (int) $argv[1];
}
if ($port <= 0 || $port > 65535) {
    exit("Puerto no válido");
}

$base = new EventBase();
$http = new EventHttp($base);

$http->setDefaultCallback("_http_default", NULL);
$http->bind("0.0.0.0", $port);
$base->loop();

?>

   
```
