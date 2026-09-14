---
title: Uri\WhatWg\Url::toUnicodeString
description: Recompone la URL como un string Unicode
source_url: https://www.php.net/manual/es/uri-whatwg-url.tounicodestring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/whatwg/url/tounicodestring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99980
---

Uri\WhatWg\Url::toUnicodeString

Recompone la URL como un

string

Unicode

## Descripción

```php
public Uri\WhatWg\Url::toUnicodeString(): string
```php

Recompone la URL como un `string`, donde el componente del host puede contener caracteres Unicode.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la URL recompuesta como un `string` Unicode.

## Ejemplos

Ejemplo básico de Uri\WhatWg\Url::toUnicodeString

```
<?php
$url = new \Uri\WhatWg\Url("https://example.com/foo/bar?baz");

echo $url->toUnicodeString();
?>

   
```php

El ejemplo anterior mostrará:

    https://example.com/foo/bar?baz

## Véase también

Uri\WhatWg\Url::toAsciiString

Uri\Rfc3986\Uri::toRawString

Uri\Rfc3986\Uri::toString
