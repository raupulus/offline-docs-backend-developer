---
title: EventBufferEvent::sslFilter
description: Crea un nuevo búfer de evento SSL, cuyos datos serán enviados a través
  de otro búfer de evento
source_url: https://www.php.net/manual/es/eventbufferevent.sslfilter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent/sslfilter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: a47dff201
order: 19570
---

EventBufferEvent::sslFilter

Crea un nuevo búfer de evento SSL, cuyos datos serán enviados a través de otro búfer de evento

## Descripción

```php
public static EventBufferEvent::sslFilter(EventBase $base, EventBufferEvent $underlying, EventSslContext $ctx, int $state, [int $options]): EventBufferEvent
```php

Crea un nuevo búfer de evento SSL, cuyos datos serán enviados a través de otro búfer de evento.

> [!NOTE]
> Este método solo está disponible si `Event` ha sido compilado con soporte OpenSSL.

## Parámetros

`base`  
Evento base asociado.

`underlying`  
Un socket de búfer de evento a utilizar para este SSL.

`ctx`  
Objeto de la clase `EventSslContext`.

`state`  
El estado actual de la conexión SSL: `EventBufferEvent::SSL_OPEN`, `EventBufferEvent::SSL_ACCEPTING` o `EventBufferEvent::SSL_CONNECTING`.

`options`  
Una o más opciones de búfer de evento.

## Valores devueltos

Devuelve un nuevo objeto `EventBufferEvent` SSL.

## Ejemplos

## Véase también

EventBufferEvent::sslSocket
