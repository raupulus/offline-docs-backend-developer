---
title: EventBase::loop
description: Distribuye los eventos en espera
source_url: https://www.php.net/manual/es/eventbase.loop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbase/loop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: a47dff201
order: 19100
---

EventBase::loop

Distribuye los eventos en espera

## Descripción

```php
public EventBase::loop([int $flags]): bool
```php

Espera a que los eventos se vuelvan activos, luego, ejecuta sus funciones de retrollamada.

> [!WARNING]

## Parámetros

`flags`  
Banderas opcionales. Una constante `EventBase::LOOP_*`. Ver las [constantes EventBase](#eventbase.constants).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

EventBase::dispatch
