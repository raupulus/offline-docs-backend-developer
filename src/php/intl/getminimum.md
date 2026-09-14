---
title: IntlCalendar::getMinimum
description: Obtiene el valor mínimo global para un campo
source_url: https://www.php.net/manual/es/intlcalendar.getminimum.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/getminimum.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40420
---

IntlCalendar::getMinimum

Obtiene el valor mínimo global para un campo

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::getMinimum(int $field): int
```php

Estilo procedimental

```php
intlcal_get_minimum(IntlCalendar $calendar, int $field): int
```

Devuelve el valor mínimo global para un campo, en este calendario específico. Este valor es menor o igual al devuelto por `IntlCalendar::getActualMinimum`, que a su vez es menor o igual al devuelto por `IntlCalendar::getGreatestMinimum`. Para el calendario gregoriano, estas tres funciones siempre devuelven el mismo valor (para cada campo).

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

`field`  

## Valores devueltos

Un `int` que representa un valor de campo, en la unidad del campo, o `false` si ocurre un error.
