---
title: RecursiveFilterIterator::__construct
description: Crea un RecursiveFilterIterator a partir de un RecursiveIterator
source_url: https://www.php.net/manual/es/recursivefilteriterator.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/recursivefilteriterator/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: d51166ca1
order: 83150
---

RecursiveFilterIterator::\_\_construct

Crea un RecursiveFilterIterator a partir de un RecursiveIterator

## Descripción

```php
public RecursiveFilterIterator::__construct(RecursiveIterator $iterator)
```php

Crea un `RecursiveFilterIterator` a partir de un `RecursiveIterator`.

## Parámetros

`iterator`  
El `RecursiveIterator` a ser filtrado.

## Ejemplos

Ejemplo básico de RecursiveFilterIterator

```
<?php
class TestsOnlyFilter extends RecursiveFilterIterator {
    public function accept() {
        // Aceptar el elemento actual si podemos utilizar la recursión en este
        // o este valor empieza con "test"
        return $this->hasChildren() || (strpos($this->current(), "test") !== FALSE);
    }
}

$array    = array("test1", array("taste2", "test3", "test4"), "test5");
$iterator = new RecursiveArrayIterator($array);
$filter   = new TestsOnlyFilter($iterator);

foreach(new RecursiveIteratorIterator($filter) as $key => $value)
{
    echo $value . "\n";
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    test1
    test3
    test4
    test5

Ejemplo de RecursiveFilterIterator

```
<?php
class StartsWithFilter extends RecursiveFilterIterator {

    protected $word;

    public function __construct(RecursiveIterator $rit, $word) {
        $this->word = $word;
        parent::__construct($rit);
    }

    public function accept() {
        return $this->hasChildren() OR strpos($this->current(), $this->word) === 0;
    }

    public function getChildren() {
        return new self($this->getInnerIterator()->getChildren(), $this->word);
    }
}

$array    = array("test1", array("taste2", "test3", "test4"), "test5");
$iterator = new RecursiveArrayIterator($array);
$filter   = new StartsWithFilter($iterator, "test");

foreach(new RecursiveIteratorIterator($filter) as $key => $value)
{
    echo $value . "\n";
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    test1
    test3
    test4
    test5

## Véase también

RecursiveFilterIterator::getChildren, RecursiveFilterIterator::hasChildren, FilterIterator::accept
