---
title: EvStat::createStopped
description: Crea un objeto EvStat watcher detenido
source_url: https://www.php.net/manual/es/evstat.createstopped.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evstat/createstopped.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18550
---

EvStat::createStopped

Crea un objeto EvStat watcher detenido

## Descripción

```php
final public static EvStat::createStopped(string $path, float $interval, callable $callback, [mixed $data], [int $priority]): void
```php

Crea un objeto EvStat watcher, pero no lo inicia automáticamente (a diferencia del método EvStat::\_\_construct).

## Parámetros

`path`  
La ruta de acceso para la cual se debe esperar un cambio de estado.

`interval`  
Intervalo de detección de la modificación; debe normalmente valer `0.0` para dejar que *libev* elija un buen valor.

`callback`  
Ver las [funciones de retrollamada Watcher](#ev.watcher-callbacks).

`data`  
Datos personalizados para asociar con el watcher.

`priority`  
[las prioridades del Watcher](#ev.constants.watcher-pri)

## Valores devueltos

Devuelve un objeto EvStat watcher detenido en caso de éxito.

## Véase también

EvStat::\_\_construct

EvWatcher::start
