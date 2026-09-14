---
title: IntlChar::isblank
description: Verifica si un punto de código es un carácter "blanco" o "espacio horizontal"
source_url: https://www.php.net/manual/es/intlchar.isblank.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/isblank.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40980
---

IntlChar::isblank

Verifica si un punto de código es un carácter "blanco" o "espacio horizontal"

## Descripción

```php
public static IntlChar::isblank(int $codepoint): bool
```php

Determina si el punto de código especificado es un carácter "blanco" o "espacio horizontal", un carácter que separa visualmente las palabras en una línea.

Las definiciones siguientes son equivalentes: `true` para los caracteres Unicode White_Space con excepción de los "controles de espacio vertical" donde los "controles de espacio vertical" son los caracteres siguientes: U+000A (LF) U+000B (VT) U+000C (FF) U+000D (CR) U+0085 (NEL) U+2028 (LS) U+2029 (PS), `true` para U+0009 (TAB) y los caracteres de categoría general "Zs" (separadores de espacio) con excepción del espacio de ancho cero (ZWSP, U+200B).

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve `true` si `codepoint` es un carácter "blanco" o "espacio horizontal", `false` en caso contrario. Devuelve `null` en caso de error.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::isblank("A"));
var_dump(IntlChar::isblank(" "));
var_dump(IntlChar::isblank("\t"));
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(false)
    bool(true)
    bool(true)

## Véase también

`IntlChar::isspace`, `IntlChar::isJavaSpaceChar`, `IntlChar::isUWhiteSpace`, `IntlChar::isWhitespace`
