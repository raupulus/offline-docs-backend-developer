---
title: QuickHashStringIntHash::saveToFile
description: Este método almacena un hash en memoria en el disco
source_url: https://www.php.net/manual/es/quickhashstringinthash.savetofile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashstringinthash/savetofile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67450
---

QuickHashStringIntHash::saveToFile

Este método almacena un hash en memoria en el disco

## Descripción

```php
public QuickHashStringIntHash::saveToFile(string $filename): void
```php

Este método almacena un hash existente en un fichero en el disco, en el mismo formato que loadFromFile() puede leer.

## Parámetros

`filename`  
El nombre del fichero donde almacenar el hash.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `QuickHashStringIntHash::saveToFile`

```
<?php
$hash = new QuickHashStringIntHash( 1024 );
var_dump( $hash->add( "forty three", 42 ) );
var_dump( $hash->add( "fifty two", 52 ) );

$hash->saveToFile( '/tmp/test.hash.string' );
?>

   
```php
