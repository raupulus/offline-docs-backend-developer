---
title: Uri\Rfc3986\Uri::toRawString
description: Recompone la URI sin procesar
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.torawstring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/torawstring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99710
---

Uri\Rfc3986\Uri::toRawString

Recompone la URI sin procesar

## Descripción

```php
public Uri\Rfc3986\Uri::toRawString(): string
```php

Recompone la URI sin procesar (no normalizada) en un `string`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la URI recompuesta sin procesar (no normalizada) como un `string`.

## Ejemplos

Ejemplo básico de Uri\Rfc3986\Uri::toRawString

```
<?php
$uri = new \Uri\Rfc3986\Uri("https://example.com/foo/bar?baz");

echo $uri->toRawString();
?>

   
```php

El ejemplo anterior mostrará:

    https://example.com/foo/bar?baz

## Véase también

Uri\Rfc3986\Uri::toString

Uri\WhatWg\Url::toAsciiString

Uri\WhatWg\Url::toUnicodeString
