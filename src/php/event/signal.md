---
title: Event::signal
description: Construye un objeto de evento de señal
source_url: https://www.php.net/manual/es/event.signal.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/event/signal.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 18940
---

Event::signal

Construye un objeto de evento de señal

## Descripción

```php
public static Event::signal(EventBase $base, int $signum, callable $cb, [mixed $arg]): Event
```php

Construye un objeto de evento de señal. Es un método simple para crear un evento de señal. Tenga en cuenta que el método genérico Event::\_\_construct también puede construir un objeto de evento de señal.

## Parámetros

`base`  
El objeto de base de evento asociado.

`signum`  
El número de la señal.

`cb`  
La función de retrollamada del evento de señal. Ver las [funciones de retrollamada de eventos](#event.callbacks).

`arg`  
Datos personalizados. Si se especifican, serán pasados a la función de retrollamada cuando el evento lance los triggers.

## Valores devueltos

Devuelve un objeto de evento en caso de éxito, `false` de lo contrario.

## Véase también

La construcción de eventos de señal
