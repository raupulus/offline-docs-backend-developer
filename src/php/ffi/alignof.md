---
title: FFI::alignof
description: Recupera el alineamiento
source_url: https://www.php.net/manual/es/ffi.alignof.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ffi/ffi/alignof.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ffi
translation_status: ready
translation_reviewed: false
translation_revision: e14fdcab8
order: 22900
---

FFI::alignof

Recupera el alineamiento

## Descripción

```php
public static FFI::alignof(FFI\CData $ptr): int
```php

Recupera el alineamiento del objeto `FFI\CData` o `FFI\CType` dado.

## Parámetros

`ptr`  
El identificador de la data o del tipo C.

## Valores devueltos

Devuelve el alineamiento del objeto `FFI\CData` o `FFI\CType` dado.
