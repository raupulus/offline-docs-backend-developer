---
title: http_get_last_response_headers
description: Obtiene los últimos encabezados de respuesta HTTP
source_url: https://www.php.net/manual/es/function.http-get-last-response-headers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/http-get-last-response-headers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: true
translation_revision: 3f1cd5121
order: 56430
---

http_get_last_response_headers

Obtiene los últimos encabezados de respuesta HTTP

## Descripción

```php
http_get_last_response_headers(): array
```php

Obtiene un `array` que contiene los últimos encabezados de respuesta HTTP recibidos a través de [la envoltura HTTP](#wrappers.http). Si no hay ninguno, se devuelve `null` en su lugar.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `array` indexado de los encabezados HTTP que fueron recibidos al utilizar [la envoltura HTTP](#wrappers.http). Si no hay ninguno, se devuelve `null` en su lugar.

## Ejemplos

Ejemplo de `http_get_last_response_headers`

Descripción.

```
<?php
file_get_contents("http://example.com");
var_dump(http_get_last_response_headers());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(14) {
      [0]=>
      string(15) "HTTP/1.1 200 OK"
      [1]=>
      string(20) "Accept-Ranges: bytes"
      [2]=>
      string(11) "Age: 326940"
      [3]=>
      string(29) "Cache-Control: max-age=604800"
      [4]=>
      string(38) "Content-Type: text/html; charset=UTF-8"
      [5]=>
      string(35) "Date: Mon, 11 Nov 2024 13:34:09 GMT"
      [6]=>
      string(23) "Etag: "3147526947+gzip""
      [7]=>
      string(38) "Expires: Mon, 18 Nov 2024 13:34:09 GMT"
      [8]=>
      string(44) "Last-Modified: Thu, 17 Oct 2019 07:18:26 GMT"
      [9]=>
      string(24) "Server: ECAcc (nyd/D16C)"
      [10]=>
      string(21) "Vary: Accept-Encoding"
      [11]=>
      string(12) "X-Cache: HIT"
      [12]=>
      string(20) "Content-Length: 1256"
      [13]=>
      string(17) "Connection: close"
    }

## Véase también

http_clear_last_response_headers
