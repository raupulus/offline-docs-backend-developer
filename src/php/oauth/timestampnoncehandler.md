---
title: OAuthProvider::timestampNonceHandler
description: Establece el callback timestampNonceHandler
source_url: https://www.php.net/manual/es/oauthprovider.timestampnoncehandler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauthprovider/timestampnoncehandler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_revision: bdee7e8c1
order: 57070
---

OAuthProvider::timestampNonceHandler

Establece el callback timestampNonceHandler

## Descripción

```php
public OAuthProvider::timestampNonceHandler(callable $callback_function): void
```php

Establece el manejador callback timestamp nonce, el cual será llamado luego con OAuthProvider::callTimestampNonceHandler. Errores relacionados con timestamp/nonce son lanzados a este callback.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`callback_function`  
El nombre de la función `callable`.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de OAuthProvider::timestampNonceHandler

```
<?php
function timestampNonceChecker($provider) {

    if ($provider->nonce === 'bad') {
        return OAUTH_BAD_NONCE;
    } elseif ($provider->timestamp == '0') {
        return OAUTH_BAD_TIMESTAMP;
    }

    return OAUTH_OK;
}
?>

   
```php

## Véase también

OAuthProvider::callTimestampNonceHandler
