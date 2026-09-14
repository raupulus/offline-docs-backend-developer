---
title: EvLoop::child
description: Crea un objeto EvChild asociado con el bucle de eventos actual
source_url: https://www.php.net/manual/es/evloop.child.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evloop/child.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18180
---

EvLoop::child

Crea un objeto EvChild asociado con el bucle de eventos actual

## Descripción

```php
final public EvLoop::child(string $pid, string $trace, string $callback, [string $data], [string $priority]): EvChild
```php

Crea un objeto EvChild asociado con el bucle de eventos actual.

## Parámetros

Todos los argumentos tienen el mismo significado que para el método EvChild::\_\_construct.

## Valores devueltos

Devuelve un objeto EvChild en caso de éxito.

## Véase también

EvChild::\_\_construct
