---
title: EvLoop::idle
description: Crea un objeto EvIdle watcher asociado con la instancia del bucle de
  eventos actual
source_url: https://www.php.net/manual/es/evloop.idle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evloop/idle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18230
---

EvLoop::idle

Crea un objeto EvIdle watcher asociado con la instancia del bucle de eventos actual

## Descripción

```php
final public EvLoop::idle(callable $callback, [mixed $data], [int $priority]): EvIdle
```php

Crea un objeto EvIdle watcher asociado con la instancia del bucle de eventos actual

## Parámetros

Todos los parámetros tienen el mismo significado que los de la función EvIdle::\_\_construct

## Valores devueltos

Devuelve un objeto EvIdle en caso de éxito.

## Véase también

EvIdle::\_\_construct
