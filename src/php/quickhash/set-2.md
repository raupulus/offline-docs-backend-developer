---
title: QuickHashIntStringHash::set
description: Este método actualiza una entrada en el hash con un nuevo valor, o añade
  una nueva entrada si la entrada no existe
source_url: https://www.php.net/manual/es/quickhashintstringhash.set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashintstringhash/set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67340
---

QuickHashIntStringHash::set

Este método actualiza una entrada en el hash con un nuevo valor, o añade una nueva entrada si la entrada no existe

## Descripción

```php
public QuickHashIntStringHash::set(int $key, string $value): int
```php

Este método intenta actualizar una entrada con un nuevo valor. Si la entrada no existía, añadirá una nueva entrada. Devuelve si la entrada ha sido añadida o actualizada. Si hay claves duplicadas, solo el primer elemento encontrado será actualizado. Utilice QuickHashIntStringHash::CHECK_FOR_DUPES al crear el hash para evitar que las claves duplicadas formen parte del hash.

## Parámetros

`key`  
La clave de la entrada a añadir o actualizar.

`value`  
El valor de la entrada a añadir. Si se pasa un valor que no es una string, será convertido automáticamente a string si es posible.

## Valores devueltos

2 si la entrada ha sido encontrada y actualizada, 1 si la entrada ha sido nuevamente añadida o 0 si ha habido un error.

## Ejemplos

Ejemplo de `QuickHashIntStringHash::set`

```
<?php
$hash = new QuickHashIntStringHash( 1024 );

echo "Set->Add\n";
var_dump( $hash->get( 46692 ) );
var_dump( $hash->set( 46692, "sixteen thousand ninety one" ) );
var_dump( $hash->get( 46692 ) );

echo "Set->Update\n";
var_dump( $hash->set( 46692, "twenty nine thousand nine hundred six" ) );
var_dump( $hash->get( 46692 ) );
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Set->Add
    bool(false)
    int(2)
    string(27) "sixteen thousand ninety one"
    Set->Update
    int(1)
    string(37) "twenty nine thousand nine hundred six"
