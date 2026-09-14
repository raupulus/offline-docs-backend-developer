---
title: array_replace
description: Sustituye los elementos de un array por los de otros arrays
source_url: https://www.php.net/manual/es/function.array-replace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-replace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: 5cc10e8d9
order: 5550
---

array_replace

Sustituye los elementos de un array por los de otros arrays

## Descripción

```php
array_replace(array $array, array ...$replacements): array
```php

`array_replace` crea un nuevo array y asigna elementos para cada clave en cada uno de los arrays proporcionados. Si una clave aparece en varios arrays de entrada, se utilizará el valor del array de entrada más a la derecha.

`array_replace` no trata los elementos de manera recursiva, sustituye el valor entero para cada clave cuando realiza una sustitución.

## Parámetros

`array`  
El array en el que se sustituyen los elementos.

`replacements`  
Arrays desde los cuales se extraerán los elementos. Los valores de los arrays futuros sobrescribirán los valores anteriores.

## Valores devueltos

Devuelve un `array`.

## Ejemplos

Ejemplo con `array_replace`

```
<?php
$base = array("orange", "banana", "apple", "raspberry");
$replacements = array(0 => "pineapple", 4 => "cherry");
$replacements2 = array(0 => "grape");

$basket = array_replace($base, $replacements, $replacements2);
var_dump($basket);
?>

    
```php

El ejemplo anterior mostrará:

```
array(5) {
  [0]=>
  string(5) "grape"
  [1]=>
  string(6) "banana"
  [2]=>
  string(5) "apple"
  [3]=>
  string(9) "raspberry"
  [4]=>
  string(6) "cherry"
}

    
```php

Ejemplo de cómo se manejan los arrays anidados

```
<?php
$base = [ 'citrus' => [ 'orange', 'lemon' ], 'pome' => [ 'apple' ] ];
$replacements = [ 'citrus' => [ 'grapefruit' ] ];
$replacements2 = [ 'citrus' => [ 'kumquat', 'citron' ], 'pome' => [ 'loquat' ] ];

$basket = array_replace($base, $replacements, $replacements2);
var_dump($basket);
?>

    
```php

El ejemplo anterior mostrará:

```
array(2) {
  ["citrus"]=>
  array(2) {
    [0]=>
    string(7) "kumquat"
    [1]=>
    string(6) "citron"
  }
  ["pome"]=>
  array(1) {
    [0]=>
    string(6) "loquat"
  }
}

    
```php

## Véase también

`array_replace_recursive`, `array_merge`
