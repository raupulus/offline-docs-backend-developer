---
title: ctype_xdigit
description: Chequear posibles caracteres que representen un dígito hexadecimal
source_url: https://www.php.net/manual/es/function.ctype-xdigit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ctype/functions/ctype-xdigit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ctype
translation_status: ready
translation_reviewed: false
translation_revision: e20e74073
order: 8550
---

ctype_xdigit

Chequear posibles caracteres que representen un dígito hexadecimal

## Descripción

```php
ctype_xdigit(mixed $text): bool
```php

Verifica si todos los caracteres de la `string` entregada, `text`, son 'dígitos' hexadecimales.

## Parámetros

`text`  
La cadena de prueba.

> [!NOTE]
> Si se proporciona un `int` entre -128 y 255 inclusive, este se interpreta como el valor ASCII de un solo carácter (a los valores negativos se les añade 256 para permitir caracteres del rango ASCII extendido). Cualquier otro entero se interpreta como un string que contiene los dígitos decimales del entero.

> [!WARNING]
> A partir de PHP 8.1.0, pasar un argumento que no sea string está obsoleto. En el futuro, el argumento se interpretará como un string en lugar de un punto de código ASCII. Según el comportamiento deseado, el argumento debería convertirse a `string` o se debería realizar una llamada explícita a `chr`.

## Valores devueltos

Devuelve `true` si cada caracter del `text` es un 'dígito' hexadecimal, lo que quiere decir un dígito decimal o un caracter del rango `[A-Fa-f]`; `false` de lo contrario. Cuando se llama con una cadena vacía, el resultado será siempre `false`.

## Ejemplos

Un ejemplo de `ctype_xdigit`

```
<?php
$cadenas = array('AB10BC99', 'AR1012', 'ab12bc99');
foreach ($cadenas as $caso_prueba) {
    if (ctype_xdigit($caso_prueba)) {
        echo "La cadena $caso_prueba consiste completamente de dígitos hexadecimales.\n";
    } else {
        echo "La cadena $caso_prueba no consiste completamente de dígitos hexadecimales.\n";
    }
}
?>

    
```php

El ejemplo anterior mostrará:

    La cadena AB10BC99 consiste completamente de dígitos hexadecimales.
    La cadena AR1012 no consiste completamente de dígitos hexadecimales.
    La cadena ab12bc99 consiste completamente de dígitos hexadecimales.

## Véase también

`ctype_digit`, `IntlChar::isxdigit`
