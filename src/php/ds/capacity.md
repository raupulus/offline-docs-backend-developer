---
title: Ds\Deque::capacity
description: Devuelve la capacidad actual
source_url: https://www.php.net/manual/es/ds-deque.capacity.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/deque/capacity.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 14470
---

Ds\Deque::capacity

Devuelve la capacidad actual

## Descripción

```php
public Ds\Deque::capacity(): int
```php

Devuelve la capacidad actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La capacidad actual.

## Ejemplos

Ejemplo de `Ds\Deque::capacity`

```
<?php
$deque = new \Ds\Deque();
var_dump($deque->capacity());

$deque->push(...range(1, 50));
var_dump($deque->capacity());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(8)
    int(64)
