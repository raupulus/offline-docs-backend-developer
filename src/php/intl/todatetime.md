---
title: IntlCalendar::toDateTime
description: Convierte un objeto IntlCalendar en un objeto DateTime
source_url: https://www.php.net/manual/es/intlcalendar.todatetime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/todatetime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 40660
---

IntlCalendar::toDateTime

Convierte un objeto IntlCalendar en un objeto DateTime

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::toDateTime(): DateTime
```php

Estilo procedimental

```php
intlcal_to_date_time(IntlCalendar $calendar): DateTime
```

Crea un objeto `DateTime` que representa el mismo instante (con una precisión de segundo) y con un huso horario similar al objeto inicial (la única diferencia es que el huso horario del objeto `DateTime` será comprendido por PHP, mientras que el huso horario del objeto `IntlCalendar` será comprendido por ICU).

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

## Valores devueltos

Un objeto `DateTime` con el mismo huso horario que el objeto original (utilizando la base de datos de PHP en lugar de la de ICU) y que representa el mismo momento, salvo por la precisión (precisión de segundo en lugar de milisegundo). Devuelve `false` en caso de error.

## Ejemplos

Ejemplo con `IntlCalendar::toDateTime`

```php
<?php
ini_set('date.timezone', 'UTC');
ini_set('intl.default_locale', 'pt_PT');

$cal = IntlCalendar::createInstance('Europe/Lisbon'); //tiempo actual

$dt = $cal->toDateTime();
print_r($dt);

    
```

El ejemplo anterior mostrará:

    DateTime Object
    (
        [date] => 2013-07-02 00:29:13
        [timezone_type] => 3
        [timezone] => Europe/Lisbon
    )

## Véase también

IntlCalendar::fromDateTime, IntlCalendar::getTime, IntlCalendar::createInstance, DateTime::\_\_construct
