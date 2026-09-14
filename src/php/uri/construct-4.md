---
title: Uri\WhatWg\UrlValidationError::__construct
description: Construye un objeto UrlValidationError
source_url: https://www.php.net/manual/es/uri-whatwg-urlvalidationerror.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri/whatwg/urlvalidationerror/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: ab4cf5ea8
order: 100080
---

Uri\WhatWg\UrlValidationError::\_\_construct

Construye un objeto UrlValidationError

## Descripción

```php
public Uri\WhatWg\UrlValidationError::__construct(string $context, Uri\WhatWg\UrlValidationErrorType $type, bool $failure)
```php

Construye un objeto `Uri\WhatWg\UrlValidationError`.

## Parámetros

`context`  
La URL de entrada en el punto donde se detectó el error.

`type`  
El tipo de error.

`failure`  
Si es `true`, el error ha causado que la URL sea rechazada como inválida. Si es `false`, el error es un error leve que fue corregido automáticamente durante el análisis.
