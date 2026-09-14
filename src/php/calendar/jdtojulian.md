---
title: jdtojulian
description: Convierte el número de días del calendario Juliano en fecha del calendario
  Juliano
source_url: https://www.php.net/manual/es/function.jdtojulian.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/calendar/functions/jdtojulian.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: calendar
translation_status: ready
translation_reviewed: true
translation_revision: 789af8343
order: 6660
---

jdtojulian

Convierte el número de días del calendario Juliano en fecha del calendario Juliano

## Descripción

```php
jdtojulian(int $julian_day): string
```php

Convierte el número de días del calendario Juliano en una cadena que contiene la fecha del calendario Juliano, en formato "mes/día/año".

## Parámetros

`julian_day`  
El número de días Julianos, en forma de `int`

## Valores devueltos

La fecha Juliana, en forma de `string` "mes/día/año".

## Véase también

`juliantojd`, `cal_from_jd`
