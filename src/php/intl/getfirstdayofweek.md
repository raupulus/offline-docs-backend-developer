---
title: IntlCalendar::getFirstDayOfWeek
description: Devuelve el primer día de la semana para la configuración local del calendario
source_url: https://www.php.net/manual/es/intlcalendar.getfirstdayofweek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/getfirstdayofweek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40350
---

IntlCalendar::getFirstDayOfWeek

Devuelve el primer día de la semana para la configuración local del calendario

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::getFirstDayOfWeek(): int
```php

Estilo procedimental

```php
intlcal_get_first_day_of_week(IntlCalendar $calendar): int
```

Devuelve el día de la semana considerado como primer día de la semana, ya sea el valor por omisión para esta configuración local, o el valor definido con `IntlCalendar::setFirstDayOfWeek`.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

## Valores devueltos

Una de las constantes `IntlCalendar::DOW_SUNDAY`, `IntlCalendar::DOW_MONDAY`, …, `IntlCalendar::DOW_SATURDAY` o `false` si ocurre un error.

## Ejemplos

`IntlCalendar::getFirstDayOfWeek`

```php
<?php
ini_set('date.timezone', 'UTC');

$cal1 = IntlCalendar::createInstance(NULL, 'es_ES');
var_dump($cal1->getFirstDayOfWeek()); // Lunes
$cal1->set(2013, 1 /* February */, 3); // un domingo
var_dump($cal1->get(IntlCalendar::FIELD_WEEK_OF_YEAR)); // 5

$cal2 = IntlCalendar::createInstance(NULL, 'en_US');
var_dump($cal2->getFirstDayOfWeek()); // Domingo
$cal2->set(2013, 1 /* February */, 3); // un domingo
var_dump($cal2->get(IntlCalendar::FIELD_WEEK_OF_YEAR)); // 6

    
```

El ejemplo anterior mostrará:

    int(2)
    int(5)
    int(1)
    int(6)

## Véase también

IntlCalendar::setFirstDayOfWeek
