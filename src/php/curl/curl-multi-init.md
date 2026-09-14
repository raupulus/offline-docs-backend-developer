---
title: curl_multi_init
description: Devuelve un nuevo cURL múltiple
source_url: https://www.php.net/manual/es/function.curl-multi-init.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-multi-init.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: false
translation_revision: 92226911a
order: 9970
---

curl_multi_init

Devuelve un nuevo cURL múltiple

## Descripción

```php
curl_multi_init(): CurlMultiHandle
```php

Permite la ejecución de múltiples gestores cURL de forma asíncrona.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un gestor cURL múltiple.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función devuelve ahora una instancia de `CurlMultiHandle`; anteriormente, se devolvía un `resource`. |

## Véase también

`curl_init`, `curl_multi_close`
