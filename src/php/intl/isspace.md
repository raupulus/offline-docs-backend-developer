---
title: IntlChar::isspace
description: Verifica si un punto de código es un carácter de espacio
source_url: https://www.php.net/manual/es/intlchar.isspace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/isspace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: e20e74073
order: 41140
---

IntlChar::isspace

Verifica si un punto de código es un carácter de espacio

## Descripción

```php
public static IntlChar::isspace(int $codepoint): bool
```php

Determina si el punto de código especificado es un carácter de espacio.

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve `true` si `codepoint` es un carácter de espacio, `false` en caso contrario. Devuelve `null` en caso de error.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::isspace("A"));
var_dump(IntlChar::isspace(" "));
var_dump(IntlChar::isspace("\n"));
var_dump(IntlChar::isspace("\t"));
var_dump(IntlChar::isspace("\u{00A0}"));
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(false)
    bool(true)
    bool(true)
    bool(true)
    bool(true)

## Véase también

`IntlChar::isJavaSpaceChar`, `IntlChar::isWhitespace`, `IntlChar::isUWhiteSpace`, `ctype_space`
