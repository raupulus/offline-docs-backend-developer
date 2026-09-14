---
title: OAuthProvider::setParam
description: Establece un parámetro
source_url: https://www.php.net/manual/es/oauthprovider.setparam.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauthprovider/setparam.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_revision: bdee7e8c1
order: 57050
---

OAuthProvider::setParam

Establece un parámetro

## Descripción

```php
final public OAuthProvider::setParam(string $param_key, [mixed $param_val]): bool
```php

Establece un parámetro.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`param_key`  
La clave del parámetro.

`param_val`  
El valor opcional del parámetro.

Para excluir un parámetro de la verificación de firmas, colocar este valor a `null`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

OAuthProvider::addRequiredParameter
