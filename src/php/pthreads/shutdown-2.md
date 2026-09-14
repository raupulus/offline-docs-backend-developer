---
title: Worker::shutdown
description: Detener el worker
source_url: https://www.php.net/manual/es/worker.shutdown.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/worker/shutdown.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66960
---

Worker::shutdown

Detener el worker

## Descripción

```php
public Worker::shutdown(): bool
```php

Detiene el Worker después de ejecutar todas las tareas apiladas.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Apaga el worker referenciado

```
<?php
$my = new Worker();
$my->start();
/* apilar/ejecutar tareas */
var_dump($my->shutdown());

   
```php

El ejemplo anterior mostrará:

    bool(true)
