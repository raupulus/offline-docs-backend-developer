---
title: Uri\WhatWg\Url::resolve
description: Resuelve una URL con el objeto actual como URL base
source_url: https://www.php.net/manual/es/uri-whatwg-url.resolve.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/whatwg/url/resolve.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99950
---

Uri\WhatWg\Url::resolve

Resuelve una URL con el objeto actual como URL base

## Descripción

```php
public Uri\WhatWg\Url::resolve(string $uri, [array $softErrors]): static
```php

Resuelve una cadena de URL válida, que potencialmente puede ser una cadena de URL relativa, con el objeto actual como URL base.

## Parámetros

`uri`  
Una cadena de URL válida (p.ej. `/foo` o (p.ej. `https://example.com/foo`) a aplicar sobre el objeto actual.

`softErrors`  
Un `array` para pasar por referencia una lista de instancias de `Uri\WhatWg\UrlValidationError` que proporcionan información extendida sobre los errores leves generados durante la resolución de referencia.

## Valores devueltos

Una nueva instancia de `Uri\WhatWg\Url`.

## Errores/Excepciones

Si la URL resultante es inválida, se lanza una excepción Uri\WhatWg\InvalidUrlException.

## Ejemplos

Ejemplo básico de Uri\WhatWg\Url::resolve

```
<?php
$url = new \Uri\WhatWg\Url("https://example.com");
$url = $url->resolve("/foo");

echo $url->toAsciiString();
?>

   
```php

El ejemplo anterior mostrará:

    https://example.com/foo

## Véase también

Uri\WhatWg\Url::\_\_construct

Uri\WhatWg\Url::parse

Uri\Rfc3986\Uri::resolve
