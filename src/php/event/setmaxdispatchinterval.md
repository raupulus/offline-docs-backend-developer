---
title: EventConfig::setMaxDispatchInterval
description: Evita la inversión de prioridades
source_url: https://www.php.net/manual/es/eventconfig.setmaxdispatchinterval.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventconfig/setmaxdispatchinterval.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19720
---

EventConfig::setMaxDispatchInterval

Evita la inversión de prioridades

## Descripción

```php
public EventConfig::setMaxDispatchInterval(int $max_interval, int $max_callbacks, int $min_priority): void
```php

Evita la inversión de prioridades limitando el número de funciones de retrollamada de eventos de baja prioridad que pueden ser invocadas antes de verificar la presencia de eventos de alta prioridad.

> [!NOTE]
> Disponible a partir de `libevent 2.1.0-alpha`.

## Parámetros

`max_interval`  
Un intervalo después del cual Libevent detendrá la ejecución de las funciones de retrollamada y verificará la presencia de otros eventos, o `0` si no debe haber tal intervalo.

`max_callbacks`  
Un número de funciones de retrollamada después del cual Libevent debe detener la ejecución de las funciones de retrollamada y verificar la presencia de otros eventos, o `-1` si no debe haber tal límite.

`min_priority`  
Una prioridad por debajo de la cual `max_interval` y `max_callbacks` no deben ser tomados en cuenta. Si se define a `0`, serán tomados en cuenta para los eventos de cualquier prioridad; si se define a `1`, serán tomados en cuenta para los eventos de prioridad `1` y así sucesivamente.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
