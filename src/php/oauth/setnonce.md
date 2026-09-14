---
title: OAuth::setNonce
description: Configura el nonce OAuth
source_url: https://www.php.net/manual/es/oauth.setnonce.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauth/setnonce.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_reviewed: false
translation_revision: bdee7e8c1
order: 56840
---

OAuth::setNonce

Configura el nonce OAuth

## Descripción

```php
public OAuth::setNonce(string $nonce): mixed
```php

Configura el nonce OAuth para las llamadas siguientes.

## Parámetros

`nonce`  
El valor de oauth_nonce.

## Valores devueltos

Devuelve `true` en caso de éxito, o `false` si el argumento `nonce` es considerado inválido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL oauth 1.0.0 | Antes de esta versión, `null` era devuelto en lugar de `false`. |

## Véase también

OAuth::setToken

OAuth::setAuthType

OAuth::setVersion
