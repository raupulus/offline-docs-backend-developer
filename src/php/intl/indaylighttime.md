---
title: IntlCalendar::inDaylightTime
description: Indica si el objeto está en horario de verano
source_url: https://www.php.net/manual/es/intlcalendar.indaylighttime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/indaylighttime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40500
---

IntlCalendar::inDaylightTime

Indica si el objeto está en horario de verano

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::inDaylightTime(): bool
```php

Estilo procedimental

```php
intlcal_in_daylight_time(IntlCalendar $calendar): bool
```

Si, para el instante representado por este objeto y para la zona horaria de este objeto, el horario de verano está en vigor.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

## Valores devueltos

Devuelve `true` si la fecha está en horario de verano, de lo contrario `false`.

En caso de fallo, también se devuelve `false`. Para detectar condiciones de error, utilice `intl_get_error_code`, o configure Intl para lanzar [excepciones](#ini.intl.use-exceptions).

## Ejemplos

`IntlCalendar::inDaylightTime`

```php
<?php
ini_set('date.timezone', 'Europe/Lisbon');
ini_set('intl.default_locale', 'pt_PT');

$cal = new IntlGregorianCalendar(2013, 6 /* July */, 1, 4, 56, 31);
var_dump($cal->inDaylightTime()); // true
$cal->set(IntlCalendar::FIELD_MONTH, 11 /* December */);
var_dump($cal->inDaylightTime()); // false

//Fin del horario de verano el 2013-10-27 a 0200 (retraso de una hora)
$cal = new IntlGregorianCalendar(2013, 9 /* October */, 27, 1, 30, 0);

var_dump($cal->inDaylightTime()); // false (default WALLTIME_LAST)

$cal->setRepeatedWallTimeOption(IntlCalendar::WALLTIME_FIRST);
$cal->set(IntlCalendar::FIELD_HOUR_OF_DAY, 1); // fuerza el recálculo de la hora
var_dump($cal->inDaylightTime()); // true

    
```
