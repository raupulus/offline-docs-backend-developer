---
title: Worker::collect
description: Recopila las referencias de las tareas finalizadas
source_url: https://www.php.net/manual/es/worker.collect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/worker/collect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: true
translation_revision: bf92d8bd8
order: 66930
---

Worker::collect

Recopila las referencias de las tareas finalizadas

## Descripción

```php
public Worker::collect([Callable $collector]): int
```php

Permite al worker recopilar las referencias determinadas como migajas por el collector eventualmente proporcionado.

## Parámetros

`collector`  
Una función de retrollamada que devuelve un booleano sobre la posibilidad de recopilar la tarea o no. Solo en casos raros debería utilizarse un collector personalizado.

## Valores devueltos

El número de tareas restantes en la pila del worker a recopilar.

## Ejemplos

Un ejemplo básico de Worker::collect

```
<?php
$worker = new Worker();

echo "There are currently {$worker->collect()} tasks on the stack to be collected\n";

for ($i = 0; $i < 15; ++$i) {
    $worker->stack(new class extends Threaded {});
}

echo "There are {$worker->collect()} tasks remaining on the stack to be collected\n";

$worker->start();

while ($worker->collect()); // bloque hasta que todas las tareas estén finalizadas

echo "There are now {$worker->collect()} tasks on the stack to be collected\n";

$worker->shutdown();

   
```php

El ejemplo anterior mostrará:

    There are currently 0 tasks on the stack to be collected
    There are 15 tasks remaining on the stack to be collected
    There are now 0 tasks on the stack to be collected
