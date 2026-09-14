---
title: EventHttpRequest::getBufferEvent
description: Devuelve el objeto EventBufferEvent
source_url: https://www.php.net/manual/es/eventhttprequest.getbufferevent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventhttprequest/getbufferevent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 184764a63
order: 20160
---

EventHttpRequest::getBufferEvent

Devuelve el objeto EventBufferEvent

## Descripción

```php
public EventHttpRequest::getBufferEvent(): EventBufferEvent
```php

Devuelve el objeto `EventBufferEvent` que representa el evento de buffer que la conexión utiliza.

> [!WARNING]
> El contador de referencia del objeto devuelto será incrementado en uno para proteger las estructuras internas contra destrucciones prematuras cuando el método es llamado desde una función de retrollamada. El objeto `EventBufferEvent` debe ser liberado explícitamente a través del método EventBufferEvent::free. De lo contrario, habrá una fuga de memoria.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un objeto `EventBufferEvent`.

## Véase también

EventHttpRequest::getConnection
