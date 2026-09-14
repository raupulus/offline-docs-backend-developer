---
title: IntlChar::ord
description: Devuelve el valor del punto de código Unicode de un carácter
source_url: https://www.php.net/manual/es/intlchar.ord.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/ord.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 41230
---

IntlChar::ord

Devuelve el valor del punto de código Unicode de un carácter

## Descripción

```php
public static IntlChar::ord(int $character): int
```php

Devuelve el valor del punto de código Unicode del carácter dado.

Esta función complementa `IntlChar::chr`.

## Parámetros

`character`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve el valor del punto de código Unicode en forma de entero.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::ord("A"));
var_dump(IntlChar::ord(" "));
var_dump(IntlChar::ord("\u{2603}"));
?>

   
```php

El ejemplo anterior mostrará:

        
    int(65)
    int(32)
    int(9731)

## Véase también

`IntlChar::chr`, `mb_ord`, `ord`
