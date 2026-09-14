---
title: array_intersect_uassoc
description: Calcula la intersección de dos arrays con pruebas en los índices, compara
  los índices utilizando una función de retrollamada
source_url: https://www.php.net/manual/es/function.array-intersect-uassoc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-intersect-uassoc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: 2226ad08f
order: 5350
---

array_intersect_uassoc

Calcula la intersección de dos arrays con pruebas en los índices, compara los índices utilizando una función de retrollamada

## Descripción

```php
array_intersect_uassoc(array $array, array ...$arrays, callable $key_compare_func): array
```php

`array_intersect_uassoc` devuelve un array conteniendo todos los valores del array `array` que están presentes en todos los argumentos. Note que las claves son utilizadas en la comparación en oposición a la función `array_intersect`.

## Parámetros

`array`  
Array inicial para la comparación de los otros arrays.

`arrays`  
Arrays a comparar contra

`key_compare_func`  
La función de comparación debe retornar un entero menor que, igual a, o mayor que 0 si el primer argumento es considerado, respectivamente, menor que, igual a, o mayor que el segundo.

```php
callback(mixed $a, mixed $b): int
```

> [!CAUTION]
> Devolver valores *no enteros* (como `float`) desde la función de comparación resultará en una conversión interna del valor de retorno de la retrollamada a `int`. Así, valores como `0.99` y `0.1` serán convertidos ambos al valor entero `0`, por lo que se compararán como iguales.

## Valores devueltos

Devuelve los valores del array `array` cuyos valores existen en todos los otros argumentos.

## Ejemplos

Ejemplo con `array_intersect_uassoc`

```php
<?php
$array1 = array("a" => "green", "b" => "brown", "c" => "blue", "red");
$array2 = array("a" => "GREEN", "B" => "brown", "yellow", "red");

print_r(array_intersect_uassoc($array1, $array2, "strcasecmp"));
?>

    
```

El ejemplo anterior mostrará:

    Array
    (
        [b] => brown
    )

## Véase también

`array_intersect`, `array_intersect_assoc`, `array_uintersect_assoc`, `array_uintersect_uassoc`, `array_intersect_key`, `array_intersect_ukey`
