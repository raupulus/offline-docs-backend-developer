---
title: array_fill
description: Rellena un array con un mismo valor
source_url: https://www.php.net/manual/es/function.array-fill.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-fill.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 2e60c5134
order: 5270
---

array_fill

Rellena un array con un mismo valor

## Descripción

```php
array_fill(int $start_index, int $count, mixed $value): array
```php

Crea un array con `count` entradas, todas con el valor `value`. Los índices comienzan con el valor `start_index`.

## Parámetros

`start_index`  
El primer índice del array devuelto.

Si `start_index` es negativo, el primer índice del array devuelto será `start_index`, seguido por índices comenzando en cero en versiones anteriores a PHP 8.0.0 ; a partir de PHP 8.0.0, los índices negativos se incrementan normalmente. (ver el '[ejemplo](#function.array-fill.example.negative-start-index)).

`count`  
Número de elementos a insertar. Debe ser superior o igual a cero, e inferior o igual a `2147483647`.

`value`  
Valor a utilizar para rellenar el array

## Valores devueltos

Devuelve el array rellenado.

## Errores/Excepciones

Lanza una excepción `ValueError` si `count` está fuera del rango permitido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | La función `array_fill` lanza ahora una `ValueError` si `count` está fuera del rango permitido; anteriormente se emitía una advertencia de nivel `E_WARNING` y la función devolvía `false`. |

## Ejemplos

Ejemplo con `array_fill`

```
<?php
$a = array_fill(5, 6, 'banana');
print_r($a);
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [5]  => banana
        [6]  => banana
        [7]  => banana
        [8]  => banana
        [9]  => banana
        [10] => banana
    )

Ejemplo de `array_fill` con un índice de inicio negativo

```
<?php
$a = array_fill(-2, 4, 'pear');
print_r($a);
?>

    
```php

Resultado del ejemplo anterior en PHP 8:

    Array
    (
        [-2] => pear
        [-1] => pear
        [0] => pear
        [1] => pear
    )

        

Resultado del ejemplo anterior en PHP 7:

    Array
    (
        [-2] => pear
        [0] => pear
        [1] => pear
        [2] => pear
    )

Observe que el índice `-1` no estaba presente antes de PHP 8.0.0.

## Notas

Ver también la sección del manual sobre los [arrays](#language.types.array) para más información sobre las claves negativas.

## Véase también

`array_fill_keys`, `str_repeat`, `range`
