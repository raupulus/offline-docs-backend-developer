---
title: IntlCalendar::isWeekend
description: Indica si una fecha/hora es un fin de semana
source_url: https://www.php.net/manual/es/intlcalendar.isweekend.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/isweekend.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40540
---

IntlCalendar::isWeekend

Indica si una fecha/hora es un fin de semana

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::isWeekend([float $timestamp]): bool
```php

Estilo procedimental

```php
intlcal_is_weekend(IntlCalendar $calendar, [float $timestamp]): bool
```

Devuelve si la hora actual del objeto o el timestamp proporcionado ocurre durante un fin de semana en el sistema de calendario de este objeto.

Esta función requiere ICU 4.4 o más reciente.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

`timestamp`  
Un timestamp opcional que representa el número de milisegundos transcurridos desde el epoch, excluyendo los segundos intercalares. Si es `null`, se utiliza el tiempo actual de este objeto en su lugar.

## Valores devueltos

Un `bool` que indica si el tiempo dado o el de este objeto ocurre durante un fin de semana.

En caso de fallo, también se devuelve `false`. Para detectar condiciones de error, utilice `intl_get_error_code`, o configure Intl para lanzar [excepciones](#ini.intl.use-exceptions).

## Ejemplos

`IntlCalendar::isWeekend`

```php
<?php
ini_set('date.timezone', 'Europe/Lisbon');

$cal = new IntlGregorianCalendar(NULL, 'en_US');
$cal->set(2013, 6 /* July */, 7); // un domingo

var_dump($cal->isWeekend()); // true
var_dump($cal->isWeekend(strtotime('2013-07-01 00:00:00'))); // false, Monday

$cal = new IntlGregorianCalendar(NULL, 'ar_SA');
$cal->set(2013, 6 /* July */, 7); // un domingo
var_dump($cal->isWeekend()); // false, domingo no es fin de semana en este calendario

    
```

## Véase también

IntlCalendar::getDayOfWeekType, IntlCalendar::getWeekendTransition
