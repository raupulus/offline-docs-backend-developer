---
title: jewishtojd
description: Convierte una fecha del calendario judío en número de días del calendario
  juliano
source_url: https://www.php.net/manual/es/function.jewishtojd.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/calendar/functions/jewishtojd.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: calendar
translation_status: ready
translation_reviewed: true
translation_revision: e80cd5ffc
order: 6680
---

jewishtojd

Convierte una fecha del calendario judío en número de días del calendario juliano

## Descripción

```php
jewishtojd(int $month, int $day, int $year): int
```php

Aunque es posible manipular fechas a partir del año 1 (3761 antes de J.C.), un uso de este tipo tiene poco sentido. El calendario judío ha sido utilizado durante varios siglos, pero en los primeros tiempos no existía una fórmula para determinar el inicio del mes. Un nuevo mes comenzaba cuando una nueva luna era observada.

## Parámetros

`month`  
El mes, en forma de número entre `1` y `13`, donde `1` significa `Tishri`, `13` significa `Eloul`, y `6` *y* `7` significa `Adar` en los años regulares, pero `Adar I` y `Adar II`, respectivamente, en los años bisiestos.

`day`  
El día, en forma de número entre `1` y `30`. Si el mes tiene solo 29 días, se asume el primer día del mes siguiente.

`year`  
El año, en forma de número entre 1 y 9999

## Valores devueltos

El día juliano para la fecha judía dada, en forma de `int`.

## Véase también

`jdtojewish`, `cal_to_jd`
