---
title: IntlDateFormatter::setTimeZone
description: Define el formateador para el desplazamiento horario
source_url: https://www.php.net/manual/es/intldateformatter.settimezone.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/dateformatter/settimezone.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 574787bef
order: 39740
---

IntlDateFormatter::setTimeZone

datefmt_set_timezone

Define el formateador para el desplazamiento horario

## Descripción

Estilo orientado a objetos

```php
public IntlDateFormatter::setTimeZone(IntlTimeZone $timezone): bool
```php

Estilo procedimental

```php
datefmt_set_timezone(IntlDateFormatter $formatter, IntlTimeZone $timezone): bool
```

Define el desplazamiento horario utilizado por el objeto IntlDateFormatter.

## Parámetros

`formatter`  
El formateador de recursos.

`timezone`  
El desplazamiento horario a utilizar con este formateador. Puede ser especificado mediante los siguientes formatos:

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Esta función devuelve ahora `true` en caso de éxito; previamente devolvía `null`. |

## Ejemplos

Ejemplo con `IntlDateFormatter::setTimeZone`

```php
<?php
ini_set('date.timezone', 'Europe/Amsterdam');

$formatter = IntlDateFormatter::create(NULL, NULL, NULL, "UTC");

$formatter->setTimeZone(NULL);
echo "NULL\n    ", $formatter->getTimeZone()->getId(), "\n";

$formatter->setTimeZone(IntlTimeZone::createTimeZone('Europe/Lisbon'));
echo "IntlTimeZone\n    ", $formatter->getTimeZone()->getId(), "\n";

$formatter->setTimeZone(new DateTimeZone('Europe/Paris'));
echo "DateTimeZone\n    ", $formatter->getTimeZone()->getId(), "\n";

$formatter->setTimeZone('Europe/Rome');
echo "String\n    ", $formatter->getTimeZone()->getId(), "\n";

$formatter->setTimeZone('GMT+00:30');
print_r($formatter->getTimeZone());

    
```

El ejemplo anterior mostrará:

    NULL
        Europe/Amsterdam
    IntlTimeZone
        Europe/Lisbon
    DateTimeZone
        Europe/Paris
    String
        Europe/Rome
    IntlTimeZone Object
    (
        [valid] => 1
        [id] => GMT+00:30
        [rawOffset] => 1800000
        [currentOffset] => 1800000
    )

## Véase también

`IntlDateFormatter::getTimeZone`
