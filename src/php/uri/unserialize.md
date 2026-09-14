---
title: Uri\Rfc3986\Uri::__unserialize
description: Deserializa el parámetro data en un objeto Uri
source_url: https://www.php.net/manual/es/uri-rfc3986-uri.unserialize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/rfc3986/uri/unserialize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99730
---

Uri\Rfc3986\Uri::\_\_unserialize

Deserializa el parámetro data en un objeto Uri

## Descripción

```php
public Uri\Rfc3986\Uri::__unserialize(array $data): void
```php

Deserializa un parámetro data en un objeto `Uri\Rfc3986\Uri`.

## Parámetros

`data`  
Los datos serializados como un `array`.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Si el método \_\_unserialize se llama sobre una URI ya existente, se lanza un Error.

Si la URI resultante es inválida, se lanza una excepción Uri\InvalidUriException.

## Véase también

Uri\Rfc3986\Uri::\_\_serialize

Uri\WhatWg\Url::\_\_unserialize
