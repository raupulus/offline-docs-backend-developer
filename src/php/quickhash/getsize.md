---
title: QuickHashIntHash::getSize
description: Devuelve el número de elementos en el hash
source_url: https://www.php.net/manual/es/quickhashinthash.getsize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashinthash/getsize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67060
---

QuickHashIntHash::getSize

Devuelve el número de elementos en el hash

## Descripción

```php
public QuickHashIntHash::getSize(): int
```php

Devuelve el número de elementos en el hash.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El número de elementos en el hash.

## Ejemplos

Ejemplo de `QuickHashIntHash::getSize`

```
<?php
$hash = new QuickHashIntHash( 8 );
var_dump( $hash->add( 2 ) );
var_dump( $hash->add( 3, 5 ) );
var_dump( $hash->getSize() );
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    bool(true)
    int(2)
