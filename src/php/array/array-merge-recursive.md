---
title: array_merge_recursive
description: Combina uno o varios arrays juntos, de manera recursiva
source_url: https://www.php.net/manual/es/function.array-merge-recursive.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-merge-recursive.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 9e0f03ac3
order: 5450
---

array_merge_recursive

Combina uno o varios arrays juntos, de manera recursiva

## Descripción

```php
array_merge_recursive(array ...$arrays): array
```php

`array_merge_recursive` reúne los elementos de dos o más arrays juntos, añadiendo los elementos de uno a continuación de los elementos del anterior.

Si los arrays pasados como argumentos tienen las mismas claves (strings), los valores son entonces reunidos en un array, de manera recursiva, de forma que, si uno de estos valores es un array en sí mismo, la función lo reunirá con los valores de la entrada actual. Sin embargo, si dos arrays tienen la misma clave numérica, el último valor no sobrescribirá el anterior, sino que será añadido al final del array.

## Parámetros

`arrays`  
Lista variable de arrays a reunir de manera recursiva.

## Valores devueltos

Un array de valores resultantes de la fusión de los argumentos. Si es llamada sin argumentos, devuelve un `array` vacío.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.4.0 | Esta función puede ahora ser llamada sin parámetros. Anteriormente, al menos un parámetro era requerido. |

## Ejemplos

Ejemplo con `array_merge_recursive`

```
<?php
$ar1 = array("color" => array("favorite" => "red"), 5);
$ar2 = array(10, "color" => array("favorite" => "green", "blue"));
$result = array_merge_recursive($ar1, $ar2);
print_r($result);
?>

    
```php

El ejemplo anterior mostrará:

```
Array
(
    [color] => Array
        (
            [favorite] => Array
                (
                    [0] => red
                    [1] => green
                )

            [0] => blue
        )

    [0] => 5
    [1] => 10
)

    
```php

## Véase también

`array_merge`, `array_replace_recursive`
