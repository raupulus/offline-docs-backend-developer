---
title: Thread::join
description: Sincronización
source_url: https://www.php.net/manual/es/thread.join.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/thread/join.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66750
---

Thread::join

Sincronización

## Descripción

```php
public Thread::join(): bool
```php

Permite esperar al contexto llamante del Thread referenciado hasta que finalice la ejecución.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Une el Thread referenciado

```
<?php
class My extends Thread {
    public function run() {
        /* ... */
    }
}
$my = new My();
$my->start();
/* ... */
var_dump($my->join());
/* ... */
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)
