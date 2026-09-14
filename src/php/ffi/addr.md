---
title: FFI::addr
description: Crea un puntero no gestionado hacia datos C
source_url: https://www.php.net/manual/es/ffi.addr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ffi/ffi/addr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ffi
translation_status: ready
translation_reviewed: false
translation_revision: e14fdcab8
order: 22890
---

FFI::addr

Crea un puntero no gestionado hacia datos C

## Descripción

```php
public static FFI::addr(FFI\CData $ptr): FFI\CData
```php

Crea un puntero no gestionado hacia los datos C representados por el elemento `FFI\CData`. La fuente `ptr` debe sobrevivir al puntero resultante. Esta función es principalmente útil para transmitir argumentos a funciones C a través de un puntero.

## Parámetros

`ptr`  
El gestor del puntero hacia una estructura de datos C.

## Valores devueltos

Devuelve el objeto `FFI\CData` recién creado.
