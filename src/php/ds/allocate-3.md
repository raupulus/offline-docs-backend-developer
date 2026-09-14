---
title: Ds\PriorityQueue::allocate
description: Asigna suficiente memoria para una capacidad requerida
source_url: https://www.php.net/manual/es/ds-priorityqueue.allocate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/priorityqueue/allocate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dfd68fd22
order: 15250
---

Ds\PriorityQueue::allocate

Asigna suficiente memoria para una capacidad requerida

## Descripción

```php
public Ds\PriorityQueue::allocate(int $capacity): void
```php

Asegura que se asigne suficiente memoria para una capacidad requerida. Esto elimina la necesidad de reasignar el búfer interno a medida que se añaden valores.

## Parámetros

`capacity`  
El número de valores para los cuales se debe asignar la capacidad.

> [!NOTE]
> La capacidad permanecerá igual si este valor es inferior o igual a la capacidad actual.

> [!NOTE]
> La capacidad siempre se redondeará a la potencia de 2 más cercana.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\PriorityQueue::allocate`

```
<?php
$queue = new \Ds\PriorityQueue();
var_dump($queue->capacity());

$queue->allocate(100);
var_dump($queue->capacity());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(8)
    int(128)
