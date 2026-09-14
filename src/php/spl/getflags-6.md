---
title: RegexIterator::getFlags
description: Obtener flags
source_url: https://www.php.net/manual/es/regexiterator.getflags.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/regexiterator/getflags.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 83660
---

RegexIterator::getFlags

Obtener flags

## Descripción

```php
public RegexIterator::getFlags(): int
```php

Devuelve las flags, véase RegexIterator::setFlags para una lista de todas las flags disponibles.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve las flags establecidas.

## Ejemplos

Ejemplo de RegexIterator::getFlags

```
<?php

$test = array ('str1' => 'test 1', 'teststr2' => 'another test', 'str3' => 'test 123');

$arrayIterator = new ArrayIterator($test);
$regexIterator = new RegexIterator($arrayIterator, '/^test/');
$regexIterator->setFlags(RegexIterator::USE_KEY);

if ($regexIterator->getFlags() & RegexIterator::USE_KEY) {
    echo 'Filtrado basado en las claves del array.';
} else {
    echo 'Filtrado basado en los valores del array.';
}
?>

    
```php

El ejemplo anterior mostrará:

    Filtrado basado en las claves del array.

## Véase también

RegexIterator::setFlags
