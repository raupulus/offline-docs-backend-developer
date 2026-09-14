---
title: OAuth::setAuthType
description: Define el tipo de autorización
source_url: https://www.php.net/manual/es/oauth.setauthtype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauth/setauthtype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_reviewed: false
translation_revision: bdee7e8c1
order: 56820
---

OAuth::setAuthType

Define el tipo de autorización

## Descripción

```php
public OAuth::setAuthType(int $auth_type): bool
```php

Configura los parámetros OAuth.

## Parámetros

`auth_type`  
`auth_type` puede ser una de las siguientes opciones (clasificadas por orden decreciente de preferencia, como se especifica en la sección 5.2 de OAuth 1.0) :

`OAUTH_AUTH_TYPE_AUTHORIZATION`  
Pasa los parámetros OAuth en el encabezado HTTP `Authorization`.

`OAUTH_AUTH_TYPE_FORM`  
Añade los parámetros OAuth al cuerpo de la petición HTTP POST.

`OAUTH_AUTH_TYPE_URI`  
Añade los parámetros OAuth a la URI.

`OAUTH_AUTH_TYPE_NONE`  
Ninguno.

## Valores devueltos

Devuelve `true` si un parámetro es definido correctamente, `false` en los demás casos.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL oauth 1.0.0 | Antes de esta versión, `null` era devuelto en lugar de `false`. |
