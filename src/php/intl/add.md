---
title: IntlCalendar::add
description: Añade una duración (con signo) a un campo
source_url: https://www.php.net/manual/es/intlcalendar.add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 40190
---

IntlCalendar::add

Añade una duración (con signo) a un campo

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::add(int $field, int $value): bool
```php

Estilo procedimental

```php
intlcal_add(IntlCalendar $calendar, int $field, int $value): bool
```

Añade una duración con signo a un campo. La adición de una duración positiva permite avanzar en el tiempo, incluso si el valor numérico del campo disminuye (por ejemplo, cuando se trabaja con años en fechas BC).

Los otros campos deben ajustarse; por ejemplo, añadir un mes a la fecha del 31 de Enero devolverá el 28 (o 29) de Febrero. A diferencia de la función `IntlCalendar::roll`, cuando un valor abarca varios valores, varios campos pueden cambiar significativamente. Por ejemplo, añadir un día al 31 de Enero devolverá el 1 de Febrero, y no el 1 de Enero.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

`field`  

`value`  
La duración con signo a añadir al campo actual. Si la duración es positiva, el instante se moverá hacia adelante; si es negativa, el instante se moverá hacia el pasado. La unidad es implícita según el tipo de campo. Por ejemplo, será en horas para la constante `IntlCalendar::FIELD_HOUR_OF_DAY`.

## Valores devueltos

Devuelve `true` en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `IntlCalendar::add`

```php
<?php
ini_set('intl.default_locale', 'fr_FR');
ini_set('date.timezone', 'UTC');

$cal = new IntlGregorianCalendar(2012, 0 /* January */, 31);
echo IntlDateFormatter::formatObject($cal), "\n";

$cal->add(IntlCalendar::FIELD_MONTH, 1);
echo IntlDateFormatter::formatObject($cal), "\n";

$cal->add(IntlCalendar::FIELD_DAY_OF_MONTH, 1);
echo IntlDateFormatter::formatObject($cal), "\n";

    
```

El ejemplo anterior mostrará:

    31 janv. 2012 00:00:00
    29 févr. 2012 00:00:00
    1 mars 2012 00:00:00
