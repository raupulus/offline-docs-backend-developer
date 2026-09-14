---
title: EventBufferEvent::setPriority
description: Asigna una prioridad para un búfer de eventos
source_url: https://www.php.net/manual/es/eventbufferevent.setpriority.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent/setpriority.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: da9d81816
order: 19530
---

EventBufferEvent::setPriority

Asigna una prioridad para un búfer de eventos

## Descripción

```php
public EventBufferEvent::setPriority(int $priority): bool
```php

Asigna una prioridad para un búfer de eventos.

> [!WARNING]
> Solo soportado para los sockets de búfer de eventos.

## Parámetros

`priority`  
Valor de la prioridad.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
