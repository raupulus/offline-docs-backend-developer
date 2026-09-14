---
title: array
description: Crea un array
source_url: https://www.php.net/manual/es/function.array.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: 2e60c5134
order: 5730
---

array

Crea un array

## Descripción

```php
array(mixed ...$values): array
```php

Crea un array. Consulte la sección sobre los [tipos array](#language.types.array) para obtener más información sobre qué es un array, incluyendo los detalles sobre la sintaxis alternativa de corchetes (`[]`).

## Parámetros

`values`  
La sintaxis "índice =\> valor", separada por comas, define los índices y sus valores. Un índice puede ser una cadena o un número. Si el índice se omite, se generará automáticamente un índice numérico (comenzando en 0). Si el índice es un entero, el siguiente índice generado tomará el valor del índice más grande + 1. Tenga en cuenta que si se definen dos índices idénticos, el último sobrescribirá al primero.

Tener una coma después de definir la última entrada, aunque innecesario, es una sintaxis válida.

## Valores devueltos

Devuelve un array de los argumentos. Los argumentos pueden proporcionar un índice utilizando el operador `=>`. Consulte la sección sobre los [tipos array](#language.types.array) para obtener más información sobre qué es un array.

## Ejemplos

El siguiente ejemplo muestra cómo crear un array de dos dimensiones, cómo especificar los índices de un array asociativo, y cómo generar automáticamente índices numéricos.

Ejemplo con `array`

```
<?php
$fruits = array (
    "fruits"  => array("a" => "orange", "b" => "banana", "c" => "apple"),
    "numbers" => array(1, 2, 3, 4, 5, 6),
    "holes"   => array("first", 5 => "second", "third")
);
print_r($fruits);
?>

    
```php

Índices automáticos con `array`

```
<?php
$array = array(1, 1, 1, 1,  1, 8 => 1, 4 => 1, 19, 3 => 13);
print_r($array);
?>

    
```php

El ejemplo anterior mostrará:

```
Array
(
    [0] => 1
    [1] => 1
    [2] => 1
    [3] => 13
    [4] => 1
    [8] => 1
    [9] => 19
)

    
```php

Observe que el índice '3' se define dos veces, y finalmente conserva su último valor de 13. El índice '4' se define después del índice '8', y el siguiente índice generado (valor 19) es 9, ya que el índice más grande es entonces 8.

Este ejemplo crea un array cuyos índices comienzan en 1.

Índices comenzando en 1 con `array`

```
<?php
$firstQuarter = array(1 => 'January', 'February', 'March');
print_r($firstQuarter);
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [1] => January
        [2] => February
        [3] => March
    )

Al igual que en Perl, puede acceder a un valor de un array en comillas dobles. Sin embargo, con PHP, debe rodear su array con llaves.

Acceder a un array en comillas dobles

```
<?php
$foo = array('bar' => 'baz');
echo "Hello {$foo['bar']}!"; // Hello baz!
?>

    
```php

## Notas

> [!NOTE]
> `array` es un constructor de lenguaje utilizado para representar literalmente los arrays, pero en ningún caso es una función regular.

## Véase también

`array_pad`, `list`, `count`, `range`, [`foreach`](#control-structures.foreach), El tipo [array](#language.types.array)
