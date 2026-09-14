---
title: IntlChar::isxdigit
description: Verifica si un punto de código es un dígito hexadecimal
source_url: https://www.php.net/manual/es/intlchar.isxdigit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/isxdigit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: e20e74073
order: 41220
---

IntlChar::isxdigit

Verifica si un punto de código es un dígito hexadecimal

## Descripción

```php
public static IntlChar::isxdigit(int $codepoint): bool
```php

Determina si el punto de código especificado es un dígito hexadecimal.

`true` para los caracteres de categoría general "Nd" (dígitos decimales) así como las letras latinas a-f y A-F en ASCII y ASCII completo. (Es decir, para las letras con puntos de código 0041..0046, 0061..0066, FF21..FF26, FF41..FF46.)

Esto es equivalente a `IntlChar::digit($codepoint, 16) >= 0`.

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve `true` si `codepoint` es un dígito hexadecimal, `false` en caso contrario. Devuelve `null` en caso de error.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::isxdigit("A"));
var_dump(IntlChar::isxdigit("1"));
var_dump(IntlChar::isxdigit("\u{2603}"));
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(true)
    bool(true)
    bool(false)

## Notas

> [!NOTE]
> Para restringir la definición de dígitos hexadecimales únicamente a los caracteres ASCII, utilice:
>
> ```
>     
> <?php
> $isASCIIHexadecimal = IntlChar::ord($codepoint) <= 0x7F && IntlChar::isxdigit($codepoint);
> ?>
>
>    
> ```

## Véase también

`IntlChar::isdigit`, `ctype_xdigit`
