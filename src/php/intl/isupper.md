---
title: IntlChar::isupper
description: Verifica si un punto de código tiene la categoría general "Lu" (letra
  mayúscula)
source_url: https://www.php.net/manual/es/intlchar.isupper.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/isupper.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: e20e74073
order: 41180
---

IntlChar::isupper

Verifica si un punto de código tiene la categoría general "Lu" (letra mayúscula)

## Descripción

```php
public static IntlChar::isupper(int $codepoint): bool
```php

Determina si el punto de código especificado tiene la categoría general "Lu" (letra mayúscula).

> [!NOTE]
> Esto no incluye algunos caracteres que también son mayúsculas pero tienen un valor de categoría general diferente. Para incluirlos, utilice `IntlChar::isUUppercase`.

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve `true` si `codepoint` es una letra mayúscula, `false` en caso contrario. Devuelve `null` en caso de error.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::isupper("A"));
var_dump(IntlChar::isupper("a"));
var_dump(IntlChar::isupper("Φ"));
var_dump(IntlChar::isupper("φ"));
var_dump(IntlChar::isupper("1"));
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(true)
    bool(false)
    bool(true)
    bool(false)
    bool(false)

## Véase también

`IntlChar::islower`, `IntlChar::istitle`, `IntlChar::tolower`, `IntlChar::toupper`, `IntlChar::PROPERTY_UPPERCASE`, `ctype_upper`
