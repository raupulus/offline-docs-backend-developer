---
title: spl_classes
description: Devuelve las clases SPL disponibles
source_url: https://www.php.net/manual/es/function.spl-classes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/functions/spl-classes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 14af302c9
order: 82310
---

spl_classes

Devuelve las clases SPL disponibles

## Descripción

```php
spl_classes(): array
```php

Esta función devuelve un array con las clases SPL actualmente disponibles.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `array` que contiene las clases SPL actualmente disponibles.

## Ejemplos

Ejemplo de `spl_classes`

```
<?php

print_r(spl_classes());

?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [ArrayObject] => ArrayObject
        [ArrayIterator] => ArrayIterator
        [CachingIterator] => CachingIterator
        [RecursiveCachingIterator] => RecursiveCachingIterator
        [DirectoryIterator] => DirectoryIterator
        [FilterIterator] => FilterIterator
        [LimitIterator] => LimitIterator
        [ParentIterator] => ParentIterator
        [RecursiveDirectoryIterator] => RecursiveDirectoryIterator
        [RecursiveIterator] => RecursiveIterator
        [RecursiveIteratorIterator] => RecursiveIteratorIterator
        [SeekableIterator] => SeekableIterator
        [SimpleXMLIterator] => SimpleXMLIterator
    )
