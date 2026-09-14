---
title: EventBase::dispatch
description: Despacha eventos pendientes
source_url: https://www.php.net/manual/es/eventbase.dispatch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbase/dispatch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_revision: a47dff201
order: 19020
---

EventBase::dispatch

Despacha eventos pendientes

## Descripción

```php
public EventBase::dispatch(): void
```php

Espara a que los eventos estén activos y ejecuta sus llamadas de retorno. Hace lo mismo que EventBase::loop pero sin flags definidas.

> [!WARNING]

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

EventBase::loop
