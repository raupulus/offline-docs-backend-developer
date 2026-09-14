---
title: EventHttp::setCallback
description: Define una retrollamada para una URI específica
source_url: https://www.php.net/manual/es/eventhttp.setcallback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventhttp/setcallback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: a47dff201
order: 19910
---

EventHttp::setCallback

Define una retrollamada para una URI específica

## Descripción

```php
public EventHttp::setCallback(string $path, string $cb, [string $arg]): void
```php

Define una retrollamada para una URI específica.

## Parámetros

`path`  
La URI para la cual la retrollamada debe ser invocada.

`cb`  
La retrollamada `callable` que será invocada durante una petición en la URI `path`. Debe corresponder al siguiente prototipo:

```php
callback([EventHttpRequest $req], [mixed $arg]): void
```

`req`  
Un objeto `EventHttpRequest`.

`arg`  
Datos personalizados.

`arg`  
Datos personalizados.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `EventHttp::setCallback`

```php
<?php
/*
 * Servidor HTTP simple.
 *
 * Para probarlo:
 * 1) Ejecútelo en el puerto de su elección, i.e. :
 * $ php examples/http.php 8010
 * 2) En otro terminal, conéctese a una dirección de este puerto
 * y realice una petición GET o POST (las otras están desactivadas aquí), i.e.:
 * $ nc -t 127.0.0.1 8010
 * POST /about HTTP/1.0
 * Content-Type: text/plain
 * Content-Length: 4
 * Connection: close
 * (presione Enter)
 *
 * Debería mostrar:
 * a=12
 * HTTP/1.0 200 OK
 * Content-Type: text/html; charset=ISO-8859-1
 * Connection: close
 *
 * 3) Ver lo que muestra el servidor en el terminal anterior.
 */

function _http_dump($req, $data) {
    static $counter      = 0;
    static $max_requests = 2;

    if (++$counter >= $max_requests)  {
        echo "Counter reached max requests $max_requests. Exiting\n";
        exit();
    }

    echo __METHOD__, " called\n";
    echo "request:"; var_dump($req);
    echo "data:"; var_dump($data);

    echo "\n===== DUMP =====\n";
    echo "Command:", $req->getCommand(), PHP_EOL;
    echo "URI:", $req->getUri(), PHP_EOL;
    echo "Input headers:"; var_dump($req->getInputHeaders());
    echo "Output headers:"; var_dump($req->getOutputHeaders());

    echo "\n >> Sending reply ...";
    $req->sendReply(200, "OK");
    echo "OK\n";

    echo "\n >> Reading input buffer ...\n";
    $buf = $req->getInputBuffer();
    while ($s = $buf->readLine(EventBuffer::EOL_ANY)) {
        echo $s, PHP_EOL;
    }
    echo "No more data in the buffer\n";
}

function _http_about($req) {
    echo __METHOD__, PHP_EOL;
    echo "URI: ", $req->getUri(), PHP_EOL;
    echo "\n >> Sending reply ...";
    $req->sendReply(200, "OK");
    echo "OK\n";
}

function _http_default($req, $data) {
    echo __METHOD__, PHP_EOL;
    echo "URI: ", $req->getUri(), PHP_EOL;
    echo "\n >> Sending reply ...";
    $req->sendReply(200, "OK");
    echo "OK\n";
}

$port = 8010;
if ($argc > 1) {
    $port = (int) $argv[1];
}
if ($port <= 0 || $port > 65535) {
    exit("Invalid port");
}

$base = new EventBase();
$http = new EventHttp($base);
$http->setAllowedMethods(EventHttpRequest::CMD_GET | EventHttpRequest::CMD_POST);

$http->setCallback("/dump", "_http_dump", array(4, 8));
$http->setCallback("/about", "_http_about");
$http->setDefaultCallback("_http_default", "custom data value");

$http->bind("0.0.0.0", 8010);
$base->loop();
?>

   
```

Resultado del ejemplo anterior es similar a:

    a=12
    HTTP/1.0 200 OK
    Content-Type: text/html; charset=ISO-8859-1
    Connection: close

## Véase también

EventHttp::setDefaultCallback
