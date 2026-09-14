---
title: IntlChar::charType
description: Devuelve el valor de la categoría general para un punto de código
source_url: https://www.php.net/manual/es/intlchar.chartype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/chartype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40740
---

IntlChar::charType

Devuelve el valor de la categoría general para un punto de código

## Descripción

```php
public static IntlChar::charType(int $codepoint): int
```php

Devuelve la categoría general para el punto de código.

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve la categoría general, que puede ser una de las constantes siguientes: `IntlChar::CHAR_CATEGORY_UNASSIGNED`, `IntlChar::CHAR_CATEGORY_GENERAL_OTHER_TYPES`, `IntlChar::CHAR_CATEGORY_UPPERCASE_LETTER`, `IntlChar::CHAR_CATEGORY_LOWERCASE_LETTER`, `IntlChar::CHAR_CATEGORY_TITLECASE_LETTER`, `IntlChar::CHAR_CATEGORY_MODIFIER_LETTER`, `IntlChar::CHAR_CATEGORY_OTHER_LETTER`, `IntlChar::CHAR_CATEGORY_NON_SPACING_MARK`, `IntlChar::CHAR_CATEGORY_ENCLOSING_MARK`, `IntlChar::CHAR_CATEGORY_COMBINING_SPACING_MARK`, `IntlChar::CHAR_CATEGORY_DECIMAL_DIGIT_NUMBER`, `IntlChar::CHAR_CATEGORY_LETTER_NUMBER`, `IntlChar::CHAR_CATEGORY_OTHER_NUMBER`, `IntlChar::CHAR_CATEGORY_SPACE_SEPARATOR`, `IntlChar::CHAR_CATEGORY_LINE_SEPARATOR`, `IntlChar::CHAR_CATEGORY_PARAGRAPH_SEPARATOR`, `IntlChar::CHAR_CATEGORY_CONTROL_CHAR`, `IntlChar::CHAR_CATEGORY_FORMAT_CHAR`, `IntlChar::CHAR_CATEGORY_PRIVATE_USE_CHAR`, `IntlChar::CHAR_CATEGORY_SURROGATE`, `IntlChar::CHAR_CATEGORY_DASH_PUNCTUATION`, `IntlChar::CHAR_CATEGORY_START_PUNCTUATION`, `IntlChar::CHAR_CATEGORY_END_PUNCTUATION`, `IntlChar::CHAR_CATEGORY_CONNECTOR_PUNCTUATION`, `IntlChar::CHAR_CATEGORY_OTHER_PUNCTUATION`, `IntlChar::CHAR_CATEGORY_MATH_SYMBOL`, `IntlChar::CHAR_CATEGORY_CURRENCY_SYMBOL`, `IntlChar::CHAR_CATEGORY_MODIFIER_SYMBOL`, `IntlChar::CHAR_CATEGORY_OTHER_SYMBOL`, `IntlChar::CHAR_CATEGORY_INITIAL_PUNCTUATION`, `IntlChar::CHAR_CATEGORY_FINAL_PUNCTUATION`, `IntlChar::CHAR_CATEGORY_CHAR_CATEGORY_COUNT`

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::charType("A") === IntlChar::CHAR_CATEGORY_UPPERCASE_LETTER);
var_dump(IntlChar::charType(".") === IntlChar::CHAR_CATEGORY_OTHER_PUNCTUATION);
var_dump(IntlChar::charType("\t") === IntlChar::CHAR_CATEGORY_CONTROL_CHAR);
var_dump(IntlChar::charType("\u{2603}") === IntlChar::CHAR_CATEGORY_OTHER_SYMBOL);
var_dump(IntlChar::charType("multiple chars") === null);
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(true)
    bool(true)
    bool(true)
    bool(true)
    bool(true)
