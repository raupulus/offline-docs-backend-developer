---
title: gmp_legendre
description: Símbolo Legendre
source_url: https://www.php.net/manual/es/function.gmp-legendre.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-legendre.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28590
---

gmp_legendre

Símbolo Legendre

## Descripción

```php
gmp_legendre(GMP $num1, GMP $num2): int
```php

Computa el [ Símbolo Legendre](http://primes.utm.edu/glossary/page.php?sort=LegendreSymbol) de `num1` y `num2`. `num2` debería ser impar y tiene que ser positivo.

## Parámetros

`num1`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`num2`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

debería ser impar y tiene que ser positivo.

## Valores devueltos

Un objeto `GMP`.

## Ejemplos

Ejemplo de `gmp_legendre`

```
<?php
echo gmp_legendre("1", "3") . "\n";
echo gmp_legendre("2", "3") . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    1
    0

## Véase también

gmp_jacobi

gmp_kronecker
