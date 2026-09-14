---
title: EventHttpRequest::sendReplyChunk
description: Envía otro bloque de datos como parte de un bloque de respuesta entrante
source_url: https://www.php.net/manual/es/eventhttprequest.sendreplychunk.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventhttprequest/sendreplychunk.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 919c8a799
order: 20290
---

EventHttpRequest::sendReplyChunk

Envía otro bloque de datos como parte de un bloque de respuesta entrante

## Descripción

```php
public EventHttpRequest::sendReplyChunk(EventBuffer $buf): void
```php

Envía otro bloque de datos como parte de un bloque de respuesta entrante. Después de la llamada a este método, el parámetro `buf` estará vacío.

## Parámetros

`buf`  
El bloque de datos a enviar como parte de la respuesta.

## Valores devueltos

No se retorna ningún valor.

## Véase también

EventHttpRequest::sendReplyStart

EventHttpRequest::sendReplyEnd
