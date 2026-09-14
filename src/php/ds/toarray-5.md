---
title: Ds\PriorityQueue::toArray
description: Convierte la cola en un array.
source_url: https://www.php.net/manual/es/ds-priorityqueue.toarray.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/priorityqueue/toarray.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15360
---

Ds\PriorityQueue::toArray

Convierte la cola en un

array

.

## Descripción

```php
public Ds\PriorityQueue::toArray(): array
```php

Convierte la cola en un `array`.

> [!NOTE]
> Este método no es destructivo.

> [!NOTE]
> La conversión en un `array` aún no es soportada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `array` que contiene todos los valores en el mismo orden que la cola.

## Ejemplos

Ejemplo de `Ds\PriorityQueue::toArray`

```
<?php
$queue = new \Ds\PriorityQueue();

$queue->push("a",  5);
$queue->push("b", 15);
$queue->push("c", 10);

var_dump($queue->toArray());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(3) {
      [0]=>
      string(1) "b"
      [1]=>
      string(1) "c"
      [2]=>
      string(1) "a"
    }
