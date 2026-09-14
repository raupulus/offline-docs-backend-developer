---
title: Uri\Rfc3986\Uri::getUsername
description: Recupera el nombre de usuario normalizado
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.getusername.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/getusername.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99670
---

Uri\Rfc3986\Uri::getUsername

Recupera el nombre de usuario normalizado

## Descripción

```php
public Uri\Rfc3986\Uri::getUsername(): string
```php

Recupera la parte del nombre de usuario normalizado (el texto antes del primer carácter `:`) del componente userinfo.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el nombre de usuario normalizado como un `string` si el componente userinfo existe; de lo contrario, se devuelve `null`.

## Ejemplos

Ejemplo básico de Uri\Rfc3986\Uri::getUsername

```
<?php
$uri = new \Uri\Rfc3986\Uri("https://user:password@example.com");

echo $uri->getUsername();
?>

   
```php

El ejemplo anterior mostrará:

    user

## Véase también

Uri\Rfc3986\Uri::getRawUsername

Uri\Rfc3986\Uri::getRawUserInfo

Uri\Rfc3986\Uri::getUserInfo

Uri\Rfc3986\Uri::withUserInfo

Uri\WhatWg\Url::getUsername
