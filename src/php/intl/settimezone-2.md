---
title: IntlCalendar::setTimeZone
description: Define el huso horario utilizado por este calendario
source_url: https://www.php.net/manual/es/intlcalendar.settimezone.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/settimezone.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 40650
---

IntlCalendar::setTimeZone

Define el huso horario utilizado por este calendario

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::setTimeZone(IntlTimeZone $timezone): bool
```php

Estilo procedimental

```php
intlcal_set_time_zone(IntlCalendar $calendar, IntlTimeZone $timezone): bool
```

Define un nuevo huso horario para este calendario. El momento representado por este objeto es preservado a expensas de los valores de los campos.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

`timezone`  
El nuevo huso horario a utilizar por este calendario. Puede ser especificado de la siguiente manera:

## Valores devueltos

Retorna `true` en caso de éxito, `false` si ocurre un error.

## Ejemplos

Ejemplo con `IntlCalendar::setTimeZone`

```php
<?php
ini_set('date.timezone', 'Europe/Lisbon');
ini_set('intl.default_locale', 'es_ES');

$cal = new IntlGregorianCalendar(2013, 5 /* May */, 1, 12, 0, 0);

echo IntlDateFormatter::formatObject($cal, IntlDateFormatter::FULL), "\n";
echo "(instant {$cal->getTime()})\n";

$cal->setTimeZone(IntlTimeZone::getGMT());
echo IntlDateFormatter::formatObject($cal, IntlDateFormatter::FULL), "\n";
echo "(instant {$cal->getTime()})\n";

$cal->setTimeZone('GMT+03:33');
echo IntlDateFormatter::formatObject($cal, IntlDateFormatter::FULL), "\n";
echo "(instant {$cal->getTime()})\n";

    
```

El ejemplo anterior mostrará:

    sábado, 1 de junio de 2013 12:00:00 Hora de verano de Europa occidental
    (instant 1370084400000)
    sábado, 1 de junio de 2013 11:00:00 GMT
    (instant 1370084400000)
    sábado, 1 de junio de 2013 14:33:00 GMT+03:33
    (instant 1370084400000)
