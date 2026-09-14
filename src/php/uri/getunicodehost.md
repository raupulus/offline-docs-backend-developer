---
title: Uri\WhatWg\Url::getUnicodeHost
description: Recupera el componente de host como una cadena Unicode
source_url: https://www.php.net/manual/es/uri-whatwg-url.getunicodehost.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/whatwg/url/getunicodehost.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99920
---

Uri\WhatWg\Url::getUnicodeHost

Recupera el componente de host como una cadena Unicode

## Descripción

```php
public Uri\WhatWg\Url::getUnicodeHost(): string
```php

Recupera el componente de host como un `string`, que puede contener caracteres Unicode.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el componente de host como un `string` Unicode si el componente de host existe, en caso contrario se devuelve `null`.

## Ejemplos

Ejemplo básico de Uri\WhatWg\Url::getUnicodeHost

```
<?php
$url = new \Uri\WhatWg\Url("https://example.com");

echo $url->getUnicodeHost();
?>

   
```php

El ejemplo anterior mostrará:

    example.com

## Véase también

Uri\WhatWg\Url::getAsciiHost

Uri\WhatWg\Url::withHost

Uri\Rfc3986\Uri::getRawHost

Uri\Rfc3986\Uri::getHost
