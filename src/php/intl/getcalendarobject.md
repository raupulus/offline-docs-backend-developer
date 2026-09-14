---
title: IntlDateFormatter::getCalendarObject
description: Obtiene una copia del objeto formateador de calendario
source_url: https://www.php.net/manual/es/intldateformatter.getcalendarobject.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/dateformatter/getcalendarobject.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 39650
---

IntlDateFormatter::getCalendarObject

datefmt_get_calendar_object

Obtiene una copia del objeto formateador de calendario

## Descripción

Estilo orientado a objetos

```php
public IntlDateFormatter::getCalendarObject(): IntlCalendar
```php

Estilo procedimental

```php
datefmt_get_calendar_object(IntlDateFormatter $formatter): IntlCalendar
```

Obtiene una copia del objeto calendario utilizado internamente por este formateador. Este calendario tendrá un tipo (como gregoriano, japonés, budista, islámico, etc.) y un desplazamiento horario que correspondan al tipo y al desplazamiento horario utilizados por el formateador. La fecha/hora del objeto no está especificada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una copia del objeto calendario interno utilizado por este formateador, o `null` si ninguno ha sido definido, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `IntlDateFormatter::getCalendarObject`

```php
<?php
$formatter = IntlDateFormatter::create(
    "fr_FR@calendar=islamic",
    NULL,
    NULL,
    "GMT-01:00",
    IntlDateFormatter::TRADITIONAL
);

$cal = $formatter->getCalendarObject();

var_dump(
    $cal->getType(),
    $cal->getTimeZone(),
    $cal->getLocale(Locale::VALID_LOCALE)
);
?>

    
```

El ejemplo anterior mostrará:

    string(7) "islamic"
    object(IntlTimeZone)#3 (4) {
      ["valid"]=>
      bool(true)
      ["id"]=>
      string(9) "GMT-01:00"
      ["rawOffset"]=>
      int(-3600000)
      ["currentOffset"]=>
      int(-3600000)
    }
    string(5) "fr_FR"

## Véase también

`IntlDateFormatter::getCalendar`, `IntlDateFormatter::setCalendar`, `IntlCalendar`
