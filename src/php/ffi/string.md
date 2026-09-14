---
title: FFI::string
description: Crea una string PHP a partir de una zona de memoria
source_url: https://www.php.net/manual/es/ffi.string.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ffi/ffi/string.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ffi
translation_status: ready
translation_reviewed: false
translation_revision: e14fdcab8
order: 23030
---

FFI::string

Crea una string PHP a partir de una zona de memoria

## Descripción

```php
public static FFI::string(FFI\CData $ptr, [int $size]): string
```php

Crea una `string` PHP a partir de `size` bytes de la zona de memoria apuntada por `ptr`.

## Parámetros

`ptr`  
El inicio de la zona de memoria a partir de la cual crear una `string`.

`size`  
El número de bytes a copiar en `string`. Si `size` es omitido o `null`, `ptr` debe ser un array de caracteres C de `char` C con terminación nula.

## Valores devueltos

La `string` PHP recién creada.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `size` es ahora nullable; anteriormente, su valor por omisión era `0`. |
