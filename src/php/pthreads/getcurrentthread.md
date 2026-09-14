---
title: Thread::getCurrentThread
description: Identificación
source_url: https://www.php.net/manual/es/thread.getcurrentthread.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/thread/getcurrentthread.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66700
---

Thread::getCurrentThread

Identificación

## Descripción

```php
public static Thread::getCurrentThread(): Thread
```php

Devuelve una referencia del hilo actualmente en ejecución

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un objeto que representa el hilo actualmente en ejecución.

## Ejemplos

Devuelve el hilo actualmente en ejecución

```
<?php
class My extends Thread {
    public function run() {
        var_dump(Thread::getCurrentThread());
    }
}
$my = new My();
$my->start();
?>

   
```php

El ejemplo anterior mostrará:

    object(My)#2 (0) {
    }
