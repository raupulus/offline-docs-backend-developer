---
title: RegexIterator::accept
description: Obtener el estado de aceptación
source_url: https://www.php.net/manual/es/regexiterator.accept.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/regexiterator/accept.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 83640
---

RegexIterator::accept

Obtener el estado de aceptación

## Descripción

```php
public RegexIterator::accept(): bool
```php

Coincidir `(string)` RegexIterator::current (o RegexIterator::key si la flag [RegexIterator::USE_KEY](#regexiterator.constants.use-key) está establecida) con la expresión regular.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` si coincide, en caso contrario `false`.

## Ejemplos

RegexIterator::accept example

Este ejemplo muestra sólo los elementos aceptados que coinciden con la expresión regular.

```
<?php
$names = new ArrayIterator(array('Ann', 'Bob', 'Charlie', 'David'));
$filter = new RegexIterator($names, '/^[B-D]/');
foreach ($filter as $name) {
    echo $name . PHP_EOL;
}
?>

    
```php

El ejemplo anterior mostrará:

    Bob
    Charlie
    David

## Véase también

[RegexIterator constants](#regexiterator.constants), RegexIterator::setFlags
