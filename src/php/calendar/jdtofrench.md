---
title: jdtofrench
description: Convierte el número de días del calendario juliano en fecha del calendario
  francés republicano
source_url: https://www.php.net/manual/es/function.jdtofrench.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/calendar/functions/jdtofrench.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: calendar
translation_status: ready
translation_reviewed: true
translation_revision: 1ae151672
order: 6630
---

jdtofrench

Convierte el número de días del calendario juliano en fecha del calendario francés republicano

## Descripción

```php
jdtofrench(int $julian_day): string
```php

Convierte el número de días del calendario juliano en fecha del calendario francés republicano.

## Parámetros

`julian_day`  
El número del día juliano, en forma de `int`

## Valores devueltos

La fecha francesa republicana, en forma de `string` "mes/día/año".

## Véase también

`frenchtojd`, `cal_from_jd`
