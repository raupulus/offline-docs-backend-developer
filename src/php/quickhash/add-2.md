---
title: QuickHashIntSet::add
description: Este método añade una nueva entrada al conjunto
source_url: https://www.php.net/manual/es/quickhashintset.add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashintset/add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67140
---

QuickHashIntSet::add

Este método añade una nueva entrada al conjunto

## Descripción

```php
public QuickHashIntSet::add(int $key): bool
```php

Este método añade una nueva entrada al conjunto y devuelve si la entrada ha sido añadida. Las entradas se añaden por omisión siempre que `QuickHashIntSet::CHECK_FOR_DUPES` no haya sido pasado durante la creación del conjunto.

## Parámetros

`key`  
La clave de la entrada a añadir.

## Valores devueltos

`true` cuando la entrada ha sido añadida, y `false` si la entrada no ha sido añadida.

## Ejemplos

Ejemplo de `QuickHashIntSet::add`

```
<?php
echo "sin verificación de duplicados\n";
$set = new QuickHashIntSet( 1024 );
var_dump( $set->exists( 4 ) );
var_dump( $set->add( 4 ) );
var_dump( $set->exists( 4 ) );
var_dump( $set->add( 4 ) );

echo "\ncon verificación de duplicados\n";
$set = new QuickHashIntSet( 1024, QuickHashIntSet::CHECK_FOR_DUPES );
var_dump( $set->exists( 4 ) );
var_dump( $set->add( 4 ) );
var_dump( $set->exists( 4 ) );
var_dump( $set->add( 4 ) );
?>

   
```php

Resultado del ejemplo anterior es similar a:

    sin verificación de duplicados
    bool(false)
    bool(true)
    bool(true)
    bool(true)

    con verificación de duplicados
    bool(false)
    bool(true)
    bool(true)
    bool(false)
