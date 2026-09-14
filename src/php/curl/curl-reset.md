---
title: curl_reset
description: Reinicia todas las opciones de un manejador de sesión libcurl
source_url: https://www.php.net/manual/es/function.curl-reset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-reset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_revision: fc9a0a8b2
order: 10030
---

curl_reset

Reinicia todas las opciones de un manejador de sesión libcurl

## Descripción

```php
curl_reset(CurlHandle $handle): void
```php

Esta función reinicia todas las opciones definidas en el manejador cURL dado a sus valores por omisión.

## Parámetros

`handle`  
Un gestor cURL devuelto por `curl_init`.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `handle` ahora espera una instancia de `CurlHandle` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `curl_reset`

```
<?php
// Crea un manejador cURL
$ch = curl_init();

// Define la opción CURLOPT_USERAGENT
curl_setopt($ch, CURLOPT_USERAGENT, "Mi user-agent de prueba");

// Reinicia todas las opciones definidas previamente
curl_reset($ch);

// Envía la petición HTTP
curl_setopt($ch, CURLOPT_URL, 'http://example.com/');
curl_exec($ch); // el user-agent definido previamente no será enviado, fue reiniciado por la función curl_reset
?>

    
```php

## Notas

> [!NOTE]
> La función `curl_reset` también reiniciará la URL proporcionada como argumento de la función `curl_init`.

## Véase también

`curl_setopt`
