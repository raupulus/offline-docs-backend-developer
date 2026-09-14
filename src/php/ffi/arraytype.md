---
title: FFI::arrayType
description: Construye dinámicamente un nuevo tipo de array C
source_url: https://www.php.net/manual/es/ffi.arraytype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ffi/ffi/arraytype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ffi
translation_status: ready
translation_reviewed: false
translation_revision: e14fdcab8
order: 22910
---

FFI::arrayType

Construye dinámicamente un nuevo tipo de array C

## Descripción

```php
public static FFI::arrayType(FFI\CType $type, array $dimensions): FFI\CType
```php

Construye dinámicamente un nuevo tipo de array C con elementos de tipo definido por `type`, y dimensiones especificadas por `dimensions`. En el siguiente ejemplo, `$t1` y `$t2` son tipos de array equivalentes:

```
<?php
$t1 = FFI::type("int[2][3]");
$t2 = FFI::arrayType(FFI::type("int"), [2, 3]);
?>

    
```php

## Parámetros

`type`  
Una declaración C válida como `string`, o una instancia de `FFI\CType` que ya ha sido creada.

`dimensions`  
Las dimensiones del tipo como `array`.

## Valores devueltos

Devuelve el objeto `FFI\CType` recién creado.
