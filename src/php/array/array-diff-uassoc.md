---
title: array_diff_uassoc
description: Calcula la diferencia entre dos arrays asociativos, utilizando una función
  de retrollamada
source_url: https://www.php.net/manual/es/function.array-diff-uassoc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-diff-uassoc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 6b64170da
order: 5230
---

array_diff_uassoc

Calcula la diferencia entre dos arrays asociativos, utilizando una función de retrollamada

## Descripción

```php
array_diff_uassoc(array $array, array ...$arrays, callable $key_compare_func): array
```php

Se compara el array `array` con los arrays `arrays` y se devuelve la diferencia. A diferencia de la función `array_diff`, las claves del array son utilizadas en la comparación.

A diferencia de la función `array_diff_assoc`, un usuario proporciona una función de retrollamada utilizada para la comparación de los índices, y no una función interna.

## Parámetros

`array`  
El array a comparar

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

Devuelve un `array` que contiene todas las entradas del array `array` que no están presentes en ningún otro array.

## Ejemplos

Ejemplo con `array_diff_uassoc`

En este ejemplo, la pareja `"a" => "green"` está presente en los dos arrays, y por lo tanto, no está presente en el resultado de la función. Por el contrario, la pareja `0 => "red"` está presente en el resultado, ya que la clave de `"red"` es automáticamente asignada a `0` en el primer array, mientras que es asignada a `1` en el segundo array, ya que la clave `0` ya está asignada a `yellow`.

```php
<?php
function key_compare_func($a, $b)
{
    return $a <=> $b;
}

$array1 = array("a" => "green", "b" => "brown", "c" => "blue", "red");
$array2 = array("a" => "green", "yellow", "red");
$result = array_diff_uassoc($array1, $array2, "key_compare_func");
print_r($result);
?>

    
```

El ejemplo anterior mostrará:

    Array
    (
        [b] => brown
        [c] => blue
        [0] => red
    )

        

La igualdad de dos índices es verificada por la función del usuario.

## Notas

> [!NOTE]
> Esta función solo verifica una dimensión de un array multidimensional. Es posible verificar subdimensiones utilizando, por ejemplo, `array_diff_uassoc($array1[1], $array2[1], "key_compare_func");`.

## Véase también

`array_diff`, `array_diff_assoc`, `array_udiff`, `array_udiff_assoc`, `array_udiff_uassoc`, `array_intersect`, `array_intersect_assoc`, `array_uintersect`, `array_uintersect_assoc`, `array_uintersect_uassoc`
