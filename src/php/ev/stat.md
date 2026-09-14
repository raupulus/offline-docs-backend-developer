---
title: EvLoop::stat
description: Crea un objeto EvStat watcher asociado con la instancia del bucle de
  eventos actual
source_url: https://www.php.net/manual/es/evloop.stat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evloop/stat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18340
---

EvLoop::stat

Crea un objeto EvStat watcher asociado con la instancia del bucle de eventos actual

## Descripción

```php
final public EvLoop::stat(string $path, float $interval, callable $callback, [mixed $data], [int $priority]): EvStat
```php

Crea un objeto EvStat watcher asociado con la instancia del bucle de eventos actual.

## Parámetros

Todos los parámetros tienen el mismo significado que los de la función EvSignal::\_\_construct.

## Valores devueltos

Devuelve un objeto EvStat en caso de éxito.

## Véase también

EvSignal::\_\_construct
