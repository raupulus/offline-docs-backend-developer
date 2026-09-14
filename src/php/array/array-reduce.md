---
title: array_reduce
description: Reduce itérativemente un array
source_url: https://www.php.net/manual/es/function.array-reduce.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-reduce.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: 31cacb6f2
order: 5530
---

array_reduce

Reduce itérativemente un array

## Descripción

```php
array_reduce(array $array, callable $callback, [mixed $initial]): mixed
```php

`array_reduce` aplica itérativemente la función `callback` a los elementos del array `array`, de manera que se reduce el array a un valor simple.

## Parámetros

`array`  
El array de entrada.

`callback`  
```php
callback(mixed $carry, mixed $item): mixed
```

`carry`  
Contiene el valor devuelto de la iteración previa; en el caso de la primera iteración, será el valor del parámetro `initial`.

`item`  
Contiene el valor de la iteración actual.

`initial`  
Si el argumento opcional `initial` está disponible, será utilizado para inicializar el proceso, o bien como valor final si el array está vacío.

## Valores devueltos

Devuelve el valor resultante.

Si el array está vacío y el parámetro `initial` no es pasado, `array_reduce` devuelve `null`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Si `callback` espera un parámetro a ser pasado por referencia, esta función emite ahora una `E_WARNING`. |

## Ejemplos

Ejemplo con `array_reduce`

```php
<?php
function sum($carry, $item)
{
    $carry += $item;
    return $carry;
}

function product($carry, $item)
{
    $carry *= $item;
    return $carry;
}

$a = array(1, 2, 3, 4, 5);
$x = array();

var_dump(array_reduce($a, "sum")); // int(15)
var_dump(array_reduce($a, "product", 10)); // int(1200), ya que: 10*1*2*3*4*5
var_dump(array_reduce($x, "sum", "No data to reduce")); // string(17) "No data to reduce"
?>

    
```

## Véase también

`array_filter`, `array_map`, `array_unique`, `array_count_values`
