---
title: curl_errno
description: Devuelve el último mensaje de error cURL
source_url: https://www.php.net/manual/es/function.curl-errno.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-errno.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_revision: fc9a0a8b2
order: 9850
---

curl_errno

Devuelve el último mensaje de error cURL

## Descripción

```php
curl_errno(CurlHandle $handle): int
```php

Devuelve el número de error de la última operación cURL.

## Parámetros

`handle`  
Un gestor cURL devuelto por `curl_init`.

## Valores devueltos

Devuelve el número de error o `0` si no ha ocurrido ningún error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `handle` ahora espera una instancia de `CurlHandle` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `curl_errno`

```
<?php
// Creación de un manejador curl hacia una URL inexistente
$ch = curl_init('http://404.php.net/');

// Ejecución
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_exec($ch);

// Verifica si ocurre un error
if(curl_errno($ch))
{
    echo 'Error Curl : ' . curl_error($ch);
}
?>

    
```php

## Véase también

`curl_error`, [los códigos de error cURL](http://curl.haxx.se/libcurl/c/libcurl-errors.html)
