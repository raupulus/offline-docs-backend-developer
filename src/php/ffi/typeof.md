---
title: FFI::typeof
description: Recupera el FFI\CType de FFI\CData
source_url: https://www.php.net/manual/es/ffi.typeof.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ffi/ffi/typeof.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ffi
translation_status: ready
translation_reviewed: false
translation_revision: e14fdcab8
order: 23050
---

FFI::typeof

Recupera el FFI\CType de FFI\CData

## Descripción

```php
public static FFI::typeof(FFI\CData $ptr): FFI\CType
```php

Recupera el objeto `FFI\CType` que representa el tipo del objeto `FFI\CData` dado.

## Parámetros

`ptr`  
El gestor del puntero hacia una estructura de datos C.

## Valores devueltos

Devuelve el objeto `FFI\CType` que representa el tipo del objeto `FFI\CData` dado.
