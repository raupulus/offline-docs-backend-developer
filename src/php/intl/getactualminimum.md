---
title: IntlCalendar::getActualMinimum
description: El valor mínimo para un campo, considerando el tiempo actual del objeto
source_url: https://www.php.net/manual/es/intlcalendar.getactualminimum.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/getactualminimum.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40300
---

IntlCalendar::getActualMinimum

El valor mínimo para un campo, considerando el tiempo actual del objeto

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::getActualMinimum(int $field): int
```php

Estilo procedimental

```php
intlcal_get_actual_minimum(IntlCalendar $calendar, int $field): int
```

Devuelve el valor mínimo para un campo, considerando el tiempo actual del objeto. La semántica exacta varía según el campo, pero en el caso general, es el valor que se obtendría si se fijara el valor del campo al [mínimo relativo más grande](#intlcalendar.getgreatestminimum) para el campo y se decrementara hasta alcanzar el [mínimo global](#intlcalendar.getminimum) o que el valor del campo se reinicie, en cuyo caso el valor devuelto sería el mínimo global o el valor antes del reinicio, respectivamente.

Para el calendario gregoriano, es siempre el mismo valor que `IntlCalendar::getMinimum`.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

`field`  

## Valores devueltos

Un `int` que representa el valor mínimo en la unidad del campo o `false` si ocurre un error.

## Véase también

IntlCalendar::getMinimum, IntlCalendar::getGreatestMinimum, IntlCalendar::getActualMaximum
