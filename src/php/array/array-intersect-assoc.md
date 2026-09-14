---
title: array_intersect_assoc
description: Calcula la intersección de dos arrays con pruebas sobre los índices
source_url: https://www.php.net/manual/es/function.array-intersect-assoc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-intersect-assoc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: c84024092
order: 5330
---

array_intersect_assoc

Calcula la intersección de dos arrays con pruebas sobre los índices

## Descripción

```php
array_intersect_assoc(array $array, array ...$arrays): array
```php

`array_intersect_assoc` devuelve un array que contiene todos los valores de `array` que también están presentes en todos los otros argumentos. Tenga en cuenta que las claves también se utilizan durante la comparación, a diferencia de `array_intersect`.

## Parámetros

`array`  
El array con los valores maestros a verificar.

`arrays`  
Arrays a comparar

## Valores devueltos

Devuelve un array asociativo que contiene todos los valores del array `array` que están presentes en todos los argumentos.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función puede ser llamada ahora con un solo parámetro. Anteriormente, al menos dos parámetros eran necesarios. |

## Ejemplos

Ejemplo con `array_intersect_assoc`

```
<?php
$array1 = array("a" => "green", "b" => "brown", "c" => "blue", "red");
$array2 = array("a" => "green", "b" => "yellow", "blue", "red");
$result_array = array_intersect_assoc($array1, $array2);
print_r($result_array);
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [a] => green
    )

En nuestro ejemplo, se puede ver que el par `"a" => "green"` está presente en ambos arrays, y por lo tanto se coloca en el último array. El valor `red` no se devuelve porque en `$array1` su índice es `0` mientras que en el array `$array2`, su índice es `1`, y la clave `"b"` no se devuelve, porque su valor es diferente en cada array.

Los dos valores del par `clave => valor` se consideran iguales solo si `(string) $elem1 === (string) $elem2`. En otras palabras, se realiza una comparación estricta en las representaciones de los índices, con el tipo string.

## Véase también

array_intersect

array_uintersect_assoc

array_intersect_uassoc

array_uintersect_uassoc

array_diff

array_diff_assoc
