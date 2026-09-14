---
title: array_pad
description: Completa un array con un valor hasta la longitud especificada
source_url: https://www.php.net/manual/es/function.array-pad.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-pad.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: 2e60c5134
order: 5480
---

array_pad

Completa un array con un valor hasta la longitud especificada

## Descripción

```php
array_pad(array $array, int $length, mixed $value): array
```php

`array_pad` devuelve una copia del array `array` completado hasta el tamaño de `length` con el valor `value`. Si `length` es positivo, entonces el array se completa a la derecha, si es negativo, se completa a la izquierda. Si el valor absoluto de `length` es más pequeño que el tamaño del array `array`, entonces el array no se completa.

## Parámetros

`array`  
Array inicial de valores a completar.

`length`  
Nueva longitud del array.

`value`  
Valor a insertar si el argumento `array` es más pequeño que el argumento `length`.

## Valores devueltos

Devuelve una copia del array `array` completado hasta el tamaño de `length` con el valor `value`. Si `length` es positivo, entonces el array se completa a la derecha, si es negativo, se completa a la izquierda. Si el valor absoluto de `length` es más pequeño que el tamaño del array `array`, entonces el array no se completa.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Antes de la versión 8.3, solo podían añadirse 1048576 elementos a la vez. Ahora, esto está limitado únicamente por el tamaño máximo de un array. |

## Ejemplos

Ejemplo con `array_pad`

```
<?php
$input = array(12, 10, 9);

$result = array_pad($input, 5, 0);
// El resultado es : array(12, 10, 9, 0, 0)
echo join(', ', $result), PHP_EOL;

$result = array_pad($input, -7, -1);
// El resultado es : array(-1, -1, -1, -1, 12, 10, 9)
echo join(', ', $result), PHP_EOL;

$result = array_pad($input, 2, "noop");
// no se completa
echo join(', ', $result), PHP_EOL;
?>

    
```php

## Véase también

`array_fill`, `range`
