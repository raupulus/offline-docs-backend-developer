---
title: EventBufferEvent::setTimeouts
description: Define el modo de lectura y escritura para el tiempo de espera máximo
  de un búfer de eventos
source_url: https://www.php.net/manual/es/eventbufferevent.settimeouts.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent/settimeouts.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: da9d81816
order: 19540
---

EventBufferEvent::setTimeouts

Define el modo de lectura y escritura para el tiempo de espera máximo de un búfer de eventos

## Descripción

```php
public EventBufferEvent::setTimeouts(float $timeout_read, float $timeout_write): bool
```php

Define el modo de lectura y escritura para el tiempo de espera máximo de un búfer de eventos.

## Parámetros

`timeout_read`  
La lectura del tiempo de espera máximo

`timeout_write`  
La escritura del tiempo de espera máximo

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
