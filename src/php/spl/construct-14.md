---
title: NoRewindIterator::__construct
description: Construye un NoRewindIterator
source_url: https://www.php.net/manual/es/norewinditerator.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/norewinditerator/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: d51166ca1
order: 82750
---

NoRewindIterator::\_\_construct

Construye un NoRewindIterator

## Descripción

```php
public NoRewindIterator::__construct(Iterator $iterator)
```php

Construye un NoRewindIterator.

## Parámetros

`iterator`  
El iterador a ser usado.

## Ejemplos

Ejemplo de NoRewindIterator::\_\_construct

El segundo bucle no imprime nada porque el iterador solo puede usarse una vez, no se puede rebobinar.

```
<?php
$fruit = array('manzana', 'banano', 'arándano');

$arr = new ArrayObject($fruit);
$it  = new NoRewindIterator($arr->getIterator());

echo "Fruit A:\n";
foreach( $it as $item ) {
    echo $item . "\n";
}

echo "Fruit B:\n";
foreach( $it as $item ) {
    echo $item . "\n";
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Fruit A:
    manzana
    banano
    arándano
    Fruit B:

## Véase también

NoRewindIterator::valid
