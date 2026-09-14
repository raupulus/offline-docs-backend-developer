---
title: EventBuffer::unfreeze
description: Re-activa las llamadas que permiten modificar un buffer de eventos
source_url: https://www.php.net/manual/es/eventbuffer.unfreeze.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbuffer/unfreeze.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: da9d81816
order: 19340
---

EventBuffer::unfreeze

Re-activa las llamadas que permiten modificar un buffer de eventos

## Descripción

```php
public EventBuffer::unfreeze(bool $at_front): bool
```php

Re-activa las llamadas que permiten modificar un buffer de eventos.

## Parámetros

`at_front`  
Si se deben activar los eventos al principio o al final del buffer.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

EventBuffer::freeze
