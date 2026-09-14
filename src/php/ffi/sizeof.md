---
title: FFI::sizeof
description: Recupera el tamaño de los datos o tipos C
source_url: https://www.php.net/manual/es/ffi.sizeof.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ffi/ffi/sizeof.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ffi
translation_status: ready
translation_reviewed: false
translation_revision: e14fdcab8
order: 23020
---

FFI::sizeof

Recupera el tamaño de los datos o tipos C

## Descripción

```php
public static FFI::sizeof(FFI\CData $ptr): int
```php

Devuelve el tamaño del objeto `FFI\CData` o `FFI\CType` objeto.

## Parámetros

`ptr`  
El gestor de la data o del tipo C.

## Valores devueltos

Tamaño de la zona de memoria apuntada por `ptr`.
