---
title: Uri\WhatWg\Url::toAsciiString
description: Recompone la URL como un string ASCII
source_url: https://www.php.net/manual/es/uri-whatwg-url.toasciistring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/whatwg/url/toasciistring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99970
---

Uri\WhatWg\Url::toAsciiString

Recompone la URL como un

string

ASCII

## Descripción

```php
public Uri\WhatWg\Url::toAsciiString(): string
```php

Recompone la URL como un `string` ASCII, utilizando la transcripción punycode en lugar de caracteres Unicode en el componente del host.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la URL recompuesta como un `string` ASCII.

## Ejemplos

Ejemplo básico de Uri\WhatWg\Url::toAsciiString

```
<?php
$url = new \Uri\WhatWg\Url("https://example.com/foo/bar?baz");

echo $url->toAsciiString();
?>

   
```php

El ejemplo anterior mostrará:

    https://example.com/foo/bar?baz

## Véase también

Uri\WhatWg\Url::toUnicodeString

Uri\Rfc3986\Uri::toRawString

Uri\Rfc3986\Uri::toString
