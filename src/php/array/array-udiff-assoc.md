---
title: array_udiff_assoc
description: Calcula la diferencia entre arrays con verificación de índices, compara
  los datos con una función de retrollamada
source_url: https://www.php.net/manual/es/function.array-udiff-assoc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-udiff-assoc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: 56509d07a
order: 5620
---

array_udiff_assoc

Calcula la diferencia entre arrays con verificación de índices, compara los datos con una función de retrollamada

## Descripción

```php
array_udiff_assoc(array $array, array ...$arrays, callable $value_compare_func): array
```php

Calcula la diferencia entre arrays con verificación de índices, compara los datos con una función de retrollamada.

> [!NOTE]
> Tenga en cuenta que esta función solo verifica una dimensión de un array multidimensional. Por supuesto, se puede probar una dimensión particular utilizando, por ejemplo, `array_udiff_assoc($array1[1], $array2[1], "compare_func");`.

## Parámetros

`array`  
El primer array.

`arrays`  
Arrays a comparar contra

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

## Valores devueltos

`array_udiff_assoc` devuelve un array que contiene todos los valores de `array` que no están presentes en ninguno de los otros argumentos. Tenga en cuenta que las claves se utilizan en las comparaciones a diferencia de `array_diff` y `array_udiff`. La comparación de datos se realiza utilizando una función de retrollamada proporcionada por el usuario, `data_compare_func`. Este comportamiento es diferente al de `array_diff_assoc` que utiliza una función de comparación interna.

## Ejemplos

Ejemplo con `array_udiff_assoc`

```php
<?php
class cr {
    private $priv_member;
    function __construct($val)
    {
        $this->priv_member = $val;
    }

    static function comp_func_cr($a, $b)
    {
        if ($a->priv_member === $b->priv_member) return 0;
        return ($a->priv_member > $b->priv_member)? 1:-1;
    }
}

$a = array("0.1" => new cr(9), "0.5" => new cr(12), 0 => new cr(23), 1=> new cr(4), 2 => new cr(-15),);
$b = array("0.2" => new cr(9), "0.5" => new cr(22), 0 => new cr(3), 1=> new cr(4), 2 => new cr(-15),);

$result = array_udiff_assoc($a, $b, array("cr", "comp_func_cr"));
print_r($result);
?>

    
```

El ejemplo anterior mostrará:

    Array
    (
        [0.1] => cr Object
            (
                [priv_member:private] => 9
            )

        [0.5] => cr Object
            (
                [priv_member:private] => 12
            )

        [0] => cr Object
            (
                [priv_member:private] => 23
            )
    )

En nuestro ejemplo, se puede ver que la pareja `"1" => new cr(4)` está presente en ambos arrays y, por lo tanto, está ausente en el array resultante.

## Véase también

`array_diff`, `array_diff_assoc`, `array_diff_uassoc`, `array_udiff`, `array_udiff_uassoc`, `array_intersect`, `array_intersect_assoc`, `array_uintersect`, `array_uintersect_assoc`, `array_uintersect_uassoc`
