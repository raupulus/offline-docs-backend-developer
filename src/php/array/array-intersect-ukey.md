---
title: array_intersect_ukey
description: Calcula la intersección de dos arrays utilizando una función de retrollamada
  sobre las claves para la comparación
source_url: https://www.php.net/manual/es/function.array-intersect-ukey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-intersect-ukey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: 2226ad08f
order: 5360
---

array_intersect_ukey

Calcula la intersección de dos arrays utilizando una función de retrollamada sobre las claves para la comparación

## Descripción

```php
array_intersect_ukey(array $array, array ...$arrays, callable $key_compare_func): array
```php

`array_intersect_ukey` devuelve un array que contiene todas las valores del array `array` que contienen claves presentes en todos los argumentos.

## Parámetros

`array`  
Array inicial para la comparación de arrays.

`arrays`  
Arrays a comparar.

`key_compare_func`  
La función de comparación debe retornar un entero menor que, igual a, o mayor que 0 si el primer argumento es considerado, respectivamente, menor que, igual a, o mayor que el segundo.

```php
callback(mixed $a, mixed $b): int
```

> [!CAUTION]
> Devolver valores *no enteros* (como `float`) desde la función de comparación resultará en una conversión interna del valor de retorno de la retrollamada a `int`. Así, valores como `0.99` y `0.1` serán convertidos ambos al valor entero `0`, por lo que se compararán como iguales.

## Valores devueltos

Devuelve los valores del array `array` cuyas claves existen en todos los argumentos.

## Ejemplos

Ejemplo con `array_intersect_ukey`

```php
<?php
function key_compare_func($key1, $key2)
{
    if ($key1 == $key2)
        return 0;
    else if ($key1 > $key2)
        return 1;
    else
        return -1;
}

$array1 = array('blue'  => 1, 'red'  => 2, 'green'  => 3, 'purple' => 4);
$array2 = array('green' => 5, 'blue' => 6, 'yellow' => 7, 'cyan'   => 8);

var_dump(array_intersect_ukey($array1, $array2, 'key_compare_func'));
?>

    
```

El ejemplo anterior mostrará:

    array(2) {
      ["blue"]=>
      int(1)
      ["green"]=>
      int(3)
    }

En este ejemplo, se puede ver que solo las claves `'blue'` y `'green'` están presentes en ambos arrays y, por lo tanto, son devueltas. Note también que los valores para las claves `'blue'` y `'green'` difieren entre los dos arrays. No obstante, aún coinciden porque solo las claves son verificadas. Los valores devueltos son los del array `array`.

## Véase también

`array_diff`, `array_udiff`, `array_diff_assoc`, `array_diff_uassoc`, `array_udiff_assoc`, `array_udiff_uassoc`, `array_diff_key`, `array_diff_ukey`, `array_intersect`, `array_intersect_assoc`, `array_intersect_uassoc`, `array_intersect_key`
