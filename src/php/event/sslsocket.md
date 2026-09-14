---
title: EventBufferEvent::sslSocket
description: Crea un nuevo buffer SSL cuyos datos serán enviados a través de un socket
  SSL
source_url: https://www.php.net/manual/es/eventbufferevent.sslsocket.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent/sslsocket.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19630
---

EventBufferEvent::sslSocket

Crea un nuevo buffer SSL cuyos datos serán enviados a través de un socket SSL

## Descripción

```php
public static EventBufferEvent::sslSocket(EventBase $base, mixed $socket, EventSslContext $ctx, int $state, [int $options]): EventBufferEvent
```php

Crea un nuevo buffer SSL cuyos datos serán enviados a través de un socket SSL.

## Parámetros

`base`  
Evento base asociado.

`socket`  
Socket a utilizar para este SSL. Puede ser un flujo, un recurso de socket, un descriptor numérico de fichero, o `null`. Si el argumento `socket` es `null`, se asume que el descriptor de fichero para este socket será asignado posteriormente a través del método EventBufferEvent::connectHost.

`ctx`  
Objeto de la clase `EventSslContext`.

`state`  
El estado actual de la conexión SSL: `EventBufferEvent::SSL_OPEN`, `EventBufferEvent::SSL_ACCEPTING` o `EventBufferEvent::SSL_CONNECTING`.

`options`  
Las opciones del buffer de evento.

## Valores devueltos

Devuelve un objeto `EventBufferEvent`.

## Véase también

EventBufferEvent::sslFilter
