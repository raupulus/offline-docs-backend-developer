---
title: IntlChar::isIDStart
description: Verifica si un punto de código es permitido como primer carácter en un
  identificador
source_url: https://www.php.net/manual/es/intlchar.isidstart.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/isidstart.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 41050
---

IntlChar::isIDStart

Verifica si un punto de código es permitido como primer carácter en un identificador

## Descripción

```php
public static IntlChar::isIDStart(int $codepoint): bool
```php

Determina si el carácter especificado es permitido como primer carácter en un identificador según Unicode (The Unicode Standard, Version 3.0, capítulo 5.16 Identificadores).

`true` para los caracteres de categoría general "L" (letras) y "Nl" (números letras).

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve `true` si `codepoint` puede comenzar un identificador, `false` en caso contrario. Devuelve `null` en caso de fallo.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::isIDStart("A"));
var_dump(IntlChar::isIDStart("$"));
var_dump(IntlChar::isIDStart("\n"));
var_dump(IntlChar::isIDStart("\u{2603}"));
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(true)
    bool(false)
    bool(false)
    bool(false)

## Véase también

`IntlChar::isalpha`, `IntlChar::isIDPart`, `IntlChar::PROPERTY_ID_START`
