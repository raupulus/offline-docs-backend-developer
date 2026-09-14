---
title: IntlCalendar::getSkippedWallTimeOption
description: Obtiene el comportamiento para la gestión de las horas murales omitidas
source_url: https://www.php.net/manual/es/intlcalendar.getskippedwalltimeoption.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/getskippedwalltimeoption.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40450
---

IntlCalendar::getSkippedWallTimeOption

Obtiene el comportamiento para la gestión de las horas murales omitidas

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::getSkippedWallTimeOption(): int
```php

Estilo procedimental

```php
intlcal_get_skipped_wall_time_option(IntlCalendar $calendar): int
```

Devuelve la estrategia actual para la gestión de las horas murales omitidas cuando el reloj se adelanta durante las transiciones de inicio de hora de verano. El valor por omisión es `IntlCalendar::WALLTIME_LAST`.

El calendario debe ser [tolerante](#intlcalendar.setlenient) para que esta opción tenga efecto, de lo contrario intentar definir una hora inexistente provocará una error.

Esta función requiere ICU 4.9 o más reciente.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

## Valores devueltos

Una de las constantes `IntlCalendar::WALLTIME_FIRST`, `IntlCalendar::WALLTIME_LAST` o `IntlCalendar::WALLTIME_NEXT_VALID`.

## Ejemplos

`IntlCalendar::getSkippedWallTimeOption`

```php
<?php
ini_set('date.timezone', 'Europe/Lisbon');
ini_set('intl.default_locale', 'en_US');
ini_set('intl.error_level', E_WARNING);

//El 31 de Marzo a las 0100, el reloj avanzará una hora de GMT+00 a GMT+01
$cal = new IntlGregorianCalendar(2013, 2 /* March */, 31, 1, 30);

var_dump(
    $cal->isLenient(),               // true
    $cal->getSkippedWalltimeOption() // 0 WALLTIME_LAST
);

$formatter = IntlDateFormatter::create(
    NULL,
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'UTC'
);
var_dump($formatter->format($cal->getTime() / 1000));

$cal->setSkippedWallTimeOption(IntlCalendar::WALLTIME_FIRST);
var_dump($cal->getSkippedWalltimeOption()); // 1 WALLTIME_FIRST
$cal->set(IntlCalendar::FIELD_HOUR_OF_DAY, 1);

var_dump($formatter->format($cal->getTime() / 1000));

$cal->setSkippedWallTimeOption(IntlCalendar::WALLTIME_NEXT_VALID);
var_dump($cal->getSkippedWalltimeOption()); // 2 WALLTIME_NEXT_VALID
$cal->set(IntlCalendar::FIELD_HOUR_OF_DAY, 1);

var_dump($formatter->format($cal->getTime() / 1000));

    
```

El ejemplo anterior mostrará:

    bool(true)
    int(0)
    string(40) "Sunday, March 31, 2013 at 1:30:00 AM GMT"
    int(1)
    string(41) "Sunday, March 31, 2013 at 12:30:00 AM GMT"
    int(2)
    string(40) "Sunday, March 31, 2013 at 1:00:00 AM GMT"

## Véase también

IntlCalendar::getRepeatedWallTimeOption, IntlCalendar::setSkippedWallTimeOption, IntlCalendar::setRepeatedWallTimeOption
