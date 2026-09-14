---
title: Ds\Queue::peek
description: Devuelve el valor al frente de la cola
source_url: https://www.php.net/manual/es/ds-queue.peek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/queue/peek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15450
---

Ds\Queue::peek

Devuelve el valor al frente de la cola

## Descripción

```php
public Ds\Queue::peek(): mixed
```php

Devuelve el valor al frente de la cola, pero no lo elimina.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el valor al frente de la cola.

## Errores/Excepciones

`UnderflowException` si está vacía.

## Ejemplos

Ejemplo de `Ds\Queue::peek`

```
<?php
$queue = new \Ds\Queue();

$queue->push("a");
$queue->push("b");
$queue->push("c");

var_dump($queue->peek());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(1) "a"
