---
title: Event::setTimer
description: Reconfigurar un evento timer
source_url: https://www.php.net/manual/es/event.settimer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/event/settimer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 18930
---

Event::setTimer

Reconfigurar un evento timer

## Descripción

```php
public Event::setTimer(EventBase $base, callable $cb, [mixed $arg]): bool
```php

Reconfigurar un evento timer. Téngase en cuenta que este método no llama a la función obsoleta `event_set` de libevent. En su lugar, llama a la función `event_assign`.

## Parámetros

`base`  
La base de evento a asociar.

`cb`  
La función de retrollamada del evento timer. Ver las [funciones de retrollamada de eventos](#event.callbacks).

`arg`  
Datos personalizados. Si se especifican, serán pasados a la función de retrollamada cuando el evento dispare los triggers.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

Event::\_\_construct

Event::timer
