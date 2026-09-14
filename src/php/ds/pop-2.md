---
title: Ds\PriorityQueue::pop
description: Elimina y devuelve el valor con la prioridad más alta
source_url: https://www.php.net/manual/es/ds-priorityqueue.pop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/priorityqueue/pop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15340
---

Ds\PriorityQueue::pop

Elimina y devuelve el valor con la prioridad más alta

## Descripción

```php
public Ds\PriorityQueue::pop(): mixed
```php

Elimina y devuelve el valor al frente de la cola, es decir, el valor con la prioridad más alta.

> [!NOTE]
> Los valores con prioridad igual se tratan en FIFO (primero en entrar, primero en salir).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El valor eliminado que estaba al frente de la cola.

## Errores/Excepciones

`UnderflowException` si está vacío.

## Ejemplos

Ejemplo de `Ds\PriorityQueue::pop`

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

    string(1) "a"
    string(1) "b"
    string(1) "c"
