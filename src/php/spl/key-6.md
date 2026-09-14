---
title: FilesystemIterator::key
description: Lee el nombre del fichero
source_url: https://www.php.net/manual/es/filesystemiterator.key.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/filesystemiterator/key.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: a7d00d0b9
order: 82060
---

FilesystemIterator::key

Lee el nombre del fichero

## Descripción

```php
public FilesystemIterator::key(): string
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la ruta o el nombre del fichero, según las opciones activadas. Véase las [Constantes de `FilesystemIterator`](#filesystemiterator.constants).

## Ejemplos

Ejemplo con FilesystemIterator::key

Este ejemplo mostrará el contenido del directorio que contiene el script en curso.

```
<?php
$iterator = new FilesystemIterator(dirname(__FILE__), FilesystemIterator::KEY_AS_FILENAME);
foreach ($iterator as $fileinfo) {
    echo $iterator->key() . "\n";
}
?>

    
```php

Resultado del ejemplo anterior en PHP 8.2 es similar a:

    .
    ..
    apple.jpg
    banana.jpg
    example.php

## Véase también

[Constantes de `FilesystemIterator`](#filesystemiterator.constants), DirectoryIterator::key, DirectoryIterator::getFilename, DirectoryIterator::getPathname
