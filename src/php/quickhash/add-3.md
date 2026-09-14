---
title: QuickHashIntStringHash::add
description: Este método añade una nueva entrada al hash
source_url: https://www.php.net/manual/es/quickhashintstringhash.add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashintstringhash/add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67240
---

QuickHashIntStringHash::add

Este método añade una nueva entrada al hash

## Descripción

```php
public QuickHashIntStringHash::add(int $key, string $value): bool
```php

Este método añade una nueva entrada al hash y devuelve si la entrada ha sido añadida. Las entradas se añaden por omisión siempre que `QuickHashIntStringHash::CHECK_FOR_DUPES` no haya sido pasado durante la creación del hash.

## Parámetros

`key`  
La clave de la entrada a añadir.

`value`  
El valor de la entrada a añadir. Si se pasa un valor no-string, se convertirá automáticamente en string si es posible.

## Valores devueltos

`true` cuando la entrada ha sido añadida, y `false` si la entrada no ha sido añadida.

## Ejemplos

Ejemplo de `QuickHashIntStringHash::add`

```
<?php
echo "sin verificación de duplicados\n";
$hash = new QuickHashIntStringHash( 1024 );
var_dump( $hash->exists( 4 ) );
var_dump( $hash->get( 4 ) );
var_dump( $hash->add( 4, "twenty two" ) );
var_dump( $hash->exists( 4 ) );
var_dump( $hash->get( 4 ) );
var_dump( $hash->add( 4, "twelve" ) );

echo "\ncon verificación de duplicados\n";
$hash = new QuickHashIntStringHash( 1024, QuickHashIntStringHash::CHECK_FOR_DUPES );
var_dump( $hash->exists( 4 ) );
var_dump( $hash->get( 4 ) );
var_dump( $hash->add( 4, "seventy eight" ) );
var_dump( $hash->exists( 4 ) );
var_dump( $hash->get( 4 ) );
var_dump( $hash->add( 4, "nine" ) );
?>

   
```php

Resultado del ejemplo anterior es similar a:

    sin verificación de duplicados
    bool(false)
    bool(false)
    bool(true)
    bool(true)
    string(10) "twenty two"
    bool(true)

    con verificación de duplicados
    bool(false)
    bool(false)
    bool(true)
    bool(true)
    string(13) "seventy eight"
    bool(false)
