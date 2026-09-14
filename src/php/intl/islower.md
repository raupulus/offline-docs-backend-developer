---
title: IntlChar::islower
description: Verifica si un punto de código es una letra minúscula
source_url: https://www.php.net/manual/es/intlchar.islower.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/islower.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: e20e74073
order: 41100
---

IntlChar::islower

Verifica si un punto de código es una letra minúscula

## Descripción

```php
public static IntlChar::islower(int $codepoint): bool
```php

Determina si el punto de código especificado tiene la categoría general "Ll" (letra minúscula).

> [!NOTE]
> Esto no incluye algunos caracteres que también son minúsculas pero tienen un valor de categoría general diferente. Para incluirlos, utilice `IntlChar::isULowercase`.

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve `true` si `codepoint` es una letra minúscula, `false` en caso contrario. Devuelve `null` en caso de error.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::islower("A"));
var_dump(IntlChar::islower("a"));
var_dump(IntlChar::islower("Φ"));
var_dump(IntlChar::islower("φ"));
var_dump(IntlChar::islower("1"));
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(false)
    bool(true)
    bool(false)
    bool(true)
    bool(false)

## Véase también

`IntlChar::isupper`, `IntlChar::istitle`, `IntlChar::tolower`, `IntlChar::toupper`, `IntlChar::PROPERTY_LOWERCASE`, `ctype_lower`
