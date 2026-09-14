---
title: IntlChar::isalnum
description: Verifica si un punto de código es un carácter alfanumérico
source_url: https://www.php.net/manual/es/intlchar.isalnum.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/isalnum.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: e20e74073
order: 40950
---

IntlChar::isalnum

Verifica si un punto de código es un carácter alfanumérico

## Descripción

```php
public static IntlChar::isalnum(int $codepoint): bool
```php

Determina si el punto de código especificado es un carácter alfanumérico (letra o dígito). `true` para los caracteres con las categorías generales "L" (letras) y "Nd" (dígitos decimales).

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve `true` si `codepoint` es un carácter alfanumérico, `false` en caso contrario. Devuelve `null` en caso de error.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::isalnum("A"));
var_dump(IntlChar::isalnum("1"));
var_dump(IntlChar::isalnum("\u{2603}"));
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(true)
    bool(true)
    bool(false)

## Véase también

`IntlChar::isalpha`, `IntlChar::isdigit`, `ctype_alnum`
