---
title: QuickHashIntSet::saveToFile
description: Este método almacena un conjunto en memoria en disco
source_url: https://www.php.net/manual/es/quickhashintset.savetofile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashintset/savetofile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67210
---

QuickHashIntSet::saveToFile

Este método almacena un conjunto en memoria en disco

## Descripción

```php
public QuickHashIntSet::saveToFile(string $filename): void
```php

Este método almacena un conjunto existente en un fichero en disco, en el mismo formato que QuickHashIntSet::loadFromFile puede leer.

## Parámetros

`filename`  
El nombre del fichero en el cual almacenar el conjunto.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `QuickHashIntSet::saveToFile`

```
<?php
$set = new QuickHashIntSet( 1024 );
var_dump( $set->exists( 4 ) );
var_dump( $set->add( 4 ) );
var_dump( $set->exists( 4 ) );
var_dump( $set->add( 4 ) );

$set->saveToFile( '/tmp/test.set' );
?>

   
```php
