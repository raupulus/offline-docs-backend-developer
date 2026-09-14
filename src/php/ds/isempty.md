---
title: Ds\Collection::isEmpty
description: Indica si la colección está vacía
source_url: https://www.php.net/manual/es/ds-collection.isempty.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/collection/isempty.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 6bd5455a1
order: 14430
---

Ds\Collection::isEmpty

Indica si la colección está vacía

## Descripción

```php
public Ds\Collection::isEmpty(): bool
```php

Indica si la colección está vacía.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si la colección está vacía, `false` en caso contrario.

## Ejemplos

`Ds\Collection::isEmpty` ejemplo

```
<?php
$a = new \Ds\Vector([1, 2, 3]);
$b = new \Ds\Vector();

var_dump($a->isEmpty());
var_dump($b->isEmpty());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(false)
    bool(true)
