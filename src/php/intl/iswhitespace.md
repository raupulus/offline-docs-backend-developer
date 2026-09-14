---
title: IntlChar::isWhitespace
description: Verifica si un punto de código es un carácter de espacio según ICU
source_url: https://www.php.net/manual/es/intlchar.iswhitespace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/iswhitespace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 41210
---

IntlChar::isWhitespace

Verifica si un punto de código es un carácter de espacio según ICU

## Descripción

```php
public static IntlChar::isWhitespace(int $codepoint): bool
```php

Determina si el punto de código especificado es un carácter de espacio según ICU.

Un carácter se considera un carácter de espacio ICU si y solo si cumple uno de los siguientes criterios: Si es un carácter de espacio Unicode (categorías "Z" = "Zs" o "Zl" o "Zp"), pero no es un espacio insustituible (U+00A0 NBSP o U+2007 Figure Space o U+202F Narrow NBSP)., Si es U+0009 HORIZONTAL TABULATION., Si es U+000A LINE FEED., Si es U+000B VERTICAL TABULATION., Si es U+000C FORM FEED., Si es U+000D CARRIAGE RETURN., Si es U+001C FILE SEPARATOR., Si es U+001D GROUP SEPARATOR., Si es U+001E RECORD SEPARATOR., Si es U+001F UNIT SEPARATOR.

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve `true` si `codepoint` es un carácter de espacio según ICU, `false` en caso contrario. Devuelve `null` en caso de fallo.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::iswhitespace("A"));
var_dump(IntlChar::iswhitespace(" "));
var_dump(IntlChar::iswhitespace("\n"));
var_dump(IntlChar::iswhitespace("\t"));
var_dump(IntlChar::iswhitespace("\u{00A0}"));
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(false)
    bool(true)
    bool(true)
    bool(true)
    bool(false)

## Véase también

`IntlChar::isspace`, `IntlChar::isJavaSpaceChar`, `IntlChar::isUWhiteSpace`
