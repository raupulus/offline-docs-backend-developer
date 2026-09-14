---
title: La interfaz Iterator
source_url: https://www.php.net/manual/es/class.iterator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/iterator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 4d17b7b49
order: 3780
---

## Introducción

Interfaz para iteradores externos u objetos que pueden ser iterados internamente por sí mismos.

## Sinopsis de la interfaz

Iterator

extends

Traversable

Métodos

## Iteradores Predefinidos

PHP ya ofrece un número de iteradores para muchas de las tareas del día a día. Véase la lista de [iteradores SPL](#spl.iterators).

## Ejemplos

Uso básico

Este ejemplo muestra el orden en el que se llaman a los métodos cuando se emplea un [`foreach`](#control-structures.foreach) con un iterator.

```php
<?php
class myIterator implements Iterator {
    private $position = 0;
    private $array = array(
        "firstelement",
        "secondelement",
        "lastelement",
    );

    public function __construct() {
        $this->position = 0;
    }

    public function rewind(): void {
        var_dump(__METHOD__);
        $this->position = 0;
    }

    #[\ReturnTypeWillChange]
    public function current() {
        var_dump(__METHOD__);
        return $this->array[$this->position];
    }

    #[\ReturnTypeWillChange]
    public function key() {
        var_dump(__METHOD__);
        return $this->position;
    }

    public function next(): void {
        var_dump(__METHOD__);
        ++$this->position;
    }

    public function valid(): bool {
        var_dump(__METHOD__);
        return isset($this->array[$this->position]);
    }
}

$it = new myIterator;

foreach($it as $key => $value) {
    var_dump($key, $value);
    echo "\n";
}
?>

    
```

Resultado del ejemplo anterior es similar a:

    string(18) "myIterator::rewind"
    string(17) "myIterator::valid"
    string(19) "myIterator::current"
    string(15) "myIterator::key"
    int(0)
    string(12) "firstelement"

    string(16) "myIterator::next"
    string(17) "myIterator::valid"
    string(19) "myIterator::current"
    string(15) "myIterator::key"
    int(1)
    string(13) "secondelement"

    string(16) "myIterator::next"
    string(17) "myIterator::valid"
    string(19) "myIterator::current"
    string(15) "myIterator::key"
    int(2)
    string(11) "lastelement"

    string(16) "myIterator::next"
    string(17) "myIterator::valid"

## Véase también

Véase también [iteración de objetos](#language.oop5.iterations).
