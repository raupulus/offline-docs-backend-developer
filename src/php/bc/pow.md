---
title: BcMath\Number::pow
description: Eleva un número de precisión arbitraria
source_url: https://www.php.net/manual/es/bcmath-number.pow.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/bcmath/number/pow.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: c7e83fbbb
order: 6120
---

BcMath\Number::pow

Eleva un número de precisión arbitraria

## Descripción

```php
public BcMath\Number::pow(BcMath\Number $exponent, [int $scale]): BcMath\Number
```php

Eleva `$this` a la potencia `exponent`.

## Parámetros

`exponent`  
El exponente. Debe ser un valor sin parte fraccionaria. El rango válido del `exponent` es específico de la plataforma, pero es al menos de `-2147483648` a `2147483647`.

## Valores devueltos

Devuelve el valor de la potencia como un nuevo objeto `BcMath\Number`.

Cuando el BcMath\Number::scale del resultado se establece automáticamente, según el valor de `exponent`, el BcMath\Number::scale del resultado será como sigue:

| `exponent` | BcMath\Number::scale del resultado |
|----|----|
| positivo | (BcMath\Number::scale de la potencia base) \* (el valor del `exponent`) |
| `0` | `0` |
| negativo | Entre (BcMath\Number::scale de la potencia base) y (BcMath\Number::scale de la potencia base + `10`) |

Si se produce una división indivisible debido a un `exponent` negativo, el BcMath\Number::scale del resultado se extiende. La extensión se realiza solo si es necesario, hasta un máximo de `+10`. Este comportamiento es el mismo que BcMath\Number::div, por lo que se debe consultar esto para más detalles.

## Errores/Excepciones

Este método lanza una ValueError en los siguientes casos: `exponent` es un `string` no es una cadena BCMath bien formada, `exponent` tiene una parte fraccionaria, `exponent` o `scale` está fuera del rango válido, El BcMath\Number::scale del resultado está fuera del rango válido

Este método lanza una excepción DivisionByZeroError si el valor de `$this` es `0` y `exponent` es un valor negativo.

## Ejemplos

Ejemplo de BcMath\Number::pow cuando `scale` no está especificado

```
<?php
$number = new BcMath\Number('3.0');

$ret1 = $number->pow(new BcMath\Number('5'));
$ret2 = $number->pow('-1');
$ret3 = $number->pow(0);

var_dump($number, $ret1, $ret2, $ret3);
?>

   
```php

El ejemplo anterior mostrará:

    object(BcMath\Number)#1 (2) {
      ["value"]=>
      string(3) "3.0"
      ["scale"]=>
      int(1)
    }
    object(BcMath\Number)#3 (2) {
      ["value"]=>
      string(9) "243.00000"
      ["scale"]=>
      int(5)
    }
    object(BcMath\Number)#2 (2) {
      ["value"]=>
      string(13) "0.33333333333"
      ["scale"]=>
      int(11)
    }
    object(BcMath\Number)#4 (2) {
      ["value"]=>
      string(1) "1"
      ["scale"]=>
      int(0)
    }

Ejemplo de BcMath\Number::pow especificando `scale` explícitamente

```
<?php
$number = new BcMath\Number('3.0');

$ret1 = $number->pow(new BcMath\Number('5'), 0);
$ret2 = $number->pow('-1', 2);
$ret3 = $number->pow(0, 10);

var_dump($number, $ret1, $ret2, $ret3);
?>

   
```php

El ejemplo anterior mostrará:

    object(BcMath\Number)#1 (2) {
      ["value"]=>
      string(3) "3.0"
      ["scale"]=>
      int(1)
    }
    object(BcMath\Number)#3 (2) {
      ["value"]=>
      string(3) "243"
      ["scale"]=>
      int(0)
    }
    object(BcMath\Number)#2 (2) {
      ["value"]=>
      string(4) "0.33"
      ["scale"]=>
      int(2)
    }
    object(BcMath\Number)#4 (2) {
      ["value"]=>
      string(12) "1.0000000000"
      ["scale"]=>
      int(10)
    }

## Véase también

bcpow

BcMath\Number::powmod

BcMath\Number::mul

BcMath\Number::sqrt

BcMath\Number::div
