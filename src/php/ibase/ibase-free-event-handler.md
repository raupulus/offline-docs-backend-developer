---
title: ibase_free_event_handler
description: Libera un gestor de eventos iBase
source_url: https://www.php.net/manual/es/function.ibase-free-event-handler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-free-event-handler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30360
---

ibase_free_event_handler

Libera un gestor de eventos iBase

## Descripción

```php
ibase_free_event_handler(resource $event): bool
```php

`ibase_free_event_handler` anula el gestor de eventos registrado, especificado por `event`. La función de retrollamada no será más ejecutada para los eventos que debía gestionar.

## Parámetros

`event`  
Un recurso de evento, creado por la función `ibase_set_event_handler`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

ibase_set_event_handler
