---
title: array_diff_key
description: Calcula la diferencia de dos arrays utilizando las claves para la comparación
source_url: https://www.php.net/manual/es/function.array-diff-key.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-diff-key.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: c84024092
order: 5220
---

array_diff_key

Calcula la diferencia de dos arrays utilizando las claves para la comparación

## Descripción

```php
array_diff_key(array $array, array ...$arrays): array
```php

Compara las claves del array `array` con las claves de los arrays `arrays` y devuelve la diferencia. Esta función es idéntica a la función `array_diff`, excepto en el hecho de que la comparación se realiza sobre las claves, en lugar de sobre los valores.

## Parámetros

`array`  
El array a comparar

`arrays`  
Arrays a comparar contra

## Valores devueltos

Devuelve un `array` que contiene todas las entradas del array `array` cuyas claves están ausentes en todos los otros arrays.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función puede ser llamada ahora con un solo parámetro. Anteriormente, al menos dos parámetros eran necesarios. |

## Ejemplos

Ejemplo con `array_diff_key`

Las dos claves desde los pares `clave => valor` se consideran iguales únicamente si `(string) $clave1 === (string) $clave2`. En otras palabras, se realiza un análisis de tipo estricto, por lo que el tipo debe ser exactamente el mismo.

```
<?php
$array1 = array('blue' => 1, 'red' => 2, 'green' => 3, 'purple' => 4);
$array2 = array('green' => 5, 'yellow' => 7, 'cyan' => 8);

var_dump(array_diff_key($array1, $array2));
?>

    
```php

El ejemplo anterior mostrará:

    array(3) {
      ["blue"]=>
      int(1)
      ["red"]=>
      int(2)
      ["purple"]=>
      int(4)
    }

         

```
<?php
$array1 = array('blue' => 1, 'red'  => 2, 'green' => 3, 'purple' => 4);
$array2 = array('green' => 5, 'yellow' => 7, 'cyan' => 8);
$array3 = array('blue' => 6, 'yellow' => 7, 'mauve' => 8);

var_dump(array_diff_key($array1, $array2, $array3));
?>

    
```php

El ejemplo anterior mostrará:

    array(2) {
      ["red"]=>
      int(2)
      ["purple"]=>
      int(4)
    }

## Notas

> [!NOTE]
> Tenga en cuenta que esta función verifica únicamente una dimensión de un array que posee n dimensiones. Por supuesto, se puede verificar una dimensión más profunda utilizando, por ejemplo, `array_diff_key($array1[0], $array2[0]);`.

## Véase también

`array_diff`, `array_udiff`, `array_diff_assoc`, `array_diff_uassoc`, `array_udiff_assoc`, `array_udiff_uassoc`, `array_diff_ukey`, `array_intersect`, `array_intersect_assoc`, `array_intersect_uassoc`, `array_intersect_key`, `array_intersect_ukey`
