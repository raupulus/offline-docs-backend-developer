---
title: Uri\Rfc3986\Uri::getScheme
description: Recupera el componente de esquema normalizado
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.getscheme.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/getscheme.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99650
---

Uri\Rfc3986\Uri::getScheme

Recupera el componente de esquema normalizado

## Descripción

```php
public Uri\Rfc3986\Uri::getScheme(): string
```php

Recupera el componente de esquema normalizado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el componente de esquema normalizado como un `string` si el componente de esquema existe; de lo contrario, se devuelve `null`.

## Ejemplos

Ejemplo básico de Uri\Rfc3986\Uri::getScheme

```
<?php
$uri = new \Uri\Rfc3986\Uri("https://example.com");

echo $uri->getScheme();
?>

   
```php

El ejemplo anterior mostrará:

    https

## Véase también

Uri\Rfc3986\Uri::getRawScheme

Uri\Rfc3986\Uri::withScheme

Uri\WhatWg\Url::getScheme
