---
title: RecursiveArrayIterator::hasChildren
description: Devuelve si la entrada actual es un array o un objeto
source_url: https://www.php.net/manual/es/recursivearrayiterator.haschildren.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/recursivearrayiterator/haschildren.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 82960
---

RecursiveArrayIterator::hasChildren

Devuelve si la entrada actual es un array o un objeto

## Descripción

```php
public RecursiveArrayIterator::hasChildren(): bool
```php

Devuelve si la entrada actual es un `array` o un `object` para que un iterador puede ser obtenido a través de RecursiveArrayIterator::getChildren.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si la entrada actual es un `array` o un `object`, en caso contrario `false`.

## Ejemplos

Ejemplo de `RecursiveArrayIterator::hasChildren`

```
<?php
$fruits = array("a" => "limon", "b" => "naranja", array("a" => "manzana", "p" => "pera"));

$iterator = new RecursiveArrayIterator($fruits);

while ($iterator->valid()) {

    // Comprueba si hay hijos
    if ($iterator->hasChildren()) {
        // imprime todos los hijos
        foreach ($iterator->getChildren() as $key => $value) {
            echo $key . ' : ' . $value . "\n";
        }
    } else {
        echo "No hijos.\n";
    }

    $iterator->next();
}
?>

    
```php

El ejemplo anterior mostrará:

    No hijos.
    No hijos.
    a : manzana
    p : pera

## Véase también

`RecursiveArrayIterator::getChildren`
