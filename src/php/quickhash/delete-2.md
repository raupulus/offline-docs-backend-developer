---
title: QuickHashIntSet::delete
description: Este método elimina una entrada del conjunto
source_url: https://www.php.net/manual/es/quickhashintset.delete.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashintset/delete.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67160
---

QuickHashIntSet::delete

Este método elimina una entrada del conjunto

## Descripción

```php
public QuickHashIntSet::delete(int $key): bool
```php

Este método elimina una entrada del conjunto y devuelve si la entrada ha sido eliminada. Las estructuras de memoria asociadas no se liberarán inmediatamente, sino cuando el conjunto mismo sea liberado.

## Parámetros

`key`  
La clave de la entrada a eliminar.

## Valores devueltos

`true` cuando la entrada ha sido eliminada, y `false` si la entrada no ha sido eliminada.

## Ejemplos

Ejemplo de `QuickHashIntSet::delete`

```
<?php
$set = new QuickHashIntSet( 1024 );
var_dump( $set->exists( 4 ) );
var_dump( $set->add( 4 ) );
var_dump( $set->delete( 4 ) );
var_dump( $set->exists( 4 ) );
var_dump( $set->delete( 4 ) );
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(false)
    bool(true)
    bool(true)
    bool(false)
    bool(false)
