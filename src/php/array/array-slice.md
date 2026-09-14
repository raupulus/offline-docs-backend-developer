---
title: array_slice
description: Extrae una porción de array
source_url: https://www.php.net/manual/es/function.array-slice.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-slice.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: cd943f94a
order: 5590
---

array_slice

Extrae una porción de array

## Descripción

```php
array_slice(array $array, int $offset, [int $length], [bool $preserve_keys]): array
```php

`array_slice` devuelve una serie de elementos del array `array` comenzando en el offset `offset` y representando `length` elementos.

## Parámetros

`array`  
El array de entrada.

`offset`  
Si `offset` es no negativo, la secuencia comenzará en esta posición en el array `array`.

Si `offset` es negativo, la secuencia comenzará en la posición `offset`, pero comenzando desde el final del array `array`.

> [!NOTE]
> El parámetro `offset` indica la posición en el array, no la clave.

`length`  
Si `length` es proporcionado y positivo, entonces la secuencia tendrá hasta ese número de elementos.

Si el array es más corto que `length`, entonces solo los elementos del array disponibles estarán presentes.

Si `length` es proporcionado y negativo, entonces la secuencia excluirá ese número de elementos del final del array.

Si es omitido, la secuencia tendrá todo desde la posición `offset` hasta el final de `array`.

`preserve_keys`  
> [!NOTE]
> Por omisión `array_slice` reordenará y reinicializará los índices enteros del array. Este comportamiento puede ser modificado definiendo el parámetro `preserve_keys` a `true`. Las claves en forma de string son siempre conservadas, independientemente de este parámetro.

## Valores devueltos

Devuelve la porción del array. Si la posición es mayor que el tamaño del array, un array vacío es devuelto.

## Ejemplos

Ejemplo con `array_slice`

```
<?php
$input = array("a", "b", "c", "d", "e");

$output = array_slice($input, 2);         // devuelve "c", "d", y "e"
$output = array_slice($input, -2, 1);     // devuelve "d"
$output = array_slice($input, 0, 3);      // devuelve "a", "b", y "c"

// note las claves de índice diferentes
print_r(array_slice($input, 2, -1));
print_r(array_slice($input, 2, -1, true));
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => c
        [1] => d
    )
    Array
    (
        [2] => c
        [3] => d
    )

`array_slice` y basado en un array

```
<?php
$input = array(1 => "a", "b", "c", "d", "e");
print_r(array_slice($input, 1, 2));
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => b
        [1] => c
    )

`array_slice` y array con claves mixtas

```
<?php
$ar = array('a'=>'apple', 'b'=>'banana', '42'=>'pear', 'd'=>'orange');
print_r(array_slice($ar, 0, 3));
print_r(array_slice($ar, 0, 3, true));
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [a] => apple
        [b] => banana
        [0] => pear
    )
    Array
    (
        [a] => apple
        [b] => banana
        [42] => pear
    )

## Véase también

`array_chunk`, `array_splice`, `unset`
