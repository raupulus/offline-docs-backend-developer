---
title: DateTimeImmutable::setISODate
description: Establece la fecha ISO
source_url: https://www.php.net/manual/es/datetimeimmutable.setisodate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimeimmutable/setisodate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 726154e3c
order: 10670
---

DateTimeImmutable::setISODate

Establece la fecha ISO

## Descripción

```php
#[\NoDiscard(message: "as DateTimeImmutable::setISODate() does not modify the object itself")] public DateTimeImmutable::setISODate(int $year, int $week, [int $dayOfWeek]): DateTimeImmutable
```php

Devuelve un nuevo objeto DateTimeImmutable con la fecha establecida de acuerdo al estándar ISO 8601 - usando semanas y desplazamientos de días en lugar de fechas específicas.

## Parámetros

`year`  
Año de la fecha.

`week`  
Semana de la fecha.

`dayOfWeek`  
Desplazamiento desde el primer día de la semana.

## Valores devueltos

Retorna un nuevo objeto `DateTimeImmutable` con los datos modificados.

## Ejemplos

Ejemplo de `DateTimeImmutable::setISODate`

Estilo orientado a objetos

```
<?php
$date = new DateTimeImmutable();

$newDate = $date->setISODate(2008, 2);
echo $newDate->format('Y-m-d') . "\n";

$newDate = $date->setISODate(2008, 2, 7);
echo $newDate->format('Y-m-d') . "\n";

   
```php

El ejemplo anterior mostrará:

    2008-01-07
    2008-01-13

       

Estilo procedimental

```
<?php

$date = date_create();

date_isodate_set($date, 2008, 2);
echo date_format($date, 'Y-m-d') . "\n";

date_isodate_set($date, 2008, 2, 7);
echo date_format($date, 'Y-m-d') . "\n";

   
```php

El ejemplo anterior mostrará:

    2008-01-07
    2008-01-13

Valores que exceden los rangos se añaden a sus valores padres

```
<?php

$date = new DateTimeImmutable();

$newDate = $date->setISODate(2008, 2, 7);
echo $newDate->format('Y-m-d') . "\n";

$newDate = $date->setISODate(2008, 2, 8);
echo $newDate->format('Y-m-d') . "\n";

$newDate = $date->setISODate(2008, 53, 7);
echo $newDate->format('Y-m-d') . "\n";

   
```php

El ejemplo anterior mostrará:

    2008-01-13
    2008-01-14
    2009-01-04

Buscando el mes en el que se encuentra una semana

```
<?php

$date = new DateTimeImmutable();
$newDate = $date->setISODate(2008, 14);
echo $newDate->format('n');

   
```php

El ejemplo anterior mostrará:

    3

## Véase también

DateTimeImmutable::setDate

DateTimeImmutable::setTime
