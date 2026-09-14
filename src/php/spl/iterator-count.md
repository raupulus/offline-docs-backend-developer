---
title: iterator_count
description: Cuenta el número de elementos en un iterador
source_url: https://www.php.net/manual/es/function.iterator-count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/functions/iterator-count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: 70ac605e6
order: 82230
---

iterator_count

Cuenta el número de elementos en un iterador

## Descripción

```php
iterator_count(Traversable $iterator): int
```php

Cuenta los elementos en un iterador. No se garantiza que la función `iterator_count` conserve la posición actual del iterador `iterator`.

## Parámetros

`iterator`  
El iterador del cual contar los elementos.

## Valores devueltos

El número de elementos en el iterador `iterator`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | El tipo de `iterator` ha sido ampliado de `Traversable` a `Traversablearray`. |

## Ejemplos

Ejemplo con `iterator_count`

```
<?php
$iterator = new ArrayIterator(array('recipe'=>'crêpes', 'oeufs', 'lait', 'farine'));
var_dump(iterator_count($iterator));
?>

    
```php

El ejemplo anterior mostrará:

    int(4)

Ejemplo con `iterator_count` que modifica la posición

```
<?php
$iterator = new ArrayIterator(['one', 'two', 'three']);
var_dump($iterator->current());
var_dump(iterator_count($iterator));
var_dump($iterator->current());
?>

    
```php

El ejemplo anterior mostrará:

    string(3) "one"
    int(3)
    NULL

Ejemplo con `iterator_count` en un ciclo [`foreach`](#control-structures.foreach)

```
<?php
$iterator = new ArrayIterator(['one', 'two', 'three']);
foreach ($iterator as $key => $value) {
    echo "$key: $value (", iterator_count($iterator), ")\n";
}?>

    
```php

El ejemplo anterior mostrará:

    0: one (3)
