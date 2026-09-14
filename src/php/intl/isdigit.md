---
title: IntlChar::isdigit
description: Verifica si un punto de código es un dígito
source_url: https://www.php.net/manual/es/intlchar.isdigit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/isdigit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: e20e74073
order: 41010
---

IntlChar::isdigit

Verifica si un punto de código es un dígito

## Descripción

```php
public static IntlChar::isdigit(int $codepoint): bool
```php

Determina si el punto de código especificado es un dígito.

`true` para los caracteres de categoría general "Nd" (dígitos decimales). A partir de Unicode 4, esto es lo mismo que probar el Type_Numeric de Decimal.

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve `true` si `codepoint` es un dígito, `false` en caso contrario. Devuelve `null` en caso de error.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::isdigit("A"));
var_dump(IntlChar::isdigit("1"));
var_dump(IntlChar::isdigit("\t"));
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(false)
    bool(true)
    bool(false)

## Véase también

`IntlChar::isalpha`, `IntlChar::isalnum`, `IntlChar::isxdigit`, `ctype_digit`
