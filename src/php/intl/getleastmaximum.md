---
title: IntlCalendar::getLeastMaximum
description: Obtiene el mínimo máximo local para un campo
source_url: https://www.php.net/manual/es/intlcalendar.getleastmaximum.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/getleastmaximum.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 330a38c4d
order: 40380
---

IntlCalendar::getLeastMaximum

Obtiene el mínimo máximo local para un campo

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::getLeastMaximum(int $field): int
```php

Estilo procedimental

```php
intlcal_get_least_maximum(IntlCalendar $calendar, int $field): int
```

Devuelve el mínimo máximo local para un campo. Esto debería ser un valor menor o igual al devuelto por `IntlCalendar::getActualMaximum`, que a su vez es menor o igual al devuelto por `IntlCalendar::getMaximum`.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

`field`  

## Valores devueltos

Un `int` que representa un valor de campo, en la unidad del campo, o `false` si ocurre un error.

## Ejemplos

Ejemplo de máximo

```php
<?php
ini_set('date.timezone', 'UTC');
ini_set('intl.default_locale', 'it_IT');

$cal = new IntlGregorianCalendar(2013, 3 /* April */, 6);
var_dump(
    $cal->getLeastMaximum(IntlCalendar::FIELD_DAY_OF_MONTH),  // 28
    $cal->getActualMaximum(IntlCalendar::FIELD_DAY_OF_MONTH), // 30
    $cal->getMaximum(IntlCalendar::FIELD_DAY_OF_MONTH)        // 31
);

    
```

El ejemplo anterior mostrará:

    int(28)
    int(30)
    int(31)

## Véase también

IntlCalendar::getActualMaximum, IntlCalendar::getMaximum, IntlCalendar::getGreatestMinimum
