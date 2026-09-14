---
title: QuickHashIntHash::update
description: Este método actualiza una entrada en el hash con un nuevo valor
source_url: https://www.php.net/manual/es/quickhashinthash.update.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashinthash/update.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67120
---

QuickHashIntHash::update

Este método actualiza una entrada en el hash con un nuevo valor

## Descripción

```php
public QuickHashIntHash::update(int $key, int $value): bool
```php

Este método actualiza una entrada con un nuevo valor y devuelve si la entrada ha sido actualizada. Si hay claves duplicadas, solo el primer elemento encontrado será actualizado. Utilice `QuickHashIntHash::CHECK_FOR_DUPES` al crear el hash para evitar que las claves duplicadas formen parte del hash.

## Parámetros

`key`  
La clave de la entrada a actualizar.

`value`  
El nuevo valor para actualizar la entrada.

## Valores devueltos

`true` cuando la entrada ha sido encontrada y actualizada, y `false` si la entrada no estaba ya presente en el hash.

## Ejemplos

Ejemplo de `QuickHashIntHash::update`

```
<?php
$hash = new QuickHashIntHash( 1024 );

var_dump( $hash->add( 141421, 173205 ) );
var_dump( $hash->update( 141421, 223606 ) );
var_dump( $hash->get( 141421 ) );
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    bool(true)
    int(223606)
