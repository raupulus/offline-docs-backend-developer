---
title: BcMath\Number::powmod
description: Eleva un número de precisión arbitraria, reducido por un módulo especificado
source_url: https://www.php.net/manual/es/bcmath-number.powmod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/bcmath/number/powmod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: 6fdd8cf86
order: 6130
---

BcMath\Number::powmod

Eleva un número de precisión arbitraria, reducido por un módulo especificado

## Descripción

```php
public BcMath\Number::powmod(BcMath\Number $exponent, BcMath\Number $modulus, [int $scale]): BcMath\Number
```php

Utiliza el método rápido de exponentiación para elevar `$this` a la potencia `exponent` en relación con el módulo `modulus`.

## Parámetros

`exponent`  
El exponente, como no negativo e integral (es decir, la escala debe ser cero).

`modulus`  
El módulo, como integral (es decir, la escala debe ser cero).

## Valores devueltos

Devuelve el resultado en forma de un nuevo objeto `BcMath\Number`.

Cuando la propiedad BcMath\Number::scale del resultado se establece automáticamente, se utiliza la mayor BcMath\Number::scale de los tres números utilizados para la operación de módulo.

## Errores/Excepciones

Este método lanza una ValueError en los siguientes casos: `exponent` o `modulus` es un `string` y no es una cadena numérica BCMath bien formada, `$this`, `exponent` o `modulus` tiene una parte fraccionaria, `exponent` es un valor negativo, `scale` está fuera del rango válido

Este método lanza una excepción DivisionByZeroError si `modulus` es `0`.

## Ejemplos

Ejemplo de BcMath\Number::powmod cuando `scale` no está especificado

```
<?php
var_dump(
    new BcMath\Number('8')->powmod(new BcMath\Number('3'), 5),
    new BcMath\Number('-8')->powmod(new BcMath\Number('3'), 5),
    new BcMath\Number('8')->powmod('2', -3),
    new BcMath\Number('-8')->powmod(5, 7),
);
?>

   
```php

El ejemplo anterior mostrará:

    object(BcMath\Number)#3 (2) {
      ["value"]=>
      string(1) "2"
      ["scale"]=>
      int(0)
    }
    object(BcMath\Number)#4 (2) {
      ["value"]=>
      string(2) "-2"
      ["scale"]=>
      int(0)
    }
    object(BcMath\Number)#2 (2) {
      ["value"]=>
      string(1) "1"
      ["scale"]=>
      int(0)
    }
    object(BcMath\Number)#5 (2) {
      ["value"]=>
      string(2) "-1"
      ["scale"]=>
      int(0)
    }

Ejemplo de BcMath\Number::powmod especificando `scale` explícitamente

```
<?php
var_dump(
    new BcMath\Number('8')->powmod(new BcMath\Number('3'), 5, 1),
    new BcMath\Number('-8')->powmod(new BcMath\Number('3'), 5, 2),
    new BcMath\Number('8')->powmod('2', -3, 3),
    new BcMath\Number('-8')->powmod(5, 7, 4),
);
?>

   
```php

El ejemplo anterior mostrará:

    object(BcMath\Number)#3 (2) {
      ["value"]=>
      string(3) "2.0"
      ["scale"]=>
      int(1)
    }
    object(BcMath\Number)#4 (2) {
      ["value"]=>
      string(5) "-2.00"
      ["scale"]=>
      int(2)
    }
    object(BcMath\Number)#2 (2) {
      ["value"]=>
      string(5) "1.000"
      ["scale"]=>
      int(3)
    }
    object(BcMath\Number)#5 (2) {
      ["value"]=>
      string(7) "-1.0000"
      ["scale"]=>
      int(4)
    }

## Véase también

bcpowmod

BcMath\Number::pow

BcMath\Number::mod
