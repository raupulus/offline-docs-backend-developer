---
title: DirectoryIterator::valid
description: Comprueba si la actual posición de DirectoryIterator es un fichero válido
source_url: https://www.php.net/manual/es/directoryiterator.valid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/directoryiterator/valid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 81920
---

DirectoryIterator::valid

Comprueba si la actual posición de DirectoryIterator es un fichero válido

## Descripción

```php
public DirectoryIterator::valid(): bool
```php

Comprobar si la posición actual de `DirectoryIterator` es un fichero válido.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si la posición es válida, en caso contrario `false`

## Ejemplos

Ejemplo de DirectoryIterator::valid

```
<?php
$iterator = new DirectoryIterator(dirname(__FILE__));

// Bucle hasta el final del iterador
while($iterator->valid()) {
    $iterator->next();
}

$iterator->valid(); // FALSE
$iterator->rewind();
$iterator->valid(); // TRUE

?>

    
```php

## Véase también

DirectoryIterator::current, DirectoryIterator::key, DirectoryIterator::next, DirectoryIterator::rewind, Iterator::valid
