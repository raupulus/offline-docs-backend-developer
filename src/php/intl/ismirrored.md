---
title: IntlChar::isMirrored
description: Verifica si un punto de código tiene la propiedad Bidi_Mirrored
source_url: https://www.php.net/manual/es/intlchar.ismirrored.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/ismirrored.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 41110
---

IntlChar::isMirrored

Verifica si un punto de código tiene la propiedad Bidi_Mirrored

## Descripción

```php
public static IntlChar::isMirrored(int $codepoint): bool
```php

Determina si el punto de código tiene la propiedad Bidi_Mirrored.

Esta propiedad está definida para los caracteres que se utilizan comúnmente en contextos de derecha a izquierda y que deben mostrarse con un glifo "espejo".

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve `true` si `codepoint` tiene la propiedad Bidi_Mirrored, `false` en caso contrario. Devuelve `null` en caso de error.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::isMirrored("A"));
var_dump(IntlChar::isMirrored("<"));
var_dump(IntlChar::isMirrored("("));
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(false)
    bool(true)
    bool(true)

## Véase también

`IntlChar::charMirror`, `IntlChar::PROPERTY_BIDI_MIRRORED`
