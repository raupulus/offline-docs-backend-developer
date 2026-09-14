---
title: DatePeriod::getRecurrences
description: Recupera el número de recurrencias
source_url: https://www.php.net/manual/es/dateperiod.getrecurrences.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/dateperiod/getrecurrences.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 10360
---

DatePeriod::getRecurrences

Recupera el número de recurrencias

## Descripción

Estilo orientado a objetos

```php
public DatePeriod::getRecurrences(): int
```php

Recupera el número de recurrencias.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El número de recurrencias se define pasando explícitamente las `$recurrences` al constructor de la clase `DatePeriod`, de lo contrario se define como `null`.

## Ejemplos

Valores diferentes para DatePeriod::getRecurrences

```
<?php
$start = new DateTime('2018-12-31 00:00:00');
$end   = new DateTime('2021-12-31 00:00:00');
$interval = new DateInterval('P1M');
$recurrences = 5;
// recurrencias definidas explícitamente a través del constructor
$period = new DatePeriod($start, $interval, $recurrences, DatePeriod::EXCLUDE_START_DATE);
echo $period->getRecurrences(), "\n";

$period = new DatePeriod($start, $interval, $recurrences);
echo $period->getRecurrences(), "\n";

$period = new DatePeriod($start, $interval, $recurrences, DatePeriod::INCLUDE_END_DATE);
echo $period->getRecurrences(), "\n\n";

// recurrencias no definidas en el constructor
$period = new DatePeriod($start, $interval, $end);
var_dump($period->getRecurrences());

$period = new DatePeriod($start, $interval, $end, DatePeriod::EXCLUDE_START_DATE);
var_dump($period->getRecurrences());

   
```php

El ejemplo anterior mostrará:

```
5
5
5

NULL
NULL

    
```php

## Véase también

DatePeriod::\$recurrences
