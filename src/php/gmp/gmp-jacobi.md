---
title: gmp_jacobi
description: Símbolo Jacobi
source_url: https://www.php.net/manual/es/function.gmp-jacobi.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-jacobi.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28560
---

gmp_jacobi

Símbolo Jacobi

## Descripción

```php
gmp_jacobi(GMP $num1, GMP $num2): int
```php

Computa el [símbolo Jacobi](http://primes.utm.edu/glossary/page.php?sort=JacobiSymbol) de `num1` y `num2`. `num2` debería ser impar y tiene que ser positivo.

## Parámetros

`num1`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`num2`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

Debería ser impar y tiene que ser positivo.

## Valores devueltos

Un objeto `GMP`.

## Ejemplos

Ejemplo de `gmp_jacobi`

```
<?php
echo gmp_jacobi("1", "3") . "\n";
echo gmp_jacobi("2", "3") . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    1
    0

## Véase también

gmp_kronecker

gmp_legendre
