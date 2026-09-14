---
title: IntlDateFormatter::getPattern
description: Lee el patrón utilizado por IntlDateFormatter
source_url: https://www.php.net/manual/es/intldateformatter.getpattern.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/dateformatter/get-pattern.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 39620
---

IntlDateFormatter::getPattern

datefmt_get_pattern

Lee el patrón utilizado por IntlDateFormatter

## Descripción

Estilo orientado a objetos

```php
public IntlDateFormatter::getPattern(): string
```php

Estilo procedimental

```php
datefmt_get_pattern(IntlDateFormatter $formatter): string
```

Lee el patrón utilizado por el formateador.

## Parámetros

`formatter`  
El recurso de formateador `IntlDateFormatter`.

## Valores devueltos

El patrón utilizado para analizar y formar, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `datefmt_get_pattern`

```php
<?php
$fmt = datefmt_create(
    'en_US',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN,
    'MM/dd/yyyy'
);
echo 'El patrón del formateador es: ' . datefmt_get_pattern($fmt);
echo 'El primer resultado con el patrón es ' . datefmt_format($fmt, 0);
datefmt_set_pattern($fmt,'yyyymmdd hh:mm:ss z');
echo 'Ahora el patrón del formateador es: ' . datefmt_get_pattern($fmt);
echo 'El segundo resultado con el patrón es ' . datefmt_format($fmt, 0);

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
    IntlDateFormatter::GREGORIAN,
    'MM/dd/yyyy'
);
echo 'El patrón del formateador es: ' . $fmt->getPattern();
echo 'El primer resultado con el patrón es ' . $fmt->format(0);
$fmt->setPattern('yyyymmdd hh:mm:ss z');
echo 'Ahora el patrón del formateador es: ' . $fmt->getPattern();
echo 'El segundo resultado con el patrón es ' . $fmt->format(0);
?>

   
```

El ejemplo anterior mostrará:

    El patrón del formateador es: MM/dd/yyyy
    El primer resultado con el patrón es 12/31/1969
    Ahora el patrón del formateador es: yyyymmdd hh:mm:ss z
    El segundo resultado con el patrón es 19690031 04:00:00 PST

      

## Véase también

`datefmt_set_pattern`, `datefmt_create`
