---
title: EvLoop::fork
description: Crea un objeto EvFork watcher asociado con la instancia del bucle de
  eventos actual
source_url: https://www.php.net/manual/es/evloop.fork.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evloop/fork.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18220
---

EvLoop::fork

Crea un objeto EvFork watcher asociado con la instancia del bucle de eventos actual

## Descripción

```php
final public EvLoop::fork(callable $callback, [mixed $data], [int $priority]): EvFork
```php

Crea un objeto EvFork watcher asociado con la instancia del bucle de eventos actual

## Parámetros

Todos los parámetros tienen el mismo significado que los de la función EvFork::\_\_construct.

## Valores devueltos

Devuelve el objeto EvFork en caso de éxito.

## Véase también

EvFork::\_\_construct
