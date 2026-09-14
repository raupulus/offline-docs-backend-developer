---
title: curl_multi_add_handle
description: Añade un recurso cURL a un cURL múltiple
source_url: https://www.php.net/manual/es/function.curl-multi-add-handle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-multi-add-handle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: false
translation_revision: 89ae180a8
order: 9910
---

curl_multi_add_handle

Añade un recurso cURL a un cURL múltiple

## Descripción

```php
curl_multi_add_handle(CurlMultiHandle $multi_handle, CurlHandle $handle): int
```php

Añade la sesión `handle` al gestor múltiple `multi_handle`

## Parámetros

`multi_handle`  
Un gestor múltiple cURL devuelto por `curl_multi_init`.

`handle`  
Un gestor cURL devuelto por `curl_init`.

## Valores devueltos

Devuelve `0` en caso de éxito, o uno de los códigos de error `CURLM_*`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `multi_handle` ahora espera una instancia de `CurlMultiHandle` ; anteriormente, se esperaba un `resource`. |
| 8.0.0 | `handle` ahora espera una instancia de `CurlHandle` ; anteriormente, se esperaba un `resource`. |

## Véase también

`curl_multi_remove_handle`, `curl_multi_init`, `curl_init`
