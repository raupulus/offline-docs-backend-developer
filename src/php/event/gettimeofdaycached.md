---
title: EventBase::getTimeOfDayCached
description: Devuelve el tiempo del evento base actual
source_url: https://www.php.net/manual/es/eventbase.gettimeofdaycached.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbase/gettimeofdaycached.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_revision: '475439775'
order: 19070
---

EventBase::getTimeOfDayCached

Devuelve el tiempo del evento base actual

## Descripción

```php
public EventBase::getTimeOfDayCached(): float
```php

En caso de éxito devuelve el tiempo actual(como el devuelto por `gettimeofday()` ), mirando el valor en la caché dentro de *base* si es posible, y llamando a `gettimeofday()` o `clock_gettime()` si no hay tiempo disponible en la caché.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el actual tiempo de *event base* . En caso de error devuelve `null`.
