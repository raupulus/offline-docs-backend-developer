---
title: EventBuffer::readFrom
description: Lee datos desde un fichero y los coloca al final del búfer
source_url: https://www.php.net/manual/es/eventbuffer.readfrom.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbuffer/readfrom.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 940ea8c1b
order: 19290
---

EventBuffer::readFrom

Lee datos desde un fichero y los coloca al final del búfer

## Descripción

```php
public EventBuffer::read(mixed $fd, int $howmuch): int
```php

Lee datos desde el fichero `fd` y los coloca al final del búfer.

## Parámetros

`fd`  
Un socket, un flujo, o un descriptor de fichero numérico.

`howmuch`  
Número máximo de bytes a leer.

## Valores devueltos

Devuelve el número de bytes leídos, o `false` si ocurre un error.

## Véase también

EventBuffer::copyout

EventBuffer::drain

EventBuffer::pullup

EventBuffer::readLine

EventBuffer::appendFrom
