---
title: array_replace_recursive
description: Sustituye recursivamente en el primer array los elementos de los otros
  arrays proporcionados
source_url: https://www.php.net/manual/es/function.array-replace-recursive.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-replace-recursive.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: 0e6f9948f
order: 5540
---

array_replace_recursive

Sustituye recursivamente en el primer array los elementos de los otros arrays proporcionados

## Descripción

```php
array_replace_recursive(array $array, array ...$replacements): array
```php

`array_replace_recursive` sustituye los valores del array `array` con los valores de las mismas claves provenientes de los arrays siguientes. Si una clave del primer array existe en uno de los arrays siguientes, su valor será sustituido. Si la clave no existe en el primer array, será creada. Si la clave solo existe en el primer array, será dejada intacta. Si varios arrays son pasados como argumentos de sustitución, serán tratados en orden.

`array_replace_recursive` es recursiva: si un valor es un array, la misma función de sustitución le será aplicada.

Si el valor en el primer array es escalar, será sustituido por el valor del segundo array, ya sea un escalar o un array. Si los valores del primer y segundo array son ambos arrays, `array_replace_recursive` sustituirá los valores recursivamente.

## Parámetros

`array`  
El array en el cual los elementos son sustituidos.

`replacements`  
Arrays desde los cuales los elementos pueden ser extraídos.

## Valores devueltos

Devuelve un `array`.

## Ejemplos

Ejemplo con `array_replace_recursive`

```
<?php
$base = array('citrus' => array("orange"), 'berries' => array("blackberry", "raspberry"));
$replacements = array('citrus' => array('pineapple'), 'berries' => array('blueberry'));

$basket = array_replace_recursive($base, $replacements);
print_r($basket);

$basket = array_replace($base, $replacements);
print_r($basket);
?>

    
```php

El ejemplo anterior mostrará:

```
Array
(
    [citrus] => Array
        (
            [0] => pineapple
        )

    [berries] => Array
        (
            [0] => blueberry
            [1] => raspberry
        )

)
Array
(
    [citrus] => Array
        (
            [0] => pineapple
        )

    [berries] => Array
        (
            [0] => blueberry
        )

)

    
```php

Ejemplo con `array_replace_recursive` y la recursividad

```
<?php
$base = array('citrus' => array("orange") , 'berries' => array("blackberry", "raspberry"), 'others' => 'banana' );
$replacements = array('citrus' => 'pineapple', 'berries' => array('blueberry'), 'others' => array('litchis'));
$replacements2 = array('citrus' => array('pineapple'), 'berries' => array('blueberry'), 'others' => 'litchis');

$basket = array_replace_recursive($base, $replacements, $replacements2);
print_r($basket);

?>

    
```php

El ejemplo anterior mostrará:

```
Array
(
    [citrus] => Array
        (
            [0] => pineapple
        )

    [berries] => Array
        (
            [0] => blueberry
            [1] => raspberry
        )

    [others] => litchis
)

    
```php

## Véase también

`array_replace`, `array_merge_recursive`
