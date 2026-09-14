---
title: curl_share_errno
description: Devuelve el último número de error del gestor compartido cURL
source_url: https://www.php.net/manual/es/function.curl-share-errno.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-share-errno.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: false
translation_revision: 3f118edd6
order: 10070
---

curl_share_errno

Devuelve el último número de error del gestor compartido cURL

## Descripción

```php
curl_share_errno(CurlShareHandle $share_handle): int
```php

Devuelve un integer que contiene el último número de error del gestor compartido cURL.

## Parámetros

`share_handle`  
Un gestor compartido cURL devuelto por `curl_share_init`.

## Valores devueltos

Devuelve un integer que contiene el último número de error del gestor compartido cURL.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | La función ya no devuelve `false` en caso de fallo. |
| 8.0.0 | `share_handle` ahora espera una instancia de `CurlShareHandle` ; anteriormente, se esperaba un `resource`. |

## Véase también

curl_errno
