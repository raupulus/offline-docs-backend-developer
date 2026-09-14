---
title: QuickHashIntHash::saveToString
description: Este método devuelve una versión serializada del hash
source_url: https://www.php.net/manual/es/quickhashinthash.savetostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashinthash/savetostring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67100
---

QuickHashIntHash::saveToString

Este método devuelve una versión serializada del hash

## Descripción

```php
public QuickHashIntHash::saveToString(): string
```php

Este método devuelve una versión serializada del hash en el mismo formato que QuickHashIntHash::loadFromString puede leer.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Este método devuelve una string que contiene una versión serializada del hash. Cada elemento se almacena como un valor de cuatro bytes en el Endianness que el sistema actual utiliza.

## Ejemplos

Ejemplo de `QuickHashIntHash::saveToString`

```
<?php
$hash = new QuickHashIntHash( 1024 );
var_dump( $hash->exists( 4 ) );
var_dump( $hash->add( 4, 34 ) );
var_dump( $hash->exists( 4 ) );
var_dump( $hash->add( 4, 55 ) );

var_dump( $hash->saveToString() );
?>

   
```php
