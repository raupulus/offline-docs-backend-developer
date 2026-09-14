---
title: bcround
description: Redondea un número de precisión arbitraria
source_url: https://www.php.net/manual/es/function.bcround.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/functions/bcround.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_revision: c142be811
order: 6320
---

bcround

Redondea un número de precisión arbitraria

## Descripción

```php
bcround(string $num, [int $precision], [RoundingMode $mode]): string
```php

Devuelve el valor redondeado de `num` a la precisión especificada `precision` (número de dígitos después del punto decimal). `precision` puede ser también negativo o nulo (por omisión).

## Parámetros

## Valores devueltos

Devuelve una cadena numérica representando `num` redondeado a la precisión dada.

## Errores/Excepciones

Esta función lanza una ValueError en los siguientes casos: `num` no es una cadena numérica BCMath bien formada., Un `mode` inválido es especificado.

## Ejemplos

Ejemplos de `bcround`

```
<?php
var_dump(bcround('3.4'));
var_dump(bcround('3.5'));
var_dump(bcround('3.6'));
var_dump(bcround('3.6', 0));
var_dump(bcround('5.045', 2));
var_dump(bcround('5.055', 2));
var_dump(bcround('345', -2));
var_dump(bcround('345', -3));
var_dump(bcround('678', -2));
var_dump(bcround('678', -3));
?>

   
```php

El ejemplo anterior mostrará:

```
string(1) "3"
string(1) "4"
string(1) "4"
string(1) "4"
string(4) "5.05"
string(4) "5.06"
string(3) "300"
string(1) "0"
string(3) "700"
string(4) "1000"

   
```php

Ejemplo de la utilización de `bcround` con diferentes valores de `precision`

```
<?php
$number = '123.45';

var_dump(bcround($number, 3));
var_dump(bcround($number, 2));
var_dump(bcround($number, 1));
var_dump(bcround($number, 0));
var_dump(bcround($number, -1));
var_dump(bcround($number, -2));
var_dump(bcround($number, -3));
?>

   
```php

El ejemplo anterior mostrará:

```
string(7) "123.450"
string(6) "123.45"
string(5) "123.5"
string(3) "123"
string(3) "120"
string(3) "100"
string(1) "0"

   
```php

Ejemplo de la utilización de `bcround` con diferentes valores de `mode`

```
<?php
echo 'Modos de redondeo con 9.5' . PHP_EOL;
var_dump(bcround('9.5', 0, RoundingMode::HalfAwayFromZero));
var_dump(bcround('9.5', 0, RoundingMode::HalfTowardsZero));
var_dump(bcround('9.5', 0, RoundingMode::HalfEven));
var_dump(bcround('9.5', 0, RoundingMode::HalfOdd));
var_dump(bcround('9.5', 0, RoundingMode::TowardsZero));
var_dump(bcround('9.5', 0, RoundingMode::AwayFromZero));
var_dump(bcround('9.5', 0, RoundingMode::NegativeInfinity));
var_dump(bcround('9.5', 0, RoundingMode::PositiveInfinity));

echo PHP_EOL;
echo 'Modos de redondeo con 8.5' . PHP_EOL;
var_dump(bcround('8.5', 0, RoundingMode::HalfAwayFromZero));
var_dump(bcround('8.5', 0, RoundingMode::HalfTowardsZero));
var_dump(bcround('8.5', 0, RoundingMode::HalfEven));
var_dump(bcround('8.5', 0, RoundingMode::HalfOdd));
var_dump(bcround('8.5', 0, RoundingMode::TowardsZero));
var_dump(bcround('8.5', 0, RoundingMode::AwayFromZero));
var_dump(bcround('8.5', 0, RoundingMode::NegativeInfinity));
var_dump(bcround('8.5', 0, RoundingMode::PositiveInfinity));
?>

   
```php

El ejemplo anterior mostrará:

