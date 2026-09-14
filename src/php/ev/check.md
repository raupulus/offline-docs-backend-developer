---
title: EvLoop::check
description: Crea un objeto EvCheck asociado con la instancia del bucle de eventos
  actual
source_url: https://www.php.net/manual/es/evloop.check.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evloop/check.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18170
---

EvLoop::check

Crea un objeto EvCheck asociado con la instancia del bucle de eventos actual

## Descripción

```php
final public EvLoop::check(string $callback, [string $data], [string $priority]): EvCheck
```php

Crea un objeto EvCheck asociado con la instancia del bucle de eventos actual.

## Parámetros

Todos los argumentos tienen el mismo significado que para el método EvCheck::\_\_construct.

## Valores devueltos

Devuelve un objeto EvCheck en caso de éxito.

## Véase también

EvCheck::\_\_construct
