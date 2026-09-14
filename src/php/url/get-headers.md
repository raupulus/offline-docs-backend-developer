---
title: get_headers
description: Devuelve todos los encabezados enviados por el servidor en respuesta
  a una petición HTTP
source_url: https://www.php.net/manual/es/function.get-headers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/url/functions/get-headers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: url
translation_status: ready
translation_reviewed: false
translation_revision: 943c1285b
order: 100210
---

get_headers

Devuelve todos los encabezados enviados por el servidor en respuesta a una petición HTTP

## Descripción

```php
get_headers(string $url, [bool $associative], [resource $context]): array
```php

`get_headers` devuelve un array con los encabezados enviados por el servidor en respuesta a una petición HTTP.

## Parámetros

`url`  
La URL de destino.

`associative`  
Si el argumento opcional `associative` está definido como `true`, `get_headers` analiza la respuesta y define los índices del array.

`context`  
Un contexto de recurso válido creado con `stream_context_create`, o `null` para utilizar el contexto por omisión.

## Valores devueltos

Devuelve un array indexado o asociativo que contiene los encabezados, o `false` en caso de error.

## Historial de cambios

| Versión | Descripción                                       |
|---------|---------------------------------------------------|
| 8.0.0   | `associative` ha sido cambiado de `int` a `bool`. |
| 7.1.0   | El argumento `context` ha sido añadido.           |

## Ejemplos

Ejemplo con `get_headers`

```
<?php
$url = 'http://www.example.com';

print_r(get_headers($url));

print_r(get_headers($url, true));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => HTTP/1.1 200 OK
        [1] => Date: Sat, 29 May 2004 12:28:13 GMT
        [2] => Server: Apache/1.3.27 (Unix)  (Red-Hat/Linux)
        [3] => Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
        [4] => ETag: "3f80f-1b6-3e1cb03b"
        [5] => Accept-Ranges: bytes
        [6] => Content-Length: 438
        [7] => Connection: close
        [8] => Content-Type: text/html
    )

    Array
    (
        [0] => HTTP/1.1 200 OK
        [Date] => Sat, 29 May 2004 12:28:14 GMT
        [Server] => Apache/1.3.27 (Unix)  (Red-Hat/Linux)
        [Last-Modified] => Wed, 08 Jan 2003 23:11:55 GMT
        [ETag] => "3f80f-1b6-3e1cb03b"
        [Accept-Ranges] => bytes
        [Content-Length] => 438
        [Connection] => close
        [Content-Type] => text/html
    )

Ejemplo con `get_headers` utilizando HEAD

```
<?php
// Por omisión, get_headers utiliza una petición GET para recuperar los
// encabezados. Si se desea enviar una petición HEAD, puede hacerse
// utilizando un contexto de flujo:
$context = stream_context_create(
    [
        'http' => array(
            'method' => 'HEAD'
        )
    ]
);
$headers = get_headers('http://example.com', false, $context);
?>

    
```php

## Véase también

`apache_request_headers`
