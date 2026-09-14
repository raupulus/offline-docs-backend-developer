---
title: Ds\Collection::copy
description: Devuelve una copia superficial de la colección
source_url: https://www.php.net/manual/es/ds-collection.copy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/collection/copy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 6bd5455a1
order: 14420
---

Ds\Collection::copy

Devuelve una copia superficial de la colección

## Descripción

```php
public Ds\Collection::copy(): Ds\Collection
```php

Devuelve una copia superficial de la colección.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una copia superficial de la colección.

## Ejemplos

`Ds\Collection::copy` ejemplo

```
<?php
$a = new \Ds\Vector([1, 2, 3]);
$b = $a->copy();

$b->push(4);

print_r($a);
print_r($b);
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
        [0] => 1
        [1] => 2
        [2] => 3
        [3] => 4
    )
