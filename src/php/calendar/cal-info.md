---
title: cal_info
description: Devuelve información sobre un calendario en particular
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/calendar/functions/cal-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: calendar
translation_status: ready
translation_reviewed: false
translation_revision: e41aab5ec
order: 6550
---

cal_info

Devuelve información sobre un calendario en particular

## Descripción

```php
cal_info([int $calendar]): array
```php

`cal_info` devuelve información sobre el calendario `calendar` especificado.

La información del calendario es devuelta como una matriz que contiene los elementos `calname`, `calsymbol`, `month`, `abbrevmonth` y `maxdaysinmonth`. Los nombre de los diferentes calendarios que se pueden usar en `calendar` son los siguientes:

- 0 o `CAL_GREGORIAN` - Calendario Gregoriano

- 1 o `CAL_JULIAN` - Calendario Juliano

- 2 o `CAL_JEWISH` - Calendario Judío

- 3 o `CAL_FRENCH` - Calendario Republicano Francés

Si no se especifica `calendar` la información de todos los calendarios soportados es devuelta como un matriz.

## Parámetros

`calendar`  
El calendario del que se va a devolver la información. Si no se especifica ningún calendario se devolverá la información sobre todos los calendarios.

## Valores devueltos

## Ejemplos

Ejemplo de `cal_info`

```
<?php
$info = cal_info(0);
print_r($info);
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [months] => Array
            (
                [1] => January
                [2] => February
                [3] => March
                [4] => April
                [5] => May
                [6] => June
                [7] => July
                [8] => August
                [9] => September
                [10] => October
                [11] => November
                [12] => December
            )

        [abbrevmonths] => Array
            (
                [1] => Jan
                [2] => Feb
                [3] => Mar
                [4] => Apr
                [5] => May
                [6] => Jun
                [7] => Jul
                [8] => Aug
                [9] => Sep
                [10] => Oct
                [11] => Nov
                [12] => Dec
            )

        [maxdaysinmonth] => 31
        [calname] => Gregorian
        [calsymbol] => CAL_GREGORIAN
    )
