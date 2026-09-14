---
title: IntlCalendar::getGreatestMinimum
description: Devuelve el valor mínimo local más grande para un campo
source_url: https://www.php.net/manual/es/intlcalendar.getgreatestminimum.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/getgreatestminimum.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40360
---

IntlCalendar::getGreatestMinimum

Devuelve el valor mínimo local más grande para un campo

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::getGreatestMinimum(int $field): int
```php

Estilo procedimental

```php
intlcal_get_greatest_minimum(IntlCalendar $calendar, int $field): int
```

Devuelve el valor mínimo local más grande para un campo. Este valor debe ser mayor o igual al devuelto por `IntlCalendar::getActualMinimum`, que a su vez debe ser mayor o igual al devuelto por `IntlCalendar::getMinimum`. Estas tres funciones devuelven el mismo valor para el calendario gregoriano.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

`field`  

## Valores devueltos

Un `int` que representa un valor de campo, en la unidad del campo, o `false` si ocurre un error.
