---
title: ArrayObject::setIteratorClass
description: Define el nombre de la clase del iterador para el objeto ArrayObject
source_url: https://www.php.net/manual/es/arrayobject.setiteratorclass.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayobject/setiteratorclass.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: 52e3799c4
order: 81530
---

ArrayObject::setIteratorClass

Define el nombre de la clase del iterador para el objeto ArrayObject

## Descripción

```php
public ArrayObject::setIteratorClass(string $iteratorClass): void
```php

Define el nombre de la clase del iterador del array, utilizado por [ArrayObject::getIterator()](#arrayobject.getiterator).

## Parámetros

`iteratorClass`  
El nombre de la clase del iterador a utilizar para iterar sobre este objeto.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `ArrayObject::setIteratorClass`

```
<?php
// ArrayIterator personalizado (hereda de ArrayIterator)
class MonArrayIterator extends ArrayIterator {
    // implementación personal
}

// Lista de frutas
$fruits = array("citrons" => 1, "oranges" => 4, "bananes" => 5, "pommes" => 10);

$fruitsArrayObject = new ArrayObject($fruits);

// Asigna el nuevo nombre de clase de iteración
$fruitsArrayObject->setIteratorClass('MonArrayIterator');
var_dump($fruitsArrayObject->getIterator());

?>

    
```php

El ejemplo anterior mostrará:

    object(MonArrayIterator)#2 (1) {
      ["storage":"ArrayIterator":private]=>
      object(ArrayObject)#1 (1) {
        ["storage":"ArrayObject":private]=>
        array(4) {
          ["citrons"]=>
          int(1)
          ["oranges"]=>
          int(4)
          ["bananes"]=>
          int(5)
          ["pommes"]=>
          int(10)
        }
      }
    }
