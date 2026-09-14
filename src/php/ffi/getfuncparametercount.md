---
title: FFI\CType::getFuncParameterCount
description: Recuperar el número de argumentos de un tipo de función
source_url: https://www.php.net/manual/es/ffi-ctype.getfuncparametercount.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ffi/ctype/getfuncparametercount.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ffi
translation_status: ready
translation_reviewed: false
translation_revision: e14fdcab8
order: 22780
---

FFI\CType::getFuncParameterCount

Recuperar el número de argumentos de un tipo de función

## Descripción

```php
public FFI\CType::getFuncParameterCount(): int
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de argumentos del tipo de función subyacente. Si el tipo subyacente no es una función, se lanza una FFI\Exception.
