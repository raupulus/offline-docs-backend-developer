---
title: is_numeric
description: Determina si una variable es un número o una cadena numérica
source_url: https://www.php.net/manual/es/function.is-numeric.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/is-numeric.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: false
translation_revision: 0817d5b28
order: 100660
---

is_numeric

Determina si una variable es un número o una cadena numérica

## Descripción

```php
is_numeric(mixed $value): bool
```php

Determina si la variable dada es un número o una [cadena numérica](#language.types.numeric-strings).

## Parámetros

`value`  
La variable a evaluar.

## Valores devueltos

Retorna `true` si `value` es un número o una [cadena numérica](#language.types.numeric-strings), `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Las cadenas numéricas que terminan con caracteres de espaciado en blanco (`"42 "`) retornarán ahora `true`. Anteriormente, se retornaba `false` en su lugar. |

## Ejemplos

Ejemplo con `is_numeric`

```
<?php
$tests = array(
    "42",
    1337,
    0x539,
    02471,
    0b10100111001,
    1337e0,
    "0x539",
    "02471",
    "0b10100111001",
    "1337e0",
    "not numeric",
    array(),
    9.1,
    null,
    '',
);

foreach ($tests as $element) {
    if (is_numeric($element)) {
        echo var_export($element, true) . " es numérico", PHP_EOL;
    } else {
        echo var_export($element, true) . " NO es numérico", PHP_EOL;
    }
}
?>

    
```php

El ejemplo anterior mostrará:

    '42' es numérico
    1337 es numérico
    1337 es numérico
    1337 es numérico
    1337 es numérico
    1337.0 es numérico
    '0x539' NO es numérico
    '02471' es numérico
    '0b10100111001' NO es numérico
    '1337e0' es numérico
    'not numeric' NO es numérico
    array (
    ) NO es numérico
    9.1 es numérico
    NULL NO es numérico
    '' NO es numérico

`is_numeric` con caracteres de espaciado en blanco

```
<?php
$tests = [
    " 42",
    "42 ",
    "\u{A0}9001", // non-breaking space
    "9001\u{A0}", // non-breaking space
];

foreach ($tests as $element) {
    if (is_numeric($element)) {
        echo var_export($element, true) . " is numeric", PHP_EOL;
    } else {
        echo var_export($element, true) . " is NOT numeric", PHP_EOL;
    }
}
?>

    
```php

Resultado del ejemplo anterior en PHP 8:

    ' 42' is numeric
    '42 ' is numeric
    ' 9001' is NOT numeric
    '9001 ' is NOT numeric

        

Resultado del ejemplo anterior en PHP 7:

    ' 42' is numeric
    '42 ' is NOT numeric
    ' 9001' is NOT numeric
    '9001 ' is NOT numeric

## Véase también

[Las cadenas numéricas](#language.types.numeric-strings), `ctype_digit`, `is_bool`, `is_null`, `is_float`, `is_int`, `is_string`, `is_object`, `is_array`, `filter_var`
