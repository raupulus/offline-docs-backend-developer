---
title: Uri\Rfc3986\Uri::getRawFragment
description: Recupera el componente de fragmento sin procesar
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.getrawfragment.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/getrawfragment.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: c5ff5efb9
order: 99570
---

Uri\Rfc3986\Uri::getRawFragment

Recupera el componente de fragmento sin procesar

## Descripción

```php
public Uri\Rfc3986\Uri::getRawFragment(): string
```php

Recupera el componente de fragmento sin procesar (no normalizado).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el componente de fragmento sin procesar como un `string` si el componente de fragmento existe; de lo contrario, se devuelve `null`.

## Ejemplos

Ejemplo básico de Uri\Rfc3986\Uri::getRawFragment

```
<?php
$uri = new \Uri\Rfc3986\Uri("https://example.com#foo=bar");

echo $uri->getRawFragment();
?>

   
```php

El ejemplo anterior mostrará:

    foo=bar

## Véase también

Uri\Rfc3986\Uri::getFragment

Uri\Rfc3986\Uri::withFragment

Uri\WhatWg\Url::getFragment
