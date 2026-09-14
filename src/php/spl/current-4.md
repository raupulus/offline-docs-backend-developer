---
title: DirectoryIterator::current
description: Devuelve el elemento actual del DirectoryIterator
source_url: https://www.php.net/manual/es/directoryiterator.current.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/directoryiterator/current.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: d51166ca1
order: 81820
---

DirectoryIterator::current

Devuelve el elemento actual del DirectoryIterator

## Descripción

```php
public DirectoryIterator::current(): mixed
```php

Obtiene el elemento actual del `DirectoryIterator`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El elemento actual del `DirectoryIterator`.

## Ejemplos

Ejemplo de DirectoryIterator::current

Este ejemplo mostrará el contenido del directorio que contiene al script.

```
<?php
$iterador = new DirectoryIterator(__DIR__);
while($iterador->valid()) {
    $fichero = $iterador->current();
    echo $iterador->key() . " => " . $fichero->getFilename() . "\n";
    $iterador->next();
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    0 => .
    1 => ..
    2 => manzana.jpg
    3 => banana.jpg
    4 => index.php
    5 => pera.jpg

## Véase también

DirectoryIterator::key, DirectoryIterator::next, DirectoryIterator::rewind, DirectoryIterator::valid, Iterator::current
