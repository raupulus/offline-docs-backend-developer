---
title: DateTimeImmutable::sub
description: Sustrae una cantidad de días, meses, años, horas, minutos y segundos
source_url: https://www.php.net/manual/es/datetimeimmutable.sub.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimeimmutable/sub.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 726154e3c
order: 10720
---

DateTimeImmutable::sub

Sustrae una cantidad de días, meses, años, horas, minutos y segundos

## Descripción

```php
#[\NoDiscard(message: "as DateTimeImmutable::sub() does not modify the object itself")] public DateTimeImmutable::sub(DateInterval $interval): DateTimeImmutable
```php

Devuelve un nuevo objeto `DateTimeImmutable`, con el objeto `DateInterval` especificado sustraído del objeto `DateTimeImmutable` especificado.

## Parámetros

`interval`  
Un objeto `DateInterval`

## Valores devueltos

Retorna un nuevo objeto `DateTimeImmutable` con los datos modificados.

## Errores/Excepciones

Si se intenta realizar una operación no soportada, como usar un objeto `DateInterval` que represente especificaciones de tiempo relativas como `próximo día de la semana`, se lanzará una DateInvalidOperationException.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Ahora lanza una DateInvalidOperationException en lugar de una advertencia cuando se intenta realizar una operación no soportada. |

## Ejemplos

Ejemplo de `DateTimeImmutable::sub`

Estilo orientado a objetos

```
<?php
$date = new DateTimeImmutable('2000-01-20');
$newDate = $date->sub(new DateInterval('P10D'));
echo $newDate->format('Y-m-d') . "\n";
?>

   
```php

El ejemplo anterior mostrará:

    2000-01-10

Más ejemplos de `DateTimeImmutable::sub`

```
<?php
$date = new DateTimeImmutable('2000-01-20');
$newDate = $date->sub(new DateInterval('PT10H30S'));
echo $newDate->format('Y-m-d H:i:s') . "\n";

$date = new DateTimeImmutable('2000-01-20');
$newDate = $date->sub(new DateInterval('P7Y5M4DT4H3M2S'));
echo $newDate->format('Y-m-d H:i:s') . "\n";
?>

   
```php

El ejemplo anterior mostrará:

    2000-01-19 13:59:30
    1992-08-15 19:56:58

Tenga cuidado al substraer meses

```
<?php
$date = new DateTimeImmutable('2001-04-30');
$interval = new DateInterval('P1M');

$newDate1 = $date->sub($interval);
echo $newDate1->format('Y-m-d') . "\n";

$newDate2 = $newDate1->sub($interval);
echo $newDate2->format('Y-m-d') . "\n";
?>

   
```php

El ejemplo anterior mostrará:

    2001-03-30
    2001-03-02

## Véase también

DateTimeImmutable::add

DateTimeImmutable::diff

DateTimeImmutable::modify
