---
title: Pool::shutdown
description: Detiene todos los workers
source_url: https://www.php.net/manual/es/pool.shutdown.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/pool/shutdown.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66640
---

Pool::shutdown

Detiene todos los workers

## Descripción

```php
public Pool::shutdown(): void
```php

Detiene todos los workers de este Pool. Esto se bloqueará hasta que todas las tareas enviadas hayan sido ejecutadas.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Detener un pool

```
<?php
class Task extends Threaded
{
    public function run()
    {
        usleep(500000);
    }
}

$pool = new Pool(4);

for ($i = 0; $i < 10; ++$i) {
    $pool->submit(new Task());
}

$pool->shutdown(); // se bloquea hasta que todas las tareas enviadas hayan terminado la ejecución

   
```php
