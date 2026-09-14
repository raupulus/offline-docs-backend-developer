---
title: Event::__construct
description: Construye un objeto Event
source_url: https://www.php.net/manual/es/event.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/event/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 18840
---

Event::\_\_construct

Construye un objeto Event

## Descripción

```php
public Event::__construct(EventBase $base, mixed $fd, int $what, callable $cb, [mixed $arg])
```php

Construye un objeto Event.

## Parámetros

`base`  
La base de evento a asociar.

`fd`  
Recurso de flujo, recurso de socket, o descriptor numérico de fichero. Para los eventos timer, pase como valor `-1`. Para los eventos de tipo señal, pase el número de la señal, i.e. `SIGHUP`.

`what`  
Flags de eventos. Ver los [flags de eventos](#event.flags) para más detalles.

`cb`  
La función de retrollamada del evento. Ver las [funciones de retrollamada de eventos](#event.callbacks) para más detalles.

`arg`  
Datos personalizados. Si se especifican, serán pasados a la función de retrollamada cuando el evento haya lanzado los triggers.

## Véase también

Event::signal

Event::timer
