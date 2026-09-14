---
title: gmp_prob_prime
description: Revisa si el número es "probablemente primo"
source_url: https://www.php.net/manual/es/function.gmp-prob-prime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-prob-prime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28700
---

gmp_prob_prime

Revisa si el número es "probablemente primo"

## Descripción

```php
gmp_prob_prime(GMP $num, [int $repetitions]): int
```php

La función usa la prueba probabilística de Miller-Rabin para revisar si un número es primo.

## Parámetros

`num`  
El número a ser revisado como primo.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`repetitions`  
Valores rasonables de `repetitions` varían de 5 a 10 (por defecto siendo 10); un valor superior disminuye la probabilidad para un número no primo a pasar como un "probable" primo.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

Si ésta función devolvier 0, `num` es definitivamente no primo. Si devuelve 1, entonces `num` es "probablemente" primo. si devolviera 2, entonces `num` es seguramente primo.

## Ejemplos

Ejemplo de `gmp_prob_prime`

```
<?php
// definitivamente no primo
echo gmp_prob_prime("6") . "\n";

// probablemente primo
echo gmp_prob_prime("1111111111111111111") . "\n";

// definitivamente primo
echo gmp_prob_prime("11") . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    0
    1
    2
