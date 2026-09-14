---
title: FilesystemIterator::current
description: Lee el fichero actual
source_url: https://www.php.net/manual/es/filesystemiterator.current.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/filesystemiterator/current.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: a7d00d0b9
order: 82040
---

FilesystemIterator::current

Lee el fichero actual

## Descripción

```php
public FilesystemIterator::current(): string
```php

Lee las informaciones sobre el fichero actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El nombre del fichero, las informaciones del fichero, o bien `$this`, en función de las opciones utilizadas. Véase la [lista de constantes `FilesystemIterator`](#filesystemiterator.constants).

## Ejemplos

Ejemplo con FilesystemIterator::current

Este ejemplo va a probar la lista de ficheros en el script actual.

```
<?php
$iterator = new FilesystemIterator(__DIR__, FilesystemIterator::CURRENT_AS_PATHNAME);
foreach ($iterator as $fileinfo) {
    echo $iterator->current() . "\n";
}
?>

    
```php

Resultado del ejemplo anterior en PHP 8.2 es similar a:

    /www/examples/.
    /www/examples/..
    /www/examples/apple.jpg
    /www/examples/banana.jpg
    /www/examples/example.php

## Véase también

Las [constantes FilesystemIterator](#filesystemiterator.constants), DirectoryIterator::current, DirectoryIterator::getFileName
