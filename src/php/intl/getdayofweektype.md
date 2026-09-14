---
title: IntlCalendar::getDayOfWeekType
description: Indica si un día es un día de la semana, un fin de semana o un día de
  transición entre ambos
source_url: https://www.php.net/manual/es/intlcalendar.getdayofweektype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/getdayofweektype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40320
---

IntlCalendar::getDayOfWeekType

Indica si un día es un día de la semana, un fin de semana o un día de transición entre ambos

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::getDayOfWeekType(int $dayOfWeek): int
```php

Estilo procedimental

```php
intlcal_get_day_of_week_type(IntlCalendar $calendar, int $dayOfWeek): int
```

Devuelve si el día pasado es un día de semana (`IntlCalendar::DOW_TYPE_WEEKDAY`), un día de fin de semana (`IntlCalendar::DOW_TYPE_WEEKEND`), un día de transición hacia el fin de semana (`IntlCalendar::DOW_TYPE_WEEKEND_OFFSET`) o un día de transición fuera del fin de semana (`IntlCalendar::DOW_TYPE_WEEKEND_CEASE`).

Si el retorno es `IntlCalendar::DOW_TYPE_WEEKEND_OFFSET` o `IntlCalendar::DOW_TYPE_WEEKEND_CEASE`, entonces `IntlCalendar::getWeekendTransition` puede ser llamada para obtener el tiempo de la transición.

Esta función requiere ICU 4.4 o más reciente.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

`dayOfWeek`  
Una de las constantes `IntlCalendar::DOW_SUNDAY`, `IntlCalendar::DOW_MONDAY`, …, `IntlCalendar::DOW_SATURDAY`.

## Valores devueltos

Una de las constantes `IntlCalendar::DOW_TYPE_WEEKDAY`, `IntlCalendar::DOW_TYPE_WEEKEND`, `IntlCalendar::DOW_TYPE_WEEKEND_OFFSET` o `IntlCalendar::DOW_TYPE_WEEKEND_CEASE` o `false` si ocurre un error.

## Ejemplos

`IntlCalendar::getDayOfWeekType`

```php
<?php
foreach (array('en_US', 'ar_SA') as $locale) {
    echo "Locale: ", Locale::getDisplayName($locale, "en_US"), "\n";

    $cal = IntlCalendar::createInstance('UTC', $locale);

    for ($i = IntlCalendar::DOW_SUNDAY; $i <= IntlCalendar::DOW_SATURDAY; $i++) {
        $type = $cal->getDayOfWeekType($i);
        $transition = ($type !== IntlCalendar::DOW_TYPE_WEEKDAY)
            ? $cal->getWeekendTransition($i)
            : '';
        echo $i, " ", $type, " ", $transition, "\n";
    }
    echo "\n";
}
?>

    
```

El ejemplo anterior mostrará:

    Locale: English (United States)
    1 1 86400000
    2 0
    3 0
    4 0
    5 0
    6 0
    7 1 0

    Locale: Arabic (Saudi Arabia)
    1 0
    2 0
    3 0
    4 0
    5 0
    6 1 0
    7 1 86400000
