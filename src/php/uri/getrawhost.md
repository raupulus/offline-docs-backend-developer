---
title: Uri\Rfc3986\Uri::getRawHost
description: Recupera el componente de host sin procesar
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.getrawhost.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/getrawhost.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99580
---

Uri\Rfc3986\Uri::getRawHost

Recupera el componente de host sin procesar

## Descripción

```php
public Uri\Rfc3986\Uri::getRawHost(): string
```php

Recupera el componente de host sin procesar (no normalizado).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el componente de host sin procesar como un `string` si el componente de host existe; de lo contrario, se devuelve `null`.

## Ejemplos

Ejemplo básico de Uri\Rfc3986\Uri::getRawHost

```
<?php
$uri = new \Uri\Rfc3986\Uri("https://example.com");

echo $uri->getRawHost();
?>

   
```php

El ejemplo anterior mostrará:

    example.com

## Véase también

Uri\Rfc3986\Uri::getHost

Uri\Rfc3986\Uri::withHost

Uri\WhatWg\Url::getAsciiHost

Uri\WhatWg\Url::getUnicodeHost
