---
title: curl_multi_errno
description: Devuelve el último número de error múltiple cURL
source_url: https://www.php.net/manual/es/function.curl-multi-errno.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-multi-errno.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: false
translation_revision: 7f99d5e48
order: 9930
---

curl_multi_errno

Devuelve el último número de error múltiple cURL

## Descripción

```php
curl_multi_errno(CurlMultiHandle $multi_handle): int
```php

Devuelve un integer que contiene el último número de error múltiple cURL.

## Parámetros

`multi_handle`  
Un gestor múltiple cURL devuelto por `curl_multi_init`.

## Valores devueltos

Devuelve un integer que contiene el último número de error múltiple cURL.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función ya no devuelve `false` en caso de fallo. |
| 8.0.0 | `multi_handle` ahora espera una instancia de `CurlMultiHandle` ; anteriormente, se esperaba un `resource`. |

## Véase también

curl_errno
