---
title: QuickHashStringIntHash::update
description: Este método actualiza una entrada en el hash con un nuevo valor
source_url: https://www.php.net/manual/es/quickhashstringinthash.update.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashstringinthash/update.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67480
---

QuickHashStringIntHash::update

Este método actualiza una entrada en el hash con un nuevo valor

## Descripción

```php
public QuickHashStringIntHash::update(string $key, int $value): bool
```php

Este método actualiza una entrada con un nuevo valor y devuelve si la entrada ha sido actualizada. Si hay claves duplicadas, solo el primer elemento encontrado será actualizado. Utilice QuickHashStringIntHash::CHECK_FOR_DUPES al crear el hash para evitar que las claves duplicadas formen parte del hash.

## Parámetros

`key`  
La clave de la entrada a actualizar.

`value`  
El nuevo valor de la entrada. Si se pasa un valor que no es una cadena, se convertirá automáticamente en una cadena si es posible.

## Valores devueltos

`true` cuando la entrada ha sido encontrada y actualizada, y `false` si la entrada no era ya parte del hash.

## Ejemplos

Ejemplo de `QuickHashStringIntHash::update`

```
<?php
$hash = new QuickHashStringIntHash( 1024 );

$hash->add( 'six', 314159265 );
$hash->add( "a lot", 314159265 );

echo $hash->get( 'six' ), "\n";
echo $hash->get( 'a lot' ), "\n";

var_dump( $hash->update( 'a lot', 314159266 ) );
var_dump( $hash->update( "a lot plus one", 314159999 ) );

echo $hash->get( 'six' ), "\n";
echo $hash->get( 'a lot' ), "\n";
?>

   
```php

Resultado del ejemplo anterior es similar a:

    314159265
    314159265
    bool(true)
    bool(false)
    314159265
    314159266
