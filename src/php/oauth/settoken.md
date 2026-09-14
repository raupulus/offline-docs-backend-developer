---
title: OAuth::setToken
description: Establece el token y el secreto
source_url: https://www.php.net/manual/es/oauth.settoken.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauth/settoken.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_revision: bdee7e8c1
order: 56890
---

OAuth::setToken

Establece el token y el secreto

## Descripción

```php
public OAuth::setToken(string $token, string $token_secret): bool
```php

Establece el token y el secreto para las subsecuentes peticiones.

## Parámetros

`token`  
El token OAuth.

`token_secret`  
El secreto OAuth.

## Valores devueltos

`true`

## Ejemplos

Ejemplo `OAuth::setToken`

```
<?php
$oauth = new OAuth(OAUTH_CONSUMER_KEY,OAUTH_CONSUMER_SECRET);
$oauth->setToken("token","token-secret");
?>

   
```php
