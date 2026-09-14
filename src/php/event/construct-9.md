---
title: EventHttpRequest::__construct
description: Construye un objeto EventHttpRequest
source_url: https://www.php.net/manual/es/eventhttprequest.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventhttprequest/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: b621ab27a
order: 20130
---

EventHttpRequest::\_\_construct

Construye un objeto EventHttpRequest

## Descripción

```php
public EventHttpRequest::__construct(callable $callback, [mixed $data])
```php

Construye un objeto EventHttpRequest.

## Parámetros

`callback`  
Función de retrollamada llamada con la ruta solicitada. Debe corresponder al siguiente prototipo:

```php
callback([EventHttpRequest $req], [mixed $arg]): void
```

`data`  
Datos personalizados del usuario para pasar a la función de retrollamada.

## Ejemplos

Ejemplo con `EventHttpRequest::__construct`

```php
<?php

function _request_handler($req, $base) {
    echo __FUNCTION__, PHP_EOL;

    if (is_null($req)) {
        echo "Tiempo límite de ejecución alcanzado\n";
    } else {
        $response_code = $req->getResponseCode();

        if ($response_code == 0) {
            echo "Conexión rechazada\n";
        } elseif ($response_code != 200) {
            echo "Respuesta inesperada: $response_code\n";
        } else {
            echo "Éxito: $response_code\n";
            $buf = $req->getInputBuffer();
            echo "Body:\n";
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

   
```

## Véase también

EventHttpRequest::cancel

EventHttpRequest::addHeader
