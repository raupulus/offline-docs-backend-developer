---
title: ArrayObject::getIteratorClass
description: Lee el nombre de la clase de ArrayObject
source_url: https://www.php.net/manual/es/arrayobject.getiteratorclass.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayobject/getiteratorclass.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: d51166ca1
order: 81430
---

ArrayObject::getIteratorClass

Lee el nombre de la clase de

ArrayObject

## Descripción

```php
public ArrayObject::getIteratorClass(): string
```php

Lee el nombre de la clase utilizado por el iterador de array utilizado por [ArrayObject::getIterator()](#arrayobject.getiterator).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el nombre de la clase de iterador utilizado por este objeto.

## Ejemplos

Ejemplo con `ArrayObject::getIteratorClass`

```
<?php
// ArrayIterator personalizado (hereda de ArrayIterator)
class MyArrayIterator extends ArrayIterator {
    // implementación personalizada
}

// Array de frutas
$fruits = array("citrons" => 1, "oranges" => 4, "bananes" => 5, "pommes" => 10);

$fruitsArrayObject = new ArrayObject($fruits);

// Lee el nombre de la clase actual
$className = $fruitsArrayObject->getIteratorClass();
var_dump($className);

// Configura el nombre de la nueva clase
$fruitsArrayObject->setIteratorClass('MyArrayIterator');

// Lee el nombre de la clase del nuevo iterador
$className = $fruitsArrayObject->getIteratorClass();
var_dump($className);
?>

    
```php

El ejemplo anterior mostrará:

    string(13) "ArrayIterator"
    string(15) "MyArrayIterator"

## Véase también

El método [ArrayObject::setIteratorClass](#arrayobject.setiteratorclass)
