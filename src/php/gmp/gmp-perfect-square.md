---
title: gmp_perfect_square
description: Comprueba el cuadrado perfecto
source_url: https://www.php.net/manual/es/function.gmp-perfect-square.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-perfect-square.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28660
---

gmp_perfect_square

Comprueba el cuadrado perfecto

## Descripción

```php
gmp_perfect_square(GMP $num): bool
```php

Revisa si un número es cuadrado perfecto.

## Parámetros

`num`  
El número a ser revisado como un cuadrado perfecto.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

Devielve `true` si `num` es un cuadrado perfecto, sino `false`.

## Ejemplos

Ejemplo de `gmp_perfect_square`

```
<?php
// 3 * 3, cuadrado perfecto
var_dump(gmp_perfect_square("9"));

// no es un cuadrado perfecto
var_dump(gmp_perfect_square("7"));

// 1234567890 * 1234567890, cuadrado perfecto
var_dump(gmp_perfect_square("1524157875019052100"));
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(false)
    bool(true)

## Véase también

`gmp_perfect_power`, `gmp_sqrt`, `gmp_sqrtrem`
