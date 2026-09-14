---
title: EventBase::gotExit
description: Verifica si se ha solicitado que el bucle de eventos salga
source_url: https://www.php.net/manual/es/eventbase.gotexit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbase/gotexit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19080
---

EventBase::gotExit

Verifica si se ha solicitado que el bucle de eventos salga

## Descripción

```php
public EventBase::gotExit(): bool
```php

Verifica si se ha solicitado que el bucle de eventos salga mediante el método EventBase::exit.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si se ha solicitado que el bucle de eventos salga mediante el método EventBase::exit. `false` en caso contrario.

## Véase también

EventBase::exit

EventBase::stop

EventBase::gotStop
