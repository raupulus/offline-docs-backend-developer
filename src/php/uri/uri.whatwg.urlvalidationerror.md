---
title: La clase Uri\WhatWg\UrlValidationError
source_url: https://www.php.net/manual/es/class.uri-whatwg-urlvalidationerror.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri.whatwg.urlvalidationerror.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: b6e9565ba
order: 100160
---

## Introducción

Proporciona detalles sobre los errores detectados al analizar una URL con `Uri\WhatWg\Url`.

## Sinopsis de la clase

Uri\WhatWg

final

readonly

UrlValidationError

Propiedades

public

string

context

public

Uri\WhatWg\UrlValidationErrorType

type

public

bool

failure

Métodos

## Propiedades

`context`  
La URL de entrada en el punto donde se detectó el error.

`type`  
El tipo de error.

`failure`  
Si es `true`, el error provocó que la URL fuera rechazada como inválida. Si es `false`, el error es un error leve que fue corregido automáticamente durante el análisis.
