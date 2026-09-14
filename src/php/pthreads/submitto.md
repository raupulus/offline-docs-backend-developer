---
title: Pool::submitTo
description: Envía una tarea a un worker específico para su ejecución
source_url: https://www.php.net/manual/es/pool.submitTo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/pool/submitTo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66660
---

Pool::submitTo

Envía una tarea a un worker específico para su ejecución

## Descripción

```php
public Pool::submitTo(int $worker, Threaded $task): int
```php

Envía la tarea al worker especificado en el Pool. Los workers están indexados a partir de 0, y solo existirán si el pool necesita crearlos (ya que los threads se generan de forma perezosa).

## Parámetros

`worker`  
El worker donde apilar la tarea, indexado a partir de `0`.

`size`  
La tarea, para su ejecución

## Valores devueltos

El identificador del Worker que ha aceptado la tarea.

## Ejemplos

Envío de una tarea a un worker específico

```
<?php
class Task extends Threaded {
    public function run() {
        var_dump(Thread::getCurrentThreadID());
    }
}

$pool = new Pool(2);

$pool->submit(new Task());

for ($i = 0; $i < 5; ++$i) {
    $pool->submitTo(0, new Task()); // apilar todas las tareas en el primer worker
}

$pool->submitTo(1, new Task()); // No es posible apilar la tarea en el segundo worker ya que aún no existe

$pool->shutdown();
?>

   
```php

El ejemplo anterior mostrará:

    int(4475011072)
    int(4475011072)
    int(4475011072)
    int(4475011072)
    int(4475011072)
    int(4475011072)

    Fatal error: Uncaught Exception: The selected worker (1) does not exist in %s:%d
