---
title: Threaded::notifyOne
description: Sincronizar
source_url: https://www.php.net/manual/es/threaded.notifyone.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/threaded/notifyone.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: true
translation_revision: bf92d8bd8
order: 66850
---

Threaded::notifyOne

Sincronizar

## Descripción

```php
public Threaded::notifyOne(): bool
```php

Envía una notificación al objeto referenciado. Esto desbloquea al menos uno de los threads bloqueados (a diferencia de desbloquearlos todos, como ocurre con Threaded::notify).

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
        /** causa que este thread espere **/
        $this->synchronized(function($thread){
            if (!$thread->done)
                $this->wait();
        }, $this);
    }
}
$my = new My();
$my->start();
/** envía una notificación al thread en espera **/
$my->synchronized(function($thread){
    $thread->done = true;
    $thread->notifyOne();
}, $my);
var_dump($my->join());
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)
