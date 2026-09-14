---
title: array_diff_assoc
description: Calcula la diferencia de dos arrays, teniendo en cuenta las claves
source_url: https://www.php.net/manual/es/function.array-diff-assoc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-diff-assoc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: 6b64170da
order: 5210
---

array_diff_assoc

Calcula la diferencia de dos arrays, teniendo en cuenta las claves

## Descripción

```php
array_diff_assoc(array $array, array ...$arrays): array
```php

Compara `array` con los arrays `arrays` y devuelve la diferencia. A diferencia de la función `array_diff`, las claves del array también se utilizan en la comparación.

## Parámetros

`array`  
El array a comparar

`arrays`  
Arrays a comparar contra

## Valores devueltos

Devuelve un `array` que contiene todos los valores del array `array` que no están presentes en los otros arrays.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función puede ser llamada ahora con un solo parámetro. Anteriormente, al menos dos parámetros eran necesarios. |

## Ejemplos

Ejemplo con `array_diff_assoc`

En este ejemplo, el par `"a" => "green"` está presente en ambos arrays, y por lo tanto, no está presente en el resultado de la función. Por el contrario, el par `0 => "red"` está presente en el resultado, ya que la clave de `"red"` es automáticamente asignada a `0` en el primer array, mientras que es asignada a `1` en el segundo array, ya que la clave `0` ya está asignada a `yellow`.

```
<?php
$array1 = array("a" => "green", "b" => "brown", "c" => "blue", "red");
$array2 = array("a" => "green", "yellow", "red");
$result = array_diff_assoc($array1, $array2);
print_r($result);
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [b] => brown
        [c] => blue
        [0] => red
    )

Ejemplo con `array_diff_assoc`

Dos valores de los pares *clave =\> valor* se consideran iguales solo si `(string) $elem1 === (string) $elem2`. En otras palabras, se realiza una verificación estricta en la representación en strings.

```
<?php
$array1 = array(0, 1, 2);
$array2 = array("00", "01", "2");
$result = array_diff_assoc($array1, $array2);
print_r($result);
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => 0
        [1] => 1
    )

## Notas

> [!NOTE]
> Esta función solo verifica una dimensión de un array multidimensional. Es posible verificar subdimensiones utilizando, por ejemplo, `array_diff_assoc($array1[0], $array2[0]);`.

> [!NOTE]
> Es necesario asegurarse de que los argumentos se proporcionen en el orden correcto al comparar arrays similares con más claves. El nuevo array debe ser el primero de la lista.

## Véase también

`array_diff`, `array_diff_uassoc`, `array_udiff_assoc`, `array_udiff_uassoc`, `array_intersect`, `array_intersect_assoc`
