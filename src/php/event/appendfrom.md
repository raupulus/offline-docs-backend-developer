---
title: EventBuffer::appendFrom
description: Mueve el número de bytes especificados desde un buffer fuente, al final
  del buffer actual
source_url: https://www.php.net/manual/es/eventbuffer.appendfrom.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbuffer/appendfrom.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: a47dff201
order: 19170
---

EventBuffer::appendFrom

Mueve el número de bytes especificados desde un buffer fuente, al final del buffer actual

## Descripción

```php
public EventBuffer::appendFrom(EventBuffer $buf, int $len): int
```php

Mueve el número de bytes especificados desde un buffer fuente, al final del buffer actual. Si hay menos bytes, mueve todos los bytes disponibles del buffer fuente.

## Parámetros

`buf`  
Buffer fuente.

`len`  

## Valores devueltos

Devuelve el número de bytes leídos.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL event 1.6.0 | Renombrado de EventBuffer::appendFrom(nombre antiguo del método) a EventBuffer::appendFrom. |

## Véase también

EventBuffer::copyout

EventBuffer::drain

EventBuffer::pullup

EventBuffer::readLine

EventBuffer::read
