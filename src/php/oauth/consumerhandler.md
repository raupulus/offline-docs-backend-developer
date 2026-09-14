---
title: OAuthProvider::consumerHandler
description: Establece el manejador callback consumerHandler
source_url: https://www.php.net/manual/es/oauthprovider.consumerhandler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauthprovider/consumerhandler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_revision: bdee7e8c1
order: 56990
---

OAuthProvider::consumerHandler

Establece el manejador callback consumerHandler

## Descripción

```php
public OAuthProvider::consumerHandler(callable $callback_function): void
```php

Establece el manejador callback, que más tarde será llamado con OAuthProvider::callConsumerHandler.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`callback_function`  
El nombre de la función `callable`.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo del callback OAuthProvider::consumerHandler

```
<?php
function lookupConsumer($provider) {

    if ($provider->consumer_key === 'unknown') {
        return OAUTH_CONSUMER_KEY_UNKNOWN;
    } else if($provider->consumer_key == 'blacklisted' || $provider->consumer_key === 'throttled') {
        return OAUTH_CONSUMER_KEY_REFUSED;
    }

    $provider->consumer_secret = "the_consumers_secret";

    return OAUTH_OK;
}
?>

   
```php

## Véase también

OAuthProvider::callConsumerHandler
