---
title: IntlCalendar::getMinimalDaysInFirstWeek
description: Obtiene el número mínimo de días que la primera semana de un año o mes
  puede tener
source_url: https://www.php.net/manual/es/intlcalendar.getminimaldaysinfirstweek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/getminimaldaysinfirstweek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40410
---

IntlCalendar::getMinimalDaysInFirstWeek

Obtiene el número mínimo de días que la primera semana de un año o mes puede tener

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::getMinimalDaysInFirstWeek(): int
```php

Estilo procedimental

```php
intlcal_get_minimal_days_in_first_week(IntlCalendar $calendar): int
```

Devuelve el número más pequeño de días que la primera semana de un año o mes debe tener en el nuevo año o mes. Por ejemplo, en el calendario gregoriano, si este valor es 1, entonces la primera semana del año incluirá necesariamente el 1 de enero, mientras que si este valor es 7, entonces la semana con el 1 de enero será la primera semana del año solo si el día de la semana para el 1 de enero coincide con el día de la semana devuelto por `IntlCalendar::getFirstDayOfWeek`; de lo contrario, será la última semana del año anterior.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

## Valores devueltos

Un `int` que representa un número de día o `false` si ocurre un error.

## Ejemplos

`IntlCalendar::getMinimalDaysInFirstWeek`

```php
<?php
ini_set('date.timezone', 'UTC');
ini_set('intl.default_locale', 'en_US');

$cal = new IntlGregorianCalendar(2013, 0 /* January */, 2);
var_dump(IntlDateFormatter::formatObject($cal, 'cccc')); // Miércoles

var_dump($cal->getMinimalDaysInFirstWeek(), // 1
$cal->getFirstDayofWeek()); // 1 (Domingo)

// Semana 1 de 2013
var_dump(IntlDateFormatter::formatObject($cal, "'Week 'w' of 'Y"));

$cal->setMinimalDaysInFirstWeek(4);
// Siempre semana 1 de 2013 (La 1ª semana tiene 5 días en el nuevo año)
var_dump(IntlDateFormatter::formatObject($cal, "'Week 'w' of 'Y"));

$cal->setMinimalDaysInFirstWeek(6);
// Semana 53 de 2012
var_dump(IntlDateFormatter::formatObject($cal, "'Week 'w' of 'Y"));

    
```

El ejemplo anterior mostrará:

    string(9) "Wednesday"
    int(1)
    int(1)
    string(14) "Week 1 of 2013"
    string(14) "Week 1 of 2013"
    string(15) "Week 53 of 2012"
