---
title: FFI::free
description: Libera una estructura de datos no gestionada
source_url: https://www.php.net/manual/es/ffi.free.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ffi/ffi/free.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ffi
translation_status: ready
translation_reviewed: false
translation_revision: e14fdcab8
order: 22940
---

FFI::free

Libera una estructura de datos no gestionada

## Descripción

```php
public static FFI::free(FFI\CData $ptr): void
```php

Libera manualmente una estructura de datos no gestionada creada previamente.

## Parámetros

`ptr`  
El gestor del puntero no gestionado de una estructura de datos C.

## Valores devueltos

No se retorna ningún valor.
