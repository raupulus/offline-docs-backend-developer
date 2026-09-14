---
title: gmp_div_qr
description: Divide los números y obtiene el cociente y resto
source_url: https://www.php.net/manual/es/function.gmp-div-qr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-div-qr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28430
---

gmp_div_qr

Divide los números y obtiene el cociente y resto

## Descripción

```php
gmp_div_qr(GMP $num1, GMP $num2, [int $rounding_mode]): array
```php

La función divide a `num1` por `num2`.

## Parámetros

`num1`  
El número que es dividido.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`num2`  
El número que es dividido por `num1`.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`rounding_mode`  
Ver la función `gmp_div_q` para la descripción del argumento `rounding_mode`.

## Valores devueltos

Devuelve un `array`, con el primer elemento siendo `[n/d]` (el entero resultante de la división) y el segundo siendo `(n - [n/d] * d)` (el resto de la división).

## Ejemplos

División de números GMP

```
<?php
$a = gmp_init("0x41682179fbf5");
$res = gmp_div_qr($a, "0xDEFE75");
printf("El resultado es: q - %s, r - %s",
       gmp_strval($res[0]), gmp_strval($res[1]));
?>

    
```php

## Véase también

`gmp_div_q`, `gmp_div_r`
