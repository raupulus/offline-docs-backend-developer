---
title: DateTimeImmutable::setDate
description: Establece la fecha
source_url: https://www.php.net/manual/es/datetimeimmutable.setdate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimeimmutable/setdate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 726154e3c
order: 10660
---

DateTimeImmutable::setDate

Establece la fecha

## Descripción

```php
#[\NoDiscard(message: "as DateTimeImmutable::setDate() does not modify the object itself")] public DateTimeImmutable::setDate(int $year, int $month, int $day): DateTimeImmutable
```php

Devuelve un nuevo objeto DateTimeImmutable con la fecha actual del objeto DateTimeImmutable establecida a la fecha dada.

## Parámetros

`object`  
Solo en estilo procedimental: Un objeto `DateTime` retornado por la función `date_create`. Esta función modifica este objeto.

`year`  
Año de la fecha.

`month`  
Mes de la fecha.

`day`  
Día de la fecha.

## Valores devueltos

Retorna un nuevo objeto `DateTimeImmutable` con los datos modificados.

## Ejemplos

Ejemplo de `DateTimeImmutable::setDate`

Estilo orientado a objetos

```
<?php
$date = new DateTimeImmutable();
$newDate = $date->setDate(2001, 2, 3);
echo $newDate->format('Y-m-d');

   
```php

El ejemplo anterior mostrará:

    2001-02-03

Valores que exceden los rangos se añaden a sus valores padres

```
<?php
$date = new DateTimeImmutable();

$newDate = $date->setDate(2001, 2, 28);
echo $newDate->format('Y-m-d') . "\n";

$newDate = $date->setDate(2001, 2, 29);
echo $newDate->format('Y-m-d') . "\n";

$newDate = $date->setDate(2001, 14, 3);
echo $newDate->format('Y-m-d') . "\n";

   
```php

El ejemplo anterior mostrará:

    2001-02-28
    2001-03-01
    2002-02-03

## Véase también

DateTimeImmutable::setISODate

DateTimeImmutable::setTime
