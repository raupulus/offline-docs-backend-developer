---
title: Worker::getStacked
description: Obtiene el tamaño de pila restante
source_url: https://www.php.net/manual/es/worker.getstacked.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/worker/getstacked.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66940
---

Worker::getStacked

Obtiene el tamaño de pila restante

## Descripción

```php
public Worker::getStacked(): int
```php

Devuelve el número de tareas dejadas en la pila

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de tareas actualmente en espera de ser ejecutadas por el worker

## Ejemplos

Un ejemplo básico de `Worker::getStacked`

```
<?php
$worker = new Worker();

for ($i = 0; $i < 5; ++$i) {
    $worker->stack(new class extends Threaded {});
}

echo "Hay {$worker->getStacked()} tareas apiladas\n";

   
```php

El ejemplo anterior mostrará:

    Hay 5 tareas apiladas
