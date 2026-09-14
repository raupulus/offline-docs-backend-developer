---
title: DatePeriod::getEndDate
description: Devuelve la fecha de fin
source_url: https://www.php.net/manual/es/dateperiod.getenddate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/dateperiod/getenddate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 10350
---

DatePeriod::getEndDate

Devuelve la fecha de fin

## Descripción

Estilo orientado a objetos

```php
public DatePeriod::getEndDate(): DateTimeInterface
```php

Devuelve la fecha de fin del período.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `null` si la `DatePeriod` no tiene fecha de fin. Por ejemplo, cuando se inicializa con el argumento `recurrences`, o con el argumento `isostr` sin fecha de fin.

Retorna un `object` `DateTimeImmutable` cuando la `DatePeriod` se inicializa con un `object` `DateTimeImmutable` como argumento `end`.

Devuelve un `object` `DateTime` clonado que representa la fecha de fin en caso contrario.

## Ejemplos

Ejemplos con DatePeriod::getEndDate

```
<?php
$period = new DatePeriod(
    new DateTime('2016-05-16T00:00:00Z'),
    new DateInterval('P1D'),
    new DateTime('2016-05-20T00:00:00Z')
);
$start = $period->getEndDate();
echo $start->format(DateTime::ISO8601);

   
```php

Los ejemplos anteriores mostrarán:

    2016-05-20T00:00:00+0000

DatePeriod::getEndDate sin fecha de fin

```
<?php
$period = new DatePeriod(
    new DateTime('2016-05-16T00:00:00Z'),
    new DateInterval('P1D'),
    7
);
var_dump($period->getEndDate());

   
```php

El ejemplo anterior mostrará:

    NULL

## Véase también

DatePeriod::getStartDate

DatePeriod::getDateInterval
