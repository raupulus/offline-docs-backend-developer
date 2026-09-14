---
title: DatePeriod::getStartDate
description: Obtiene la fecha de inicio
source_url: https://www.php.net/manual/es/dateperiod.getstartdate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/dateperiod/getstartdate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 10370
---

DatePeriod::getStartDate

Obtiene la fecha de inicio

## Descripción

Estilo orientado a objetos

```php
public DatePeriod::getStartDate(): DateTimeInterface
```php

Obtiene la fecha de inicio de un período.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `object` `DateTimeImmutable` cuando la `DatePeriod` se inicializa con un `object` `DateTimeImmutable` como argumento `start`.

Devuelve un `object` `DateTime` en los demás casos.

## Ejemplos

Ejemplo DatePeriod::getStartDate

```
<?php
$period = DatePeriod::createFromIso8601String('R7/2016-05-16T00:00:00Z/P1D');
$start = $period->getStartDate();
echo $start->format(DateTime::ISO8601);

   
```php

El ejemplo anterior mostrará:

    2016-05-16T00:00:00+0000

## Véase también

DatePeriod::getEndDate

DatePeriod::getDateInterval
