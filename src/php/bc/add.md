---
title: BcMath\Number::add
description: Añadir un número de precisión arbitraria
source_url: https://www.php.net/manual/es/bcmath-number.add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/bcmath/number/add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: a414ee95e
order: 6030
---

BcMath\Number::add

Añadir un número de precisión arbitraria

## Descripción

```php
public BcMath\Number::add(BcMath\Number $num, [int $scale]): BcMath\Number
```php

Añade `$this` y `num`.

## Parámetros

`num`  
El valor a añadir.

`scale`  
BcMath\Number::scale especificado explícitamente para los resultados del cálculo. Si `null`, el BcMath\Number::scale del resultado del cálculo será definido automáticamente.

## Valores devueltos

Devuelve el resultado de la adición en forma de un nuevo objeto `BcMath\Number`.

Cuando el BcMath\Number::scale del resultado es definido automáticamente, el mayor BcMath\Number::scale de los dos números utilizados para la adición es utilizado.

Es decir, si los BcMath\Number::scale de dos valores son `2` y `5` respectivamente, el BcMath\Number::scale del resultado será `5`.

## Errores/Excepciones

Este método lanza una ValueError en los siguientes casos: `num` es un `string` y no es una cadena numérica BCMath bien formada, `scale` está fuera del rango válido

## Ejemplos

Ejemplo de BcMath\Number::add cuando `scale` no está especificado

```
<?php
$number = new BcMath\Number('1.234');

$ret1 = $number->add(new BcMath\Number('2.34567'));
$ret2 = $number->add('-3.456');
$ret3 = $number->add(7);

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
      string(7) "3.57967"
      ["scale"]=>
      int(5)
    }
    object(BcMath\Number)#2 (2) {
      ["value"]=>
      string(6) "-2.222"
      ["scale"]=>
      int(3)
    }
    object(BcMath\Number)#4 (2) {
      ["value"]=>
      string(5) "8.234"
      ["scale"]=>
      int(3)
    }

Ejemplo de BcMath\Number::add especificando `scale` explícitamente

```
<?php
$number = new BcMath\Number('1.234');

$ret1 = $number->add(new BcMath\Number('2.34567'), 1);
$ret2 = $number->add('-3.456', 10);
$ret3 = $number->add(7, 0);

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
      string(3) "3.5"
      ["scale"]=>
      int(1)
    }
    object(BcMath\Number)#2 (2) {
      ["value"]=>
      string(13) "-2.2220000000"
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

bcadd

BcMath\Number::sub
