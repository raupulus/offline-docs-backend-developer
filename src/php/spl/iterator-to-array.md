---
title: iterator_to_array
description: Copia un iterador en un array
source_url: https://www.php.net/manual/es/function.iterator-to-array.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/functions/iterator-to-array.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 70ac605e6
order: 82240
---

iterator_to_array

Copia un iterador en un array

## Descripción

```php
iterator_to_array(Traversable $iterator, [bool $preserve_keys]): array
```php

Copia los elementos de un iterador en un `array`.

## Parámetros

`iterator`  
El iterador a copiar.

`preserve_keys`  
Si se deben utilizar los elementos del iterador como clave.

Si una clave es un `array` o un `object`, se generará una advertencia. Las claves `null` serán convertidas en una cadena vacía, las claves de tipo `float` serán truncadas a sus partes `int`, las claves de tipo `resource` generarán una advertencia y serán convertidas en identificador de la recurso, y las claves de tipo `bool` serán convertidas en enteros.

> [!NOTE]
> Si este argumento no está definido o está definido en `true`, las claves duplicadas serán sobrescritas. El último valor con una clave dada estará en el `array` devuelto. Definir este argumento en `false` para obtener todas las valores en todo caso.

## Valores devueltos

Un `array` que contiene los elementos del iterador `iterator`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | El tipo de `iterator` ha sido ampliado de `Traversable` a `Traversablearray`. |

## Ejemplos

Ejemplo con `iterator_to_array`

```
<?php
$iterator = new ArrayIterator(array('recipe'=>'crêpes', 'oeufs', 'lait', 'farine'));
var_dump(iterator_to_array($iterator, true));
var_dump(iterator_to_array($iterator, false));
?>

    
```php

El ejemplo anterior mostrará:

    array(4) {
      ["recipe"]=>
      string(7) "crêpes"
      [0]=>
      string(5) "oeufs"
      [1]=>
      string(4) "lait"
      [2]=>
      string(6) "farine"
    }
    array(4) {
      [0]=>
      string(7) "crêpes"
      [1]=>
      string(5) "oeufs"
      [2]=>
      string(4) "lait"
      [3]=>
      string(6) "farine"
    }
