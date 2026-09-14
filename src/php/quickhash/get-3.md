---
title: QuickHashStringIntHash::get
description: Este método recupera un valor del hash por su clave
source_url: https://www.php.net/manual/es/quickhashstringinthash.get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashstringinthash/get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67410
---

QuickHashStringIntHash::get

Este método recupera un valor del hash por su clave

## Descripción

```php
public QuickHashStringIntHash::get(string $key): mixed
```php

Este método recupera un valor del hash por su clave.

## Parámetros

`key`  
La clave de la entrada a recuperar.

## Valores devueltos

El valor si la clave existe, o `null` si la clave no era parte del hash.

## Ejemplos

Ejemplo de `QuickHashStringIntHash::get`

```
<?php
$hash = new QuickHashStringIntHash( 8 );
var_dump( $hash->get( "one" ) );

var_dump( $hash->add( "two", 2 ) );
var_dump( $hash->get( "two" ) );
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(false)
    bool(true)
    int(2)
