---
title: EventBuffer::freeze
description: Evita que las llamadas puedan modificar un buffer de eventos
source_url: https://www.php.net/manual/es/eventbuffer.freeze.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbuffer/freeze.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: da9d81816
order: 19230
---

EventBuffer::freeze

Evita que las llamadas puedan modificar un buffer de eventos

## Descripción

```php
public EventBuffer::freeze(bool $at_front): bool
```php

Evita que las llamadas puedan modificar un buffer de eventos

## Parámetros

`at_front`  
Permite desactivar cambios en el principio o final del buffer.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

EventBuffer::unfreeze
