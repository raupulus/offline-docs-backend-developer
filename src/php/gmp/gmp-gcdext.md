---
title: gmp_gcdext
description: Calcula el máximo común divisor y multiplicadores
source_url: https://www.php.net/manual/es/function.gmp-gcdext.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-gcdext.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28500
---

gmp_gcdext

Calcula el máximo común divisor y multiplicadores

## Descripción

```php
gmp_gcdext(GMP $num1, GMP $num2): array
```php

Calcula g, s, y t, tal que `a*s + b*t = g = gcd(a,b)`, donde gcd es el máximo común divisor. Devuelve un arreglo con los elementos respectivos g, s y t.

Esta función puede ser usada para resolver ecuaciones diofánticas lineales en dos variables. Son ecuaciones que solo admiten soluciones enteras y tienen la forma: `a*x + b*y = c`. Para más información, vaya a ["Ecuación diofántica" en la página MathWorld](http://mathworld.wolfram.com/DiophantineEquation.html)

## Parámetros

`num1`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`num2`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

Un `array` de números GMP.

## Ejemplos

Resolver ecuaciones de diofántica lineal

```
<?php
// Resolver la ecuación a*s + b*t = g
// donde a = 12, b = 21, g = gcd(12, 21) = 3
$a = gmp_init(12);
$b = gmp_init(21);
$g = gmp_gcd($a, $b);
$r = gmp_gcdext($a, $b);

$check_gcd = (gmp_strval($g) == gmp_strval($r['g']));
$eq_res = gmp_add(gmp_mul($a, $r['s']), gmp_mul($b, $r['t']));
$check_res = (gmp_strval($g) == gmp_strval($eq_res));

if ($check_gcd && $check_res) {
    $fmt = "Solución: %d*%d + %d*%d = %d\n";
    printf($fmt, gmp_strval($a), gmp_strval($r['s']), gmp_strval($b),
    gmp_strval($r['t']), gmp_strval($r['g']));
} else {
    echo "Error mientras se resolvia la ecuación\n";
}

// output: Solución: 12*2 + 21*-1 = 3
?>

    
```php
