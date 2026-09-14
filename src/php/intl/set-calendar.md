---
title: IntlDateFormatter::setCalendar
description: Define el tipo de calendario utilizado por el formateador
source_url: https://www.php.net/manual/es/intldateformatter.setcalendar.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/dateformatter/set-calendar.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 0545e305c
order: 39710
---

IntlDateFormatter::setCalendar

datefmt_set_calendar

Define el tipo de calendario utilizado por el formateador

## Descripción

Estilo orientado a objetos

```php
public IntlDateFormatter::setCalendar(IntlCalendar $calendar): bool
```php

Estilo procedimental

```php
datefmt_set_calendar(IntlDateFormatter $formatter, IntlCalendar $calendar): bool
```

Configura el calendario o el tipo de calendario a utilizar por el formateador.

## Parámetros

`formatter`  
El recurso de formateador `IntlDateFormatter`.

`calendar`  
Puede ser: el [tipo de calendario](#intl.intldateformatter-constants.calendartypes) a utilizar (por omisión, `IntlDateFormatter::GREGORIAN`, que también es utilizado si `null` es especificado) o un objeto `IntlCalendar`.

Cualquier objeto `IntlCalendar` pasado será clonado; ninguna modificación será realizada sobre el objeto en argumento.

El desplazamiento horario del formateador solo será conservado si un objeto `IntlCalendar` no es pasado, de lo contrario, el nuevo desplazamiento horario será el del objeto pasado.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión         | Descripción                                     |
|-----------------|-------------------------------------------------|
| PECL intl 3.0.0 | Se hace posible pasar un objeto `IntlCalendar`. |

## Ejemplos

Ejemplo con `datefmt_set_calendar`

```php
<?php
$fmt = datefmt_create(
    'en_US',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN
);
echo 'El calendario del formateador es: ' . datefmt_get_calendar($fmt);
datefmt_set_calendar($fmt, IntlDateFormatter::TRADITIONAL);
echo 'El calendario es ahora: ' . datefmt_get_calendar($fmt);
?>

   
```

Ejemplo orientado a objetos

```php
<?php
$fmt = new IntlDateFormatter(
    'en_US',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN
);
echo 'El calendario del formateador es: ' . $fmt->getCalendar();
$fmt->setCalendar(IntlDateFormatter::TRADITIONAL);
echo 'El calendario es ahora: ' . $fmt->getCalendar();
?>

   
```

El ejemplo anterior mostrará:

    El calendario del formateador es: 1
    El calendario es ahora: 0

Ejemplo con argumentos a `IntlCalendar`

```php
<?php
$time = strtotime("2013-03-03 00:00:00 UTC");
$formatter = IntlDateFormatter::create("en_US", NULL, NULL, "Europe/Amsterdam");

echo "antes: ", $formatter->format($time), "\n";

/* note que la configuración local del calendario no es utilizada! */
$formatter->setCalendar(IntlCalendar::createInstance(
               "America/New_York", "pt_PT@calendar=islamic"));

echo "después:  ", $formatter->format($time), "\n";

   
```

El ejemplo anterior mostrará:

    antes: Sunday, March 3, 2013 at 1:00:00 AM Central European Standard Time
    después:  Saturday, Rabiʻ II 20, 1434 at 7:00:00 PM Eastern Standard Time

## Véase también

`datefmt_get_calendar`, `datefmt_get_calendar_object`, `datefmt_create`
