---
title: DirectoryIterator::key
description: Devuelve la entrada actual del directorio
source_url: https://www.php.net/manual/es/directoryiterator.key.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/directoryiterator/key.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: d51166ca1
order: 81870
---

DirectoryIterator::key

Devuelve la entrada actual del directorio

## Descripción

```php
public DirectoryIterator::key(): mixed
```php

Devuelve la entrada actual del objeto `DirectoryIterator`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La clave para la entrada actual de `DirectoryIterator` como `int`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Cuando el iterador no está inicializado, ahora se lanza una `Error`. Anteriormente, el método devolvía `false`. |

## Ejemplos

Ejemplo con DirectoryIterator::key

```
<?php
$dir = new DirectoryIterator(dirname(__FILE__));
foreach ($dir as $fileinfo) {
    if (!$fileinfo->isDot()) {
        echo $fileinfo->key() . " => " . $fileinfo->getFilename() . "\n";
    }
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    0 => apple.jpg
    1 => banana.jpg
    2 => index.php
    3 => pear.jpg

## Véase también

DirectoryIterator::current, DirectoryIterator::next, DirectoryIterator::rewind, DirectoryIterator::valid, Iterator::key
