---
title: Threaded::synchronized
description: Sincronización
source_url: https://www.php.net/manual/es/threaded.synchronized.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/threaded/synchronized.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66890
---

Threaded::synchronized

Sincronización

## Descripción

```php
public Threaded::synchronized(Closure $block, mixed ...$args): mixed
```php

Se ejecuta el bloque mientras se retienen los candados de sincronización de los objetos referenciados para el contexto llamante.

## Parámetros

`block`  
El bloque de código a ejecutar

`args`  
Lista variable de argumentos a utilizar como argumento de la función

## Valores devueltos

El valor devuelto del bloque

## Ejemplos

Sincronización

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
$my->synchronized(function($thread){
    $thread->done = true;
    $thread->notify();
}, $my);
var_dump($my->join());
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)
