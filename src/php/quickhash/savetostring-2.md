---
title: QuickHashIntSet::saveToString
description: Este método devuelve una versión serializada del conjunto
source_url: https://www.php.net/manual/es/quickhashintset.savetostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashintset/savetostring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67220
---

QuickHashIntSet::saveToString

Este método devuelve una versión serializada del conjunto

## Descripción

```php
public QuickHashIntSet::saveToString(): string
```php

Este método devuelve una versión serializada del conjunto en el mismo formato que QuickHashIntSet::loadFromString puede leer.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Este método devuelve una string que contiene una versión serializada del conjunto. Cada elemento se almacena como un valor de cuatro bytes en el orden de bytes que el sistema actual utiliza.

## Ejemplos

Ejemplo de `QuickHashIntSet::saveToString`

```
<?php
$set = new QuickHashIntSet( 1024 );
var_dump( $set->exists( 4 ) );
var_dump( $set->add( 4 ) );
var_dump( $set->exists( 4 ) );
var_dump( $set->add( 4 ) );

var_dump( $set->saveToString() );
?>

   
```php
