---
title: BcMath\Number::div
description: Divide por un número de precisión arbitraria
source_url: https://www.php.net/manual/es/bcmath-number.div.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/bcmath/number/div.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: a414ee95e
order: 6070
---

BcMath\Number::div

Divide por un número de precisión arbitraria

## Descripción

```php
public BcMath\Number::div(BcMath\Number $num, [int $scale]): BcMath\Number
```php

Divide `$this` por `num`.

## Parámetros

`num`  
El divisor.

## Valores devueltos

Devuelve el resultado de una división en forma de un nuevo objeto `BcMath\Number`.

Cuando el BcMath\Number::scale del resultado se define automáticamente, se utiliza el BcMath\Number::scale del dividendo. Sin embargo, en casos como la división indivisible, el BcMath\Number::scale del resultado se extiende. La extensión se realiza solo si es necesario, hasta un máximo de `+10`.

Es decir, si el BcMath\Number::scale del dividendo es `5`, el BcMath\Number::scale del resultado está entre `5` y `15`.

Incluso en cálculos indivisibles, el BcMath\Number::scale no siempre será `+10`. Un `0` al final del resultado se considera que no necesita extensión, por lo que el BcMath\Number::scale se reduce en esa cantidad. El BcMath\Number::scale nunca será inferior al BcMath\Number::scale antes de la extensión. Véase también los [ejemplos de código](#bcmath-number.div.example.expansion-scale).

## Errores/Excepciones

Este método lanza una ValueError en los siguientes casos: `num` es un `string` y no es una cadena numérica BCMath bien formada, `scale` está fuera del rango válido, BcMath\Number::scale del resultado está fuera del rango válido

Este método lanza una DivisionByZeroError si `num` es `0`.

## Ejemplos

Ejemplo BcMath\Number::div cuando `scale` no está especificado

```
<?php
$number = new BcMath\Number('0.002');

$ret1 = $number->div(new BcMath\Number('2.000'));
$ret2 = $number->div('-3');
$ret3 = $number->div(32);

var_dump($number, $ret1, $ret2, $ret3);
?>

   
```php

El ejemplo anterior mostrará:

    object(BcMath\Number)#1 (2) {
      ["value"]=>
      string(5) "0.002"
      ["scale"]=>
      int(3)
    }
    object(BcMath\Number)#3 (2) {
      ["value"]=>
      string(5) "0.001"
      ["scale"]=>
      int(3)
    }
    object(BcMath\Number)#2 (2) {
      ["value"]=>
      string(16) "-0.0006666666666"
      ["scale"]=>
      int(13)
    }
    object(BcMath\Number)#4 (2) {
      ["value"]=>
      string(9) "0.0000625"
      ["scale"]=>
      int(7)
    }

Ejemplo de BcMath\Number::div especificando `scale` explícitamente

```
<?php
$number = new BcMath\Number('0.002');

$ret1 = $number->div(new BcMath\Number('2.000'), 15);
$ret2 = $number->div('-3', 5);
$ret3 = $number->div(32, 2);

var_dump($number, $ret1, $ret2, $ret3);
?>

   
```php

El ejemplo anterior mostrará:

    object(BcMath\Number)#1 (2) {
      ["value"]=>
      string(5) "0.002"
      ["scale"]=>
      int(3)
    }
    object(BcMath\Number)#3 (2) {
      ["value"]=>
      string(17) "0.001000000000000"
      ["scale"]=>
      int(15)
    }
    object(BcMath\Number)#2 (2) {
      ["value"]=>
      string(8) "-0.00066"
      ["scale"]=>
      int(5)
    }
    object(BcMath\Number)#4 (2) {
      ["value"]=>
      string(4) "0.00"
      ["scale"]=>
      int(2)
    }

Ejemplo de BcMath\Number::div expandiendo BcMath\Number::scale del objeto resultado

```
<?php
var_dump(
    new BcMath\Number('0.001')->div('10001'),
    new BcMath\Number('0.001')->div('10001', 13),
    new BcMath\Number('0.001')->div('100000000000001'),
);
?>

   
```php

El ejemplo anterior mostrará:

    object(BcMath\Number)#2 (2) {
      ["value"]=>
      string(13) "0.00000009999"
      ["scale"]=>
      int(11)
    }
    object(BcMath\Number)#3 (2) {
      ["value"]=>
      string(15) "0.0000000999900"
      ["scale"]=>
      int(13)
    }
    object(BcMath\Number)#4 (2) {
      ["value"]=>
      string(5) "0.000"
      ["scale"]=>
      int(3)
    }

## Véase también

bcdiv

BcMath\Number::divmod

BcMath\Number::mod

BcMath\Number::sqrt

BcMath\Number::pow

BcMath\Number::mul
