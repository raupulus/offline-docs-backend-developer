---
title: Ds\PriorityQueue::clear
description: Elimina todos los valores
source_url: https://www.php.net/manual/es/ds-priorityqueue.clear.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/priorityqueue/clear.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15270
---

Ds\PriorityQueue::clear

Elimina todos los valores

## Descripción

```php
public Ds\PriorityQueue::clear(): void
```php

Elimina todos los valores de la cola.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\PriorityQueue::clear`

```
<?php
$queue = new \Ds\PriorityQueue();

$queue->push("a",  5);
$queue->push("b", 15);
$queue->push("c", 10);

$queue->clear();
print_r($queue);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\PriorityQueue Object
    (
    )
