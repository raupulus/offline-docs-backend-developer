---
title: BcMath\Number::mul
description: Multiplica un número de precisión arbitraria
source_url: https://www.php.net/manual/es/bcmath-number.mul.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/bcmath/number/mul.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: c7e83fbbb
order: 6110
---

BcMath\Number::mul

Multiplica un número de precisión arbitraria

## Descripción

```php
public BcMath\Number::mul(BcMath\Number $num, [int $scale]): BcMath\Number
```php

Multiplica `$this` por `num`.

## Parámetros

`num`  
El multiplicador.

## Valores devueltos

Devuelve el resultado de la multiplicación como un nuevo objeto `BcMath\Number`.

Cuando la BcMath\Number::scale del resultado se establece automáticamente, se utiliza la suma de las BcMath\Number::scales de los dos valores utilizados para la multiplicación.

Es decir, si las BcMath\Number::scales de dos valores son `2` y `5` respectivamente, la BcMath\Number::scale del resultado será `7`.

## Errores/Excepciones

## Ejemplos

Ejemplo de BcMath\Number::mul cuando `scale` no está especificado

```
<?php
$number = new BcMath\Number('1.234');

$ret1 = $number->mul(new BcMath\Number('2.3456'));
$ret2 = $number->mul('-3.4');
$ret3 = $number->mul(7);

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
      string(9) "2.8944704"
      ["scale"]=>
      int(7)
    }
    object(BcMath\Number)#2 (2) {
      ["value"]=>
      string(7) "-4.1956"
      ["scale"]=>
      int(4)
    }
    object(BcMath\Number)#4 (2) {
      ["value"]=>
      string(5) "8.638"
      ["scale"]=>
      int(3)
    }

Ejemplo de BcMath\Number::mul especificando `scale` explícitamente

```
<?php
$number = new BcMath\Number('1.234');

$ret1 = $number->mul(new BcMath\Number('2.3456'), 1);
$ret2 = $number->mul('-3.4', 10);
$ret3 = $number->mul(7, 0);

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
      string(3) "2.8"
      ["scale"]=>
      int(1)
    }
    object(BcMath\Number)#2 (2) {
      ["value"]=>
      string(13) "-4.1956000000"
      ["scale"]=>
      int(10)
    }
    object(BcMath\Number)#4 (2) {
      ["value"]=>
      string(1) "8"
      ["scale"]=>
      int(0)
    }

## Véase también

bcmul

BcMath\Number::div

BcMath\Number::pow

BcMath\Number::powmod
