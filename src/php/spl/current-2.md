---
title: ArrayIterator::current
description: Devuelve la entrada actual del array
source_url: https://www.php.net/manual/es/arrayiterator.current.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayiterator/current.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 81140
---

ArrayIterator::current

Devuelve la entrada actual del array

## Descripción

```php
public ArrayIterator::current(): mixed
```php

Obtiene la entrada actual del `array`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La entrada actual del `array`.

## Ejemplos

Ejemplo de `ArrayIterator::current`

```
<?php
$array = array('1' => 'uno',
               '2' => 'dos',
               '3' => 'tres');

$arrayobject = new ArrayObject($array);

for($iterator = $arrayobject->getIterator();
    $iterator->valid();
    $iterator->next()) {

    echo $iterator->key() . ' => ' . $iterator->current() . "\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    1 => uno
    2 => dos
    3 => tres
