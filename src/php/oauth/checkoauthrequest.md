---
title: OAuthProvider::checkOAuthRequest
description: Verifica una petición OAuth
source_url: https://www.php.net/manual/es/oauthprovider.checkoauthrequest.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauthprovider/checkoauthrequest.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_reviewed: false
translation_revision: bdee7e8c1
order: 56970
---

OAuthProvider::checkOAuthRequest

Verifica una petición OAuth

## Descripción

```php
public OAuthProvider::checkOAuthRequest([string $uri], [string $method]): void
```php

Verifica una petición OAuth.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`uri`  
La URI, opcional, o un punto final.

`method`  
El método HTTP. Opcional; pase una de las constantes OAuth `OAUTH_HTTP_METHOD_*`.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Emite un error de nivel `E_ERROR` si el método HTTP no puede ser detectado.

## Véase también

OAuthProvider::reportProblem
