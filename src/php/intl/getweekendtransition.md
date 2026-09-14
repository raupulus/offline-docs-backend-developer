---
title: IntlCalendar::getWeekendTransition
description: Obtiene la hora del día en la que comienza o termina el fin de semana
source_url: https://www.php.net/manual/es/intlcalendar.getweekendtransition.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/getweekendtransition.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40490
---

IntlCalendar::getWeekendTransition

Obtiene la hora del día en la que comienza o termina el fin de semana

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::getWeekendTransition(int $dayOfWeek): int
```php

Estilo procedimental

```php
intlcal_get_weekend_transition(IntlCalendar $calendar, int $dayOfWeek): int
```

Devuelve el número de milisegundos transcurridos desde la medianoche en la hora en la que comienza o termina el fin de semana.

Esto es aplicable únicamente para los días de la semana para los cuales `IntlCalendar::getDayOfWeekType` devuelve `IntlCalendar::DOW_TYPE_WEEKEND_OFFSET` o `IntlCalendar::DOW_TYPE_WEEKEND_CEASE`. Llamar a esta función para otros días de la semana es una condición de error.

Esta función requiere ICU 4.4 o superior.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

`dayOfWeek`  
Una de las constantes `IntlCalendar::DOW_SUNDAY`, `IntlCalendar::DOW_MONDAY`, …, `IntlCalendar::DOW_SATURDAY`.

## Valores devueltos

El número de milisegundos transcurridos desde la medianoche en la hora en la que el fin de semana comienza o termina o `false` si ocurre un error.

## Ejemplos

Ver un ejemplo en `IntlCalendar::getDayOfWeekType`.
