---
title: OAuth::__construct
description: Crea un nuevo objeto OAuth
source_url: https://www.php.net/manual/es/oauth.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauth/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_reviewed: false
translation_revision: bdee7e8c1
order: 56650
---

OAuth::\_\_construct

Crea un nuevo objeto OAuth

## Descripción

```php
public OAuth::__construct(string $consumer_key, string $consumer_secret, [string $signature_method], [int $auth_type])
```php

Crea un nuevo objeto OAuth.

## Parámetros

`consumer_key`  
La clave de consumidor proporcionada por el proveedor de servicios.

`consumer_secret`  
El secreto de consumidor proporcionado por el proveedor de servicios.

`signature_method`  
Este parámetro opcional define el método de firma utilizado. Por omisión, es `OAUTH_SIG_METHOD_HMACSHA1` (HMAC-SHA1).

`auth_type`  
Este parámetro opcional define el método de paso de los parámetros OAuth al proveedor de servicios. Por omisión, es `OAUTH_AUTH_TYPE_AUTHORIZATION` (en el encabezado `Authorization`).
