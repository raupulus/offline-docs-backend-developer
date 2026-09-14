---
title: Threaded::isRunning
description: Detección de estado
source_url: https://www.php.net/manual/es/thread.isrunning.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/threaded/isrunning.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: e2f2172bf
order: 66810
---

Threaded::isRunning

Detección de estado

## Descripción

```php
public Threaded::isRunning(): bool
```php

Se verifica si el objeto referenciado está en ejecución.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un valor booleano que indica el estado.

> [!NOTE]
> Un objeto se considera en ejecución cuando ejecuta el método run.

## Ejemplos

Detecta el estado del objeto referenciado

```
<?php
class My extends Thread {
    public function run() {
        $this->synchronized(function($thread){
            if (!$thread->done)
                $thread->wait();
        }, $this);
    }
}
$my = new My();
$my->start();
var_dump($my->isRunning());
$my->synchronized(function($thread){
    $thread->done = true;
    $thread->notify();
}, $my);
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)
