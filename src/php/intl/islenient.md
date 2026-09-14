---
title: IntlCalendar::isLenient
description: Indica si la interpretación de la fecha/hora está en modo tolerante
source_url: https://www.php.net/manual/es/intlcalendar.islenient.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/islenient.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40520
---

IntlCalendar::isLenient

Indica si la interpretación de la fecha/hora está en modo tolerante

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::isLenient(): bool
```php

Estilo procedimental

```php
intlcal_is_lenient(IntlCalendar $calendar): bool
```

Devuelve si la interpretación de la fecha/hora está en modo tolerante (el modo por omisión). Si es así, ciertos valores fuera de límites para los campos serán aceptados en lugar de generar un error.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

## Valores devueltos

Un `bool` que representa si el calendario está en modo tolerante.

## Ejemplos

`IntlCalendar::isLenient`

```php
<?php
ini_set('date.timezone', 'Europe/Lisbon');
ini_set('intl.default_locale', 'pt_PT');
ini_set('intl.use_exceptions', '1');

$cal = new IntlGregorianCalendar(2013, 6 /* July */, 1);
var_dump(IntlDateFormatter::formatObject($cal), // 01/07/2013, 00:00:00
$cal->isLenient()); // true

$cal->set(IntlCalendar::FIELD_DAY_OF_MONTH, 33);
var_dump(IntlDateFormatter::formatObject($cal)); // 02/08/2013, 00:00:00

$cal->setLenient(false);
var_dump($cal->isLenient()); // false
$cal->set(IntlCalendar::FIELD_DAY_OF_MONTH, 33);
var_dump(IntlDateFormatter::formatObject($cal)); // error

    
```

El ejemplo anterior mostrará:

    string(20) "01/07/2013, 00:00:00"
    bool(true)
    string(20) "02/08/2013, 00:00:00"
    bool(false)

    Fatal error: Uncaught exception 'IntlException' with message 'datefmt_format_object: error obtaining instant from IntlCalendar' in /home/foobar/example.php:16
    Stack trace:
    #0 /home/foobar/example.php(16): IntlDateFormatter::formatObject(Object(IntlGregorianCalendar))
    #1 {main}
      thrown in /home/foobar/example.php on line 16
