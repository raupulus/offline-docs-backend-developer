---
title: QuickHashIntStringHash::get
description: Este método recupera un valor del hash por su clave
source_url: https://www.php.net/manual/es/quickhashintstringhash.get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashintstringhash/get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67280
---

QuickHashIntStringHash::get

Este método recupera un valor del hash por su clave

## Descripción

```php
public QuickHashIntStringHash::get(int $key): mixed
```php

Este método recupera un valor del hash por su clave.

## Parámetros

`key`  
La clave de la entrada a recuperar.

## Valores devueltos

El valor si la clave existe, o `null` si la clave no era parte del hash.

## Ejemplos

Ejemplo de `QuickHashIntStringHash::get`

```
<?php
$hash = new QuickHashIntStringHash( 8 );
var_dump( $hash->get( 1 ) );

var_dump( $hash->add( 2, "two" ) );
var_dump( $hash->get( 2 ) );

var_dump( $hash->add( 3, 5 ) );
var_dump( $hash->get( 3 ) );
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(false)
    bool(true)
    string(3) "two"
    bool(true)
    string(1) "5"
