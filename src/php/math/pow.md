---
title: pow
description: Expresión exponencial
source_url: https://www.php.net/manual/es/function.pow.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/pow.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: false
translation_revision: 761d72245
order: 44830
---

pow

Expresión exponencial

## Descripción

```php
pow(mixed $num, mixed $exponent): int
```php

Devuelve `num` elevado a la potencia `exponent`.

> [!NOTE]
> Es posible utilizar el operador [\*\*](#language.operators.arithmetic) en su lugar.

## Parámetros

`num`  
La base a utilizar

`exponent`  
El exponente

## Valores devueltos

`num` elevado a la potencia `exponent`. Si los argumentos no son enteros negativos, y el resultado puede ser representado como un entero, el resultado será `int`, de lo contrario será devuelto como `float`.

Las extensiones PHP pueden reemplazar el comportamiento de esta operación y hacer que devuelva un objeto.

## Historial de cambios

| Versión | Descripción                                             |
|---------|---------------------------------------------------------|
| 8.4.0   | Elevar `0` a un `exponente` negativo es ahora obsoleto. |

## Ejemplos

Ejemplo con `pow`

```
<?php

var_dump(pow(2, 8)); // int(256)
echo pow(-1, 20), PHP_EOL; // 1
echo pow(0, 0), PHP_EOL; // 1
echo pow(10, -1), PHP_EOL; // 0.1

echo pow(-1, 5.5), PHP_EOL; // NAN
?>

    
```php

Ejemplos de `pow` con un objeto de la extensión GMP

```
<?php
var_dump(pow(new GMP("3"), new GMP("2"))); // object(GMP)
?>

    
```php

## Notas

> [!NOTE]
> Esta función convertirá todas las entradas en un número, incluyendo valores no escalares, lo que puede llevar a resultados *impredecibles*.

## Véase también

Operador de exponenciación [`**`](#language.operators.arithmetic), `fpow`, `exp`, `sqrt`, `bcpow`, `gmp_pow`
