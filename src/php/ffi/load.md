---
title: FFI::load
description: Carga las declaraciones C desde un archivo de encabezado C
source_url: https://www.php.net/manual/es/ffi.load.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ffi/ffi/load.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ffi
translation_status: ready
translation_reviewed: false
translation_revision: e14fdcab8
order: 22960
---

FFI::load

Carga las declaraciones C desde un archivo de encabezado C

## Descripción

```php
public static FFI::load(string $filename): FFI
```php

Carga las declaraciones C desde un archivo de encabezado C. Es posible especificar las bibliotecas compartidas que deben ser cargadas, utilizando definiciones especiales `FFI_LIB` en el archivo de encabezado C cargado.

## Parámetros

`filename`  
El nombre de un archivo de encabezado C.

Las directivas del preprocesador C no son soportadas, es decir, `#include`, `#define` y las macros CPP no funcionan, excepto en los casos particulares enumerados a continuación.

El archivo de encabezado *debería* contener una declaración `#define` para la variable `FFI_SCOPE`, por ejemplo: `#define FFI_SCOPE "MYLIB"`. Consulte la [introducción de la clase](#ffi.intro) para más detalles.

El archivo de encabezado *puede* contener una declaración `#define` para la variable `FFI_LIB` para especificar la biblioteca que expone. Si se trata de una biblioteca del sistema, solo se requiere el nombre del archivo, por ejemplo: `#define FFI_LIB "libc.so.6"`. Si se trata de una biblioteca personalizada, se requiere una ruta relativa, por ejemplo: `#define FFI_LIB "./mylib.so"`.

## Valores devueltos

Devuelve el objeto `FFI` recién creado, o `null` en caso de fallo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | FFI::load ahora está permitido en los [scripts de precarga](#opcache.preloading) cuando el usuario del sistema actual es el mismo que el definido en la directiva de configuración `opcache.preload_user`. |

## Véase también

FFI::scope
