---
title: IntlCalendar::getMaximum
description: Obtiene el valor máximo global para un campo
source_url: https://www.php.net/manual/es/intlcalendar.getmaximum.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/getmaximum.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40400
---

IntlCalendar::getMaximum

Obtiene el valor máximo global para un campo

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::getMaximum(int $field): int
```php

Estilo procedimental

```php
intlcal_get_maximum(IntlCalendar $calendar, int $field): int
```

Devuelve el máximo global para un campo, en este calendario específico. Este valor es mayor o igual al devuelto por `IntlCalendar::getActualMaximum`, que a su vez es mayor o igual al devuelto por `IntlCalendar::getLeastMaximum`.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

`field`  

## Valores devueltos

Un `int` que representa un valor de campo, en la unidad del campo, o `false` si ocurre un error.

## Véase también

IntlCalendar::getActualMaximum, IntlCalendar::getLeastMaximum, IntlCalendar::getMinimum
