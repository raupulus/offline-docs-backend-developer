---
title: IntlChar::getBlockCode
description: Devuelve el bloque de asignación Unicode que contiene un punto de código
source_url: https://www.php.net/manual/es/intlchar.getblockcode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/getblockcode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40820
---

IntlChar::getBlockCode

Devuelve el bloque de asignación Unicode que contiene un punto de código

## Descripción

```php
public static IntlChar::getBlockCode(int $codepoint): int
```php

Devuelve el bloque de asignación Unicode que contiene el carácter.

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve el valor del bloque para `codepoint`. Consulte las constantes `IntlChar::BLOCK_CODE_*` para los valores de retorno posibles. Devuelve `null` en caso de error.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::getBlockCode("A") === IntlChar::BLOCK_CODE_BASIC_LATIN);
var_dump(IntlChar::getBlockCode("Φ") === IntlChar::BLOCK_CODE_GREEK);
var_dump(IntlChar::getBlockCode("\u{2603}") === IntlChar::BLOCK_CODE_MISCELLANEOUS_SYMBOLS);
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(true)
    bool(true)
    bool(true)