```
Modos de redondeo con 9.5
string(2) "10"
string(1) "9"
string(2) "10"
string(1) "9"
string(1) "9"
string(2) "10"
string(1) "9"
string(2) "10"

Modos de redondeo con 8.5
string(1) "9"
string(1) "8"
string(1) "8"
string(1) "9"
string(1) "8"
string(1) "9"
string(1) "8"
string(1) "9"

   
```php

Ejemplo de la utilización de `bcround` con diferentes valores de `mode` al especificar `precision`

```
<?php
echo 'Utilización de RoundingMode::HalfAwayFromZero con una precisión decimal de 1' . PHP_EOL;
var_dump(bcround( 1.55, 1, RoundingMode::HalfAwayFromZero));
var_dump(bcround(-1.55, 1, RoundingMode::HalfAwayFromZero));

echo PHP_EOL;
echo 'Utilización de RoundingMode::HalfTowardsZero con una precisión decimal de 1' . PHP_EOL;
var_dump(bcround( 1.55, 1, RoundingMode::HalfTowardsZero));
var_dump(bcround(-1.55, 1, RoundingMode::HalfTowardsZero));

echo PHP_EOL;
echo 'Utilización de RoundingMode::HalfEven con una precisión decimal de 1' . PHP_EOL;
var_dump(bcround( 1.55, 1, RoundingMode::HalfEven));
var_dump(bcround(-1.55, 1, RoundingMode::HalfEven));

echo PHP_EOL;
echo 'Utilización de RoundingMode::HalfOdd con una precisión decimal de 1' . PHP_EOL;
var_dump(bcround( 1.55, 1, RoundingMode::HalfOdd));
var_dump(bcround(-1.55, 1, RoundingMode::HalfOdd));

echo PHP_EOL;
echo 'Utilización de RoundingMode::TowardsZero con una precisión decimal de 1' . PHP_EOL;
var_dump(bcround( 1.55, 1, RoundingMode::TowardsZero));
var_dump(bcround(-1.55, 1, RoundingMode::TowardsZero));

echo PHP_EOL;
echo 'Utilización de RoundingMode::AwayFromZero con una precisión decimal de 1' . PHP_EOL;
var_dump(bcround( 1.55, 1, RoundingMode::AwayFromZero));
var_dump(bcround(-1.55, 1, RoundingMode::AwayFromZero));

echo PHP_EOL;
echo 'Utilización de RoundingMode::NegativeInfinity con una precisión decimal de 1' . PHP_EOL;
var_dump(bcround( 1.55, 1, RoundingMode::NegativeInfinity));
var_dump(bcround(-1.55, 1, RoundingMode::NegativeInfinity));

echo PHP_EOL;
echo 'Utilización de RoundingMode::PositiveInfinity con una precisión decimal de 1' . PHP_EOL;
var_dump(bcround( 1.55, 1, RoundingMode::PositiveInfinity));
var_dump(bcround(-1.55, 1, RoundingMode::PositiveInfinity));
?>

   
```php

El ejemplo anterior mostrará:

```
Utilización de RoundingMode::HalfAwayFromZero con una precisión decimal de 1
string(3) "1.6"
string(4) "-1.6"

Utilización de RoundingMode::HalfTowardsZero con una precisión decimal de 1
string(3) "1.5"
string(4) "-1.5"

Utilización de RoundingMode::HalfEven con una precisión decimal de 1
string(3) "1.6"
string(4) "-1.6"

Utilización de RoundingMode::HalfOdd con una precisión decimal de 1
string(3) "1.5"
string(4) "-1.5"

Utilización de RoundingMode::TowardsZero con una precisión decimal de 1
string(3) "1.5"
string(4) "-1.5"

Utilización de RoundingMode::AwayFromZero con una precisión decimal de 1
string(3) "1.6"
string(4) "-1.6"

Utilización de RoundingMode::NegativeInfinity con una precisión decimal de 1
string(3) "1.5"
string(4) "-1.6"

Utilización de RoundingMode::PositiveInfinity con una precisión decimal de 1
string(3) "1.6"
string(4) "-1.5"

   
```php

## Véase también

bcceil

bcfloor

BcMath\Number::round
