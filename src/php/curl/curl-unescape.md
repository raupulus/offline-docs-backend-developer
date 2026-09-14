---
title: curl_unescape
description: Decodifica la URL proporcionada
source_url: https://www.php.net/manual/es/function.curl-unescape.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-unescape.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_revision: fc9a0a8b2
order: 10130
---

curl_unescape

Decodifica la URL proporcionada

## Descripción

```php
curl_unescape(CurlHandle $handle, string $string): string
```php

Esta función decodifica la URL proporcionada.

## Parámetros

`handle`  
Un gestor cURL devuelto por `curl_init`.

`string`  
La URL codificada, a decodificar.

## Valores devueltos

Devuelve el string decodificado o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `handle` ahora espera una instancia de `CurlHandle` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `curl_escape`

```
<?php
// Creación de un manejador curl
$ch = curl_init('http://example.com/redirect.php');

// Envía una petición HTTP y sigue las redirecciones
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
curl_exec($ch);

// Obtiene la última URL efectiva
$effective_url = curl_getinfo($ch, CURLINFO_EFFECTIVE_URL);
// es decir, "http://example.com/show_location.php?loc=M%C3%BCnchen"

// Decodifica la URL
$effective_url_decoded = curl_unescape($ch, $effective_url);
// "http://example.com/show_location.php?loc=München"
?>

    
```php

## Notas

> [!NOTE]
> `curl_unescape` no decodifica los símbolos "más" (+) en espacios, a diferencia de la función `urldecode`.

## Véase también

`curl_escape`, `urlencode`, `urldecode`, `rawurlencode`, `rawurldecode`
