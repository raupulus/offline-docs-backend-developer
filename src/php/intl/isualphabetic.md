---
title: IntlChar::isUAlphabetic
description: Verifica si un punto de código tiene la propiedad Unicode Alphabetic
source_url: https://www.php.net/manual/es/intlchar.isualphabetic.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/isualphabetic.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 41160
---

IntlChar::isUAlphabetic

Verifica si un punto de código tiene la propiedad Unicode Alphabetic

## Descripción

```php
public static IntlChar::isUAlphabetic(int $codepoint): bool
```php

Verifica si un punto de código tiene la propiedad Unicode Alphabetic.

Esto es idéntico a `IntlChar::hasBinaryProperty($codepoint, IntlChar::PROPERTY_ALPHABETIC)`

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve `true` si `codepoint` tiene la propiedad Unicode Alphabetic, `false` en caso contrario. Devuelve `null` en caso de fallo.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::isUAlphabetic("A"));
var_dump(IntlChar::isUAlphabetic("1"));
var_dump(IntlChar::isUAlphabetic("\u{2603}"));
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(true)
    bool(false)
    bool(false)

## Véase también

`IntlChar::isalpha`, `IntlChar::hasBinaryProperty`, `IntlChar::PROPERTY_ALPHABETIC`
