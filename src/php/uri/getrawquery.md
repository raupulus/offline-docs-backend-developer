---
title: Uri\Rfc3986\Uri::getRawQuery
description: Recupera el componente de consulta sin procesar
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.getrawquery.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/getrawquery.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99610
---

Uri\Rfc3986\Uri::getRawQuery

Recupera el componente de consulta sin procesar

## Descripción

```php
public Uri\Rfc3986\Uri::getRawQuery(): string
```php

Recupera el componente de consulta sin procesar (no normalizado).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el componente de consulta sin procesar como un `string` si el componente de consulta existe; de lo contrario, se devuelve `null`.

## Ejemplos

Ejemplo básico de Uri\Rfc3986\Uri::getRawQuery

```
<?php
$uri = new \Uri\Rfc3986\Uri("https://example.com?foo=bar");

echo $uri->getRawQuery();
?>

   
```php

El ejemplo anterior mostrará:

    foo=bar

## Véase también

Uri\Rfc3986\Uri::getQuery

Uri\Rfc3986\Uri::withQuery

Uri\WhatWg\Url::getQuery
