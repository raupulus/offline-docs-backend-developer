---
title: BcMath\Number::round
description: Redondea un número de precisión arbitraria
source_url: https://www.php.net/manual/es/bcmath-number.round.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/bcmath/number/round.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_revision: c142be811
order: 6140
---

BcMath\Number::round

Redondea un número de precisión arbitraria

## Descripción

```php
public BcMath\Number::round([int $precision], [RoundingMode $mode]): BcMath\Number
```php

Devuelve el valor redondeado de `$this` a la `precisión` especificada (el número de dígitos después del punto decimal). `precisión` puede ser también negativo o nulo (por omisión).

## Parámetros

`mode`  
Especifica el método de redondeo. Para más información sobre los métodos, ver RoundingMode.

## Valores devueltos

Devuelve el resultado en forma de un nuevo objeto `BcMath\Number`.

## Errores/Excepciones

Este método lanza una ValueError si se especifica un `mode` inválido.

## Ejemplos

Ejemplo de BcMath\Number::round

```
<?php
var_dump(
    new BcMath\Number('3.4')->round(),
    new BcMath\Number('3.5')->round(),
    new BcMath\Number('3.6')->round(),
    new BcMath\Number('3.6')->round(0),
    new BcMath\Number('5.045')->round(2),
    new BcMath\Number('5.055')->round(2),
    new BcMath\Number('345')->round(-2),
    new BcMath\Number('345')->round(-3),
    new BcMath\Number('678')->round(-2),
    new BcMath\Number('678')->round(-3),
);
?>

   
```php

El ejemplo anterior mostrará:

```
object(BcMath\Number)#2 (2) {
  ["value"]=>
  string(1) "3"
  ["scale"]=>
  int(0)
}
object(BcMath\Number)#3 (2) {
  ["value"]=>
  string(1) "4"
  ["scale"]=>
  int(0)
}
object(BcMath\Number)#4 (2) {
  ["value"]=>
  string(1) "4"
  ["scale"]=>
  int(0)
}
object(BcMath\Number)#5 (2) {
  ["value"]=>
  string(1) "4"
  ["scale"]=>
  int(0)
}
object(BcMath\Number)#6 (2) {
  ["value"]=>
  string(4) "5.05"
  ["scale"]=>
  int(2)
}
object(BcMath\Number)#7 (2) {
  ["value"]=>
  string(4) "5.06"
  ["scale"]=>
  int(2)
}
object(BcMath\Number)#8 (2) {
  ["value"]=>
  string(3) "300"
  ["scale"]=>
  int(0)
}
object(BcMath\Number)#9 (2) {
  ["value"]=>
  string(1) "0"
  ["scale"]=>
  int(0)
}
object(BcMath\Number)#10 (2) {
  ["value"]=>
  string(3) "700"
  ["scale"]=>
  int(0)
}
object(BcMath\Number)#11 (2) {
  ["value"]=>
  string(4) "1000"
  ["scale"]=>
  int(0)
}

   
```php

Ejemplo de uso de BcMath\Number::round con diferentes valores de `precisión`

```
<?php
$number = new BcMath\Number('123.45');

var_dump(
    $number->round(3),
    $number->round(2),
    $number->round(1),
    $number->round(0),
    $number->round(-1),
    $number->round(-2),
    $number->round(-3),
);
?>

   
```php

El ejemplo anterior mostrará:

```
object(BcMath\Number)#2 (2) {
  ["value"]=>
  string(7) "123.450"
  ["scale"]=>
  int(3)
}
object(BcMath\Number)#3 (2) {
  ["value"]=>
  string(6) "123.45"
  ["scale"]=>
  int(2)
}
object(BcMath\Number)#4 (2) {
  ["value"]=>
  string(5) "123.5"
  ["scale"]=>
  int(1)
}
object(BcMath\Number)#5 (2) {
  ["value"]=>
  string(3) "123"
  ["scale"]=>
  int(0)
}
object(BcMath\Number)#6 (2) {
  ["value"]=>
  string(3) "120"
  ["scale"]=>
  int(0)
}
object(BcMath\Number)#7 (2) {
  ["value"]=>
  string(3) "100"
  ["scale"]=>
  int(0)
}
object(BcMath\Number)#8 (2) {
  ["value"]=>
  string(1) "0"
  ["scale"]=>
  int(0)
}

   
```php

Ejemplo de uso de BcMath\Number::round con diferentes valores de `mode`

