---
title: FFI\CType::getFuncParameterType
description: Recuperar el tipo de un parámetro de función
source_url: https://www.php.net/manual/es/ffi-ctype.getfuncparametertype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ffi/ctype/getfuncparametertype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ffi
translation_status: ready
translation_reviewed: false
translation_revision: e14fdcab8
order: 22790
---

FFI\CType::getFuncParameterType

Recuperar el tipo de un parámetro de función

## Descripción

```php
public FFI\CType::getFuncParameterType(int $index): FFI\CType
```php

Devuelve el tipo de un parámetro para el tipo de función subyacente.

## Parámetros

`index`  
Índice del parámetro de la función, basado en cero.

## Valores devueltos

Devuelve el tipo de un parámetro para el tipo de función subyacente. Si el tipo subyacente no es una función, o si el índice proporcionado está fuera del rango de los parámetros de la función, se lanza una FFI\Exception.
