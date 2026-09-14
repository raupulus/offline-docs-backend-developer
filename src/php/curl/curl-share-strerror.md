---
title: curl_share_strerror
description: Devuelve un string que describe el código de error proporcionado
source_url: https://www.php.net/manual/es/function.curl-share-strerror.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/functions/curl-share-strerror.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: false
translation_revision: b7f8c11e5
order: 10110
---

curl_share_strerror

Devuelve un string que describe el código de error proporcionado

## Descripción

```php
curl_share_strerror(int $error_code): string
```php

Devuelve un mensaje de error textual que describe el código de error proporcionado.

## Parámetros

`error_code`  
Una de las constantes de los [códigos de error cURL](http://curl.haxx.se/libcurl/c/libcurl-errors.html).

## Valores devueltos

Devuelve una descripción del error o `null` para los códigos de error inválidos.

## Véase también

curl_share_errno

curl_strerror
