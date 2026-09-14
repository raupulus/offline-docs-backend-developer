---
title: EventBufferEvent::enable
description: Activa los eventos de lectura, escritura, o ambos, en un evento de buffer
source_url: https://www.php.net/manual/es/eventbufferevent.enable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent/enable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19440
---

EventBufferEvent::enable

Activa los eventos de lectura, escritura, o ambos, en un evento de buffer

## Descripción

```php
public EventBufferEvent::enable(int $events): bool
```php

Activa los eventos `Event::READ`, `Event::WRITE`, o `Event::READ``|``Event::WRITE` en un evento de buffer.

## Parámetros

`events`  
`Event::READ`, `Event::WRITE`, o `Event::READ``|``Event::WRITE` en un evento de buffer.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

EventBufferEvent::disable
