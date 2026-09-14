---
title: QuickHashStringIntHash::add
description: Este método añade una nueva entrada al hash
source_url: https://www.php.net/manual/es/quickhashstringinthash.add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashstringinthash/add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67370
---

QuickHashStringIntHash::add

Este método añade una nueva entrada al hash

## Descripción

```php
public QuickHashStringIntHash::add(string $key, int $value): bool
```php

Este método añade una nueva entrada al hash y devuelve si la entrada ha sido añadida. Por omisión, las entradas siempre se añaden a menos que `QuickHashStringIntHash::CHECK_FOR_DUPES` haya sido pasado durante la creación del hash.

## Parámetros

`key`  
La clave de la entrada a añadir.

`value`  
El valor de la entrada a añadir.

## Valores devueltos

`true` cuando la entrada ha sido añadida, y `false` si la entrada no ha sido añadida.

## Ejemplos

Ejemplo de `QuickHashStringIntHash::add`

```
<?php
echo "sin verificación de duplicados\n";
$hash = new QuickHashStringIntHash( 1024 );
var_dump( $hash );
var_dump( $hash->exists( "four" ) );
var_dump( $hash->get( "four" ) );
var_dump( $hash->add( "four", 22 ) );
var_dump( $hash->exists( "four" ) );
var_dump( $hash->get( "four" ) );
var_dump( $hash->add( "four", 12 ) );

echo "\ncon verificación de duplicados\n";
$hash = new QuickHashStringIntHash( 1024, QuickHashStringIntHash::CHECK_FOR_DUPES );
var_dump( $hash );
var_dump( $hash->exists( "four" ) );
var_dump( $hash->get( "four" ) );
var_dump( $hash->add( "four", 78 ) );
var_dump( $hash->exists( "four" ) );
var_dump( $hash->get( "four" ) );
var_dump( $hash->add( "four", 9 ) );
?>

   
```php

Resultado del ejemplo anterior es similar a:

    sin verificación de duplicados
    object(QuickHashStringIntHash)#1 (0) {
    }
    bool(false)
    bool(false)
    bool(true)
    bool(true)
    int(22)
    bool(true)

    con verificación de duplicados
    object(QuickHashStringIntHash)#2 (0) {
    }
    bool(false)
    bool(false)
    bool(true)
    bool(true)
    int(78)
    bool(false)
