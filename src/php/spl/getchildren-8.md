---
title: RecursiveRegexIterator::getChildren
description: Devuelve un iterador para la entrada actual
source_url: https://www.php.net/manual/es/recursiveregexiterator.getchildren.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/recursiveregexiterator/getchildren.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 83420
---

RecursiveRegexIterator::getChildren

Devuelve un iterador para la entrada actual

## Descripción

```php
public RecursiveRegexIterator::getChildren(): RecursiveRegexIterator
```php

Devuelve un iterador para la entrada actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un iterador para la entrada actual, si este puede se puede iterar sobre el iterador interno.

## Errores/Excepciones

Se lanza una `InvalidArgumentException` si la entrada actual no contiene un valor que pueda ser iterado sobre el iterador interno.

## Ejemplos

Ejemplo de `RecursiveRegexIterator::getChildren`

```
<?php
$rArrayIterator = new RecursiveArrayIterator(array('test1', array('tet3', 'test4', 'test5')));
$rRegexIterator = new RecursiveRegexIterator($rArrayIterator, '/^test/',
    RecursiveRegexIterator::ALL_MATCHES);

foreach ($rRegexIterator as $key1 => $value1) {

    if ($rRegexIterator->hasChildren()) {

        // imprime todos los hijos
        echo "Hijos: ";
        foreach ($rRegexIterator->getChildren() as $key => $value) {
            echo $value . " ";
        }
        echo "\n";
    } else {
        echo "No tiene hijos\n";
    }

}
?>

    
```php

El ejemplo anterior mostrará:

    No tiene hijos
    Hijos: test4 test5

## Véase también

`RecursiveRegexIterator::hasChildren`
