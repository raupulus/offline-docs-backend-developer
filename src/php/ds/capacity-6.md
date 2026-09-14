---
title: Ds\Set::capacity
description: Devuelve la capacidad actual
source_url: https://www.php.net/manual/es/ds-set.capacity.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/set/capacity.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: f064d22f6
order: 15780
---

Ds\Set::capacity

Devuelve la capacidad actual

## Descripción

```php
public Ds\Set::capacity(): int
```php

Devuelve la capacidad actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La capacidad actual.

## Ejemplos

Ejemplo de `Ds\Set::capacity`

```
<?php
$set = new \Ds\Set();
var_dump($set->capacity());

$set->add(...range(1, 50));
var_dump($set->capacity());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(16)
    int(64)
