---
title: Ds\Pair::isEmpty
description: Indica si la pareja está vacía
source_url: https://www.php.net/manual/es/ds-pair.isempty.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/pair/isempty.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 9e924f5b8
order: 15220
---

Ds\Pair::isEmpty

Indica si la pareja está vacía

## Descripción

```php
public Ds\Pair::isEmpty(): bool
```php

Indica si la pareja está vacía.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si la pareja está vacía, de lo contrario `false`.

## Ejemplos

Ejemplo de `Ds\Pair::isEmpty`

```
<?php
$a = new \Ds\Pair("a", 1);
$b = new \Ds\Pair();

var_dump($a->isEmpty());
var_dump($b->isEmpty());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(false)
    bool(true)
