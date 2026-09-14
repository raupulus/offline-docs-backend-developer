---
title: Ds\Collection::clear
description: Eliminar todos los valores
source_url: https://www.php.net/manual/es/ds-collection.clear.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/collection/clear.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 6bd5455a1
order: 14410
---

Ds\Collection::clear

Eliminar todos los valores

## Descripción

```php
public Ds\Collection::clear(): void
```php

Eliminar todos los valores de la colección.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

`Ds\Collection::clear` example

```
<?php
$collection = new \Ds\Vector([1, 2, 3]);
print_r($collection);

$collection->clear();
print_r($collection);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Vector Object
    (
        [0] => 1
        [1] => 2
        [2] => 3
    )
    Ds\Vector Object
    (
    )
