---
title: Las funciones de retrollamada de un Watcher
source_url: https://www.php.net/manual/es/ev.watcher-callbacks.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/watcher-callbacks.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: 7cecc752c
order: 18780
---

## Las funciones de retrollamada de un Watcher

Todos los watchers pueden estar activos (esperando eventos) o inactivos (en pausa). Solo los watchers activos pueden tener sus funciones de retrollamada llamadas. Todas las funciones de retrollamada serán llamadas con al menos dos argumentos: `watcher` - el watcher, y `revents`, una máscara de eventos recibidos.

Las funciones de retrollamada de los watchers son pasadas a los constructores de los watchers (una clase derivada de `EvWatcher` - EvCheck::\_\_construct, EvChild::\_\_construct etc.). Una función de retrollamada de un watcher debe coincidir con el siguiente prototipo:

```php
callback([object $watcher], [int $revents]): void
```php

`watcher`  
La instancia del watcher (de una clase que extiende `EvWatcher`).

`revents`  
[Un watcher que recibe los eventos](#ev.constants.watcher-revents).

Cada tipo de watcher tiene un byte asociado en `revents`, por lo tanto, se puede utilizar la misma función de retrollamada para varios watchers. La máscara de eventos se nombra según el tipo, es decir, `EvChild` (o EvLoop::child) define `Ev::CHILD`, `EvPrepare` (o EvLoop::prepare) define `Ev::PREPARE`, `EvPeriodic` (o EvLoop::periodic) define `Ev::PERIODIC` y así sucesivamente, con la excepción de los eventos de E/S (que pueden definir tanto los bytes `Ev::READ` como `Ev::WRITE`).
