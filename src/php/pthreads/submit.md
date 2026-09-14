---
title: Pool::submit
description: Envía un objeto para su ejecución
source_url: https://www.php.net/manual/es/pool.submit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/pool/submit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66650
---

Pool::submit

Envía un objeto para su ejecución

## Descripción

```php
public Pool::submit(Threaded $task): int
```php

Envía la tarea al próximo Worker del Pool

## Parámetros

`size`  
La tarea para su ejecución

## Valores devueltos

El identificador del Worker que ejecuta el objeto

## Ejemplos

Envío de tareas

```
<?php
class MyWork extends Threaded {

    public function run() {
        /* ... */
    }
}

class MyWorker extends Worker {

    public function __construct(Something $something) {
        $this->something = $something;
    }

    public function run() {
        /** ... **/
    }
}

$pool = new Pool(8, \MyWorker::class, [new Something()]);
$pool->submit(new MyWork());
var_dump($pool);
?>

   
```php

El ejemplo anterior mostrará:

    object(Pool)#1 (6) {
      ["size":protected]=>
      int(8)
      ["class":protected]=>
      string(8) "MyWorker"
      ["workers":protected]=>
      array(1) {
        [0]=>
        object(MyWorker)#4 (1) {
          ["something"]=>
          object(Something)#5 (0) {
          }
        }
      }
      ["work":protected]=>
      array(1) {
        [0]=>
        object(MyWork)#3 (1) {
          ["worker"]=>
          object(MyWorker)#5 (1) {
            ["something"]=>
            object(Something)#6 (0) {
            }
          }
        }
      }
      ["ctor":protected]=>
      array(1) {
        [0]=>
        object(Something)#2 (0) {
        }
      }
      ["last":protected]=>
      int(1)
    }
