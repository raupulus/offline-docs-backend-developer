---
title: array_values
description: Devuelve todos los valores de un array
source_url: https://www.php.net/manual/es/function.array-values.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-values.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: d1b2cfcca
order: 5700
---

array_values

Devuelve todos los valores de un array

## Descripción

```php
array_values(array $array): array
```php

`array_values` devuelve los valores del array `array` y los indexa de forma numérica.

## Parámetros

`array`  
El array.

## Valores devueltos

Devuelve un array de valores indexado.

## Ejemplos

Ejemplo con `array_values`

```
<?php
$array = array("size" => "XL", "color" => "gold");
print_r(array_values($array));
?>

    
```php

El ejemplo anterior mostrará:

```
Array
(
    [0] => XL
    [1] => gold
)

    
```php

## Véase también

`array_keys`, `array_combine`
