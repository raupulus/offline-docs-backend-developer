---
title: RegexIterator::getMode
description: Devuelve el modo de operación
source_url: https://www.php.net/manual/es/regexiterator.getmode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/regexiterator/getmode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 83670
---

RegexIterator::getMode

Devuelve el modo de operación

## Descripción

```php
public RegexIterator::getMode(): int
```php

Devuelve el modo de operación, véase RegexIterator::setMode para una lista de todos los modos de operación.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve los modos de operación.

## Ejemplos

Ejemplo de RegexIterator::getMode

```
<?php

$test = array ('str1' => 'test 1', 'teststr2' => 'otro test', 'str3' => 'test 123');

$arrayIterator = new ArrayIterator($test);
$regexIterator = new RegexIterator($arrayIterator, '/^[a-z]+/', RegexIterator::GET_MATCH);

$mode = $regexIterator->getMode();
if ($mode & RegexIterator::GET_MATCH) {
    echo 'Obteniendo la coincidencia para cada elemento.';
} elseif ($mode & RegexIterator::ALL_MATCHES) {
    echo 'Obteniendo las coincidencias para cada elemento.';
} elseif ($mode & RegexIterator::MATCH) {
    echo 'Obteniendo cada elemento si este coincide.';
} elseif ($mode & RegexIterator::SPLIT) {
    echo 'Obteniendo las piezas de cada elemento.';
}
?>

    
```php

El ejemplo anterior mostrará:

    Obteniendo la coincidencia para cada elemento.

## Véase también

RegexIterator::setMode
