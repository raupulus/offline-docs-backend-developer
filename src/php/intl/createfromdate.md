---
title: IntlGregorianCalendar::createFromDate
description: Crear una nueva instancia de IntlGregorianCalendar a partir de una fecha
source_url: https://www.php.net/manual/es/intlgregoriancalendar.createfromdate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlgregoriancalendar/createfromdate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: d715365c0
order: 41350
---

IntlGregorianCalendar::createFromDate

Crear una nueva instancia de IntlGregorianCalendar a partir de una fecha

## Descripción

```php
public static IntlGregorianCalendar::createFromDate(int $year, int $month, int $dayOfMonth): static
```php

Crear una nueva instancia de `IntlGregorianCalendar` a partir de una fecha.

## Parámetros

`year`  
El nuevo valor para `IntlGregorianCalendar::FIELD_YEAR`.

`month`  
El nuevo valor para `IntlGregorianCalendar::FIELD_MONTH`. La secuencia de los meses comienza en cero, es decir, que enero está representado por 0, febrero por 1, ..., diciembre es 11 y Undécembre (si el calendario lo permite) es 12.

`dayOfMonth`  
El nuevo valor para `IntlGregorianCalendar::FIELD_DAY_OF_MONTH`.

## Valores devueltos

Devuelve una nueva instancia de `IntlGregorianCalendar`.

## Ejemplos

Ejemplo de IntlGregorianCalendar::createFromDate

```
<?php

$intlCalendar = IntlGregorianCalendar::createFromDate(2023, 11, 23);
var_dump($intlCalendar);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    object(IntlGregorianCalendar)#1 (5) {
      ["valid"]=>
      bool(true)
      ["type"]=>
      string(9) "gregorian"
      ["timeZone"]=>
      array(4) {
        ["valid"]=>
        bool(true)
        ["id"]=>
        string(16) "Europe/Amsterdam"
        ["rawOffset"]=>
        int(3600000)
        ["currentOffset"]=>
        int(3600000)
      }
      ["locale"]=>
      string(11) "en_US_POSIX"
      ["fields"]=>
      array(23) {
        ["era"]=>
        int(1)
        ["year"]=>
        int(2023)
        ["month"]=>
        int(11)
        ["week of year"]=>
        int(51)
        ["week of month"]=>
        int(4)
        ["day of year"]=>
        int(357)
        ["day of month"]=>
        int(23)
        ["day of week"]=>
        int(7)
        ["day of week in month"]=>
        int(4)
        ["AM/PM"]=>
        int(0)
        ["hour"]=>
        int(0)
        ["hour of day"]=>
        int(0)
        ["minute"]=>
        int(0)
        ["second"]=>
        int(0)
        ["millisecond"]=>
        int(0)
        ["zone offset"]=>
        int(3600000)
        ["DST offset"]=>
        int(0)
        ["year for week of year"]=>
        int(2023)
        ["localized day of week"]=>
        int(7)
        ["extended year"]=>
        int(2023)
        ["julian day"]=>
        int(2460302)
        ["milliseconds in day"]=>
        int(0)
        ["is leap month"]=>
        int(0)
      }
    }

## Véase también

IntlGregorianCalendar::createFromDateTime
