---
title: Yar_Concurrent_Client::call
description: Registrar una llamada concurrente
source_url: https://www.php.net/manual/es/yar-concurrent-client.call.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yar/yar_concurrent_client/call.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yar
translation_status: ready
translation_revision: c50df321d
order: 107660
---

Yar_Concurrent_Client::call

Registrar una llamada concurrente

## Descripción

```php
public static Yar_Concurrent_Client::call(string $uri, string $method, [array $parameters], [callable $callback], [callable $error_callback], [array $options]): int
```php

Registra una llamada RPC, aunque no la envía inmediatamente. Se enviará al llamar a Yar_Concurrent_Client::loop.

## Parámetros

`uri`  
El URI del servidor de RPC (HTTP, TCP).

`method`  
El nombre del servicio (es decir, el nombre del método).

`parameters`  
Parámetros.

`callback`  
Una retrollamada a una función, la cual será invocada mientras se devuelve la respuesta.

`error_callback`  
Si se establece esta retrollamada, Yar la invocará cuando ocurra un error.

`options`  
Un `array` de opciones. Ver la lista de [constantes](#yar.constants).

## Valores devueltos

Un ID único que se puede utilizar para identificar la llamada que es.

## Ejemplos

```
<?php

function callback($retval, $callinfo)
{
    var_dump($retval);
}

function error_callback($type, $error, $callinfo)
{
    error_log($error);
}

Yar_Concurrent_Client::call("http://host/api/", "some_method", array("parameters"), "callback");

// Si no se especifica la retrollamada, se usará la retrollamada en bucle
Yar_Concurrent_Client::call("http://host/api/", "some_method", array("parameters"));

// Este servidor acepta empaquetador JSON
Yar_Concurrent_Client::call("http://host/api/", "some_method", array("parameters"), "callback", NULL, array(YAR_OPT_PACKAGER => "json"));

// Tiempo de espera personalizado
Yar_Concurrent_Client::call("http://host/api/", "some_method", array("parameters"), "callback", NULL, array(YAR_OPT_TIMEOUT => 1));

// Las peticiones aún no se han enviado

   
```php

Resultado del ejemplo anterior es similar a:

## Véase también

Yar_Concurrent_Client::loop

Yar_Concurrent_Client::reset

Yar_Server::\_\_construct

Yar_Server::handle
