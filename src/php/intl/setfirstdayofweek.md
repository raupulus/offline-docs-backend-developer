---
title: IntlCalendar::setFirstDayOfWeek
description: Define el día de inicio de la semana
source_url: https://www.php.net/manual/es/intlcalendar.setfirstdayofweek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/setfirstdayofweek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 2ca090342
order: 40590
---

IntlCalendar::setFirstDayOfWeek

Define el día de inicio de la semana

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::setFirstDayOfWeek(int $dayOfWeek): true
```php

Estilo procedimental

```php
intlcal_set_first_day_of_week(IntlCalendar $calendar, int $dayOfWeek): true
```

Define el día de inicio de la semana. Esto afecta al comportamiento de los campos que dependen del concepto de inicio y fin de semana, como `IntlCalendar::FIELD_WEEK_OF_YEAR` y `IntlCalendar::FIELD_YEAR_WOY`.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

`dayOfWeek`  
Una constante entre `IntlCalendar::DOW_SUNDAY`, `IntlCalendar::DOW_MONDAY`, …, `IntlCalendar::DOW_SATURDAY`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.2.0   | El tipo de retorno es ahora `true`, anteriormente era `bool`. |

## Ejemplos

Ejemplo con `IntlCalendar::setFirstDayOfWeek`

```php
<?php
ini_set('date.timezone', 'Europe/Lisbon');
ini_set('intl.default_locale', 'es_ES');

$cal = IntlCalendar::createInstance();
$cal->set(2013, 5 /* Junio */, 30); // Un domingo

var_dump($cal->getFirstDayOfWeek()); // 2 (Lunes)

echo IntlDateFormatter::formatObject($cal, <<<EOD
'día local de la semana : 'cc'
semana del mes           : 'W'
semana del año           : 'ww
EOD
), "\n";

$cal->setFirstDayOfWeek(IntlCalendar::DOW_SUNDAY);

echo IntlDateFormatter::formatObject($cal, <<<EOD
'día local de la semana : 'cc'
semana del mes           : 'W'
semana del año           : 'ww
EOD
), "\n";

    
```

El ejemplo anterior mostrará:

    int(2)
    día local de la semana  : 7
    semana del mes           : 4
    semana del año           : 26
    día local de la semana  : 1
    semana del mes           : 5
    semana del año           : 27
