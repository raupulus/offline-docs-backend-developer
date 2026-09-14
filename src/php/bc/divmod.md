---
title: BcMath\Number::divmod
description: Devuelve el cociente y el módulo de un número de precisión arbitraria
source_url: https://www.php.net/manual/es/bcmath-number.divmod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/bcmath/number/divmod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: 6fdd8cf86
order: 6080
---

BcMath\Number::divmod

Devuelve el cociente y el módulo de un número de precisión arbitraria

## Descripción

```php
public BcMath\Number::divmod(BcMath\Number $num, [int $scale]): array
```php

Devuelve el cociente y el módulo de la división de `$this` por `num`.

## Valores devueltos

Devuelve un `array` indexado donde el primer elemento es el cociente en forma de un nuevo objeto `BcMath\Number` y el segundo elemento es el módulo en forma de un nuevo objeto `BcMath\Number`.

El cociente es siempre un valor entero, por lo que BcMath\Number::scale del cociente será siempre `0`, independientemente de si `scale` es explícitamente especificado.

Si `scale` es explícitamente especificado, BcMath\Number::scale del módulo será el valor especificado. Cuando el BcMath\Number::scale del objeto de módulo del resultado es definido automáticamente, el mayor BcMath\Number::scale de los dos números utilizados para la operación de módulo es utilizado.

Es decir, si los BcMath\Number::scales de dos valores son `2` y `5` respectivamente, el BcMath\Number::scale del módulo será `5`.

## Errores/Excepciones

## Ejemplos

Ejemplo de BcMath\Number::divmod cuando `scale` no es especificado

```
<?php
echo '8.3 / 2.22' . PHP_EOL;
[$quot, $rem] = new BcMath\Number('8')->divmod(new BcMath\Number('2.22'));
var_dump($quot, $rem);

echo PHP_EOL . '8.3 / 8.3' . PHP_EOL;
[$quot, $rem] = new BcMath\Number('8.3')->divmod('8.3');
var_dump($quot, $rem);

echo PHP_EOL . '10 / -3' . PHP_EOL;
[$quot, $rem] = new BcMath\Number('10')->divmod(-3);
var_dump($quot, $rem);
?>

   
```php

El ejemplo anterior mostrará:

    8.3 / 2.22
    object(BcMath\Number)#3 (2) {
      ["value"]=>
      string(1) "3"
      ["scale"]=>
      int(0)
    }
    object(BcMath\Number)#4 (2) {
      ["value"]=>
      string(4) "1.34"
      ["scale"]=>
      int(2)
    }

    8.3 / 8.3
    object(BcMath\Number)#2 (2) {
      ["value"]=>
      string(1) "1"
      ["scale"]=>
      int(0)
    }
    object(BcMath\Number)#5 (2) {
      ["value"]=>
      string(3) "0.0"
      ["scale"]=>
      int(1)
    }

    10 / -3
    object(BcMath\Number)#3 (2) {
      ["value"]=>
      string(2) "-3"
      ["scale"]=>
      int(0)
    }
    object(BcMath\Number)#1 (2) {
      ["value"]=>
      string(1) "1"
      ["scale"]=>
      int(0)
    }

Ejemplo de BcMath\Number::divmod especificando `scale` explícitamente

```
<?php
echo '8.3 / 2.22' . PHP_EOL;
[$quot, $rem] = new BcMath\Number('8')->divmod(new BcMath\Number('2.22'), 1);
var_dump($quot, $rem);

echo PHP_EOL . '8.3 / 8.3' . PHP_EOL;
[$quot, $rem] = new BcMath\Number('8.3')->divmod('8.3', 4);
var_dump($quot, $rem);

echo PHP_EOL . '10 / -3' . PHP_EOL;
[$quot, $rem] = new BcMath\Number('10')->divmod(-3, 5);
var_dump($quot, $rem);
?>

   
```php

El ejemplo anterior mostrará:

    8.3 / 2.22
    object(BcMath\Number)#3 (2) {
      ["value"]=>
      string(1) "3"
      ["scale"]=>
      int(0)
    }
    object(BcMath\Number)#4 (2) {
      ["value"]=>
      string(3) "1.3"
      ["scale"]=>
      int(1)
    }

    8.3 / 8.3
    object(BcMath\Number)#2 (2) {
      ["value"]=>
      string(1) "1"
      ["scale"]=>
      int(0)
    }
    object(BcMath\Number)#5 (2) {
      ["value"]=>
      string(6) "0.0000"
      ["scale"]=>
      int(4)
    }

    10 / -3
    object(BcMath\Number)#3 (2) {
      ["value"]=>
      string(2) "-3"
      ["scale"]=>
      int(0)
    }
    object(BcMath\Number)#1 (2) {
      ["value"]=>
      string(7) "1.00000"
      ["scale"]=>
      int(5)
    }

## Véase también

bcdivmod

BcMath\Number::div

BcMath\Number::mod
