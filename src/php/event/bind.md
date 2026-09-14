---
title: EventHttp::bind
description: Liga un servidor HTTP a una dirección y un puerto especificados
source_url: https://www.php.net/manual/es/eventhttp.bind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventhttp/bind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: da9d81816
order: 19870
---

EventHttp::bind

Liga un servidor HTTP a una dirección y un puerto especificados

## Descripción

```php
public EventHttp::bind(string $address, int $port): void
```php

Liga un servidor HTTP a una dirección y un puerto especificados.

Puede ser llamada varias veces para ligar el mismo servidor HTTP a varios puertos.

## Parámetros

`address`  
Un string que contiene la dirección IP a escuchar.

`port`  
El número de puerto en el que se realizará la escucha.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `EventHttp::bind`

```
<?php
$base = new EventBase();
$http = new EventHttp($base);

$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);

if (!$http->bind("127.0.0.1", 8088)) {
    exit("bind(1) ha fallado\n");
};
if (!$http->bind("127.0.0.1", 8089)) {
    exit("bind(2) ha fallado\n");

};

$http->setCallback("/about", function($req) {
    echo "URI : ", $req->getUri(), PHP_EOL;
    $req->sendReply(200, "OK");
    echo "OK\n";
});

$base->dispatch();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Cliente:

    $ nc 127.0.0.1 8088
    GET /about HTTP/1.0
    Connection: close

    HTTP/1.0 200 OK
    Content-Type: text/html; charset=ISO-8859-1
    Connection: close

    $ nc 127.0.0.1 8089
    GET /unknown HTTP/1.0
    Connection: close

    HTTP/1.1 404 Not Found
    Content-Type: text/html
    Date: Wed, 13 Mar 2013 04:14:41 GMT
    Content-Length: 149
    Connection: close

    <html><head><title>404 Not Found</title></head><body><h1>Not Found</h1><p>The requested URL /unknown was not found on this server.</p></body></html>

    Servidor:
    URI: /about
    OK

## Véase también

EventHttp::accept
