---
title: IntlChar::isJavaSpaceChar
description: Verifica si un punto de código es un carácter de espacio según Java
source_url: https://www.php.net/manual/es/intlchar.isjavaspacechar.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/isjavaspacechar.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 41090
---

IntlChar::isJavaSpaceChar

Verifica si un punto de código es un carácter de espacio según Java

## Descripción

```php
public static IntlChar::isJavaSpaceChar(int $codepoint): bool
```php

Determina si el punto de código especificado es un carácter de espacio según Java.

`true` para los caracteres de categoría general "Z" (separadores), lo que no incluye los códigos de control (por ejemplo, TAB o Line Feed).

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve `true` si `codepoint` es un carácter de espacio según Java, `false` en caso contrario. Devuelve `null` en caso de error.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::isJavaSpaceChar("A"));
var_dump(IntlChar::isJavaSpaceChar(" "));
var_dump(IntlChar::isJavaSpaceChar("\n"));
var_dump(IntlChar::isJavaSpaceChar("\t"));
var_dump(IntlChar::isJavaSpaceChar("\u{00A0}"));
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(false)
    bool(true)
    bool(false)
    bool(false)
    bool(true)

## Véase también

`IntlChar::isspace`, `IntlChar::isWhitespace`, `IntlChar::isUWhiteSpace`
