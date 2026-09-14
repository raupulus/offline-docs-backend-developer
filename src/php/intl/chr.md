---
title: IntlChar::chr
description: Devuelve el carácter Unicode por valor de punto de código
source_url: https://www.php.net/manual/es/intlchar.chr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/chr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: feab22a67
order: 40750
---

IntlChar::chr

Devuelve el carácter Unicode por valor de punto de código

## Descripción

```php
public static IntlChar::chr(int $codepoint): string
```php

Devuelve una cadena que contiene el carácter especificado por el valor de punto de código Unicode.

Este método complementa `IntlChar::ord`.

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Una cadena que contiene el carácter único especificado por el valor de punto de código Unicode, o `null` en caso de error.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
$values = ["A", 63, 123, 9731];
foreach ($values as $value) {
    var_dump(IntlChar::chr($value));
}
?>

   
```php

El ejemplo anterior mostrará:

        
    string(1) "A"
    string(1) "?"
    string(1) "{"
    string(3) "☃"

## Véase también

`IntlChar::ord`, `mb_chr`, `chr`
