---
title: Uri\Rfc3986\Uri::toString
description: Recompone la URI normalizada
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.tostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/tostring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99720
---

Uri\Rfc3986\Uri::toString

Recompone la URI normalizada

## Descripción

```php
public Uri\Rfc3986\Uri::toString(): string
```php

Recompone la URI normalizada en un `string`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la URI recompuesta normalizada como un `string`.

## Ejemplos

Ejemplo básico de Uri\Rfc3986\Uri::toString

```
<?php
$uri = new \Uri\Rfc3986\Uri("https://example.com/foo/bar?baz");

echo $uri->toString();
?>

   
```php

El ejemplo anterior mostrará:

    https://example.com/foo/bar?baz

## Véase también

Uri\Rfc3986\Uri::toRawString

Uri\WhatWg\Url::toAsciiString

Uri\WhatWg\Url::toUnicodeString
