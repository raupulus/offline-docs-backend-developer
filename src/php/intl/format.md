---
title: IntlDateFormatter::format
description: Formatea la fecha y la hora como string
source_url: https://www.php.net/manual/es/intldateformatter.format.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/dateformatter/format.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 0545e305c
order: 39550
---

IntlDateFormatter::format

datefmt_format

Formatea la fecha y la hora como string

## Descripción

Estilo orientado a objetos

```php
public IntlDateFormatter::format(IntlCalendar $datetime): string
```php

Estilo procedimental

```php
datefmt_format(IntlDateFormatter $formatter, IntlCalendar $datetime): string
```

Formatea la hora como string.

## Parámetros

`formatter`  
El recurso de formateador `IntlDateFormatter`.

`datetime`  
El valor a formatear. Puede ser un objeto `DateTimeInterface`, un objeto `IntlCalendar`, un tipo `numeric` representando un (puede ser fraccionado) número de segundos desde la época o un `array` en el formato de salida de la función `localtime`.

Si se pasa un objeto `DateTime` o un objeto `IntlCalendar`, su zona horaria no será considerada. El objeto deberá ser formateado utilizando la zona horaria configurada para este formateador. Si se desea utilizar la zona horaria del objeto a formatear, el método `IntlDateFormatter::setTimeZone` deberá ser llamado antes de la zona horaria del objeto. También puede utilizarse el método `IntlDateFormatter::formatObject` para obtener el mismo resultado.

## Valores devueltos

El string formateado, o, si ocurre un error, `false`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.1.5 | Se añadió el soporte para proporcionar un objeto genérico `DateTimeInterface` para el argumento `datetime`. Anteriormente, solo los objetos válidos `DateTime` eran soportados. |
| PECL intl 3.0.0 | Ahora es posible pasar un objeto `IntlCalendar` como valor del argumento `datetime`. |

## Ejemplos

Ejemplo con `datefmt_format`

```php
<?php
$fmt = datefmt_create(
    'en_US',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN
);
echo 'El primer formato mostrado es ' . datefmt_format($fmt, 0);

$fmt = datefmt_create(
    'de-DE',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN
);
echo 'El segundo formato mostrado es ' . datefmt_format($fmt, 0);

$fmt = datefmt_create(
    'en_US',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN,
    'MM/dd/yyyy'
);
echo 'El primer formato es mostrado con el patrón ' . datefmt_format($fmt, 0);

$fmt = datefmt_create(
    'de-DE',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN,
    'MM/dd/yyyy'
);
echo "El segundo formato es mostrado con el patrón " . datefmt_format($fmt, 0);
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
echo 'El primer formato mostrado es ' . $fmt->format(0);

$fmt = new IntlDateFormatter(
    'de-DE',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN
);
echo 'El segundo formato mostrado es ' . $fmt->format(0);

$fmt = new IntlDateFormatter(
    'en_US',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN,
    'MM/dd/yyyy'
);
echo 'El primer formato es mostrado con el patrón ' . $fmt->format(0);

$fmt = new IntlDateFormatter(
    'de-DE',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN,
    'MM/dd/yyyy'
);
echo 'El segundo formato es mostrado con el patrón ' . $fmt->format(0);
?>

   
```

El ejemplo anterior mostrará:

    El primer formato mostrado es Wednesday, December 31, 1969 4:00:00 PM PT
    El segundo formato mostrado es Mittwoch, 31. Dezember 1969 16:00 Uhr GMT-08:00
    El primer formato es mostrado con el patrón : 12/31/1969
    El segundo formato es mostrado con el patrón : 12/31/1969

Ejemplo con un objeto `IntlCalendar`

```php
<?php
$tz = reset(iterator_to_array(IntlTimeZone::createEnumeration('FR')));
$formatter = IntlDateFormatter::create(
    'fr_FR',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    $tz,
    IntlDateFormatter::GREGORIAN
);

$cal = IntlCalendar::createInstance($tz, '@calendar=islamic-civil');
$cal->set(IntlCalendar::FIELD_MONTH, 8); //9º mes, Ramadán
$cal->set(IntlCalendar::FIELD_DAY_OF_MONTH, 1); //1º día
$cal->clear(IntlCalendar::FIELD_HOUR_OF_DAY);
$cal->clear(IntlCalendar::FIELD_MINUTE);
$cal->clear(IntlCalendar::FIELD_SECOND);
$cal->clear(IntlCalendar::FIELD_MILLISECOND);

echo "En el año Islámico, el Ramadán comienza el :\n\t",
        $formatter->format($cal), "\n";

//Es la zona horaria del formateador la que se utiliza aquí :
$formatter->setTimeZone('Asia/Tokyo');
echo "Después de modificar la zona horaria :\n\t",
        $formatter->format($cal), "\n";

   
```

El ejemplo anterior mostrará:

    En el año Islámico, el Ramadán comienza el :
        martes 9 julio 2013 19:00:00 hora avanzada de Europa central
    Después de modificar la zona horaria :
        miércoles 10 julio 2013 02:00:00 hora normal de Japón

## Véase también

`datefmt_create`, `datefmt_parse`, `datefmt_get_error_code`, `datefmt_get_error_message`, `datefmt_format_object`
