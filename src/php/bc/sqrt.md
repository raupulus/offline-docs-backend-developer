---
title: BcMath\Number::sqrt
description: Devuelve la raíz cuadrada de un número de precisión arbitraria
source_url: https://www.php.net/manual/es/bcmath-number.sqrt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/bcmath/number/sqrt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: a414ee95e
order: 6160
---

BcMath\Number::sqrt

Devuelve la raíz cuadrada de un número de precisión arbitraria

## Descripción

```php
public BcMath\Number::sqrt([int $scale]): BcMath\Number
```php

Devuelve la raíz cuadrada de `$this`.

## Parámetros

## Valores devueltos

Devuelve la raíz cuadrada en forma de un nuevo objeto `BcMath\Number`.

Cuando el BcMath\Number::scale del resultado se define automáticamente, el BcMath\Number::scale de `$this` es utilizado. Sin embargo, en casos tales como la división indivisible, el BcMath\Number::scale del resultado se extiende. La expansión se realiza únicamente si es necesario, hasta un máximo de `+10`. Este comportamiento es similar al de BcMath\Number::div, consulte esto para más detalles.

Es decir, si el BcMath\Number::scale de este objeto es `5`, el BcMath\Number::scale del resultado está entre `5` y `15`.

## Errores/Excepciones

Este método lanza una ValueError en los siguientes casos: `$this` es un valor negativo, `scale` está fuera del rango válido, El BcMath\Number::scale del resultado está fuera del rango válido

## Ejemplos

Ejemplo de BcMath\Number::sqrt

```
<?php
var_dump(
    new BcMath\Number('2')->sqrt(),
    new BcMath\Number('2')->sqrt(3),
    new BcMath\Number('4')->sqrt(),
    new BcMath\Number('4')->sqrt(3),
);
?>

   
```php

El ejemplo anterior mostrará:

    object(BcMath\Number)#2 (2) {
      ["value"]=>
      string(12) "1.4142135623"
      ["scale"]=>
      int(10)
    }
    object(BcMath\Number)#3 (2) {
      ["value"]=>
      string(5) "1.414"
      ["scale"]=>
      int(3)
    }
    object(BcMath\Number)#4 (2) {
      ["value"]=>
      string(1) "2"
      ["scale"]=>
      int(0)
    }
    object(BcMath\Number)#5 (2) {
      ["value"]=>
      string(5) "2.000"
      ["scale"]=>
      int(3)
    }

## Véase también

bcsqrt

BcMath\Number::div

BcMath\Number::pow
