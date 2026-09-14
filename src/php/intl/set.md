---
title: IntlCalendar::set
description: Define un campo de tiempo o varios campos comunes a la vez
source_url: https://www.php.net/manual/es/intlcalendar.set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: d3ee29b81
order: 40560
---

IntlCalendar::set

Define un campo de tiempo o varios campos comunes a la vez

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::set(int $field, int $value): true
```php

```php
public IntlCalendar::set(int $year, int $month, [int $dayOfMonth], [int $hour], [int $minute], [int $second]): true
```

Estilo procedimental

```php
intlcal_set(IntlCalendar $cal, int $field, int $value): true
```php

```php
intlcal_set(IntlCalendar $cal, int $year, int $month, [int $dayOfMonth], [int $hour], [int $minute], [int $second]): bool
```

Define ya sea un campo específico con el valor dado, o define varios campos comunes a la vez. El rango de valores aceptables depende de si el calendario utiliza el [modo tolerante](#intlcalendar.setlenient).

Para los campos que entran en conflicto, los campos definidos más tarde tienen prioridad.

Este método no puede ser llamado con exactamente cuatro argumentos.

## Parámetros

`cal`  
Una instancia de `IntlCalendar`.

`field`  

`value`  
El nuevo valor del campo dado.

`year`  
El nuevo valor para `IntlCalendar::FIELD_YEAR`.

`month`  
El nuevo valor para `IntlCalendar::FIELD_MONTH`. La secuencia de los meses comienza en cero, es decir que enero es representado por 0, febrero por 1, ..., diciembre por 11 y Undecember (si el calendario lo soporta) por 12.

`dayOfMonth`  
El nuevo valor para `IntlCalendar::FIELD_DAY_OF_MONTH`.

`hour`  
El nuevo valor para `IntlCalendar::FIELD_HOUR_OF_DAY`.

`minute`  
El nuevo valor para `IntlCalendar::FIELD_MINUTE`.

`second`  
El nuevo valor para `IntlCalendar::FIELD_SECOND`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | El tipo de retorno es ahora `true`, anteriormente era `bool`. |
| 8.4.0 | Esto ha sido deprecado en favor de los métodos IntlCalendar::setDate y IntlCalendar::setDateTime. |

## Ejemplos

`IntlCalendar::set`

```php
<?php
ini_set('date.timezone', 'Europe/Lisbon');
ini_set('intl.default_locale', 'pt_PT');

//Las últimas llamadas tienen prioridad
$cal = new IntlGregorianCalendar(2013, 6 /* July */, 1);
$cal->set(IntlCalendar::FIELD_YEAR, 2012);
$cal->set(IntlCalendar::FIELD_EXTENDED_YEAR, 2011);
var_dump(IntlDateFormatter::formatObject($cal));

$cal = new IntlGregorianCalendar(2013, 6 /* July */, 1);
$cal->set(IntlCalendar::FIELD_YEAR, 2012);
$cal->set(IntlCalendar::FIELD_EXTENDED_YEAR, 2011);
//el tiempo no ha sido recalculado. Si borramos el año extendido,
//el año definido antes será utilizado
$cal->clear(IntlCalendar::FIELD_EXTENDED_YEAR);
var_dump(IntlDateFormatter::formatObject($cal));

    
```

El ejemplo anterior mostrará:

    string(20) "01/07/2011, 00:00:00"
    string(20) "01/07/2012, 00:00:00"

## Véase también

IntlCalendar::get, IntlCalendar::add, IntlCalendar::roll
