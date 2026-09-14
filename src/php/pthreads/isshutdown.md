---
title: Worker::isShutdown
description: Detección de estado
source_url: https://www.php.net/manual/es/worker.isshutdown.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/worker/isshutdown.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66950
---

Worker::isShutdown

Detección de estado

## Descripción

```php
public Worker::isShutdown(): bool
```php

Indica si el Worker ha sido detenido o no.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve si el Worker ha sido detenido o no.

## Ejemplos

Detecta el estado de un worker

```
<?php
$worker = new Worker();
$worker->start();

var_dump($worker->isShutdown());

$worker->shutdown();

var_dump($worker->isShutdown());

   
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(true)
