---
title: array_intersect
description: Calcula la intersección de arrays
source_url: https://www.php.net/manual/es/function.array-intersect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-intersect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: c84024092
order: 5370
---

array_intersect

Calcula la intersección de arrays

## Descripción

```php
array_intersect(array $array, array ...$arrays): array
```php

`array_intersect` devuelve un array conteniendo todos los valores de `array` que están presentes en todos los otros argumentos. Téngase en cuenta que las claves son preservadas.

## Parámetros

`array`  
El array conteniendo los valores maestros a verificar.

`arrays`  
Arrays a comparar contra

## Valores devueltos

Devuelve un array conteniendo todos los valores del array `array` cuyos valores existen en todos los argumentos.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función puede ser llamada ahora con un solo parámetro. Anteriormente, al menos dos parámetros eran necesarios. |

## Ejemplos

Ejemplo con `array_intersect`

```
<?php
$array1 = array("a" => "green", "red", "blue");
$array2 = array("b" => "green", "yellow", "red");
$result = array_intersect($array1, $array2);
print_r($result);
?>

    
```php

El ejemplo anterior mostrará:

```
Array
(
    [a] => green
    [0] => red
)

    
```php

## Notas

> [!NOTE]
> Dos elementos son considerados iguales si y solo si `(string) $elem1 === (string) $elem2`. En claro: cuando la representación en string es idéntica.

## Véase también

`array_intersect_assoc`, `array_diff`, `array_diff_assoc`
