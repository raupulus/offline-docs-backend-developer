---
title: Uri\Rfc3986\Uri::resolve
description: Resuelve una URI con el objeto actual como URL base
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.resolve.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/resolve.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99690
---

Uri\Rfc3986\Uri::resolve

Resuelve una URI con el objeto actual como URL base

## Descripción

```php
public Uri\Rfc3986\Uri::resolve(string $uri): static
```php

Resuelve una URI - que puede ser potencialmente una referencia relativa - con el objeto actual como URL base.

## Parámetros

`uri`  
Una URI a aplicar sobre el objeto actual.

## Valores devueltos

Una nueva instancia de `Uri\Rfc3986\Uri`.

## Errores/Excepciones

Si la URI resultante es inválida, se lanza una excepción Uri\InvalidUriException.

## Ejemplos

Ejemplo básico de Uri\Rfc3986\Uri::resolve

```
<?php
$uri = new \Uri\Rfc3986\Uri("https://example.com");
$uri = $uri->resolve("/foo");

echo $uri->toRawString();
?>

   
```php

El ejemplo anterior mostrará:

    https://example.com/foo

## Véase también

Uri\Rfc3986\Uri::\_\_construct

Uri\Rfc3986\Uri::parse

Uri\WhatWg\Url::resolve
