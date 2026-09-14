---
title: Uri\Rfc3986\Uri::parse
description: Analiza una URI
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.parse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/parse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 8e2cfbdce
order: 99680
---

Uri\Rfc3986\Uri::parse

Analiza una URI

## Descripción

```php
public static Uri\Rfc3986\Uri::parse(string $uri, [Uri\Rfc3986\Uri $baseUrl]): static
```php

Analiza una URI.

## Parámetros

`uri`  
URI a analizar.

`baseUrl`  
Cuando se pasa un `string`, `uri` se aplica sobre `baseUrl`, si `uri` es una referencia relativa. Si se pasa `null`, o `uri` no es una referencia relativa, `baseUrl` no tiene ningún efecto.

## Valores devueltos

Devuelve una instancia de `Uri\Rfc3986\Uri` en caso de éxito, o `null` en caso de error.

## Ejemplos

Ejemplo básico de Uri\Rfc3986\Uri::parse

```
<?php
$uri = \Uri\Rfc3986\Uri::parse("https://example.com");

if ($uri !== null) {
    echo "Valid URI: " . $uri->toString();
} else {
    echo "Invalid URI";
}
?>

   
```php

El ejemplo anterior mostrará:

    Valid URI: https://example.com

## Véase también

Uri\Rfc3986\Uri::\_\_construct

Uri\Rfc3986\Uri::resolve

Uri\WhatWg\Url::parse
