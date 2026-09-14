---
title: EventBuffer::prepend
description: Añade datos al principio del buffer
source_url: https://www.php.net/manual/es/eventbuffer.prepend.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbuffer/prepend.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: da9d81816
order: 19250
---

EventBuffer::prepend

Añade datos al principio del buffer

## Descripción

```php
public EventBuffer::prepend(string $data): bool
```php

Añade datos al principio del buffer.

## Parámetros

`data`  
String a añadir al principio del buffer.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

EventBuffer::prependBuffer

EventBuffer::add

EventBuffer::addBuffer
