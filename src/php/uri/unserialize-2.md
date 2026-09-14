---
title: Uri\WhatWg\Url::__unserialize
description: Deserializa el parámetro data en un objeto Url
source_url: https://www.php.net/manual/es/uri-whatwg-url.unserialize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/whatwg/url/unserialize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99990
---

Uri\WhatWg\Url::\_\_unserialize

Deserializa el parámetro data en un objeto Url

## Descripción

```php
public Uri\WhatWg\Url::__unserialize(array $data): void
```php

Deserializa un parámetro data en un objeto `Uri\WhatWg\Url`.

## Parámetros

`data`  
Los datos serializados como un `array`.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Si el método \_\_unserialize se invoca sobre una URL ya existente, se lanza una excepción Error.

Si la URI resultante es inválida, se lanza una excepción Uri\InvalidUriException.

## Véase también

Uri\WhatWg\Url::\_\_serialize

Uri\Rfc3986\Uri::\_\_unserialize
