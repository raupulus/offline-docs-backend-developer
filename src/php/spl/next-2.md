---
title: ArrayIterator::next
description: Desplaza a la siguiente entrada
source_url: https://www.php.net/manual/es/arrayiterator.next.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayiterator/next.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: dfd68fd22
order: 81210
---

ArrayIterator::next

Desplaza a la siguiente entrada

## Descripción

```php
public ArrayIterator::next(): void
```php

Mueve el iterador a la siguiente entrada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `ArrayIterator::next`

```
<?php
$arrayobject = new ArrayObject();

$arrayobject[] = 'cero';
$arrayobject[] = 'uno';

$iterator = $arrayobject->getIterator();

while($iterator->valid()) {
    echo $iterator->key() . ' => ' . $iterator->current() . "\n";

    $iterator->next();
}
?>

    
```php

El ejemplo anterior mostrará:

    0 => cero
    1 => uno
