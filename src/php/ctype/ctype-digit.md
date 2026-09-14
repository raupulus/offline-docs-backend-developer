---
title: ctype_digit
description: Chequear posibles caracteres numéricos
source_url: https://www.php.net/manual/es/function.ctype-digit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ctype/functions/ctype-digit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ctype
translation_status: ready
translation_reviewed: false
translation_revision: e20e74073
order: 8480
---

ctype_digit

Chequear posibles caracteres numéricos

## Descripción

```php
ctype_digit(mixed $text): bool
```php

Verifica si todos los caracteres en la `string` entregada, `text`, son numéricos.

## Parámetros

`text`  
La cadena probada.

> [!NOTE]
> Si se proporciona un `int` entre -128 y 255 inclusive, este se interpreta como el valor ASCII de un solo carácter (a los valores negativos se les añade 256 para permitir caracteres del rango ASCII extendido). Cualquier otro entero se interpreta como un string que contiene los dígitos decimales del entero.

> [!WARNING]
> A partir de PHP 8.1.0, pasar un argumento que no sea string está obsoleto. En el futuro, el argumento se interpretará como un string en lugar de un punto de código ASCII. Según el comportamiento deseado, el argumento debería convertirse a `string` o se debería realizar una llamada explícita a `chr`.

## Valores devueltos

Devuelve `true` si cada caracter del `texto` es un dígito decimal, o `false` de lo contrario. Cuando se llama con una cadena vacía, el resultado será siempre `false`.

## Ejemplos

Un ejemplo de `ctype_digit`

```
<?php
$cadenas = array('1820.20', '10002', 'wsl!12');
foreach ($cadenas as $caso_prueba) {
    if (ctype_digit($caso_prueba)) {
        echo "La cadena $caso_prueba consiste completamente de dígitos.\n";
    } else {
        echo "La cadena $caso_prueba no consiste completamente de dígitos.\n";
    }
}
?>

    
```php

El ejemplo anterior mostrará:

    La cadena 1820.20 no consiste completamente de dígitos.
    La cadena 10002 consiste completamente de dígitos.
    La cadena wsl!12 no consiste completamente de dígitos.

Un ejemplo de `ctype_digit` comparando cadenas con enteros

```
<?php

$numeric_string = '42';
$integer        = 42;

ctype_digit($numeric_string);  // true
ctype_digit($integer);         // false (ASCII 42 es el caracter *)

is_numeric($numeric_string);   // true
is_numeric($integer);          // true
?>

    
```php

## Véase también

`ctype_alnum`, `ctype_xdigit`, `is_numeric`, `is_int`, `is_string`, `IntlChar::isdigit`
