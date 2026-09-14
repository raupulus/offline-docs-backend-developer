---
title: EventBuffer::copyout
description: Copia el número de bytes especificado desde el inicio del búfer
source_url: https://www.php.net/manual/es/eventbuffer.copyout.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbuffer/copyout.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19190
---

EventBuffer::copyout

Copia el número de bytes especificado desde el inicio del búfer

## Descripción

```php
public EventBuffer::copyout(string $data, int $max_bytes): int
```php

Funciona de la misma manera que el método EventBuffer::read, pero no vacía los datos del búfer. Es decir, el método copia los primeros `max_bytes` bytes desde el inicio del búfer en el argumento `data`. Si hay menos de `max_bytes` bytes disponibles, el método copia todos los bytes presentes.

## Parámetros

`data`  
String de salida.

`max_bytes`  
El número de bytes a copiar.

## Valores devueltos

Devuelve el número de bytes copiados, o `-1` si ocurre un error.

## Véase también

EventBuffer::read

EventBuffer::appendFrom
