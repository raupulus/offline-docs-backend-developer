---
title: curl_error
description: Devuelve un string que contiene el último mensaje de error cURL
source_url: https://www.php.net/manual/es/function.curl-error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_revision: fc9a0a8b2
order: 9860
---

curl_error

Devuelve un string que contiene el último mensaje de error cURL

## Descripción

```php
curl_error(CurlHandle $handle): string
```php

Devuelve un mensaje claro que representa el último error cURL.

## Parámetros

`handle`  
Un gestor cURL devuelto por `curl_init`.

## Valores devueltos

Devuelve el mensaje de error o `''` (string vacío) si no ha ocurrido ningún error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `handle` ahora espera una instancia de `CurlHandle` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `curl_error`

```
<?php
// Creación de un manejador curl hacia una URL inexistente
$ch = curl_init('http://404.php.net/');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

if(curl_exec($ch) === false)
{
    echo 'Error Curl : ' . curl_error($ch);
}
else
{
    echo 'La operación se ha completado sin ningún error';
}
?>

    
```php

## Véase también

`curl_errno`, [Códigos de error Curl](http://curl.haxx.se/libcurl/c/libcurl-errors.html)
