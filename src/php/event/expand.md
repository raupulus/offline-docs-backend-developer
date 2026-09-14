---
title: EventBuffer::expand
description: Reserva espacio en el buffer
source_url: https://www.php.net/manual/es/eventbuffer.expand.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbuffer/expand.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: da9d81816
order: 19220
---

EventBuffer::expand

Reserva espacio en el buffer

## Descripción

```php
public EventBuffer::expand(int $len): bool
```php

Modifica el último bloque de memoria del buffer, o añade un nuevo bloque, de modo que el buffer es ahora suficientemente grande para contener `len` bytes sin añadir espacios suplementarios.

## Parámetros

`len`  
El número de bytes a reservar del buffer

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
