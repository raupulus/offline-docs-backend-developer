---
title: OAuthProvider::tokenHandler
description: Establece el manejador callback de tokenHandler
source_url: https://www.php.net/manual/es/oauthprovider.tokenhandler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauthprovider/tokenhandler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_revision: bdee7e8c1
order: 57080
---

OAuthProvider::tokenHandler

Establece el manejador callback de tokenHandler

## Descripción

```php
public OAuthProvider::tokenHandler(callable $callback_function): void
```php

Establece el token del callback, que será llamado después con OAuthProvider::callTokenHandler.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`callback_function`  
El nombre de la función `callable`.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo del callback OAuthProvider::tokenHandler

```
<?php
function tokenHandler($provider) {

    if ($provider->token === 'rejected') {
        return OAUTH_TOKEN_REJECTED;
    } elseif ($provider->token === 'revoked') {
        return OAUTH_TOKEN_REVOKED;
    }

    $provider->token_secret = "the_tokens_secret";
    return OAUTH_OK;
}
?>

   
```php

## Véase también

OAuthProvider::callTokenHandler
