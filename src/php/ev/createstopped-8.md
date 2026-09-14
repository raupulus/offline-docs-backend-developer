---
title: EvPrepare::createStopped
description: Crea una instancia detenida del watcher EvPrepare
source_url: https://www.php.net/manual/es/evprepare.createstopped.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evprepare/createstopped.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: 7cecc752c
order: 18470
---

EvPrepare::createStopped

Crea una instancia detenida del watcher EvPrepare

## Descripción

```php
final public static EvPrepare::createStopped(callable $callback, [mixed $data], [int $priority]): EvPrepare
```php

Crea una instancia detenida del watcher EvPrepare. A diferencia del método EvPrepare::\_\_construct, este método no inicia el watcher automáticamente.

## Parámetros

`callback`  
Ver las [funciones de retrollamada de los Watchers](#ev.watcher-callbacks).

`data`  
Datos personalizados para asociar con el watcher.

`priority`  
[Prioridad del Watcher](#ev.constants.watcher-pri)

## Valores devueltos

Devuelve un objeto EvPrepare en caso de éxito.

## Véase también

EvPrepare::\_\_construct

EvWatcher::start
