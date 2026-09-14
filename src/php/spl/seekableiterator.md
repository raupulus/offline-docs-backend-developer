---
title: La interfaz SeekableIterator
source_url: https://www.php.net/manual/es/class.seekableiterator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/seekableiterator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: 4d17b7b49
order: 83760
---

## Introducción

El iterador Seekable.

## Sinopsis de la interfaz

SeekableIterator

extends

Iterator

Métodos

Métodos heredados

## Ejemplos

Uso básico

Este ejemplo muestra cómo crear un `SeekableIterator` personalizado, buscar una posición y manejar una posición inválida.

```php
<?php
class MySeekableIterator implements SeekableIterator {

    private $position;

    private $array = array(
        "first element",
        "second element",
        "third element",
        "fourth element"
    );

    /* Métodos requeridos para la interfaz SeekableIterator */

    public function seek($position) {
      if (!isset($this->array[$position])) {
          throw new OutOfBoundsException("invalid seek position ($position)");
      }

      $this->position = $position;
    }

    /* Métodos requeridos para la interfaz Iterador */

    public function rewind() {
        $this->position = 0;
    }

    public function current() {
        return $this->array[$this->position];
    }

    public function key() {
        return $this->position;
    }

    public function next() {
        ++$this->position;
    }

    public function valid() {
        return isset($this->array[$this->position]);
    }
}

try {

    $it = new MySeekableIterator;
    echo $it->current(), "\n";

    $it->seek(2);
    echo $it->current(), "\n";

    $it->seek(1);
    echo $it->current(), "\n";

    $it->seek(10);

} catch (OutOfBoundsException $e) {
    echo $e->getMessage();
}
?>

    
```

Resultado del ejemplo anterior es similar a:

    first element
    third element
    second element
    invalid seek position (10)
