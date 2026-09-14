---
title: curl_multi_setopt
description: Define una opción múltiple cURL
source_url: https://www.php.net/manual/es/function.curl-multi-setopt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-multi-setopt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: false
translation_revision: 56171c30f
order: 10000
---

curl_multi_setopt

Define una opción múltiple cURL

## Descripción

```php
curl_multi_setopt(CurlMultiHandle $multi_handle, int $option, mixed $value): bool
```php

Define una opción en el manejador multi cURL dado.

## Parámetros

`multi_handle`  
Un gestor múltiple cURL devuelto por `curl_multi_init`.

`option`  
Una de las constantes `CURLMOPT_*`.

`value`  
El valor a definir para el parámetro `option`. Ver la descripción de las constantes `CURLMOPT_*` para detalles sobre el tipo de valores esperados por cada constante.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | Añadido `CURLMOPT_MAX_CONCURRENT_STREAMS`. |
| 8.0.0 | `multi_handle` ahora espera una instancia de `CurlMultiHandle` ; anteriormente, se esperaba un `resource`. |
| 7.1.0 | Añadido `CURLMOPT_PUSHFUNCTION`. |
| 7.0.7 | Añadido `CURLMOPT_CHUNK_LENGTH_PENALTY_SIZE`, `CURLMOPT_CONTENT_LENGTH_PENALTY_SIZE`, `CURLMOPT_MAX_HOST_CONNECTIONS`, `CURLMOPT_MAX_PIPELINE_LENGTH` y `CURLMOPT_MAX_TOTAL_CONNECTIONS`. |
