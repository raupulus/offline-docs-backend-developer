---
title: EventBufferEvent::write
description: Añade datos a un buffer de evento de salida
source_url: https://www.php.net/manual/es/eventbufferevent.write.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent/write.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: da9d81816
order: 19640
---

EventBufferEvent::write

Añade datos a un buffer de evento de salida

## Descripción

```php
public EventBufferEvent::write(string $data): bool
```php

Añade datos a un buffer de evento de salida.

## Parámetros

`data`  
Datos a añadir al buffer.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

EventBufferEvent::writeBuffer
