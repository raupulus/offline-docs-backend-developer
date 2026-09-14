---
title: IntlDateFormatter::getCalendar
description: Lee el calendario utilizado por el objeto IntlDateFormatter
source_url: https://www.php.net/manual/es/intldateformatter.getcalendar.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/dateformatter/get-calendar.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: b2332afcd
order: 39570
---

IntlDateFormatter::getCalendar

datefmt_get_calendar

Lee el calendario utilizado por el objeto IntlDateFormatter

## Descripción

Estilo orientado a objetos

```php
public IntlDateFormatter::getCalendar(): int
```php

Estilo procedimental

```php
datefmt_get_calendar(IntlDateFormatter $formatter): int
```

## Parámetros

`formatter`  
El recurso de formateador `IntlDateFormatter`.

## Valores devueltos

El [tipo de calendario](#intl.intldateformatter-constants.calendartypes) utilizado por el formateador. Puede ser ya sea la constante `IntlDateFormatter::TRADITIONAL`, ya sea la constante `IntlDateFormatter::GREGORIAN`. Devuelve `false` en caso de fallo.

## Ejemplos

Ejemplo con `datefmt_get_calendar`

```php
<?php
$fmt = datefmt_create(
    'en_US',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN
);
echo 'El calendario del formateador es : ' . datefmt_get_calendar($fmt);
datefmt_set_calendar($fmt, IntlDateFormatter::TRADITIONAL);
echo 'El calendario es ahora : ' . datefmt_get_calendar($fmt);
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
echo 'El calendario del formateador es : ' . $fmt->getCalendar();
$fmt->setCalendar(IntlDateFormatter::TRADITIONAL);
echo 'El calendario es ahora : ' . $fmt->getCalendar();

?>

   
```

Ejemplo de manejo de configuración local inválida

```php
<?php
try {
    $fmt = new IntlDateFormatter(
        'locale_invalide',
        IntlDateFormatter::FULL,
        IntlDateFormatter::FULL,
        'je_ne_sais_pas',
        IntlDateFormatter::GREGORIAN,
    );
    $cal = $fmt->getCalendar();
} catch (\Error $e) {
    // ...
}
?>

    
```

El ejemplo anterior mostrará:

    El calendario del formateador es : 1
    El calendario es ahora : 0

      

## Véase también

`datefmt_get_calendar_object`, `datefmt_set_calendar`, `datefmt_create`
