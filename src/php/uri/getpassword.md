---
title: Uri\Rfc3986\Uri::getPassword
description: Recupera la contraseña normalizada
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.getpassword.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/getpassword.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: c5ff5efb9
order: 99530
---

Uri\Rfc3986\Uri::getPassword

Recupera la contraseña normalizada

## Descripción

```php
public Uri\Rfc3986\Uri::getPassword(): string
```php

Recupera la parte de contraseña normalizada (el texto después del primer carácter `:`) del componente userinfo.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la contraseña normalizada como un `string` si el componente userinfo contiene un carácter `:`. Se devuelve una cadena vacía cuando el componente userinfo no contiene un carácter `:`. Se devuelve `null` cuando el componente userinfo no existe.

## Ejemplos

Ejemplo básico de Uri\Rfc3986\Uri::getPassword

```
<?php
$uri = new \Uri\Rfc3986\Uri("https://user:password@example.com");

echo $uri->getPassword();
?>

   
```php

El ejemplo anterior mostrará:

    password

## Véase también

Uri\Rfc3986\Uri::getRawPassword

Uri\Rfc3986\Uri::getRawUserInfo

Uri\Rfc3986\Uri::getUserInfo

Uri\Rfc3986\Uri::withPassword

Uri\WhatWg\Url::getPassword
