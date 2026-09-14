---
title: curl_share_init
description: Inicializa un manejador compartido cURL
source_url: https://www.php.net/manual/es/function.curl-share-init.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-share-init.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_revision: fc9a0a8b2
order: 10090
---

curl_share_init

Inicializa un manejador compartido cURL

## Descripción

```php
curl_share_init(): CurlShareHandle
```php

Permite el intercambio de datos entre manejadores cURL.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un manejador cURL compartido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función devuelve ahora una instancia de `CurlShareHandle`; anteriormente, se devolvía un `resource`. |

## Ejemplos

Ejemplo con `curl_share_init`

Este ejemplo crea un manejador compartido cURL, añade dos manejadores cURL, y luego los ejecuta con cookies de datos compartidos.

```
<?php
// Crea un manejador compartido cURL, y lo configura para compartir datos de cookies
$sh = curl_share_init();
curl_share_setopt($sh, CURLSHOPT_SHARE, CURL_LOCK_DATA_COOKIE);

// Inicializa el primer manejador cURL, y le asigna el manejador compartido
$ch1 = curl_init("http://example.com/");
curl_setopt($ch1, CURLOPT_SHARE, $sh);

// Ejecuta el primer manejador cURL
curl_exec($ch1);

// Inicializa el segundo manejador cURL y le asigna el manejador compartido
$ch2 = curl_init("http://php.net/");
curl_setopt($ch2, CURLOPT_SHARE, $sh);

// Ejecuta el segundo manejador cURL.
// Todas las cookies del manejador $ch1 son compartidas con el manejador $ch2.
curl_exec($ch2);
?>

    
```php

## Véase también

`curl_share_setopt`, `curl_share_init_persistent`
