---
title: EvIdle::__construct
description: Construye el objeto observador EvIdle
source_url: https://www.php.net/manual/es/evidle.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evidle/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18090
---

EvIdle::\_\_construct

Construye el objeto observador EvIdle

## Descripción

```php
public EvIdle::__construct(callable $callback, [mixed $data], [int $priority])
```php

Construye el objeto observador EvIdle e inicia automáticamente el observador.

## Parámetros

`callback`  
Ver las [funciones de retrollamada de los observadores](#ev.watcher-callbacks).

`data`  
Datos personalizados asociados con el observador.

`priority`  
[Prioridad del observador](#ev.constants.watcher-pri)

## Véase también

EvIdle::createStopped

EvLoop::idle