```
<?php
echo 'Modos de redondeo con 9.5' . PHP_EOL;
$number = new BcMath\Number('9.5');
var_dump(
    $number->round(0, RoundingMode::HalfAwayFromZero),
    $number->round(0, RoundingMode::HalfTowardsZero),
    $number->round(0, RoundingMode::HalfEven),
    $number->round(0, RoundingMode::HalfOdd),
    $number->round(0, RoundingMode::TowardsZero),
    $number->round(0, RoundingMode::AwayFromZero),
    $number->round(0, RoundingMode::NegativeInfinity),
    $number->round(0, RoundingMode::PositiveInfinity),
);

echo PHP_EOL;
echo 'Modos de redondeo con 8.5' . PHP_EOL;
$number = new BcMath\Number('8.5');
var_dump(
    $number->round(0, RoundingMode::HalfAwayFromZero),
    $number->round(0, RoundingMode::HalfTowardsZero),
    $number->round(0, RoundingMode::HalfEven),
    $number->round(0, RoundingMode::HalfOdd),
    $number->round(0, RoundingMode::TowardsZero),
    $number->round(0, RoundingMode::AwayFromZero),
    $number->round(0, RoundingMode::NegativeInfinity),
    $number->round(0, RoundingMode::PositiveInfinity),
);
?>

   
```php

El ejemplo anterior mostrará:

```
Modos de redondeo con 9.5
object(BcMath\Number)#3 (2) {
  ["value"]=>
  string(2) "10"
  ["scale"]=>
  int(0)
}
object(BcMath\Number)#5 (2) {
  ["value"]=>
  string(1) "9"
  ["scale"]=>
  int(0)
}
object(BcMath\Number)#7 (2) {
  ["value"]=>
  string(2) "10"
  ["scale"]=>
  int(0)
}
object(BcMath\Number)#9 (2) {
  ["value"]=>
  string(1) "9"
  ["scale"]=>
  int(0)
}
object(BcMath\Number)#11 (2) {
  ["value"]=>
  string(1) "9"
  ["scale"]=>
  int(0)
}
object(BcMath\Number)#13 (2) {
  ["value"]=>
  string(2) "10"
  ["scale"]=>
  int(0)
}
object(BcMath\Number)#15 (2) {
  ["value"]=>
  string(1) "9"
  ["scale"]=>
  int(0)
}
object(BcMath\Number)#17 (2) {
  ["value"]=>
  string(2) "10"
  ["scale"]=>
  int(0)
}

Modos de redondeo con 8.5
object(BcMath\Number)#1 (2) {
  ["value"]=>
  string(1) "9"
  ["scale"]=>
  int(0)
}
object(BcMath\Number)#15 (2) {
  ["value"]=>
  string(1) "8"
  ["scale"]=>
  int(0)
}
object(BcMath\Number)#13 (2) {
  ["value"]=>
  string(1) "8"
  ["scale"]=>
  int(0)
}
object(BcMath\Number)#11 (2) {
  ["value"]=>
  string(1) "9"
  ["scale"]=>
  int(0)
}
object(BcMath\Number)#9 (2) {
  ["value"]=>
  string(1) "8"
  ["scale"]=>
  int(0)
}
object(BcMath\Number)#7 (2) {
  ["value"]=>
  string(1) "9"
  ["scale"]=>
  int(0)
}
object(BcMath\Number)#5 (2) {
  ["value"]=>
  string(1) "8"
  ["scale"]=>
  int(0)
}
object(BcMath\Number)#3 (2) {
  ["value"]=>
  string(1) "9"
  ["scale"]=>
  int(0)
}

   
```php

Ejemplo de uso de BcMath\Number::round con diferentes valores de `mode` especificando `precisión`

