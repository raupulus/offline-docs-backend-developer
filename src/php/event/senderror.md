---
title: EventHttpRequest::sendError
description: Envía un mensaje de error HTML al cliente
source_url: https://www.php.net/manual/es/eventhttprequest.senderror.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventhttprequest/senderror.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 7cecc752c
order: 20270
---

EventHttpRequest::sendError

Envía un mensaje de error HTML al cliente

## Descripción

```php
public EventHttpRequest::sendError(int $error, [string $reason]): void
```php

Envía un mensaje de error HTML al cliente.

## Parámetros

`error`  
El código de error HTTP.

`reason`  
Una breve explicación del error. Si es `null`, se utilizará el significado estándar del código de error.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `EventHttpRequest::sendError`

```
<?php
function _http_400($req) {
    $req->sendError(400);
}

$base = new EventBase();
$http = new EventHttp($base);

$http->setCallback("/err400", "_http_400");

$http->bind("0.0.0.0", 8010);
$base->loop();
?>

   
```php

## Véase también

EventHttpRequest::sendReply
