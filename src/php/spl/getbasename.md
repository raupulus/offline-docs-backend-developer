---
title: DirectoryIterator::getBasename
description: Obtener el nombre base del elemento actual DirectoryIterator
source_url: https://www.php.net/manual/es/directoryiterator.getbasename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/directoryiterator/getbasename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 81830
---

DirectoryIterator::getBasename

Obtener el nombre base del elemento actual DirectoryIterator

## Descripción

```php
public DirectoryIterator::getBasename([string $suffix]): string
```php

Obtiene el nombre base del elemento actual `DirectoryIterator`.

## Parámetros

`suffix`  
Si el nombre base termina en `suffix`, este será cortado.

## Valores devueltos

El nombre base del elemento actual `DirectoryIterator`.

## Ejemplos

Ejemplo de DirectoryIterator::getBasename

Este ejemplo mostrará una lista completa de los nombres base y los nombres base con sufijo `.jpg` eliminado de los ficheros del directorio que contiene el script.

```
<?php
$dir = new DirectoryIterator(dirname(__FILE__));
foreach ($dir as $fileinfo) {
    if ($fileinfo->isFile()) {
        echo $fileinfo->getBasename() . "\n";
        echo $fileinfo->getBasename('.jpg') . "\n";
    }
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    manzana.jpg
    manzana
    banana.jpg
    banana
    index.php
    index.php
    pera.jpg
    pera

## Véase también

DirectoryIterator::getFilename, DirectoryIterator::getPath, DirectoryIterator::getPathname, `basename`, `pathinfo`
