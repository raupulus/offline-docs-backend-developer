---
title: EventBufferEvent::disable
description: Desactiva los eventos de lectura, escritura o ambos en un evento de búfer
source_url: https://www.php.net/manual/es/eventbufferevent.disable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent/disable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19430
---

EventBufferEvent::disable

Desactiva los eventos de lectura, escritura o ambos en un evento de búfer

## Descripción

```php
public EventBufferEvent::disable(int $events): bool
```php

Desactiva los eventos `Event::READ`, `Event::WRITE`, o `Event::READ``|``Event::WRITE` en un evento de búfer.

## Parámetros

`events`  

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

EventBufferEvent::enable
