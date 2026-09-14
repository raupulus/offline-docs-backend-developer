---
title: EvLoop::prepare
description: Crea un objeto EvPrepare watcher asociado con la instancia del bucle
  de eventos actual
source_url: https://www.php.net/manual/es/evloop.prepare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evloop/prepare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: 940ea8c1b
order: 18300
---

EvLoop::prepare

Crea un objeto EvPrepare watcher asociado con la instancia del bucle de eventos actual

## Descripción

```php
final public EvLoop::prepare(callable $callback, [mixed $data], [int $priority]): EvPrepare
```php

Crea un objeto EvPrepare watcher asociado con la instancia del bucle de eventos actual.

## Parámetros

Todos los parámetros tienen el mismo significado que los de la función EvPrepare.

## Valores devueltos

Devuelve un objeto EvPrepare en caso de éxito.

## Véase también

EvPrepare::\_\_construct
