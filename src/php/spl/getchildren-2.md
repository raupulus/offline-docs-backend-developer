---
title: RecursiveArrayIterator::getChildren
description: Devuelve un iterador para la entrada actual
source_url: https://www.php.net/manual/es/recursivearrayiterator.getchildren.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/recursivearrayiterator/getchildren.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 82950
---

RecursiveArrayIterator::getChildren

Devuelve un iterador para la entrada actual

## Descripción

```php
public RecursiveArrayIterator::getChildren(): RecursiveArrayIterator
```php

Devuelve un iterador para la entrada del iterador actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un iterador para la entrada actual, si es un `array` o un `object`; o `null` si ocurre un error.

## Errores/Excepciones

Se lanzará una excepción `InvalidArgumentException` si la entrada actual no contiene un `array` o un `object`.

## Ejemplos

Ejemplo con `RecursiveArrayIterator::getChildren`

```
<?php
$fruits = array("a" => "lemon", "b" => "orange", array("a" => "apple", "p" => "pear"));

$iterator = new RecursiveArrayIterator($fruits);

while ($iterator->valid()) {

    if ($iterator->hasChildren()) {
        // Muestra todos los hijos
        foreach ($iterator->getChildren() as $key => $value) {
            echo $key . ' : ' . $value . "\n";
        }
    } else {
        echo "Sin hijos.\n";
    }

    $iterator->next();
}
?>

    
```php

El ejemplo anterior mostrará:

    Sin hijos.
    Sin hijos.
    a : apple
    p : pear

## Véase también

`RecursiveArrayIterator::hasChildren`
