---
title: QuickHashIntHash::saveToFile
description: Este método almacena un hash en memoria en disco
source_url: https://www.php.net/manual/es/quickhashinthash.savetofile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashinthash/savetofile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67090
---

QuickHashIntHash::saveToFile

Este método almacena un hash en memoria en disco

## Descripción

```php
public QuickHashIntHash::saveToFile(string $filename): void
```php

Este método almacena un hash existente en un fichero en disco, en el mismo formato que QuickHashIntHash::loadFromFile puede leer.

## Parámetros

`filename`  
El nombre del fichero en el cual almacenar el hash.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `QuickHashIntHash::saveToFile`

```
<?php
$hash = new QuickHashIntHash( 1024 );
var_dump( $hash->exists( 4 ) );
var_dump( $hash->add( 4, 43 ) );
var_dump( $hash->exists( 4 ) );
var_dump( $hash->add( 4, 52 ) );

$hash->saveToFile( '/tmp/test.hash' );
?>

   
```php
