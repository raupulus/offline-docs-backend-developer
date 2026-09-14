---
title: fmod
description: Devuelve el resto de la división
source_url: https://www.php.net/manual/es/function.fmod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/fmod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_revision: 54a788ca5
order: 44680
---

fmod

Devuelve el resto de la división

## Descripción

```php
fmod(float $num1, float $num2): float
```php

Devuelve el resto de la división de `num1` por `num2`. Este resto es un número de punto flotante. El resto (`r`) se define por: num1 = i \* num2 + r, para un entero `i`. Si `num2` no es nulo, `r` tiene el mismo signo que `num1` y un valor absoluto menor que `num2`.

## Parámetros

`num1`  
El dividendo

`num2`  
El divisor

## Valores devueltos

El resto de la división de `num1` por `num2`. `NAN` (`float`) si el segundo argumento es 0.

## Ejemplos

Ejemplo con `fmod`

```
<?php
$x = 5.7;
$y = 1.3;
$r = fmod($x, $y);
// $r vale 0.5, porque 4 * 1.3 + 0.5 = 5.7

var_dump($x, $y, $r);
?>

    
```php

## Véase también

[`/`](#language.operators.arithmetic) - División de punto flotante, [`%`](#language.operators.arithmetic) - Módulo de enteros, `intdiv` - División de enteros
