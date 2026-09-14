---
title: EventBase::gotStop
description: Verifica si se ha solicitado que la iteración de eventos se detenga
source_url: https://www.php.net/manual/es/eventbase.gotstop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbase/gotstop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19090
---

EventBase::gotStop

Verifica si se ha solicitado que la iteración de eventos se detenga

## Descripción

```php
public EventBase::gotStop(): bool
```php

Verifica si se ha solicitado que la iteración de eventos se detenga mediante el método EventBase::stop.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si se ha solicitado que la iteración de eventos se detenga mediante el método EventBase::stop. `false` en caso contrario.

## Véase también

EventBase::exit

EventBase::stop

EventBase::gotExit
