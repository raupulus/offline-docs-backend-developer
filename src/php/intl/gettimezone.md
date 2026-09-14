---
title: IntlDateFormatter::getTimeZone
description: Obtiene el formateador del huso horario
source_url: https://www.php.net/manual/es/intldateformatter.gettimezone.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/dateformatter/gettimezone.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 39660
---

IntlDateFormatter::getTimeZone

datefmt_get_timezone

Obtiene el formateador del huso horario

## Descripción

Estilo orientado a objetos

```php
public IntlDateFormatter::getTimeZone(): IntlTimeZone
```php

Estilo procedimental

```php
datefmt_get_timezone(IntlDateFormatter $formatter): IntlTimeZone
```

Devuelve un objeto `IntlTimeZone` que representa el huso horario utilizado por este objeto para formatear fechas y horas. Al formatear objetos `IntlCalendar` y `DateTime` con este `IntlDateFormatter`, el huso horario utilizado será devuelto por este método, y no aquel asociado con los objetos formateados.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El objeto `IntlTimeZone` asociado o `false` si ocurre un error.

## Ejemplos

Ejemplo con `IntlDateFormatter::getTimeZone`

```php
<?php

$madrid = IntlDateFormatter::create(NULL, NULL, NULL, 'Europe/Madrid');
$lisbon = IntlDateFormatter::create(NULL, NULL, NULL, 'Europe/Lisbon');

var_dump($madrid->getTimezone());
echo $madrid->getTimezone()->getDisplayName(
        false, IntlTimeZone::DISPLAY_GENERIC_LOCATION, "en_US"), "\n";
echo $lisbon->getTimeZone()->getId(), "\n";
// El identificador también puede ser obtenido con ->getTimezoneId()
echo $lisbon->getTimeZoneId(), "\n";

    
```

El ejemplo anterior mostrará:

    object(IntlTimeZone)#4 (4) {
      ["valid"]=>
      bool(true)
      ["id"]=>
      string(13) "Europe/Madrid"
      ["rawOffset"]=>
      int(3600000)
      ["currentOffset"]=>
      int(7200000)
    }
    Spain Time
    Europe/Lisbon
    Europe/Lisbon

## Véase también

`IntlDateFormatter::getTimeZoneId`, `IntlDateFormatter::setTimeZone`, `IntlTimeZone`
