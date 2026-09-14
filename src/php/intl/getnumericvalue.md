---
title: IntlChar::getNumericValue
description: Devuelve el valor numérico de un punto de código Unicode
source_url: https://www.php.net/manual/es/intlchar.getnumericvalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/getnumericvalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40880
---

IntlChar::getNumericValue

Devuelve el valor numérico de un punto de código Unicode

## Descripción

```php
public static IntlChar::getNumericValue(int $codepoint): float
```php

Devuelve el valor numérico de un punto de código Unicode tal como se define en la base de datos de caracteres Unicode.

Para los caracteres sin valor numérico en la base de datos de caracteres Unicode, esta función devolverá `IntlChar::NO_NUMERIC_VALUE`.

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

El valor numérico del `codepoint`, o `IntlChar::NO_NUMERIC_VALUE` si no está definido. Esta constante fue añadida en PHP 7.0.6, antes de esta versión el valor literal (`float`)`-123456789` puede ser utilizado en su lugar. Devuelve `null` en caso de error.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::getNumericValue("4"));
var_dump(IntlChar::getNumericValue("x"));
var_dump(IntlChar::getNumericValue("\u{216C}"));
?>

   
```php

El ejemplo anterior mostrará:

        
    float(4)
    float(-123456789)
    float(50)
