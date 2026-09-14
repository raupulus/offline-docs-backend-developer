---
title: IntlCalendar::setDateTime
description: Establece un campo de fecha y hora
source_url: https://www.php.net/manual/es/intlcalendar.setdatetime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/setdatetime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: d715365c0
order: 40580
---

IntlCalendar::setDateTime

Establece un campo de fecha y hora

## Descripción

```php
public IntlCalendar::setDateTime(int $year, int $month, int $dayOfMonth, int $hour, int $minute, [int $second]): void
```php

Establece un campo de fecha y hora al valor dado.

## Parámetros

`year`  
El nuevo valor para `IntlCalendar::FIELD_YEAR`.

`month`  
El nuevo valor para `IntlCalendar::FIELD_MONTH`. La secuencia de los meses comienza en cero, es decir, enero está representado por 0, febrero por 1, ..., diciembre por 11 y Undecember (si el calendario lo soporta) por 12.

`dayOfMonth`  
El nuevo valor para `IntlCalendar::FIELD_DAY_OF_MONTH`.

`hour`  
El nuevo valor para `IntlCalendar::FIELD_HOUR_OF_DAY`.

`minute`  
El nuevo valor para `IntlCalendar::FIELD_MINUTE`.

`second`  
El nuevo valor para `IntlCalendar::FIELD_SECOND`.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `IntlCalendar::setDateTime`

```
<?php
$intlCal = IntlCalendar::createInstance('UTC');

$intlCal->setDateTime(2012, 1, 29, 23, 58);
?>

    
```php
