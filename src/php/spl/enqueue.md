---
title: SplQueue::enqueue
description: Añade un elemento a la cola
source_url: https://www.php.net/manual/es/splqueue.enqueue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splqueue/enqueue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 85460
---

SplQueue::enqueue

Añade un elemento a la cola

## Descripción

```php
public SplQueue::enqueue(mixed $value): void
```php

Añadir un `value` al final de la cola.

> [!NOTE]
> SplQueue::enqueue es un alias de SplDoublyLinkedList::push.

## Parámetros

`value`  
El valor que se va a añadir.

## Valores devueltos

No se retorna ningún valor.
