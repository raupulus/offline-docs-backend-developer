---
title: array_merge
description: Fusiona varios arrays en uno solo
source_url: https://www.php.net/manual/es/function.array-merge.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-merge.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 2e60c5134
order: 5460
---

array_merge

Fusiona varios arrays en uno solo

## Descripción

```php
array_merge(array ...$arrays): array
```php

`array_merge` combina los elementos de uno o varios arrays añadiendo los valores de uno al final del otro. El resultado es un array.

Si los arrays de entrada tienen claves comunes, entonces, el valor final para esa clave sobrescribirá al anterior. Sin embargo, si los arrays contienen claves numéricas, el valor final **no sobrescribirá** el valor original, sino que será añadido.

Las claves numéricas de los arrays de entrada serán renumeradas en claves incrementadas partiendo de cero en el array fusionado.

## Parámetros

`arrays`  
Lista de arrays variable para fusionar.

## Valores devueltos

Devuelve el array resultante. Si se invoca sin argumentos, devuelve un `array` vacío.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.4.0 | Esta función puede ser ahora llamada sin parámetros. Anteriormente, al menos un parámetro era requerido. |

## Ejemplos

Ejemplo con `array_merge`

```
<?php
$array1 = array("color" => "red", 2, 4);
$array2 = array("a", "b", "color" => "green", "shape" => "trapezoid", 4);
$result = array_merge($array1, $array2);
print_r($result);
?>

    
```php

El ejemplo anterior mostrará:

```
Array
(
    [color] => green
    [0] => 2
    [1] => 4
    [2] => a
    [3] => b
    [shape] => trapezoid
    [4] => 4
)

    
```php

Ejemplo simple con `array_merge`

```
<?php
$array1 = array();
$array2 = array(1 => "data");
$result = array_merge($array1, $array2);
print_r($result);
?>

    
```php

No se olvide de que los índices numéricos serán reindexados.

```
Array
(
    [0] => data
)

    
```php

Si se desea añadir elementos del segundo array al primero sin sobrescribir o reindexar los elementos del primero, utilice el operador de unión `+`:

```
<?php
$array1 = array(0 => 'zero_a', 2 => 'two_a', 3 => 'three_a');
$array2 = array(1 => 'one_b', 3 => 'three_b', 4 => 'four_b');
$result = $array1 + $array2;
var_dump($result);
?>

    
```php

Las claves del primer array son preservadas. Si una clave existe en los 2 arrays, entonces el elemento del primero será utilizado y la clave correspondiente del segundo será ignorada.

```
array(5) {
  [0]=>
  string(6) "zero_a"
  [2]=>
  string(5) "two_a"
  [3]=>
  string(7) "three_a"
  [1]=>
  string(5) "one_b"
  [4]=>
  string(6) "four_b"
}

    
```php

Ejemplo con `array_merge` con tipos no-array

```
<?php
$beginning = 'foo';
$end = array(1 => 'bar');
$result = array_merge((array) $beginning, (array) $end);
print_r($result);
?>

    
```php

El ejemplo anterior mostrará:

```
Array
(
    [0] => foo
    [1] => bar
)

    
```php

## Véase también

`array_merge_recursive`, `array_replace`, `array_combine`, [operadores de array](#language.operators.array)
