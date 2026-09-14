---
title: Worker::unstack
description: Desapila una tarea
source_url: https://www.php.net/manual/es/worker.unstack.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/worker/unstack.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66980
---

Worker::unstack

Desapila una tarea

## Descripción

```php
public Worker::unstack(): int
```php

Elimina la primera tarea (la más antigua) de la pila.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El nuevo tamaño de la pila.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL pthreads 3.0.0 | El argumento para especificar la tarea a desapilar ha sido eliminado. Ahora, solo la primera tarea en la pila es eliminada. |

## Ejemplos

Elimina el objeto desde la cola de espera de los Workers

```
<?php
$my = new Worker();
$work = new class extends Threaded {};

var_dump($my->stack($work));
var_dump($my->unstack());

   
```php

El ejemplo anterior mostrará:

    int(1)
    int(0)
