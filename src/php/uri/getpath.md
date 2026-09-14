---
title: Uri\Rfc3986\Uri::getPath
description: Recupera el componente de ruta normalizado
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.getpath.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/getpath.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: c5ff5efb9
order: 99540
---

Uri\Rfc3986\Uri::getPath

Recupera el componente de ruta normalizado

## Descripción

```php
public Uri\Rfc3986\Uri::getPath(): string
```php

Recupera el componente de ruta normalizado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el componente de ruta normalizado como un `string`.

## Ejemplos

Ejemplo básico de Uri\Rfc3986\Uri::getPath

```
<?php
$uri = new \Uri\Rfc3986\Uri("https://example.com/foo/bar");

echo $uri->getPath();
?>

   
```php

El ejemplo anterior mostrará:

    /foo/bar

## Véase también

Uri\Rfc3986\Uri::getRawPath

Uri\Rfc3986\Uri::withPath

Uri\WhatWg\Url::getPath
