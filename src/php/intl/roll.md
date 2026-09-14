---
title: IntlCalendar::roll
description: Añade un valor a un campo sin reportarlo a los campos más significativos
source_url: https://www.php.net/manual/es/intlcalendar.roll.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/roll.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40550
---

IntlCalendar::roll

Añade un valor a un campo sin reportarlo a los campos más significativos

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::roll(int $field, int $value): bool
```php

Estilo procedimental

```php
intlcal_roll(IntlCalendar $calendar, int $field, int $value): bool
```

Añade un valor (signado) a un campo. La diferencia con `IntlCalendar::add` es que cuando el valor del campo desborda, no se reporta a los campos más significativos.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

`field`  

`value`  
El valor (signado) a añadir al campo, `true` para ir hacia arriba (añadiendo `1`), o `false` para ir hacia abajo (restando `1`).

## Valores devueltos

Devuelve `true` en caso de éxito o `false` en caso de fallo.

## Ejemplos

`IntlCalendar::roll`

```php
<?php
ini_set('date.timezone', 'Europe/Lisbon');
ini_set('intl.default_locale', 'pt_PT');

$cal = new IntlGregorianCalendar(2013, 5 /* June */, 30);

$cal->add(IntlCalendar::FIELD_DAY_OF_MONTH, 1);
var_dump(IntlDateFormatter::formatObject($cal)); // "01/07/2013, 00:00:00"

$cal->set(2013, 5 /* June */, 30);
$cal->roll(IntlCalendar::FIELD_DAY_OF_MONTH, true); // ir hacia arriba, como rodar +1
var_dump(IntlDateFormatter::formatObject($cal)); // "01/06/2013, 00:00:00"

    
```

El ejemplo anterior mostrará:

    string(20) "01/07/2013, 00:00:00"
    string(20) "01/06/2013, 00:00:00"

## Véase también

IntlCalendar::add, IntlCalendar::set
