---
title: OAuthProvider::reportProblem
description: Se informa sobre un problema
source_url: https://www.php.net/manual/es/oauthprovider.reportproblem.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauthprovider/reportproblem.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_reviewed: false
translation_revision: bdee7e8c1
order: 57040
---

OAuthProvider::reportProblem

Se informa sobre un problema

## Descripción

```php
final public static OAuthProvider::reportProblem(string $oauthexception, [bool $send_headers]): string
```php

Se informa sobre un problema en forma de excepción `OAuthException`; los problemas posibles se enumeran en la sección de las [constantes OAuth](#oauth.constants).

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`oauthexception`  
La excepción `OAuthException`.

## Valores devueltos

No se retorna ningún valor.

## Véase también

OAuthProvider::checkOAuthRequest

OAuthProvider::isRequestTokenEndpoint
