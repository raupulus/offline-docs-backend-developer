---
title: array_keys
description: Devuelve todas las claves o un conjunto de las claves de un array
source_url: https://www.php.net/manual/es/function.array-keys.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-keys.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 5414f7297
order: 5420
---

array_keys

Devuelve todas las claves o un conjunto de las claves de un array

## Descripción

```php
array_keys(array $array): array
```php

```php
array_keys(array $array, mixed $filter_value, [bool $strict]): array
```

`array_keys` devuelve las claves numéricas y literales del array `array`.

Si se especifica un valor de búsqueda `filter_value`, solo se devolverán las claves que contengan este valor. De lo contrario, se devolverán todas las claves de `array`.

## Parámetros

`array`  
Un array que contiene las claves a devolver.

`filter_value`  
Si se especifica, solo se devolverán las claves que contengan estos valores.

`strict`  
El argumento `strict` fuerza la comparación en modo estricto, incluyendo el tipo, con el operador ===.

## Valores devueltos

Devuelve un array de todas las claves en `array`.

## Ejemplos

Ejemplo con `array_keys`

```php
<?php
$array = array(0 => 100, "color" => "red");
print_r(array_keys($array));

$array = array("blue", "red", "green", "blue", "blue");
print_r(array_keys($array, "blue"));

$array = array("color" => array("blue", "red", "green"),
               "size"  => array("small", "medium", "large"));
print_r(array_keys($array));
?>

    
```

El ejemplo anterior mostrará:

    Array
    (
        [0] => 0
        [1] => color
    )
    Array
    (
        [0] => 0
        [1] => 3
        [2] => 4
    )
    Array
    (
        [0] => color
        [1] => size
    )

## Véase también

`array_values`, `array_combine`, `array_key_exists`, `array_search`
