---
title: QuickHashIntStringHash::update
description: Este método actualiza una entrada en el hash con un nuevo valor
source_url: https://www.php.net/manual/es/quickhashintstringhash.update.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashintstringhash/update.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67350
---

QuickHashIntStringHash::update

Este método actualiza una entrada en el hash con un nuevo valor

## Descripción

```php
public QuickHashIntStringHash::update(int $key, string $value): bool
```php

Este método actualiza una entrada con un nuevo valor y devuelve si la entrada ha sido actualizada. Si hay claves duplicadas, solo el primer elemento encontrado será actualizado. Utilice QuickHashIntStringHash::CHECK_FOR_DUPES al crear el hash para evitar que las claves duplicadas formen parte del hash.

## Parámetros

`key`  
La clave de la entrada a actualizar.

`value`  
El nuevo valor para la entrada. Si se pasa un valor que no es una string, se convertirá automáticamente en una string si es posible.

## Valores devueltos

`true` cuando la entrada ha sido encontrada y actualizada, y `false` si la entrada no era ya parte del hash.

## Ejemplos

Ejemplo de `QuickHashIntStringHash::update`

```
<?php
$hash->add( 161803398, "--" );
$hash->add( 314159265, "a lot" );

echo $hash->get( 161803398 ), "\n";
echo $hash->get( 314159265 ), "\n";

var_dump( $hash->update( 314159265, "a lot plus one" ) );
var_dump( $hash->update( 314159999, "a lot plus one" ) );

echo $hash->get( 161803398 ), "\n";
echo $hash->get( 314159265 ), "\n";
?>

   
```php

Resultado del ejemplo anterior es similar a:

    --
    a lot
    bool(true)
    bool(false)
    --
    a lot plus one
