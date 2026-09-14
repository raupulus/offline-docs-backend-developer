---
title: EventBuffer::unlock
description: Libera un bloqueo adquirido con EventBuffer::lock
source_url: https://www.php.net/manual/es/eventbuffer.unlock.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbuffer/unlock.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19350
---

EventBuffer::unlock

Libera un bloqueo adquirido con EventBuffer::lock

## Descripción

```php
public EventBuffer::unlock(): bool
```php

Libera un bloqueo adquirido con el método EventBuffer::lock.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

EventBuffer::lock
