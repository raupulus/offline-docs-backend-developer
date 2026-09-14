---
title: Uri\WhatWg\Url::getAsciiHost
description: Recupera el componente de host como un string ASCII
source_url: https://www.php.net/manual/es/uri-whatwg-url.getasciihost.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/whatwg/url/getasciihost.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99850
---

Uri\WhatWg\Url::getAsciiHost

Recupera el componente de host como un

string

ASCII

## Descripción

```php
public Uri\WhatWg\Url::getAsciiHost(): string
```php

Recupera el componente de host como un `string` utilizando la transcripción punycode en lugar de caracteres Unicode.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el componente de host como un `string` ASCII si el componente de host existe, en caso contrario se devuelve `null`.

## Ejemplos

Ejemplo básico de Uri\WhatWg\Url::getAsciiHost

```
<?php
$url = new \Uri\WhatWg\Url("https://example.com");

echo $url->getAsciiHost();
?>

   
```php

El ejemplo anterior mostrará:

    example.com

## Véase también

Uri\WhatWg\Url::getUnicodeHost

Uri\WhatWg\Url::withHost

Uri\Rfc3986\Uri::getRawHost

Uri\Rfc3986\Uri::getHost
