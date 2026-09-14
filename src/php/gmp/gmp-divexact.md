---
title: gmp_divexact
description: División exacta de números GMP
source_url: https://www.php.net/manual/es/function.gmp-divexact.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-divexact.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_reviewed: false
translation_revision: 4b00c7916
order: 28460
---

gmp_divexact

División exacta de números GMP

## Descripción

```php
gmp_divexact(GMP $num1, GMP $num2): GMP
```php

Divide `num1` entre `num2`, utilizando los algoritmos de "división exacta". Esta función solo proporciona resultados coherentes cuando se sabe de antemano que `num2` divide `num1`.

## Parámetros

`num1`  
El número a dividir.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`num2`  
El divisor.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

Un objeto `GMP`.

## Ejemplos

Ejemplo con `gmp_divexact`

```
<?php
$div1 = gmp_divexact("10", "2");
echo gmp_strval($div1) . "\n";

$div2 = gmp_divexact("10", "3"); // resultado incoherente
echo gmp_strval($div2) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    5
    2863311534
