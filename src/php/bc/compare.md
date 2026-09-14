---
title: BcMath\Number::compare
description: Comparar dos números de precisión arbitraria
source_url: https://www.php.net/manual/es/bcmath-number.compare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/bcmath/number/compare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: c7e83fbbb
order: 6050
---

BcMath\Number::compare

Comparar dos números de precisión arbitraria

## Descripción

```php
public BcMath\Number::compare(BcMath\Number $num, [int $scale]): int
```php

Comparar dos números de precisión arbitraria. Este método se comporta de manera similar al [operador spaceship](#language.operators.comparison).

## Parámetros

`num`  
El valor al que comparar.

`scale`  
Especifica el `scale` a utilizar para la comparación. Si `null`, todos los dígitos son utilizados en la comparación.

## Valores devueltos

Devuelve `0` si los dos números son iguales, `1` si `$this` es mayor que `num`, de lo contrario `-1`.

## Ejemplos

Ejemplo de BcMath\Number::compare cuando `scale` no está especificado

```
<?php
$number = new BcMath\Number('1.234');

var_dump(
    $number->compare(new BcMath\Number('1.234')),
    $number->compare('1.23400'),
    $number->compare('1.23401'),
    $number->compare(1),
);
?>

   
```php

El ejemplo anterior mostrará:

    int(0)
    int(0)
    int(-1)
    int(1)

Ejemplo de BcMath\Number::compare especificando `scale` explícitamente

```
<?php
$number = new BcMath\Number('1.234');

var_dump(
    $number->compare(new BcMath\Number('1.299'), 1),
    $number->compare('1.24', 2),
    $number->compare('1.22', 2),
    $number->compare(1, 0),
);
?>

   
```php

El ejemplo anterior mostrará:

    int(0)
    int(-1)
    int(1)
    int(0)

## Véase también

bccomp
