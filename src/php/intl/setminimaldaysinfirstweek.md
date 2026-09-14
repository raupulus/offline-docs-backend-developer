---
title: IntlCalendar::setMinimalDaysInFirstWeek
description: Define el número mínimo de días que la primera semana de un año o mes
  puede tener
source_url: https://www.php.net/manual/es/intlcalendar.setminimaldaysinfirstweek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/setminimaldaysinfirstweek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: bad9acb50
order: 40610
---

IntlCalendar::setMinimalDaysInFirstWeek

Define el número mínimo de días que la primera semana de un año o mes puede tener

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::setMinimalDaysInFirstWeek(int $days): true
```php

Estilo procedimental

```php
intlcal_set_minimal_days_in_first_week(IntlCalendar $calendar, int $days): true
```

Define el número mínimo de días que la primera semana de un año o mes puede tener en el nuevo año o mes. Por ejemplo, en el calendario gregoriano, si este valor es 1, entonces la primera semana del año incluirá necesariamente el 1 de enero, mientras que si este valor es 7, entonces la semana con el 1 de enero será la primera semana del año únicamente si el día de la semana para el 1 de enero corresponde al día de la semana devuelto por `IntlCalendar::getFirstDayOfWeek`; de lo contrario, será la última semana del año anterior.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

`days`  
El número de días mínimo a definir.

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

`ValueError` si `days` está fuera de rango (menos que `1` o más que `7`).

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Se lanza una `ValueError` ante una entrada inválida. Anteriormente, se devolvía `false`. |
