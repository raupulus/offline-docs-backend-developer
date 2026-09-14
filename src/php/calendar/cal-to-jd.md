---
title: cal_to_jd
description: Convertir un calendario soportado a la Fecha Juliana
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/calendar/functions/cal-to-jd.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: calendar
translation_status: ready
translation_revision: 96c9d88ba
order: 6560
---

cal_to_jd

Convertir un calendario soportado a la Fecha Juliana

## Descripción

```php
cal_to_jd(int $calendar, int $month, int $day, int $year): int
```php

`cal_to_jd` calcula la Fecha Juliana para una fecha en el calendario `calendar` especificado. Los calendarios `calendar` soportados son `CAL_GREGORIAN`, `CAL_JULIAN`, `CAL_JEWISH` y `CAL_FRENCH`.

## Parámetros

`calendar`  
El calendario desde el que se va a hacer la conversión, `CAL_GREGORIAN`, `CAL_JULIAN`, `CAL_JEWISH` o `CAL_FRENCH`.

`month`  
El mes como número, el rango válido depende de `calendar`

`day`  
El día como número, el rango válido depende de `calendar`

`year`  
El año como número, el rango válido depende de `calendar`

## Valores devueltos

Un número de día de la Fecha Juliana.

## Véase también

`cal_from_jd`, `frenchtojd`, `gregoriantojd`, `jewishtojd`, `juliantojd`, `unixtojd`
