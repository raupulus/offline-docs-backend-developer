---
title: QuickHashIntHash::get
description: Este método recupera un valor del hash por su clave
source_url: https://www.php.net/manual/es/quickhashinthash.get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashinthash/get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67050
---

QuickHashIntHash::get

Este método recupera un valor del hash por su clave

## Descripción

```php
public QuickHashIntHash::get(int $key): int
```php

Este método recupera un valor del hash por su clave.

## Parámetros

`key`  
La clave de la entrada a recuperar.

## Valores devueltos

El valor si la clave existe, o `null` si la clave no era parte del hash.

## Ejemplos

Ejemplo de `QuickHashIntHash::get`

```
<?php
$hash = new QuickHashIntHash( 8 );
var_dump( $hash->get( 1 ) );

var_dump( $hash->add( 2 ) );
var_dump( $hash->get( 2 ) );

var_dump( $hash->add( 3, 5 ) );
var_dump( $hash->get( 3 ) );
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(false)
    bool(true)
    int(1)
    bool(true)
    int(5)
