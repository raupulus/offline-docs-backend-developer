---
title: QuickHashStringIntHash::saveToString
description: Este método devuelve una versión serializada del hash
source_url: https://www.php.net/manual/es/quickhashstringinthash.savetostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashstringinthash/savetostring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67460
---

QuickHashStringIntHash::saveToString

Este método devuelve una versión serializada del hash

## Descripción

```php
public QuickHashStringIntHash::saveToString(): string
```php

Este método devuelve una versión serializada del hash en el mismo formato que QuickHashStringIntHash::loadFromString puede leer.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Este método devuelve una versión serializada del hash, en el mismo formato que QuickHashStringIntHash::loadFromString puede leer.

## Ejemplos

Ejemplo de `QuickHashStringIntHash::saveToString`

```
<?php
$hash = new QuickHashStringIntHash( 1024 );
var_dump( $hash->add( "forty three", 42 ) );
var_dump( $hash->add( "fifty two", 52 ) );

var_dump( $hash->saveToString() );
?>

   
```php
