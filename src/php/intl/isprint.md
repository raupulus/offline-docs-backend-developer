---
title: IntlChar::isprint
description: Verifica si un punto de código es un carácter imprimible
source_url: https://www.php.net/manual/es/intlchar.isprint.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/isprint.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: e20e74073
order: 41120
---

IntlChar::isprint

Verifica si un punto de código es un carácter imprimible

## Descripción

```php
public static IntlChar::isprint(int $codepoint): bool
```php

Determina si el punto de código especificado es un carácter imprimible.

`true` para las categorías generales distintas de "C" (controles).

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve `true` si `codepoint` es un carácter imprimible, `false` en caso contrario. Devuelve `null` en caso de fallo.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::isprint("A"));
var_dump(IntlChar::isprint(" "));
var_dump(IntlChar::isprint("\n"));
var_dump(IntlChar::isprint("\u{200e}"));
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(true)
    bool(true)
    bool(false)
    bool(false)

## Véase también

`IntlChar::iscntrl`, `IntlChar::PROPERTY_DEFAULT_IGNORABLE_CODE_POINT`, `ctype_print`
