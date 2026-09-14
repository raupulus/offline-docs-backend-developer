---
title: EventBufferEvent::read
description: Lee los datos del búfer
source_url: https://www.php.net/manual/es/eventbufferevent.read.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent/read.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 5e5902c5d
order: 19500
---

EventBufferEvent::read

Lee los datos del búfer

## Descripción

```php
public EventBufferEvent::read(int $size): string
```php

Elimina los `size` bytes del búfer de entrada. Devuelve un string de datos leídos desde el búfer de entrada.

## Parámetros

`size`  
Número máximo de bytes a leer

## Valores devueltos

Devuelve el string de datos leídos desde el búfer de entrada.

## Véase también

EventBufferEvent::readBuffer
