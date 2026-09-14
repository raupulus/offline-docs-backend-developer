---
title: BcMath\Number::ceil
description: Redondea al alza un número de precisión arbitraria
source_url: https://www.php.net/manual/es/bcmath-number.ceil.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/bcmath/number/ceil.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: c7e83fbbb
order: 6040
---

BcMath\Number::ceil

Redondea al alza un número de precisión arbitraria

## Descripción

```php
public BcMath\Number::ceil(): BcMath\Number
```php

Devuelve el valor entero superior redondeando al alza `$this` si es necesario.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el resultado como un nuevo objeto `BcMath\Number`. La BcMath\Number::scale del resultado es siempre `0`.

## Ejemplos

Ejemplo de BcMath\Number::ceil

```
<?php
$num1 = new BcMath\Number('4.3')->ceil();
$num2 = new BcMath\Number('9.999')->ceil();
$num3 = new BcMath\Number('-3.14')->ceil();

var_dump($num1, $num2, $num3);
?>

   
```php

El ejemplo anterior mostrará:

    object(BcMath\Number)#2 (2) {
      ["value"]=>
      string(1) "5"
      ["scale"]=>
      int(0)
    }
    object(BcMath\Number)#3 (2) {
      ["value"]=>
      string(2) "10"
      ["scale"]=>
      int(0)
    }
    object(BcMath\Number)#4 (2) {
      ["value"]=>
      string(2) "-3"
      ["scale"]=>
      int(0)
    }

## Véase también

bcceil

BcMath\Number::floor

BcMath\Number::round
