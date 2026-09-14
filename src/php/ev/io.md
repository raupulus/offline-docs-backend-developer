---
title: EvLoop::io
description: Crea un objeto EvIo watcher asociado con la instancia del bucle de eventos
  actual
source_url: https://www.php.net/manual/es/evloop.io.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evloop/io.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18250
---

EvLoop::io

Crea un objeto EvIo watcher asociado con la instancia del bucle de eventos actual

## Descripción

```php
final public EvLoop::io(mixed $fd, int $events, callable $callback, [mixed $data], [int $priority]): EvIo
```php

Crea un objeto EvIo watcher asociado con la instancia del bucle de eventos actual.

## Parámetros

Todos los parámetros tienen el mismo significado que los del método EvIo::\_\_construct.

## Valores devueltos

Devuelve un objeto EvIo en caso de éxito.

## Véase también

EvIo::\_\_construct
