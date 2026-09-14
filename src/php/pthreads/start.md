---
title: Thread::start
description: Ejecución
source_url: https://www.php.net/manual/es/thread.start.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/thread/start.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66760
---

Thread::start

Ejecución

## Descripción

```php
public Thread::start([int $options]): bool
```php

Inicia un nuevo Thread y ejecuta el método run implementado.

## Parámetros

`options`  
Una máscara opcional de constantes heredadas; por omisión, PTHREADS_INHERIT_ALL

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Inicia los Threads

```
<?php
class My extends Thread {
    public function run() {
        /** ... **/
    }
}
$my = new My();
var_dump($my->start());
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)
