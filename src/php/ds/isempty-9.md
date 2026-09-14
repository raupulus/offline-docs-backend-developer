---
title: Ds\Vector::isEmpty
description: Indica si el vector está vacío
source_url: https://www.php.net/manual/es/ds-vector.isempty.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/vector/isempty.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 9e924f5b8
order: 16310
---

Ds\Vector::isEmpty

Indica si el vector está vacío

## Descripción

```php
public Ds\Vector::isEmpty(): bool
```php

Indica si el vector está vacío.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si el vector está vacío, de lo contrario `false`.

## Ejemplos

Ejemplo de `Ds\Vector::isEmpty`

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
