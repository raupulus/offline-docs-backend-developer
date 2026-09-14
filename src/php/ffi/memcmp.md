---
title: FFI::memcmp
description: Comparación de zonas de memoria
source_url: https://www.php.net/manual/es/ffi.memcmp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ffi/ffi/memcmp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ffi
translation_status: ready
translation_reviewed: false
translation_revision: e14fdcab8
order: 22970
---

FFI::memcmp

Comparación de zonas de memoria

## Descripción

```php
public static FFI::memcmp(string $ptr1, string $ptr2, int $size): int
```php

Compara los `size` bytes de las zonas de memoria `ptr1` y `ptr2`. `ptr1` y `ptr2` pueden ser estructuras de datos nativas (`FFI\CData`) o `string`s PHP.

## Parámetros

`ptr1`  
Inicio de una zona de memoria.

`ptr2`  
El inicio de otra zona de memoria.

`size`  
El número de bytes a comparar.

## Valores devueltos

Devuelve un valor inferior a `0` si el contenido de la zona de memoria que comienza en `ptr1` se considera menor que el contenido de la zona de memoria que comienza en `ptr2`, un valor superior a `0` si el contenido de la primera zona de memoria se considera mayor que el de la segunda, y `0` si son iguales.
