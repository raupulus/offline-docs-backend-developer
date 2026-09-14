---
title: DatePeriod::getDateInterval
description: Devuelve el intervalo
source_url: https://www.php.net/manual/es/dateperiod.getdateinterval.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/dateperiod/getdateinterval.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 10340
---

DatePeriod::getDateInterval

Devuelve el intervalo

## Descripción

Estilo orientado a objetos

```php
public DatePeriod::getDateInterval(): DateInterval
```php

Devuelve un `DateInterval` `object` que representa el intervalo utilizado para el período.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `DateInterval` `object`

## Ejemplos

Ejemplo con DatePeriod::getDateInterval

```
<?php
$period = DatePeriod::createFromIso8601String('R7/2016-05-16T00:00:00Z/P1D');
$interval = $period->getDateInterval();
echo $interval->format('%d day');

   
```php

El ejemplo anterior mostrará:

    1 day

## Véase también

DatePeriod::getStartDate

DatePeriod::getEndDate
