---
title: EvLoop::timer
description: Crea un objeto EvTimer watcher asociado con la instancia del bucle de
  eventos actual
source_url: https://www.php.net/manual/es/evloop.timer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evloop/timer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18370
---

EvLoop::timer

Crea un objeto EvTimer watcher asociado con la instancia del bucle de eventos actual

## Descripción

```php
final public EvLoop::timer(float $after, float $repeat, callable $callback, [mixed $data], [int $priority]): EvTimer
```php

Crea un objeto EvTimer watcher asociado con la instancia del bucle de eventos actual.

## Parámetros

Todos los argumentos tienen el mismo significado que los de la función EvTimer::\_\_construct.

## Valores devueltos

Devuelve el objeto EvTimer en caso de éxito.

## Véase también

EvTimer::\_\_construct
