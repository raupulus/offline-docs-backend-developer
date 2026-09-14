---
title: FFI::memset
description: Rellena una zona de memoria
source_url: https://www.php.net/manual/es/ffi.memset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ffi/ffi/memset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ffi
translation_status: ready
translation_reviewed: false
translation_revision: e14fdcab8
order: 22990
---

FFI::memset

Rellena una zona de memoria

## Descripción

```php
public static FFI::memset(FFI\CData $ptr, int $value, int $size): void
```php

Rellena `size` bytes de la zona de memoria apuntada por `ptr` con el byte dado `value`.

## Parámetros

`ptr`  
Inicio de la zona de memoria a rellenar.

`value`  
El byte a rellenar.

`size`  
El número de bytes a rellenar.

## Valores devueltos

No se retorna ningún valor.
