---
title: Pool::__construct
description: Crea un nuevo Pool de Workers
source_url: https://www.php.net/manual/es/pool.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/pool/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66620
---

Pool::\_\_construct

Crea un nuevo Pool de Workers

## Descripción

```php
public Pool::__construct(int $size, [string $class], [array $ctor])
```php

Construye un nuevo pool de workers. Los pools crean sus hilos de forma perezosa, lo que significa que los nuevos hilos solo se generarán cuando sean necesarios para ejecutar tareas.

## Parámetros

`size`  
El número máximo de Workers que este Pool puede crear

`class`  
La clase para los nuevos Workers. Si no se proporciona ninguna clase, la clase por defecto es `Worker`.

`ctor`  
Un array de argumentos para pasar al constructor de los nuevos Workers

## Ejemplos

Creación de un Pool

```
<?php
class MyWorker extends Worker {

    public function __construct(Something $something) {
        $this->something = $something;
    }

    public function run() {
        /** ... **/
    }
}

$pool = new Pool(8, \MyWorker::class, [new Something()]);

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
      NULL
      ["work":protected]=>
      NULL
      ["ctor":protected]=>
      array(1) {
        [0]=>
        object(Something)#2 (0) {
        }
      }
      ["last":protected]=>
      int(0)
    }
