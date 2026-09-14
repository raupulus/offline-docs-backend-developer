---
title: IntlDateFormatter::parse
description: Analiza una cadena hacia un timestamp
source_url: https://www.php.net/manual/es/intldateformatter.parse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/dateformatter/parse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 39690
---

IntlDateFormatter::parse

datefmt_parse

Analiza una cadena hacia un timestamp

## Descripción

Estilo orientado a objetos

```php
public IntlDateFormatter::parse(string $string, [int $offset]): int
```php

Estilo procedimental

```php
datefmt_parse(IntlDateFormatter $formatter, string $string, [int $offset]): int
```

Convierte `string` en un valor de tiempo, comenzando en `offset` y leyendo tantos caracteres como sea posible.

## Parámetros

`formatter`  
El recurso de formateador `IntlDateFormatter`.

`string`  
La cadena a convertir en tiempo.

`offset`  
La posición desde la cual comenzar el análisis en el valor `string`. Las posiciones comienzan en 0. Si no ocurre ningún error durante el análisis de `string`, `offset` contendrá -1, y de lo contrario, contendrá la posición en la cual el análisis terminó (y el error ocurrió). Esta variable contendrá la posición de fin si el análisis falla. Si `offset` \> `strlen($string)`, el análisis falla inmediatamente.

## Valores devueltos

El valor del timestamp analizado o `false` si el valor no pudo ser analizado.

## Ejemplos

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
echo 'El primer formato analizado es ' . $fmt->parse('Wednesday, December 20, 1989 4:00:00 PM PT');
$fmt = new IntlDateFormatter(
    'de-DE',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN
);
?>

   
```

Ejemplo con `datefmt_parse`

```php
<?php
$fmt = datefmt_create(
    'en_US',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN
);
echo 'El primer formato analizado es ' . datefmt_parse($fmt, 'Wednesday, December 20, 1989 4:00:00 PM PT');
$fmt = datefmt_create(
    'de-DE',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN
);
echo 'El segundo formato analizado es ' . datefmt_parse($fmt, 'Mittwoch, 20. Dezember 1989 16:00 Uhr GMT-08:00');
?>

   
```

El ejemplo anterior mostrará:

    El primer formato analizado es 630201600
    El segundo formato analizado es 630201600

      

## Véase también

`datefmt_create`, `datefmt_format`, `datefmt_localtime`, `datefmt_get_error_code`, `datefmt_get_error_message`
