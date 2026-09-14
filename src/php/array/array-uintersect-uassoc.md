---
title: array_uintersect_uassoc
description: Calcula la intersección de dos arrays con pruebas en el índice, compara
  los datos y los índices de los dos arrays utilizando una función de retrollamada
  separada
source_url: https://www.php.net/manual/es/function.array-uintersect-uassoc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-uintersect-uassoc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: 56509d07a
order: 5660
---

array_uintersect_uassoc

Calcula la intersección de dos arrays con pruebas en el índice, compara los datos y los índices de los dos arrays utilizando una función de retrollamada separada

## Descripción

```php
array_uintersect_uassoc(array $array1, array ...$arrays, callable $value_compare_func, callable $key_compare_func): array
```php

Calcula la intersección de dos arrays con pruebas en el índice, compara los datos y los índices de los dos arrays utilizando una función de retrollamada separada.

## Parámetros

`array1`  
El primer array.

`arrays`  
Arrays adicionales

`value_compare_func`  
La función de comparación debe retornar un entero menor que, igual a, o mayor que 0 si el primer argumento es considerado, respectivamente, menor que, igual a, o mayor que el segundo.

```php
callback(mixed $a, mixed $b): int
```

> [!CAUTION]
> Devolver valores *no enteros* (como `float`) desde la función de comparación resultará en una conversión interna del valor de retorno de la retrollamada a `int`. Así, valores como `0.99` y `0.1` serán convertidos ambos al valor entero `0`, por lo que se compararán como iguales.

> [!CAUTION]
> La función de callback de ordenación debe tratar cualquier valor de cualquier array en cualquier orden, independientemente del orden en el que fueron proporcionados inicialmente. Esto se debe a que cada array individual es ordenado primero antes de ser comparado con otros arrays. Por ejemplo:
>
> ```
> <?php
> $arrayA = ["string", 1];
> $arrayB = [["value" => 1]];
> // $item1 y $item2 pueden ser cualquiera de los siguientes valores : "cadena", 1 o
> ["value" => 1] $compareFunc = static function ($item1,
>     $item2) { $value1 = is_string($item1) ? strlen($item1) : (is_array($item1) ? $item1["value"] :
>     $item1); $value2 = is_string($item2) ? strlen($item2) : (is_array($item2) ? $item2["value"] : $item2);
>     return $value1 <=> $value2;
> };
> ?>
>
>   
> ```

`key_compare_func`  
Función de retrollamada utilizada para la comparación de las claves.

## Valores devueltos

Devuelve un array que contiene todos los valores del array `array` que están presentes en todos los argumentos.

## Ejemplos

Ejemplo con `array_uintersect_uassoc`

```php
<?php
$array1 = array("a" => "green", "b" => "brown", "c" => "blue", "red");
$array2 = array("a" => "GREEN", "B" => "brown", "yellow", "red");

print_r(array_uintersect_uassoc($array1, $array2, "strcasecmp", "strcasecmp"));
?>

    
```

El ejemplo anterior mostrará:

    Array
    (
        [a] => green
        [b] => brown
    )

## Véase también

`array_uintersect`, `array_intersect_assoc`, `array_intersect_uassoc`, `array_uintersect_assoc`
