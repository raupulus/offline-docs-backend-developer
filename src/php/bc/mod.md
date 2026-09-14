---
title: BcMath\Number::mod
description: Devuelve el módulo de un número de precisión arbitraria
source_url: https://www.php.net/manual/es/bcmath-number.mod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/bcmath/number/mod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: c7e83fbbb
order: 6100
---

BcMath\Number::mod

Devuelve el módulo de un número de precisión arbitraria

## Descripción

```php
public BcMath\Number::mod(BcMath\Number $num, [int $scale]): BcMath\Number
```php

Devuelve el resto de la división de `$this` por `num`. Excepto si `num` es `0`, el resultado tiene el mismo signo que `$this`.

## Valores devueltos

Devuelve el módulo en forma de un nuevo objeto `BcMath\Number`.

Cuando el BcMath\Number::scale del resultado se define automáticamente, se utiliza el mayor BcMath\Number::scale de los dos números utilizados para la operación de módulo.

## Errores/Excepciones

## Ejemplos

Ejemplo de BcMath\Number::mod cuando `scale` no está especificado

```
<?php
$number = new BcMath\Number('8.3');

$ret1 = $number->mod(new BcMath\Number('2.22'));
$ret2 = $number->mod('8.3');
$ret3 = $number->mod(-5);

var_dump($number, $ret1, $ret2, $ret3);
?>

   
```php

El ejemplo anterior mostrará:

    object(BcMath\Number)#1 (2) {
      ["value"]=>
      string(3) "8.3"
      ["scale"]=>
      int(1)
    }
    object(BcMath\Number)#3 (2) {
      ["value"]=>
      string(4) "1.64"
      ["scale"]=>
      int(2)
    }
    object(BcMath\Number)#2 (2) {
      ["value"]=>
      string(3) "0.0"
      ["scale"]=>
      int(1)
    }
    object(BcMath\Number)#4 (2) {
      ["value"]=>
      string(3) "3.3"
      ["scale"]=>
      int(1)
    }

Ejemplo de BcMath\Number::mod definiendo `scale` explícitamente

```
<?php
$number = new BcMath\Number('8.3');

$ret1 = $number->mod(new BcMath\Number('2.22'), 1);
$ret2 = $number->mod('8.3', 3);
$ret3 = $number->mod(-5, 0);

var_dump($number, $ret1, $ret2, $ret3);
?>

   
```php

El ejemplo anterior mostrará:

    object(BcMath\Number)#1 (2) {
      ["value"]=>
      string(3) "8.3"
      ["scale"]=>
      int(1)
    }
    object(BcMath\Number)#3 (2) {
      ["value"]=>
      string(3) "1.6"
      ["scale"]=>
      int(1)
    }
    object(BcMath\Number)#2 (2) {
      ["value"]=>
      string(5) "0.000"
      ["scale"]=>
      int(3)
    }
    object(BcMath\Number)#4 (2) {
      ["value"]=>
      string(1) "3"
      ["scale"]=>
      int(0)
    }

## Véase también

bcmod

BcMath\Number::div

BcMath\Number::divmod

BcMath\Number::powmod
