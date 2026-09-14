---
title: Uri\WhatWg\Url::parse
description: Analiza una URL
source_url: https://www.php.net/manual/es/uri-whatwg-url.parse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/whatwg/url/parse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 8e2cfbdce
order: 99940
---

Uri\WhatWg\Url::parse

Analiza una URL

## Descripción

```php
public static Uri\WhatWg\Url::parse(string $uri, [Uri\WhatWg\Url $baseUrl], [array $errors]): static
```php

Analiza una URL.

## Parámetros

`uri`  
Una cadena de URL válida a analizar (p.ej. `/foo` o (p.ej. `https://example.com/foo`).

`baseUrl`  
Cuando se pasa un `string`, `uri` se aplica sobre `baseUrl`, si `uri` es una cadena de URL relativa. Si se pasa `null`, o `uri` no es una cadena de URL relativa, `baseUrl` no tiene ningún efecto.

`errors`  
Un `array` para pasar por referencia una lista de instancias de `Uri\WhatWg\UrlValidationError` que proporcionan información extendida sobre los errores generados durante el análisis.

## Valores devueltos

Devuelve una instancia de `Uri\WhatWg\Url` en caso de éxito, o `null` en caso de error.

## Ejemplos

Ejemplo básico de Uri\WhatWg\Url::parse

```
<?php
$url = \Uri\WhatWg\Url::parse("https://example.com");

if ($url !== null) {
    echo "Valid URL: " . $url->toAsciiString();
} else {
    echo "Invalid URL";
}
?>

   
```php

El ejemplo anterior mostrará:

    Valid URL: https://example.com

## Véase también

Uri\WhatWg\Url::\_\_construct

Uri\WhatWg\Url::resolve

Uri\Rfc3986\Uri::parse
