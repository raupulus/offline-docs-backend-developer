---
title: EventBuffer::read
description: Lee los datos de un evbuffer y vacía los bytes leídos
source_url: https://www.php.net/manual/es/eventbuffer.read.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbuffer/read.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 940ea8c1b
order: 19280
---

EventBuffer::read

Lee los datos de un evbuffer y vacía los bytes leídos

## Descripción

```php
public EventBuffer::read(int $max_bytes): string
```php

Lee los primeros `max_bytes` bytes desde el búfer y vacía los bytes leídos. Si el argumento `max_bytes` representa más bytes de los disponibles en el búfer, todos los bytes disponibles serán leídos.

## Parámetros

`max_bytes`  
El número máximo de bytes a leer desde el búfer.

## Valores devueltos

Devuelve el string leído, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL event 1.6.0 | El método EventBuffer::read fue renombrado a EventBuffer::read. EventBuffer::read ahora toma solo un argumento: `max_bytes` ; ahora devuelve un string en lugar de un integer. |

## Véase también

EventBuffer::copyout

EventBuffer::drain

EventBuffer::pullup

EventBuffer::readLine

EventBuffer::appendFrom
