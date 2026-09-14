---
title: ArrayIterator::valid
description: Comprueba si un array contiene más entradas
source_url: https://www.php.net/manual/es/arrayiterator.valid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayiterator/valid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 81330
---

ArrayIterator::valid

Comprueba si un array contiene más entradas

## Descripción

```php
public ArrayIterator::valid(): bool
```php

Comprueba si un `array` contiene más entradas.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si el iterador es válido, `false` si no.

## Ejemplos

Ejemplo de `ArrayIterator::valid`

```
<?php
$array = array('1' => 'uno');

$arrayobject = new ArrayObject($array);
$iterator = $arrayobject->getIterator();

var_dump($iterator->valid()); //bool(true)

$iterator->next(); // avanza al siguiente ítem

//bool(false) porque solo hay un elemento array
var_dump($iterator->valid());
?>

    
```php
