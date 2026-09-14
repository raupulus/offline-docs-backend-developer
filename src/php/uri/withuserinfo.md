---
title: Uri\Rfc3986\Uri::withUserInfo
description: Modifica el componente de información de usuario
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.withuserinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/withuserinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99800
---

Uri\Rfc3986\Uri::withUserInfo

Modifica el componente de información de usuario

## Descripción

```php
public #[\SensitiveParameter] Uri\Rfc3986\Uri::withUserInfo(string $userinfo): static
```php

Crea una nueva URI y modifica su componente de información de usuario.

## Parámetros

`userinfo`  
Nuevo componente de información de usuario.

## Valores devueltos

La instancia modificada de `Uri\Rfc3986\Uri`.

## Errores/Excepciones

Si la URI resultante es inválida, se lanza una excepción Uri\InvalidUriException.

## Ejemplos

Ejemplo básico de Uri\Rfc3986\Uri::withUserInfo

```
<?php
$uri = new \Uri\Rfc3986\Uri("https://user:password@example.com");
$uri = $uri->withUserInfo("userinfo");

echo $uri->getUserInfo();
?>

   
```php

El ejemplo anterior mostrará:

    userinfo

## Véase también

Uri\Rfc3986\Uri::getRawUserInfo

Uri\Rfc3986\Uri::getUserInfo

Uri\Rfc3986\Uri::getRawUsername

Uri\Rfc3986\Uri::getUsername

Uri\Rfc3986\Uri::getRawPassword

Uri\Rfc3986\Uri::getPassword

Uri\WhatWg\Url::withUsername

Uri\WhatWg\Url::withPassword
