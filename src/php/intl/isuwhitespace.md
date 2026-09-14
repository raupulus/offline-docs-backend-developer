---
title: IntlChar::isUWhiteSpace
description: Verifica si un punto de código tiene la propiedad Unicode White_Space
source_url: https://www.php.net/manual/es/intlchar.isuwhitespace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/isuwhitespace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 41200
---

IntlChar::isUWhiteSpace

Verifica si un punto de código tiene la propiedad Unicode White_Space

## Descripción

```php
public static IntlChar::isUWhiteSpace(int $codepoint): bool
```php

Verifica si un punto de código tiene la propiedad Unicode White_Space.

Esto es idéntico a `IntlChar::hasBinaryProperty($codepoint, IntlChar::PROPERTY_WHITE_SPACE)`

> [!NOTE]
> Esto es diferente de `IntlChar::isspace` y de `IntlChar::isWhitespace`.

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve `true` si `codepoint` tiene la propiedad Unicode White_Space, `false` en caso contrario. Devuelve `null` en caso de error.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::isUWhiteSpace("A"));
var_dump(IntlChar::isUWhiteSpace(" "));
var_dump(IntlChar::isUWhiteSpace("\n"));
var_dump(IntlChar::isUWhiteSpace("\t"));
var_dump(IntlChar::isUWhiteSpace("\u{00A0}"));
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(false)
    bool(true)
    bool(true)
    bool(true)
    bool(true)

## Véase también

`IntlChar::isspace`, `IntlChar::isWhitespace`, `IntlChar::isJavaSpaceChar`, `IntlChar::hasBinaryProperty`, `IntlChar::PROPERTY_WHITE_SPACE`
