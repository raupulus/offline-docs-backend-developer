---
title: FilesystemIterator::next
description: Moverse al siguiente fichero
source_url: https://www.php.net/manual/es/filesystemiterator.next.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/filesystemiterator/next.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 82070
---

FilesystemIterator::next

Moverse al siguiente fichero

## Descripción

```php
public FilesystemIterator::next(): void
```php

Moverse al siguiente fichero.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de FilesystemIterator::next

Lista el contenido de un directorio usando un bucle while.

```
<?php
$iterator = new FilesystemIterator(dirname(__FILE__));
while($iterator->valid()) {
    echo $iterator->getFilename() . "\n";
    $iterator->next();
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    manzana.jpg
    banana.jpg
    ejemplo.php

## Véase también

DirectoryIterator::next
