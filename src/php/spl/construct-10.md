---
title: InfiniteIterator::__construct
description: Construye un InfiniteIterator
source_url: https://www.php.net/manual/es/infiniteiterator.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/infiniteiterator/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: d51166ca1
order: 82370
---

InfiniteIterator::\_\_construct

Construye un InfiniteIterator

## Descripción

```php
public InfiniteIterator::__construct(Iterator $iterator)
```php

Construye un `InfiniteIterator` de un `Iterator`.

## Parámetros

`iterator`  
El iterador a iterar infinitamente.

## Ejemplos

Ejemplo de `InfiniteIterator::__construct`

```
<?php
$arrayit  = new ArrayIterator(array('gato','perro'));
$infinite = new InfiniteIterator($arrayit);
$limit    = new LimitIterator($infinite, 0, 7);
foreach($limit as $value)
{
    echo "$value\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    gato
    perro
    gato
    perro
    gato
    perro
    gato

## Véase también

InfiniteIterator::next
