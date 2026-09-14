---
title: FFI::memcpy
description: Copia de una zona de memoria en otra
source_url: https://www.php.net/manual/es/ffi.memcpy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ffi/ffi/memcpy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ffi
translation_status: ready
translation_reviewed: false
translation_revision: e14fdcab8
order: 22980
---

FFI::memcpy

Copia de una zona de memoria en otra

## Descripción

```php
public static FFI::memcpy(FFI\CData $to, FFI\CData $from, int $size): void
```php

Copia `size` bytes de la zona de memoria `from` hacia la zona de memoria `to`.

## Parámetros

`to`  
Inicio de la zona de memoria a copiar.

`from`  
El inicio de la zona de memoria donde la copia debe ser efectuada.

`size`  
El número de bytes a copiar.

## Valores devueltos

No se retorna ningún valor.
