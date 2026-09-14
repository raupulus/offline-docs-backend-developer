---
title: LimitIterator::getPosition
description: Devuelve la posición actual
source_url: https://www.php.net/manual/es/limititerator.getposition.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/limititerator/getposition.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: d51166ca1
order: 82540
---

LimitIterator::getPosition

Devuelve la posición actual

## Descripción

```php
public LimitIterator::getPosition(): int
```php

Devuelve la posición (partiendo de cero) del iterador interno `Iterator`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La posición actual.

## Ejemplos

Ejemplo `LimitIterator::getPosition`

```
<?php
$fruits = array(
    'a' => 'apple',
    'b' => 'banana',
    'c' => 'cherry',
    'd' => 'damson',
    'e' => 'elderberry'
);
$array_it = new ArrayIterator($fruits);
$limit_it = new LimitIterator($array_it, 2, 3);
foreach ($limit_it as $item) {
    echo $limit_it->getPosition() . ' ' . $item . "\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    2 cherry
    3 damson
    4 elderberry

## Véase también

FilterIterator::key
