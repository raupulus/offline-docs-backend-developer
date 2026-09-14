---
title: Uri\Rfc3986\Uri::getFragment
description: Recupera el componente de fragmento normalizado
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.getfragment.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/getfragment.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99510
---

Uri\Rfc3986\Uri::getFragment

Recupera el componente de fragmento normalizado

## Descripción

```php
public Uri\Rfc3986\Uri::getFragment(): string
```php

Recupera el componente de fragmento normalizado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el componente de fragmento normalizado como un `string` si el componente de fragmento existe; de lo contrario, se devuelve `null`.

## Ejemplos

Ejemplo básico de Uri\Rfc3986\Uri::getFragment

```
<?php
$uri = new \Uri\Rfc3986\Uri("https://example.com#foo=bar");

echo $uri->getFragment();
?>

   
```php

El ejemplo anterior mostrará:

    foo=bar

## Véase también

Uri\Rfc3986\Uri::getRawFragment

Uri\Rfc3986\Uri::withFragment

Uri\WhatWg\Url::getFragment
