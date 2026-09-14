---
title: oauth_get_sbs
description: Genera una cadena de firma base
source_url: https://www.php.net/manual/es/function.oauth-get-sbs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/functions/oauth-get-sbs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_revision: bdee7e8c1
order: 56630
---

oauth_get_sbs

Genera una cadena de firma base

## Descripción

```php
oauth_get_sbs(string $http_method, string $uri, [array $request_parameters]): string
```php

Genera un string de firma base con PECL/OAuth.

## Parámetros

`http_method`  
El método HTTP.

`uri`  
La URI a códificar.

`request_parameters`  
Array de parámetros de petición.

## Valores devueltos

Devuelve el string de firma base.
