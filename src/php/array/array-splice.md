---
title: array_splice
description: Elimina y reemplaza una porción de array
source_url: https://www.php.net/manual/es/function.array-splice.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-splice.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 2e60c5134
order: 5600
---

array_splice

Elimina y reemplaza una porción de array

## Descripción

```php
array_splice(array $array, int $offset, [int $length], [mixed $replacement]): array
```php

`array_splice` elimina los elementos designados por `offset` y `length` del array `array` y los reemplaza por los elementos del array `replacement`, si este último es proporcionado.

> [!NOTE]
> Las claves numéricas en `array` no son preservadas.

> [!NOTE]
> Si `replacement` no es un array, se convertirá en uno por [conversión](#language.types.array.casting) (i.e. `(array) $replacement`). Esto puede producir resultados inesperados al utilizar un objeto o `null` como argumento `replacement`.

## Parámetros

`array`  
El array de entrada.

`offset`  
Si `offset` es positivo, el inicio de la sección a eliminar estará en esta posición partiendo del inicio del array `array`.

Si `offset` es negativo, el inicio de la sección a eliminar estará en esta posición partiendo del final del array `array`.

`length`  
Si `length` es omitido, todos los elementos del array desde la posición `offset` hasta el final del array serán eliminados.

Si `length` es proporcionado y positivo, entonces tantos elementos serán eliminados.

Si `length` es proporcionado y negativo, entonces tantos elementos serán eliminados del final del array.

Si `length` es proporcionado y vale cero, entonces ningún elemento será eliminado.

> [!TIP]
> Para eliminar todo desde la posición `offset` hasta el final del array cuando `replacement` también es proporcionado, utilizar `count($input)` para `length`.

`replacement`  
Si el `array` `replacement` es proporcionado, entonces los elementos eliminados son reemplazados por los elementos de este `array`.

Si el `offset` y `length` son tales que nada es eliminado, entonces los elementos del `array` `replacement` son insertados en la posición `offset`.

> [!NOTE]
> Las claves del `array` `replacement` no son preservadas.

Si `replacement` es solo un elemento no es necesario rodear el elemento con `array()` o corchetes, a menos que el elemento sea él mismo un array, un objeto o `null`.

## Valores devueltos

Retorna un `array` conteniendo los elementos extraídos.

## Historial de cambios

| Versión | Descripción                 |
|---------|-----------------------------|
| 8.0.0   | `length` ahora es nullable. |

## Ejemplos

Ejemplos con `array_splice`

```
<?php
$input = array("red", "green", "blue", "yellow");
array_splice($input, 2);
var_dump($input);

$input = array("red", "green", "blue", "yellow");
array_splice($input, 1, -1);
var_dump($input);

$input = array("red", "green", "blue", "yellow");
array_splice($input, 1, count($input), "orange");
var_dump($input);

$input = array("red", "green", "blue", "yellow");
array_splice($input, -1, 1, array("black", "maroon"));
var_dump($input);
?>

    
```php

El ejemplo anterior mostrará:

    array(2) {
      [0]=>
      string(3) "red"
      [1]=>
      string(5) "green"
    }
    array(2) {
      [0]=>
      string(3) "red"
      [1]=>
      string(6) "yellow"
    }
    array(2) {
      [0]=>
      string(3) "red"
      [1]=>
      string(6) "orange"
    }
    array(5) {
      [0]=>
      string(3) "red"
      [1]=>
      string(5) "green"
      [2]=>
      string(4) "blue"
      [3]=>
      string(5) "black"
      [4]=>
      string(6) "maroon"
    }

Declaraciones equivalentes a ejemplos de `array_splice` diversos

Las declaraciones siguientes son equivalentes:

```
<?php

// añadir dos elementos a $input
array_push($input, $x, $y);
array_splice($input, count($input), 0, array($x, $y));

// eliminar el último elemento de $input
array_pop($input);
array_splice($input, -1);

// eliminar el primer elemento de $input
array_shift($input);
array_splice($input, 0, 1);

// insertar dos elementos al inicio de $input
array_unshift($input, $x, $y);
array_splice($input, 0, 0, array($x, $y));

// reemplazar el valor en $input en el índice $x
$input[$x] = $y; // para arrays donde las claves son iguales al offset
array_splice($input, $x, 1, $y);

?>

    
```php

## Véase también

`array_merge`, `array_slice`, `unset`
