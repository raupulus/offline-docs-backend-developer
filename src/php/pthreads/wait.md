---
title: Threaded::wait
description: Sincronización
source_url: https://www.php.net/manual/es/threaded.wait.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/threaded/wait.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66900
---

Threaded::wait

Sincronización

## Descripción

```php
public Threaded::wait([int $timeout]): bool
```php

Hace esperar al contexto llamante una notificación desde el objeto referenciado.

## Parámetros

`timeout`  
Un tiempo de espera máximo opcional, en microsegundos.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Notificaciones y espera

```
<?php
class My extends Thread {
    public function run() {
        /** Hace esperar este hilo **/
        $this->synchronized(function($thread){
            if (!$thread->done)
                $thread->wait();
        }, $this);
    }
}
$my = new My();
$my->start();
/** Envía la notificación al hilo que espera **/
$my->synchronized(function($thread){
    $thread->done = true;
    $thread->notify();
}, $my);
var_dump($my->join());
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)
