---
title: FFI::cdef
description: Crea un nuevo objeto FFI
source_url: https://www.php.net/manual/es/ffi.cdef.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ffi/ffi/cdef.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ffi
translation_status: ready
translation_reviewed: false
translation_revision: e14fdcab8
order: 22930
---

FFI::cdef

Crea un nuevo objeto FFI

## Descripción

```php
public static FFI::cdef([string $code], [string $lib]): FFI
```php

Crea un nuevo objeto FFI.

## Parámetros

`code`  
Un string que contiene una secuencia de declaraciones en lenguaje C ordinario (tipos, estructuras, funciones, variables, etc). De hecho, este string puede ser copiado y pegado desde ficheros de encabezado C.

> [!NOTE]
> Las directivas del preprocesador C no son soportadas, es decir, `#include`, `#define` y las macros CPP no funcionan.

`lib`  
El nombre de un fichero de biblioteca compartida, para cargar y enlazar con las definiciones.

> [!NOTE]
> Si `lib` es omitido o `null`, las plataformas que soportan `RTLD_DEFAULT` intentan buscar los símbolos declarados en `code` en el ámbito global. Los otros sistemas no lograrán resolver estos símbolos.

## Valores devueltos

Devuelve el objeto `FFI` recién creado.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Las funciones C que devuelven `void` devuelven un `null` PHP en lugar de `FFI\CType::TYPE_VOID`. |
| 8.0.0 | `lib` es ahora nullable. |
