---
title: RegexIterator::getPregFlags
description: Devuelve las flags de expresión regular
source_url: https://www.php.net/manual/es/regexiterator.getpregflags.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/regexiterator/getpregflags.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 83680
---

RegexIterator::getPregFlags

Devuelve las flags de expresión regular

## Descripción

```php
public RegexIterator::getPregFlags(): int
```php

Devuelve las flags de expresión regular, véase RegexIterator::\_\_construct para una lista de todas las flags.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un bitmask de las flags de expresión regular.

## Ejemplos

Ejemplo de RegexIterator::getPregFlags

```
<?php

$test = array ('str1' => 'test 1', 'teststr2' => 'otro test', 'str3' => 'test 123');

$arrayIterator = new ArrayIterator($test);
$regexIterator = new RegexIterator($arrayIterator, '/\s/', RegexIterator::SPLIT);
$regexIterator->setPregFlags(PREG_SPLIT_NO_EMPTY | PREG_SPLIT_OFFSET_CAPTURE);

if ($regexIterator->getPregFlags() & PREG_SPLIT_NO_EMPTY) {
    echo 'Ignorando las piezas vacías';
} else {
    echo 'No ignora piezas vacías';
}

?>

    
```php

El ejemplo anterior mostrará:

    Ignorando las piezas vacías

## Véase también

RegexIterator::setPregFlags
