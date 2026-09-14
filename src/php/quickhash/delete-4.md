---
title: QuickHashStringIntHash::delete
description: Este método elimina una entrada del hash
source_url: https://www.php.net/manual/es/quickhashstringinthash.delete.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashstringinthash/delete.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67390
---

QuickHashStringIntHash::delete

Este método elimina una entrada del hash

## Descripción

```php
public QuickHashStringIntHash::delete(string $key): bool
```php

Este método elimina una entrada del hash y devuelve si la entrada ha sido eliminada o no. Las estructuras de memoria asociadas no serán liberadas inmediatamente, sino cuando el hash mismo es liberado.

Los elementos no pueden ser eliminados cuando el hash está siendo utilizado en un iterador. La método no lanzará una excepción, sino que simplemente devolverá `false` como ocurriría con cualquier otro fallo de eliminación.

## Parámetros

`key`  
La clave de la entrada a eliminar.

## Valores devueltos

`true` cuando la entrada ha sido eliminada, y `false` si la entrada no ha sido eliminada.

## Ejemplos

Ejemplo de `QuickHashStringIntHash::delete`

```
<?php
$hash = new QuickHashStringIntHash( 1024 );
var_dump( $hash->exists( 'four' ) );
var_dump( $hash->add( 'four', 5 ) );
var_dump( $hash->get( 'four' ) );
var_dump( $hash->delete( 'four' ) );
var_dump( $hash->exists( 'four' ) );
var_dump( $hash->get( 'four' ) );
var_dump( $hash->delete( 'four' ) );
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(false)
    bool(true)
    int(5)
    bool(true)
    bool(false)
    bool(false)
    bool(false)
