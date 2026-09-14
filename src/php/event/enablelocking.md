---
title: EventBuffer::enableLocking
source_url: https://www.php.net/manual/es/eventbuffer.enablelocking.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbuffer/enablelocking.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: e8ac70bf5
order: 19210
---

EventBuffer::enableLocking

## Descripción

```php
public EventBuffer::enableLocking(): void
```php

Se activa el bloqueo del `EventBuffer`, permitiendo así su uso seguro por varios hilos simultáneamente. Cuando el bloqueo está activado, el bloqueo se coloca cuando se llaman las funciones de retrollamada. Este comportamiento puede provocar bloqueos si no se tiene cuidado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Véase también

Evbuffers and Thread-safety
