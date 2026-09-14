---
title: Uri\Rfc3986\Uri::__construct
description: Construye el objeto Uri
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99480
---

Uri\Rfc3986\Uri::\_\_construct

Construye el objeto Uri

## Descripción

```php
public Uri\Rfc3986\Uri::__construct(string $uri, [Uri\Rfc3986\Uri $baseUrl])
```php

Construye el objeto `Uri\Rfc3986\Uri`.

## Parámetros

`uri`  
URI a analizar.

`baseUrl`  
Cuando se pasa un `string`, `uri` se aplica sobre `baseUrl`, si `uri` es una referencia relativa. Si se pasa `null`, o `uri` no es una referencia relativa, `baseUrl` no tiene ningún efecto.

## Errores/Excepciones

Si la URI resultante es inválida, se lanza una excepción Uri\InvalidUriException.

## Véase también

Uri\Rfc3986\Uri::parse

Uri\Rfc3986\Uri::resolve

Uri\WhatWg\Url::\_\_construct
