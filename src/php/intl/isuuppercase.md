---
title: IntlChar::isUUppercase
description: Verifica si un punto de código tiene la propiedad Unicode Uppercase
source_url: https://www.php.net/manual/es/intlchar.isuuppercase.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/isuuppercase.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 41190
---

IntlChar::isUUppercase

Verifica si un punto de código tiene la propiedad Unicode Uppercase

## Descripción

```php
public static IntlChar::isUUppercase(int $codepoint): bool
```php

Verifica si un punto de código tiene la propiedad Unicode Uppercase.

Esto es idéntico a `IntlChar::hasBinaryProperty($codepoint, IntlChar::PROPERTY_UPPERCASE)`

> [!NOTE]
> Esto es diferente de `IntlChar::isupper` y devolverá `true` para más caracteres.

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve `true` si `codepoint` tiene la propiedad Unicode Uppercase, `false` en caso contrario. Devuelve `null` en caso de error.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::isUUppercase("A"));
var_dump(IntlChar::isUUppercase("a"));
var_dump(IntlChar::isUUppercase("Φ"));
var_dump(IntlChar::isUUppercase("φ"));
var_dump(IntlChar::isUUppercase("1"));
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(true)
    bool(false)
    bool(true)
    bool(false)
    bool(false)

## Véase también

`IntlChar::isupper`, `IntlChar::hasBinaryProperty`, `IntlChar::PROPERTY_UPPERCASE`
