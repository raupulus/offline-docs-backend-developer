---
title: gmp_gcd
description: Calcula el máximo común divisor
source_url: https://www.php.net/manual/es/function.gmp-gcd.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-gcd.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28490
---

gmp_gcd

Calcula el máximo común divisor

## Descripción

```php
gmp_gcd(GMP $num1, GMP $num2): GMP
```php

Calcula el máximo común divisor de `num1` y `num2`. El resultado es siempre positivo aun si cualquiera de, o ambos, operadores fueran negativos.

## Parámetros

`num1`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`num2`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

Un número positivo GMP que divide dentro a ambos `num1` y `num2`.

## Ejemplos

Ejemplo de`gmp_gcd`

```
<?php
$gcd = gmp_gcd("12", "21");
echo gmp_strval($gcd) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    3

## Véase también

gmp_lcm
