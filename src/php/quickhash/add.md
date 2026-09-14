---
title: QuickHashIntHash::add
description: Este método añade una nueva entrada al hash
source_url: https://www.php.net/manual/es/quickhashinthash.add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashinthash/add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67010
---

QuickHashIntHash::add

Este método añade una nueva entrada al hash

## Descripción

```php
public QuickHashIntHash::add(int $key, [int $value]): bool
```php

Este método añade una nueva entrada al hash y devuelve si la entrada ha sido añadida. Las entradas se añaden por omisión siempre que `QuickHashIntHash::CHECK_FOR_DUPES` no haya sido pasado durante la creación del hash.

## Parámetros

`key`  
La clave de la entrada a añadir.

`value`  
El valor opcional de la entrada a añadir. Si no se especifica ningún valor, `1` será utilizado.

## Valores devueltos

`true` cuando la entrada ha sido añadida, y `false` si la entrada no ha sido añadida.

## Ejemplos

Ejemplo de `QuickHashIntHash::add`

```
<?php
echo "sin verificación de duplicados\n";
$hash = new QuickHashIntHash( 1024 );
var_dump( $hash->exists( 4 ) );
var_dump( $hash->get( 4 ) );
var_dump( $hash->add( 4, 22 ) );
var_dump( $hash->exists( 4 ) );
var_dump( $hash->get( 4 ) );
var_dump( $hash->add( 4, 12 ) );

echo "\ncon verificación de duplicados\n";
$hash = new QuickHashIntHash( 1024, QuickHashIntHash::CHECK_FOR_DUPES );
var_dump( $hash->exists( 4 ) );
var_dump( $hash->get( 4 ) );
var_dump( $hash->add( 4, 78 ) );
var_dump( $hash->exists( 4 ) );
var_dump( $hash->get( 4 ) );
var_dump( $hash->add( 4, 9 ) );

echo "\nvalor por omisión\n";
var_dump( $hash->add( 5 ) );
var_dump( $hash->get( 5 ) );
?>

   
```php

Resultado del ejemplo anterior es similar a:

    sin verificación de duplicados
    bool(false)
    bool(false)
    bool(true)
    bool(true)
    int(22)
    bool(true)

    con verificación de duplicados
    bool(false)
    bool(false)
    bool(true)
    bool(true)
    int(78)
    bool(false)

    valor por omisión
    bool(true)
    int(1)
