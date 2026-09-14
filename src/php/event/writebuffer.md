---
title: EventBufferEvent::writeBuffer
description: Añade el contenido entero de un buffer en un buffer de evento de salida
source_url: https://www.php.net/manual/es/eventbufferevent.writebuffer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent/writebuffer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: da9d81816
order: 19650
---

EventBufferEvent::writeBuffer

Añade el contenido entero de un buffer en un buffer de evento de salida

## Descripción

```php
public EventBufferEvent::writeBuffer(EventBuffer $buf): bool
```php

Añade el contenido entero de un buffer en un buffer de evento de salida.

## Parámetros

`buf`  
Objeto `EventBuffer` fuente.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

EventBufferEvent::write
