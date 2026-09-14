---
title: AppendIterator::key
description: Obtiene la clave actual
source_url: https://www.php.net/manual/es/appenditerator.key.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/appenditerator/key.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 81050
---

AppendIterator::key

Obtiene la clave actual

## Descripción

```php
public AppendIterator::key(): scalar
```php

Obtener la clave actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La clave actual si es válida o `null` en caso contrario.

## Ejemplos

Ejemplo básico de AppendIterator::key

```
<?php
$array_a = new ArrayIterator(array('a' => 'aardwolf', 'b' => 'bear', 'c' => 'capybara'));
$array_b = new ArrayIterator(array('apple', 'orange', 'lemon'));

$iterator = new AppendIterator;
$iterator->append($array_a);
$iterator->append($array_b);

// Manual iteration
$iterator->rewind();
while ($iterator->valid()) {
    echo $iterator->key() . ' ' . $iterator->current() . PHP_EOL;
    $iterator->next();
}

echo PHP_EOL;

// With foreach
foreach ($iterator as $key => $current) {
    echo $key . ' ' . $current . PHP_EOL;
}
?>

    
```php

El ejemplo anterior mostrará:

    a aardwolf
    b bear
    c capybara
    0 apple
    1 orange
    2 lemon

    a aardwolf
    b bear
    c capybara
    0 apple
    1 orange
    2 lemon

## Véase también

Iterator::key, AppendIterator::current, AppendIterator::valid, AppendIterator::next, AppendIterator::rewind
