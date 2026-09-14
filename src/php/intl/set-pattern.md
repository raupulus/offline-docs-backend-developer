---
title: IntlDateFormatter::setPattern
description: Configura el patrón utilizado por IntlDateFormatter
source_url: https://www.php.net/manual/es/intldateformatter.setpattern.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/dateformatter/set-pattern.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 39730
---

IntlDateFormatter::setPattern

datefmt_set_pattern

Configura el patrón utilizado por IntlDateFormatter

## Descripción

Estilo orientado a objetos

```php
public IntlDateFormatter::setPattern(string $pattern): bool
```php

Estilo procedimental

```php
datefmt_set_pattern(IntlDateFormatter $formatter, string $pattern): bool
```

Configura el patrón utilizado por `IntlDateFormatter`.

## Parámetros

`formatter`  
El recurso de formateador `IntlDateFormatter`.

`pattern`  
El nuevo patrón a utilizar. Los patrones posibles están documentados en <https://unicode-org.github.io/icu/userguide/format_parse/datetime/>.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Un formato incorrecto de la cadena es generalmente la causa del fallo de esta función.

## Ejemplos

Ejemplo con `datefmt_get_pattern`

```php
<?php
$fmt = datefmt_create(
    'en_US',
    IntlDateFormatter::FULL,IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN,
    'MM/dd/yyyy'
);
echo 'El patrón del formateador es: ', datefmt_get_pattern($fmt), PHP_EOL;
echo 'La primera salida formateada con el patrón es ', datefmt_format($fmt, 0), PHP_EOL;
datefmt_set_pattern($fmt, 'yyyyMMdd hh:mm:ss z');
echo 'Ahora el patrón del formateador es: ', datefmt_get_pattern($fmt), PHP_EOL;
echo 'La segunda salida formateada con el patrón es ', datefmt_format($fmt, 0), PHP_EOL;
?>

   
```

Ejemplo orientado a objetos

```php
<?php
$fmt = new IntlDateFormatter(
    'en_US',
    IntlDateFormatter::FULL,IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN,
    'MM/dd/yyyy'
);
echo 'El patrón del formateador es: ', $fmt->getPattern(), PHP_EOL;
echo 'La primera salida formateada es ', $fmt->format(0), PHP_EOL;
$fmt->setPattern('yyyyMMdd hh:mm:ss z');
echo 'Ahora el patrón del formateador es: ', $fmt->getPattern(), PHP_EOL;
echo 'La segunda salida formateada es ', $fmt->format(0), PHP_EOL;
?>

   
```

El ejemplo anterior mostrará:

    El patrón del formateador es: MM/dd/yyyy
    La primera salida formateada es 12/31/1969
    Ahora el patrón del formateador es: yyyyMMdd hh:mm:ss z
    La segunda salida formateada es 19691231 04:00:00 PST

      

## Véase también

`datefmt_get_pattern`, `datefmt_create`
