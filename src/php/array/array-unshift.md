---
title: array_unshift
description: Empila uno o más elementos al inicio de un array
source_url: https://www.php.net/manual/es/function.array-unshift.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-unshift.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 0987e913f
order: 5690
---

array_unshift

Empila uno o más elementos al inicio de un array

## Descripción

```php
array_unshift(array $array, mixed ...$values): int
```php

`array_unshift` añade los elementos `value1`, `...`, pasados como argumento al inicio del array `array`. Se debe tener en cuenta que los elementos se añaden como un todo, y que permanecen en el mismo orden. Todas las claves numéricas se modificarán para comenzar desde cero, mientras que las claves literales no se verán afectadas.

> [!NOTE]
> Reinicia el puntero interno del array al primer elemento.

## Parámetros

`array`  
El array de entrada.

`values`  
Valor a empilar.

## Valores devueltos

Devuelve el nuevo número de elementos del array `array`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.3.0 | Esta función puede ahora ser llamada con un solo parámetro. Anteriormente, se requerían al menos dos parámetros. |

## Ejemplos

Ejemplo con `array_unshift`

```
<?php

$queue = [
    "orange",
    "banana"
];

array_unshift($queue, "apple", "raspberry");

var_dump($queue);

?>

    
```php

El ejemplo anterior mostrará:

```
array(4) {
  [0] =>
  string(5) "apple"
  [1] =>
  string(9) "raspberry"
  [2] =>
  string(6) "orange"
  [3] =>
  string(6) "banana"
}

    
```php

Uso con arrays asociativos

Si un array asociativo es añadido como prefijo a otro array asociativo, el array añadido es indexado numéricamente en el array precedente.

```
<?php

$foods = [
    'apples' => [
        'McIntosh' => 'red',
        'Granny Smith' => 'green',
    ],
    'oranges' => [
        'Navel' => 'orange',
        'Valencia' => 'orange',
    ],
];

$vegetables = [
    'lettuce' => [
        'Iceberg' => 'green',
        'Butterhead' => 'green',
    ],
    'carrots' => [
        'Deep Purple Hybrid' => 'purple',
        'Imperator' => 'orange',
    ],
    'cucumber' => [
        'Kirby' => 'green',
        'Gherkin' => 'green',
    ],
];

array_unshift($foods, $vegetables);

var_dump($foods);

    
```php

El ejemplo anterior mostrará:

```
array(3) {
  [0]=>
  array(3) {
    ["lettuce"]=>
    array(2) {
      ["Iceberg"]=>
      string(5) "green"
      ["Butterhead"]=>
      string(5) "green"
    }
    ["carrots"]=>
    array(2) {
      ["Deep Purple Hybrid"]=>
      string(6) "purple"
      ["Imperator"]=>
      string(6) "orange"
    }
    ["cucumber"]=>
    array(2) {
      ["Kirby"]=>
      string(5) "green"
      ["Gherkin"]=>
      string(5) "green"
    }
  }
  ["apples"]=>
  array(2) {
    ["McIntosh"]=>
    string(3) "red"
    ["Granny Smith"]=>
    string(5) "green"
  }
  ["oranges"]=>
  array(2) {
    ["Navel"]=>
    string(6) "orange"
    ["Valencia"]=>
    string(6) "orange"
  }
}

    
```php

## Véase también

`array_merge`, `array_shift`, `array_push`, `array_pop`
