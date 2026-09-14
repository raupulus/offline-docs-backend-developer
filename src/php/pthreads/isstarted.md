---
title: Thread::isStarted
description: Detección de estado
source_url: https://www.php.net/manual/es/thread.isstarted.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/thread/isstarted.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66740
---

Thread::isStarted

Detección de estado

## Descripción

```php
public Thread::isStarted(): bool
```php

Indica si el Thread referenciado ha sido iniciado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Indica si el Thread referenciado ha sido iniciado

```
<?php
$worker = new Worker();
$worker->start();
var_dump($worker->isStarted());
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)
