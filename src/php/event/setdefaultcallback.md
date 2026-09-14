---
title: EventHttp::setDefaultCallback
description: Define la función de retrollamada por defecto para manejar las peticiones
  que no son capturadas por funciones de retrollamada específicas
source_url: https://www.php.net/manual/es/eventhttp.setdefaultcallback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventhttp/setdefaultcallback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: a47dff201
order: 19920
---

EventHttp::setDefaultCallback

Define la función de retrollamada por defecto para manejar las peticiones que no son capturadas por funciones de retrollamada específicas

## Descripción

```php
public EventHttp::setDefaultCallback(string $cb, [string $arg]): void
```php

Define la función de retrollamada por defecto para manejar las peticiones que no son capturadas por funciones de retrollamada específicas.

## Parámetros

`cb`  
La función de retrollamada de tipo `callable`. Debe corresponder al siguiente prototipo:

```php
callback([EventHttpRequest $req], [mixed $arg]): void
```

`req`  
`EventHttpRequest` Objeto.

`arg`  
Datos personalizados.

`arg`  
Datos personalizados proporcionados por el usuario a la función de retrollamada.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `EventHttp::setDefaultCallback`

```php
<?php
$base = new EventBase();
$http = new EventHttp($base);

$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);

if (!$http->bind("127.0.0.1", 8088)) {
    exit("Fallo en bind(1)\n");
};

$http->setDefaultCallback(function($req) {
    echo "URI : ", $req->getUri(), PHP_EOL;
    $req->sendReply(200, "OK");
});

$base->dispatch();
?>

   
```

## Véase también

EventHttp::setCallback
