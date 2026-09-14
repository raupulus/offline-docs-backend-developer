---
title: array_map
description: Aplica una función sobre los elementos de un array
source_url: https://www.php.net/manual/es/function.array-map.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-map.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_revision: 1f5bcc30e
order: 5440
---

array_map

Aplica una función sobre los elementos de un array

## Descripción

```php
array_map(callable $callback, array $array, array ...$arrays): array
```php

`array_map` devuelve un `array` que contiene los resultados de la aplicación de la función de devolución de llamada `callback` al valor correspondiente de `array` (y `arrays` si se proporcionan más arrays) utilizados como argumentos para la función de devolución de llamada. El número de argumentos que la función de devolución de llamada `callback` acepta debe corresponder al número de arrays pasados a `array_map`. Los arrays de entrada adicionales son ignorados. Se lanza una `ArgumentCountError` si se proporciona un número insuficiente de argumentos.

## Parámetros

`callback`  
La función de devolución de llamada de tipo `callable` a ejecutar para cada elemento de cada array.

`null` puede ser pasado como valor a `callback` para ejecutar una operación zip sobre varios arrays y devolver un array donde cada elemento es un array que contiene los elementos de los arrays de entrada en la misma posición del puntero interno del array (ver ejemplo a continuación). Si solo `array` es proporcionado, array_map devolverá el array de entrada.

`array`  
Un array a ejecutar a través de la función de devolución de llamada `callback`.

`arrays`  
Lista variable de argumentos de arrays adicionales a ejecutar a través de la función de devolución de llamada `callback`.

## Valores devueltos

Devuelve un `array` que contiene los resultados de la aplicación de la función de devolución de llamada `callback` al valor correspondiente de `array` (y `arrays` si se proporcionan más arrays) utilizados como argumentos para la función de devolución de llamada.

El `array` devuelto conservará las claves del array pasado como argumento, si y solo si, se pasa un solo array. Si se pasan varios arrays como argumento, el `array` devuelto tendrá claves secuenciales en forma de `int`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Si `callback` espera un parámetro a ser pasado por referencia, esta función emite ahora una `E_WARNING`. |

## Ejemplos

Ejemplo con `array_map`

```
<?php
function cube($n)
{
    return ($n * $n * $n);
}

$a = [1, 2, 3, 4, 5];
$b = array_map('cube', $a);
print_r($b);
?>

    
```php

El contenido de la variable `$b` será:

    Array
    (
        [0] => 1
        [1] => 8
        [2] => 27
        [3] => 64
        [4] => 125
    )

`array_map` utilizando una función cualquiera

```
<?php

$func = function(int $value): int {
    return $value * 2;
};

print_r(array_map($func, range(1, 5)));

// O a partir de PHP 7.4.0:

print_r(array_map(fn($value): int => $value * 2, range(1, 5)));

?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => 2
        [1] => 4
        [2] => 6
        [3] => 8
        [4] => 10
    )

`array_map`: uso de varios arrays

```
<?php
function show_Spanish(int $n, string $m): string
{
    return "El número {$n} se dice {$m} en Español";
}

function map_Spanish(int $n, string $m): array
{
    return [$n => $m];
}

$a = [1, 2, 3, 4, 5];
$b = ['uno', 'dos', 'tres', 'cuatro', 'cinco'];

$c = array_map('show_Spanish', $a, $b);
print_r($c);

$d = array_map('map_Spanish', $a , $b);
print_r($d);
?>

    
```php

El ejemplo anterior mostrará:

    // Contenido de $c
    Array
    (
        [0] => El número 1 se dice uno en Español
        [1] => El número 2 se dice dos en Español
        [2] => El número 3 se dice tres en Español
        [3] => El número 4 se dice cuatro en Español
        [4] => El número 5 se dice cinco en Español
    )

    // Contenido de $d
    Array
    (
        [0] => Array
            (
                [1] => uno
            )

        [1] => Array
            (
                [2] => dos
            )

        [2] => Array
            (
                [3] => tres
            )

        [3] => Array
            (
                [4] => cuatro
            )

        [4] => Array
            (
                [5] => cinco
            )

    )

Generalmente, al utilizar varios arrays, estos deben tener la misma longitud, ya que la función de devolución de llamada se aplica de manera similar a todos los arrays. Si los arrays tienen longitudes desiguales, los más pequeños serán completados con elementos vacíos para alcanzar la longitud del más grande.

Un uso interesante de esta función es la construcción de arrays de arrays, fácilmente realizada pasando el valor `null` como nombre de función de devolución de llamada.

Ejecutar una operación zip de arrays

```
<?php
$a = [1, 2, 3, 4, 5];
$b = ['one', 'two', 'three', 'four', 'five'];
$c = ['uno', 'dos', 'tres', 'cuatro', 'cinco'];

$d = array_map(null, $a, $b, $c);
print_r($d);
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => Array
            (
                [0] => 1
                [1] => one
                [2] => uno
            )

        [1] => Array
            (
                [0] => 2
                [1] => two
                [2] => dos
            )

        [2] => Array
            (
                [0] => 3
                [1] => three
                [2] => tres
            )

        [3] => Array
            (
                [0] => 4
                [1] => four
                [2] => cuatro
            )

        [4] => Array
            (
                [0] => 5
                [1] => five
                [2] => cinco
            )

    )

`null` `callback` con solo `array`

```
<?php
$array = [1, 2, 3];
var_dump(array_map(null, $array));
?>

    
```php

El ejemplo anterior mostrará:

    array(3) {
      [0]=>
      int(1)
      [1]=>
      int(2)
      [2]=>
      int(3)
    }

`array_map` - con claves en forma de `string`

```
<?php
$arr = ['stringkey' => 'value'];
function cb1($a) {
    return [$a];
}
function cb2($a, $b) {
    return [$a, $b];
}
var_dump(array_map('cb1', $arr));
var_dump(array_map('cb2', $arr, $arr));
var_dump(array_map(null,  $arr));
var_dump(array_map(null, $arr, $arr));
?>

    
```php

El ejemplo anterior mostrará:

    array(1) {
      ["stringkey"]=>
      array(1) {
        [0]=>
        string(5) "value"
      }
    }
    array(1) {
      [0]=>
      array(2) {
        [0]=>
        string(5) "value"
        [1]=>
        string(5) "value"
      }
    }
    array(1) {
      ["stringkey"]=>
      string(5) "value"
    }
    array(1) {
      [0]=>
      array(2) {
        [0]=>
        string(5) "value"
        [1]=>
        string(5) "value"
      }
    }

`array_map` - arrays asociativos

Aunque `array_map` no soporta directamente el uso de las claves de un array como entrada, esto puede ser simulado utilizando `array_keys`.

```
<?php
$arr = [
    'v1' => 'Primera versión',
    'v2' => 'Segunda versión',
    'v3' => 'Tercera versión',
];
// Nota: Anterior a 7.4.0, se debe utilizar la sintaxis más larga para las
// funciones anónimas en su lugar.
$callback = fn(string $k, string $v): string => "$k era la $v";
$result = array_map($callback, array_keys($arr), array_values($arr));
var_dump($result);
?>

    
```php

El ejemplo anterior mostrará:

    array(3) {
      [0]=>
      string(24) "v1 era la Primera versión"
      [1]=>
      string(25) "v2 era la Segunda versión"
      [2]=>
      string(24) "v3 era la Tercera versión"
    }

## Véase también

`array_filter`, `array_reduce`, `array_walk`
