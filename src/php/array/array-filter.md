---
title: array_filter
description: Filtra los elementos de un array mediante una función de retrollamada
source_url: https://www.php.net/manual/es/function.array-filter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-filter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: 596c11440
order: 5280
---

array_filter

Filtra los elementos de un array mediante una función de retrollamada

## Descripción

```php
array_filter(array $array, [callable $callback], [int $mode]): array
```php

Evalúa cada valor del array `array` pasándolos a la función de retrollamada `callback`. Si la función de retrollamada `callback` devuelve `true`, el valor actual del array `array` es devuelto en el `array` resultante.

Las claves del array son preservadas, y puede causar anomalías si el array `array` estaba indexado. El array resultante puede ser reindexado utilizando la función `array_values`.

## Parámetros

`array`  
El array a recorrer

`callback`  
La función de retrollamada a utilizar

Si no se proporciona ninguna función de retrollamada `callback`, todas las entradas vacías del array `array` serán eliminadas. Ver la función `empty` para comprender cómo PHP maneja el vacío en este caso.

`mode`  
Flag que indica cuáles son los argumentos a enviar a la función de retrollamada `callback`:

- `ARRAY_FILTER_USE_KEY` - pasar la clave como único argumento a `callback` en lugar del valor.

- `ARRAY_FILTER_USE_BOTH` - pasar tanto el valor como la clave como argumentos de `callback` en lugar del valor.

Por omisión `0`, que pasará el valor como único argumento de `callback`.

## Valores devueltos

Devuelve el array filtrado.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `callback` es ahora nullable. |
| 8.0.0 | Si `callback` espera un parámetro a ser pasado por referencia, esta función emite ahora una `E_WARNING`. |

## Ejemplos

Ejemplo con `array_filter`

```
<?php
function odd($var)
{
    // devuelve si el entero de entrada es impar
    return $var & 1;
}

function even($var)
{
    // devuelve si el entero de entrada es par
    return !($var & 1);
}

$array1 = ['a' => 1, 'b' => 2, 'c' => 3, 'd' => 4, 'e' => 5];
$array2 = [6, 7, 8, 9, 10, 11, 12];

echo "Impar :\n";
print_r(array_filter($array1, "odd"));
echo "Par :\n";
print_r(array_filter($array2, "even"));
?>

    
```php

El ejemplo anterior mostrará:

```
Impar :
Array
(
    [a] => 1
    [c] => 3
    [e] => 5
)
Par :
Array
(
    [0] => 6
    [2] => 8
    [4] => 10
    [6] => 12
)

    
```php

Ejemplo con `array_filter` `callback`

```
<?php

$entry = [
    0 => 'foo',
    1 => false,
    2 => -1,
    3 => null,
    4 => '',
    5 => '0',
    6 => 0,
];

print_r(array_filter($entry));
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => foo
        [2] => -1
    )

Ejemplo con `array_filter` y `mode`

```
<?php

$arr = ['a' => 1, 'b' => 2, 'c' => 3, 'd' => 4];

var_dump(array_filter($arr, function($k) {
    return $k == 'b';
}, ARRAY_FILTER_USE_KEY));

var_dump(array_filter($arr, function($v, $k) {
    return $k == 'b' || $v == 4;
}, ARRAY_FILTER_USE_BOTH));
?>

    
```php

El ejemplo anterior mostrará:

    array(1) {
      ["b"]=>
      int(2)
    }
    array(2) {
      ["b"]=>
      int(2)
      ["d"]=>
      int(4)
    }

## Notas

> [!CAUTION]
> Si el array es modificado desde la función de retrollamada (por ejemplo se añaden o eliminan elementos), el comportamiento de esta función es indefinido.

## Véase también

`array_intersect`, `array_find`, `array_any`, `array_map`, `array_reduce`
