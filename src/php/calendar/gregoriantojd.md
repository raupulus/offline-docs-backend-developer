---
title: gregoriantojd
description: Convierte una fecha gregoriana en número de días del calendario juliano
source_url: https://www.php.net/manual/es/function.gregoriantojd.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/calendar/functions/gregoriantojd.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: calendar
translation_status: ready
translation_reviewed: true
translation_revision: cca0f0ce4
order: 6600
---

gregoriantojd

Convierte una fecha gregoriana en número de días del calendario juliano

## Descripción

```php
gregoriantojd(int $month, int $day, int $year): int
```php

El intervalo de validez para el calendario gregoriano es del 25 de noviembre, 4714 a.C. al menos hasta el 31 de diciembre 9999 d.C.

Aunque es posible manipular fechas hasta el 4714 a.C., tal uso no es significativo. Este calendario fue creado el 18 de octubre de 1582 d.C. (o 5 de octubre 1582 en calendario juliano). Algunos países no lo aceptaron hasta mucho más tarde. Por ejemplo, los británicos no lo adoptaron hasta 1752, los rusos en 1918 y los griegos en 1923. La mayoría de los países europeos utilizaban el calendario juliano antes del gregoriano.

## Parámetros

`month`  
El mes, en forma de número comprendido entre 1 (para Enero) y 12 (para Diciembre)

`day`  
El día, en forma de número comprendido entre 1 y 31. Si el mes tiene menos días de los proporcionados, se produce un desbordamiento; ver ejemplo a continuación.

`year`  
El año, en forma de número comprendido entre -4714 y 9999. Los números negativos significan años antes de C., los números positivos significan después de C. Se observa que no existe el año `0`; 31 de diciembre, 1 a.C. es inmediatamente seguido por 1 de enero, 1 d.C.

## Valores devueltos

El día juliano para la fecha gregoriana proporcionada, en forma de `int`. Las fechas fuera del intervalo válido devuelven `0`.

## Ejemplos

Funciones calendario

```
<?php
$jd = gregoriantojd(10, 11, 1970);
echo "$jd\n";
$gregorian = jdtogregorian($jd);
echo "$gregorian\n";
?>

    
```php

El ejemplo anterior mostrará:

    2440871
    10/11/1970

Comportamiento de desbordamiento

```
<?php
echo gregoriantojd(2, 31, 2018), PHP_EOL,
     gregoriantojd(3,  3, 2018), PHP_EOL;
?>

    
```php

El ejemplo anterior mostrará:

    2458181
    2458181

## Véase también

`jdtogregorian`, `cal_to_jd`
