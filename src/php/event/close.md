---
title: EventBufferEvent::close
description: Cierra el descriptor de fichero asociado con el buffer de eventos actual
source_url: https://www.php.net/manual/es/eventbufferevent.close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent/close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 04f603bc6
order: 19380
---

EventBufferEvent::close

Cierra el descriptor de fichero asociado con el buffer de eventos actual

## Descripción

```php
public EventBufferEvent::close(): void
```php

Cierra el descriptor de fichero asociado con el buffer de eventos actual.

Este método puede ser utilizado en los casos donde la opción `EventBufferEvent::OPT_CLOSE_ON_FREE` no es apropiada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.
