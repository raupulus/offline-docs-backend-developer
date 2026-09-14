---
title: Ds\PriorityQueue::capacity
description: Devuelve la capacidad actual
source_url: https://www.php.net/manual/es/ds-priorityqueue.capacity.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/priorityqueue/capacity.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15260
---

Ds\PriorityQueue::capacity

Devuelve la capacidad actual

## Descripción

```php
public Ds\PriorityQueue::capacity(): int
```php

Devuelve la capacidad actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La capacidad actual.

## Ejemplos

Ejemplo de `Ds\PriorityQueue::capacity`

```
<?php
$queue = new \Ds\PriorityQueue();
var_dump($queue->capacity());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(8)
