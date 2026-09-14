---
title: RecursiveRegexIterator::hasChildren
description: Retorna si un iterador puede ser obtenido de la entrada actual
source_url: https://www.php.net/manual/es/recursiveregexiterator.haschildren.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/recursiveregexiterator/haschildren.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 83430
---

RecursiveRegexIterator::hasChildren

Retorna si un iterador puede ser obtenido de la entrada actual

## Descripción

```php
public RecursiveRegexIterator::hasChildren(): bool
```php

Retorna si un iterador puede ser obtenido de la entrada actual. Este iterador puede ser obtenido mediante RecursiveRegexIterator::getChildren.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si un iterador puede ser obtenido de la entrada actual, en caso contrario `false`.

## Ejemplos

Ejemplo de `RecursiveRegexIterator::hasChildren`

```
<?php
$rArrayIterator = new RecursiveArrayIterator(array('test1', array('tet3', 'test4', 'test5')));
$rRegexIterator = new RecursiveRegexIterator($rArrayIterator, '/^test/',
    RecursiveRegexIterator::ALL_MATCHES);

foreach ($rRegexIterator as $value) {
    var_dump($rRegexIterator->hasChildren());
}
?>

    
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(true)

## Véase también

`RecursiveRegexIterator::getChildren`
