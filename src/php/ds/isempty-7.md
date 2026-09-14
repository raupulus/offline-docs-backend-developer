---
title: Ds\Set::isEmpty
description: Indica si el conjunto está vacío
source_url: https://www.php.net/manual/es/ds-set.isempty.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/set/isempty.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 9e924f5b8
order: 15890
---

Ds\Set::isEmpty

Indica si el conjunto está vacío

## Descripción

```php
public Ds\Set::isEmpty(): bool
```php

Indica si el conjunto está vacío.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si el conjunto está vacío, de lo contrario `false`.

## Ejemplos

Ejemplo de `Ds\Set::isEmpty`

```
<?php
$a = new \Ds\Set([1, 2, 3]);
$b = new \Ds\Set();

var_dump($a->isEmpty());
var_dump($b->isEmpty());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(false)
    bool(true)
