---
title: EvLoop::signal
description: Crea un objeto EvSignal watcher asociado con la instancia del bucle de
  eventos actual
source_url: https://www.php.net/manual/es/evloop.signal.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evloop/signal.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18330
---

EvLoop::signal

Crea un objeto EvSignal watcher asociado con la instancia del bucle de eventos actual

## Descripción

```php
final public EvLoop::signal(int $signum, callable $callback, [mixed $data], [int $priority]): EvSignal
```php

Crea un objeto EvSignal watcher asociado con la instancia del bucle de eventos actual.

## Parámetros

Todos los argumentos tienen el mismo significado que los de la método EvSignal::\_\_construct.

## Valores devueltos

Devuelve un objeto EvSignal en caso de éxito.

## Véase también

EvSignal::\_\_construct
