---
title: ReflectionClass::isIterable
description: Verifica si esta clase es iterable
source_url: https://www.php.net/manual/es/reflectionclass.isiterable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/isiterable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: '246613573'
order: 69520
---

ReflectionClass::isIterable

Verifica si esta clase es iterable

## Descripción

```php
public ReflectionClass::isIterable(): bool
```php

Verifica si esta clase es iterable (es decir, que puede ser utilizada en [`foreach`](#control-structures.foreach)).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna `true` si la clase es iterable o `false` en caso contrario.

## Ejemplos

Uso simple de ReflectionClass::isIterable

```
<?php

class IteratorClass implements Iterator
{
    public function __construct() {}

    public function key(): mixed {}

    public function current(): mixed {}

    public function next(): void {}

    public function valid(): bool {}

    public function rewind(): void {}
}

class DerivedClass extends IteratorClass {}

class NonIterator {}

function dump_iterable($class)
{
    $reflection = new ReflectionClass($class);
    var_dump($reflection->isIterable());
}

$classes = ["ArrayObject", "IteratorClass", "DerivedClass", "NonIterator",];

foreach ($classes as $class) {
    echo "¿Es $class iterable? ";
    dump_iterable($class);
}
?>

    
```php

El ejemplo anterior mostrará:

    ¿Es ArrayObject iterable? bool(true)
    ¿Es IteratorClass iterable? bool(true)
    ¿Es DerivedClass iterable? bool(true)
    ¿Es NonIterator iterable? bool(false)

## Véase también

ReflectionClass::\_\_construct
