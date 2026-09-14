---
title: array_flip
description: Reemplaza las claves por los valores, y los valores por las claves
source_url: https://www.php.net/manual/es/function.array-flip.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-flip.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: 8a7836bf8
order: 5320
---

array_flip

Reemplaza las claves por los valores, y los valores por las claves

## Descripción

```php
array_flip(array $array): array
```php

`array_flip` devuelve un `array` invertido, es decir, las claves de `array` se convierten en valores y los valores de `array` se convierten en claves.

Téngase en cuenta que los valores de `array` deben ser claves válidas, es decir, deben ser `int` o `string`. Se emitirá una alerta si un valor es de un tipo que no es adecuado y la pareja en cuestión *no será incluida en el resultado*.

Si un valor no es único, solo la última clave será utilizada como valor, y todas las demás se perderán.

## Parámetros

`array`  
Un array de pares clave/valor a invertir.

## Valores devueltos

Devuelve un array invertido.

## Ejemplos

Ejemplo con `array_flip`

```
<?php
$input = array("oranges", "apples", "pears");
$flipped = array_flip($input);

print_r($flipped);
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [oranges] => 0
        [apples] => 1
        [pears] => 2
    )

Ejemplo con `array_flip` : colisión

```
<?php
$input = array("a" => 1, "b" => 1, "c" => 2);
$flipped = array_flip($input);

print_r($flipped);
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [1] => b
        [2] => c
    )

## Véase también

`array_values`, `array_keys`, `array_reverse`
