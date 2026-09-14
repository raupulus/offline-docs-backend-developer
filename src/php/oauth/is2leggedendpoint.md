---
title: OAuthProvider::is2LeggedEndpoint
description: is2LeggedEndpoint
source_url: https://www.php.net/manual/es/oauthprovider.is2leggedendpoint.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauthprovider/is2leggedendpoint.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_revision: bdee7e8c1
order: 57010
---

OAuthProvider::is2LeggedEndpoint

is2LeggedEndpoint

## Descripción

```php
public OAuthProvider::is2LeggedEndpoint(mixed $params_array): void
```php

El flujo de 2-piernas, o la suscripción de petición. No requiere token.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`params_array`  

## Valores devueltos

Un `object` de `OAuthProvider`.

## Ejemplos

Ejemplo de `OAuthProvider::is2LeggedEndpoint`

```
<?php

$provider = new OAuthProvider();

$provider->is2LeggedEndpoint(true);

?>

   
```php

## Véase también

OAuthProvider::\_\_construct
