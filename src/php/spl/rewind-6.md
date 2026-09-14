---
title: FilesystemIterator::rewind
description: Reinicia la lectura del directorio
source_url: https://www.php.net/manual/es/filesystemiterator.rewind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/filesystemiterator/rewind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: d51166ca1
order: 82080
---

FilesystemIterator::rewind

Reinicia la lectura del directorio

## Descripción

```php
public FilesystemIterator::rewind(): void
```php

Reinicia la lectura del directorio desde el principio.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con FilesystemIterator::rewind

```
<?php
$iterator = new FilesystemIterator(dirname(__FILE__), FilesystemIterator::KEY_AS_FILENAME);

echo $iterator->key() . "\n";

$iterator->next();
echo $iterator->key() . "\n";

$iterator->rewind();
echo $iterator->key() . "\n";
?>

    
```php

Resultado del ejemplo anterior es similar a:

    apple.jpg
    banana.jpg
    apple.jpg

## Véase también

DirectoryIterator::rewind
