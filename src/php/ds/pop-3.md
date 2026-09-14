---
title: Ds\Queue::pop
description: Elimina y devuelve el valor al frente de la cola
source_url: https://www.php.net/manual/es/ds-queue.pop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/queue/pop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15460
---

Ds\Queue::pop

Elimina y devuelve el valor al frente de la cola

## Descripción

```php
public Ds\Queue::pop(): mixed
```php

Elimina y devuelve el valor al frente de la cola.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El valor eliminado que estaba al frente de la cola.

## Errores/Excepciones

`UnderflowException`.

## Ejemplos

Ejemplo de `Ds\Queue::pop`

```
<?php
$queue = new \Ds\Queue();

$queue->push("a");
$queue->push("b");
$queue->push("c");

var_dump($queue->pop());
var_dump($queue->pop());
var_dump($queue->pop());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(1) "a"
    string(1) "b"
    string(1) "c"
