---
title: Uri\Rfc3986\Uri::getRawUserInfo
description: Recupera el componente userinfo sin procesar
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.getrawuserinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/getrawuserinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99630
---

Uri\Rfc3986\Uri::getRawUserInfo

Recupera el componente userinfo sin procesar

## Descripción

```php
public Uri\Rfc3986\Uri::getRawUserInfo(): string
```php

Recupera el componente userinfo sin procesar (no normalizado).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el componente userinfo sin procesar como un `string` si el componente userinfo existe; de lo contrario, se devuelve `null`.

## Ejemplos

Ejemplo básico de Uri\Rfc3986\Uri::getRawUserInfo

```
<?php
$uri = new \Uri\Rfc3986\Uri("https://user:password@example.com");

echo $uri->getRawUserInfo();
?>

   
```php

El ejemplo anterior mostrará:

    user:password

## Véase también

Uri\Rfc3986\Uri::getUserInfo

Uri\Rfc3986\Uri::getUsername

Uri\Rfc3986\Uri::getPassword

Uri\Rfc3986\Uri::withUserInfo

Uri\WhatWg\Url::getUsername

Uri\WhatWg\Url::getPassword
