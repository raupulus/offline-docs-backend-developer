---
title: EventBufferEvent::readBuffer
description: Vacía el contenido entero del búfer de entrada y lo coloca en el búfer
source_url: https://www.php.net/manual/es/eventbufferevent.readbuffer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent/readbuffer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19510
---

EventBufferEvent::readBuffer

Vacía el contenido entero del búfer de entrada y lo coloca en el búfer

## Descripción

```php
public EventBufferEvent::readBuffer(EventBuffer $buf): bool
```php

Vacía el contenido entero del búfer de entrada y lo coloca en el búfer `buf`.

## Parámetros

`buf`  
Búfer objetivo

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

EventBufferEvent::read
