---
title: Thread::isJoined
description: Detección de estado
source_url: https://www.php.net/manual/es/thread.isjoined.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/thread/isjoined.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66730
---

Thread::isJoined

Detección de estado

## Descripción

```php
public Thread::isJoined(): bool
```php

Indica si el Thread referenciado ha sido unido.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Detecta el estado del Thread referenciado

```
<?php
class My extends Thread {
    public function run() {
        $this->synchronized(function($thread){
            if (!$thread->done)
                $this->wait();
        }, $this);
    }
}
$my = new My();
$my->start();
var_dump($my->isJoined());
$my->synchronized(function($thread){
    $thread->done = true;
    $thread->notify();
}, $my);
?>

   
```php

El ejemplo anterior mostrará:

    bool(false)
