---
title: QuickHashStringIntHash::set
description: Este método actualiza una entrada en el hash con un nuevo valor, o añade
  una nueva entrada si la entrada no existe
source_url: https://www.php.net/manual/es/quickhashstringinthash.set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashstringinthash/set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67470
---

QuickHashStringIntHash::set

Este método actualiza una entrada en el hash con un nuevo valor, o añade una nueva entrada si la entrada no existe

## Descripción

```php
public QuickHashStringIntHash::set(string $key, int $value): int
```php

Este método actualiza una entrada con un nuevo valor. Si la entrada no existía, añadirá una nueva entrada. Devuelve si la entrada ha sido añadida o actualizada. Si hay claves duplicadas, solo el primer elemento encontrado será actualizado. Utilice QuickHashStringIntHash::CHECK_FOR_DUPES al crear el hash para evitar que las claves duplicadas formen parte del hash.

## Parámetros

`key`  
La clave de la entrada a añadir o actualizar.

`value`  
El valor de la entrada a añadir. Si se pasa un valor no string, será convertido a string automáticamente si es posible.

## Valores devueltos

2 si la entrada ha sido encontrada y actualizada, 1 si la entrada ha sido nuevamente añadida o 0 si ha habido un error.

## Ejemplos

Ejemplo de `QuickHashStringIntHash::set`

```
<?php
$hash = new QuickHashStringIntHash( 1024 );

echo "Set->Add\n";
var_dump( $hash->get( "forty six thousand six hundred ninety two" ) );
var_dump( $hash->set( "forty six thousand six hundred ninety two", 16091 ) );
var_dump( $hash->get( "forty six thousand six hundred ninety two" ) );

echo "Set->Update\n";
var_dump( $hash->set( "forty six thousand six hundred ninety two", 29906 ) );
var_dump( $hash->get( "forty six thousand six hundred ninety two" ) );
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Set->Add
    bool(false)
    int(2)
    int(16091)
    Set->Update
    int(1)
    int(29906)
