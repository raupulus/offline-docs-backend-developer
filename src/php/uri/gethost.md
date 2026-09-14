---
title: Uri\Rfc3986\Uri::getHost
description: Recupera el componente de host normalizado
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.gethost.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/gethost.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99520
---

Uri\Rfc3986\Uri::getHost

Recupera el componente de host normalizado

## Descripción

```php
public Uri\Rfc3986\Uri::getHost(): string
```php

Recupera el componente de host normalizado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el componente de host normalizado como un `string` si el componente de host existe; de lo contrario, se devuelve `null`.

## Ejemplos

Ejemplo básico de Uri\Rfc3986\Uri::getHost

```
<?php
$uri = new \Uri\Rfc3986\Uri("https://example.com");

echo $uri->getHost();
?>

   
```php

El ejemplo anterior mostrará:

    example.com

## Véase también

Uri\Rfc3986\Uri::getRawHost

Uri\Rfc3986\Uri::withHost

Uri\WhatWg\Url::getAsciiHost

Uri\WhatWg\Url::getUnicodeHost
