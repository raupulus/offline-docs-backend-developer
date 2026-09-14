---
title: Ds\PriorityQueue::copy
description: Devuelve una copia superficial de la cola
source_url: https://www.php.net/manual/es/ds-priorityqueue.copy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/priorityqueue/copy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15290
---

Ds\PriorityQueue::copy

Devuelve una copia superficial de la cola

## Descripción

```php
public Ds\PriorityQueue::copy(): Ds\PriorityQueue
```php

Devuelve una copia superficial de la cola.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una copia superficial de la cola.

## Ejemplos

Ejemplo de `Ds\PriorityQueue::copy`

```
<?php
$queue = new \Ds\PriorityQueue();

$queue->push("a",  5);
$queue->push("b", 15);
$queue->push("c", 10);

print_r($queue->copy());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\PriorityQueue Object
    (
        [0] => b
        [1] => c
        [2] => a
    )
