---
title: EventBuffer::prependBuffer
description: Desplaza todos los datos desde el buffer fuente hacia el inicio del buffer
  actual
source_url: https://www.php.net/manual/es/eventbuffer.prependbuffer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbuffer/prependbuffer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19260
---

EventBuffer::prependBuffer

Desplaza todos los datos desde el buffer fuente hacia el inicio del buffer actual

## Descripción

```php
public EventBuffer::prependBuffer(EventBuffer $buf): bool
```php

Funciona exactamente como el método EventBuffer::addBuffer, excepto que desplaza los datos al inicio del buffer.

## Parámetros

`buf`  
Buffer fuente.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

EventBuffer::add

EventBuffer::addBuffer

EventBuffer::prepend
