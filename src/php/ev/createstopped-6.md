---
title: EvIo::createStopped
description: Crea un objeto observador EvIo detenido
source_url: https://www.php.net/manual/es/evio.createstopped.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evio/createstopped.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18130
---

EvIo::createStopped

Crea un objeto observador EvIo detenido

## Descripción

```php
final public static EvIo::createStopped(mixed $fd, int $events, callable $callback, [mixed $data], [int $priority]): EvIo
```php

Idéntico al método EvIo::\_\_construct pero no inicia automáticamente el observador.

## Parámetros

`fd`  
Idéntico al método EvIo::\_\_construct

`events`  
Idéntico al método EvIo::\_\_construct

`callback`  
Ver las [funciones de retrollamada de los observadores](#ev.watcher-callbacks).

`data`  
Datos personalizados asociados con el observador.

`priority`  
[Prioridad del observador](#ev.constants.watcher-pri)

## Valores devueltos

Devuelve un objeto EvIo en caso de éxito.

## Véase también

EvIo::\_\_construct

EvLoop::io
