---
title: EvFork::__construct
description: Construye el objeto observador EvFork
source_url: https://www.php.net/manual/es/evfork.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evfork/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18060
---

EvFork::\_\_construct

Construye el objeto observador EvFork

## Descripción

```php
public EvFork::__construct(callable $callback, [mixed $data], [int $priority])
```php

Construye el objeto observador EvFork y arranca el observador automáticamente.

## Parámetros

`callback`  
Véase también las [funciones de retrollamada para los observadores](#ev.watcher-callbacks).

`data`  
Datos personalizados asociados al observador.

`priority`  
[Prioridad del observador](#ev.constants.watcher-pri)

## Véase también

EvLoop::fork

EvCheck
