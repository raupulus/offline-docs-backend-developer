---
title: gmp_hamdist
description: Distancia Hamming
source_url: https://www.php.net/manual/es/function.gmp-hamdist.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-hamdist.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28510
---

gmp_hamdist

Distancia Hamming

## Descripción

```php
gmp_hamdist(GMP $num1, GMP $num2): int
```php

Devuelve la distancia hamming entre `num1` y `num2`. Ambos operadores deberían ser no negativos.

## Parámetros

`num1`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

Debería ser positivo.

`num2`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

Debería ser positivo.

## Valores devueltos

La distancia de Hamming entre `num1` y `num2`, como un `int`.

## Ejemplos

Ejemplo de`gmp_hamdist`

```
<?php
$ham1 = gmp_init("1001010011", 2);
$ham2 = gmp_init("1011111100", 2);
echo gmp_hamdist($ham1, $ham2) . "\n";

/* la distancia hamming es equivalente a: */
echo gmp_popcount(gmp_xor($ham1, $ham2)) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    6
    6

## Véase también

`gmp_popcount`, `gmp_xor`
