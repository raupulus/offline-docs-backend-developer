---
title: OAuthProvider::__construct
description: Construye un nuevo objeto OAuthProvider
source_url: https://www.php.net/manual/es/oauthprovider.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauthprovider/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_revision: bdee7e8c1
order: 56980
---

OAuthProvider::\_\_construct

Construye un nuevo objeto OAuthProvider

## Descripción

```php
public OAuthProvider::__construct([array $params_array])
```php

Inicia un nuevo `object` `OAuthProvider` .

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`params_array`  
La configuración de estos parámetros opcionales se limita al [CLI SAPI](#features.commandline).

## Valores devueltos

Un `object` `OAuthProvider` .

## Ejemplos

Ejemplo de `OAuthProvider::__construct`

```
<?php
try {

    $op = new OAuthProvider();

    // Usa funciones callback definidas por el usuario
    $op->consumerHandler(array($this, 'lookupConsumer'));
    $op->timestampNonceHandler(array($this, 'timestampNonceChecker'));
    $op->tokenHandler(array($this, 'myTokenHandler'));

    // Ignora el parámetro foo_uri
    $op->setParam('foo_uri', NULL);

    // No es necesario el token para este punto final
    $op->setRequestTokenPath('/v1/oauth/request_token');

    $op->checkOAuthRequest();

} catch (OAuthException $e) {

    echo OAuthProvider::reportProblem($e);
}
?>

   
```php

## Véase también

OAuthProvider::setParam
