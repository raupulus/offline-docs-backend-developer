---
title: IntlCalendar::getTime
description: Obtiene el tiempo actualmente representado por el objeto
source_url: https://www.php.net/manual/es/intlcalendar.gettime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/gettime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40460
---

IntlCalendar::getTime

Obtiene el tiempo actualmente representado por el objeto

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::getTime(): float
```php

Estilo procedimental

```php
intlcal_get_time(IntlCalendar $calendar): float
```

Devuelve el tiempo asociado a este objeto, expresado como número de milisegundos transcurridos desde la época.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

## Valores devueltos

Un `float` que representa el número de milisegundos transcurridos desde el tiempo de referencia (1 Ene 1970 00:00:00 UTC), o `false` si ocurre un error

## Ejemplos

`IntlCalendar::getTime`

```php
<?php
ini_set('date.timezone', 'Europe/Lisbon');
ini_set('intl.default_locale', 'en_US');

$cal = new IntlGregorianCalendar(2013, 4 /* May */, 1, 0, 0, 0);
$time = $cal->getTime();
var_dump($time, $time / 1000 == strtotime('2013-05-01 00:00:00')); //true

    
```

El ejemplo anterior mostrará:

    float(1367362800000)
    bool(true)

## Véase también

IntlCalendar::getNow
