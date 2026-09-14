---
title: cal_days_in_month
description: Devolver el número de días de un mes para un año y un calendario dados
source_url: https://www.php.net/manual/es/function.cal-days-in-month.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/calendar/functions/cal-days-in-month.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: calendar
translation_status: ready
translation_revision: 87d952ec1
order: 6530
---

cal_days_in_month

Devolver el número de días de un mes para un año y un calendario dados

## Descripción

```php
cal_days_in_month(int $calendar, int $month, int $year): int
```php

Esta función devolverá el número de días del mes `month` del año `year` para el calendario `calendar` especificado.

## Parámetros

`calendar`  
El calendario que se va a usar para el cálculo

`month`  
El mes del calendario seleccionado

`year`  
El año del calendario seleccionado

## Valores devueltos

La longitud en días del mes seleccionado en el calendario dado.

## Ejemplos

Ejemplo de `cal_days_in_month`

```
<?php
$número = cal_days_in_month(CAL_GREGORIAN, 8, 2003); // 31
echo "Hubo {$número} días en agosto del 2003";
?>

    
```php
