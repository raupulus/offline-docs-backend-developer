---
title: Uri\Rfc3986\Uri::equals
description: Verifica si dos URIs son equivalentes
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.equals.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/equals.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99500
---

Uri\Rfc3986\Uri::equals

Verifica si dos URIs son equivalentes

## Descripción

```php
public Uri\Rfc3986\Uri::equals(Uri\Rfc3986\Uri $uri, [Uri\UriComparisonMode $comparisonMode]): bool
```php

Verifica si dos URIs son equivalentes.

## Parámetros

`uri`  
URI con la que comparar la URI actual.

`comparisonMode`  
Indica si el componente de fragmento se tiene en cuenta en la comparación (`Uri\UriComparisonMode::IncludeFragment`) o no (`Uri\UriComparisonMode::ExcludeFragment`). Por defecto, el fragmento se excluye.

## Valores devueltos

Devuelve `true` si las dos URIs son equivalentes, o `false` en caso contrario.

## Ejemplos

Ejemplo básico de Uri\Rfc3986\Uri::equals

```
<?php
$uri1 = new \Uri\Rfc3986\Uri("https://example.com");
$uri2 = new \Uri\Rfc3986\Uri("HTTPS://example.com");

var_dump($uri1->equals($uri2));
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)

## Véase también

Uri\WhatWg\Url::equals
