---
title: IntlChar::charDirection
description: Devuelve el valor de la categoría bidireccional para un punto de código
source_url: https://www.php.net/manual/es/intlchar.chardirection.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/chardirection.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: e8ac70bf5
order: 40700
---

IntlChar::charDirection

Devuelve el valor de la categoría bidireccional para un punto de código

## Descripción

```php
public static IntlChar::charDirection(int $codepoint): int
```php

Devuelve el valor de la categoría bidireccional para un punto de código, que se utiliza en el [algoritmo bidireccional Unicode (UAX \#9)](http://www.unicode.org/reports/tr9/).

> [!NOTE]
> Algunos puntos de código no asignados tienen valores bidireccionales de R o AL ya que se encuentran en bloques reservados para scripts de derecha a izquierda.

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

El valor de la categoría bidireccional; una de las constantes siguientes: `IntlChar::CHAR_DIRECTION_LEFT_TO_RIGHT`, `IntlChar::CHAR_DIRECTION_RIGHT_TO_LEFT`, `IntlChar::CHAR_DIRECTION_EUROPEAN_NUMBER`, `IntlChar::CHAR_DIRECTION_EUROPEAN_NUMBER_SEPARATOR`, `IntlChar::CHAR_DIRECTION_EUROPEAN_NUMBER_TERMINATOR`, `IntlChar::CHAR_DIRECTION_ARABIC_NUMBER`, `IntlChar::CHAR_DIRECTION_COMMON_NUMBER_SEPARATOR`, `IntlChar::CHAR_DIRECTION_BLOCK_SEPARATOR`, `IntlChar::CHAR_DIRECTION_SEGMENT_SEPARATOR`, `IntlChar::CHAR_DIRECTION_WHITE_SPACE_NEUTRAL`, `IntlChar::CHAR_DIRECTION_OTHER_NEUTRAL`, `IntlChar::CHAR_DIRECTION_LEFT_TO_RIGHT_EMBEDDING`, `IntlChar::CHAR_DIRECTION_LEFT_TO_RIGHT_OVERRIDE`, `IntlChar::CHAR_DIRECTION_RIGHT_TO_LEFT_ARABIC`, `IntlChar::CHAR_DIRECTION_RIGHT_TO_LEFT_EMBEDDING`, `IntlChar::CHAR_DIRECTION_RIGHT_TO_LEFT_OVERRIDE`, `IntlChar::CHAR_DIRECTION_POP_DIRECTIONAL_FORMAT`, `IntlChar::CHAR_DIRECTION_DIR_NON_SPACING_MARK`, `IntlChar::CHAR_DIRECTION_BOUNDARY_NEUTRAL`, `IntlChar::CHAR_DIRECTION_FIRST_STRONG_ISOLATE`, `IntlChar::CHAR_DIRECTION_LEFT_TO_RIGHT_ISOLATE`, `IntlChar::CHAR_DIRECTION_RIGHT_TO_LEFT_ISOLATE`, `IntlChar::CHAR_DIRECTION_POP_DIRECTIONAL_ISOLATE`, `IntlChar::CHAR_DIRECTION_CHAR_DIRECTION_COUNT` Devuelve `null` en caso de error.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::charDirection("A") === IntlChar::CHAR_DIRECTION_LEFT_TO_RIGHT);
var_dump(IntlChar::charDirection("\u{05E9}") === IntlChar::CHAR_DIRECTION_RIGHT_TO_LEFT);
var_dump(IntlChar::charDirection("+") === IntlChar::CHAR_DIRECTION_EUROPEAN_NUMBER_SEPARATOR);
var_dump(IntlChar::charDirection(".") === IntlChar::CHAR_DIRECTION_COMMON_NUMBER_SEPARATOR);
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(true)
    bool(true)
    bool(true)
    bool(true)
