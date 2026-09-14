---
title: jdmonthname
description: Devuelve el nombre del mes
source_url: https://www.php.net/manual/es/function.jdmonthname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/calendar/functions/jdmonthname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: calendar
translation_status: ready
translation_reviewed: true
translation_revision: c6fb604f3
order: 6620
---

jdmonthname

Devuelve el nombre del mes

## Descripción

```php
jdmonthname(int $julian_day, int $mode): string
```php

Devuelve una cadena que contiene el nombre del mes. `mode` indica de qué calendario depende este mes, y qué tipo de nombre debe ser devuelto.

| Modo | Significado | Valores |
|----|----|----|
| `CAL_MONTH_GREGORIAN_SHORT` | Gregoriano - abreviado | Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec |
| `CAL_MONTH_GREGORIAN_LONG` | Gregoriano | January, February, March, April, May, June, July, August, September, October, November, December |
| `CAL_MONTH_JULIAN_SHORT` | Juliano - abreviado | Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec |
| `CAL_MONTH_JULIAN_LONG` | Juliano | January, February, March, April, May, June, July, August, September, October, November, December |
| `CAL_MONTH_JEWISH` | Judío | Tishri, Heshvan, Kislev, Tevet, Shevat, Adar, Adar I, Adar II, Nisan, Iyyar, Sivan, Tammuz, Av, Elul |
| `CAL_MONTH_FRENCH` | Francés republicano | Vendemiaire, Brumaire, Frimaire, Nivose, Pluviose, Ventose, Germinal, Floreal, Prairial, Messidor, Thermidor, Fructidor, Extra |

Modos de calendario

## Parámetros

`julian_day`  
El día juliano a analizar

`mode`  
El modo de calendario (ver tabla anterior).

## Valores devueltos

El nombre del mes para el día juliano y el `mode`.
