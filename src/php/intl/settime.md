---
title: IntlCalendar::setTime
description: Define el tiempo del calendario en milisegundos desde la época
source_url: https://www.php.net/manual/es/intlcalendar.settime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/settime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 40640
---

IntlCalendar::setTime

Define el tiempo del calendario en milisegundos desde la época

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::setTime(float $timestamp): bool
```php

Estilo procedimental

```php
intlcal_set_time(IntlCalendar $calendar, float $timestamp): bool
```

Define el instante representado por este objeto. El instante se representa mediante un `float` cuyo valor es un número entero de milisegundos desde la época Unix (1 de enero de 1970 00:00:00.000 UTC), ignorando el último segundo. Todos los valores de los campos serán recalculados en consecuencia.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

`timestamp`  
Un instante, representado por el número de milisegundos entre el instante y la época Unix, ignorando el último segundo.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` si ocurre un error.

## Ejemplos

Ejemplo con `IntlCalendar::setTime`

```php
<?php
ini_set('date.timezone', 'Europe/Lisbon');
ini_set('intl.default_locale', 'fr_FR');

$cal = new IntlGregorianCalendar(2013, 5 /* May */, 1, 12, 0, 0);

echo IntlDateFormatter::formatObject($cal, IntlDateFormatter::FULL), "\n";

/* En Europe/Lisbon, el 2013-10-27 a las 0200, el reloj pierde una hora
   y la zona horaria pasa de UTC+01 a UTC+00 */

$cal->setTime(strtotime('2013-10-27 00:30:00 UTC') * 1000.);

echo IntlDateFormatter::formatObject($cal, IntlDateFormatter::FULL), "\n";

$cal->setTime(strtotime('2013-10-27 01:30:00 UTC') * 1000.);

echo IntlDateFormatter::formatObject($cal, IntlDateFormatter::FULL), "\n";

    
```

El ejemplo anterior mostrará:

    sábado 1 de junio de 2013 12:00:00 hora de verano de Europa Occidental
    domingo 27 de octubre de 2013 01:30:00 hora de verano de Europa Occidental
    domingo 27 de octubre de 2013 01:30:00 hora estándar de Europa Occidental
