---
title: Uri\Rfc3986\Uri::getRawPassword
description: Recupera la contraseña sin procesar
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.getrawpassword.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/getrawpassword.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99590
---

Uri\Rfc3986\Uri::getRawPassword

Recupera la contraseña sin procesar

## Descripción

```php
public Uri\Rfc3986\Uri::getRawPassword(): string
```php

Recupera la parte de contraseña sin procesar (no normalizada) (el texto después del primer carácter `:`) del componente userinfo.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la contraseña sin procesar (no normalizada) como un `string` si el componente userinfo contiene un carácter `:`. Se devuelve una cadena vacía cuando el componente userinfo no contiene un carácter `:`. Se devuelve `null` cuando el componente userinfo no existe.

## Ejemplos

Ejemplo básico de Uri\Rfc3986\Uri::getRawPassword

```
<?php
$uri = new \Uri\Rfc3986\Uri("https://user:password@example.com");

echo $uri->getRawPassword();
?>

   
```php

El ejemplo anterior mostrará:

    password

## Véase también

Uri\Rfc3986\Uri::getPassword

Uri\Rfc3986\Uri::withUserInfo

Uri\WhatWg\Url::getPassword
