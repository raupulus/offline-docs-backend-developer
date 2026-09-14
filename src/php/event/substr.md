---
title: EventBuffer::substr
description: Sustrae una porción de los datos del búfer
source_url: https://www.php.net/manual/es/eventbuffer.substr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbuffer/substr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 940ea8c1b
order: 19330
---

EventBuffer::substr

Sustrae una porción de los datos del búfer

## Descripción

```php
public EventBuffer::substr(int $start, [int $length]): string
```php

Sustrae una cantidad de `length` bytes del búfer, comenzando en la posición `start`.

## Parámetros

`start`  
La posición de inicio de los datos a sustraer.

`length`  
Número máximo de bytes a sustraer.

## Valores devueltos

Devuelve los datos sustraídos en forma de string en caso de éxito, o bien `false` si ocurre un error.

## Véase también

EventBuffer::read
