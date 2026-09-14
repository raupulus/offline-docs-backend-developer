---
title: EventHttpConnection::makeRequest
description: Realiza una petición HTTP en la conexión especificada
source_url: https://www.php.net/manual/es/eventhttpconnection.makerequest.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventhttpconnection/makerequest.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 20000
---

EventHttpConnection::makeRequest

Realiza una petición HTTP en la conexión especificada

## Descripción

```php
public EventHttpConnection::makeRequest(EventHttpRequest $req, int $type, string $uri): bool
```php

Realiza una petición HTTP en la conexión especificada. El parámetro `type` será una constante `EventHttpRequest::CMD_*`.

## Parámetros

`req`  
El objeto que representa la conexión en la que se enviará la petición.

`type`  
Una constante [`EventHttpRequest::CMD_*`](#eventhttprequest.constants).

`uri`  
El URI asociado a la petición.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `EventHttpConnection::makeRequest`

```
<?php
function _request_handler($req, $base) {
    echo __FUNCTION__, PHP_EOL;

    if (is_null($req)) {
        echo "Tiempo límite excedido\n";
    } else {
        $response_code = $req->getResponseCode();

        if ($response_code == 0) {
            echo "Conexión rechazada\n";
        } elseif ($response_code != 200) {
            echo "Respuesta inesperada: $response_code\n";
        } else {
            echo "Éxito: $response_code\n";
            $buf = $req->getInputBuffer();
            echo "Cuerpo:\n";
            while ($s = $buf->readLine(EventBuffer::EOL_ANY)) {
                echo $s, PHP_EOL;
            }
        }
    }

    $base->exit(NULL);
}

$address = "127.0.0.1";
$port = 80;

$base = new EventBase();
$conn = new EventHttpConnection($base, NULL, $address, $port);
$conn->setTimeout(5);
$req = new EventHttpRequest("_request_handler", $base);

$req->addHeader("Host", $address, EventHttpRequest::OUTPUT_HEADER);
$req->addHeader("Content-Length", "0", EventHttpRequest::OUTPUT_HEADER);
$conn->makeRequest($req, EventHttpRequest::CMD_GET, "/index.cphp");

$base->loop();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    _request_handler
    Éxito: 200
    Cuerpo:
    PHP, date:
    2013-03-13T20:27:52+05:00

## Véase también

EventHttpRequest::addHeader
