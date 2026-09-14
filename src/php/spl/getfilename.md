---
title: DirectoryIterator::getFilename
description: Devuelve el nombre del fichero del elemento actual DirectoryIterator
source_url: https://www.php.net/manual/es/directoryiterator.getfilename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/directoryiterator/getfilename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 81850
---

DirectoryIterator::getFilename

Devuelve el nombre del fichero del elemento actual DirectoryIterator

## Descripción

```php
public DirectoryIterator::getFilename(): string
```php

Obtiene el nombre del elemento actual `DirectoryIterator`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el nombre del fichero del elemento actual `DirectoryIterator`.

## Ejemplos

Ejemplo de DirectoryIterator::getFilename

Este ejemplo mostrará el contenido de el directorio que contiene al script.

```
<?php
$dir = new DirectoryIterator(dirname(__FILE__));
foreach ($dir as $fileinfo) {
    echo $fileinfo->getFilename() . "\n";
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

DirectoryIterator::getBasename, DirectoryIterator::getPath, DirectoryIterator::getPathname, `pathinfo`
