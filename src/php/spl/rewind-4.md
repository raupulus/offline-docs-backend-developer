---
title: DirectoryIterator::rewind
description: Robobina DirectoryIterator hasta volver al inicio
source_url: https://www.php.net/manual/es/directoryiterator.rewind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/directoryiterator/rewind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 81890
---

DirectoryIterator::rewind

Robobina DirectoryIterator hasta volver al inicio

## Descripción

```php
public DirectoryIterator::rewind(): void
```php

Robobinar `DirectoryIterator` hasta volver al inicio.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de DirectoryIterator::rewind

```
<?php
$iterator = new DirectoryIterator(dirname(__FILE__));

$iterator->next();
echo $iterator->key(); //1

$iterator->rewind(); //Rebobinándose al inicio
echo $iterator->key(); //0
?>

    
```php

## Véase también

DirectoryIterator::current, DirectoryIterator::key, DirectoryIterator::next, DirectoryIterator::valid, Iterator::rewind
