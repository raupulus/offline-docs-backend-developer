---
title: array_diff_ukey
description: Calcula la diferencia entre dos arrays utilizando una función de retrollamada
  sobre las claves para comparación
source_url: https://www.php.net/manual/es/function.array-diff-ukey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-diff-ukey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: 2226ad08f
order: 5240
---

array_diff_ukey

Calcula la diferencia entre dos arrays utilizando una función de retrollamada sobre las claves para comparación

## Descripción

```php
array_diff_ukey(array $array, array ...$arrays, callable $key_compare_func): array
```php

Compara las claves del array `array` con las de los arrays `arrays` y devuelve la diferencia. Esta función es idéntica a la función `array_diff`, excepto que la comparación se realiza sobre las claves, en lugar de sobre los valores.

A diferencia de la función `array_diff_key`, se proporciona una función de usuario para la comparación de índices, y no una función interna.

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

Ejemplo con `array_diff_ukey`

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

var_dump(array_diff_ukey($array1, $array2, 'key_compare_func'));
?>

    
```

El ejemplo anterior mostrará:

    array(2) {
      ["red"]=>
      int(2)
      ["purple"]=>
      int(4)
    }

## Notas

> [!NOTE]
> Se debe tener en cuenta que esta función verifica únicamente una dimensión de un array que posee n dimensiones. Por supuesto, se puede verificar una dimensión más profunda utilizando, por ejemplo, `array_diff_ukey($array1[0], $array2[0], 'callback_func');`.

## Véase también

`array_diff`, `array_udiff`, `array_diff_assoc`, `array_diff_uassoc`, `array_udiff_assoc`, `array_udiff_uassoc`, `array_diff_key`, `array_intersect`, `array_intersect_assoc`, `array_intersect_uassoc`, `array_intersect_key`, `array_intersect_ukey`
