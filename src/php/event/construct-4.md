---
title: EventBufferEvent::__construct
description: Construye un objeto EventBufferEvent
source_url: https://www.php.net/manual/es/eventbufferevent.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19410
---

EventBufferEvent::\_\_construct

Construye un objeto EventBufferEvent

## Descripción

```php
public EventBufferEvent::__construct(EventBase $base, [mixed $socket], [int $options], [callable $readcb], [callable $writecb], [callable $eventcb], [mixed $arg])
```php

Crea un buffer de eventos en un socket, un flujo o un descriptor de fichero. Pasar el valor `null` al parámetro `socket` significa que el socket debe ser creado posteriormente, es decir, a través del método EventBufferEvent::connect.

## Parámetros

`base`  
Evento base que debe ser asociado con el nuevo buffer de eventos.

`socket`  
Debe ser creado como flujo (no necesariamente a través de la extensión `sockets`)

`options`  
Una constante entre las constantes [EventBufferEvent::OPT\_\*](#eventbufferevent.constants), o `0`.

`readcb`  
Función de retrollamada para los eventos de lectura. Ver también las [funciones de retrollamada del buffer de eventos](#eventbufferevent.about.callbacks).

`writecb`  
Función de retrollamada para los eventos de escritura. Ver también las [funciones de retrollamada del buffer de eventos](#eventbufferevent.about.callbacks).

`eventcb`  
Función de retrollamada para los eventos de cambio de estado. Ver también las [funciones de retrollamada del buffer de eventos](#eventbufferevent.about.callbacks).

`arg`  
Una variable que será pasada a todas las funciones de retrollamada.

## Véase también

EventBufferEvent::sslFilter

EventBufferEvent::sslSocket
