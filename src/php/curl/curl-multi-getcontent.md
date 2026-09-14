---
title: curl_multi_getcontent
description: Devuelve el contenido obtenido con la opción CURLOPT_RETURNTRANSFER
source_url: https://www.php.net/manual/es/function.curl-multi-getcontent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-multi-getcontent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: false
translation_revision: 427ab27e5
order: 9950
---

curl_multi_getcontent

Devuelve el contenido obtenido con la opción

CURLOPT_RETURNTRANSFER

## Descripción

```php
curl_multi_getcontent(CurlHandle $handle): string
```php

Si `CURLOPT_RETURNTRANSFER` es una opción definida para un manejador específico, entonces esta función devolverá el contenido de ese manejador cURL, en forma de `string`.

## Parámetros

`handle`  
Un gestor cURL devuelto por `curl_init`.

## Valores devueltos

Devuelve el contenido del manejador cURL, si `CURLOPT_RETURNTRANSFER` está definido o `null` si no lo está.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `handle` ahora espera una instancia de `CurlHandle` ; anteriormente, se esperaba un `resource`. |

## Véase también

`curl_multi_init`
