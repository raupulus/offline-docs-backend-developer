---
title: curl_multi_strerror
description: Devuelve la descripción de un código de error
source_url: https://www.php.net/manual/es/function.curl-multi-strerror.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-multi-strerror.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: false
translation_revision: 56171c30f
order: 10010
---

curl_multi_strerror

Devuelve la descripción de un código de error

## Descripción

```php
curl_multi_strerror(int $error_code): string
```php

Devuelve el mensaje de error que describe el código de error `CURLM_*` proporcionado.

## Parámetros

`error_code`  
Una constante entre las constantes de `CURLM_*`

## Valores devueltos

Devuelve la descripción de un código de error válido, `null` en caso contrario.

## Véase también

`curl_strerror`, [los códigos de error cURL](http://curl.haxx.se/libcurl/c/libcurl-errors.html)
