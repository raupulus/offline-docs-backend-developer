---
title: IntlChar::isISOControl
description: Verifica si un punto de código es un carácter de control ISO
source_url: https://www.php.net/manual/es/intlchar.isisocontrol.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/isisocontrol.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 41060
---

IntlChar::isISOControl

Verifica si un punto de código es un carácter de control ISO

## Descripción

```php
public static IntlChar::isISOControl(int $codepoint): bool
```php

Determina si el punto de código especificado es un código de control ISO.

`true` para U+0000..U+001f y U+007f..U+009f (categoría general "Cc").

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve `true` si `codepoint` es un código de control ISO, `false` en caso contrario. Devuelve `null` en caso de fallo.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::isISOControl(" "));
var_dump(IntlChar::isISOControl("\n"));
var_dump(IntlChar::isISOControl("\u{200e}"));
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(false)
    bool(true)
    bool(false)

## Véase también

`IntlChar::iscntrl`
