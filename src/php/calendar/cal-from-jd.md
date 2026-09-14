---
title: cal_from_jd
description: Convierte el número de días Julianos a un calendario específico
source_url: https://www.php.net/manual/es/function.cal-from-jd.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/calendar/functions/cal-from-jd.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: calendar
translation_status: ready
translation_reviewed: true
translation_revision: 789af8343
order: 6540
---

cal_from_jd

Convierte el número de días Julianos a un calendario específico

## Descripción

```php
cal_from_jd(int $julian_day, int $calendar): array
```php

`cal_from_jd` convierte el número de días Julianos `julian_day` a una fecha del calendario `calendar`. Los valores posibles para `calendar` son `CAL_GREGORIAN`, `CAL_JULIAN`, `CAL_JEWISH` y `CAL_FRENCH`.

## Parámetros

`julian_day`  
Día Juliano, en forma de un `int`

`calendar`  
Calendario a utilizar

## Valores devueltos

Retorna un array que contiene información sobre el calendario, como el mes, el día, el año, el día de la semana (`dow`), los nombres abreviados y completos de los días de la semana y del mes, y la fecha, en forma de una `string` "mes/día/año". El intervalo del día de la semana va de `0` (Domingo) a `6` (Sábado).

## Ejemplos

Ejemplo con `cal_from_jd`

```
<?php
$today = unixtojd(mktime(0, 0, 0, 8, 16, 2003));
print_r(cal_from_jd($today, CAL_GREGORIAN));
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
       [date] => 8/16/2003
       [month] => 8
       [day] => 16
       [year] => 2003
       [dow] => 6
       [abbrevdayname] => Sat
       [dayname] => Saturday
       [abbrevmonth] => Aug
       [monthname] => August
    )

## Véase también

`cal_to_jd`, `jdtofrench`, `jdtogregorian`, `jdtojewish`, `jdtojulian`, `jdtounix`
