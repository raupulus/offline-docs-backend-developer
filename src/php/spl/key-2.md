---
title: ArrayIterator::key
description: Devuelve la clave actual del array
source_url: https://www.php.net/manual/es/arrayiterator.key.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayiterator/key.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 81170
---

ArrayIterator::key

Devuelve la clave actual del array

## Descripción

```php
public ArrayIterator::key(): string
```php

Esta función devuelve la clave actual del array

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La clave actual del `array`.

## Ejemplos

Ejemplo de `ArrayIterator::key`

```
<?php
$array = array('key' => 'value');

$arrayobject = new ArrayObject($array);
$iterator = $arrayobject->getIterator();

echo $iterator->key(); //key
?>

    
```php
