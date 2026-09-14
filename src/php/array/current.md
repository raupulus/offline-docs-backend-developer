---
title: current
description: Devuelve el elemento actual del array
source_url: https://www.php.net/manual/es/function.current.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/current.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 2e60c5134
order: 5780
---

current

Devuelve el elemento actual del array

## Descripción

```php
current(array $array): mixed
```php

Cada array mantiene un puntero interno, que se inicializa cuando se inserta el primer elemento en el array.

## Parámetros

`array`  
El array.

## Valores devueltos

`current` solo devuelve el elemento actual apuntado por el puntero interno del array `array`. `current` no desplaza el puntero. Si el puntero está más allá del último elemento de la lista, `current` devuelve `false`.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | O bien convertir el `object` en un `array` utilizando `get_mangled_object_vars` primero, o utilizar los métodos proporcionados por una clase que implemente Iterator, tal como `ArrayIterator`. |
| 7.4.0 | A partir de PHP 7.4.0, las instancias de clases [SPL](#book.spl) son tratadas como objetos vacíos sin propiedades en lugar de llamar al método Iterator con el mismo nombre que esta función. |

## Ejemplos

Ejemplo de uso de `current`

```
<?php
echo $mode = current($transport), PHP_EOL; // $mode = 'foot';
echo $mode = next($transport), PHP_EOL;    // $mode = 'bike';
echo $mode = current($transport), PHP_EOL; // $mode = 'bike';
echo $mode = prev($transport), PHP_EOL;    // $mode = 'foot';
echo $mode = end($transport), PHP_EOL;     // $mode = 'plane';
echo $mode = current($transport), PHP_EOL; // $mode = 'plane';

$arr = array();
var_dump(current($arr)); // bool(false)

$arr = array(array());
var_dump(current($arr)); // array(0) { }
?>

    
```php

## Notas

> [!NOTE]
> No es posible distinguir el final de un array o el resultado de la llamada `current` sobre un array vacío, a partir del elemento `bool` `false`. Para recorrer correctamente un array que puede contener el elemento `false`, ver la estructura de control [`foreach`](#control-structures.foreach).
>
> Para seguir utilizando `current` y verificar correctamente si el valor es realmente un elemento del array, la `key` del elemento `current` debería compararse estrictamente diferente del elemento `null`.

## Véase también

`end`, `key`, `each`, `prev`, `reset`, `next`, [`foreach`](#control-structures.foreach)
