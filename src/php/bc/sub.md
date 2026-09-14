---
title: BcMath\Number::sub
description: Sustrae un número de precisión arbitraria
source_url: https://www.php.net/manual/es/bcmath-number.sub.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/bcmath/number/sub.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: c7e83fbbb
order: 6170
---

BcMath\Number::sub

Sustrae un número de precisión arbitraria

## Descripción

```php
public BcMath\Number::sub(BcMath\Number $num, [int $scale]): BcMath\Number
```php

Sustrae `num` de `$this`.

## Parámetros

`num`  
El valor a sustraer.

## Valores devueltos

Devuelve el resultado de la sustracción como un nuevo objeto `BcMath\Number`.

Cuando el BcMath\Number::scale del resultado se define automáticamente, se utiliza el mayor BcMath\Number::scale de los dos números utilizados para la sustracción.

## Ejemplos

Ejemplo de BcMath\Number::sub cuando `scale` no está especificado

```
<?php
$number = new BcMath\Number('1.234');

$ret1 = $number->sub(new BcMath\Number('2.34567'));
$ret2 = $number->sub('-3.456');
$ret3 = $number->sub(7);

var_dump($number, $ret1, $ret2, $ret3);
?>

   
```php

El ejemplo anterior mostrará:

    object(BcMath\Number)#1 (2) {
      ["value"]=>
      string(5) "1.234"
      ["scale"]=>
      int(3)
    }
    object(BcMath\Number)#3 (2) {
      ["value"]=>
      string(8) "-1.11167"
      ["scale"]=>
      int(5)
    }
    object(BcMath\Number)#2 (2) {
      ["value"]=>
      string(5) "4.690"
      ["scale"]=>
      int(3)
    }
    object(BcMath\Number)#4 (2) {
      ["value"]=>
      string(6) "-5.766"
      ["scale"]=>
      int(3)
    }

Ejemplo de BcMath\Number::sub especificando `scale` explícitamente

```
<?php
$number = new BcMath\Number('1.234');

$ret1 = $number->sub(new BcMath\Number('2.34567'), 1);
$ret2 = $number->sub('-3.456', 10);
$ret3 = $number->sub(7, 0);

var_dump($number, $ret1, $ret2, $ret3);
?>

   
```php

El ejemplo anterior mostrará:

    object(BcMath\Number)#1 (2) {
      ["value"]=>
      string(5) "1.234"
      ["scale"]=>
      int(3)
    }
    object(BcMath\Number)#3 (2) {
      ["value"]=>
      string(4) "-1.1"
      ["scale"]=>
      int(1)
    }
    object(BcMath\Number)#2 (2) {
      ["value"]=>
      string(12) "4.6900000000"
      ["scale"]=>
      int(10)
    }
    object(BcMath\Number)#4 (2) {
      ["value"]=>
      string(2) "-5"
      ["scale"]=>
      int(0)
    }

## Véase también

bcsub

BcMath\Number::add
