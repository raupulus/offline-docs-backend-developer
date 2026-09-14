---
title: OAuthProvider::isRequestTokenEndpoint
description: Establece isRequestTokenEndpoint
source_url: https://www.php.net/manual/es/oauthprovider.isrequesttokenendpoint.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauthprovider/isrequesttokenendpoint.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_revision: bdee7e8c1
order: 57020
---

OAuthProvider::isRequestTokenEndpoint

Establece isRequestTokenEndpoint

## Descripción

```php
public OAuthProvider::isRequestTokenEndpoint(bool $will_issue_request_token): void
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`will_issue_request_token`  
Establece si emitirá o no una emisión de petición de token, determinando si OAuthProvider::tokenHandler necesita ser llamado.

## Valores devueltos

No se retorna ningún valor.

## Véase también

OAuthProvider::setRequestTokenPath

OAuthProvider::reportProblem
