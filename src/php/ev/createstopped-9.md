---
title: EvSignal::createStopped
description: Crea un objeto watcher EvSignal detenido
source_url: https://www.php.net/manual/es/evsignal.createstopped.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evsignal/createstopped.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: 7cecc752c
order: 18500
---

EvSignal::createStopped

Crea un objeto watcher EvSignal detenido

## Descripción

```php
final public static EvSignal::createStopped(int $signum, callable $callback, [mixed $data], [int $priority]): EvSignal
```php

Crea un objeto watcher EvSignal detenido. A diferencia del método EvSignal::\_\_construct, este método no inicia automáticamente el watcher.

## Parámetros

`signum`  
Número de la señal. Ver las constantes exportadas por la extensión *pcntl*. Ver también la página del manual del sistema `signal(7)`.

`callback`  
Ver las [funciones de retrollamada de los Watchers](#ev.watcher-callbacks).

`data`  
Datos personalizados para asociar con el watcher.

`priority`  
[Prioridad del Watcher](#ev.constants.watcher-pri)

## Valores devueltos

Devuelve un objeto EvSignal en caso de éxito.

## Véase también

EvWatcher::start

EvSignal::\_\_construct
