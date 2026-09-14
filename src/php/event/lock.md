---
title: EventBuffer::lock
description: Bloquea un buffer
source_url: https://www.php.net/manual/es/eventbuffer.lock.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbuffer/lock.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 2b5c62c3b
order: 19240
---

EventBuffer::lock

Bloquea un buffer

## Descripción

```php
public EventBuffer::lock(): void
```php

Bloquea un buffer. Puede ser utilizado junto con EventBuffer::unlock para que un conjunto de operaciones sean atómicas, p.e. thread-safe. Notar que no se necesita bloquear buffers para operaciones *individuales* . Cuando el bloqueo está activo (ver EventBuffer::enableLocking ), las operaciones individuales en buffers de eventos ya son atómicas.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Véase también

EventBuffer::unlock
