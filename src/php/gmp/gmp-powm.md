---
title: gmp_powm
description: Eleva un número a la potencia con modulo
source_url: https://www.php.net/manual/es/function.gmp-powm.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-powm.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28690
---

gmp_powm

Eleva un número a la potencia con modulo

## Descripción

```php
gmp_powm(GMP $num, GMP $exponent, GMP $modulus): GMP
```php

Calcula la (`num` elevada a la potencia `exponent`) con modulo `modulus`. Si `exponent` es negativo, el resultado es indefinido.

## Parámetros

`num`  
La base del número.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`exponent`  
La potencia positiva a elevar la `num`.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`modulus`  
El modulo.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

El nuevo (elevado) número, como un número GMP.

## Ejemplos

Ejemplo de `gmp_powm`

```
<?php
$pow1 = gmp_powm("2", "31", "2147483649");
echo gmp_strval($pow1) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    2147483648
