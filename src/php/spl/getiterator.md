---
title: ArrayObject::getIterator
description: Crea un nuevo iterador a partir de un objeto ArrayObject
source_url: https://www.php.net/manual/es/arrayobject.getiterator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayobject/getiterator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: ba762ce19
order: 81420
---

ArrayObject::getIterator

Crea un nuevo iterador a partir de un objeto

ArrayObject

## Descripción

```php
public ArrayObject::getIterator(): Iterator
```php

Crea un nuevo Iterator (por omisión `ArrayIterator`) a partir de una instancia de `ArrayObject`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un iterador desde un `ArrayObject`.

## Ejemplos

Ejemplo con `ArrayObject::getIterator`

```
<?php

$array = [
    '1' => 'one',
    '2' => 'two',
    '3' => 'three',
];

$arrayobject = new ArrayObject($array);

$iterator = $arrayobject->getIterator();

while ($iterator->valid()) {
    echo $iterator->key() . ' => ' . $iterator->current() . "\n";

    $iterator->next();
}

?>

    
```php

El ejemplo anterior mostrará:

    1 => one
    2 => two
    3 => three
