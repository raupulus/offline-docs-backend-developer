---
title: SplQueue::dequeue
description: Quita un nodo de la cola
source_url: https://www.php.net/manual/es/splqueue.dequeue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splqueue/dequeue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 85450
---

SplQueue::dequeue

Quita un nodo de la cola

## Descripción

```php
public SplQueue::dequeue(): mixed
```php

Quita un `value` en la parte superior de la cola.

> [!NOTE]
> SplQueue::dequeue es un alias de SplDoublyLinkedList::shift.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El valor de el nodo a quitar de la cola.
