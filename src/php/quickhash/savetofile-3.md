---
title: QuickHashIntStringHash::saveToFile
description: Este método almacena un hash en memoria en disco
source_url: https://www.php.net/manual/es/quickhashintstringhash.savetofile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashintstringhash/savetofile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67320
---

QuickHashIntStringHash::saveToFile

Este método almacena un hash en memoria en disco

## Descripción

```php
public QuickHashIntStringHash::saveToFile(string $filename): void
```php

Este método almacena un hash existente en un fichero en disco, en el mismo formato que loadFromFile() puede leer.

## Parámetros

`filename`  
El nombre del fichero donde almacenar el hash.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `QuickHashIntStringHash::saveToFile`

```
<?php
$hash = new QuickHashIntStringHash( 1024 );
var_dump( $hash->exists( 4 ) );
var_dump( $hash->add( 4, "forty three" ) );
var_dump( $hash->exists( 4 ) );
var_dump( $hash->add( 4, "fifty two" ) );

$hash->saveToFile( '/tmp/test.string.hash' );
?>

   
```php
