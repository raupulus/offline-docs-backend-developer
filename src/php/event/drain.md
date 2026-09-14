---
title: EventBuffer::drain
description: Elimina un número especificado de bytes desde el inicio del búfer sin
  copiar los datos
source_url: https://www.php.net/manual/es/eventbuffer.drain.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbuffer/drain.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19200
---

EventBuffer::drain

Elimina un número especificado de bytes desde el inicio del búfer sin copiar los datos

## Descripción

```php
public EventBuffer::drain(int $len): bool
```php

Funciona de la misma manera que el método EventBuffer::read excepto que los datos eliminados no son copiados: solo se eliminan del inicio del búfer.

## Parámetros

`len`  
El número de bytes a eliminar del búfer.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

EventBuffer::read

EventBuffer::appendFrom
