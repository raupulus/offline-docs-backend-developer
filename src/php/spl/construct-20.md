---
title: RecursiveIteratorIterator::__construct
description: Crea una instancia de RecursiveIteratorIterator
source_url: https://www.php.net/manual/es/recursiveiteratoriterator.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/recursiveiteratoriterator/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: c142be811
order: 83260
---

RecursiveIteratorIterator::\_\_construct

Crea una instancia de RecursiveIteratorIterator

## Descripción

```php
public RecursiveIteratorIterator::__construct(Traversable $iterator, [int $mode], [int $flags])
```php

Crea un `RecursiveIteratorIterator` a partir de un `RecursiveIterator`.

## Parámetros

`iterator`  
El iterador a partir del cual va a ser creado. Puede ser tanto un `RecursiveIterator` o un `IteratorAggregate`.

`mode`  
Opcional. Los valores posibles son `RecursiveIteratorIterator::LEAVES_ONLY` - El predeterminado. Lista sólo las hojas en la iteración., `RecursiveIteratorIterator::SELF_FIRST` - Lista las hojas y los padres en la iteración con los padres primero., `RecursiveIteratorIterator::CHILD_FIRST` - Lista las hojas y los padres en la iteración con las hojas primero.

`flags`  
Opcional. Los valores posibles son `RecursiveIteratorIterator::CATCH_GET_CHILD` el cual ignorará las excepciones lanzadas en llamadas a RecursiveIteratorIterator::getChildren.

## Ejemplos

Iterando un RecursiveIteratorIterator

```
<?php
$array = array(
    array(
        array(
            array(
                'leaf-0-0-0-0',
                'leaf-0-0-0-1'
            ),
            'leaf-0-0-0'
        ),
        array(
            array(
                'leaf-0-1-0-0',
                'leaf-0-1-0-1'
            ),
            'leaf-0-1-0'
        ),
        'leaf-0-0'
    )
);

$iterator = new RecursiveIteratorIterator(
    new RecursiveArrayIterator($array),
    $mode
);
foreach ($iterator as $key => $leaf) {
    echo "$key => $leaf", PHP_EOL;
}
?>

    
```php

Salida con `$mode = RecursiveIteratorIterator::LEAVES_ONLY`

    0 => leaf-0-0-0-0
    1 => leaf-0-0-0-1
    0 => leaf-0-0-0
    0 => leaf-0-1-0-0
    1 => leaf-0-1-0-1
    0 => leaf-0-1-0
    0 => leaf-0-0

        

Salida con `$mode = RecursiveIteratorIterator::SELF_FIRST`

    0 => Array
    0 => Array
    0 => Array
    0 => leaf-0-0-0-0
    1 => leaf-0-0-0-1
    1 => leaf-0-0-0
    1 => Array
    0 => Array
    0 => leaf-0-1-0-0
    1 => leaf-0-1-0-1
    1 => leaf-0-1-0
    2 => leaf-0-0

        

Salida con `$mode = RecursiveIteratorIterator::CHILD_FIRST`

    0 => leaf-0-0-0-0
    1 => leaf-0-0-0-1
    0 => Array
    1 => leaf-0-0-0
    0 => Array
    0 => leaf-0-1-0-0
    1 => leaf-0-1-0-1
    0 => Array
    1 => leaf-0-1-0
    1 => Array
    2 => leaf-0-0
    0 => Array
