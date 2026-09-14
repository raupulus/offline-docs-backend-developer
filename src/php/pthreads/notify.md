---
title: Threaded::notify
description: Sincronización
source_url: https://www.php.net/manual/es/threaded.notify.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/threaded/notify.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66840
---

Threaded::notify

Sincronización

## Descripción

```php
public Threaded::notify(): bool
```php

Envía una notificación al objeto referenciado

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Notificaciones y espera

```
<?php
class My extends Thread {
    public function run() {
        /** hace que el hilo espere **/
        $this->synchronized(function($thread){
            if (!$thread->done)
                $this->wait();
        }, $this);
    }
}
$my = new My();
$my->start();
/** envía la notificación al hilo que espera **/
$my->synchronized(function($thread){
    $thread->done = true;
    $thread->notify();
}, $my);
var_dump($my->join());
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)
