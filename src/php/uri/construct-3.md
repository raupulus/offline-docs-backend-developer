---
title: Uri\WhatWg\Url::__construct
description: Construye el objeto Url
source_url: https://www.php.net/manual/es/uri-whatwg-url.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/whatwg/url/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 39596f122
order: 99820
---

Uri\WhatWg\Url::\_\_construct

Construye el objeto Url

## Descripción

```php
public Uri\WhatWg\Url::__construct(string $uri, [Uri\WhatWg\Url $baseUrl], [array $softErrors])
```php

Construye el objeto `Uri\Rfc3986\Uri`.

## Parámetros

`uri`  
Una cadena de URL válida a analizar (por ejemplo, `/foo` o `https://example.com/foo`).

`baseUrl`  
Cuando se pasa un `string`, `uri` se aplica sobre `baseUrl`, si `uri` es una cadena de URL relativa. Si se pasa `null`, o `uri` no es una cadena de URL relativa, `baseUrl` no tiene ningún efecto.

`softErrors`  
Un `array` para pasar por referencia una lista de instancias de `Uri\WhatWg\UrlValidationError` que proporciona información extendida sobre los errores generados durante el análisis.

## Errores/Excepciones

Si la URL resultante es inválida, se lanza una excepción Uri\WhatWg\InvalidUrlException.

## Véase también

Uri\WhatWg\Url::parse

Uri\WhatWg\Url::resolve

Uri\Rfc3986\Uri::\_\_construct
