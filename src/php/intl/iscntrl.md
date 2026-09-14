---
title: IntlChar::iscntrl
description: Verifica si un punto de código es un carácter de control
source_url: https://www.php.net/manual/es/intlchar.iscntrl.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/iscntrl.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: e20e74073
order: 40990
---

IntlChar::iscntrl

Verifica si un punto de código es un carácter de control

## Descripción

```php
public static IntlChar::iscntrl(int $codepoint): bool
```php

Determina si el punto de código especificado es un carácter de control.

Un carácter de control es uno de los siguientes: Carácter de control ISO de 8 bits (U+0000..U+001f y U+007f..U+009f), `IntlChar::CHAR_CATEGORY_CONTROL_CHAR` (Cc), `IntlChar::CHAR_CATEGORY_FORMAT_CHAR` (Cf), `IntlChar::CHAR_CATEGORY_LINE_SEPARATOR` (Zl), `IntlChar::CHAR_CATEGORY_PARAGRAPH_SEPARATOR` (Zp)

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve `true` si `codepoint` es un carácter de control, `false` en caso contrario. Devuelve `null` en caso de error.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::iscntrl("A"));
var_dump(IntlChar::iscntrl(" "));
var_dump(IntlChar::iscntrl("\n"));
var_dump(IntlChar::iscntrl("\u{200e}"));
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(false)
    bool(false)
    bool(true)
    bool(true)

## Véase también

`IntlChar::isprint`, `IntlChar::PROPERTY_DEFAULT_IGNORABLE_CODE_POINT`, `ctype_cntrl`
