---
title: IntlCalendar::getActualMaximum
description: El valor máximo para un campo, considerando el tiempo actual del objeto
source_url: https://www.php.net/manual/es/intlcalendar.getactualmaximum.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/getactualmaximum.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40290
---

IntlCalendar::getActualMaximum

El valor máximo para un campo, considerando el tiempo actual del objeto

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::getActualMaximum(int $field): int
```php

Estilo procedimental

```php
intlcal_get_actual_maximum(IntlCalendar $calendar, int $field): int
```

Devuelve el valor máximo para un campo, considerando el tiempo actual del objeto. La semántica exacta varía según el campo, pero en el caso general, es el valor que se obtendría si se fijara el valor del campo al [mínimo máximo relativo](#intlcalendar.getleastmaximum) para el campo y se incrementara hasta alcanzar el [máximo global](#intlcalendar.getmaximum) o que el valor del campo se reinicie, en cuyo caso el valor devuelto sería el máximo global o el valor antes del reinicio, respectivamente.

Por ejemplo, en el calendario gregoriano, el valor máximo real para el [día del mes](#intlcalendar.constants.field-day-of-month) variaría entre `28` y `31`, según el mes y el año del tiempo actual.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

`field`  

## Valores devueltos

Un `int` que representa el valor máximo en las unidades asociadas al `field` dado o `false` si ocurre un error.

## Ejemplos

`IntlCalendar::getActualMaximum`

```php
<?php
ini_set('date.timezone', 'Europe/Lisbon');

$cal = IntlCalendar::fromDateTime('2013-02-15');
var_dump($cal->getActualMaximum(IntlCalendar::FIELD_DAY_OF_MONTH)); //28

$cal->add(IntlCalendar::FIELD_EXTENDED_YEAR, -1);
var_dump($cal->getActualMaximum(IntlCalendar::FIELD_DAY_OF_MONTH)); //29

    
```

El ejemplo anterior mostrará:

    int(28)
    int(29)

## Véase también

IntlCalendar::getMaximum, IntlCalendar::getLeastMaximum, IntlCalendar::getActualMinimum
