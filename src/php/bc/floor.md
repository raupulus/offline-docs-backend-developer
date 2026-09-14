---
title: BcMath\Number::floor
description: Redondea hacia abajo un número de precisión arbitraria
source_url: https://www.php.net/manual/es/bcmath-number.floor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/bcmath/number/floor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: c7e83fbbb
order: 6090
---

BcMath\Number::floor

Redondea hacia abajo un número de precisión arbitraria

## Descripción

```php
public BcMath\Number::floor(): BcMath\Number
```php

Devuelve el valor entero inferior siguiente redondeando hacia abajo `$this` si es necesario.

## Parámetros

Esta función no contiene ningún parámetro.

## Ejemplos

Ejemplo de BcMath\Number::floor

```
<?php
$num1 = new BcMath\Number('4.3')->floor();
$num2 = new BcMath\Number('9.999')->floor();
$num3 = new BcMath\Number('-3.14')->floor();

var_dump($num1, $num2, $num3);
?>

   
```php

El ejemplo anterior mostrará:

    object(BcMath\Number)#2 (2) {
      ["value"]=>
      string(1) "4"
      ["scale"]=>
      int(0)
    }
    object(BcMath\Number)#3 (2) {
      ["value"]=>
      string(1) "9"
      ["scale"]=>
      int(0)
    }
    object(BcMath\Number)#4 (2) {
      ["value"]=>
      string(2) "-4"
      ["scale"]=>
      int(0)
    }

## Véase también

bcfloor

BcMath\Number::ceil

BcMath\Number::round
