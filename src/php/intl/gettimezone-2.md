---
title: IntlCalendar::getTimeZone
description: Recupera la zona horaria del objeto
source_url: https://www.php.net/manual/es/intlcalendar.gettimezone.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/gettimezone.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 40470
---

IntlCalendar::getTimeZone

Recupera la zona horaria del objeto

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::getTimeZone(): IntlTimeZone
```php

Estilo procedimental

```php
intlcal_get_time_zone(IntlCalendar $calendar): IntlTimeZone
```

Devuelve el objeto `IntlTimeZone` asociado con este calendario.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

## Valores devueltos

Un objeto `IntlTimeZone` correspondiente al utilizado internamente por este objeto. Devuelve `false` en caso de error.

## Ejemplos

Ejemplo con `IntlCalendar::getTimeZone`

```php
<?php
ini_set('date.timezone', 'Europe/Lisbon');
ini_set('intl.default_locale', 'en_US');

$cal = IntlCalendar::createInstance();
print_r($cal->getTimeZone());

$cal->setTimeZone('UTC');
print_r($cal->getTimeZone());

$cal = IntlCalendar::fromDateTime('2012-01-01 00:00:00 GMT+03:33');
print_r($cal->getTimeZone());

    
```

El ejemplo anterior mostrará:

    IntlTimeZone Object
    (
        [valid] => 1
        [id] => Europe/Lisbon
        [rawOffset] => 0
        [currentOffset] => 3600000
    )
    IntlTimeZone Object
    (
        [valid] => 1
        [id] => UTC
        [rawOffset] => 0
        [currentOffset] => 0
    )
    IntlTimeZone Object
    (
        [valid] => 1
        [id] => GMT+03:33
        [rawOffset] => 12780000
        [currentOffset] => 12780000
    )

## Véase también

IntlCalendar::setTimeZone, IntlCalendar::createInstance, IntlGregorianCalendar::\_\_construct
