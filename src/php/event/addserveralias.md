---
title: EventHttp::addServerAlias
description: Añade un alias del servidor para el objeto servidor HTTP
source_url: https://www.php.net/manual/es/eventhttp.addserveralias.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventhttp/addserveralias.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: da9d81816
order: 19860
---

EventHttp::addServerAlias

Añade un alias del servidor para el objeto servidor HTTP

## Descripción

```php
public EventHttp::addServerAlias(string $alias): bool
```php

Añade un alias del servidor para el objeto servidor HTTP.

## Parámetros

`alias`  
El alias a añadir.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `EventHttp::addServerAlias`

```
<?php
$base = new EventBase();
$http = new EventHttp($base);

$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);

if (!$http->bind("127.0.0.1", 8088)) {
    exit("bind(1) ha fallado\n");
};

if (!$http->addServerAlias("local.net")) {
    exit("Imposible añadir el alias del servidor\n");
}

$http->setCallback("/about", function($req) {
    echo "URI : ", $req->getUri(), PHP_EOL;
    $req->sendReply(200, "OK");
});
$base->dispatch();
?>

   
```php

## Véase también

EventHttp::removeServerAlias
