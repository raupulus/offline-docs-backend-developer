---
title: jdtogregorian
description: Convierte el número de días del calendario Juliano en fecha Gregoriana
source_url: https://www.php.net/manual/es/function.jdtogregorian.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/calendar/functions/jdtogregorian.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: calendar
translation_status: ready
translation_reviewed: true
translation_revision: 789af8343
order: 6640
---

jdtogregorian

Convierte el número de días del calendario Juliano en fecha Gregoriana

## Descripción

```php
jdtogregorian(int $julian_day): string
```php

Convierte el número de días del calendario Juliano en una cadena que contiene una fecha del calendario Gregoriano, en formato "mes/día/año".

## Parámetros

`julian_day`  
El número del día Juliano, en forma de `int`

## Valores devueltos

La fecha Gregoriana, en forma de `string` "mes/día/año".

## Véase también

`gregoriantojd`, `cal_from_jd`
