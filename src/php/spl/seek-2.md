---
title: DirectoryIterator::seek
description: Mueve el apuntador interno del elemento DirectoryIterator
source_url: https://www.php.net/manual/es/directoryiterator.seek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/directoryiterator/seek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 81900
---

DirectoryIterator::seek

Mueve el apuntador interno del elemento DirectoryIterator

## Descripción

```php
public DirectoryIterator::seek(int $offset): void
```php

Mueve el apuntador interno a la posición dada en el elemento `DirectoryIterator`.

## Parámetros

`offset`  
La base cero de la posición numérica a mover el apuntador interno.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de DirectoryIterator::seek

Mueve el apuntador interno al cuarto elemento en el directorio que contiene al script. Los primeros dos son generalmente `.` y `..`

```
<?php
$iterator = new DirectoryIterator(dirname(__FILE__));
$iterator->seek(3);
if ($iterator->valid()) {
    echo $iterator->getFilename();
} else {
    echo 'No hay fichero en la posición 3';
}
?>

    
```php

## Véase también

DirectoryIterator::rewind, DirectoryIterator::next, SeekableIterator::seek
