---
title: IntlCalendar::setDate
description: Establece un campo de fecha
source_url: https://www.php.net/manual/es/intlcalendar.setdate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/setdate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 2a9c4f55b
order: 40570
---

IntlCalendar::setDate

Establece un campo de fecha

## Descripción

```php
public IntlCalendar::setDate(int $year, int $month, int $dayOfMonth): void
```php

Establece un campo de fecha al valor dado.

## Parámetros

`year`  
El nuevo valor para `IntlCalendar::FIELD_YEAR`.

`month`  
El nuevo valor para `IntlCalendar::FIELD_MONTH`. La secuencia de meses comienza en cero, es decir, que enero está representado por 0, febrero por 1, ..., diciembre por 11 y Undecember (si el calendario lo soporta) por 12.

`dayOfMonth`  
El nuevo valor para `IntlCalendar::FIELD_DAY_OF_MONTH`.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `IntlCalendar::setDate`

```
<?php
$intlCal = IntlCalendar::createInstance('UTC');

$intlCal->setDate(2012, 1, 29);
?>

    
```php
