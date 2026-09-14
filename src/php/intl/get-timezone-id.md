---
title: IntlDateFormatter::getTimeZoneId
description: Lee el huso horario de IntlDateFormatter
source_url: https://www.php.net/manual/es/intldateformatter.gettimezoneid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/dateformatter/get-timezone-id.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 39640
---

IntlDateFormatter::getTimeZoneId

datefmt_get_timezone_id

Lee el huso horario de IntlDateFormatter

## Descripción

Estilo orientado a objetos

```php
public IntlDateFormatter::getTimeZoneId(): string
```php

Estilo procedimental

```php
datefmt_get_timezone_id(IntlDateFormatter $formatter): string
```

Lee el huso horario utilizado por IntlDateFormatter.

## Parámetros

`formatter`  
El recurso de formateador `IntlDateFormatter`.

## Valores devueltos

El identificador del huso horario utilizado por este formateador, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `datefmt_get_timezone_id`

```php
<?php
$fmt = datefmt_create(
    'en_US',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN
);
echo 'El timezone_id del formateador es:' . datefmt_get_timezone_id($fmt) . "\n";
datefmt_set_timezone($fmt, 'Europe/Madrid');
echo 'Ahora el timezone_id del formateador es:' . datefmt_get_timezone_id($fmt);

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
echo 'El timezone_id del formateador es:' . $fmt->getTimezoneId() . "\n";
$fmt->setTimezone('Europe/Madrid');
echo 'Ahora el timezone_id del formateador es:' . $fmt->getTimezoneId();

?>

   
```

El ejemplo anterior mostrará:

    El timezone_id del formateador es:America/Los_Angeles
    Ahora el timezone_id del formateador es:Europe/Madrid

      

## Véase también

`datefmt_set_timezone`, `datefmt_create`
