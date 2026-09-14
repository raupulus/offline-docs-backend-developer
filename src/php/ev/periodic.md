---
title: EvLoop::periodic
description: Crea un objeto EvPeriodic watcher asociado con la instancia del bucle
  de eventos actual
source_url: https://www.php.net/manual/es/evloop.periodic.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evloop/periodic.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: 940ea8c1b
order: 18290
---

EvLoop::periodic

Crea un objeto EvPeriodic watcher asociado con la instancia del bucle de eventos actual

## Descripción

```php
final public EvLoop::periodic(float $offset, float $interval, callable $callback, [mixed $data], [int $priority]): EvPeriodic
```php

Crea un objeto EvPeriodic watcher asociado con la instancia del bucle de eventos actual.

## Parámetros

Todos los parámetros tienen el mismo significado que los de la método EvPeriodic::\_\_construct.

## Valores devueltos

Devuelve un objeto EvPeriodic en caso de éxito.

## Véase también

EvPeriodic::\_\_construct
