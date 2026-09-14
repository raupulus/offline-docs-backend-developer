---
title: gmp_pow
description: Aumenta el número a la potencia
source_url: https://www.php.net/manual/es/function.gmp-pow.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-pow.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28680
---

gmp_pow

Aumenta el número a la potencia

## Descripción

```php
gmp_pow(GMP $num, int $exponent): GMP
```php

Aumenta la `num` a la potencia `exponent`.

## Parámetros

`num`  
La base del número.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`exponent`  
La potencia positiva a elevar la `num`.

## Valores devueltos

El nuevo (elevado) número, como un número GMP. El caso de `0^0` produce 1.

## Ejemplos

Ejemplo de `gmp_pow`

```
<?php
$pow1 = gmp_pow("2", 31);
echo gmp_strval($pow1) . "\n";
$pow2 = gmp_pow("0", 0);
echo gmp_strval($pow2) . "\n";
$pow3 = gmp_pow("2", -1); // exponente negativo, genera peligro
echo gmp_strval($pow3) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    2147483648
    1
