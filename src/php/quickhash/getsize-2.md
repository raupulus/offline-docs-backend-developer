---
title: QuickHashIntSet::getSize
description: Devuelve el número de elementos en el conjunto
source_url: https://www.php.net/manual/es/quickhashintset.getsize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashintset/getsize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67180
---

QuickHashIntSet::getSize

Devuelve el número de elementos en el conjunto

## Descripción

```php
public QuickHashIntSet::getSize(): int
```php

Devuelve el número de elementos en el conjunto.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El número de elementos en el conjunto.

## Ejemplos

Ejemplo de `QuickHashIntSet::getSize`

```
<?php
$set = new QuickHashIntSet( 8 );
var_dump( $set->add( 2 ) );
var_dump( $set->add( 3 ) );
var_dump( $set->getSize() );
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    bool(true)
    int(2)
