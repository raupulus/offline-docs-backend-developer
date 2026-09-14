---
title: IntlCalendar::getRepeatedWallTimeOption
description: Obtiene el comportamiento para la gestión de las horas murales repetidas
source_url: https://www.php.net/manual/es/intlcalendar.getrepeatedwalltimeoption.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/getrepeatedwalltimeoption.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40440
---

IntlCalendar::getRepeatedWallTimeOption

Obtiene el comportamiento para la gestión de las horas murales repetidas

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::getRepeatedWallTimeOption(): int
```php

Estilo procedimental

```php
intlcal_get_repeated_wall_time_option(IntlCalendar $calendar): int
```

Devuelve la estrategia actual para la gestión de las horas murales repetidas cuando el reloj se atrasa durante las transiciones de fin de hora de verano. El valor por omisión es `IntlCalendar::WALLTIME_LAST`.

Esta función requiere ICU 4.9 o más reciente.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

## Valores devueltos

Una de las constantes `IntlCalendar::WALLTIME_FIRST` o `IntlCalendar::WALLTIME_LAST`.

## Ejemplos

`IntlCalendar::getRepeatedWallTimeOption`

```php
<?php
ini_set('date.timezone', 'Europe/Lisbon');
ini_set('intl.default_locale', 'en_US');
ini_set('intl.error_level', E_WARNING);

//El 27 de Octubre a las 0200, la hora retrocederá de GMT+01 a GMT+00
$cal = new IntlGregorianCalendar(2013, 9 /* October */, 27, 1, 30);

var_dump($cal->getRepeatedWalltimeOption()); // 0 WALLTIME_LAST

$formatter = IntlDateFormatter::create(
    NULL,
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'UTC'
);
var_dump($formatter->format($cal->getTime() / 1000.));

$cal->setRepeatedWalltimeOption(IntlCalendar::WALLTIME_FIRST);
var_dump($cal->getRepeatedWalltimeOption()); // 1 WALLTIME_FIRST
$cal->set(IntlCalendar::FIELD_HOUR_OF_DAY, 1);

var_dump($formatter->format($cal->getTime() / 1000.));

    
```

El ejemplo anterior mostrará:

    int(0)
    string(42) "Sunday, October 27, 2013 at 1:30:00 AM GMT"
    int(1)
    string(43) "Sunday, October 27, 2013 at 12:30:00 AM GMT"

## Véase también

IntlCalendar::getSkippedWallTimeOption, IntlCalendar::setSkippedWallTimeOption, IntlCalendar::setRepeatedWallTimeOption
