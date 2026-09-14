---
title: EventBuffer::addBuffer
description: Desplaza todos los datos del búfer proporcionado al EventBuffer actual
source_url: https://www.php.net/manual/es/eventbuffer.addbuffer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbuffer/addbuffer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19160
---

EventBuffer::addBuffer

Desplaza todos los datos del búfer proporcionado al EventBuffer actual

## Descripción

```php
public EventBuffer::addBuffer(EventBuffer $buf): bool
```php

Desplaza todos los datos del búfer proporcionado por el argumento `buf` al final del `EventBuffer` actual. Se trata de una adición destructiva. Los datos del primer búfer son desplazados al otro. Sin embargo, no se produce ninguna copia en memoria.

## Parámetros

`buf`  
El objeto EventBuffer de origen.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

EventBuffer::add
