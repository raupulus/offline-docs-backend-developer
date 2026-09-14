---
title: SplPriorityQueue::insert
description: Inserta un elemento en la cola
source_url: https://www.php.net/manual/es/splpriorityqueue.insert.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splpriorityqueue/insert.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: eb39dbdba
order: 85340
---

SplPriorityQueue::insert

Inserta un elemento en la cola

## Descripción

```php
public SplPriorityQueue::insert(mixed $value, mixed $priority): true
```php

Inserta el valor `value` con la prioridad `priority` en la cola.

## Parámetros

`value`  
El valor a insertar.

`priority`  
La prioridad asociada.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | SplPriorityQueue::insert posee ahora un retorno provisional de tipo `true`. |
