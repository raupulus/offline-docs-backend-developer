---
title: prev
description: Retrocede el puntero actual del array
source_url: https://www.php.net/manual/es/function.prev.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/prev.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 2e60c5134
order: 5920
---

prev

Retrocede el puntero actual del array

## Descripción

```php
prev(array $array): mixed
```php

Retrocede el puntero actual del array.

`prev` se comporta exactamente como `next`, pero retrocede el puntero en lugar de avanzarlo.

## Parámetros

`array`  
El array de entrada.

## Valores devueltos

Devuelve el valor anterior del array según el puntero interno del array, o `false` si no hay más elementos.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | O bien convertir el `object` en un `array` utilizando `get_mangled_object_vars` primero, o utilizar los métodos proporcionados por una clase que implemente Iterator, tal como `ArrayIterator`. |
| 7.4.0 | A partir de PHP 7.4.0, las instancias de clases [SPL](#book.spl) son tratadas como objetos vacíos sin propiedades en lugar de llamar al método Iterator con el mismo nombre que esta función. |

## Ejemplos

Ejemplo con `prev`

```
<?php
$transport = array('foot', 'bike', 'car', 'plane');
echo $mode = current($transport), PHP_EOL; // $mode = 'foot';
echo $mode = next($transport), PHP_EOL;    // $mode = 'bike';
echo $mode = next($transport), PHP_EOL;    // $mode = 'car';
echo $mode = prev($transport), PHP_EOL;    // $mode = 'bike';
echo $mode = end($transport), PHP_EOL;     // $mode = 'plane';
?>

    
```php

## Notas

> [!NOTE]
> No es posible distinguir el inicio de un array del elemento `bool` `false`. Para hacer la distinción, verifique si la `key` del elemento `prev` no es `null`.

## Véase también

`current`, `end`, `next`, `reset`, `each`
