---
title: array_chunk
description: Divide un array en arrays de menor tamaño
source_url: https://www.php.net/manual/es/function.array-chunk.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-chunk.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: 214519fdb
order: 5170
---

array_chunk

Divide un array en arrays de menor tamaño

## Descripción

```php
array_chunk(array $array, int $length, [bool $preserve_keys]): array
```php

Divide el array `array` en varios arrays conteniendo `length` elementos. Es posible que el último array contenga menos valores.

## Parámetros

`array`  
El array a tratar

`length`  
El tamaño de cada array

`preserve_keys`  
Cuando se define como `true`, las claves serán preservadas. Por omisión, vale `false` lo que reindexará el array resultante numéricamente

## Valores devueltos

Devuelve un array multidimensional indexado numéricamente, comenzando en cero, cuyas dimensiones contienen `length` elementos.

## Errores/Excepciones

Si `length` es menor que `1`, se lanza una `ValueError`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Si `length` es menor que `1`, se lanza una `ValueError`; anteriormente, se generaba un error de nivel `E_WARNING` y la función devolvía `null`. |

## Ejemplos

Ejemplo con `array_chunk`

```
<?php
$input_array = array('a', 'b', 'c', 'd', 'e');
print_r(array_chunk($input_array, 2));
print_r(array_chunk($input_array, 2, true));
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => Array
            (
                [0] => a
                [1] => b
            )

        [1] => Array
            (
                [0] => c
                [1] => d
            )

        [2] => Array
            (
                [0] => e
            )

    )
    Array
    (
        [0] => Array
            (
                [0] => a
                [1] => b
            )

        [1] => Array
            (
                [2] => c
                [3] => d
            )

        [2] => Array
            (
                [4] => e
            )

    )

## Véase también

`array_slice`
