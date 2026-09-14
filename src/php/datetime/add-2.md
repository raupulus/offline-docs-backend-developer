---
title: DateTimeImmutable::add
description: Devuelve un nuevo objeto, con una cantidad añadida de días, meses, años,
  horas, minutos y segundos
source_url: https://www.php.net/manual/es/datetimeimmutable.add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimeimmutable/add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 726154e3c
order: 10570
---

DateTimeImmutable::add

Devuelve un nuevo objeto, con una cantidad añadida de días, meses, años, horas, minutos y segundos

## Descripción

```php
#[\NoDiscard(message: "as DateTimeImmutable::add() does not modify the object itself")] public DateTimeImmutable::add(DateInterval $interval): DateTimeImmutable
```php

Crea un nuevo objeto `DateTimeImmutable`, y añade el objeto `DateInterval` especificado para representar el nuevo valor.

## Parámetros

`interval`  
Un objeto `DateInterval`

## Valores devueltos

Retorna un nuevo objeto `DateTimeImmutable` con los datos modificados.

## Ejemplos

Ejemplo de `DateTimeImmutable::add`

Estilo orientado a objetos

```
<?php
$date = new DateTimeImmutable('2000-01-01');
$newDate = $date->add(new DateInterval('P10D'));
echo $newDate->format('Y-m-d') . "\n";
?>

   
```php

Más ejemplos de `DateTimeImmutable::add`

```
<?php
$date = new DateTimeImmutable('2000-01-01');
$newDate = $date->add(new DateInterval('PT10H30S'));
echo $newDate->format('Y-m-d H:i:s') . "\n";

$date = new DateTimeImmutable('2000-01-01');
$newDate = $date->add(new DateInterval('P7Y5M4DT4H3M2S'));
echo $newDate->format('Y-m-d H:i:s') . "\n";
?>

   
```php

El ejemplo anterior mostrará:

    2000-01-01 10:00:30
    2007-06-05 04:03:02

Tenga cuidado al agregar meses

```
<?php
$date = new DateTimeImmutable('2000-12-31');
$interval = new DateInterval('P1M');

$newDate1 = $date->add($interval);
echo $newDate1->format('Y-m-d') . "\n";

$newDate2 = $newDate1->add($interval);
echo $newDate2->format('Y-m-d') . "\n";
?>

   
```php

El ejemplo anterior mostrará:

    2001-01-31
    2001-03-03

## Véase también

DateTimeImmutable::sub

DateTimeImmutable::diff

DateTimeImmutable::modify
