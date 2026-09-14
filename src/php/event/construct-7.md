---
title: EventHttp::__construct
description: Construye un objeto EventHttp (el servidor HTTP)
source_url: https://www.php.net/manual/es/eventhttp.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventhttp/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: a47dff201
order: 19880
---

EventHttp::\_\_construct

Construye un objeto EventHttp (el servidor HTTP)

## Descripción

```php
public EventHttp::__construct(EventBase $base, [EventSslContext $ctx])
```php

Construye el objeto del servidor HTTP.

## Parámetros

`base`  
Evento base asociado.

`ctx`  
El objeto de la clase `EventSslContext`. Transforma un servidor HTTP en un servidor HTTPS. Esto significa que si el argumento `ctx` está configurado correctamente, entonces el buffer de eventos subyacente se basará en sockets OpenSSL. Asimismo, todo el tráfico pasará a través de SSL o TLS.

> [!NOTE]
> Este argumento solo está disponible si `Event` ha sido compilado con soporte para OpenSSL, y solo a partir de la versión `Libevent 2.1.0-alpha` o superiores.

## Historial de cambios

| Versión          | Descripción                           |
|------------------|---------------------------------------|
| PECL event 1.9.0 | Añadido soporte para OpenSSL (`ctx`). |

## Ejemplos

Servidor HTTP simple

```
<?php
/*
 * Servidor HTTP simple.
 *
 * Para probarlo:
 * 1) Ejecútelo en el puerto de su elección, i.e. :
 * $ php examples/http.php 8010
 * 2) En otro terminal, conéctese a una dirección de este puerto
 * y realice una solicitud GET o POST (las otras están deshabilitadas aquí),
 * i.e. :
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
 * $ nc -t 127.0.0.1 8010
 * GET /dump HTTP/1.0
 * Content-Type: text/plain
 * Content-Encoding: UTF-8
 * Connection: close
 * (presione Enter)
 *
 * Debería mostrar:
 * HTTP/1.0 200 OK
 * Content-Type: text/html; charset=ISO-8859-1
 * Connection: close
 * (presione Enter)
 *
 * $ nc -t 127.0.0.1 8010
 * GET /unknown HTTP/1.0
 * Connection: close
 *
 * Debería mostrar:
 * HTTP/1.0 200 OK
 * Content-Type: text/html; charset=ISO-8859-1
 * Connection: close
 *
 * 3) Observe lo que muestra el servidor en el terminal anterior.
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

   
```php

Resultado del ejemplo anterior es similar a:

    a=12
    HTTP/1.0 200 OK
    Content-Type: text/html; charset=ISO-8859-1
    Connection: close

    HTTP/1.0 200 OK
    Content-Type: text/html; charset=ISO-8859-1
    Connection: close
    (presione Enter)

    HTTP/1.0 200 OK
    Content-Type: text/html; charset=ISO-8859-1
    Connection: close
