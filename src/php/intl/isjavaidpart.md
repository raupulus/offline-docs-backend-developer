---
title: IntlChar::isJavaIDPart
description: Verifica si un punto de código es permitido en un identificador Java
source_url: https://www.php.net/manual/es/intlchar.isjavaidpart.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/isjavaidpart.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 41070
---

IntlChar::isJavaIDPart

Verifica si un punto de código es permitido en un identificador Java

## Descripción

```php
public static IntlChar::isJavaIDPart(int $codepoint): bool
```php

Determina si el carácter especificado es permitido en un identificador Java.

Además de `IntlChar::isIDPart`, `true` para los caracteres de categoría general "Sc" (símbolos de moneda).

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve `true` si `codepoint` puede aparecer en un identificador Java, `false` de lo contrario. Devuelve `null` en caso de fallo.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::isJavaIDPart("A"));
var_dump(IntlChar::isJavaIDPart("$"));
var_dump(IntlChar::isJavaIDPart("\n"));
var_dump(IntlChar::isJavaIDPart("\u{2603}"));
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(true)
    bool(true)
    bool(false)
    bool(false)

## Véase también

`IntlChar::isIDIgnorable`, `IntlChar::isIDPart`, `IntlChar::isJavaIDStart`, `IntlChar::isalpha`, `IntlChar::isdigit`
