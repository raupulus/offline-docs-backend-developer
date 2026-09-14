---
title: EventBufferEvent::setCallbacks
description: Asigna las funciones de retrollamada para la lectura, la escritura y
  los estados de eventos
source_url: https://www.php.net/manual/es/eventbufferevent.setcallbacks.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent/setcallbacks.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19520
---

EventBufferEvent::setCallbacks

Asigna las funciones de retrollamada para la lectura, la escritura y los estados de eventos

## Descripción

```php
public EventBufferEvent::setCallbacks(callable $readcb, callable $writecb, callable $eventcb, [mixed $arg]): void
```php

Asigna las funciones de retrollamada para la lectura, la escritura y los estados de eventos.

## Parámetros

`readcb`  
Función de retrollamada para un evento de lectura. Véase las [funciones de retrollamada para los tampones de eventos](#eventbufferevent.about.callbacks).

`writecb`  
Función de retrollamada para un evento de escritura. Véase las [funciones de retrollamada para los tampones de eventos](#eventbufferevent.about.callbacks).

`eventcb`  
Función de retrollamada para un evento de cambio de estado. Véase las [funciones de retrollamada para los tampones de eventos](#eventbufferevent.about.callbacks).

`arg`  
Una variable que será pasada a todas las funciones de retrollamada.

## Valores devueltos

No se retorna ningún valor.

## Véase también

EventBufferEvent::\_\_construct
