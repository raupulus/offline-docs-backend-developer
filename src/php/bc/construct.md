---
title: BcMath\Number::__construct
description: Crear un objeto BcMath\Number
source_url: https://www.php.net/manual/es/bcmath-number.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/bcmath/number/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: a414ee95e
order: 6060
---

BcMath\Number::\_\_construct

Crear un objeto BcMath\Number

## Descripción

```php
public BcMath\Number::__construct(string $num)
```php

Crear un objeto `BcMath\Number` a partir de un valor `int` o `string`.

## Parámetros

`num`  
Un valor `int` o `string`. Si `num` es un `int`, la BcMath\Number::scale se define siempre a `0`. Si `num` es un `string`, debe ser un número válido, y la BcMath\Number::scale se define automáticamente analizando el string.

## Errores/Excepciones

Este método lanza una ValueError si `num` es un `string` y no es un string numérico BCMath bien formado.

## Ejemplos

Ejemplo de BcMath\Number::\_\_construct

```
<?php
$num1 = new BcMath\Number(100);
$num2 = new BcMath\Number('-200');
$num3 = new BcMath\Number('300.00');

var_dump($num1, $num2, $num3);
?>

   
```php

El ejemplo anterior mostrará:

    object(BcMath\Number)#1 (2) {
      ["value"]=>
      string(3) "100"
      ["scale"]=>
      int(0)
    }
    object(BcMath\Number)#2 (2) {
      ["value"]=>
      string(4) "-200"
      ["scale"]=>
      int(0)
    }
    object(BcMath\Number)#3 (2) {
      ["value"]=>
      string(6) "300.00"
      ["scale"]=>
      int(2)
    }

## Véase también

BcMath\Number::\_\_serialize

BcMath\Number::\_\_unserialize
