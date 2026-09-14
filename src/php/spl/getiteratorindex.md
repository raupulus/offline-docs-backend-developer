---
title: AppendIterator::getIteratorIndex
description: Lee el índice de un iterador
source_url: https://www.php.net/manual/es/appenditerator.getiteratorindex.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/appenditerator/getiteratorindex.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 81040
---

AppendIterator::getIteratorIndex

Lee el índice de un iterador

## Descripción

```php
public AppendIterator::getIteratorIndex(): int
```php

Lee el índice del iterador interno actual.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el índice entero, comenzando desde 0, del iterador interno si existe, `null` en caso contrario.

## Ejemplos

Ejemplo con AppendIterator.getIteratorIndex

```
<?php
$array_a = new ArrayIterator(array('a' => 'aardwolf', 'b' => 'bear', 'c' => 'capybara'));
$array_b = new ArrayIterator(array('apple', 'orange', 'lemon'));

$iterator = new AppendIterator;
$iterator->append($array_a);
$iterator->append($array_b);

foreach ($iterator as $key => $current) {
    echo $iterator->getIteratorIndex() . '  ' . $key . ' ' . $current . PHP_EOL;
}
?>

    
```php

El ejemplo anterior mostrará:

    0  a aardwolf
    0  b bear
    0  c capybara
    1  0 apple
    1  1 orange
    1  2 lemon

## Véase también

AppendIterator::getInnerIterator, AppendIterator::getArrayIterator
