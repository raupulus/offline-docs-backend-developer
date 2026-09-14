---
title: Ds\PriorityQueue::push
description: Añade valores a la cola
source_url: https://www.php.net/manual/es/ds-priorityqueue.push.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/priorityqueue/push.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15350
---

Ds\PriorityQueue::push

Añade valores a la cola

## Descripción

```php
public Ds\PriorityQueue::push(mixed $value, int $priority): void
```php

Añade un `value` con una `priority` dada a la cola.

## Parámetros

`value`  
El valor a añadir a la cola.

`priority`  
La prioridad asociada al valor.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\PriorityQueue::push`

```
<?php
$queue = new \Ds\PriorityQueue();

$queue->push("a",  5);
$queue->push("b", 15);
$queue->push("c", 10);

print_r($queue->pop());
print_r($queue->pop());
print_r($queue->pop());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(1) "b"
    string(1) "c"
    string(1) "a"
