---
title: EvChild::createStopped
description: Crea una instancia del observador detenido EvChild
source_url: https://www.php.net/manual/es/evchild.createstopped.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evchild/createstopped.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: 184764a63
order: 17980
---

EvChild::createStopped

Crea una instancia del observador detenido EvChild

## Descripción

```php
final public static EvChild::createStopped(int $pid, bool $trace, callable $callback, [mixed $data], [int $priority]): object
```php

Idéntico a EvChild::\_\_construct, pero no inicia automáticamente el observador.

## Parámetros

`pid`  
Idéntico al utilizado para EvChild::\_\_construct

`trace`  
Idéntico al utilizado para EvChild::\_\_construct

`callback`  
Ver las [funciones de retrollamada de los observadores](#ev.watcher-callbacks).

`data`  
Datos personalizados asociados con el observador.

`priority`  
[Prioridad de el observador](#ev.constants.watcher-pri)

## Valores devueltos

## Véase también

EvChild::\_\_construct

EvLoop::child
