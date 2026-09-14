---
title: DirectoryIterator::next
description: Avanza al siguiente elemento DirectoryIterator
source_url: https://www.php.net/manual/es/directoryiterator.next.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/directoryiterator/next.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 81880
---

DirectoryIterator::next

Avanza al siguiente elemento DirectoryIterator

## Descripción

```php
public DirectoryIterator::next(): void
```php

Avanzar al siguiente elemento `DirectoryIterator`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de DirectoryIterator::next

Lista el contenido de un directorio usando un bucle while.

```
<?php
$iterator = new DirectoryIterator(dirname(__FILE__));
while($iterator->valid()) {
    echo $iterator->getFilename() . "\n";
    $iterator->next();
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    .
    ..
    manzana.jpg
    banana.jpg
    index.php
    pera.jpg

## Véase también

DirectoryIterator::current, DirectoryIterator::key, DirectoryIterator::rewind, DirectoryIterator::valid, Iterator::next
