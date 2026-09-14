---
title: QuickHashIntHash::delete
description: Este método elimina una entrada del hash
source_url: https://www.php.net/manual/es/quickhashinthash.delete.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashinthash/delete.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67030
---

QuickHashIntHash::delete

Este método elimina una entrada del hash

## Descripción

```php
public QuickHashIntHash::delete(int $key): bool
```php

Este método elimina una entrada del hash y devuelve si la entrada ha sido eliminada. Las estructuras de memoria asociadas no se liberarán inmediatamente, sino cuando el hash mismo es liberado.

Los elementos no pueden ser eliminados cuando el hash está siendo utilizado en un iterador. El método no lanzará una excepción, sino que simplemente devolverá `false` como ocurriría con cualquier otro fallo de eliminación.

## Parámetros

`key`  
La clave de la entrada a eliminar.

## Valores devueltos

`true` cuando la entrada ha sido eliminada, y `false` si la entrada no ha sido eliminada.

## Ejemplos

Ejemplo de `QuickHashIntHash::delete`

```
<?php
$hash = new QuickHashIntHash( 1024 );
var_dump( $hash->exists( 4 ) );
var_dump( $hash->add( 4, 5 ) );
var_dump( $hash->delete( 4 ) );
var_dump( $hash->exists( 4 ) );
var_dump( $hash->delete( 4 ) );
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(false)
    bool(true)
    bool(true)
    bool(false)
    bool(false)
