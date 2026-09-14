---
title: ArrayIterator::rewind
description: Rebobinar array al inicio
source_url: https://www.php.net/manual/es/arrayiterator.rewind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayiterator/rewind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 81260
---

ArrayIterator::rewind

Rebobinar array al inicio

## Descripción

```php
public ArrayIterator::rewind(): void
```php

Rebobina el iterador al inicio del array.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `ArrayIterator::rewind`

```
<?php
$arrayobject = new ArrayObject();

$arrayobject[] = 'zero';
$arrayobject[] = 'one';
$arrayobject[] = 'two';

$iterator = $arrayobject->getIterator();

$iterator->next();
echo $iterator->key(); //1

$iterator->rewind(); //rebobinar al inicio
echo $iterator->key(); //0
?>

    
```php
