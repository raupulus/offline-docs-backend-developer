---
title: IntlChar::charDigitValue
description: Devuelve el valor decimal del dígito decimal
source_url: https://www.php.net/manual/es/intlchar.chardigitvalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/chardigitvalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40690
---

IntlChar::charDigitValue

Devuelve el valor decimal del dígito decimal

## Descripción

```php
public static IntlChar::charDigitValue(int $codepoint): int
```php

Devuelve el valor decimal del carácter dígito decimal.

Tales caracteres tienen la categoría general "Nd" (dígitos decimales) y un Numeric_Type de Decimal.

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

El valor decimal del carácter dígito decimal, o `-1` si no es un carácter decimal. Devuelve `null` en caso de fallo.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::charDigitValue("1"));
var_dump(IntlChar::charDigitValue("\u{0662}"));
var_dump(IntlChar::charDigitValue("\u{0E53}"));
?>

   
```php

El ejemplo anterior mostrará:

        
    int(1)
    int(2)
    int(3)

## Véase también

`IntlChar::getNumericValue`
