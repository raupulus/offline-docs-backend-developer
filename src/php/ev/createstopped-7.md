---
title: EvPeriodic::createStopped
description: Crea un watcher EvPeriodic detenido
source_url: https://www.php.net/manual/es/evperiodic.createstopped.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evperiodic/createstopped.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18430
---

EvPeriodic::createStopped

Crea un watcher EvPeriodic detenido

## Descripción

```php
final public static EvPeriodic::createStopped(float $offset, float $interval, callable $reschedule_cb, callable $callback, [mixed $data], [int $priority]): EvPeriodic
```php

Crea un objeto EvPeriodic. A diferencia del método EvPeriodic::\_\_construct, este método no inicia el watcher automáticamente.

## Parámetros

`offset`  
Ver [modos de operación del watcher periódico](#ev.periodic-modes)

`interval`  
Ver los [modos de operación del watcher periódico](#ev.periodic-modes)

`reschedule_cb`  
Función de retrollamada Reschedule. Puede pasarse el valor `null`. Ver los [modos de operación del watcher periódico](#ev.periodic-modes)

`callback`  
Ver las [funciones de retrollamada de los Watchers](#ev.watcher-callbacks).

`data`  
Datos personalizados para asociar con el watcher.

`priority`  
[Prioridad del Watcher](#ev.constants.watcher-pri)

## Valores devueltos

Devuelve un objeto watcher EvPeriodic en caso de éxito.

## Véase también

EvPeriodic::\_\_construct

EvTimer::createStopped
