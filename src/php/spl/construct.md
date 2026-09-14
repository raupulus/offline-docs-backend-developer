---
title: AppendIterator::__construct
description: Construye un AppendIterator
source_url: https://www.php.net/manual/es/appenditerator.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/appenditerator/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: d51166ca1
order: 81010
---

AppendIterator::\_\_construct

Construye un AppendIterator

## Descripción

```php
public AppendIterator::__construct()
```php

Construye un AppendIterator.

## Parámetros

Esta función no contiene ningún parámetro.

## Ejemplos

Recorriendo AppendIterator con foreach

```
<?php
$pizzas   = new ArrayIterator(array('Margarita', 'Siciliana', 'Hawaii'));
$ingredientes = new ArrayIterator(array('Cheese', 'Anchovies', 'Olives', 'Pineapple', 'Ham'));

$appendIterator = new AppendIterator;
$appendIterator->append($pizzas);
$appendIterator->append($ingredientes);

foreach ($appendIterator as $key => $item) {
    echo $key . ' => ' . $item . PHP_EOL;
}
?>

    
```php

El ejemplo anterior mostrará:

    0 => Margarita
    1 => Siciliana
    2 => Hawaii
    0 => Cheese
    1 => Anchovies
    2 => Olives
    3 => Pineapple
    4 => Ham

Recorriendo AppendIterator con la API de AppendIterator

```
<?php
$pizzas   = new ArrayIterator(array('Margarita', 'Siciliana', 'Hawaii'));
$ingredientes = new ArrayIterator(array('Cheese', 'Anchovies', 'Olives', 'Pineapple', 'Ham'));

$appendIterator = new AppendIterator;
$appendIterator->append($pizzas);
$appendIterator->append($ingredientes);

while ($appendIterator->valid()) {
    printf(
        '%s => %s => %s%s',
        $appendIterator->getIteratorIndex(),
        $appendIterator->key(),
        $appendIterator->current(),
        PHP_EOL
    );
    $appendIterator->next();
}
?>

    
```php

El ejemplo anterior mostrará:

    0 => 0 => Margarita
    0 => 1 => Siciliana
    0 => 2 => Hawaii
    1 => 0 => Cheese
    1 => 1 => Anchovies
    1 => 2 => Olives
    1 => 3 => Pineapple
    1 => 4 => Ham

## Notas

> [!CAUTION]
> Al usar `iterator_to_array` para copiar los valores de AppendIterator a un array, debe asignarse al parámetro opcional `use_key` el valor `false`. Si `use_key` no es `false`, las claves que se repitan en los iteradores internos se sobrescribirán en el array final. No existe ninguna forma para preservar las claves originales.

## Véase también

AppendIterator::append
