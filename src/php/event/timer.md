---
title: Event::timer
description: Construye un objeto de evento timer
source_url: https://www.php.net/manual/es/event.timer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/event/timer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 18950
---

Event::timer

Construye un objeto de evento timer

## Descripción

```php
public static Event::timer(EventBase $base, callable $cb, [mixed $arg]): Event
```php

Construye un objeto de evento timer. Se trata de un método simple para crear un evento timer. Téngase en cuenta que el método genérico Event::\_\_construct también puede construir objetos de eventos signal.

## Parámetros

`base`  
El objeto de base de evento asociado.

`cb`  
La función de retrollamada de evento signal. Ver las [funciones de retrollamada de eventos](#event.callbacks).

`arg`  
Datos personalizados. Si se especifican, serán pasados a la función de retrollamada cuando el evento lance los triggers.

## Valores devueltos

Devuelve un objeto de evento en caso de éxito, `false` en caso contrario.
