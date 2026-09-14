---
title: Thread::getCurrentThreadId
description: Identificación
source_url: https://www.php.net/manual/es/thread.getcurrentthreadid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/thread/getcurrentthreadid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66710
---

Thread::getCurrentThreadId

Identificación

## Descripción

```php
public static Thread::getCurrentThreadId(): int
```php

Se devuelve la identidad del hilo actualmente en ejecución

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una identidad numérica

## Ejemplos

Se devuelve la identidad del hilo actualmente en ejecución

```
<?php
class My extends Thread {
    public function run() {
        printf("%s es Hilo #%lu\n", __CLASS__, Thread::getCurrentThreadId());
    }
}
$my = new My();
$my->start();
?>

   
```php

El ejemplo anterior mostrará:

    My es Hilo #123456778899
