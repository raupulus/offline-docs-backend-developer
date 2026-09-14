---
title: QuickHashIntStringHash::getSize
description: Devuelve el número de elementos en el hash
source_url: https://www.php.net/manual/es/quickhashintstringhash.getsize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashintstringhash/getsize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67290
---

QuickHashIntStringHash::getSize

Devuelve el número de elementos en el hash

## Descripción

```php
public QuickHashIntStringHash::getSize(): int
```php

Devuelve el número de elementos en el hash.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El número de elementos en el hash.

## Ejemplos

Ejemplo de `QuickHashIntStringHash::getSize`

```
<?php
$hash = new QuickHashIntStringHash( 8 );
var_dump( $hash->add( 2, "two" ) );
var_dump( $hash->add( 3, 5 ) );
var_dump( $hash->getSize() );
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    bool(true)
    int(2)