```
<?php
$positive = new BcMath\Number('1.55');
$negative = new BcMath\Number('-1.55');

echo 'Uso de RoundingMode::HalfAwayFromZero con precisión de 1 dígito decimal' . PHP_EOL;
var_dump(
    $positive->round(1, RoundingMode::HalfAwayFromZero),
    $negative->round(1, RoundingMode::HalfAwayFromZero),
);

echo PHP_EOL;
echo 'Uso de RoundingMode::HalfTowardsZero con precisión de 1 dígito decimal' . PHP_EOL;
var_dump(
    $positive->round(1, RoundingMode::HalfTowardsZero),
    $negative->round(1, RoundingMode::HalfTowardsZero),
);

echo PHP_EOL;
echo 'Uso de RoundingMode::HalfEven con precisión de 1 dígito decimal' . PHP_EOL;
var_dump(
    $positive->round(1, RoundingMode::HalfEven),
    $negative->round(1, RoundingMode::HalfEven),
);

echo PHP_EOL;
echo 'Uso de RoundingMode::HalfOdd con precisión de 1 dígito decimal' . PHP_EOL;
var_dump(
    $positive->round(1, RoundingMode::HalfOdd),
    $negative->round(1, RoundingMode::HalfOdd),
);

echo PHP_EOL;
echo 'Uso de RoundingMode::TowardsZero con precisión de 1 dígito decimal' . PHP_EOL;
var_dump(
    $positive->round(1, RoundingMode::TowardsZero),
    $negative->round(1, RoundingMode::TowardsZero),
);

echo PHP_EOL;
echo 'Uso de RoundingMode::AwayFromZero con precisión de 1 dígito decimal' . PHP_EOL;
var_dump(
    $positive->round(1, RoundingMode::AwayFromZero),
    $negative->round(1, RoundingMode::AwayFromZero),
);

echo PHP_EOL;
echo 'Uso de RoundingMode::NegativeInfinity con precisión de 1 dígito decimal' . PHP_EOL;
var_dump(
    $positive->round(1, RoundingMode::NegativeInfinity),
    $negative->round(1, RoundingMode::NegativeInfinity),
);

echo PHP_EOL;
echo 'Uso de RoundingMode::PositiveInfinity con precisión de 1 dígito decimal' . PHP_EOL;
var_dump(
    $positive->round(1, RoundingMode::PositiveInfinity),
    $negative->round(1, RoundingMode::PositiveInfinity),
);
?>

   
```php

El ejemplo anterior mostrará:

```
Uso de RoundingMode::HalfAwayFromZero con precisión de 1 dígito decimal
object(BcMath\Number)#4 (2) {
  ["value"]=>
  string(3) "1.6"
  ["scale"]=>
  int(1)
}
object(BcMath\Number)#5 (2) {
  ["value"]=>
  string(4) "-1.6"
  ["scale"]=>
  int(1)
}

Uso de RoundingMode::HalfTowardsZero con precisión de 1 dígito decimal
object(BcMath\Number)#4 (2) {
  ["value"]=>
  string(3) "1.5"
  ["scale"]=>
  int(1)
}
object(BcMath\Number)#6 (2) {
  ["value"]=>
  string(4) "-1.5"
  ["scale"]=>
  int(1)
}

Uso de RoundingMode::HalfEven con precisión de 1 dígito decimal
object(BcMath\Number)#4 (2) {
  ["value"]=>
  string(3) "1.6"
  ["scale"]=>
  int(1)
}
object(BcMath\Number)#7 (2) {
  ["value"]=>
  string(4) "-1.6"
  ["scale"]=>
  int(1)
}

Uso de RoundingMode::HalfOdd con precisión de 1 dígito decimal
object(BcMath\Number)#4 (2) {
  ["value"]=>
  string(3) "1.5"
  ["scale"]=>
  int(1)
}
object(BcMath\Number)#8 (2) {
  ["value"]=>
  string(4) "-1.5"
  ["scale"]=>
  int(1)
}

Uso de RoundingMode::TowardsZero con precisión de 1 dígito decimal
object(BcMath\Number)#4 (2) {
  ["value"]=>
  string(3) "1.5"
  ["scale"]=>
  int(1)
}
object(BcMath\Number)#9 (2) {
  ["value"]=>
  string(4) "-1.5"
  ["scale"]=>
  int(1)
}

Uso de RoundingMode::AwayFromZero con precisión de 1 dígito decimal
object(BcMath\Number)#4 (2) {
  ["value"]=>
  string(3) "1.6"
  ["scale"]=>
  int(1)
}
object(BcMath\Number)#10 (2) {
  ["value"]=>
  string(4) "-1.6"
  ["scale"]=>
  int(1)
}

Uso de RoundingMode::NegativeInfinity con precisión de 1 dígito decimal
object(BcMath\Number)#4 (2) {
  ["value"]=>
  string(3) "1.5"
  ["scale"]=>
  int(1)
}
object(BcMath\Number)#11 (2) {
  ["value"]=>
  string(4) "-1.6"
  ["scale"]=>
  int(1)
}

Uso de RoundingMode::PositiveInfinity con precisión de 1 dígito decimal
object(BcMath\Number)#4 (2) {
  ["value"]=>
  string(3) "1.6"
  ["scale"]=>
  int(1)
}
object(BcMath\Number)#12 (2) {
  ["value"]=>
  string(4) "-1.5"
  ["scale"]=>
  int(1)
}

   
```php

## Véase también

bcround

BcMath\Number::ceil

BcMath\Number::floor
