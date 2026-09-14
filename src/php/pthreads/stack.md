---
title: Worker::stack
description: Apila la tarea
source_url: https://www.php.net/manual/es/worker.stack.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/worker/stack.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66970
---

Worker::stack

Apila la tarea

## Descripción

```php
public Worker::stack(Threaded $work): int
```php

Añade la nueva tarea a la pila del worker referenciado.

## Parámetros

`work`  
Objeto `Threaded` a ejecutar por el worker.

## Valores devueltos

El nuevo tamaño de la pila.

## Ejemplos

Apilamiento de una tarea para ejecución en un worker

```
<?php
$worker = new Worker();
$work = new class extends Threaded {};

var_dump($worker->stack($work));
   
```php

El ejemplo anterior mostrará:

    int(1)
