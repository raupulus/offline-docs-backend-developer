---
title: intdiv
description: División de Enteros
source_url: https://www.php.net/manual/es/function.intdiv.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/intdiv.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: false
translation_revision: 761d72245
order: 44720
---

intdiv

División de Enteros

## Descripción

```php
intdiv(int $num1, int $num2): int
```php

Devuelve el cociente entero de la división de `num1` por `num2`.

## Parámetros

`num1`  
Número a dividir.

`num2`  
Número que divide `num1`.

## Valores devueltos

El cociente entero de la división de `num1` por `num2`.

## Errores/Excepciones

Si `num2` es `0`, se emitirá una excepción `DivisionByZeroError`. Si `num1` es `PHP_INT_MIN` y `num2` es `-1`, en este caso se emite una excepción `ArithmeticError`.

## Ejemplos

Ejemplo de `intdiv`

```
<?php
var_dump(intdiv(3, 2));
var_dump(intdiv(-3, 2));
var_dump(intdiv(3, -2));
var_dump(intdiv(-3, -2));
var_dump(intdiv(PHP_INT_MAX, PHP_INT_MAX));
var_dump(intdiv(PHP_INT_MIN, PHP_INT_MIN));
?>

    
```php

El ejemplo anterior mostrará:

    int(1)
    int(-1)
    int(-1)
    int(1)
    int(1)
    int(1)

Ejemplo de `intdiv` con un divisor inválido

```
<?php
try {
    intdiv(PHP_INT_MIN, -1);
} catch (Error $e) {
    echo get_class($e), ': ', $e->getMessage(), PHP_EOL;
}

try {
    intdiv(1, 0);
} catch (Error $e) {
    echo get_class($e), ': ', $e->getMessage(), PHP_EOL;
}
?>

    
```php

El ejemplo anterior mostrará:

    ArithmeticError: Division of PHP_INT_MIN by -1 is not an integer
    DivisionByZeroError: Division by zero

## Véase también

[`/`](#language.operators.arithmetic) - División de número flotante, [`%`](#language.operators.arithmetic) - Módulo entero, `fmod` - Módulo de número flotante
