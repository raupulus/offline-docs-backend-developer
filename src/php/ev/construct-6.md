---
title: EvIo::__construct
description: Construye un nuevo objeto EvIo
source_url: https://www.php.net/manual/es/evio.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evio/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18120
---

EvIo::\_\_construct

Construye un nuevo objeto EvIo

## Descripción

```php
public EvIo::__construct(mixed $fd, int $events, callable $callback, [mixed $data], [int $priority])
```php

Construye un nuevo objeto EvIo y arranca el observador automáticamente.

## Parámetros

`fd`  
Puede ser un flujo abierto con la función `fopen` o cualquier función similar, descriptores de ficheros o sockets.

`events`  
`Ev::READ` y/o `Ev::WRITE`. Ver las [máscaras de octetos](#ev.constants.watcher-revents).

`callback`  
Ver las [funciones de retrollamada de los observadores](#ev.watcher-callbacks).

`data`  
Datos personalizados asociados con el observador.

`priority`  
[Prioridad del observador](#ev.constants.watcher-pri)

## Véase también

EvIo::createStopped

EvLoop::io
