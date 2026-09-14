---
title: curl_multi_remove_handle
description: Retira un manejador de un conjunto de manejadores cURL
source_url: https://www.php.net/manual/es/function.curl-multi-remove-handle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-multi-remove-handle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: false
translation_revision: 64436290a
order: 9980
---

curl_multi_remove_handle

Retira un manejador de un conjunto de manejadores cURL

## Descripción

```php
curl_multi_remove_handle(CurlMultiHandle $multi_handle, CurlHandle $handle): int
```php

Retira un manejador `handle` dado del `multi_handle`. Cuando el manejador `handle` ha sido retirado, es nuevamente perfectamente correcto ejecutar la función `curl_exec`. El hecho de retirar el `handle` en uso detiene todas las transferencias en curso.

## Parámetros

`multi_handle`  
Un gestor múltiple cURL devuelto por `curl_multi_init`.

`handle`  
Un gestor cURL devuelto por `curl_init`.

## Valores devueltos

Retorna 0 en caso de éxito, o uno de los códigos de error `CURLM_*`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `multi_handle` ahora espera una instancia de `CurlMultiHandle` ; anteriormente, se esperaba un `resource`. |
| 8.0.0 | `handle` ahora espera una instancia de `CurlHandle` ; anteriormente, se esperaba un `resource`. |

## Véase también

`curl_init`, `curl_multi_init`, `curl_multi_add_handle`
