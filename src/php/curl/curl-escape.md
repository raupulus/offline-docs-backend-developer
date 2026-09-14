---
title: curl_escape
description: Codificar la cadena proporcionada para URL
source_url: https://www.php.net/manual/es/function.curl-escape.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-escape.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_revision: 98ee565bf
order: 9870
---

curl_escape

Codificar la cadena proporcionada para URL

## Descripción

```php
curl_escape(CurlHandle $handle, string $string): string
```php

Esta función codifica la cadena proporcionada para URL según [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986).

## Parámetros

`handle`  
Un gestor cURL devuelto por `curl_init`.

`string`  
La cadena a codificar.

## Valores devueltos

Devuelve la cadena codificada o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `handle` ahora espera una instancia de `CurlHandle` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `curl_escape`

```
<?php

// Crea un manejador curl
$ch = curl_init();

// Escapa una cadena utilizada como parámetro GET
$location = curl_escape($ch, 'Hofbräuhaus / München');
// Resultado: Hofbr%C3%A4uhaus%20%2F%20M%C3%BCnchen

// Compone una URL con la cadena escapada
$url = "http://example.com/add_location.php?location={$location}";
// Resultado: http://example.com/add_location.php?location=Hofbr%C3%A4uhaus%20%2F%20M%C3%BCnchen

// Establece las opciones y envía la petición HTTP
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_exec($ch);
?>

    
```php

## Véase también

`curl_unescape`, `urlencode`, `rawurlencode`, [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986)
