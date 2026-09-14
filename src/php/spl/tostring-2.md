---
title: DirectoryIterator::__toString
description: Lee el nombre del fichero
source_url: https://www.php.net/manual/es/directoryiterator.tostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/directoryiterator/tostring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: bfef87dc1
order: 81910
---

DirectoryIterator::\_\_toString

Lee el nombre del fichero

## Descripción

```php
public DirectoryIterator::__toString(): string
```php

Lee el nombre del fichero del elemento `DirectoryIterator` actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el nombre del fichero actual del elemento `DirectoryIterator`.

## Ejemplos

Ejemplo con DirectoryIterator::\_\_toString

Este ejemplo va a listar los elementos del directorio actual.

```
<?php
$dir = new DirectoryIterator(dirname(__FILE__));
foreach ($dir as $fileinfo) {
    echo $fileinfo;
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    .
    ..
    apple.jpg
    banana.jpg
    index.php
    pear.jpg

## Véase también

DirectoryIterator::getFilename, el método mágico [\_\_toString](#object.tostring)
